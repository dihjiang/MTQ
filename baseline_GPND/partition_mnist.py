from utils import mnist_reader
from utils.download import download
import random
import pickle

download(directory="mnist", url="http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz", extract_gz=True)
download(directory="mnist", url="http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz", extract_gz=True)
download(directory="mnist", url="http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz", extract_gz=True)
download(directory="mnist", url="http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz", extract_gz=True)

folds = 3

#Split mnist into 5 folds:
mnist = items_train = mnist_reader.Reader('mnist', train=True).items
items_test = mnist_reader.Reader('mnist', test=True).items 
class_bins = {}
items_valid = mnist[int(0.9*len(items_train)):]
random.shuffle(mnist)

# for x in mnist:
#     if x[0] not in class_bins:
#         class_bins[x[0]] = []
#     class_bins[x[0]].append(x)

# mnist_folds = [[] for _ in range(folds)]

# for _class, data in class_bins.items():
#     count = len(data)
#     print("Class %d count: %d" % (_class, count))

#     count_per_fold = count // folds

#     for i in range(folds):
#         mnist_folds[i] += data[i * count_per_fold: (i + 1) * count_per_fold]


# print("Folds sizes:")
# for i in range(len(mnist_folds)):
#     print(len(mnist_folds[i]))

#     output = open('data_fold_%d.pkl' % i, 'wb')
#     pickle.dump(mnist_folds[i], output)
#     output.close()

output = open('traindata.pkl' , 'wb')
pickle.dump(mnist, output)
output.close()
output = open('testdata.pkl' , 'wb')
pickle.dump(items_test, output)
output.close()
output = open('validdata.pkl', 'wb')
pickle.dump(items_test, output)
output.close()