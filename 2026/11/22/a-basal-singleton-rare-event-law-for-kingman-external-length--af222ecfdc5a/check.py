"""Exact checks for the Kingman basal-singleton conditional external-length identity.
All arithmetic in the finite-history phase is rational; no statistical simulation is used.
"""
from fractions import Fraction as F
from itertools import combinations
from math import prod


def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)), F(0))

def formulas(n):
    h=harmonic(n)
    p=F(2,n-1)
    conditional_mean=2*(1-F(1,n)) + F(2,n-2)*(n+1-2*h)
    covariance=4*(n*n+2-2*n*h)/F(n*(n-1)*(n-2))
    assert covariance==p*(conditional_mean-2)
    return p,conditional_mean,covariance


def exact_history(n):
    total=0
    total_root=0
    summed=F(0)
    summed_root=F(0)
    def recur(state, accumulated):
        nonlocal total,total_root,summed,summed_root
        k=len(state)
        accumulated=accumulated+F(2,k*(k-1))*sum(len(s)==1 for s in state)
        if k==2:
            total+=1
            summed+=accumulated
            if any(len(s)==1 for s in state):
                total_root+=1
                summed_root+=accumulated
            return
        for i,j in combinations(range(k),2):
            nxt=[state[t] for t in range(k) if t!=i and t!=j]+[state[i]|state[j]]
            recur(nxt,accumulated)
    recur([frozenset((i,)) for i in range(n)], F(0))
    p,mu,cov=formulas(n)
    assert F(total_root,total)==p,(n,total_root,total,p)
    assert summed/F(total)==2,(n,summed,total)
    assert summed_root/F(total_root)==mu,(n,summed_root,total_root,mu)
    assert (summed_root/F(total)-p*2)==cov
    return n,total,p,mu,cov


def conditional_expectation_by_stage(n):
    # Conditional on a fixed singleton lineage surviving until the final merger.
    # Other n-1 lineages follow the standard pure Kingman pair-merging topology.
    # Singleton expectation at the k-lineage stage is 1+(k-1)(k-2)/(n-2).
    vals=[F(2,k*(k-1))*(1+F((k-1)*(k-2),n-2)) for k in range(2,n+1)]
    assert sum(vals,F(0))==formulas(n)[1]
    return vals

if __name__=='__main__':
    for n in range(3,8):
        r=exact_history(n)
        conditional_expectation_by_stage(n)
        print('exact',r)
    for n in range(4,501):
        p,mu,cov=formulas(n)
        assert cov>0
        assert n*F(2,n*(n-1))==p  # disjoint root-survivor events, one per original label
        assert F(0)<mu<4
    for n in (10,100,1000,10000):
        p,mu,cov=formulas(n)
        print('asymptotic',n,'P',float(p),'E[L|R]',float(mu),'n*Cov',float(n*cov))
    print('PASS: complete finite-history enumerations through seven labels and analytic consistency checks')
