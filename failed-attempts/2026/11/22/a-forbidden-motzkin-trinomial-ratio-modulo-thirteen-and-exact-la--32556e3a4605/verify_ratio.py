#!/usr/bin/env python3
"""Exact integer and finite digital checks for Motzkin/trinomial ratios.

Requires Python's standard library only.  Finite checks support, but do not
replace, the all-index and all-prime arguments in RESULT.md.
"""
from collections import Counter
from fractions import Fraction


def terms(nmax):
    t = [1, 1]
    m = [1, 1]
    for n in range(2, nmax + 1):
        a = (2 * n - 1) * t[-1] + 3 * (n - 1) * t[-2]
        b = (2 * n + 1) * m[-1] + 3 * (n - 1) * m[-2]
        assert a % n == 0 and b % (n + 2) == 0
        t.append(a // n)
        m.append(b // (n + 2))
    return t, m


def digit_t(n, w, p):
    out = 1
    while n:
        out = out * w[n % p] % p
        n //= p
    return out


def data(p, t):
    w = tuple(a % p for a in t[:p])
    if 0 in w:
        return None
    assert w[0] == w[1] == 1
    assert w[-1] in (1, p - 1)
    c = pow(w[-1], -1, p)
    v = [w[j + 1] * pow(w[j], -1, p) % p for j in range(p - 1)]
    a = Counter(v)
    if c == 1:
        mu = {u: Fraction(a[u], p - 1) for u in range(1, p)}
    else:
        mu = {u: Fraction(p * a[u] + a[-u % p], p * p - 1)
              for u in range(1, p)}
    fixed = [(3 * w[d] + 2 * w[d + 1] - w[d + 2]) *
             pow(2 * w[d], -1, p) % p for d in range(p - 2)]
    f = lambda u: (3 * w[-2] + 2 * w[-1] - u) * pow(2 * w[-2], -1, p) % p
    g = lambda u: (3 * w[-1] + u) * pow(2 * w[-1], -1, p) % p
    density = [Fraction(fixed.count(r), p) +
               sum((mu[u] * (int(f(u) == r) + int(g(u) == r))
                    for u in range(1, p)), Fraction(0)) / p
               for r in range(p)]
    assert sum(mu.values()) == 1 and sum(density) == 1
    return w, v, fixed, f, g, density


T, M = terms(2500)
for n in range(2498):
    assert 2 * M[n] == 3 * T[n] + 2 * T[n + 1] - T[n + 2]
prime_count = 0
for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
    row = data(p, T)
    if row is None:
        continue
    prime_count += 1
    w, v, fixed, f, g, density = row
    for n in range(2499):
        assert digit_t(n, w, p) == T[n] % p
        assert T[n] % p != 0
        q, d = divmod(n, p)
        r = T[q + 1] * pow(T[q], -1, p) % p
        predicted = fixed[d] if d < p - 2 else (f(r) if d == p - 2 else g(r))
        assert predicted == M[n] * pow(T[n], -1, p) % p
assert prime_count >= 4

p = 13
w, v, fixed, f, g, density = data(p, T)
F = Counter(fixed)
G = Counter([f(u) for u in v] + [g(u) for u in v])
E = Counter([f(1), g(1)])
assert [F[r] for r in range(p)] == [0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 3]
assert [G[r] for r in range(p)] == [2, 2, 2, 4, 3, 0, 2, 2, 2, 2, 2, 0, 1]
assert [E[r] for r in range(p)] == [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert [156 * density[r] for r in range(p)] == [2, 26, 2, 4, 3, 24, 2, 26, 26, 2, 2, 0, 37]

# This direct enumeration uses the separate digit product and 3-term integer
# identity, NOT the f/g transition formulas or the predicted count vectors.
for k in range(1, 5):
    cnt = Counter()
    for n in range(p**k):
        t0 = digit_t(n, w, p)
        t1 = digit_t(n + 1, w, p)
        t2 = digit_t(n + 2, w, p)
        mn = (3 * t0 + 2 * t1 - t2) * pow(2, -1, p) % p
        cnt[mn * pow(t0, -1, p) % p] += 1
    for r in range(p):
        exact = p**(k - 1) * F[r] + ((p**(k - 1) - 1) // 12) * G[r] + E[r]
        assert cnt[r] == exact, (k, r, cnt[r], exact)
    assert cnt[11] == 0

print('VERIFY_OK independent_integer_terms=2501 direct_modular_ratios=all_admissible_primes')
print('prime_samples=', prime_count, 'p13_complete_power_levels=4',
      'p13_max_index=', 13**4 - 1, 'forbidden_ratio=11')
