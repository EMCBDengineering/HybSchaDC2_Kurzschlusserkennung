import numpy as np
import matplotlib.pyplot as plt

U = 1500
R = 10
L = 100e-3
C = 1e-6
t = np.linspace(0, 0.1, 1000)
a = R/(2*L)
b = np.emath.sqrt(a**2 - 1/(L*C))


i = U/L * 1/(2*b) * (np.exp(-t*(a - b)) - np.exp(-t*(a + b)))
di_dt = np.diff(i, 1, -1)
plt.plot(np.real(i), label="i(t) [A]")
plt.plot(np.real(di_dt), label="di_dt (t) [A/s]")
plt.xlabel("Zeit t [s]")
plt.legend()
plt.show()