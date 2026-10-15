import numpy as np
from scipy.constants import mu_0
from sympy import Eq, symbols, solve

u, M, di_dt = symbols("u M di_dt")
equation_u = Eq(u, M * di_dt)

N, A, l_m = symbols("N A l_m")
equation_M = Eq(M, mu_0*N*A/l_m)

r_m = symbols("r_m")
equation_l_m = Eq(l_m, 2 * np.pi * r_m)

r_A = symbols("r_A")
equation_A = Eq(A, np.pi*(r_A**2))

# parameters
values = {
    di_dt : 10/(10**(-6)), # A/s
    u : 5, # V
    r_m : 5 * 10**(-2), # m
    N : 200
}

result = solve(
    [equation_u, equation_M, equation_l_m, equation_A],
    [M, A, l_m, r_A],
    dict=True
)

solutions = [
    sol[r_A].subs(values)
    for sol in result
]

print("r_A =", [round(float(r) * 100, 2) for r in solutions], "cm")