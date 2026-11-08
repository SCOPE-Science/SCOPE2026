"""Exact finite checks for random-edge greedy matching after disjoint-edge deletion.

Run with Python 3: python verify.py
"""
from fractions import Fraction
from functools import lru_cache
from math import factorial, log

assertions = 0

def check(cond, message):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(message)

@lru_cache(None)
def reduced_failure(k, t):
    assert k >= 1 and 0 <= t <= k
    if k == 1:
        return Fraction(t, 1)
    den = k * k - t
    ans = Fraction(0, 1)
    if t >= 2:
        ans += Fraction(t * (t - 1), den) * reduced_failure(k - 1, t - 2)
    if 0 < t < k:
        ans += Fraction(2 * t * (k - t), den) * reduced_failure(k - 1, t - 1)
    if t < k:
        ans += Fraction((k - t) ** 2, den) * reduced_failure(k - 1, t)
    return ans


def independent_failure(n, r):
    # A separate full unmatched-vertex-subset recursion, not a (k,t) chain.
    edges = tuple((i, j) for i in range(n) for j in range(n)
                  if not (i < r and j == i))
    full = (1 << n) - 1

    @lru_cache(None)
    def rec(left, right):
        available = [(i, j) for i, j in edges
                     if (left >> i) & 1 and (right >> j) & 1]
        if not available:
            return Fraction(int(left != 0), 1)
        return sum((rec(left ^ (1 << i), right ^ (1 << j))
                    for i, j in available), Fraction(0, 1)) / len(available)
    return rec(full, full)


def exact_moments(k, t):
    den = k * k - t
    terms = []
    if t >= 2:
        terms.append((t - 2, Fraction(t * (t - 1), den)))
    if 0 < t < k:
        terms.append((t - 1, Fraction(2 * t * (k - t), den)))
    if t < k:
        terms.append((t, Fraction((k - t) ** 2, den)))
    return terms


def U(k, t):
    return Fraction(t, k * (k + 1))


def V(k, t):
    return Fraction(t * (t - 1), k * (k - 1) * (k + 1) * (k + 2))


for k in range(2, 41):
    for t in range(k + 1):
        terms = exact_moments(k, t)
        check(sum((prob for _, prob in terms), Fraction(0)) == 1,
              f'transition mass k={k},t={t}')
        eu = sum((prob * U(k - 1, q) for q, prob in terms), Fraction(0))
        wanted_u = -Fraction(2 * t * (t - 1),
                            k * (k - 1) * (k + 1) * (k * k - t))
        check(eu - U(k, t) == wanted_u,
              f'first-moment identity k={k},t={t}')
        if k >= 3:
            ev = sum((prob * V(k - 1, q) for q, prob in terms), Fraction(0))
            wanted_v = V(k, t) * (1 - Fraction(2 * (k + 2 * t - 6),
                                                 (k - 2) * (k * k - t))) if t >= 2 else 0
            check(ev == wanted_v,
                  f'second-moment identity k={k},t={t}')
            if t >= 2:
                eta = Fraction(2 * (k + 2 * t - 6),
                               (k - 2) * (k * k - t))
                check(0 <= eta <= Fraction(6, k * (k - 1)),
                      f'drift bound k={k},t={t}')

for n in range(2, 7):
    for r in range(n + 1):
        check(reduced_failure(n, r) == independent_failure(n, r),
              f'full-state verification n={n},r={r}')
        check(reduced_failure(n, r) >= 0, 'nonnegative')

for n in range(2, 31):
    harmonic = sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))
    for r in range(n + 1):
        p = reduced_failure(n, r)
        leading = Fraction(2 * r, n * (n + 1))
        v = Fraction(r * (r - 1), n * (n - 1) * (n + 1) * (n + 2))
        d = leading - p
        check(0 <= p <= 1, f'probability range n={n},r={r}')
        check(0 <= d, f'nonnegative correction n={n},r={r}')
        check(abs(d - 4 * v * (harmonic - 1)) <= 36 * v,
              f'uniform quantitative bound n={n},r={r}')
        if r <= 1:
            check(p == leading, f'one-forbidden-edge exactness n={n},r={r}')

print(f'VERIFY_OK {assertions} exact assertions')
