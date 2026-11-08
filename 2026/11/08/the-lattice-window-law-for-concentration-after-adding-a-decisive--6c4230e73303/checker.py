#!/usr/bin/env python3
"""Standalone exact finite checks for graphic voting-game concentration changes.

Scientific definitions: a graph edge is one minimal winning coalition; each player
has Deegan--Packel index degree/(2 * edge_count). This program does not treat
finite experiments as proofs of asymptotic statements.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import random


def concentration(n, edges):
    assert len(edges) > 0
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    m = len(edges)
    return sum(Fraction(d, 2*m)**2 for d in deg), deg


def wedge_count(deg):
    return sum(comb(d, 2) for d in deg)


def independent_check(n=5):
    tests = 0
    for size in range(3, n+1):
        pairs = list(combinations(range(size), 2))
        for mask in range(1, 1 << len(pairs)):
            edges = {e for i,e in enumerate(pairs) if mask & (1 << i)}
            m = len(edges)
            old, deg = concentration(size, edges)
            w = wedge_count(deg)
            assert old == Fraction(2*m+2*w, 4*m*m)
            for e in pairs:
                if e in edges: continue
                new, _ = concentration(size, edges | {e})
                D = deg[e[0]] + deg[e[1]]
                criterion = 2*m*m*(D+1) > (2*m+1)*(2*m+2*w)
                assert (new > old) == criterion
                tests += 1
    return tests


def check_random_graph_moments():
    # Exact enumeration validates the explicit two-chaos expansion's mean/variance.
    tests = 0
    for n in (3, 4, 5):
        pairs = list(combinations(range(n), 2))
        N = len(pairs)
        K = n*comb(n-1, 2)
        for c in (Fraction(1, 2), Fraction(1, 1), Fraction(3, 2)):
            p = c/n
            ex = Fraction(0); ex2=Fraction(0)
            for mask in range(1 << N):
                m = mask.bit_count()
                deg = [0]*n
                for i, (u,v) in enumerate(pairs):
                    if mask & (1 << i):
                        deg[u] += 1; deg[v] += 1
                W = wedge_count(deg)
                val = W-c*m
                probability = p**m*(1-p)**(N-m)
                ex += val*probability
                ex2 += val*val*probability
                tests += 1
            expected = K*p*p - c*N*p
            variance = (2*(n-2)*p-c)**2 * N*p*(1-p) + K*p*p*(1-p)**2
            assert ex == expected and ex2-ex*ex == variance
    return tests


def graph_sparse(n, p, rng):
    # Geometric skip sampler for exact independent Bernoulli edges, except edge (0,1)
    import math
    N = n*(n-1)//2
    logq = math.log1p(-p)
    deg = [0]*n
    m=0
    pos=-1
    u=0
    first=0
    while True:
        pos += 1+int(math.log(rng.random())/logq)
        if pos >= N: break
        while pos >= first+(n-u-1):
            first += n-u-1
            u+=1
        v=u+1+(pos-first)
        if u==0 and v==1: continue
        deg[u]+=1;deg[v]+=1;m+=1
    return m,deg


def increase_event(m,deg):
    if m == 0: return False
    S=sum(d*d for d in deg)
    D=deg[0]+deg[1]
    return 2*m*m*(D+1)>(2*m+1)*S


def simulate(n=1600, repetitions=800, c=1.0, beta=0.0, seed=2309):
    import math
    from statistics import NormalDist
    rng=random.Random(seed)
    p=c/n+beta/n**1.5
    count=0
    for _ in range(repetitions):
        m,deg=graph_sparse(n,p,rng)
        count+=increase_event(m,deg)
    def poisson_pmf(k):return math.exp(-2*c)*(2*c)**k/math.factorial(k)
    k=round(2*c)
    if abs(2*c-k)<1.e-12:
        base=1-sum(poisson_pmf(j) for j in range(k+2))
        limit=base+NormalDist().cdf(-beta/math.sqrt(2*(1+c)))*poisson_pmf(k+1)
    else:
        r=math.floor(2*c+1)
        limit=1-sum(poisson_pmf(j) for j in range(r+1))
    return count/repetitions,limit


if __name__=='__main__':
    a=independent_check(5)
    b=check_random_graph_moments()
    print('EXACT finite edge-addition comparisons:',a)
    print('EXACT finite second-moment enumerations:',b)
    for args in ((.7,0),(1,0),(1,-1.5),(1,1.5),(1.4,0)):
        estimate,limit=simulate(n=1400,repetitions=800,c=args[0],beta=args[1])
        print('limit-check c,beta:',args,'Monte Carlo',round(estimate,4),'limit',round(limit,4))
        assert abs(estimate-limit)<0.09
    print('PASS: exact finite identities and independent asymptotic spot checks')
