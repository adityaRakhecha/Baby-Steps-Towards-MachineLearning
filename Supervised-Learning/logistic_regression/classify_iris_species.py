#import required modules
import numpy as np
import cv2
from sklearn import datasets
from sklearn import model_selection
from sklearn import metrics
import matplotlib.pyplot as plt
%matplotlib inline

plt.style.use('ggplot')

#load dataset
iris = datasets.load_iris()

#to know dataset structure
#dir(iris)

#taking only two labels/class labels
idx = iris.target != 2
data = iris.data[idx].astype(np.float32)
target = iris.target[idx].astype(np.float32)

#plot the altered dataset
plt.scatter(data[:,0], data[:, 1], c=target,
           cmap=plt.cm.Paired, s=100)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
#see fig.1 at description

#splitting the dataset
X_train, X_test, y_train, y_test = model_selection.train_test_split(data, target, test_size=0.1, random_state=42)

#create classifier
lr = cv2.ml.LogisticRegression_create()

#train the classifier
lr.setTrainMethod(cv2.ml.LogisticRegression_MINI_BATCH)
lr.setMiniBatchSize(1)
lr.setIterations(100)
lr.train(X_train, cv2.ml.ROW_SAMPLE, y_train)
#will output True if the training was successful

#to see the calculated weights or thetas
#lr.get_learnt_thetas()

#check the accuracy of our training set
_, y_pred = lr.predict(X_train)
metrics.accuracy_score(y_train, y_pred)

#finally check the accuracy of our test set
_, y_pred = lr.predict(X_test)
metrics.accuracy_score(y_test, y_pred)

### to do - build the same model for all three class label and check it's accuracy ###

