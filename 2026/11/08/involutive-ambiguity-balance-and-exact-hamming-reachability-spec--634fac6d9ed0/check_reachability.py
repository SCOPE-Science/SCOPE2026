#!/usr/bin/env python3
"""Independent enumeration of four-valued move-warrant formulas.

This file contains the source truth table, separate from the derived
source-profile and aggregate polynomial formulas under test.
"""
from itertools import product
from math import comb

V = ('Y', 'N', 'B', 'U')
# Truth-lattice conjunction: row Y, N, B, U; columns in same order.
AND = (
 ('Y','N','B','U'),
 ('N','N','N','N'),
 ('B','N','B','N'),
 ('U','N','N','U'),
)
# Transition warrant: row source, column destination.
WARRANT = (
 ('Y','N','B','U'),
 ('Y','Y','Y','Y'),
 ('B','N','B','U'),
 ('Y','U','B','U'),
)

def warrant(src, dst):
    value = 0  # Y is conjunction identity
    distance = 0
    for u, v in zip(src, dst):
        if u == v:
            continue
        distance += 1
        value = V.index(AND[value][V.index(WARRANT[u][v])])
    return distance, V[value]

def convolution(p, q):
    r = [0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            r[i+j] += a*b
    return r

def pow_poly(base, power):
    out = [1]
    for _ in range(power):
        out = convolution(out, base)
    return out

def source_formula(src):
    a,b,c,d = (src.count(i) for i in range(4))
    D = convolution(pow_poly([1,3],b), pow_poly([1,1],d))
    C = convolution(convolution(pow_poly([1,1],a+c), pow_poly([1,3],b)), pow_poly([1,2],d))
    D += [0] * (len(src)+1-len(D))
    C += [0] * (len(src)+1-len(C))
    P = [2*x-y for x,y in zip(C,D)]
    return D,C,P

def flip_destination(s, t):
    # Independent coordinate involution swapping B/U local warrants.
    swaps = ((2,3), None, (0,3), (1,2))
    out = list(t)
    for j,(source,target) in enumerate(zip(s,t)):
        pair = swaps[source]
        if pair is not None:
            x,y = pair
            if target == x: out[j] = y
            elif target == y: out[j] = x
    return tuple(out)

def check(n):
    states = list(product(range(4),repeat=n))
    global_counts = [[0]*(n+1) for _ in range(3)]
    universal_possible = []
    universal_credible = []
    for s in states:
        observed = [[0]*(n+1) for _ in range(3)]
        grade_counts = [[0]*(n+1) for _ in range(4)]
        all_possible = True
        all_credible = True
        for t in states:
            k, kind = warrant(s,t)
            grade_counts[V.index(kind)][k] += 1
            if n <= 4:
                paired = flip_destination(s,t)
                kp, kindp = warrant(s,paired)
                assert kp == k
                sigma = {'Y':'Y','N':'N','B':'U','U':'B'}
                assert kindp == sigma[kind],(n,s,t,k,kind,paired,kp,kindp)
            if k and kind == 'N': all_possible = False
            if k and kind in ('N', 'U'): all_credible = False
            if kind == 'Y':
                for i in range(3): observed[i][k] += 1
            elif kind == 'B':
                for i in (1,2): observed[i][k] += 1
            elif kind == 'U':
                observed[2][k] += 1
            else: assert kind == 'N'
        assert grade_counts[2] == grade_counts[3],(n,s,grade_counts)
        if all_possible: universal_possible.append(s)
        if all_credible: universal_credible.append(s)
        expected = source_formula(s)
        assert tuple(observed)==expected,(n,s,observed,expected)
        for i in range(3):
            for k in range(n+1): global_counts[i][k]+=observed[i][k]
    assert len(universal_possible) == n+1
    assert all(set(s) <= {1,3} and s.count(3)<=1 for s in universal_possible)
    assert universal_credible == [(1,)*n]
    exp_glob = (
        [comb(n,k)*4**(n-k)*4**k for k in range(n+1)],
        [comb(n,k)*4**(n-k)*7**k for k in range(n+1)],
        [comb(n,k)*4**(n-k)*(2*7**k-4**k) for k in range(n+1)],
    )
    assert tuple(global_counts) == exp_glob,(n,global_counts,exp_glob)
    assert sum(global_counts[0][1:])==8**n-4**n
    assert sum(global_counts[1][1:])==11**n-4**n
    assert sum(global_counts[2][1:])==2*11**n-8**n-4**n
    print('n=',n,'state-pairs=',16**n,'universal_possible_sources=',len(universal_possible),'global_hamming_counts=',global_counts,'OK')

if __name__ == '__main__':
    for n in range(1,6): check(n)
    print('ALL CHECKS PASSED')
