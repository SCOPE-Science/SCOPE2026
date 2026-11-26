"""Exhaustive checks of tuple-generation counts for square-zero quiver algebras.

No external dependencies. Includes the extension field GF(4) represented by
F_2[t]/(t^2+t+1). For each case it builds the generated unital subalgebra
by linear-span closure under multiplication, independently of the formula.
"""
from itertools import product
from math import prod

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q = q
    def add(self, a, b):
        return a ^ b if self.q == 4 else (a + b) % self.q
    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q
    def sub(self, a, b):
        return self.add(a, self.neg(b))
    def mul(self, a, b):
        if self.q != 4:
            return a * b % self.q
        x = 0
        while b:
            if b & 1:
                x ^= a
            a <<= 1
            if a & 4:
                a ^= 7
            b >>= 1
        return x
    def pow(self, a, power):
        z = 1
        while power:
            if power & 1:
                z = self.mul(z, a)
            a = self.mul(a, a)
            power >>= 1
        return z
    def inv(self, a):
        assert a
        return self.pow(a, self.q - 2)


def row_rank(vectors, field):
    basis = {}
    for w in vectors:
        v = list(w)
        for pivot in sorted(basis):
            row = basis[pivot]
            factor = v[pivot]
            if factor:
                v = [field.sub(x, field.mul(factor, y)) for x, y in zip(v, row)]
        pivot = next((i for i, val in enumerate(v) if val), None)
        if pivot is None:
            continue
        inv = field.inv(v[pivot])
        basis[pivot] = [field.mul(inv, val) for val in v]
    return len(basis)


def multiply(a, b, n, arrows, field):
    out = [field.mul(a[i], b[i]) for i in range(n)]
    for k, (src, dst) in enumerate(arrows):
        out.append(field.add(field.mul(a[src], b[n+k]),
                             field.mul(a[n+k], b[dst])))
    return tuple(out)


def generates(tuple_elements, n, arrows, field):
    dimension = n + len(arrows)
    unit = tuple([1] * n + [0] * len(arrows))
    independent = []
    def insert(w):
        if row_rank(independent + [w], field) > len(independent):
            independent.append(w)
    insert(unit)
    for x in tuple_elements:
        insert(x)
    cursor = 0
    while cursor < len(independent):
        v = independent[cursor]
        snapshot = list(independent)
        for w in snapshot:
            insert(multiply(v, w, n, arrows, field))
            insert(multiply(w, v, n, arrows, field))
            if len(independent) == dimension:
                return True
        cursor += 1
    return len(independent) == dimension


def predicted_count(n, arrows, d, q):
    m = [[sum(1 for i, j in arrows if (i, j) == (u, v))
          for v in range(n)] for u in range(n)]
    if n > q**d:
        return 0
    result = prod(q**d - h for h in range(n))
    for i in range(n):
        result *= prod(q**d - q**h for h in range(m[i][i]))
    for i in range(n):
        for j in range(n):
            if i != j:
                s = m[i][j]
                result *= q**s * prod(q**(d-1) - q**h for h in range(s))
    return result


def test_case(n, arrows, d, q):
    field = Field(q)
    dimension = n + len(arrows)
    elements = list(product(range(q), repeat=dimension))
    observed = sum(generates(t, n, arrows, field)
                   for t in product(elements, repeat=d))
    predicted = predicted_count(n, arrows, d, q)
    assert observed == predicted, (n, arrows, d, q, observed, predicted)
    print('PASS q=%d vertices=%d arrows=%s generators=%d count=%d total=%d' %
          (q, n, str(arrows), d, observed, q**(dimension*d)))


def main():
    cases = [
        (2, (), 2, 2),
        (2, ((0, 1),), 1, 2),
        (2, ((0, 1),), 2, 2),
        (2, ((0, 1),), 2, 3),
        (2, ((0, 1),), 2, 4),
        (2, ((0, 1),), 2, 5),
        (2, ((0, 1),), 3, 2),
        (2, ((0, 1), (0, 1)), 2, 2),
        (2, ((0, 1), (0, 1)), 3, 2),
        (2, ((0, 1), (1, 0)), 2, 2),
        (2, ((0, 1), (1, 0)), 2, 3),
        (2, ((0, 0), (0, 1)), 2, 2),
        (1, ((0, 0),), 1, 2),
        (1, ((0, 0), (0, 0)), 2, 2),
        (1, ((0, 0), (0, 0)), 2, 4),
        (3, ((0, 1), (1, 2)), 2, 2),
        (3, ((0, 1), (0, 2)), 2, 2),
    ]
    for case in cases:
        test_case(*case)
    print('ALL_GENERATION_COUNTS_VERIFIED', len(cases))

if __name__ == '__main__':
    main()
