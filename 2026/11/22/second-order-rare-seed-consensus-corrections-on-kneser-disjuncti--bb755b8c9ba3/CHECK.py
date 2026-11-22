#!/usr/bin/env python3
"""Finite reproducibility checks for sparse OR dynamics on Kneser networks."""
from itertools import combinations
from math import comb
from random import Random


def coefficients(k):
    j1 = k*(k+1)//2
    j2 = k*(k+1)*(2*k+1)//6
    a = k*k*j1
    L = k*k*(k-1)*j1/2 + k**3*j2/2
    b = L-a*a/2
    c = comb(k+2,3)*k**3+3*comb(k+2,4)*k**4
    return a,b,c


def p_disjoint(n,k):
    N=comb(n,k)
    x=1.0
    for j in range(k+1):
        x *= comb(n-j*k,k)/(N-j)
    return x


def has_small_transversal(edges,remaining):
    if not edges: return True
    if remaining==0: return False
    first=edges[0]
    return any(has_small_transversal([e for e in edges if v not in e],remaining-1) for v in first)


def check_dynamics():
    # The two-step identity is checked independently by bit-mask OR evolution.
    for n,k in [(9,3),(10,3),(6,2)]:
        verts=list(combinations(range(n),k))
        N=len(verts)
        nbr=[]
        for v in verts:
            vset=set(v)
            nbr.append(sum(1<<i for i,w in enumerate(verts) if vset.isdisjoint(w)))
        full=(1<<N)-1
        rng=Random(31415+n)
        index=list(range(N))
        states=[0,full] + [1<<i for i in index]
        for m in range(2,min(k+4,7)):
            states.extend(sum(1<<j for j in rng.sample(index,m)) for _ in range(300))
        def update(x):
            return sum((1<<i) for i,mask in enumerate(nbr) if mask&x)
        for x in states:
            y=update(x)
            z=update(y)
            assert z==(full if x else 0)
            if x:
                initial=[set(verts[i]) for i in range(N) if x>>i &1]
                assert (y==full) == (not has_small_transversal(initial,k))
        print('dynamics',n,k,len(states),'passed')


def check_expansion():
    for k in [3,4]:
        a,b,c=coefficients(k)
        print('coefficients',k,'A',int(a),'B',int(b),'C',int(c))
        for n in [120,240,480]:
            x=p_disjoint(n,k)
            approx=1-a/n-b/n**2
            # asymptotic error is third order, not required to be uniformly small at finite n
            assert abs(x-approx)<30**3*(k+1)**8/n**3
            print('matching',k,n,'exact',format(x,'.9f'),'second',format(approx,'.9f'))
    rng=Random(20261117)
    for k,n,trials in [(3,160,20000),(4,300,20000)]:
        bad=0
        for _ in range(trials):
            edges=[set(rng.sample(range(n),k)) for j in range(k+2)]
            bad+=has_small_transversal(edges,k)
        print('rare-failure',k,n,bad,trials,'leading',format(coefficients(k)[2]/n**2,'.6f'))

if __name__=='__main__':
    check_dynamics();check_expansion();print('CHECKS PASSED')
