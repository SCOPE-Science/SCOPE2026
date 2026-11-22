"""Exact reproducibility checks for occupancy-induced forest component covariance.
Run: python verify.py (Python 3 standard library)."""
from fractions import Fraction
from itertools import product
from collections import defaultdict
from math import comb,log

def closed(m, n, e):
    """Exact covariance via one-/two-/three-site vacancy events."""
    if not (m>=3 and n>=1 and 0<=e<=m-1): raise ValueError
    q=lambda k: Fraction(m-k,m)**n
    v=m*q(1)+m*(m-1)*q(2)-m*m*q(1)**2
    p2=1-2*q(1)+q(2)
    edge=2*q(1)*p2+(m-2)*(2*q(2)-q(3)-2*q(1)**2+q(1)*q(2))
    return v-e*edge

def closed_tree_exp(m,n):
    a=Fraction(m-1,m)**n
    b=Fraction(m-2,m)**n
    c=Fraction(m-3,m)**n
    return -(m-2)*a+(m-1)*(4-m)*b+(m-1)*(m-2)*c+m*(m-2)*a*a-m*(m-1)*a*b

def all_trees(m):
    if m==2:
        yield [(0,1)];return
    for seq in product(range(m),repeat=m-2):
        deg=[1]*m
        for i in seq: deg[i]+=1
        edges=[]
        for k in seq:
            leaf=next(j for j,d in enumerate(deg) if d==1)
            edges.append((leaf,k))
            deg[leaf]-=1;deg[k]-=1
        p=[j for j,d in enumerate(deg) if d==1]
        edges.append((p[0],p[1]))
        yield edges

def moments_exact(m,n,edges):
    total=m**n
    sumk=sumc=sumkc=0
    for draws in product(range(m),repeat=n):
        occ=set(draws)
        K=len(occ)
        C=K-sum(u in occ and v in occ for (u,v) in edges)
        sumk+=K;sumc+=C;sumkc+=K*C
    return Fraction(sumkc,total)-Fraction(sumk*sumc,total*total)

checks=0
for m in range(3,6):
    for n in range(1,5):
        want=closed(m,n,m-1)
        assert want==closed_tree_exp(m,n)
        checks+=1
        for edges in all_trees(m):
            got=moments_exact(m,n,edges)
            assert got==want,(m,n,edges,got,want)
            checks+=1
        if n==2: assert want==Fraction((m-1)*(m-2),m**3)
        if n>1: assert want!=0
for m in range(3,24):
    assert closed(m,1,m-1)==0
    signs=[]
    for n in range(2,4*m+1):
        got=closed(m,n,m-1)
        signs.append((got>0)-(got<0))
        checks+=1
    assert signs[0]>0 and signs[-1]<0
    assert len([i for i in range(1,len(signs)) if signs[i]!=signs[i-1]])==1

# Sample independent-vertex percolation identity for every forest, checked numerically.
for m in range(3,8):
    for e in range(0,m):
        for p in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]:
            E=m*p*(1-p)*(1-Fraction(2*e,m)*p)
            assert E==m*p*(1-p)-2*e*p*p*(1-p)
            checks+=1

# Leading asymptotic at noncritical loads from exact rational covariance.
for lam in [0.35,0.5,0.9,1.4]:
    z=__import__('math').exp(-lam)
    expected=(2*z-1)*z*(1-(1+lam)*z)
    m=1600
    n=round(m*lam)
    q=lambda k: ((m-k)/m)**n
    v=m*q(1)+m*(m-1)*q(2)-m*m*q(1)**2
    edge=2*q(1)*(1-2*q(1)+q(2))+(m-2)*(2*q(2)-q(3)-2*q(1)**2+q(1)*q(2))
    empirical=(v-(m-1)*edge)/m
    assert abs(empirical-expected)<.004,(lam,empirical,expected)
    checks+=1
print('PASS',checks,'exact rational, enumeration and asymptotic assertions')
