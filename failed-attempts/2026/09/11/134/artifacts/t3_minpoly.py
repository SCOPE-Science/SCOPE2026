import sympy as sp
u=sp.symbols('u')
# u^4-u-1=0, v=1/u^2
# wW=1/u, wNE=1/u, wS=u^2, wN=1/u^2
# Z = 2/u + u^2 + 1/u^2
Z = 2/u + u**2 + 1/u**2
Exx = (2/u)/Z
Exy = (1/u)/Z
Eyy = (u**2 + 1/u**2 + 1/u)/Z
r2 = sp.simplify(Exy**2/(Exx*Eyy))
print("r^2 =", sp.simplify(r2))
# simplify in u
r2s = sp.together(r2)
print(r2s)
num,den = r2s.as_numer_denom()
print("num:", sp.expand(num))
print("den:", sp.expand(den))
# resultant to get minpoly of R=r^2
R=sp.symbols('R')
p1 = sp.Poly(sp.expand(num - R*den), u)
print("deg in u:", p1.degree())
res = sp.resultant(p1, sp.Poly(u**4-u-1, u), u)
print("res(R)=", sp.factor(res))
