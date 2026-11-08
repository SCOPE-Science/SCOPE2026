"""Finite checks for the semi-Pell/semi-Fibonacci comparison."""
from functools import lru_cache
from math import log

N = 1 << 18
sf = [0] * N
sp = [0] * N
sf[0] = sf[1] = sp[1] = 1
for n in range(2, N):
    if n % 2 == 0:
        sf[n] = sf[n // 2]
        sp[n] = sp[n // 2]
    else:
        sf[n] = sf[n-1] + sf[n-2]
        sp[n] = 2*sp[n-1] + sp[n-2]

@lru_cache(maxsize=None)
def by_support(n, j):
    if n == 0:
        return {0: 1}
    if (1 << j) > n:
        return {}
    # Either level j is unused, or used an odd positive number of times.
    ret = dict(by_support(n, j + 1))
    q = 1
    while q * (1 << j) <= n:
        for k, v in by_support(n - q * (1 << j), j + 1).items():
            ret[k + 1] = ret.get(k + 1, 0) + v
        q += 2
    return ret

for n in range(1, 130):
    c = by_support(n, 0)
    assert sum(c.values()) == sf[n], (n, c, sf[n])
    assert sum((1 << (k-1))*v for k, v in c.items()) == sp[n], (n, c, sp[n])

for m in range(5, 18):
    n = (1 << m) - 1
    q = sp[n] / sf[n]
    assert 1 <= q <= (1 << m)
    print(f'm={m:2d} n={n:6d} sf={sf[n]} sp={sp[n]} relative_log_exponent={(log(sp[n])-log(sf[n]))/log(n):.6f}')

# The lower-bound construction is purely combinatorial; verify its conditions
# at representative m, without using this finite test to prove the limit.
for m in (16, 20, 30, 60, 120, 300):
    h = m - (2*m.bit_length() + 4)
    if h < 1: continue
    for j in range(1, h + 1):
        L = (1 << (m - j)) // (2*m)
        assert L >= 2
        assert (L + 1)//2 >= (1 << (m-j)) / (8*m)
    assert h < m
print('PASS: independent support enumerations, recurrences, and finite sanity checks')
