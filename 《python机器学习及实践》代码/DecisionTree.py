#！-*- coding:utf-8 -*-

import pandas as pd

titanic = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
# print titanic.info()

X = titanic[['pclass', 'age', 'sex']]
y = titanic['survived']

X['age'].fillna(X['age'].mean(), inplace=True)

from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

vec = DictVectorizer(sparse=False)
X_train = vec.fit_transform(X_train.to_dict(orient='record'))
X_test = vec.transform(X_test.to_dict(orient='record'))

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

y_predict = dtc.predict(X_test)

print 'The accuracy of decision tree is ', dtc.score(X_test, y_test)
print classification_report(y_predict, y_test, target_names=['died', 'survived'])

# 使用Random Forest集成模型训练以及预测分析
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)

rfc_y_predict = rfc.predict(X_test)
print 'The Accuracy of Random Forest is ', rfc.score(X_test, y_test)
print classification_report(rfc_y_predict, y_test)

# 使用GDT训练以及预测分析
from sklearn.ensemble import GradientBoostingClassifier

gbc = GradientBoostingClassifier()
gbc.fit(X_train, y_train)

gbc_y_predict = gbc.predict(X_test)
print 'The Accuray of Gradient Boosting Tree is ', gbc.score(X_test, y_test)
print classification_report(gbc_y_predict, y_test)