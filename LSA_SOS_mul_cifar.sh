python test.py --autoencoder AAE --dataset cifar10 --batch_size 256 --code_length 64 --epochs 1000 --lr 0.02 --select 1


# python test.py  --autoencoder LSA --estimator SOS  --dataset cifar10 --batch_size 256 --code_length 64    --epochs 1000    --lr 0.00001 --num_blocks 1 --hidden_size 2048 --MulObj  --select 1 --PreTrained  --premodel LSA --NoTrain --checkpoint 200 
# 0.4281

# python test.py  --autoencoder LSA --estimator SOS  --dataset cifar10 --batch_size 256 --code_length 64    --epochs 1000    --lr 0.00001 --num_blocks 1 --hidden_size 2048 --MulObj  --select 0 --PreTrained  --premodel LSA 