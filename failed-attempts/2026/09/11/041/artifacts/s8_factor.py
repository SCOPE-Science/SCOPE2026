import sympy as sp
x=sp.Symbol('x')
f = x**6 - 3*x**5 + x**4 + 3*x**2 - x + 1
print("QQ-factor:", sp.factor(f))
print("QQ-roots:", sp.solve(f,x))
# mod-p factorization shapes (Frobenius cycle type info)
for p in [3,7,11,13,17,31]:
    F=sp.GF(p); fac=sp.factorpoly(sp.Poly(f,x,domain=F))
    print(p, fac)
