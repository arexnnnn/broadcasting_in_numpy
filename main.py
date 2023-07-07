# Broadcasting in numpy

import numpy as np

a = np.random.randint(1, 10, (2,1))
b = np.random.randint(1, 10, (2,4))

# 2 rules:
# shape should be the same, start from right
# if it has one then no problem
print(a)
print(b)
print(a+b)