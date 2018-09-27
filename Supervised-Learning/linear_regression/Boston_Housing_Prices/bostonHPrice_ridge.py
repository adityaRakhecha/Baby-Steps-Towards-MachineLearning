import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn import model_selection as modsel
from sklearn import linear_model
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('ggplot')

boston = datasets.load_boston()

ridgereg = linear_model.Ridge()
X_train, X_test, y_train, y_test = modsel.train_test_split(
    boston.data, boston.target, test_size=0.1, random_state=42)
    
#ridgereg.fit(X_train, y_train)

#metrics.mean_squared_error(y_train, ridgereg.predict(X_train))
#ridgereg.score(X_train, y_train)
#y_pred = ridgereg.predict(X_test)
#metrics.mean_squared_error(y_test, y_pred)

plt.figure(figsize=(15,9))
plt.plot(y_test, linewidth=3, label='ground truth')
plt.plot(y_pred, linewidth=3, label='predicted')
plt.legend(loc='best')
plt.xlabel('test data points')
plt.ylabel('target value')
#will plot fig.5 (see at description)

plt.plot(y_test, y_pred, 'o')
plt.plot([-10, 60], [-10, 60], 'k--')
plt.axis([-10, 60, -10, 60])
plt.xlabel('ground truth')
plt.ylabel('predicted')
scorestr = r'R$^2$ = %.3f' % ridgereg.score(X_test, y_test)
errstr = 'MSE = %.3f' % metrics.mean_squared_error(y_test, y_pred)
plt.text(-5, 50, scorestr, fontsize=12)
plt.text(-5, 45, errstr, fontsize=12)

#will plot fig.6 (see description)
