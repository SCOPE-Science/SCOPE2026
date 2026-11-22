#!/usr/bin/env python3
"""Separate exact rational check of the 23 signed-convolution orbit representatives.

Requires sympy 1.14.0. Permutation multiplication and the rational matrices
are generated independently of verify_modular.py.
"""
from itertools import permutations
from collections import Counter
from pathlib import Path
import csv
from sympy import SparseMatrix

def odd_inversions(p):
    invs=0
    for i in range(5):
        for j in range(i+1,5):
            invs+=int(p[i]>p[j])
    return invs%2

G=[p for p in permutations(range(5)) if not odd_inversions(p)]
assert len(G)==60 and G[0]==tuple(range(5))
labels={p:i for i,p in enumerate(G)}

def multiply(g,h):
    return tuple(g[h[j]] for j in range(5))

def matrix(a,b):
    # The y-th column is delta_y + delta_{a*y} - delta_{b*y}.
    d={}
    for j,h in enumerate(G):
        for s,c in ((G[0],1),(G[a],1),(G[b],-1)):
            i=labels[multiply(s,h)]
            d[(i,j)]=d.get((i,j),0)+c
    return SparseMatrix(60,60,d)

def main():
    rows=list(csv.DictReader((Path(__file__).parent/'orbit_table.csv').open(encoding='utf-8')))
    assert len(rows)==23
    counts=Counter()
    for row in rows:
        a,b,expected=int(row['a']),int(row['b']),int(row['rank'])
        actual=matrix(a,b).rank()
        assert actual==expected,(a,b,actual,expected)
        counts[actual]+=int(row['signed_kernels'])
    assert counts==Counter({40:1800,45:3600,49:3600,54:3600,55:7200,56:10800,60:72060})
    print('RATIONAL PASS: 23 orbit representatives, exact sympy rational ranks, histogram',sorted(counts.items()))

if __name__=='__main__':main()
