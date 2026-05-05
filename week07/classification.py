from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784', as_frame=False)

print(mnist.keys())

X, y = mnist.data, mnist.target
print(X)
print(X.shape)
print(y)
print(y.shape)

import matplotlib.pyplot