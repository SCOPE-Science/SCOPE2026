"""Exact arithmetic cross-checks for a level-4800 modular cusp theorem.

Only finite algebraic computations are checked; the global moduli argument is in RESULT.md.
Run: python3 modular_cusp_checker.py
"""
from collections import Counter
from math import gcd

N = 4800

def phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def mul(a, b):
    z = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i + j] += x * y
    return z


def add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) +
            (b[i] if i < len(b) else 0) for i in range(n)]


def neg(a):
    return [-v for v in a]


def power(a, k):
    z = [1]
    for _ in range(k):
        z = mul(z, a)
    return z


def truncate(a, k):
    return (a + [0] * k)[:k]


def reciprocal(a, k):
    assert a[0] == 1
    z = [1] + [0] * (k - 1)
    for n in range(1, k):
        z[n] = -sum(a[j] * z[n - j] for j in range(1, min(n + 1, len(a))))
    return z


def product_factor(v, exponent, k):
    a = [1] + [0] * (k - 1)
    if v >= k:
        return a
    a[v] = -1
    if exponent >= 0:
        return truncate(power(a, exponent), k)
    return truncate(power(reciprocal(a, k), -exponent), k)


def qproduct(exps, k):
    a = [1]
    for v, exponent in exps:
        a = truncate(mul(a, product_factor(v, exponent, k)), k)
    return truncate(a, k)

# Exact polynomial identity fixing the two elliptic branch values.
t = [0, 1]
jnum = [3125, 250, 1]
A = add(power(jnum, 3), neg([0] * 5 + [1728]))
B = mul(power([-15625, -500, 1], 2), [125, 22, 1])
assert A == B

# Independent q-expansion spot check of the classical Ramanujan eta relation.
# Both sides below are multiplied by q, to eliminate the common leading pole.
K = 16
rr_exps = []
for n in range(1, K + 1):
    residue = n % 5
    if residue in (1, 4):
        rr_exps.append((n, 1))
    elif residue in (2, 3):
        rr_exps.append((n, -1))
base = qproduct(rr_exps, K + 1)
base5 = truncate(power(base, 5), K + 1)
# R(q)^5 = q * base^5; hence q/R(q)^5 - q*R(q)^5 - 11q.
left = reciprocal(base5, K)
for n in range(1, K):
    left[n] -= (base5[n - 2] if n >= 2 else 0) + (11 if n == 1 else 0)
eta_exps = [(n, 6) for n in range(1, K + 1)] + [(5 * n, -6) for n in range(1, K // 5 + 1)]
right = qproduct(eta_exps, K)
assert left == right, (left, right)

# The Galois-orbit calculation: one base closed cusp for each divisor d|N.
# Over the t-infinity cusp (5|d), the cover splits; otherwise it adds sqrt(5).
counts = Counter()
base_geometric = 0
for d in range(1, N + 1):
    if N % d:
        continue
    g = gcd(d, N // d)
    degree = phi(g)
    base_geometric += degree
    if d % 5 == 0:
        counts[degree] += 2
    else:
        assert g & (g-1) == 0  # g is a power of two; Q(zeta_g) excludes sqrt(5)
        counts[2 * degree] += 1

assert base_geometric == 144
assert counts == Counter({1: 16, 2: 16, 4: 24, 8: 10, 16: 4})
assert sum(counts.values()) == 70
assert sum(d * n for d, n in counts.items()) == 288
assert 4800 * (3/2) * (4/3) * (6/5) // 6 == 1920
print('PASS: modular j-factorization, q-expansion, 70 cusp orbits (16 rational), 288 geometric cusps')
