"""Reproducible finite-level checks for reciprocal-progression pair sums.

Requires Python 3 only. Finite checks corroborate, but cannot replace the
analytic all-prime, all-depth proof in RESULT.md.
"""
from collections import Counter


def pair_value(n, modulus, c, d):
    s = e = 0
    for j in range(n):
        u = pow(c + d*j, -1, modulus)
        e = (e + s*u) % modulus
        s = (s + u) % modulus
    return e


def derivative_at(n, p, r, c, d):
    step = p**r
    mod = step*step
    difference = (pair_value(n + step, mod, c, d)
                  - pair_value(n, mod, c, d)) % mod
    assert difference % step == 0
    return difference//step


def critical_value(p, k, c, d):
    root = pow(2, -1, p)
    assert derivative_at(root, p, 1, c, d) % p == 0
    for r in range(1, k):
        possibilities = [root + t*p**r for t in range(p)
                         if derivative_at(root + t*p**r, p, r+1, c, d) % p**(r+1) == 0]
        assert len(possibilities) == 1, (p, k, possibilities)
        root = possibilities[0]
    return root, pair_value(root, p**k, c, d)


def check_case(p, k, c, d):
    assert p in (3, 5, 7, 11) and c % p and d % p == 0
    m = p**k
    root, center = critical_value(p, k, c, d)
    inv = pow(2*c*c, -1, m)
    sq_hist = Counter((center + inv*j*j) % m for j in range(m))
    hist = Counter()
    s = e = 0
    for n in range(m):
        hist[e] += 1
        u = pow(c + d*n, -1, m)
        e = (e + s*u) % m
        s = (s + u) % m
    assert hist == sq_hist, (p,k,len(hist),len(sq_hist))
    expected_support = 1 + sum((p-1)*p**(k-2*j-1)//2
                                for j in range((k-1)//2+1))
    assert len(hist) == expected_support
    assert hist[center] == p**(k//2)
    assert center % p == (-pow(8*c*c, -1, p)) % p
    for y, cnt in hist.items():
        delta = (y - center) % m
        if not delta:
            assert cnt == p**(k//2)
        else:
            v = 0
            while delta % p == 0:
                v += 1
                delta //= p
            assert v % 2 == 0
            assert cnt == 2*p**(v//2)
    # A shift by p^k is a period, but no smaller power is.
    x = 0
    # At least one of x=0 or x=1 avoids the unique cancelling residue.
    for r in range(k):
        t = p**r
        diffs = [(pair_value(x+t, m, c, d)-pair_value(x, m, c, d))%m for x in (0,1)]
        assert any(v % p**(r+1) != 0 for v in diffs), (p,k,r,diffs)
    print(f'PASS p={p} c={c} d={d} k={k} root={root} center={center} '
          f'image={len(hist)} tested_indices={m} histogram_total={sum(hist.values())}')


if __name__ == '__main__':
    for args in [(3,4,1,3),(3,5,1,3),(3,4,2,6),(5,3,1,5),
                 (5,4,1,5),(5,3,2,10),(7,3,1,7),(7,3,2,14),(11,2,3,11)]:
        check_case(*args)
    print('PASS all nine complete modular enumerations')
