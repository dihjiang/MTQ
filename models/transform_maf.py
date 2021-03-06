"""based on MAF."""

import torch.nn as nn

from models.base import BaseModule

import models.flow_maf_models as fnn


class TinvMAF(BaseModule):
    """
    Implements an sos-flow for 1-dimensional vectors.
    1-dimensional vectors arise from the encoding of images.

    Model: T-inverse , T-inverse(z) = s, where T-inverse is built by MAFflow

        Input: latent vector z
        Output: s, -log_jacob of T (i.e., logjab of T-inverse)
    """

    def __init__(self, num_blocks, input_size, hidden_size, use_bn= True):
        # type: (int, List[int], int) -> None
        """
        Implements an estimator for 1-dimensional vectors.
        1-dimensional vectors arise from the encoding of images.

        Model: T-inverse , T-inverse(z) = s, T-inverse is built by SoSflow
        Input: latent vector z
        Output: s, -log_jacob of T (i.e., logjab of T-inverse)
        """
        num_cond_inputs = None
        act = 'relu'
        self.name = 'MAF'
        self.input_size = input_size


        super(TinvMAF, self).__init__()

        modules = []
        if use_bn:
            for _ in range(num_blocks):
                modules += [
                fnn.MADE(input_size, hidden_size, act=act),
                fnn.BatchNormFlow(input_size),
                fnn.Reverse(input_size)
                ]
        else:
            for _ in range(num_blocks):
                modules+= [
                fnn.MADE(input_size, hidden_size, act=act),
                fnn.Reverse(input_size)
                ]

        model = fnn.FlowSequential(*modules)

        # intialize
        for module in model.modules():
            if isinstance(module, nn.Linear):
                nn.init.orthogonal_(module.weight)
                
                if hasattr(module, 'bias') and module.bias is not None:
                	module.bias.data.fill_(0)

        self.T_inverse = model


    def forward(self, z):
        # type: (torch.Tensor) -> torch.Tensor
        """
        Forward propagation.

        :param x: the batch of latent vectors.
        :return: the batch of tuples (s, q(s)) CPD estimates q(s).
        """
        h = z.view(-1, self.input_size)

        s, log_jacob_T_inv = self.T_inverse(h)

        return s, log_jacob_T_inv