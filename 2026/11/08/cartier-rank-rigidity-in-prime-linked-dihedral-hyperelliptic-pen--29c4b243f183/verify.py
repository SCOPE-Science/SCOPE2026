"""Exact finite-characteristic checks for a hyperelliptic Cartier rank formula."""
from math import comb


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n ** .5) + 1))


def b_polynomials(p):
    r = (p - 1) // 2
    # The coefficient of T^k as a polynomial in the parameter a.
    b = [[0] * (r + 1) for _ in range(2 * r + 1)]
    b[0][0] = 1
    for _ in range(r):
        new = [[0] * (r + 1) for _ in range(2 * r + 1)]
        for k, poly in enumerate(b):
            for j, c in enumerate(poly):
                if c:
                    new[k][j] = (new[k][j] + c) % p
                    if k + 1 <= 2 * r and j + 1 <= r:
                        new[k + 1][j + 1] = (new[k + 1][j + 1] + c) % p
                    if k + 2 <= 2 * r:
                        new[k + 2][j] = (new[k + 2][j] + c) % p
        b = new
    return b


def evaluate(poly, a, p):
    return sum(c * pow(a, j, p) for j, c in enumerate(poly)) % p


def direct_coefficients(p, a):
    n = (p + 1) // 2
    r = n - 1
    f = {0: 1, n: a % p, 2 * n: 1}
    h = {0: 1}
    for _ in range(r):
        nxt = {}
        for i, v in h.items():
            for j, w in f.items():
                nxt[i + j] = (nxt.get(i + j, 0) + v * w) % p
        h = nxt
    return h


def rank_fp(M, p):
    a = [row[:] for row in M]
    h = len(a)
    i = 0
    for j in range(h):
        pivot = next((k for k in range(i, h) if a[k][j] % p), None)
        if pivot is None:
            continue
        a[i], a[pivot] = a[pivot], a[i]
        inv = pow(a[i][j], p - 2, p)
        a[i] = [(z * inv) % p for z in a[i]]
        for k in range(h):
            if k != i and a[k][j]:
                z = a[k][j]
                a[k] = [(u - z * v) % p for u, v in zip(a[k], a[i])]
        i += 1
    return i


def product(A, B, p):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) % p for j in range(n)] for i in range(n)]


def test_one(p):
    r = (p - 1) // 2
    n = r + 1
    b = b_polynomials(p)
    assert len(b) == 2 * r + 1
    assert all(b[j] == b[2 * r - j] for j in range(2 * r + 1))
    assert b[1][1] == r and all(b[1][j] == 0 for j in range(r + 1) if j != 1)
    for k in range(1, 2 * r, 2):
        j = min(k, 2 * r - k)
        assert b[k][j] == comb(r, j) % p
        assert all(z == 0 for z in b[k][j + 1:])
    all_a = [a for a in range(p) if (a * a - 4) % p]
    counts = {}
    for a in all_a:
        h = direct_coefficients(p, a)
        M = [[h.get(p * i - j, 0) for j in range(1, n)] for i in range(1, n)]
        target = [[evaluate(b[2 * i - 1], a, p) if j == n - i else 0
                   for j in range(1, n)] for i in range(1, n)]
        assert M == target
        expected = sum(1 for i in range(1, n) if target[i - 1][n - i - 1] != 0)
        assert rank_fp(M, p) == expected
        # For a in F_p the Frobenius-twisted product equals M^g.
        power = [[int(i == j) for j in range(r)] for i in range(r)]
        for _ in range(r):
            power = product(power, M, p)
        assert rank_fp(power, p) == expected
        assert (expected == 0) == (a == 0)
        assert a == 0 or expected >= 2
        counts[expected] = counts.get(expected, 0) + 1
    return counts


if __name__ == '__main__':
    results = {p: test_one(p) for p in range(11, 44) if is_prime(p)}
    print('VERIFY_PRIME_RIGIDITY_OK', results)
