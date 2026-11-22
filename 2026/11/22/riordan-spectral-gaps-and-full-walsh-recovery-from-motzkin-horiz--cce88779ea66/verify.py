"""Exact checks for Fourier multipliers of horizontal-step Motzkin profiles.

Run with Python 3 (standard library only): python verify.py
These finite checks supplement, but do not replace, the all-n proof.
"""
from collections import defaultdict
from math import comb

checks = 0


def catalan(k):
    return comb(2 * k, k) // (k + 1)


def profile_by_paths(n):
    hist = [0] * (1 << n)

    def walk(i, height, mask):
        if i == n:
            if height == 0:
                hist[mask] += 1
            return
        walk(i + 1, height + 1, mask)
        if height:
            walk(i + 1, height - 1, mask)
        walk(i + 1, height, mask | (1 << i))

    walk(0, 0, 0)
    return hist


def fwht(a):
    a = a[:]
    step = 1
    while step < len(a):
        for j in range(0, len(a), step << 1):
            for k in range(j, j + step):
                u, v = a[k], a[k + step]
                a[k], a[k + step] = u + v, u - v
        step <<= 1
    return a


def via_nonnegative_transfer(n, r):
    if r > n // 2:
        return (-1)**n * via_nonnegative_transfer(n, n - r)
    v = {0: 1}
    # B=A^2-I on the even heights: a Riordan-path transition.
    for _ in range(r):
        w = defaultdict(int)
        for h, value in v.items():
            if h == 0:
                w[2] += value
            else:
                w[h - 2] += value
                w[h] += value
                w[h + 2] += value
        v = w
    # (A+I)^(n-2r), ordinary Motzkin transfer.
    for _ in range(n - 2*r):
        w = defaultdict(int)
        for h, value in v.items():
            w[h] += value
            w[h + 1] += value
            if h:
                w[h - 1] += value
        v = w
    return v.get(0, 0)


for n in range(0, 13):
    hist = profile_by_paths(n)
    for mask, count in enumerate(hist):
        number_nonflat = n - mask.bit_count()
        expected = catalan(number_nonflat // 2) if number_nonflat % 2 == 0 else 0
        assert count == expected, (n, mask, count, expected)
        checks += 1
    actual = fwht(hist)
    radial = [via_nonnegative_transfer(n, r) for r in range(n + 1)]
    for mask, val in enumerate(actual):
        assert val == radial[mask.bit_count()], (n, mask, val)
        checks += 1
    assert actual[0] == sum(hist)
    checks += 1
    if n in (2, 3):
        assert sum(x == 0 for x in actual) == (2 if n == 2 else 6)
    else:
        assert all(x != 0 for x in actual)
    checks += 1

riordan_prefix = [1,0,1,1,3,6,15,36,91,232,603,1585,4213]
for m, expected in enumerate(riordan_prefix):
    assert via_nonnegative_transfer(2*m, m) == expected
    checks += 1

for n in range(0, 61):
    m = n // 2
    vals = [via_nonnegative_transfer(n, r) for r in range(n + 1)]
    assert all(vals[r] == (-1)**n * vals[n-r] for r in range(n+1))
    checks += n+1
    assert all(vals[r] >= vals[r+1] >= 0 for r in range(m))
    checks += 1
    if n >= 4:
        assert min(abs(x) for x in vals) == via_nonnegative_transfer(2*m, m) > 0
        checks += 1
print(f"PASS: {checks} exact assertions")
