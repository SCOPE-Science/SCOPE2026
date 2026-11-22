"""Independent exact integer certificate for the cyclic fixed-period-three square restriction.

Run: python3 checks/exact_transfer.py. No third-party packages required.
"""
from itertools import product


def multiply(a, b):
    n = len(a)
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        for k, aik in enumerate(a[i]):
            if aik:
                for j, bkj in enumerate(b[k]):
                    out[i][j] += aik * bkj
    return out


def charpoly(a):
    """Monic characteristic coefficients via exact Faddeev-LeVerrier."""
    n = len(a)
    b = [[int(i == j) for j in range(n)] for i in range(n)]
    c = [1]
    for k in range(1, n + 1):
        ab = multiply(a, b)
        tr = sum(ab[i][i] for i in range(n))
        assert tr % k == 0, (k, tr)
        ck = -(tr // k)
        c.append(ck)
        for i in range(n):
            ab[i][i] += ck
        b = ab
    return c  # coefficients in descending powers of t


def poly_product(*ps):
    ans = [1]
    for p in ps:
        new = [0] * (len(ans) + len(p) - 1)
        for i, x in enumerate(ans):
            for j, y in enumerate(p):
                new[i + j] += x * y
        ans = new
    return ans  # ascending powers


states = list(product((0, 1), repeat=5))
index = {s: i for i, s in enumerate(states)}
a = [[0] * 32 for _ in states]
for i, s in enumerate(states):
    for bit in (0, 1):
        block = s + (bit,)
        if block[:3] != block[3:]:
            a[i][index[block[1:]]] += 1
assert sum(map(sum, a)) == 56

# The full periodic-point zeta polynomial as a formal series identity.
den = poly_product(
    [1, -1, -1, -1],
    [1, 1],
    [1, 0, 1],
    [1, 0, 0, -1],
    [1, 0, 0, 2, 0, 0, -1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, -1],
)
assert len(den) == 25, len(den)
coeffs = charpoly(a)
assert coeffs[:25] == den  # reciprocal coefficients of nonzero spectrum
assert coeffs[25:] == [0] * 8  # eight zero eigenvalues
print('PASS: 32-state graph, 56 edges, exact degree-24 zeta denominator')
print('denominator coefficients (ascending powers):', den)
