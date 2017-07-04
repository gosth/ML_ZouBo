#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import preprocessing
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def iris_type(s):
    it = {'Iris-setosa' : 0, 'Iris-versicolor' : 1, 'Iris-virginica' : 2}
    return it[s]

if __name__ == "__main__":
    path = u'8.iris.data'
    data = np.loadtxt(path, dtype = float, delimiter = ',', converters = {4 : iris_type})
    print data
