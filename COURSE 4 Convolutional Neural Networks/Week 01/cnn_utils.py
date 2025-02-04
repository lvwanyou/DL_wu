import math
import numpy as np
import h5py
import matplotlib.pyplot as plt
from scipy import ndimage
import scipy

def load_dataset():
    train_dataset = h5py.File('datasets/train_signs.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('datasets/test_signs.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


def random_mini_batches(X, Y, mini_batch_size = 64, seed = 0):
    """
    Creates a list of random minibatches from (X, Y)
    
    Arguments:
    X -- input data, of shape (input size, number of examples) (m, Hi, Wi, Ci)
    Y -- true "label" vector (containing 0 if cat, 1 if non-cat), of shape (1, number of examples) (m, n_y)
    mini_batch_size - size of the mini-batches, integer
    seed -- this is only for the purpose of grading, so that you're "random minibatches are the same as ours.
    
    Returns:
    mini_batches -- list of synchronous (mini_batch_X, mini_batch_Y)
    """
    
    m = X.shape[0]                  # number of training examples
    mini_batches = []
    np.random.seed(seed)
    
    # Step 1: Shuffle (X, Y)
    permutation = list(np.random.permutation(m))
    shuffled_X = X[permutation,:,:,:]
    shuffled_Y = Y[permutation,:]

    # Step 2: Partition (shuffled_X, shuffled_Y). Minus the end case.
    num_complete_minibatches = math.floor(m/mini_batch_size) # number of mini batches of size mini_batch_size in your partitionning
    for k in range(0, num_complete_minibatches):
        mini_batch_X = shuffled_X[k * mini_batch_size : k * mini_batch_size + mini_batch_size,:,:,:]
        mini_batch_Y = shuffled_Y[k * mini_batch_size : k * mini_batch_size + mini_batch_size,:]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)
    
    # Handling the end case (last mini-batch < mini_batch_size)
    if m % mini_batch_size != 0:
        mini_batch_X = shuffled_X[num_complete_minibatches * mini_batch_size : m,:,:,:]
        mini_batch_Y = shuffled_Y[num_complete_minibatches * mini_batch_size : m,:]
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)
    
    return mini_batches


def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y


def data_preprocess(X_train_orig, Y_train_orig, X_test_orig, Y_test_orig):
    X_train_orig = X_train_orig / 255
    X_test_orig = X_test_orig /255
    Y_train_orig = convert_to_one_hot(Y_train_orig, 6).T
    Y_test_orig = convert_to_one_hot(Y_test_orig, 6).T
    return X_train_orig,Y_train_orig,X_test_orig,Y_test_orig


def load_image():

    """"  find ep from training set
    X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = load_dataset()  # classes show how many gestures
    X_train_orig, Y_train_orig, X_test_orig, Y_test_orig = data_preprocess(X_train_orig, Y_train_orig, X_test_orig,
                                                                           Y_test_orig)

    # show the source image from the training set
    index = 100
    pre_image = X_train_orig[index].reshape((1, 64, 64, 3))
    plt.imshow(X_train_orig[index])
    plt.show()
    """

    my_image_test1 = "thumbs_three.jpeg"
    ## END CODE HERE ##

    # We preprocess your image to fit your algorithm.
    fname = "images/" + my_image_test1
    image = np.array(ndimage.imread(fname, flatten=False))
    plt.imshow(image)
    plt.show()

    pre_image = scipy.misc.imresize(image, size=(64, 64)).reshape((1, 64, 64, 3))

    return pre_image
