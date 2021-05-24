# In this assignment students have to transform iris data into 3 dimensions and plot a 3d chart
# with transformed dimensions and color each data point with specific class.

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris()
X_reduced = PCA(n_components=3).fit_transform(iris.data)
Y=iris.target

fig=plt.figure(1,figsize=(8,6))
ax=Axes3D(fig,elev=-150,azim=110)

ax.scatter(X_reduced[:,0],X_reduced[:,1],X_reduced[:,2],c=Y,cmap=plt.cm.rainbow_r)

ax.set_title("First 3 PCA Directions")
ax.set_xlabel("1st eigenvector")
ax.set_ylabel("2nd eigenvector")
ax.set_zlabel("3rd eigenvector")
plt.show()
