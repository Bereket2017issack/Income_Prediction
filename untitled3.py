# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10sL4iG0_0a87K8qnTqD0ac1hccTbBZRf
"""

from matplotlib.colors import ListedColormap
X_set, Y_set = X_train, y_train

X1, X2 = np.meshgrid(np.arange(start = X_set.min()-1, stop = X_set.max()+1, step=0.01),
                    np.arange(start = X_set.min()-1, stop = X_set.max()+1, step=0.01))

plt.contourf(X1, X2, claddifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
            alpha = 0.75, cmap = ListedColormap(('red', 'green')))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
  plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
             c = ListedColormap(('red', 'green'))(i), label = j)
  
plt.title('Logistic Regression (Training set)')
plt.xlabel("allvalues")
plt.ylabel("Salary")
plt.legend()
plt.show()