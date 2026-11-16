#!/usr/bin/env python3
"""Independent exact monomial-moment verification for cubic harmonic octant localization."""
import sympy as sp
x,y,z=sp.symbols('x y z', real=True)
r2=x*x+y*y+z*z
polys=[x*(5*x*x-3*r2),y*(5*y*y-3*r2),z*(5*z*z-3*r2),
       x*(y*y-z*z),y*(z*z-x*x),z*(x*x-y*y),x*y*z]

def integral_monom(a,b,c,octant):
    if not octant and any(v%2 for v in (a,b,c)): return sp.Integer(0)
    ratio=sp.gamma(sp.Rational(a+1,2))*sp.gamma(sp.Rational(b+1,2))*sp.gamma(sp.Rational(c+1,2))/sp.gamma(sp.Rational(a+b+c+3,2))
    return sp.simplify(ratio/4 if octant else 2*ratio)

def integral(p,octant):
    return sp.simplify(sum(coeff*integral_monom(*exp,octant) for exp,coeff in sp.Poly(sp.expand(p),x,y,z).terms()))

assert len(polys)==7
assert all(sp.simplify(sum(sp.diff(f,u,2) for u in (x,y,z)))==0 for f in polys)
G=sp.Matrix(7,7,lambda i,j:integral(polys[i]*polys[j],False))
H=sp.Matrix(7,7,lambda i,j:integral(polys[i]*polys[j],True))
assert G==sp.diag(*([16*sp.pi/7]*3+[16*sp.pi/105]*3+[4*sp.pi/105]))
assert sp.simplify(sp.trace(G.inv()*H)) == sp.Rational(7,8)
t=sp.symbols('t')
expected=(t-(sp.pi-3)/(8*sp.pi))\
 * (t**2-(sp.Rational(1,4)-sp.Rational(1,24)/sp.pi)*t+
    ((30*sp.pi-5)**2-6505)/(240*sp.pi)**2)\
 * (t**2-(sp.Rational(1,4)+sp.Rational(5,24)/sp.pi)*t+
    ((30*sp.pi+25)**2-4045)/(240*sp.pi)**2)**2
assert sp.simplify(sp.expand(G.inv().multiply(H).charpoly(t).as_expr()-expected))==0
spect=[(sp.pi-3)/(8*sp.pi),
       (30*sp.pi-5-sp.sqrt(6505))/(240*sp.pi),
       (30*sp.pi+25-sp.sqrt(4045))/(240*sp.pi),
       (30*sp.pi-5+sp.sqrt(6505))/(240*sp.pi),
       (30*sp.pi+25+sp.sqrt(4045))/(240*sp.pi)]
mult=[1,1,2,1,2]
assert all(sp.N(spect[i+1]-spect[i],30)>0 for i in range(4))
assert sum(mult)==7
assert sp.simplify(sum(l*m for l,m in zip(spect,mult))-sp.Rational(7,8))==0
# The alternating cubic spans the bottom eigenspace; check its eigenvector equation.
w=sp.Matrix([0,0,0,1,1,1,0])
assert all(sp.simplify(v)==0 for v in (H-spect[0]*G)*w)
print('EXACT_OCTANT_CUBIC_PASS 7 harmonic modes; 49 Gram entries; 5 eigenvalues')
