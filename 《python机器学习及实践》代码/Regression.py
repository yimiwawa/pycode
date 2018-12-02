#！-*- coding:utf-8 -*-

import numpy as np
from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

boston = load_boston()

X = boston.data
y = boston.target

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    random_state=33, test_size=0.25)

# 分析回归目标值的差异
print "The max target value is ", np.max(y)
print "The min target value is ", np.min(y)
print "The average target value is ", np.mean(y)

# 对特征和目标值进行标准化处理
ss_X = StandardScaler()
ss_y = StandardScaler()
X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)
y_train = ss_y.fit_transform(y_train)
y_test = ss_y.transform(y_test)

# 使用LinearRegression预测
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor

def regression(method):
    method.fit(X_train, y_train)
    y_predict = method.predict(X_test)

    print "The value of default measurement is ", method.score(X_test, y_test)
    print "The value of R-squared is ", r2_score(y_test, y_predict)
    print "The value of MSE is ", mean_squared_error(
        ss_y.inverse_transform(y_test),
        ss_y.inverse_transform(y_predict)
    )
    print "The value of MAE is ", mean_absolute_error(
        ss_y.inverse_transform(y_test),
        ss_y.inverse_transform(y_predict)
    )

lr = LinearRegression()
# regression(lr)

sgdr = SGDRegressor()
# regression(sgdr)

# 使用三种核函数配置的SVM进行训练
linear_svr = SVR(kernel="linear")
poly_svr = SVR(kernel="poly")
rbf_svr = SVR(kernel="rbf")
# regression(linear_svr)
# regression(poly_svr)
# regression(rbf_svr)

# 使用KNN的平均回归和距离加权回归两种预测方式
uni_knr = KNeighborsRegressor(weights="uniform")
dis_knr = KNeighborsRegressor(weights="distance")
# regression(uni_knr)
# regression(dis_knr)

# 使用决策树回归
dtr = DecisionTreeRegressor()
# regression(dtr)

# 使用三种集成回归模型，随机森林，极端随机森林，提升树
rfr = RandomForestRegressor()
etr = ExtraTreesRegressor()
gbr = GradientBoostingRegressor()
regression(rfr)
regression(etr)
regression(gbr)