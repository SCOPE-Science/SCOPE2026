#!/usr/bin/env python3
"""Reproduce algebra and stationary-current numerical comparisons."""
from fractions import Fraction
from itertools import combinations
import math
import sympy as sp
from scipy.optimize import brentq

s, r, q = sp.symbols('s r q', positive=True)
R = s*(1+q*s)/(1+2*s+q*s*s)
J = q*R*s*(s+2+q*s)/((1+s)*(1+q*s)**2)
Q = (r-(1-2*r)*s)/((1-r)*s*s)
C = r-(1-2*r)*s+(1-r)*s*s
A = r-(1-2*r)*s
B = r+(1-r)*s
V = (1-r)*s*s*A*B/(r*(1+s)**2*C)
P = (r-1)**3*s**4-(r-1)*(3*r-1)*(5*r-3)*s**3-r*(5*r*r-11*r+4)*s*s+r*r*(5*r-1)*s+2*r**3
assert sp.cancel(R.subs(q,Q)-r)==0
assert sp.cancel(J.subs(q,Q)/(1+Q)-V)==0
assert sp.cancel(sp.diff(V,s)-(1-r)*s*P/(r*(1+s)**3*C**2))==0
assert sp.expand(P.subs(r,sp.Rational(1,2))+(s+1)*(s**3-s-2)/8)==0

T = sp.symbols('T',positive=True)
transformed = sp.cancel((1-2*r)**4*(1+T)**4*P.subs(s,r*T/((1-2*r)*(1+T)))/r**3)
assert sp.factor(sp.Poly(transformed,T).coeff_monomial(T**4))==r*(r-1)**2*(3*r-2)
assert sp.factor(sp.Poly(transformed,T).coeff_monomial(T**3))==-r*r*(r-1)*(2*r-1)
assert sp.factor(sp.Poly(transformed,T).coeff_monomial(T**2))==(2*r-1)**2*(13*r*r-16*r+5)
assert sp.factor(sp.Poly(transformed,T).coeff_monomial(T))==(2*r-1)**3*(11*r-7)
assert sp.factor(sp.Poly(transformed,T).coeff_monomial(1))==2*(2*r-1)**4

pfunc=sp.lambdify((s,r),P,'math')
vfunc=sp.lambdify((s,r),V,'math')

def optimal(rho):
    if rho<.5:
        upper=rho/(1-2*rho)
        hi=upper*(1-1e-12)
        root=brentq(lambda z:pfunc(z,rho),1e-14,hi,xtol=1e-14)
    else:
        hi=1.0
        while pfunc(hi,rho)>0:
            hi*=2
        root=brentq(lambda z:pfunc(z,rho),1e-14,hi,xtol=1e-14)
    qopt=(rho-(1-2*rho)*root)/((1-rho)*root**2)
    return root,qopt,float(vfunc(root,rho))

for rho in (.0001,.001,.01,.1,.2,.4,.5,.55,.6,2/3,.75,.9,.99,.999):
    s0,q0,j0=optimal(rho)
    for fac in (.01,.1,.5,2,10,100):
        qq=q0*fac
        ss=2*rho/(1-2*rho+math.sqrt((1-2*rho)**2+4*qq*(1-rho)*rho))
        Jb=qq*rho*ss*(ss+2+qq*ss)/((1+ss)*(1+qq*ss)**2*(1+qq))
        assert j0>Jb*(1+1e-12), (rho,fac,j0,Jb)
    print('rho',format(rho,'.7g'),'qopt',format(q0,'.12g'),'max/B',format(j0,'.12g'))

# Two singular regimes: normalized asymptotic coefficients.
for rr in (1e-4,1e-5,1e-6):
    _,qq,jj=optimal(rr)
    assert abs(qq*math.sqrt(rr)/math.sqrt(2/5)-1)<.015
    assert abs(jj/(2*rr**2)-1)<.06
for rr in (.99,.999,.9999):
    _,qq,jj=optimal(rr)
    assert abs(qq/((1-rr)/4)-1)<.07
    assert abs(jj/(1-rr)-1)<.07

# Independent finite-ring canonical computation at the Bernoulli parameter q=1.
# Canonical stationary uniform measure: E[110] = E[101] = K(K-1)(N-K)/[N(N-1)(N-2)].
for N,K in ((8,4),(10,6),(14,7),(18,9)):
    total=0;cnt=0
    for occupied in combinations(range(N),K):
        occ=set(occupied)
        moves=sum(1 for i in range(N) if i in occ and ((i+1)%N) in occ and ((i+2)%N) not in occ)
        moves+=sum(1 for i in range(N) if i in occ and ((i+1)%N) not in occ and ((i+2)%N) in occ)
        total+=moves;cnt+=1
    exact=Fraction(total,N*cnt)
    predicted=Fraction(2*K*(K-1)*(N-K),N*(N-1)*(N-2))
    assert exact==predicted,(N,K,exact,predicted)
print('All symbolic identities, transformed coefficient checks, parameter tests and finite-ring counts passed.')
