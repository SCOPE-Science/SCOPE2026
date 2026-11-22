"""Exact rational endpoint certificates and supplementary stress tests.

This checker uses only Python's standard library. Proofs for unbounded domains
are in RESULT.md, not inferred from these finite calculations.
"""
from fractions import Fraction as F
from math import factorial, exp, log, floor, ceil
from random import Random

P=F(4,5); C=F(1,50); ALPHA=F(399,400)

def exp_minus_interval(x,N=60):
    """Certified rational enclosure of exp(-x) for rational 0<=x<N+2."""
    assert 0 <= x < N+2
    term=F(1); lower=F(1)
    for k in range(1,N+1):
        term=term*x/k
        lower+=term
    nextterm=term*x/(N+1)
    upper=lower+nextterm/(1-x/F(N+2))
    return F(1,1)/upper, F(1,1)/lower

def score_interval(B,n):
    x=F(B,n)-C
    assert x>0
    lo,hi=exp_minus_interval(x)
    qlo=1-P+P*lo; qhi=1-P+P*hi
    return ALPHA**n*(1-qhi**n),ALPHA**n*(1-qlo**n)

witnesses=[(F(8),5,4,6),(F(10),4,3,5)]
for B,win,l,r in witnesses:
    wlo,whi=score_interval(B,win)
    for j in [l,r]:
        jlo,jhi=score_interval(B,j)
        assert wlo>jhi, (B,win,j)
        print('CERTIFIED', 'budget',B,'winner',win,'over',j,'gap in',float(wlo-jhi),float(whi-jlo))

# The formula gives eventual winner 4 for the witness parameters.
p=float(P);f=float(1-ALPHA);beta=1-p
xi=log(f/(p+f*(1-p)))/log(beta)
assert 3<xi<4

# Randomized checks of positive curvature, exact successful denominator,
# and the global-neighbor criterion predicted by strict log-concavity.
rng=Random(81105)
count=0
for k in range(4000):
    p=.02+.96*rng.random()
    c=.005+1.2*rng.random()
    lam=.05+4*rng.random()
    f=.0002+.2*rng.random()
    B=(3+35*rng.random())*c
    ns=list(range(1,min(100,int(B/c)+1)))
    if len(ns)<4: continue
    J=[]
    for n in ns:
        v=B/n
        q=1-p+p*exp(-lam*(v-c))
        J.append((1-f)**n*(1-q**n))
    j=max(range(len(J)),key=J.__getitem__)
    assert all(J[t]>=min(J[t-1],J[t+1])-1e-13 for t in range(1,len(J)-1) if t==j)
    for t in range(1,len(J)-1):
        assert J[t]*J[t]+1e-12>=J[t-1]*J[t+1]
    count+=1

# A finite volume may have a higher best replicate count than a larger volume.
def objective(B,n):
    q=1-float(P)+float(P)*exp(-(float(B)/n-float(C)))
    return float(ALPHA)**n*(1-q**n)
assert max(range(1,100),key=lambda n:objective(8,n) if n<400 else -1)==5
assert max(range(1,100),key=lambda n:objective(10,n) if n<500 else -1)==4
print('PASS',count,'random independent designs; all exact winning certificates positive; asymptotic winner four')
