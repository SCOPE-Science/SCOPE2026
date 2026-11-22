"""Exact independent parity-transform check for cyclic period-three square avoidance.

Run: python3 checks/parity_projection.py. No third-party packages required.
"""
from itertools import product


def mul(a, b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def power(a, k):
    n = len(a)
    t = [[int(i == j) for j in range(n)] for i in range(n)]
    while k:
        if k & 1:
            t = mul(t, a)
        a = mul(a, a)
        k //= 2
    return t


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def make_small(sign):
    states = list(product((0, 1), repeat=2))
    ix = {s: i for i, s in enumerate(states)}
    m = [[0]*4 for _ in states]
    for i, s in enumerate(states):
        for b in (0, 1):
            if s + (b,) == (0, 0, 0):
                continue
            m[i][ix[(s[1], b)]] += sign if b else 1
    return m

p, q = make_small(1), make_small(-1)
r = mul(mul(q, p), p)
s = mul(mul(q, q), p)
for n in range(1, 73):
    count = tr(power(p, n)) + tr(power(q, n))
    if n % 3 == 0:
        k = n // 3
        count += 3 * (tr(power(r, k)) + tr(power(s, k)))
    assert count >= 0, (n, count)
    if n <= 17:
        brute = sum(all(tuple(bits[(i+j) % n] for j in range(3)) !=
                        tuple(bits[(i+j+3) % n] for j in range(3))
                        for i in range(n))
                    for bits in product((0, 1), repeat=n))
        assert brute == count, (n, brute, count)
    if n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18):
        print(n, count)
print('PASS: parity-projection formula through 72; brute force through 17')
