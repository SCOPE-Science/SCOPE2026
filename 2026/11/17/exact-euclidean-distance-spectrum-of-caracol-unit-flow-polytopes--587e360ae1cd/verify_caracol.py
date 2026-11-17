"""Exact independent finite checks of canonical caracol flow-polytope vertex distances.

Run: python verify_caracol.py
No dependencies beyond Python's standard library.
"""
from collections import Counter
from itertools import combinations
from math import comb
from fractions import Fraction


def polynomial(L):
    """Closed histogram of squared Euclidean distances of unordered distinct paths."""
    assert L >= 2
    counts = Counter()
    for d in range(1, L):
        counts[4] += L-d
        counts[d+2] += 2*(L-d)
    for a in range(1, L-1):
        counts[a+2] += 2*comb(L-a, 2)
        counts[a+4] += 2*comb(L-a, 2)
    for d in range(2, L):
        counts[d+4] += 2*(d-1)*(L-d)
    for g in range(2, L-1):
        counts[g+4] += 3*(g-1)*comb(L-g, 2)
    return +counts


def actual_paths(n):
    assert n >= 3
    for i in range(2,n+1):
        for j in range(i,n+1):
            # Original ambient graph edge-coordinate embedding, with actual directed edges.
            yield (i,j), frozenset([(1,i),(j,n+1)] +
                                   [(k,k+1) for k in range(i,j)])


def checked(n):
    paths = list(actual_paths(n))
    assert len(paths) == (n-1)*n//2
    hist = Counter()
    diametral = set()
    for (a,pa),(b,pb) in combinations(paths,2):
        d2=len(pa.symmetric_difference(pb))
        hist[d2]+=1
        if d2==n+2:
            diametral.add(frozenset((a,b)))
    expected=polynomial(n-1)
    assert hist==expected,(n,hist,expected)
    M=(n-1)*n//2
    assert sum(hist.values())==comb(M,2)
    mean=Fraction(sum(k*v for k,v in hist.items()),comb(M,2))
    L=n-1
    predicted=Fraction(2*(3*L*L+35*L+18),15*(L+2))
    assert mean==predicted,(n,mean,predicted)
    if n==3:
        assert max(hist)==4 and hist[4]==1
    else:
        assert max(hist)==n+2 and hist[n+2]==2*(n-3)
        expected_pairs=set()
        full=(2,n)
        for t in range(3,n):
            expected_pairs.add(frozenset((full,(t,t))))
            expected_pairs.add(frozenset(((2,t),(t,n))))
        assert diametral==expected_pairs
    return len(paths),sum(hist.values()),len(hist)


def beta_kolmogorov(L):
    """Exact finite-histogram Kolmogorov difference from Beta(2,3)."""
    hist=polynomial(L)
    M=L*(L+1)//2
    norm=comb(M,2)
    def F(x):
        x=min(1,max(0,x))
        return 6*x*x-8*x*x*x+3*x**4
    levels=sorted(set([0]+list(hist)+[L]))
    delta=0
    seen=0
    for v in levels:
        x=v/L
        delta=max(delta,abs(seen/norm-F(x)))
        seen+=hist[v]
        delta=max(delta,abs(seen/norm-F(x)))
    return delta


if __name__ == '__main__':
    pv=0; checks=0; levels=0
    for n in range(3,17):
        p,k,l=checked(n)
        pv+=p;checks+=k;levels+=l
    for L in (20,50,100,200,400):
        err=beta_kolmogorov(L)
        assert err<25/L,(L,err)
        print('beta_K',L,round(err,9))
    print('CARACOL_METRIC_PASS orders=3..16 vertices=%d pairs=%d coefficient_levels=%d' % (pv,checks,levels))
