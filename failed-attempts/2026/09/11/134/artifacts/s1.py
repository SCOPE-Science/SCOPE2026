import sympy as sp
x,y,t=sp.symbols('x y t')
S=1/x+1/y+y+x*y
K=x*y*(1-t*S)
# collect in x
a=sp.expand(-t*y**2); b=sp.expand(y-t-t*y**2); c=sp.expand(-t*y)
Dx=sp.expand(b**2-4*a*c)
print("Dx(y)=",Dx)
print("Dx poly:",sp.Poly(Dx,y))
A=sp.expand(-t*x*(x+1)); B=sp.expand(x-t); C=sp.expand(-t*x)
Dy=sp.expand(B**2-4*A*C)
print("Dy(x)=",Dy)
print("Dy poly:",sp.Poly(Dy,x))
# discriminant of Dx w.r.t y as poly in t
Dxpoly=sp.Poly(Dx,y)
print("deg Dx:",Dxpoly.degree())
DyPoly=sp.Poly(Dy,x)
print("deg Dy:",DyPoly.degree())
dDx=Dxpoly.discriminant()
print("disc(Dx)=",sp.factor(dDx))
dDy=DyPoly.discriminant()
print("disc(Dy)=",sp.factor(dDy))
