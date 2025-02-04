import numpy as np
import random
from cffi.backend_ctypes import xrange
from sklearn.datasets.samples_generator import make_regression
from scipy import stats
import pandas as pd


def gradient_descent_2(alpha, x, y, numIterations):
    m = x.shape[0]  # number of samples(rows)
    theta = np.ones(2)
    x_transpose = x.transpose()
    for iter in xrange(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        J = np.sum(loss ** 2) / (2 * m)  # cost
        print("iter %s | J: %.3f" % (iter, J))
        gradient = np.dot(x_transpose, loss) / m
        theta = theta - alpha * gradient  # update
    return theta


if __name__ == '__main__':

    # x, y = make_regression(n_samples=100, n_features=1, n_informative=1,
    #                     random_state=0, noise=35)
    x = []
    y = []
    # lol = []
    for a in pd.read_csv('Data/Train/Train_Combine.csv', chunksize=656):
        df = pd.DataFrame(data=a)
        for index, row in df.iterrows():
            lol = []
            lol.append(row['T'])
            y.append(row['PM 2.5'])
            x.append(lol)

    # print ("lol",len(lol))
    # print("lol", lol)
    # print (len(y))
    # print ("Before XXX: ",x)
    m, n = np.shape(x)

    x = np.c_[np.ones(m), x]  # insert column
    # print("XXXXXXXX:",x)
    # print("AAAAAAA:",a)
    alpha = 0.01  # learning rate
    theta = gradient_descent_2(alpha, x, y, 1000)
    lol = []

    for a in pd.read_csv('Data/Test/Test_Combine.csv', chunksize=656):
        df = pd.DataFrame(data=a)
        for index, row in df.iterrows():
            lol.append(row['T'])

    X2 = np.array(lol)
    # print("X2: ", X2)
    for i in xrange(X2.shape[0]):
        print(np.dot(X2[i], theta))
