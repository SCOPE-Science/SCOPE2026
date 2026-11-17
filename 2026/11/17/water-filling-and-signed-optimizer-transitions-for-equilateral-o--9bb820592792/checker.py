"""Finite exact and independent LP checks of equilateral one-point extension minimax."""
from fractions import Fraction as F
from itertools import combinations
import random
import math

def phi(w,i):
    return (abs(1-w[i])+sum(abs(x) for j,x in enumerate(w) if j!=i))/2

def optimizer(R):
    lo=F(0); hi=F(2, min(R))
    def mass(z): return sum(max(F(0),1-z*r) for r in R)
    assert mass(lo)>1 and mass(hi)<=1
    # Exact active-set roots, not binary approximation
    candidates=[]
    for k in range(1,len(R)+1):
        for I in combinations(range(len(R)),k):
            z=F(k-1,sum(R[i] for i in I))
            if z<=0: continue
            if mass(z)==1:
                candidates.append(z)
    z=min(candidates)
    w=tuple(max(F(0),1-z*r) for r in R)
    assert sum(w)==1
    assert max(phi(w,i)/R[i] for i in range(len(R)))==z
    return z,w

def lp_check(R,z):
    from scipy.optimize import linprog
    n=len(R)
    # All nonempty subsets encode 1-Lipschitz 0/1 potentials on equilateral X.
    A=[]; B=[]
    for i in range(n):
        for mask in range(1,1<<n):
            row=[-(1 if mask>>j&1 else 0) for j in range(n)]+[-float(R[i])]
            A.append(row); B.append(-float(bool(mask>>i&1)))
    o=linprog([0]*n+[1],A_ub=A,b_ub=B,A_eq=[[1]*n+[0]],b_eq=[1],bounds=[(None,None)]*n+[(0,None)],method='highs')
    assert o.success,(R,o.message)
    assert abs(o.fun-float(z))<2e-8,(R,z,o.fun)

random.seed(23723)
Rsets = [(F(1,2),F(1,2),F(1,2),F(3,2)), (F(1,2),F(1,2),F(3,2),F(3,2)), (F(3,5),F(3,5),F(3,2),F(3,2)), (F(1,2),F(3,5),F(4,5),F(9,10)),(F(1,1),)*5]
for n in range(2,7):
    for _ in range(12):
        # Construct admissible with R_i>=1/2; individual max diff <=1
        R=tuple(F(random.randint(5,16),10) for i in range(n))
        if max(R)-min(R)>1: continue
        Rsets.append(R)
for R in Rsets:
    z,w=optimizer(R)
    lp_check(R,z)
    assert all(w[i]>=0 for i in range(len(R)))
    assert sum(max(F(0),1-z*r) for r in R)==1
    for _ in range(12):
        w0=[F(random.randint(-8,12),10) for i in range(len(R)-1)]
        w0.append(1-sum(w0))
        if any(x<0 for x in w0):
            t=sum(-x for x in w0 if x<0)
            v=[max(F(0),x)/(1+t) for x in w0]
            assert all(phi(v,i)<phi(w0,i) for i in range(len(R)))

z,w=optimizer((F(1,2),F(1,2),F(1,2),F(3,2)))
assert z==F(4,3) and w==(F(1,3),)*3+(F(0),)
z,w=optimizer((F(1,2),F(1,2),F(3,2),F(3,2)))
assert z==1 and w==(F(1,2),F(1,2),F(0),F(0))
z,w=optimizer((F(3,5),F(3,5),F(3,2),F(3,2)))
assert z<1
v=(F(1,2),F(1,2),F(-1,20),F(1,20))
assert sum(v)==1 and max(phi(v,i)/r for i,r in enumerate((F(3,5),F(3,5),F(3,2),F(3,2))))<=1
print('EQUILATERAL_NONUNIFORM_ONE_POINT_EXACT_AND_INDEPENDENT_LP_PASS profiles=%d'%(len(Rsets)))
print('THREE_PHASE_EXAMPLES_AND_NEGATIVE_COEFFICIENT_WITNESS_PASS')
