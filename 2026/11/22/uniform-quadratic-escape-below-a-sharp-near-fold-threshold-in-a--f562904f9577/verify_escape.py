#!/usr/bin/env python3
"""Exact checks for escape potential of a fixed-point-free quadratic map."""
import sympy as s
x,y,a,b,c,d=s.symbols('x y a b c d', real=True)
xp=x+y
yp=y-a*s.symbols('absy',nonnegative=True)-x*y+b*x**2-c*y**2+d
W=lambda X,Y: Y+(1+b)*X**2/2
k=(2+b)/4-c
Q=b*(x+y/2)**2+k*y**2-a*s.symbols('absy',nonnegative=True)+d
assert s.simplify(W(xp,yp)-W(x,y)-Q)==0
# At a hypothetical pair (X-z/2,z) -> (X+z/2,-z),
# the two return residuals differ by 2*z*(2-(1+b)*X).
X,z=s.symbols('X z',real=True)
G=lambda X,Y: Y-a*s.symbols('absv',nonnegative=True)-X*Y+b*X**2-c*Y**2+d
p=G(X-z/2,z).subs('absv',z)+z
m=G(X+z/2,-z).subs('absv',z)-z
assert s.simplify(p-m-2*z*(2-(1+b)*X))==0, s.factor(p-m)
K=d+4*b/(1+b)**2
cc=(2+b)/4-a*a/(4*d)
cf=(2+b)/4-a*a/(4*K)
assert s.simplify(cf-cc-a*a*b/(d*K*(1+b)**2))==0
print('Exact potential identity, mandatory period-two center, and threshold gap verified.')
for vals in [(s.Rational(1,100),s.Rational(1,10),s.Rational(1,10)),(s.Rational(1,3),s.Rational(2,3),s.Rational(3,2)),(s.Rational(1,5),s.Rational(1,4),s.Rational(2,5))]:
 av,bv,dv=vals
 C0=s.simplify(cc.subs({a:av,b:bv,d:dv})); Cf=s.simplify(cf.subs({a:av,b:bv,d:dv}))
 assert Cf>C0
 print('a,b,d=',vals,' escape c<=',C0,' first two-cycle c>=',Cf,' gap=',s.simplify(Cf-C0))
