#!-*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 创建特征列表
column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of cell size',
                'Uniformity of cell shape', 'marginal ashesion',
                'single epithelial cell size', 'bare nuclei',
                'bland chromatin', 'normal nucleoli', 'mitoses', 'Class']

# 使用pandas读取数据
data = pd.read_csv('breast-cancer-wisconsin.data', names = column_names)

# 将缺失值（?）替换为标准缺失值表示
data = data.replace(to_replace='?', value=np.nan)

# 丢弃带有缺失值的数据
data = data.dropna(how='any')

# 输出data的数据量和维度
print data.shape

from sklearn.cross_validation import train_test_split

# 随机采样25%用于测试，75%用于构建训练集
X_train, X_test, y_train, y_test = train_test_split(data[column_names[1:10]],
                                                    data[column_names[10]],
                                                    test_size=0.25, random_state=33)

# 检查训练样本的数量和分布
print y_train.value_counts()
print y_test.value_counts()

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier

# 标准化数据
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

sgdc = SGDClassifier()

sgdc.fit(X_train, y_train)
sgdc_y_predict = sgdc.predict(X_test)

# 指标测评
from sklearn.metrics import classification_report

print "Accuracy of SGD classifier:", sgdc.score(X_test, y_test)
print classification_report(y_test, sgdc_y_predict, target_names=["Benign", "Malignant"])