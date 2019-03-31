# Novelty Detection Using SoSflow density estimator


### Content

* **flows.py**,**general_maf.py** - code for sosflow.

* **train.py** - code for training novelty dector.
* **test.py** - code for testing/run novelty dector.

### How to run

## For MAFLSA Experiments

Firstly, we use MAF[1] estimator to replace the estimator in LSA[2].

Metric: AUROC (keep updating other metrics)

All the experiments are described in run_mnist.sh and run_cifar10.sh.


[1] Papamakarios G, Pavlakou T, Murray I. Masked autoregressive flow for density estimation[C]//Advances in Neural Information Processing Systems. 2017: 2338-2347.

[2] Abati D, Porrello A, Calderara S, et al. Latent Space Autoregression for Novelty Detection[C]//International Conference on Computer Vision and Pattern Recognition. 2019. 

Results will be uploaded later




