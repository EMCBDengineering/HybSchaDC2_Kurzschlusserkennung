import numpy as np
import matplotlib.pyplot as plt


k = 2
n = 3.5

t = np.linspace(1.01, 3, 1000)

f = k / (t**n - 1)

plt.plot(t, f)
plt.show()