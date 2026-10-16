from sympy import Eq, symbols, solve, pi, nsimplify


mu_0 = symbols("mu_0")

u, M, di_dt = symbols("u M di_dt")
equation_u = Eq(u, M * di_dt)

N, A, l_m = symbols("N A l_m")
equation_M = Eq(M, mu_0*N*A/l_m)

r_m = symbols("r_m")
equation_l_m = Eq(l_m, 2 * pi * r_m)

r_A = symbols("r_A")
equation_A = Eq(A, pi*(r_A**2))

# parameters
values = {
    di_dt : 10/(10**(-6)), # A/s
    u : 5, # V
    r_m : 5 * 10**(-2), # m
    N : 300, # 1
    mu_0 : 4 * pi * 10**(-7) # H/m
}

result = solve(
    [equation_u, equation_M, equation_l_m],
    [M, A, l_m],
    dict=True
)

solutions = [
    sol[A].subs(values)
    for sol in result
]

print([nsimplify(x) for x in solutions])