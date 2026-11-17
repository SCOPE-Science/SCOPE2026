"""Exact rational finite checks for Gini instability of the Cesaro residual.
Analytical arguments for all dimensions are given in RESULT.md.
"""
from fractions import Fraction as Q
from random import Random

def H(n):
    return sum((Q(1,j) for j in range(1,n+1)),Q())

def G(v):
    return sum((abs(a-b) for i,a in enumerate(v) for b in v[i+1:]),Q(0))

def D(v):
    z=[];s=Q(0)
    for i,a in enumerate(v,1):
        s+=a;z.append(a-s/i)
    return z

def g3(n):
    return Q(2*(n-1),3)+(n+7)*(H(n)-H(3))-2*(n-3)

def F(n):
    return (n+7)*(H(n)-H(3))-Q(7*n-19,3)

assert F(5)==Q(1,15)
assert F(6)-F(5)==Q(17,60)
print('ANALYTIC_THRESHOLD_BASE_F5_1_OVER_15_AND_INCREMENT_17_OVER_60_PASS')

for n,want in [(2,Q(1,2)),(3,Q(5,6)),(4,Q(11,12))]:
    candidates=[]
    for mask in range(1,(1<<n)-1):
        x=[Q((mask>>i)&1) for i in range(n)];k=mask.bit_count()
        gain=G(D(x))/Q(k*(n-k))
        candidates.append(gain)
    assert max(candidates)==want,(n,max(candidates),want)
    print('EXHAUSTIVE_SMALL_DIMENSION',n,'PASS',str(want),'cuts',len(candidates))

for n in range(5,101):
    x=[Q(i==3) for i in range(1,n+1)]
    assert G(D(x))==g3(n),(n,G(D(x)),g3(n))
    assert F(n)>0
    assert g3(n)>Q(n-1)
    assert F(n+1)-F(n)==H(n)-H(3)-Q(4,3)+Q(7,n+1)
    assert (F(n+2)-F(n+1))-(F(n+1)-F(n))==Q(n-5,(n+1)*(n+2))
print('EXACT_THIRD_COORDINATE_WITNESS_AND_INCREASING_DEFICIT_PASS_N5_TO100')

# Finite evidence for the general column-mass inequality; its proof is separate.
rng=Random(431267)
checks=0
for n in range(2,9):
    for _ in range(20):
        p=[]
        for i in range(n):
            a=[rng.randrange(1,15) for j in range(n)]
            p.append([Q(t,sum(a)) for t in a])
        M=max(sum((p[i][j] for i in range(n)),Q()) for j in range(n))
        for mask in range(1,(1<<n)-1):
            x=[Q((mask>>i)&1) for i in range(n)]
            y=[sum((a*b for a,b in zip(row,x)),Q()) for row in p]
            assert G(y)<=M*G(x)
            checks+=1
print('RANDOM_STOCHASTIC_COLUMN_MASS_BOUND_PASS',checks)

for n in range(5,101):
    low=g3(n)/Q(n-1)
    up=1+H(n)
    assert 1<low<=up
print('ASYMPTOTIC_BRACKETING_FORMULAS_PASS_N5_TO100')
print('ALL_CESARO_RESIDUAL_GINI_CHECKS_PASS')
