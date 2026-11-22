"""Independent exhaustive Walsh-coefficient check for two-row injective assignments.
Run: python check_spectrum.py
"""
from itertools import product
from math import comb


def predicted(x, y):
    return sum(x) * sum(y) - sum(a * b for a, b in zip(x, y))


def direct(x, y):
    return sum(x[i] * y[j] for i in range(len(x)) for j in range(len(x)) if i != j)


def combin_zeros(n):
    z = 0
    for u in range(n + 1):
        for v in range(n + 1):
            num = (n - 2*u)*(n - 2*v) - n + 2*(u + v)
            if num % 4:
                continue
            t = num // 4
            if max(0, u + v - n) <= t <= min(u, v):
                z += comb(n, u)*comb(u, t)*comb(n-u, v-t)
    return z


for n in range(2, 9):
    z = 0
    vals = set()
    for bits in product((-1, 1), repeat=2*n):
        x, y = bits[:n], bits[n:]
        a = direct(x, y)
        assert a == predicted(x, y), (n, bits)
        vals.add(abs(a))
        z += (a == 0)
    assert z == combin_zeros(n), (n, z)
    assert (z == 0) == (n % 4 == 3)
    expected_min = 4 if n % 4 == 1 else 2
    assert min(v for v in vals if v > 0) == expected_min
    assert max(vals) == n * (n - 1)
    print(f'n={n}, zeros={z}, rank={4**n-z}, min-positive={expected_min}: PASS')
print('exhaustive Walsh verification passed')
