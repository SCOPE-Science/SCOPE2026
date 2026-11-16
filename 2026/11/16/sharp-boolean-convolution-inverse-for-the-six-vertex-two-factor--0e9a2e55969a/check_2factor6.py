#!/usr/bin/env python3
"""Exact certificate for convolution by the 2-factor indicator of K6.

Only Python's standard library is required. All arithmetic is integral or rational.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import gcd, lcm

N = 6
EDGES = tuple(combinations(range(N), 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
M = 1 << len(EDGES)

def degrees(mask):
    d = [0] * N
    for i, (u, v) in enumerate(EDGES):
        if mask & (1 << i):
            d[u] += 1
            d[v] += 1
    return d

def brute_factors():
    # Inspect exactly the 5005 incidence vectors with 6 selected edges.
    return {sum(1 << i for i in ix)
            for ix in combinations(range(len(EDGES)), N)
            if all(z == 2 for z in degrees(sum(1 << i for i in ix)))}

def construct_factors():
    # Class 1: undirected Hamiltonian cycles, represented with vertex 0 first.
    out = set()
    for suffix in permutations(range(1, N)):
        if suffix[0] > suffix[-1]:
            continue
        p = (0,) + suffix
        edges = [tuple(sorted((p[i], p[(i+1) % N]))) for i in range(N)]
        out.add(sum(1 << EDGE_INDEX[e] for e in edges))
    assert len(out) == 60
    # Class 2: two vertex-disjoint triangles.
    for A in combinations(range(N), 3):
        B = tuple(i for i in range(N) if i not in A)
        if A[0] > B[0]:
            continue
        tri_edges = list(combinations(A, 2)) + list(combinations(B, 2))
        out.add(sum(1 << EDGE_INDEX[e] for e in tri_edges))
    assert len(out) == 70
    return out

def hadamard(v):
    a = list(v)
    for i in range(len(EDGES)):
        b = 1 << i
        for lo in range(0, M, 2*b):
            for j in range(lo, lo+b):
                x, y = a[j], a[j+b]
                a[j], a[j+b] = x+y, x-y
    return a

def main():
    first, second = brute_factors(), construct_factors()
    assert first == second and len(first) == 70
    # Single-edge incidence and the modular nonvanishing certificate.
    assert all(sum((f >> i) & 1 for f in first) == 28 for i in range(15))
    indicator = [0] * M
    for x in first:
        indicator[x] = 1
    w = hadamard(indicator)
    assert w[0] == 70
    assert all((v - 2) % 4 == 0 for v in w)
    expected = {-22: 640, -14: 3840, -2: 11520, 2: 11520,
                6: 960, 10: 384, 14: 3840, 70: 64}
    assert dict(Counter(w)) == expected
    assert sum(v*v for v in w) == M * 70
    # Independently check every character sum, not only a selected subset.
    for k in range(M):
        direct = sum(-1 if (k & t).bit_count() & 1 else 1 for t in second)
        assert w[k] == direct
    example = sum(1 << EDGE_INDEX[e] for e in ((0,1),(0,3),(1,2)))
    assert w[example] == -2
    assert min(abs(x) for x in w) == 2
    assert max(abs(x) for x in w) == 70

    denominator = lcm(*(abs(z) for z in set(w)))
    assert denominator == 2310
    reciprocal_integer = [denominator // v for v in w]
    raw_kernel = hadamard(reciprocal_integer)
    expected_kernel = {-4718592: 10, -655360: 180, -65536: 240,
                       0: 32256, 393216: 16, 2048000: 60, 8798208: 6}
    assert dict(Counter(raw_kernel)) == expected_kernel
    assert all(raw_kernel[i] == 0 or
               (i.bit_count() % 2 == 0 and all(v % 2 == 0 for v in degrees(i)))
               for i in range(M))
    assert sum(z != 0 for z in raw_kernel) == 512
    # Inverse transform coefficient from a separate 512-character quotient.
    even_euler = [x for x in range(M)
                  if x.bit_count() % 2 == 0 and all(v % 2 == 0 for v in degrees(x))]
    assert len(even_euler) == 512
    # Different frequencies are equivalent if they agree on every even
    # Eulerian edge vector. Orthogonality proves there are 512 classes.
    classes = {}
    for k in range(M):
        # Character signatures are encoded as Python integers (512 bits).
        signature = sum(((k & t).bit_count() % 2) << i for i, t in enumerate(even_euler))
        classes.setdefault(signature, k)
        assert w[k] == w[classes[signature]]
    assert len(classes) == 512
    reps = list(classes.values())
    quotient_kernel = {}
    for x in even_euler:
        v = sum((denominator // w[k]) * (-1 if (k & x).bit_count() % 2 else 1)
                for k in reps)
        quotient_kernel[x] = v
        assert raw_kernel[x] == 64 * v
    assert sum(abs(t) for t in quotient_kernel.values()) * 64 == sum(map(abs, raw_kernel))
    total_abs = sum(map(abs, raw_kernel))
    exact = Fraction(total_abs, denominator*M)
    assert total_abs == 362840064
    assert exact == Fraction(3691, 770)
    # Since full Fourier support, the inverse convolution kernel h has
    # multiplier 1/W, so f*h is the delta function.
    # Check this in the group algebra by evaluating the inverse at 70 shifts.
    for x in range(M):
        conv = sum(raw_kernel[x ^ f] for f in first)
        assert conv == (denominator * M if x == 0 else 0)
    print('TWO_FACTOR_K6_EXACT_PASS')
    print('factor_count=70 hamilton_cycles=60 triangle_pairs=10 frequencies=32768')
    print('walsh_histogram=' + repr(sorted(expected.items())))
    print('inverse_kernel_histogram=' + repr(sorted(expected_kernel.items())))
    print('inverse_l2_norm=1/2 inverse_l1_linf_norm=3691/770 condition_l2=35')
    print('inverse_support=512 inverse_abs_sum_raw=362840064 scale=75694080')

if __name__ == '__main__':
    main()
