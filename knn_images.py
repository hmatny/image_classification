import pprint
import numpy as np
import pandas as pd

pp = pprint.PrettyPrinter(indent=4)

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict



if __name__ == "__main__":
    file = 'cifar-10-batches-py/data_batch_1'
    imgs = unpickle(file)
    print(imgs.keys())
    #training phase
        #need to store images as features with label
    #classification phase
        #calculate distance of test image w.r.t all images stored



 