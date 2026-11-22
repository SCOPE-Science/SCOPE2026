"""Exact independent finite-field checks for a conic plus its tangent line.

Run: python conic_tangent_checker.py
Requires Python 3 and sympy (to choose irreducible test polynomials).
"""
from collections import Counter
from itertools import product
from math import isqrt
from sympy import Poly, symbols

x = symbols('x')


class Field:
    def __init__(self, p, k=1):
        self.p, self.k, self.q = p, k, p ** k
        if k == 1:
            self.relation = None
        else:
            for coefficients in product(range(p), repeat=k):
                expression = x ** k + sum(coefficients[i] * x ** i for i in range(k))
                if Poly(expression, x, modulus=p).is_irreducible:
                    self.relation = tuple(coefficients)
                    break
            else:
                raise RuntimeError('Irreducible polynomial not found')
        self.vectors = [tuple((a // p ** i) % p for i in range(k)) for a in range(self.q)]
        self.addition = [[self.encode(tuple((self.vectors[a][i] + self.vectors[b][i]) % p for i in range(k))) for b in range(self.q)] for a in range(self.q)]
        self.multiplication = [[self._mul_raw(a, b) for b in range(self.q)] for a in range(self.q)]
        self.zero, self.one = 0, 1
        self.two = self.addition[1][1]
        self.four = self.multiplication[self.two][self.two]
        self.negation = [next(b for b in range(self.q) if self.addition[a][b] == 0) for a in range(self.q)]
        self.squares = {self.multiplication[a][a] for a in range(1, self.q)}
        self.nonsquare = next(a for a in range(1, self.q) if a not in self.squares)

    def encode(self, digits):
        return sum(t * self.p ** i for i, t in enumerate(digits))

    def _mul_raw(self, a, b):
        p, k = self.p, self.k
        av, bv = self.vectors[a], self.vectors[b]
        coefficients = [0] * (2 * k - 1)
        for i in range(k):
            for j in range(k):
                coefficients[i + j] = (coefficients[i + j] + av[i] * bv[j]) % p
        if k > 1:
            for degree in range(2 * k - 2, k - 1, -1):
                lead = coefficients[degree]
                for i in range(k):
                    coefficients[degree - k + i] = (coefficients[degree - k + i] - lead * self.relation[i]) % p
        return self.encode(coefficients[:k])

    def add(self, a, b):
        return self.addition[a][b]

    def sub(self, a, b):
        return self.addition[a][self.negation[b]]

    def mul(self, a, b):
        return self.multiplication[a][b]

    def square(self, a):
        return self.multiplication[a][a]

    def chi(self, a):
        return 0 if a == 0 else (1 if a in self.squares else -1)


def check(p, k):
    F = Field(p, k)
    q, D = F.q, F.nonsquare
    add, sub, mul, sq, chi = F.add, F.sub, F.mul, F.square, F.chi
    N = lambda a, b: sub(sq(a), mul(D, sq(b)))
    circle = {(a, b) for a in range(q) for b in range(q) if N(a, b) == 1}
    tangent = {(1, b) for b in range(q)}
    support = circle | tangent
    assert len(circle) == q + 1 and len(support) == 2 * q
    counts = Counter((add(a, c), add(b, d)) for a, b in support for c, d in support)
    missing = set(product(range(q), repeat=2)) - set(counts)
    predicted = set()
    A = [a for a in range(q) if chi(mul(a, sub(a, F.two))) == 1]
    assert len(A) == (q - 3) // 2
    for a in range(q):
        for b in range(q):
            n = N(a, b)
            circle_count = q + 1 if a == 0 and b == 0 else 1 - chi(mul(sub(n, F.four), n))
            incidence = 1 - chi(mul(a, sub(a, F.two)))
            r = (circle_count + 2 * incidence + (q - 2) * (a == F.two)
                 - 2 * (N(sub(a, 1), b) == 1) + (a == F.two and b == 0))
            assert counts.get((a, b), 0) == r, ('convolution', p, k, a, b, r, counts.get((a, b), 0))
            if a in A and chi(mul(n, sub(n, F.four))) == 1:
                predicted.add((a, b))
    assert missing == predicted, ('zero locus', p, k)
    predicted_count = 0
    for a in A:
        h = [mul(N(a, b), sub(N(a, b), F.four)) for b in range(q)]
        Z = sum(z == 0 for z in h)
        S = sum(chi(z) for z in h)
        assert (q - Z + S) % 2 == 0
        predicted_count += (q - Z + S) // 2
        if a != F.negation[F.two]:
            trace = -S - 1
            assert abs(trace) <= 2 * q ** .5 + 1e-8, ('Hasse', p, k, a)
    assert predicted_count == len(missing)
    return q, len(missing), (q * q - len(missing)) / (q * q)


def main():
    data = []
    for p, k in [(3,1),(5,1),(7,1),(3,2),(11,1),(13,1),(17,1),(19,1),(5,2),(3,3),(7,2),(3,4)]:
        data.append(check(p,k))
    print('VERIFIED q, missing_sums, proportion_of_representable_sums')
    for row in data:
        print(*row)
    print('PASS: direct convolution, exact character-zero criterion, trace and count for',len(data),'fields')


if __name__ == '__main__':
    main()
