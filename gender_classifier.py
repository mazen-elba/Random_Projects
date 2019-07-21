# dependencies
from sklearn import tree
from sklearn.svm import SVC
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# 1. create data and labels
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

# 2. use classifiers on default values for all hyperparameters
clf_tree = tree.DecisionTreeClassifier()
clf_svm = SVC(gamma="auto")
clf_perceptron = Perceptron(max_iter=1000, tol=1e-3)
clf_KNN = KNeighborsClassifier()

# 3. train models
clf_tree.fit(X, y)
clf_svm.fit(X, y)
clf_perceptron.fit(X, y)
clf_KNN.fit(X, y)

# 4. test models using same data
pred_tree = clf_tree.predict(X)
acc_tree = accuracy_score(y, pred_tree) * 100
print("Accuracy for DecisionTree: {}".format(acc_tree))

pred_svm = clf_svm.predict(X)
acc_svm = accuracy_score(y, pred_svm) * 100
print("Accuracy for SVM: {}".format(acc_svm))

pred_per = clf_perceptron.predict(X)
acc_per = accuracy_score(y, pred_per) * 100
print("Accuracy for Perceptron: {}".format(acc_per))

pred_KNN = clf_KNN.predict(X)
acc_KNN = accuracy_score(y, pred_KNN) * 100
print("Accuracy for KNN: {}".format(acc_KNN))

# 5. best classifer from SVM, Perceptron, KNN
index = np.argmax([acc_svm, acc_per, acc_KNN])
classifiers = { 0:"SVM", 1:"Perceptron", 2:"KNN" }
print("Best gender classifier is {}".format(classifiers[index]))