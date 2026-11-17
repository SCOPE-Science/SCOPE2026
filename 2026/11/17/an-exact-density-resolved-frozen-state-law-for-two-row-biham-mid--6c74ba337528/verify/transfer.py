"""Exact weighted transfer verification for blocked BML configurations on a two-row cyclic grid."""
import itertools
import sympy as sp
u,v,z=sp.symbols('u v z')
states=[(a,b) for a,b in itertools.product('0EN',repeat=2) if (a,b) not in {('0','N'),('N','0')}]
assert len(states)==7
T=sp.zeros(7)
for i,a in enumerate(states):
    for j,b in enumerate(states):
        if all(a[r]!='E' or b[r]!='0' for r in (0,1)):
            T[i,j]=u**b.count('E')*v**b.count('N')
D=sp.Poly(sp.expand((sp.eye(7)-z*T).det()),z)
expected=1-(1+2*u+u*u+2*u*v+v*v)*z+(2*u+2*u*u+2*u*v+2*u*u*v+2*u*u*u)*z*z+(-u*u-2*u*u*u-u**4-2*u*u*v+u*u*v*v)*z**3+u**4*z**4
assert sp.expand(D.as_expr()-expected)==0
A=T.subs({u:1,v:1})
x=sp.symbols('x')
assert sp.factor(A.charpoly(x).as_expr())==x**3*(x-1)*(x**3-6*x**2+4*x-1)
counts=[int(sp.trace(A**n)) for n in range(1,13)]
assert counts==[7,29,148,777,4097,21620,114107,602257,3178732,16777469,88552141,467381700]
# Confirm all-East and all-North degeneracies from the weighted polynomial.
assert sp.expand(expected.subs(v,0)-(1-z)*(1-u*z)**2*(1-u*u*z))==0
assert sp.expand(expected.subs(u,0)-(1-(1+v*v)*z))==0
# The Perron root of x^3-6x^2+4x-1 is the unique real root > 5.
from fractions import Fraction
p=lambda xx:xx**3-6*xx**2+4*xx-1
assert p(Fraction(5278039,1000000))<0 and p(Fraction(5278040,1000000))>0
rho=float([complex(r).real for r in sp.nroots(x**3-6*x**2+4*x-1, n=30) if abs(complex(r).imag)<1e-20][0])
DD=sp.factor(expected.subs({u:sp.symbols('t'),v:sp.symbols('t')}))
t=sp.symbols('t')
z0=1/rho
fraction=(sp.diff(DD,t)/(2*z*sp.diff(DD,z))).subs({z:z0,t:1}).evalf(13)
assert abs(float(fraction)-0.847286700243823)<1e-10
print('states',states)
print('determinant',sp.factor(expected))
print('characteristic',sp.factor(A.charpoly(x).as_expr()))
print('frozen counts n=1..12',counts)
print('leading root between 5.278039 and 5.278040')
print('limiting occupied fraction',fraction)
print('all symbolic and numeric assertions passed')
