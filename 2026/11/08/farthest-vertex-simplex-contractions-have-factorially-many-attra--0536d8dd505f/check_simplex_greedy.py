"""Exact rational supporting tests for a farthest-vertex simplex contraction.

Run: python3 check_simplex_greedy.py
These finite checks supplement, rather than replace, the analytic proof.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import ceil, log, factorial
import random


def advance(x, lam):
    j = min(range(len(x)), key=lambda i: (x[i], i))
    return tuple(lam * a + (1 - lam if i == j else 0) for i, a in enumerate(x)), j


def sorted_fixed(n, lam):
    c = (1 - lam) / (1 - lam**n)
    return tuple(c * lam**(n - 1 - i) for i in range(n))


def uniform_bound(n, lam):
    delta = (1 - lam)**2 * lam**(n - 2) / (1 - lam**n)
    t = 0
    while lam**t >= delta / 4:
        t += 1
    return t


def run():
    checks = 0
    R = random.Random(20241102)
    for n in range(3, 8):
        for lam in (Q(1, 4), Q(1, 2), Q(2, 3), Q(4, 5)):
            s = sorted_fixed(n, lam)
            assert sum(s) == 1 and all(s[i] < s[i+1] for i in range(n-1))
            checks += 2
            ys, _ = advance(s, lam)
            assert tuple(sorted(ys)) == s
            checks += 1
            sample_perms = list(permutations(range(n))) if n <= 5 else [tuple(R.sample(range(n), n)) for _ in range(70)]
            for p in sample_perms:
                x = tuple(s[p[i]] for i in range(n))
                x0 = x
                symbols = []
                for step in range(n):
                    x, j = advance(x, lam)
                    symbols.append(j)
                assert x == x0
                assert len(set(symbols)) == n
                checks += 2
            t = uniform_bound(n, lam)
            for trial in range(30):
                if trial == 0:
                    x = tuple(Q(1, n) for _ in range(n))
                elif trial == 1:
                    x = (Q(1),) + tuple(Q(0) for _ in range(n-1))
                else:
                    z = [R.randrange(1, 100) for _ in range(n)]
                    x = tuple(Q(a, sum(z)) for a in z)
                for step in range(t):
                    x, _ = advance(x, lam)
                assert len(set(x)) == n
                checks += 1
                prev = None
                indices = []
                for k in range(2*n):
                    j = min(range(n),key=lambda i:(x[i],i))
                    x_new, _ = advance(x, lam)
                    assert x_new[j] == max(x_new) and sum(x_new) == 1
                    checks += 2
                    x = x_new
                    indices.append(j)
                assert indices[n:] == indices[:n] and len(set(indices[:n])) == n
                checks += 1
    print('PASS', checks, 'exact-rational assertions')

if __name__ == '__main__':
    run()
