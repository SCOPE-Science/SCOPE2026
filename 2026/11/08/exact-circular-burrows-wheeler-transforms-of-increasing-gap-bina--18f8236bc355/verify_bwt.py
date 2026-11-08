#!/usr/bin/env python3
"""Exact tests for the circular Burrows--Wheeler transform of increasing-gap words."""
from itertools import product

def source(gaps):
    assert len(gaps) >= 2 and all(x >= 1 for x in gaps)
    assert all(a < b for a, b in zip(gaps, gaps[1:]))
    return '1' + ''.join('0' * g + '1' for g in gaps)

def bwt_direct(w):
    n = len(w)
    rotations = sorted((w[i:] + w[:i], i) for i in range(n))
    return ''.join(w[(i - 1) % n] for _, i in rotations)

def predicted(gaps):
    k = len(gaps)
    g = [0] + list(gaps)
    deltas = [g[i] - g[i-1] for i in range(1, k+1)]
    return ('1' + '0' * (deltas[k-1] - 1) + '1'
            + ''.join('0' * ((k-j+1)*deltas[j-1]) + '1'
                      for j in range(k-1, 1, -1))
            + '0' * (k * deltas[0]) + '10')

def runs(w):
    return 1 + sum(a!=b for a,b in zip(w,w[1:]))

def test():
    ncases = 0
    for k in range(2, 8):
        for differences in product(range(1, 5), repeat=k):
            g=[]
            for d in differences: g.append((g[-1] if g else 0) + d)
            w = source(g)
            actual = bwt_direct(w)
            formula = predicted(g)
            assert actual == formula, (g, actual, formula)
            assert actual.count('1') == k+1
            assert len(actual) == len(w)
            assert runs(actual) == 2*k+2-2*(differences[-1]==1)
            ncases += 1
    radial = 0
    for b in range(3, 8):
        for k in range(2, 7):
            n=b**k
            if n>2400: continue
            g=[b-2]+[(b-1)*b**(j-1)-1 for j in range(2,k+1)]
            w=source(g)
            assert len(w)==n
            assert all(w[i]=='1' for i in [b**j-1 for j in range(k+1)])
            actual=bwt_direct(w)
            assert actual==predicted(g)
            assert runs(actual)==2*(k+1)
            radial+=1
    print(f'PASS exhaustive_gap_vectors={ncases}; radial_prefixes={radial}; lengths_and_runcounts=verified')

if __name__ == '__main__': test()
