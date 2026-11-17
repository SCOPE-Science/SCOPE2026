#!/usr/bin/env python3
"""Independent exact-arithmetic diagnostics for sparse-sign first-chaos sixth moments.

Requires Python 3.9+ and SymPy. No external data or network access.
These checks corroborate, but do not replace, the universal proof in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial, sqrt
import sympy as S


def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total-first, parts-1):
                yield (first,)+tail


def independent_sixth(x, t):
    """Multinomial enumeration of all independent nonzero even moments."""
    ans=Q(0)
    for m in compositions(3,len(x)):
        c=Q(factorial(6))
        for k in m:
            c/=factorial(2*k)
        for v,k in zip(x,m):
            if k:
                c*=v**k*t**(k-1)
        ans+=c
    return ans


def claimed_sixth(x,t):
    q=sum(x)
    return 15*q**3+15*(t-3)*q*sum(z*z for z in x)+(t*t-15*t+30)*sum(z**3 for z in x)


def F(k,t):
    return 15+15*(t-3)/Q(k)+(t*t-15*t+30)/Q(k*k)


checks=0
for n in range(1,7):
    xs=[Q(i+1,(n*(n+1))//2) for i in range(n)]
    for t in [Q(1),Q(3,2),Q(2),Q(3),Q(7,2),Q(4),Q(5),Q(11,2),Q(20)]:
        assert independent_sixth(xs,t)==claimed_sixth(xs,t)
        checks+=1
print('INDEPENDENT_MULTINOMIAL_IDENTITY_CASES_PASSED',checks)

# Symbolic pair identity, without using the candidate extremal formula.
u,v,T=S.symbols('u v T', real=True)
A=15*(T-3); B=T*T-15*T+30
phi=lambda w:A*w*w+B*w*w*w
assert S.simplify(phi(u)+phi(v)-phi(u+v)-u*v*(-2*A-3*B*(u+v)))==0
assert S.factor(-2*A-3*B)==-3*T*(T-5)
r=S.factor(-B/A)
assert S.simplify(r-((12-T)/15+S.Rational(2,5)/(T-3)))==0
assert S.simplify(S.diff(r,T)+S.Rational(1,15)+S.Rational(2,5)/(T-3)**2)==0
print('PAIR_SMOOTHING_AND_PHASE_DERIVATIVE_IDENTITIES_PASSED')

# Exact positive root and uniqueness of each support crossing.
prev=6.
roots=[]
for k in range(1,101):
    poly=S.expand(A*k*(k+1)+B*(2*k+1))
    a,b,c=[S.expand(poly).coeff(T,j) for j in (2,1,0)]
    tau=S.simplify((-b+S.sqrt(b*b-4*a*c))/(2*a))
    tv=float(tau.evalf(18))
    assert 3<tv<prev and abs(float(poly.subs(T,tau).evalf()))<1e-8
    assert S.simplify(F(k,S.Rational(7,2))-F(k+1,S.Rational(7,2))) == S.simplify((A*k*(k+1)+B*(2*k+1)).subs(T,S.Rational(7,2))/(k*k*(k+1)*(k+1)))
    roots.append(tv); prev=tv
assert roots[0]==5.0
print('ORDERED_STAIRCASE_THRESHOLDS_PASSED',len(roots))

# Full rational grids of squared coefficients: an independent finite stress test.
finite=0
for n in (2,3,4):
    for t in (Q(1),Q(2),Q(3),Q(13,4),Q(7,2),Q(4),Q(5),Q(6)):
        best=max(F(k,t) for k in range(1,n+1))
        for nums in compositions(12,n):
            x=tuple(Q(z,12) for z in nums)
            got=independent_sixth(x,t)
            assert got<=best,(n,t,nums,got,best)
            finite+=1
print('RATIONAL_SIMPLEX_GRID_INEQUALITIES_PASSED',finite)

# Flat two-coordinate edge exactly at t=5, and not at either neighboring value.
for i in range(1,24):
    x=(Q(i,24),Q(24-i,24))
    assert independent_sixth(x,Q(5))==Q(25)
    assert independent_sixth(x,Q(4))<=Q(19)
    assert independent_sixth(x,Q(6))<=Q(36)
print('SPECIAL_FLAT_TWO_SUPPORT_FAMILY_PASSED',23)
print('ALL_SPARSE_SIXTH_MOMENT_DIAGNOSTICS_PASSED')
