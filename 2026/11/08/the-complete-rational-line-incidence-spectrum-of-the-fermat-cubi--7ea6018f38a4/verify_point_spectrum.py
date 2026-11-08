#!/usr/bin/env python3
"""Exact projective-point and geometric 27-line multiplicity checks.

For the indicated finite fields, no external libraries are required.
Run: python verify_point_spectrum.py
"""
from itertools import product
from collections import Counter

MATCHINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))

class FiniteField:
    def __init__(self, size, binary_polynomial=None):
        self.n = size
        if binary_polynomial is None:
            self.add = lambda a, b: (a + b) % size
            self.mul = lambda a, b: (a * b) % size
            self.neg = lambda a: (-a) % size
        else:
            self.add = lambda a, b: a ^ b
            self.neg = lambda a: a
            degree = binary_polynomial.bit_length() - 1
            def mul(a, b):
                result = 0
                while b:
                    if b & 1:
                        result ^= a
                    b >>= 1
                    a <<= 1
                    if a & (1 << degree):
                        a ^= binary_polynomial
                return result
            self.mul = mul
    def power(self, x, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = self.mul(result, x)
            x = self.mul(x, x)
            exponent >>= 1
        return result
    def roots_for_pair(self, x, y):
        # Count cube roots alpha of 1, even those outside this field,
        # satisfying x + alpha*y = 0 in an algebraic closure.
        if y == 0:
            return 3 if x == 0 else 0
        alpha = self.mul(self.neg(x), self.power(y, self.n - 2))
        return 1 if self.power(alpha, 3) == 1 else 0
    def multiplicity(self, point):
        return sum(self.roots_for_pair(point[i], point[j]) *
                   self.roots_for_pair(point[k], point[l])
                   for ((i, j), (k, l)) in MATCHINGS)
    def point_spectrum(self):
        spectrum = Counter()
        for pivot in range(4):
            for leading in product(range(self.n), repeat=pivot):
                point = leading + (1,) + (0,) * (3 - pivot)
                total = 0
                for coordinate in point:
                    total = self.add(total, self.power(coordinate, 3))
                if total == 0:
                    spectrum[self.multiplicity(point)] += 1
        return dict(sorted(spectrum.items()))

def expected(q):
    if q % 3 == 1:
        if q % 2 == 0:
            return {0:(q-4)*(q-16),1:27*(q-4),2:0,3:45}
        return {0:(q-7)*(q-13),1:27*(q-7),2:81,3:18}
    if q % 2 == 0:
        return {0:q*(q-2),1:3*(q-2),2:0,3:7}
    return {0:(q-1)**2,1:3*(q-3),2:3,3:6}

TESTS = ((2,None), (4,0b111), (8,0b1011), (16,0b10011),
         (5,None), (7,None), (11,None), (13,None), (19,None), (31,None))
for q, polynomial in TESTS:
    spectrum = FiniteField(q, polynomial).point_spectrum()
    prediction = {k:v for k,v in expected(q).items() if v}
    assert spectrum == prediction, (q, spectrum, prediction)
    print('OK', q, spectrum)
print('Exact finite-field point-spectrum tests: PASS')
