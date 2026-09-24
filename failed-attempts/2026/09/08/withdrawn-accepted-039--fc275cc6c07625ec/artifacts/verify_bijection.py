"""Bijection audit: LIS over 231-avoiders equals Dyck-peak counts (Narayana), all n<=10.

Checks on EVERY generated object:
  (a) Catalan structural decomposition holds (pos of max n splits values L<R);
  (b) recursive Dyck image D(pi)="U"+D(Rstd)+"D"+D(L) is a valid Dyck word;
  (c) LIS(pi) == peaks(D(pi));
  (d) images are distinct and count == Catalan (hence bijection onto Dyck_n);
  (e) LIS histogram == Narayana closed form C(n,k)C(n,k-1)/n;
  (f) extremal uniqueness: exactly one perm attains LIS=n and one attains des=0;
  (g) descents+1 histogram == Narayana row (finite verified observation).
Standalone (no import of census.py, which has top-level side effects).
"""
import bisect
from collections import Counter
from math import comb


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def narayana(n, k):
    return comb(n, k) * comb(n, k - 1) // n


def gen231(n):
    if n == 0:
        yield ()
        return
    for k in range(1, n + 1):
        for L in gen231(k - 1):
            for R in gen231(n - k):
                Rshift = tuple(x + (k - 1) for x in R)
                yield L + (n,) + Rshift


def lis_patience(p):
    piles = []
    for x in p:
        i = bisect.bisect_left(piles, x)
        if i == len(piles):
            piles.append(x)
        else:
            piles[i] = x
    return len(piles)


def descents(p):
    return sum(1 for i in range(len(p) - 1) if p[i] > p[i + 1])


def dyck(pi):
    if not pi:
        return ""
    n = len(pi)
    assert max(pi) == n, pi
    i = pi.index(n)
    L, R = pi[:i], pi[i + 1:]
    assert set(L) == set(range(1, i + 1)), (pi, L)          # structural lemma audit
    assert set(R) == set(range(i + 1, n)), (pi, R)          # values(L) < values(R)
    Rstd = tuple(x - i for x in R)
    return "U" + dyck(Rstd) + "D" + dyck(L)


def is_dyck(w):
    bal = 0
    for c in w:
        bal += 1 if c == "U" else -1
        if bal < 0:
            return False
    return bal == 0


def peaks(w):
    return sum(1 for i in range(len(w) - 1) if w[i] == "U" and w[i + 1] == "D")


for n in range(1, 11):
    dist = Counter()
    ddes = Counter()
    images = set()
    total = 0
    n_maxlis = 0
    n_mindes = 0
    for p in gen231(n):
        total += 1
        a = lis_patience(p)
        w = dyck(p)
        assert len(w) == 2 * n and is_dyck(w), (p, w)
        assert a == peaks(w), (p, w, a)
        images.add(w)
        dist[a] += 1
        d = descents(p)
        ddes[d + 1] += 1
        if a == n:
            n_maxlis += 1
            assert p == tuple(range(1, n + 1)), p
        if d == 0:
            n_mindes += 1
            assert p == tuple(range(1, n + 1)), p
    row = {k: narayana(n, k) for k in range(1, n + 1)}
    assert total == catalan(n), (n, total)
    assert len(images) == total == catalan(n), (n, len(images), total)  # bijection
    assert dict(dist) == row, (n, dict(dist), row)                     # LIS = Narayana
    assert dict(ddes) == row, (n, dict(ddes), row)                     # des+1 = Narayana
    assert n_maxlis == 1 and n_mindes == 1, (n, n_maxlis, n_mindes)     # unique extrema
    print(f"n={n}: C={total} LIS==peaks==Narayana {dict(sorted(dist.items()))} "
          f"des+1 OK unique-maxLIS unique-mindes OK")
print("ALL BIJECTION + NARAYANA CHECKS PASS (n=1..10)")
