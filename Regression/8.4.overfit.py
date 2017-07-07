#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
import matplotlib as mpl


if __name__ == "__main__":
    np.random.seed(0)
    N = 9
    x = np.linspace(0, 6, N) + np.random.randn(N)
    x = np.sort(x)
    y = x ** 2 - 4 * x -3 + np.random.randn(N)
    x.shape = -1, 1
    y.shape = -1, 1

    model_1 =
