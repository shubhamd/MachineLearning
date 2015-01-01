import matplotlib.pyplot as plt 
from sklearn import datasets 
from sklearn import svm 
digits = datasets.load_digits()
clf = svm.SVC(gamma=0.0001,C=100)
x,y=digits.data[:-3],digits.target[:-3]
clf.fit(x,y)
print('prediction : ',clf.predict(digits.data[-2]))
plt.imshow(digits.images[-2],cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()




