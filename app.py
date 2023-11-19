import numpy as np
import torch as th

print(1 + 2)

a = 1 + 2
print(a)

b = 2 + 3
print(b)

c = a + b
print(c)

d = b + c
print(d)

print(np.zeros(10))
print(th.ones(10))
print(th.cuda.is_available())