"""Direct finite-graph and stochastic checks of the priority-network theorem.

Run: python verify.py
"""
from fractions import Fraction as F
from itertools import combinations, product
import math
import numpy as np


def exact_moments(n,p):
    edges=list(combinations(range(n),2))
    N=len(edges)
    ex=ew=ex2=ew2=exw=F(0)
    for mask in range(1<<N):
        degrees=[0]*n
        m=mask.bit_count()
        for j,(a,b) in enumerate(edges):
            if mask>>j & 1:
                degrees[a]+=1;degrees[b]+=1
        x=2*m
        w=sum(d*(d-1) for d in degrees)
        prob=p**m*(1-p)**(N-m)
        ex+=prob*x;ew+=prob*w
        ex2+=prob*x*x;ew2+=prob*w*w;exw+=prob*x*w
    return ex,ew,ex2-ex*ex,ew2-ew*ew,exw-ex*ew


def formula_moments(n,p):
    N=n*(n-1)//2
    H=n*(n-1)*(n-2)//2
    q=2*(n-2)
    return (2*N*p,2*H*p**2,4*N*p*(1-p),
            4*(H*(p**2-p**4)+N*q*(q-1)*(p**3-p**4)),
            8*H*p*p*(1-p))


count=0
for n in range(2,6):
    for p in [F(1,4),F(2,3)]:
        actual=exact_moments(n,p)
        expected=formula_moments(n,p)
        assert actual==expected,(n,p,actual,expected)
        count+=5
print('Exact graph-moment equalities:',count)


def direct_hodge_share(n,edge_mask):
    edges=list(combinations(range(n),2))
    selected=[edges[i] for i in range(len(edges)) if edge_mask>>i&1]
    if not selected:return 0.0
    matrix=np.zeros((n*2**(n-1),2**n),dtype=float)
    flow=np.zeros(n*2**(n-1),dtype=float)
    idx=0
    for agent in range(n):
        for other in range(2**n):
            if other>>agent&1:continue
            s0=other;s1=other|(1<<agent)
            matrix[idx,s0]=-1;matrix[idx,s1]=1
            def utility(s):
                mine=(s>>agent)&1
                return -sum(1 for a,b in selected if (a==agent or b==agent)
                            for rival in ([b] if a==agent else [a])
                            if ((s>>rival)&1)>mine or (((s>>rival)&1)==mine and rival<agent))
            flow[idx]=utility(s1)-utility(s0)
            idx+=1
    grad=matrix@np.linalg.lstsq(matrix,flow,rcond=None)[0]
    energy=float(flow@flow)
    harm=float((flow-grad)@(flow-grad))
    return harm/energy


count=0
for n in range(2,5):
    edges=list(combinations(range(n),2))
    for mask in range(1<<len(edges)):
        deg=[0]*n
        for j,(a,b) in enumerate(edges):
            if mask>>j & 1:deg[a]+=1;deg[b]+=1
        x=sum(deg);q=sum(d*d for d in deg)
        expected=x/(x+q) if x else 0
        actual=direct_hodge_share(n,mask)
        assert abs(actual-expected)<1e-10,(n,mask,actual,expected)
        count+=1
print('Direct Hodge least-squares graphs:',count)

# Seeded approximate checks, not a proof of asymptotics.
rng=np.random.default_rng(79143)
for lam in [0.7,1.8]:
    n=700
    samples=[]
    for rep in range(320):
        a,b=np.triu_indices(n,1)
        active=rng.random(len(a)) < lam/n
        deg=np.bincount(np.r_[a[active],b[active]],minlength=n)
        x=deg.sum();w=np.sum(deg*(deg-1))
        samples.append(math.sqrt(n)*(x/(2*x+w)-1/(lam+2)))
    pred=2*(1+lam)/(2+lam)**4
    obs=float(np.var(samples,ddof=1))
    assert abs(obs-pred)<0.018,(lam,obs,pred)
    print('Gaussian-scale variance check:',lam,round(obs,6),round(pred,6))

print('PASS')
