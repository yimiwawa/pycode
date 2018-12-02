#!-*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics

digits_train = pd.read_csv('optdigits.tra', header=None)
digits_test = pd.read_csv('optdigits.tes', header=None)

X_train = digits_train[np.arange(64)]
y_train = digits_train[64]

X_test = digits_test[np.arange(64)]
y_test = digits_test[64]

kmeans = KMeans(n_clusters=10)
kmeans.fit(X_train)

y_pred = kmeans.predict(X_test)

# 使用ARI进行性能评估
print metrics.adjusted_rand_score(y_test, y_pred)