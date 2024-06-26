#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = pd.read_csv("bank2.dat", sep = "\s+", header=None)
n = len(x)

e = np.linalg.eig((n - 1) * np.cov(x.T)/n)
e1 = e[0]
x  = np.dot(np.array(x), e[1])


# In[13]:


fig, axes = plt.subplots(2, 2, figsize = (10, 10))
axes[0, 0].scatter(x[:100, 0], x[:100, 1], c = "w", edgecolor = "b")
axes[0, 0].scatter(x[100:, 0], x[100:, 1], c = "r", marker = "+")
axes[0, 0].set_title("First vs. Second PC")
axes[0, 0].set_xlabel("PC1")
axes[0, 0].set_ylabel("PC2")

axes[0, 1].scatter(x[:100, 1], x[:100, 2], c = "w", edgecolor = "b")
axes[0, 1].scatter(x[100:, 1], x[100:, 2], c = "r", marker = "+")
axes[0, 1].set_title("Second vs. Third PC")
axes[0, 1].set_xlabel("PC2")
axes[0, 1].set_ylabel("PC3")

axes[1, 0].scatter(x[:100, 0], x[:100, 2], c = "w", edgecolor = "b")
axes[1, 0].scatter(x[100:, 0], x[100:, 2], c = "r", marker = "+")
axes[1, 0].set_title("First vs. Third PC")
axes[1, 0].set_xlabel("PC1")
axes[1, 0].set_ylabel("PC3")

axes[1, 1].scatter(range(1, 7), e1, c = "w", edgecolors = "black")
axes[1, 1].set_title("Eigenvalues of S")
axes[1, 1].set_xlabel("Index")
axes[1, 1].set_ylabel("Lambda")

fig.tight_layout()

plt.savefig('MVApcabank-1_python.png', format='png', dpi=600, transparent=True)
plt.show()

