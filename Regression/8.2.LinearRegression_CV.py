#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV

if __name__ == "__main__":
    data = pd.read_csv('8.Advertising.csv')
    x = data[['TV', 'Radio', 'Newspaper']]
    y = data['Sales']
    print x
    print y

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
    model = Lasso()
    alpha_can = np.logspace(-3, 2, 10)
    lasso_model = GridSearchCV(model, param_grid=('alpha':
