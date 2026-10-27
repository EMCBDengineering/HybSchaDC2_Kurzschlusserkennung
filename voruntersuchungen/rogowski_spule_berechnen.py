from sympy import Eq, symbols, solve, pi, nsimplify, Rational
import sympy as sp

mu_0 = symbols("mu_0")

u, M, di_dt = symbols("u M di_dt")
equation_u = Eq(u, M * di_dt)

N, A, l_m, R_min, b = symbols("N A l_m R_min b")
equation_M = Eq(M, mu_0*l_m/(2 * pi) * sp.log((R_min + b)/R_min))


# parameters
values = {
    di_dt : 5 * 1/(10**(-6)), # A/s
    u : 2, # V
    N : 1, # 1
    mu_0 : 4 * pi * 10**(-7), # H/m
    R_min : Rational(1, 100), # m
    b : Rational(10, 100) # m
}

result = solve(
    [equation_u, equation_M],
    [M, l_m],
    dict=True
)

solutions = [
    sol[l_m].subs(values)
    for sol in result
]

print(result[0][l_m])

print([x.evalf(4) for x in solutions])