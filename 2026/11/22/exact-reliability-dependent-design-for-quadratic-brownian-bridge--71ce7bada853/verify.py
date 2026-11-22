"""Exact and supplementary checks for two Bernoulli-erased bridge-energy observations.

Requires Python 3 and SymPy; NumPy is used for randomized supplemental tests.
"""
from __future__ import annotations
import sympy as sp
import numpy as np

x, y, p, a, d, h, s, z = sp.symbols('x y p a d h s z', real=True)

def cell(left, right):
    length = right-left
    return (left*(1-right)*length**3/sp.Integer(3)
            + length**4/sp.Integer(9) -4*length**5/sp.Integer(45))

# Reconstruct the nonstandard local covariance-trace coefficients by integration.
U,V=sp.symbols('U V',positive=True)
C_upper=U*(1-V)
C_lower=V*(1-U)
def integrate_square(f):
    return (sp.integrate(sp.integrate(C_upper*f,(V,U,1)),(U,0,1))+
            sp.integrate(sp.integrate(C_lower*f,(U,V,1)),(V,0,1)))
F00=sp.factor(integrate_square((1-U)*(1-V)))
F01=sp.factor(integrate_square((1-U)*V))
C2trace=sp.integrate(sp.integrate(2*C_upper**2,(V,U,1)),(U,0,1))
assert (F00,F01,C2trace)==(sp.Rational(1,45),sp.Rational(7,360),sp.Rational(1,90))
left,right=sp.symbols('left right')
ll=right-left
Kaa=left*(1-left); Kbb=right*(1-right); Kab=left*(1-right)
trace_cell=ll**4/45+4*ll**3*(F00*(Kaa+Kbb)+2*F01*Kab)
assert sp.simplify(trace_cell-cell(left,right))==0

R0 = cell(0,1)
R1 = lambda t: sp.expand(cell(0,t)+cell(t,1))
R2 = sp.expand(cell(0,x)+cell(x,y)+cell(y,1))
R = sp.expand((1-p)**2*R0+p*(1-p)*(R1(x)+R1(y))+p**2*R2)
assert R0 == sp.Rational(1,45)
assert sp.simplify(R1(x)-(1-10*x**2*(1-x)**2)/45)==0
assert sp.simplify(R2.subs(y,x)-R1(x))==0
assert sp.simplify(R2.subs(x,0)-R1(y))==0

# Symmetric midpoint displacement a and half-separation d, x=1/2-a-d, y=1/2-a+d.
newR=sp.expand(R.subs({x:sp.Rational(1,2)-a-d,y:sp.Rational(1,2)-a+d}))
centerR=sp.expand(newR.subs(a,0))
C0=2-p-24*d**2+p*(12*d**2-8*d**3)
C2=8*d*p+2*p-4
assert sp.simplify(newR-centerR-p*a**2*(C0+C2*a**2)/9)==0
assert sp.simplify(sp.diff(centerR,d)+p*(2*d-1)*((24*p+16)*d**2+(8-6*p)*d-p)/18)==0

root=(3*p+sp.sqrt(33*p**2-8*p+16)-4)/(8*(3*p+2))
assert sp.simplify(root.subs(p,sp.Rational(1,2))-sp.Rational(1,14))==0
assert sp.simplify(root.subs(p,1)-(sp.sqrt(41)-1)/40)==0
assert sp.simplify(sp.diff(centerR,d).subs(d,root))==0
assert sp.simplify(centerR.subs({d:sp.Rational(1,14),p:sp.Rational(1,2)})-sp.Rational(697,61740))==0
assert sp.simplify(centerR.subs({d:0,p:sp.Rational(1,2)})-sp.Rational(17,1440))==0

# For d >= 1/4, evaluate derivative after s=4d-1, a=(1-s)*sqrt(z)/4.
D=sp.factor(sp.diff(newR,d)*18/p)
Dsub=sp.expand(D.subs({a:a*(1-s)/4,d:(1+s)/4})).subs(a**4,z**2).subs(a**2,z)
D0=sp.factor(Dsub.subs(p,0))
D1=sp.factor(Dsub.subs(p,1))
assert sp.simplify(D0-(1-s**2)*(3+s-3*(1-s)*z)/2)==0
assert sp.simplify(D1.subs(z,1)-(1-s**2)*(s**2+18*s+1)/8)==0
assert sp.simplify(sp.diff(D1,z).subs(z,1)+(1-s)**2*(s**2+22*s+13)/16)==0
assert sp.simplify(sp.diff(D1,z,2)-(1-s)**4/8)==0
# Since D1 is convex in z and D1'(1)<=0, it decreases throughout [0,1].

# For d <= 1/4, C2<=0 and the minimum of C0+C2*a^2 is at |a|=1/2-d.
edge=sp.expand(C0+C2*(sp.Rational(1,2)-d)**2)
assert sp.simplify(edge.subs(p,0)-(1+4*d-28*d**2))==0
assert sp.simplify(edge.subs(p,1)-(1+8*d-44*d**2)/2)==0

rng=np.random.default_rng(4203)
fn=sp.lambdify((x,y,p), R,'numpy')
cr=sp.lambdify((d,p),centerR,'numpy')
for prob in [0.001,0.05,0.1,0.25,0.5,0.8,1.0]:
    optimum=float(root.subs(p,prob))
    best=float(cr(optimum,prob))
    for _ in range(2000):
        u,v=np.sort(rng.uniform(0,1,2))
        assert fn(u,v,prob)>=best-1e-13
    assert cr(0,prob)>best

print('PASS: exact risk algebra, boundary, optimizer and derivative certificates; 14000 randomized pairs.')
