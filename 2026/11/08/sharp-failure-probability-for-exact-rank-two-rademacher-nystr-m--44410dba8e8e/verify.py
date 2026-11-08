"""Exact finite-case checks for sharp Rademacher rank-two sketch recovery.

Python >=3.9, standard library only. This program checks finite samples;
the dimension-free assertion follows from the accompanying mathematical proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
import random

CHECKS = 0

def check(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)


def full_row_rank(B):
    a, b = B
    return any(a[i] * b[j] != a[j] * b[i]
               for i in range(len(a)) for j in range(i + 1, len(a)))


def projective_key(x, y):
    if x == 0 and y == 0:
        return None
    g = gcd(abs(x), abs(y))
    u, v = x // g, y // g
    if u < 0 or (u == 0 and v < 0):
        u, v = -u, -v
    return (u, v)


def masses(B):
    n = len(B[0])
    C = Counter()
    for eps in product((-1, 1), repeat=n):
        x = sum(a * e for a, e in zip(B[0], eps))
        y = sum(a * e for a, e in zip(B[1], eps))
        C[projective_key(x, y)] += 1
    return C, 1 << n


def failure_fraction(B, m):
    C, N = masses(B)
    z = C.get(None, 0)
    total = z ** m
    for key, count in C.items():
        if key is not None:
            total += (z + count) ** m - z ** m
    return Fraction(total, N ** m)


def sharp_bound(m):
    return Fraction(3, 2 ** m) - Fraction(2, 4 ** m)


def direct_failure(B, m):
    n = len(B[0]); points = []
    for eps in product((-1, 1), repeat=n):
        points.append((sum(v * e for v, e in zip(B[0], eps)),
                       sum(v * e for v, e in zip(B[1], eps))))
    count = 0
    for chosen in product(points, repeat=m):
        if all(p[0]*q[1] == p[1]*q[0] for p in chosen for q in chosen):
            count += 1
    return Fraction(count, len(points)**m)


def run():
    witness = [[1, 1, 0], [1, 0, 1]]
    for m in range(2, 12):
        check(failure_fraction(witness, m) == sharp_bound(m),
              'sharp witness mismatch')
    C, N = masses(witness)
    check(N == 8 and C[None] == 2 and sorted(v for k,v in C.items() if k is not None) == [2,2,2],
          'witness projective masses')
    for m in (2, 3, 4):
        check(direct_failure(witness, m) == failure_fraction(witness, m),
              'independent direct tuple count differs')
    for n in (2, 3, 4):
        rank_two = 0
        for entries in product((-1, 0, 1), repeat=2*n):
            B = [entries[:n], entries[n:]]
            if not full_row_rank(B):
                continue
            rank_two += 1
            C, N = masses(B)
            z = C.get(None, 0)
            check(Fraction(z,N) <= Fraction(1,4) if n >= 3 else z == 0,
                  'zero mass bound')
            for key, count in C.items():
                if key is not None:
                    check(2*(z+count) <= N, 'line anti-concentration')
            for m in (2,3,4,6):
                F = failure_fraction(B,m)
                check(F <= sharp_bound(m), 'global bound counterexample')
                if n == 2:
                    check(F == Fraction(2,2**m), 'full rank plane exact law')
        check(rank_two > 0, 'no full rank matrices')
        print(f'exhaustive integer 2x{n} rank-two configurations: {rank_two}')
    rng = random.Random(13057)
    for n in (5,6,7):
        for _ in range(300):
            B = [[rng.randrange(-4,5) for _ in range(n)] for _ in range(2)]
            if not full_row_rank(B): continue
            for m in (2,3,4,7,10):
                check(failure_fraction(B,m) <= sharp_bound(m), 'random sign failure')
    print('CHECKS_PASSED', CHECKS)
    print('WITNESS_FAILURE_m2', failure_fraction(witness, 2))
    print('WITNESS_FAILURE_m3', failure_fraction(witness, 3))
    print('WITNESS_FAILURE_m4', failure_fraction(witness, 4))
    print('FULL_RANK_TWO_DIM_m2', failure_fraction([[1,0],[0,1]],2))

if __name__ == '__main__':
    run()
