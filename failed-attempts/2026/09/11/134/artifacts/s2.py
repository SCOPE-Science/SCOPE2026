import sympy as sp
x,y,t=sp.symbols('x y t')
S=1/x+1/y+y+x*y
K=x*y*(1-t*S)
K=sp.expand(K)
print("K=",K)
dKdx=sp.expand(sp.diff(K,x))
dKdy=sp.expand(sp.diff(K,y))
print("dKdx=",dKdx)
print("dKdy=",dKdy)
# solve dKdx=0 for x
# dKdx = y-t-t*y**2-2*t*y**2*x
solx=sp.solve(dKdx,x)
print("x sol:",solx)
xsol=solx[0]
# Dx
Dx=sp.expand((y-t-t*y**2)**2-4*(-t*y**2)*(-t*y))
print("Dx check")
# plug xsol into dKdy numerator
expr=sp.simplify(dKdy.subs(x,xsol))
num=sp.simplify(sp.together(expr).as_numer_denom()[0])
print("num dKdy subst =",sp.expand(num))
print("degree in y:",sp.Poly(num,y).degree())
# resultant of Dx and num w.r.t y
Dxpoly=sp.Poly(Dx,y)
Npoly=sp.Poly(num,y)
print("Dx deg",Dxpoly.degree(),"N deg",Npoly.degree())
res=sp.resultant(Dxpoly,Npoly,y)
print("res =",sp.factor(res))
