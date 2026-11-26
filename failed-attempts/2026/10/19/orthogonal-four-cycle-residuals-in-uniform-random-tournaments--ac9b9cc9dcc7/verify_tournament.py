"""Exact finite checks for tournament cycle-count orthogonal decomposition.

Run: python3 tournament_verify.py
"""
from fractions import Fraction
from itertools import combinations, permutations
from collections import defaultdict
from math import comb


def models(n, limit=None):
    edges = list(combinations(range(n), 2))
    edge_index = {e: i for i, e in enumerate(edges)}
    triples = list(combinations(range(n), 3))
    fours = list(combinations(range(n), 4))
    cycles = []
    for s in fours:
        lead = s[0]
        for p in permutations(s[1:]):
            if p < p[::-1]:
                cycles.append((lead,) + p)

    def orientation(mask, a, b):
        if a < b:
            return (mask >> edge_index[a, b]) & 1
        return 1 - ((mask >> edge_index[b, a]) & 1)

    def x(mask, a, b):
        return 2 * orientation(mask, a, b) - 1

    def triangle(mask, a, b, c):
        return int((orientation(mask, a, b) and orientation(mask, b, c)
                    and orientation(mask, c, a)) or
                   (orientation(mask, c, b) and orientation(mask, b, a)
                    and orientation(mask, a, c)))

    def cyc4(mask, v):
        flags = [orientation(mask, v[i], v[(i + 1) % 4]) for i in range(4)]
        return int(all(flags) or not any(flags))

    moment_t, moment_q, moment_t2, moment_q2, moment_tq = (0,) * 5
    moment_z, moment_z2, moment_tz = 0, 0, 0
    count = 0
    for mask in range(min(1 << len(edges), limit or (1 << len(edges)))):
        t = sum(triangle(mask, *s) for s in triples)
        q = sum(cyc4(mask, v) for v in cycles)
        mon_sum = sum(x(mask, v[0], v[1]) * x(mask, v[1], v[2])
                      * x(mask, v[2], v[3]) * x(mask, v[3], v[0])
                      for v in cycles)
        # Multiply the identity by 8 to keep every assertion integral.
        assert 8 * q == 4 * (n-3) * t - comb(n, 4) + mon_sum
        z8 = mon_sum
        moment_t += t
        moment_q += q
        moment_t2 += t*t
        moment_q2 += q*q
        moment_tq += t*q
        moment_z += z8
        moment_z2 += z8*z8
        moment_tz += t*z8
        count += 1

    if limit is not None:
        print(f'n={n}: {count} sampled orientations; local decomposition exact')
        return

    def average(num): return Fraction(num, count)
    et,eq = average(moment_t),average(moment_q)
    vt = average(moment_t2)-et*et
    vq = average(moment_q2)-eq*eq
    cov = average(moment_tq)-et*eq
    ez8 = average(moment_z)
    vz = (average(moment_z2)-ez8*ez8)/64
    cov_tz8 = average(moment_tz)-et*ez8

    assert et == Fraction(comb(n,3), 4)
    assert eq == Fraction(3*comb(n,4),8)
    assert vt == Fraction(3*comb(n,3),16)
    assert cov == Fraction(3*comb(n,4),8)
    assert vq == Fraction(3*(4*n-11)*comb(n,4),64)
    assert ez8 == 0 and cov_tz8 == 0
    assert vz == Fraction(3*comb(n,4),64)
    print(f'n={n}: {count} tournaments; mean, variance, covariance, and chaos identities exact')


for n in (4, 5):
    models(n)
models(6, limit=1000)
print('All exact finite checks passed.')
