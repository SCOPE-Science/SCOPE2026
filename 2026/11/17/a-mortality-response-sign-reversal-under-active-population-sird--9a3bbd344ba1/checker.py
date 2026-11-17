"""Reproducible checks for high-mortality active-denominator SIRD asymptotics.
Python 3; dependencies: sympy, mpmath. All tests below run without network access.
"""
import sympy as sp
import mpmath as mp

s,r,L,E=sp.symbols('s r L E',positive=True)
a=r*L
b=r*r*L+r*(1-1/s)
x=s*(1-a*E+(a*a/sp.Integer(2)-b)*E**2)
D=sp.expand((1-E+E**2)*(1-x))
c1=sp.simplify(D.coeff(E,1))
c2=sp.simplify(D.coeff(E,2))
assert sp.simplify(c1-(s*r*L-(1-s)))==0
assert sp.simplify(c2.subs(r,(1-s)/(s*L))+(1-s)**2/(2*s))==0
# Classical fixed-population incidence has first-order logarithmic loss r(1-s)*E.
x_f=s*(1-r*(1-s)*E)
D_f=sp.expand((1-E)*(1-x_f))
assert sp.simplify(D_f.coeff(E,1)-(1-s)*(s*r-1))==0
mp.mp.dps=55

def solve(t,si,rr,active=True):
    t=mp.mpf(t); si=mp.mpf(si); rr=mp.mpf(rr)
    u=mp.mpf(0)
    for _ in range(2000):
        z=rr/t*mp.log((1+t)/(1+t*si*mp.exp(-u))) if active else rr/(1+t)*(1-si*mp.exp(-u))
        if abs(z-u)<mp.mpf('1e-48'):
            u=z; break
        u=z
    else: raise AssertionError('fixed point failed to converge')
    assert abs(u-(rr/t*mp.log((1+t)/(1+t*si*mp.exp(-u))) if active else rr/(1+t)*(1-si*mp.exp(-u))))<mp.mpf('1e-45')
    return t/(1+t)*(1-si*mp.exp(-u))

si=mp.mpf(1)/2; rr=mp.mpf(3)/2; seed=1-si
ca=si*rr*mp.log(1/si)-seed
cf=seed*(si*rr-1)
assert ca>0 and cf<0
for t in (100,1000,10000,100000):
    da=solve(t,si,rr,True)
    df=solve(t,si,rr,False)
    assert da>seed>df
    assert abs(t*(da-seed)-ca)<mp.mpf('5')/t
    assert abs(t*(df-seed)-cf)<mp.mpf('5')/t
# At the sharp active threshold, first-order vanishes and second order is negative.
crit=seed/(si*mp.log(1/si))
for t in (1000,10000):
    dc=solve(t,si,crit,True)
    second=-(1-si)**2/(2*si)
    assert abs(t*t*(dc-seed)-second)<mp.mpf('5')/t
print('PASS symbolic first/second-order expansions, equality boundary, and 12 numerical checks')
