"""Exact small-order cross-checks for uniform-edge dimer adsorption on a clique with one exceptional vertex.

Run with Python 3.9+ using only the standard library. This is an independent
finite consistency test, not a proof of the asymptotic statement.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, exp, log

checks = 0


def symmetry_recursion(N):
    """Probability of two unmatched vertices for each exceptional degree d."""
    global checks
    assert N % 2 == 0 and N >= 2
    p = [Fraction(1), Fraction(0)]  # k=1, degree a=0 or 1
    for k in range(3, N, 2):
        q = comb(k, 2)
        new = []
        for a in range(k + 1):
            b = k - a
            num = (comb(a, 2) * (p[a-2] if a >= 2 else 0)
                   + a*b * (p[a-1] if 0 <= a-1 < len(p) else 0)
                   + comb(b, 2) * (p[a] if a < len(p) else 0))
            new.append(num / (q + a))
        p = new
    return p


def full_graph_recursion(N, d):
    """Independent exhaustive recursion over actual labeled free-vertex sets."""
    ordinary = N - 1
    full = (1 << N) - 1

    @lru_cache(None)
    def prob(mask):
        free = [i for i in range(N) if mask & (1 << i)]
        choices = []
        for i, v in enumerate(free):
            for w in free[i+1:]:
                if v == ordinary or w == ordinary:
                    neighbor = w if v == ordinary else v
                    if neighbor >= d:
                        continue
                choices.append((v, w))
        if not choices:
            assert len(free) in (0, 2)
            return Fraction(int(len(free) == 2))
        return sum((prob(mask & ~(1 << v) & ~(1 << w)) for v, w in choices), Fraction()) / len(choices)
    return prob(full)


def permutation_shadow_formula(N, d):
    """Independent exact average over all choices of the neighbor ranks."""
    m = N-1
    ans = Fraction()
    for subset in combinations(range(1, m+1), d):
        if 1 in subset:
            continue
        s = set(subset)
        weight = Fraction(1)
        for k in range(3, m+1, 2):
            a = sum(r <= k for r in s)
            q = comb(k, 2)
            weight *= Fraction(q, q+a)
        ans += weight
    return ans / comb(m, d)


for N in (4, 6, 8, 10, 12):
    p = symmetry_recursion(N)
    for d in range(N):
        got = full_graph_recursion(N, d)
        assert got == p[d], (N, d, got, p[d])
        checks += 1
        got2 = permutation_shadow_formula(N, d)
        assert got2 == p[d], (N, d, got2, p[d])
        checks += 1
    assert p[0] == 1 and p[-1] == 0
    checks += 2


def float_recursion(N):
    p = [1.0, 0.0]
    for k in range(3, N, 2):
        q = k*(k-1)/2
        next_p = [0.0]*(k+1)
        for a in range(k+1):
            b = k-a
            num = ((a*(a-1)/2*p[a-2] if a >= 2 else 0.0)
                   + (a*b*p[a-1] if 0 < a <= len(p) else 0.0)
                   + (b*(b-1)/2*p[a] if a < len(p) else 0.0))
            next_p[a] = num/(q+a)
        p = next_p
    return p

# Non-asymptotic diagnostics at the scaling predicted by the theorem.
for N in (200, 400, 800, 1600):
    p = float_recursion(N)
    for c in (0.5, 1.0, 2.0):
        d = round(c * (N-1) / log(N))
        assert abs(p[d] - exp(-c)) < 0.04
        checks += 1
        print('N', N, 'c', c, 'degree', d, 'probability', format(p[d], '.9f'))
print('ALL CHECKS PASSED:', checks)
