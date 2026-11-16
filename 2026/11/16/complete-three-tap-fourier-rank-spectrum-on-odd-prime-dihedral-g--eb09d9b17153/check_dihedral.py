#!/usr/bin/env python3
"""Independent regular-matrix checks for three-point dihedral convolutions.

Requires Python 3 and numpy. Numerical ranks corroborate, not prove, the theorem.
"""
import cmath
import itertools
import math
import numpy as np


def product(g, h, p):
    return ((g[0] + (-1 if g[1] else 1) * h[0]) % p, g[1] ^ h[1])


def left_matrix(p, taps):
    group = [(i, j) for j in (0, 1) for i in range(p)]
    where = {v: i for i, v in enumerate(group)}
    mat = np.zeros((2*p, 2*p), dtype=complex)
    for g, a in taps:
        for col, h in enumerate(group):
            mat[where[product(g, h, p)], col] += a
    return mat


def nullity(p, taps):
    svals = np.linalg.svd(left_matrix(p, taps), compute_uv=False)
    return int(np.sum(svals < 1e-7))


def same_weights(p, support, level):
    exponents = [t for t, _ in support]
    if level == 0:
        return [10, 1, 1]
    if level == 2:
        return [1, 2, -3]
    if level == 4:
        z = cmath.exp(2j*math.pi/p)
        r1 = [z**e for e in exponents]
        r2 = [z**(2*e) for e in exponents]
        return [r1[(i+1)%3]*r2[(i+2)%3]-r1[(i+2)%3]*r2[(i+1)%3] for i in range(3)]
    raise ValueError(level)


def mixed_weights(p, support, level):
    counts = {u: sum(e == u for _, e in support) for u in (0,1)}
    paircoset = 0 if counts[0] == 2 else 1
    single_weight = {0:3, 1:2, 2:math.sqrt(2+2*math.cos(2*math.pi/p))}[level]
    return [1 if e == paircoset else single_weight for _,e in support]


def run():
    total=0
    for p in (3,5,7,11):
        group=[(i,j) for j in (0,1) for i in range(p)]
        per={0:0,1:0,2:0,4:0}
        for support in itertools.combinations(group,3):
            onecoset = len({e for _,e in support}) == 1
            levels = (0,2,4) if onecoset else (0,1,2)
            for expected in levels:
                w=same_weights(p,support,expected) if onecoset else mixed_weights(p,support,expected)
                assert all(abs(v)>1e-8 for v in w)
                seen=nullity(p,list(zip(support,w)))
                assert seen == expected, (p,support,expected,seen,w)
                per[expected]+=1
                total+=1
        print('PRIME',p,'triples',math.comb(2*p,3),'cases',sum(per.values()),'levels',per)
    print('DIHEDRAL_THREE_POINT_PASS cases',total)

if __name__=='__main__':
    run()
