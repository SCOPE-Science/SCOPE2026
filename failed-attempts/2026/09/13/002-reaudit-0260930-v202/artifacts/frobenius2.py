"""Fully independent character table via Frobenius power-sum formula + independent
Hurwitz evaluation. Cross-checks char_sum.py (Murnaghan-Nakayama) value-by-value."""
import sys
sys.path.insert(0, "output/artifacts")
from fractions import Fraction
from math import factorial
from itertools import permutations
from functools import lru_cache

def char_frobenius(lam, mu):
    n = sum(mu)
    lam = tuple(lam) + (0,) * (n - len(lam))
    L = [lam[i] + n - 1 - i for i in range(n)]
    parts = tuple(mu)
    @lru_cache(maxsize=None)
    def dp(j, Ekey):
        E = list(Ekey)
        if j == len(parts):
            return 1 if all(e == 0 for e in E) else 0
        k = parts[j]
        tot = 0
        for i in range(n):
            if E[i] >= k:
                E2 = list(E)
                E2[i] -= k
                tot += dp(j + 1, tuple(E2))
        return tot
    tot = 0
    for s in permutations(range(n)):
        inv = sum(1 for a in range(n) for b in range(a + 1, n) if s[a] > s[b])
        sgn = -1 if inv % 2 else 1
        E = tuple(L[i] - (n - 1 - s[i]) for i in range(n))
        if any(e < 0 for e in E):
            continue
        tot += sgn * dp(0, tuple(E))
    return tot

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for k in range(min(max_part, n), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest

def class_size2(ct, d):
    from collections import Counter
    c = Counter(ct)
    z = 1
    for ln, m in c.items():
        z *= (ln ** m) * factorial(m)
    return factorial(d) // z

def H2(mu, nu, r):
    d = sum(mu)
    parts = list(partitions(d))
    ca = class_size2(tuple(mu), d)
    cn = class_size2(tuple(nu), d)
    ct = class_size2((2,) + (1,) * (d - 2), d)
    tot = Fraction(0)
    ndiff = 0
    for lam in parts:
        a = char_frobenius(lam, mu)
        b = char_frobenius(lam, nu)
        t = char_frobenius(lam, (2,) + (1,) * (d - 2))
        dim = char_frobenius(lam, (1,) * d)
        if dim == 0:
            continue
        tot += Fraction(a * b * (t ** r), dim ** (r))
    N = Fraction(ca * cn * (ct ** r), factorial(d)) * tot
    return Fraction(N, factorial(d)), N

if __name__ == "__main__":
    import char_sum
    # full table agreement spot-check + target values
    diffs = 0
    must = [(6, 2, 1), (5, 4), (3, 3, 3), (2,) + (1,) * 7, (1,) * 9]
    for lam in partitions(9):
        for mu in must:
            if char_sum.charval(lam, mu) != char_frobenius(lam, mu):
                diffs += 1
                print("DIFF", lam, mu)
    print("table diffs:", diffs)
    for mu, nu in [((6, 2, 1), (5, 4)), ((3, 3, 3), (5, 4))]:
        h, n = H2(list(mu), list(nu), 3)
        print(mu, nu, "H2 =", h, "N2 =", n)
