#!/usr/bin/env python3
"""Exact enumerative checks for the leaf/cherry Palm law in uniform Cayley trees.

Run: python check.py
Only the finite tests here are computational; the theorem has an analytic proof.
"""
from itertools import product
from fractions import Fraction
from collections import defaultdict
from math import comb, sqrt


def statistics_from_prufer(word, n):
    degree = [1] * n
    for k in word:
        degree[k] += 1
    deg0 = degree[:]
    edges = []
    for k in word:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, k))
        degree[leaf] -= 1
        degree[k] -= 1
    last = [i for i in range(n) if degree[i] == 1]
    assert len(last) == 2
    edges.append(tuple(last))
    leaf_neighbours = [0] * n
    for u,v in edges:
        if deg0[u] == 1:
            leaf_neighbours[v] += 1
        if deg0[v] == 1:
            leaf_neighbours[u] += 1
    L = sum(d == 1 for d in deg0)
    C = sum(k * (k-1)//2 for k in leaf_neighbours)
    return L, C


def formulas(n):
    ntrees = n**(n-2)
    p1 = Fraction((n-1)**(n-2), ntrees)
    eL = n*p1
    p2 = Fraction((n-2)**(n-4), ntrees)
    eC = n*comb(n-1,2)*p2
    # For n=4 a residual single vertex is the unique one-vertex tree.
    p3 = Fraction((n-3)**(n-5),ntrees) if n>=5 else Fraction(1,ntrees)
    # The 4-leaf marked forest is possible for n>=5.
    p4 = (Fraction((n-4)**(n-6),ntrees) if n>=6 else
          Fraction(1,ntrees) if n==5 else Fraction(0))
    eC2 = (eC + n*(n-1)*(n-2)*(n-3)*p3 +
           Fraction(n*(n-1)*(n-2)*(n-3)*(n-4)**2,4)*p4)
    eL2 = eL+n*(n-1)*Fraction((n-2)**(n-2),ntrees)
    # Conditional cherry-size-biased leaf law.
    psmall = Fraction((n-3)**(n-4),(n-2)**(n-4))
    palmL = 2+(n-3)*psmall
    cov = eC*(palmL-eL)
    return eL,eC,eL2,eC2,cov,palmL


def run():
    checks=0
    for n in range(4,9):
        m=n**(n-2)
        sL=sC=sL2=sC2=sLC=0
        weighted=defaultdict(int)
        for word in product(range(n),repeat=n-2):
            L,C=statistics_from_prufer(word,n)
            sL+=L; sC+=C; sL2+=L*L; sC2+=C*C; sLC+=L*C
            weighted[L]+=C
        eL,eC,eL2,eC2,cov,palmL=formulas(n)
        assert Fraction(sL,m)==eL
        assert Fraction(sC,m)==eC
        assert Fraction(sL2,m)==eL2
        assert Fraction(sC2,m)==eC2
        assert Fraction(sLC,m)-eL*eC==cov
        assert Fraction(sLC,sC)==palmL
        assert cov>0
        checks+=7
        # Distribution of the size-biased leaf count under a uniform cherry.
        # Remove two cherry leaves; compare with T_(n-2) and a fixed center 0.
        hist=defaultdict(int)
        msmall=(n-2)**(n-4)
        for w in product(range(n-2),repeat=n-4):
            ls,cs=statistics_from_prufer(w,n-2)
            # Center 0 is a leaf iff 0 does not occur in the Prufer word,
            # except the 2-vertex tree, where both endpoints are leaves.
            center_leaf=(0 not in w)
            hist[2+ls-int(center_leaf)]+=1
        assert all(Fraction(weighted[k],sC)==Fraction(hist[k],msmall)
                   for k in set(weighted)|set(hist))
        checks+=len(set(weighted)|set(hist))
        print(f'n={n}: trees={m}, E[leaves]={eL}, E[cherries]={eC}, cov={cov}, Palm={palmL}')
    for n in range(9,201):
        eL,eC,eL2,eC2,cov,palmL=formulas(n)
        assert cov>0 and eL2>=eL*eL and eC2>=eC*eC
        checks+=3
    print(f'PASS {checks} exact assertions; exhaustive Cayley trees n=4..8; formulas checked n=9..200')

if __name__=='__main__':run()
