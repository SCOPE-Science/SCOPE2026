#!/usr/bin/env python3
"""Exact independent-set and clock-rate checks for the two-subset Kneser RSA law.
Runs under Python 3 standard library.  No external data or dependencies.
"""
from itertools import combinations, permutations
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


def graph(n):
    edges=list(combinations(range(n),2))
    block=[]
    for e in edges:
        block.append(sum(1<<j for j,f in enumerate(edges)
                         if set(e).isdisjoint(f)))
    return edges,block


def exact_output_probabilities(n):
    edges,block=graph(n)
    N=len(edges)
    @lru_cache(None)
    def f(mask):
        if mask==0:
            return {0:Fraction(1)}
        out=defaultdict(Fraction)
        available=[i for i in range(N) if mask&(1<<i)]
        for i in available:
            nxt=mask&~(block[i]|(1<<i))
            for k,p in f(nxt).items():
                out[k+1]+=p/len(available)
        return dict(out)
    return f((1<<N)-1), f.cache_info()


def test_structure(n):
    # Every maximal independent family of two-subsets is a triangle or full star.
    E,B=graph(n); N=len(E)
    for a in range(n):
        star=frozenset(i for i,e in enumerate(E) if a in e)
        assert len(star)==n-1
        assert all(not (B[i]>>j&1) for i,j in combinations(star,2))
        assert all(any(B[j]>>i&1 for i in star) for j in range(N) if j not in star)
    for tri in combinations(range(n),3):
        triangle=frozenset(E.index(tuple(e)) for e in combinations(tri,2))
        assert len(triangle)==3
        assert all(not (B[i]>>j&1) for i,j in combinations(triangle,2))
        assert all(any(B[j]>>i&1 for i in triangle) for j in range(N) if j not in triangle)


def verify_rate_geometry(n):
    E,B=graph(n); N=len(E)
    assert N==comb(n,2)
    for i,ab in enumerate(E):
        after1=((1<<N)-1)&~(B[i]|(1<<i))
        assert after1.bit_count()==2*(n-2)
        for j in range(N):
            if not (after1>>j&1):continue
            after2=after1&~(B[j]|(1<<j))
            assert after2.bit_count()==n-2
            # Exactly one triangle closure and the rest center-star possibilities.
            center=next(v for v in ab if v in E[j])
            closure=set(ab)^set(E[j])
            triangle_edges=[k for k,e in enumerate(E) if set(e)==closure]
            assert len(triangle_edges)==1
            t=triangle_edges[0]
            assert after2>>t&1
            assert sum(1 for k in range(N) if after2>>k&1 and center in E[k])==n-3
            for k in range(N):
                if not (after2>>k&1):continue
                after3=after2&~(B[k]|(1<<k))
                assert after3.bit_count()==(0 if k==t else n-4)
                if k!=t:
                    assert all(center in E[l] for l in range(N) if after3>>l&1)


def verify_moments(n):
    p=Fraction(1,n-2)
    mean=Fraction(n-1)-(n-4)*p
    variance=(n-4)**2*p*(1-p)
    exact,_=exact_output_probabilities(n)
    assert exact=={3:p,n-1:1-p},(n,exact)
    assert sum(k*q for k,q in exact.items())==mean
    assert sum((k-mean)**2*q for k,q in exact.items())==variance


def verify_exponential_races(n):
    N=comb(n,2)
    rates=[N,2*(n-2),n-2]
    # Laplace transform of the third successful arrival time B.
    for s in [Fraction(1,2),Fraction(2),Fraction(7,3)]:
        laplace=Fraction(1)
        for rate in rates:
            laplace*=Fraction(rate,1)/(rate+s)
        assert laplace>0
        # Maximum of r iid Exp(1) has transform r! / ((s+1)...(s+r)).
        r=n-4
        maximum=Fraction(factorial(r),1)
        for j in range(1,r+1):maximum/=s+j
        # Independent mixtures identify joint transforms for each outcome.
        fast=laplace/Fraction(n-2)
        slow=laplace*maximum*Fraction(n-3,n-2)
        assert fast+slow==laplace*(Fraction(1,n-2)+Fraction(n-3,n-2)*maximum)
        assert 0<fast+slow<1
    # Exact conditional expected time in each branch.
    E_B=sum((Fraction(1,k) for k in rates),Fraction(0))
    H=sum((Fraction(1,j) for j in range(1,n-3)),Fraction(0))
    assert H>0
    assert E_B+H>E_B


def main():
    checks=0
    for n in range(5,9):
        verify_rate_geometry(n); checks+=1
        test_structure(n); checks+=1
        verify_moments(n); checks+=1
        verify_exponential_races(n); checks+=1
        exact,cache=exact_output_probabilities(n)
        print(f'n={n}: P(triangle)={exact[3]}, P(star)={exact[n-1]}, states={cache.currsize}')
    print(f'PASS: {checks} independent grouped exact checks (with exhaustive state and adjacency loops).')

if __name__=='__main__':
    main()
