#!/usr/bin/env python3
"""Exact signed Fourier recovery for Eulerian orientations of C_7^2.

Run with Python 3 standard library only: python3 verify_ice7.py
All enumerations are exhaustive on finite, explicitly bounded domains.
"""
from collections import Counter
from fractions import Fraction

N_VERT = 7
EDGES = tuple(sorted({tuple(sorted((i, (i+d) % N_VERT)))
                      for i in range(N_VERT) for d in (1, 2)}))
assert len(EDGES) == 14
EDGE_ID = {e: k for k, e in enumerate(EDGES)}
DIM = len(EDGES)
SIZE = 1 << DIM


def fwht(x):
    x = list(x)
    for k in range(DIM):
        t = 1 << k
        for base in range(0, SIZE, 2*t):
            for j in range(base, base+t):
                a, b = x[j], x[j+t]
                x[j], x[j+t] = a+b, a-b
    return x


def direct_states():
    states = set()
    for mask in range(SIZE):
        out = [0] * N_VERT
        for j, (u, v) in enumerate(EDGES):
            out[v if (mask >> j) & 1 else u] += 1
        if all(c == 2 for c in out):
            states.add(mask)
    return states


def flow_states():
    """An independent jump-coordinate enumeration using local conservation."""
    result = set()
    for data in range(1 << (2*N_VERT)):
        a = tuple((data >> i) & 1 for i in range(N_VERT))
        b = tuple((data >> (N_VERT+i)) & 1 for i in range(N_VERT))
        if not all(a[i]+b[i] == a[(i-1)%N_VERT]+b[(i-2)%N_VERT]
                   for i in range(N_VERT)):
            continue
        word = 0
        for i in range(N_VERT):
            for jump, direction in ((1, a[i]), (2, b[i])):
                j = (i+jump)%N_VERT
                key = (min(i, j), max(i, j))
                # direction=1 means i -> j; bit=1 means high -> low.
                bit = int(direction == 1) if i > j else int(direction == 0)
                word |= bit << EDGE_ID[key]
        result.add(word)
    return result


def signed_coefficient(mask):
    """Independent generating-polynomial coefficient [product t_i^2]."""
    dp = {(0,)*N_VERT: 1}
    for j, (u, v) in enumerate(EDGES):
        next_dp = {}
        sign = -1 if ((mask >> j) & 1) else 1
        for degrees, weight in dp.items():
            if degrees[u] < 2:
                z = list(degrees); z[u] += 1; z = tuple(z)
                next_dp[z] = next_dp.get(z, 0)+weight
            if degrees[v] < 2:
                z = list(degrees); z[v] += 1; z = tuple(z)
                next_dp[z] = next_dp.get(z, 0)+sign*weight
        dp = next_dp
    return dp.get((2,)*N_VERT, 0)


def tree_indices():
    visited = {0}; tree=[]
    while len(visited)<N_VERT:
        found = False
        for j,(u,v) in enumerate(EDGES):
            if (u in visited) != (v in visited):
                visited.add(v if u in visited else u)
                tree.append(j); found=True; break
        assert found
    return set(tree)


def check():
    states = direct_states()
    independent = flow_states()
    assert states == independent and len(states) == 60
    indicator = [int(x in states) for x in range(SIZE)]
    W = fwht(indicator)
    hist = dict(sorted(Counter(W).items()))
    EXPECTED = {-60:32,-24:224,-20:224,-16:224,-12:224,
                -8:672,-4:1568,0:10048,4:1568,8:672,
                12:224,16:224,20:224,24:224,60:32}
    assert hist == EXPECTED
    assert sum(W[i]**2 for i in range(SIZE)) == SIZE*60
    assert all(W[i] == 0 for i in range(SIZE) if i.bit_count()%2)
    assert all(W[i]%4==0 for i in range(SIZE))
    assert min(abs(w) for w in W if w) == 4

    # Coefficient-extraction enumeration is independent of the orientation list.
    tree = tree_indices()
    free = [j for j in range(DIM) if j not in tree]
    assert len(tree) == 6 and len(free) == 8
    for m in range(1 << len(free)):
        s = sum(1 << j for i,j in enumerate(free) if m>>i&1)
        direct = sum(-1 if (s & x).bit_count()%2 else 1 for x in states)
        assert W[s] == direct == signed_coefficient(s)
    # Every frequency is a cut translate of exactly one representative.
    # Cut translations preserve zero versus nonzero by fixed-outdegree parity.
    for vertex in range(N_VERT):
        cut = sum(1 << j for j, (u,v) in enumerate(EDGES)
                  if vertex in (u,v))
        assert all((W[freq] == 0) == (W[freq ^ cut] == 0)
                   for freq in range(SIZE))

    expected_pairs = set()
    for i in range(N_VERT):
        short = EDGE_ID[tuple(sorted((i,(i+1)%N_VERT)))]
        for j in ((i+2)%N_VERT, (i+4)%N_VERT):
            long = EDGE_ID[tuple(sorted((j,(j+2)%N_VERT)))]
            expected_pairs.add((min(short,long),max(short,long)))
    actual_pairs = {(i,j) for i in range(DIM) for j in range(i+1,DIM)
                    if W[(1<<i)|(1<<j)]==0}
    assert actual_pairs==expected_pairs and len(actual_pairs)==14

    # Fourier orthogonal range projection, exact integer numerator.
    support = [int(w != 0) for w in W]
    kernel = fwht(support)
    kern_hist = dict(sorted(Counter(kernel).items()))
    expected_kernel = {-448:14,-320:42,-192:28,-64:42,0:16128,
                       64:42,192:28,320:42,448:14,1856:2,6336:2}
    assert kern_hist == expected_kernel
    assert sum(abs(x) for x in kernel) == 71936
    norm = Fraction(sum(abs(x) for x in kernel),SIZE)
    assert norm == Fraction(281,64)
    assert sum(x != 0 for x in kernel)==256
    assert sum(x*x for x in kernel) == SIZE*6336
    print('ICE7_EXACT_PASS')
    print('edges',DIM,'configurations',len(states),'frequencies',SIZE)
    print('spectrum',hist)
    print('Fourier rank',SIZE-hist[0],'nullity',hist[0])
    print('nonzero gap',4,'condition number',15)
    print('first even cancellation support',2,'zero pairs',len(actual_pairs))
    print('projection kernel numerator',kern_hist)
    print('support of kernel',sum(x!=0 for x in kernel))
    print('minimum endpoint projection norm',norm)
    return {'spectrum':hist,'kernel':kern_hist,'norm':str(norm)}


if __name__ == '__main__':
    check()
