#!/usr/bin/env pythpn
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessiong import StandardScaler
from sklearn.pipeline import Pipeline

def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[s]
