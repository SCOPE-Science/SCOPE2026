"""Finite exact and high-precision checks of critical periodic Blaschke relaxation.
Run: python verify.py
"""
from fractions import Fraction as F
from itertools import permutations
import math
import sympy as sp
from mpmath import mp

u,q=sp.symbols('u q',positive=True)
# Cayley transform of B_a with a=(1-q)/(1+q).
a=(1-q)/(1+q)
z=(1-u)/(1+u)
B=((z+a)/(1+a*z))**2
W=sp.factor((1-B)/(1+B))
assert sp.simplify(W-2*q*u/(1+q*q*u*u))==0
X=sp.symbols('X',positive=True)
assert sp.simplify(X*(1+q*q/X)**2-(X+2*q*q+q**4/X))==0

def coefficients(lambdas):
    assert math.prod(lambdas)==1
    L=F(1); cs=[]
    for lam in lambdas:
        qq=lam/2
        cs.append((qq*L)**2)
        L*=lam
    assert L==1
    C=sum(cs,F(0)); D=sum((c*c for c in cs),F(0))
    return cs,C,D

cases=[([F(2),F(1,2)],F(5,4),F(17,16),F(17,40)),
       ([F(2),F(1),F(1,2)],F(9,4),F(33,16),F(11,24)),
       ([F(2),F(1,2),F(1)],F(3,2),F(9,8),F(3,8)),
       ([F(3,2),F(4,3),F(1,2)],None,None,None)]
for ls,C0,D0,L0 in cases:
    cs,C,D=coefficients(ls)
    if C0 is not None:
        assert (C,D,D/(2*C))==(C0,D0,L0)

mp.dps=75
runs=0
# The critical block coefficient is one quarter of the sum of squared partial products.
for ls,_,_,_ in cases:
    cs,C,D=coefficients(ls)
    L=F(1); prefixes=[]
    for lam in ls:
        L*=lam; prefixes.append(L)
    assert C==sum((x*x for x in prefixes),F(0))/4

for vals in [[F(2),F(1),F(1,2)],[F(2),F(3,2),F(2,3),F(1,2)],
             [F(3,2),F(4,3),F(1,2)]]:
    candidate=[coefficients(list(perm))[1] for perm in set(permutations(vals))]
    assert min(candidate)==coefficients(sorted(vals))[1]
    assert max(candidate)==coefficients(sorted(vals,reverse=True))[1]

for ls,_,_,_ in cases:
    cs,C,D=coefficients(ls)
    m=len(ls)
    coef=mp.mpf(D.numerator)/D.denominator /(2*(mp.mpf(C.numerator)/C.denominator))
    slope=2*(mp.mpf(C.numerator)/C.denominator)
    for x0 in [mp.mpf('0'),mp.mpf('0.31'),mp.mpf('0.8')]:
        w=(1-x0)/(1+x0)
        zrec=1/(w*w)
        qlist=[mp.mpf((l/2).numerator)/(l/2).denominator for l in ls]
        llist=[mp.mpf(l.numerator)/l.denominator for l in ls]
        csmp=[mp.mpf(c.numerator)/c.denominator for c in cs]
        LL=[mp.mpf(1)]
        for lam in llist[:-1]:LL.append(LL[-1]*lam)
        checkpoints=[]
        for k in range(1,20001):
            for j in range(m):
                # Exact conjugacy recurrence and inverse-square recurrence, from the same initial state.
                w=2*qlist[j]*w/(1+qlist[j]**2*w**2)
                zrec=zrec+2*csmp[j]+csmp[j]**2/zrec
            assert abs(zrec-1/(w*w))<mp.mpf('1e-55')*max(zrec,1)
            if k in [200,1000,5000,20000]:
                checkpoints.append((k,zrec-slope*k-coef*mp.log(k)))
        # After subtraction of exact linear and logarithmic terms the remainder has finite limit.
        assert abs(checkpoints[-1][1]-checkpoints[-2][1])<mp.mpf('0.005')
        assert abs((1/w**2)/20000-slope)<mp.mpf('0.01')
        runs+=1
print('VERIFY_OK symbolic_cayley=2 exact_coefficient_cases=4 exhaustive_ordering_multisets=3 high_precision_runs=',runs,'max_sweeps=20000 precision_digits=',mp.dps)
