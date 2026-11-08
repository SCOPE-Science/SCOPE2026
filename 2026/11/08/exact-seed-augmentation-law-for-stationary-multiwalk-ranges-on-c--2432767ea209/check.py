"""Exact finite verification of random-set augmentation for complete-graph walks.
Uses only the Python standard library; verification is finite, not the proof.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb


def step_distribution(n, q, t):
    """Probability for each exact visited subset, from a uniform root."""
    states = {(1 << i, i): F(1, n) for i in range(n)}
    for _ in range(t):
        nxt = defaultdict(F)
        for (mask, vertex), p in states.items():
            nxt[(mask, vertex)] += p * q
            for w in range(n):
                if w != vertex:
                    nxt[(mask | (1 << w), w)] += p * (1-q) / (n-1)
        states = dict(nxt)
    out = defaultdict(F)
    for (mask, _), p in states.items():
        out[mask] += p
    return dict(out)


def union(a, b):
    out = defaultdict(F)
    for ma, pa in a.items():
        for mb, pb in b.items():
            out[ma | mb] += pa * pb
    return dict(out)


def seed(n):
    return {1 << i: F(1, n) for i in range(n)}


def formula(n, q, k, total, mask):
    r = mask.bit_count()
    val = F()
    for j in range(r + 1):
        u = r - j
        if u == 0:
            continue
        lam = q + (1-q) * F(u-1, n-1)
        val += (-1)**j * comb(r, j) * F(u, n)**k * lam**total
    return val


def test():
    cases = 0
    for n in (2, 3, 4, 5):
        for q in (F(0), F(1, 3), F(1, 2), F(1)):
            for k in (1, 2, 3):
                for total in range(5):
                    base = step_distribution(n, q, total)
                    augmented = base
                    for _ in range(k-1):
                        augmented = union(augmented, seed(n))
                    assert sum(augmented.values()) == 1
                    # Verify every individual subset probability from the closed law.
                    for mask in range(1 << n):
                        assert augmented.get(mask, F()) == formula(n, q, k, total, mask)
                        cases += 1
                    # All weak compositions: independent walks are allowed length zero.
                    for breaks in product(range(total+1), repeat=k):
                        if sum(breaks) != total:
                            continue
                        many = {0: F(1)}
                        for steps in breaks:
                            many = union(many, step_distribution(n, q, steps))
                        assert many == augmented, (n, q, breaks)
                        cases += 1
                    # Factorial moments of uncovered labels.
                    for b in range(n+1):
                        moment = F()
                        for mask, p in augmented.items():
                            u = n-mask.bit_count()
                            if u >= b:
                                moment += p * (1 if b==0 else __import__('math').factorial(u) // __import__('math').factorial(u-b))
                            elif b==0:
                                moment += p
                        if b == n:
                            rhs = F(0)
                        else:
                            rhs = F(__import__('math').factorial(n),__import__('math').factorial(n-b)) * F(n-b,n)**k * (1-(1-q)*F(b,n-1))**total
                        assert moment == rhs,(n,q,k,total,b,moment,rhs)
                        cases += 1
    print(f'PASS {cases} exact rational comparisons')

if __name__ == '__main__':
    test()
