#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    path = '8.Advertising.csv'
    data = pd.read_csv(path)
    x = data[['TV', 'Radio', 'Newspaper']]
    y = data['Sales']
    print x
    print y
    plt.plot(data['TV'], y, 'ro', label = 'TV')
    plt.legend(loc= 'lower right')
    plt.grid()
    plt.show()
    
