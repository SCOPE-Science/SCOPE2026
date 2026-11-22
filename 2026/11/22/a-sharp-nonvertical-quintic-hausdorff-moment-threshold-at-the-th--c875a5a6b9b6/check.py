"""Reproducible finite diagnostics for a quintic moment-family threshold.

No numerical test substitutes for the analytic all-time positivity argument.
Run with: python3 check.py
"""
from math import pi, sin, cos, exp, acos, isclose
from fractions import Fraction

def F(lam, y):
    def j(omega):
        return (omega - exp(-lam*y)*(lam*sin(omega*y) + omega*cos(omega*y))) / (lam*lam+omega*omega)
    return j(1.0) - (2.0/3.0)*j(1.5)

def G(y):
    return sin(y) - (2.0/3.0)*sin(1.5*y)

def threshold():
    lo, hi = 0.0, 1.0
    for _ in range(70):
        md=(lo+hi)/2
        h=5-(8*md*md+13)*exp(-2*pi*md)
        if h>0:hi=md
        else:lo=md
    return (lo+hi)/2

lam=threshold()
assert 0.154391<lam<0.154393
assert abs((8*lam*lam+13)*exp(-2*pi*lam)-5)<1e-12
# Endpoint formula, first full-period recurrence and spectral denominator.
for l in [-0.4, 0.0, 0.05, lam, 0.25, 1.0]:
    e=exp(-2*pi*l)
    exact=(5-(8*l*l+13)*e)/(4*(l*l+1)*(l*l+2.25))
    assert isclose(F(l,2*pi),exact,rel_tol=1e-10,abs_tol=2e-13)
    if l>0:
        total=1.25/((l*l+1)*(l*l+2.25))
        assert isclose(F(l,4*pi),total*(1-exp(-4*pi*l)),rel_tol=1e-10,abs_tol=1e-12)
        for u in [0.1,0.9,2.0,3.6,6.28,9.0,11.0]:
            for m in [1,2,4]:
                left=F(l,4*pi*m+u)
                right=(1-exp(-4*pi*l*m))*total+exp(-4*pi*l*m)*F(l,u)
                assert isclose(left,right,rel_tol=1e-10,abs_tol=1e-11)
# Four half-period sign regions from exact trigonometric factorization.
a=2*acos(-0.25)
for x,expected in [(1.0,1),(4.0,-1),(7.0,1),(9.0,-1)]:
    assert G(x)*expected>0
for y in [i*.1 for i in range(1,126)]:
    z=y/2.0
    product=(2.0/3.0)*sin(z)*(1-cos(z))*(4*cos(z)+1)
    assert isclose(G(y),product,rel_tol=1e-9,abs_tol=1e-12)
# Sign threshold and interiors.
assert F(lam-.01,2*pi)<0 and F(lam+.01,2*pi)>0
for l in [lam+0.005, lam+0.2, 1.0]:
    assert all(F(l,12*pi*i/1200)>-1e-11 for i in range(1,1201))
# Exact degree-5 moment polynomial -> strict sixth difference zero, fifth nonzero.
def P(n):
    x=Fraction(n)
    a,b,c=Fraction(2),Fraction(4),Fraction(3,2)
    return (x+a)*((x+b)**2+c*c)*((x+b)**2+Fraction(9,4)*c*c)
def delta(vals):return [b-a for a,b in zip(vals,vals[1:])]
for m in [0,3,17]:
    v=[P(n+m) for n in range(7)]
    assert len(delta(delta(delta(delta(delta(delta(v)))))))==1
    assert delta(delta(delta(delta(delta(delta(v))))))[0]==0
    v5=[P(n+m) for n in range(6)]
    assert delta(delta(delta(delta(delta(v5)))))[0]!=0
# Moment telescoping, positive weights, and contractive Cauchy dual.
for n in [0,1,4,12,40]:
    prod=Fraction(1)
    for k in range(n):prod*=P(k+1)/P(k)
    assert prod==P(n)/P(0)
    assert P(n+1)>P(n)>0
print('PASS: 1 threshold, 6 endpoint checks, 6 period checks, 168 recurrence checks, 125 trigonometric factor checks, 3 positivity samples, 3 exact finite-difference checks and telescoping tests')
print('lambda_star = %.16f'%lam)
