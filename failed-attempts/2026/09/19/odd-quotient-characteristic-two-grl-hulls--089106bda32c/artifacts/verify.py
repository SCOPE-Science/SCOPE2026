"""Finite sanity checks for the odd-quotient characteristic-two GRL hull theorem."""

from math import gcd
from random import Random


class GF2m:
    def __init__(self, m, modulus):
        self.m = m
        self.modulus = modulus
        self.q = 1 << m
        self.mask = self.q - 1
        # Frobenius sanity check for the chosen irreducible polynomial.
        for a in range(self.q):
            assert self.pow(a, self.q) == a

    def mul(self, a, b):
        out = 0
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & self.q:
                a ^= self.modulus
        return out & self.mask

    def pow(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n >>= 1
        return out

    def inv(self, a):
        assert a != 0
        return self.pow(a, self.q - 2)


def rank(matrix, field):
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rr = 0
    for c in range(cols):
        pivot = next((i for i in range(rr, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        inv = field.inv(a[rr][c])
        a[rr] = [field.mul(x, inv) for x in a[rr]]
        for i in range(rows):
            if i != rr and a[i][c]:
                t = a[i][c]
                a[i] = [x ^ field.mul(t, y) for x, y in zip(a[i], a[rr])]
        rr += 1
        if rr == rows:
            break
    return rr


def lagrange_coefficients(points, field):
    out = []
    for i, x in enumerate(points):
        prod = 1
        for j, y in enumerate(points):
            if i != j:
                prod = field.mul(prod, x ^ y)
        out.append(field.inv(prod))
    return out


def generator(points, multipliers, k, s, extension, field):
    g = []
    for t in range(k):
        row = [field.mul(multipliers[j], field.pow(points[j], t))
               for j in range(len(points))]
        row += [0] * s if t < k - s else extension[t - k + s][:]
        g.append(row)
    return g


def hull_dimension(g, ell, field):
    frob = 1 << ell
    k = len(g)
    length = len(g[0])
    gram = []
    for i in range(k):
        row = []
        for j in range(k):
            value = 0
            for c in range(length):
                value ^= field.mul(g[i][c], field.pow(g[j][c], frob))
            row.append(value)
        gram.append(row)
    return k - rank(gram, field)


def check_case(e, ell, modulus, lengths):
    field = GF2m(e, modulus)
    q = field.q
    exponent = (1 << ell) + 1
    assert (e // gcd(e, ell)) % 2 == 1
    assert gcd(exponent, q - 1) == 1
    inverse_exponent = pow(exponent, -1, q - 1)
    rng = Random(20260919 + 100 * e + ell)
    checks = 0

    for n in lengths:
        if n > q:
            continue
        for _ in range(4):
            points = rng.sample(range(q), n)
            u = lagrange_coefficients(points, field)
            roots = [field.pow(x, inverse_exponent) for x in u]
            assert all(field.pow(v, exponent) == x for v, x in zip(roots, u))
            max_k = (n + (1 << ell) - 1) // exponent

            for s in (1, 2):
                if max_k <= s:
                    continue
                while True:
                    extension = [[rng.randrange(q) for _ in range(s)] for __ in range(s)]
                    if rank(extension, field) == s:
                        break
                beta = next(x for x in range(2, q) if field.pow(x, exponent) != 1)

                for k in range(s + 1, max_k + 1):
                    for h in range(k - s + 1):
                        z = k - s - h
                        multipliers = roots[:]
                        for i in range(z):
                            multipliers[i] = field.mul(beta, multipliers[i])
                        g = generator(points, multipliers, k, s, extension, field)
                        assert hull_dimension(g, ell, field) == h
                        checks += 1
    return checks


# Arithmetic identity over a wider exponent range.
for e in range(2, 25):
    for ell in range(1, e):
        d = gcd(e, ell)
        if (e // d) % 2 == 1:
            assert gcd((1 << ell) + 1, (1 << e) - 1) == 1
print("gcd identity: PASS for e < 25")

# x^5+x^2+1 and x^6+x+1 are irreducible over F_2.
cases = [
    (5, 1, 0b100101, [8, 12, 20, 32]),
    (5, 2, 0b100101, [12, 16, 24, 32]),
    (6, 2, 0b1000011, [12, 20, 32, 64]),
]
for case in cases:
    count = check_case(*case)
    print(f"(e, ell)=({case[0]}, {case[1]}): {count} hull checks PASS")
print("ALL CHECKS PASS")
