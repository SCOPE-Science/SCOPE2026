import sympy as sp
x=sp.Symbol('x')
f = x**6 - 3*x**5 + x**4 + 3*x**2 - x + 1
print("QQ-factor:", sp.factor(f))
for p in [3,7,11,13,17,31]:
    fac=sp.factor_list(sp.Poly(f,x,domain=sp.GF(p)))
    print(p, fac)
