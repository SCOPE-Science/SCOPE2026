"""Exact independent checks for greedy matching on an off-diagonal square board.
No external dependencies; Python 3.9+.  This is finite verification, not the infinite proof.
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial
from itertools import permutations

@lru_cache(None)
def lumped_failure(m, t):
    assert 0 <= t <= m
    if m == 1:
        return Fraction(t, 1)
    den = m * m - t
    total = Fraction()
    if t >= 2:
        total += Fraction(t * (t - 1), den) * lumped_failure(m - 1, t - 2)
    if t and m > t:
        total += Fraction(2 * t * (m - t), den) * lumped_failure(m - 1, t - 1)
    if m > t:
        total += Fraction((m - t) ** 2, den) * lumped_failure(m - 1, t)
    return total

# An independent labeled-state recursion, not using the t-transition formula.
@lru_cache(None)
def labeled_failure(row_mask, col_mask):
    rows = [i for i in range(row_mask.bit_length()) if row_mask >> i & 1]
    cols = [j for j in range(col_mask.bit_length()) if col_mask >> j & 1]
    assert len(rows) == len(cols)
    edges = [(i,j) for i in rows for j in cols if i != j]
    if not edges:
        return Fraction(int(len(rows) == 1 and rows[0] == cols[0]), 1)
    return sum((labeled_failure(row_mask ^ (1 << i), col_mask ^ (1 << j))
                for i,j in edges), Fraction()) / len(edges)


def derangements(n):
    return sum((Fraction((-1)**k * factorial(n), factorial(k))
                for k in range(n+1)), Fraction())


def uniform_maximal_failure(n):
    d0, d1 = derangements(n), derangements(n-1)
    return n*d1 / (d0 + n*d1)


def state_distribution(n):
    # m=n distribution consists solely of t=n
    dist = {n: Fraction(1)}
    yield n, dist
    for m in range(n, 1, -1):
        nxt = {}
        for t, prob in dist.items():
            z = m*m - t
            for killed, count in [(2,t*(t-1)), (1,2*t*(m-t)), (0,(m-t)**2)]:
                if count:
                    nxt[t-killed] = nxt.get(t-killed, Fraction()) + prob * Fraction(count,z)
        dist = nxt
        yield m-1, dist


def run():
    tests = 0
    for n in range(2, 9):
        full = (1 << n) - 1
        assert labeled_failure(full,full) == lumped_failure(n,n)
        tests += 1
    assert lumped_failure(3,3) == Fraction(1,3)
    assert lumped_failure(4,4) == Fraction(4,21)
    assert lumped_failure(5,5) == Fraction(4,21)
    tests += 3
    for n in range(3, 31):
        p = lumped_failure(n,n)
        assert 0 < p < Fraction(2,n+1)
        assert 0 < uniform_maximal_failure(n) < 1
        tests += 2
    for n in range(3, 19):
        d = dict(state_distribution(n))
        assert sum(d[2].values(),Fraction()) == 1
        assert lumped_failure(n,n) == d[2].get(1,Fraction()) / 3
        for m, law in d.items():
            assert sum(law.values(),Fraction()) == 1
            if m >= 2:
                v = sum((t*(t-1)*mass for t,mass in law.items()), Fraction())
                # The bounded-factorial-moment inequality used in the proof.
                assert v * n * (n-1) <= 5*m*m*(m-1)*(m-1)
                tests += 1
        tests += 3
    for n in range(3, 45):
        p = lumped_failure(n,n)
        h = sum((Fraction(1,k) for k in range(3,n+1)),Fraction())
        assert 0 <= Fraction(2,n+1)-p <= Fraction(20,n*(n-1))*h + Fraction(20,3*n*(n-1))
        tests += 1
    # Independent permutation enumeration for maximal perfect and one-defect matchings.
    for n in range(3, 7):
        labels = tuple(range(n))
        perfect = sum(all(i != j for i,j in zip(labels, perm))
                      for perm in permutations(labels))
        short = 0
        for leave in labels:
            other = tuple(i for i in labels if i != leave)
            short += sum(all(i != j for i,j in zip(other, perm))
                         for perm in permutations(other))
        assert perfect == derangements(n)
        assert short == n*derangements(n-1)
        tests += 2
    # The uniform-maximal counting asymptotic follows from derangements,
    # with finite values checking definitions.
    for n in range(3, 15):
        assert uniform_maximal_failure(n) == Fraction(n*derangements(n-1), derangements(n)+n*derangements(n-1))
        tests += 1
    print(f'PASS: {tests} independent rational checks; n=3..8 labeled-state replay.')
    print('Selected greedy failure probabilities:')
    for n in [3,4,5,6,10,20,40]:
        print(n, str(lumped_failure(n,n)), float(lumped_failure(n,n)))
if __name__ == '__main__':
    run()
