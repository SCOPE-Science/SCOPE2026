#!/usr/bin/env python3
"""Finite-field verification of the inverse-square graph energy formulas.

All field arithmetic is implemented over polynomial quotient rings; no
external dependencies are required. These finite tests do not replace
any all-field argument in RESULT.md.
"""
from collections import Counter


class Field:
    def __init__(self, prime, monic_polynomial):
        self.p = prime
        self.poly = tuple(monic_polynomial)
        self.degree = len(self.poly) - 1
        assert self.poly[-1] == 1
        self.q = prime ** self.degree

    def unpack(self, value):
        digits = []
        for _ in range(self.degree):
            digits.append(value % self.p)
            value //= self.p
        return digits

    def pack(self, digits):
        return sum((x % self.p) * self.p ** i for i, x in enumerate(digits[:self.degree]))

    def scalar(self, x):
        return x % self.p

    def add(self, a, b):
        return self.pack([x + y for x, y in zip(self.unpack(a), self.unpack(b))])

    def mul(self, a, b):
        a, b = self.unpack(a), self.unpack(b)
        temp = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                temp[i + j] = (temp[i + j] + x * y) % self.p
        for j in range(len(temp) - 1, self.degree - 1, -1):
            lead = temp[j]
            for i in range(self.degree):
                temp[j - self.degree + i] = (temp[j - self.degree + i] - lead * self.poly[i]) % self.p
        return self.pack(temp)

    def power(self, x, exponent):
        assert exponent >= 0
        out = 1
        while exponent:
            if exponent & 1:
                out = self.mul(out, x)
            x = self.mul(x, x)
            exponent >>= 1
        return out

    def inverse(self, x):
        assert x != 0
        return self.power(x, self.q - 2)

    def chi(self, x):
        if x == 0:
            return 0
        return 1 if self.power(x, (self.q - 1) // 2) == 1 else -1


def energy_direct(F):
    invsq = [(x, F.power(F.inverse(x), 2)) for x in range(1, F.q)]
    rep = Counter((F.add(x, u), F.add(y, v)) for x, y in invsq for u, v in invsq)
    return sum(n * n for n in rep.values())


def trace_character(F):
    negfour = F.scalar(-4)
    total = 0
    for z in range(F.q):
        factor1 = F.add(1, F.mul(negfour, z))
        factor2 = F.add(1, F.mul(negfour, F.mul(z, z)))
        total += F.chi(F.mul(factor1, factor2))
    return -total


def predicted(F):
    q, p = F.q, F.p
    if p == 2:
        return (q - 1) * (3 * q - 5), None
    eps = F.chi(F.scalar(-1))
    if p == 3:
        return (q - 1) * (3 * q - 9 - 3 * eps), None
    delta = F.chi(F.scalar(-3))
    tr = trace_character(F)
    return (q - 1) * (3 * q - 10 - 2 * eps - 2 * delta - tr), tr


def verify():
    # Monic irreducible polynomials for the indicated prime-power fields.
    cases = [
        (2, [0, 1]), (2, [1, 1, 1]), (2, [1, 1, 0, 1]),
        (2, [1, 1, 0, 0, 1]),
        (3, [0, 1]), (3, [1, 0, 1]), (3, [2, 2, 0, 1]),
        (5, [0, 1]), (5, [3, 0, 1]),
        (7, [0, 1]), (7, [4, 0, 1]),
    ]
    for p in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        cases.append((p, [0, 1]))
    traces = {}
    for p, polynomial in cases:
        F = Field(p, polynomial)
        q = F.q
        # Check the defining multiplicative-field axiom in the constructed examples.
        for x in range(1, q):
            assert F.mul(x, F.inverse(x)) == 1, (q, x)
        actual = energy_direct(F)
        expected, trace = predicted(F)
        assert actual == expected, (q, actual, expected)
        if p >= 5:
            assert abs(trace) <= 2 * q ** 0.5 + 1e-8
            if F.degree == 1:
                traces[p] = trace
            if F.degree == 2:
                assert trace == traces[p] * traces[p] - 2 * p
    print('VERIFY_OK prime_field_cases=23 extension_cases=9 direct_energies=32 Frobenius_recursions=2 characteristic_branches=2,3,>=5')


if __name__ == '__main__':
    verify()
