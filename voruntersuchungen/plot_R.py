import sympy as sp
import matplotlib.pyplot as plt
from sympy import symbols, Rational, plot, Eq, pi
from sympy.plotting import plot3d


M, mu_0, l_m, R, R_mm, b, k = symbols("M mu_0 l_m R R_mm b k")
M_1 = mu_0*l_m/(2 * pi) * sp.log(1 + b/R)

values = {
    mu_0 : 4 * pi * Rational(1, 10**7), # H/m
    # l_m : Rational(23, 10**2), # m
    b/R: k
}


fig = plt.figure()
ax = [
    fig.add_subplot(1, 2, 1, projection="3d"),
    fig.add_subplot(1, 2, 2),
]


x_range = (k, 0, 1)
y_range = (l_m, 0, 0.5)
p1 = plot3d(M_1.subs(values) * 1e9, 
        x_range,
        y_range, 
        label = ["M [nH]"],
        fig=fig, ax=ax[0], show=False
        )

k = sp.exp((M * 2 * pi) / (mu_0 * l_m)) - 1
p2 = plot(k.subs({M: Rational(2, 10**9), mu_0: 4 * pi * Rational(1, 10**7)}),
        (l_m, 0, 0.2),
        label = ["k [1]"],
        fig=fig, ax=ax[1], show=False
        )


p1._backend.process_series()
p2._backend.process_series()


ax[0].set_xlabel("k in [1]", loc="right", fontsize=11)
ax[0].set_ylabel("l_m in [m]")
ax[0].set_zlabel("M in [nH]")

ax[1].set_ylim(0, 10)
ax[1].set_ylabel("")
ax[1].legend(loc="best")
ax[1].set_xlabel("l_m in [m]", loc="right", fontsize=11)



plt.show()