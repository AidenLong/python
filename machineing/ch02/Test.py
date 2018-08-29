import kNN
import matplotlib.pyplot as plt
from numpy import *

gorup, labels = kNN.createDataSet()
print(gorup)
print(labels)

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')
print(datingDataMat)
print(datingLabels)

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
plt.show()

normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
print(normMat)
