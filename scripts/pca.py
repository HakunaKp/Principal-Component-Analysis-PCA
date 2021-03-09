import numpy as np
from sklearn.decomposition import PCA


X = np.array([[0,1,2],[2,1,3],[3,2,5]])
reduced_dim = 1

pca= PCA(n_components=reduced_dim)

X_modified = pca.fit_transform(X)


print("Original X: \n",X)
print("Reduced Dim X: \n",X_modified)

