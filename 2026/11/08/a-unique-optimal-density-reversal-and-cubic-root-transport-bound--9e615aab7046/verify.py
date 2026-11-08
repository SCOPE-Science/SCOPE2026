#!/usr/bin/env python3
"""Exact polynomial identities and numerical tests for tandem maximal current.
Requires Python 3.10+, SymPy 1.12+; optional mpmath bundled with SymPy.
No network or external data is needed.
"""
from math import log, sqrt, isclose
import sympy as S
from sympy import Rational

s, q = S.symbols('s q')
R = s*(q*s+1)/(q*s*s+2*s+1)
J = q*s*s*((q+1)*s+2)/((s+1)*(q*s+1)*(q*s*s+2*s+1))
P = q*q*(q+1)*s**5 + 4*q*q*s**4 - 2*(q*q+1)*s**3 - (2*q*q+8*q+6)*s**2 - (5*q+9)*s - 4
D = (s+1)**2*(q*s+1)**2*(q*s*s+2*s+1)**2
assert S.factor(S.diff(J,s) + q*s*P/D) == 0
assert S.factor(S.diff(R,s) - (q*s*s+2*q*s+1)/(q*s*s+2*s+1)**2) == 0
# Verify the exact parametrization and transport input against the source equations.
assert S.factor(q*(1-R)*s*s+(1-2*R)*s-R)==0
assert S.factor(J-q*R*s*(s+2+q*s)/((s+1)*(1+q*s)**2))==0
z=s*(s+1)/(1+q*s)
ratio=(q-1)*s/((s+1)*(q*s+1))
assert S.factor(ratio-(q-1)*z/(s+1)**2)==0
N = S.cancel(S.diff(R,q)*S.diff(P,s)-S.diff(R,s)*S.diff(P,q))
H = S.cancel(N*(q*s*s+2*s+1)**2/s)
assert H.is_polynomial(s,q)
Q = 7*q**4+12*q**3+94*q**2+20*q-53
assert S.factor(S.resultant(P,H,s) - 16*q**6*(q-1)**12*Q) == 0
assert S.factor(P.subs(q,1) - 2*(s-2)*(s+1)**4)==0
assert S.simplify(N.subs({q:1,s:2})/S.diff(P,s).subs({q:1,s:2}) - Rational(1,81)) == 0

t = S.symbols('t',positive=True)
F = S.factor((q**3*P.subs(s,t/q)).cancel())
assert S.factor(F - (t**5-2*t**3+q*(t**5+4*t**4-6*t**2)+q*q*(-2*t**3-8*t**2-9*t)+q**3*(-2*t**2-5*t-4)))==0
T0=S.sqrt(2)
T1=S.simplify(-S.diff(F,q).subs({q:0,t:T0})/S.diff(F,t).subs({q:0,t:T0}))
Rsmall=S.cancel(R.subs(s,t/q))
Jsmall=S.cancel(J.subs(s,t/q))
assert S.simplify(Rsmall.subs({q:0,t:T0}) - 1/S.sqrt(2))==0
assert S.simplify(S.diff(Rsmall,q).subs({q:0,t:T0})+S.diff(Rsmall,t).subs({q:0,t:T0})*T1+S.Rational(1,4))==0
assert S.simplify(Jsmall.subs({q:0,t:T0})-(3-2*S.sqrt(2)))==0
assert S.simplify(S.diff(Jsmall,q).subs({q:0,t:T0})+S.diff(Jsmall,t).subs({q:0,t:T0})*T1-(S.Rational(9,2)-3*S.sqrt(2)))==0

e,u=S.symbols('e u',positive=True)
Flarg=S.factor(e**4*P.subs({q:e**-3,s:e*u}))
assert S.simplify(S.limit(Flarg,e,0,dir="+") - u*u*(u**3-2))==0
assert S.diff(Flarg,u).subs({e:0,u:2**S.Rational(1,3)})!=0
assert S.simplify(S.limit(S.cancel(((1-R)/e).subs({s:e*u,q:e**-3})),e,0,dir='+')-u**-2)==0
assert S.simplify(S.limit(S.cancel(((1-J)/e).subs({s:e*u,q:e**-3})),e,0,dir='+')-(u+u**-2))==0
assert S.simplify(S.limit(S.cancel(((1-ratio)/e).subs({s:e*u,q:e**-3})),e,0,dir='+')-u)==0

# Solve the unique positive root by monotone bisection without relying on nroots
p_num=S.lambdify((s,q),P,'math')
Q_num=S.lambdify(q,Q,'math')
def positive_root(qv):
    lo, hi = 0.0, 1.0
    while p_num(hi,qv) <= 0:hi*=2.0
    for k in range(170):
        mid=(lo+hi)/2
        if p_num(mid,qv)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def profile(qv):
    sv=positive_root(qv)
    rv=sv*(qv*sv+1)/(qv*sv*sv+2*sv+1)
    jv=qv*sv*sv*((qv+1)*sv+2)/((sv+1)*(qv*sv+1)*(qv*sv*sv+2*sv+1))
    ratio=(qv-1)*sv/((sv+1)*(qv*sv+1))
    xi=(-1/log(abs(ratio))) if qv!=1 else 0.0
    return sv,rv,jv,xi
lo,hi=0.0,1.0
for k in range(200):
    mid=(lo+hi)/2
    if Q_num(mid)>0:hi=mid
    else:lo=mid
qcrit=(lo+hi)/2
scrit,rcrit,jcrit,xcrit=profile(qcrit)
assert abs(qcrit-0.623631289268772)<1e-13
assert abs(rcrit-0.663810878206103)<1e-13
for x in (0.01,0.1,0.25,0.5,0.623631289268772,0.8,1,1.3,3,10,100):
    _,rv,jv,_=profile(x)
    assert rv>=rcrit-1e-12
    assert 0<rv<1 and 0<jv<1
for qv in (1e6,1e9):
    sv,rv,jv,xi=profile(qv)
    e=qv**(-1/3)
    assert abs(sv/e-2**(1/3))<0.02
    assert abs((1-rv)/e-2**(-2/3))<0.004
    assert abs((1-jv)/e-3*2**(-2/3))<0.04
    assert abs(xi*e-2**(-1/3))<0.005
for qv in (1e-5,1e-6):
    sv,rv,jv,xi=profile(qv)
    assert abs(rv-1/sqrt(2)+qv/4)<1e-9
    assert abs(jv-(3-2*sqrt(2)))<1e-5
    assert abs(xi-1/log(1+sqrt(2)))<1e-4
# Independent exact finite-ring balance checks for the inherited Gibbs premise.
from fractions import Fraction

def finite_ring_balance(n, recovery):
    weights = [recovery ** sum(((b >> i) & 1) * ((b >> ((i+1) % n)) & 1) for i in range(n)) for b in range(1 << n)]
    outgoing = [Fraction(0) for _ in weights]
    incoming = [Fraction(0) for _ in weights]
    for b in range(1 << n):
        for i in range(n):
            triple = tuple((b >> ((i+j) % n)) & 1 for j in range(3))
            if triple == (1, 1, 0):
                new = b ^ (1 << ((i+1) % n)) ^ (1 << ((i+2) % n))
                rate = Fraction(1)
            elif triple == (1, 0, 1):
                new = b ^ (1 << (i % n)) ^ (1 << ((i+1) % n))
                rate = recovery
            else:
                continue
            outgoing[b] += weights[b] * rate
            incoming[new] += weights[b] * rate
    assert incoming == outgoing

for n in range(5, 10):
    for recovery in (Fraction(1, 2), Fraction(3, 4), Fraction(2)):
        finite_ring_balance(n, recovery)
print('EXACT_GIBBS_BALANCE_15_FINITE_RING_CASES_OK')
print('EXACT_POLYNOMIAL_AND_RESULTANT_IDENTITIES_OK')
print('NUMERIC_BOUNDARIES_AND_NONMONOTONE_MINIMUM_OK')
print('qcrit:',format(qcrit,'.15g'),'rho_min:',format(rcrit,'.15g'))
print('q=1:',profile(1))
