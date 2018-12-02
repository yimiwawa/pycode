#!-*- coding:utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


# 创建特征列表
column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of cell size',
                'Uniformity of cell shape', 'marginal ashesion',
                'single epithelial cell size', 'bare nuclei',
                'bland chromatin', 'normal nucleoli', 'mitoses', 'Class']

data = pd.read_csv('breast-cancer-wisconsin.data', names = column_names)
data = data.replace(to_replace='?', value=np.nan)
data = data.dropna(how='any')

X_train, X_test, y_train, y_test = train_test_split(data[column_names[1:10]],
                                                    data[column_names[10]],
                                                    test_size=0.25, random_state=33)

# 检查训练样本的数量和分布
print y_train.value_counts()
print y_test.value_counts()

# 标准化数据
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

lr = LogisticRegression()

lr.fit(X_train, y_train)
lr_y_predict = lr.predict(X_test)

# 指标测评
print "Accuracy of LR classifier:", lr.score(X_test, y_test)
print classification_report(y_test, lr_y_predict, target_names=["Benign", "Malignant"])
