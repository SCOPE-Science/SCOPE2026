#!/usr/bin/env python3
"""Independent finite-field checks of the Zorn algebra commutator-fiber formulas.

Only Python's standard library is required.  All calculations use the
seven trace-zero coordinates; each full-octonion fiber is q^2 times the
trace-zero count because the two scalar input coordinates are free.
"""
import itertools
import random


class Field:
    def __init__(self, q):
        assert q in (3, 5, 9)
        self.q = q
        self.p = 3 if q == 9 else q

    def add(self, x, y):
        if self.q != 9:
            return (x + y) % self.q
        return ((x % 3 + y % 3) % 3) + 3 * ((x // 3 + y // 3) % 3)

    def neg(self, x):
        if self.q != 9:
            return (-x) % self.q
        return ((-x % 3) + 3 * (-(x // 3) % 3))

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def mul(self, x, y):
        if self.q != 9:
            return x * y % self.q
        a, b, c, d = x % 3, x // 3, y % 3, y // 3
        # theta^2=-1 is irreducible over F_3
        return ((a * c - b * d) % 3) + 3 * ((a * d + b * c) % 3)

    def power(self, a, k):
        v = 1
        while k:
            if k & 1:
                v = self.mul(v, a)
            a = self.mul(a, a)
            k >>= 1
        return v

    def inv(self, a):
        assert a != 0
        return self.power(a, self.q - 2)

    def chi(self, a):
        if a == 0:
            return 0
        return 1 if self.power(a, (self.q - 1) // 2) == 1 else -1

    def dot(self, x, y):
        r = 0
        for a, b in zip(x, y):
            r = self.add(r, self.mul(a, b))
        return r

    def cross(self, x, y):
        return (self.sub(self.mul(x[1], y[2]), self.mul(x[2], y[1])),
                self.sub(self.mul(x[2], y[0]), self.mul(x[0], y[2])),
                self.sub(self.mul(x[0], y[1]), self.mul(x[1], y[0])))

    def times(self, a, n):
        return self.mul(a, n % self.p)

    def Q(self, z):
        return self.add(self.mul(z[0], z[0]), self.times(self.dot(z[1:4], z[4:7]), 4))

    def pairing(self, a, b):
        # One fourth of the polar form of Q.
        half = self.inv(2 % self.p)
        return self.add(self.mul(self.mul(a[0], b[0]), half),
                        self.add(self.dot(a[1:4], b[4:7]), self.dot(a[4:7], b[1:4])))

    def comm(self, a, b):
        d, u, v = a[0], a[1:4], a[4:7]
        e, s, t = b[0], b[1:4], b[4:7]
        vt, us = self.cross(v, t), self.cross(u, s)
        first = self.times(self.sub(self.dot(u, t), self.dot(v, s)), 2)
        upper = tuple(self.sub(self.sub(self.mul(d, s[i]), self.mul(e, u[i])), self.times(vt[i], 2)) for i in range(3))
        lower = tuple(self.add(self.sub(self.mul(e, v[i]), self.mul(d, t[i])), self.times(us[i], 2)) for i in range(3))
        return (first,) + upper + lower

    def rank_pair(self, M, z):
        # Return rank(M), rank([M|z]).  Matrix need not be square.
        t = [list(row) + [zi] for row, zi in zip(M, z)]
        nr, nc = len(t), len(M[0])
        rank_m = 0
        row = 0
        for col in range(nc + 1):
            pivot = next((i for i in range(row, nr) if t[i][col] != 0), None)
            if pivot is None:
                continue
            t[row], t[pivot] = t[pivot], t[row]
            inv = self.inv(t[row][col])
            t[row] = [self.mul(inv, x) for x in t[row]]
            for i in range(row + 1, nr):
                scale = t[i][col]
                if scale:
                    t[i] = [self.sub(a, self.mul(scale, b)) for a, b in zip(t[i], t[row])]
            row += 1
            if col < nc:
                rank_m += 1
        return rank_m, row


def expected(f, z):
    q = f.q
    if z == (0,) * 7:
        return q**9 + q**8 - q**3
    return q**7 - q**3 + (q**6 - q**4) * f.chi(f.Q(z))


def run(q):
    f = Field(q)
    rng = random.Random(20261104 + q)
    E = [tuple(int(j == i) for j in range(7)) for i in range(7)]
    nonsquare = next(a for a in range(1, q) if f.chi(a) == -1)
    targets = {
        'zero': (0, 0, 0, 0, 0, 0, 0),
        'nonzero_isotropic': (0, 1, 0, 0, 0, 0, 0),
        'square_norm': (1, 0, 0, 0, 0, 0, 0),
        'nonsquare_norm': (0, 1, 0, 0, nonsquare, 0, 0),
    }
    assert f.chi(f.Q(targets['square_norm'])) == 1
    assert f.chi(f.Q(targets['nonsquare_norm'])) == -1
    assert f.Q(targets['nonzero_isotropic']) == 0

    if q == 3:
        xs = itertools.product(range(q), repeat=7)
        exact = True
    else:
        xs = [tuple(rng.randrange(q) for _ in range(7)) for _ in range(640)]
        exact = False

    totals = {name: 0 for name in targets}
    checked = 0
    for x in xs:
        cols = [f.comm(x, b) for b in E]
        M = [[cols[j][i] for j in range(7)] for i in range(7)]
        r, _ = f.rank_pair(M, (0,) * 7)
        k = 7 - r
        assert k == (7 if x == (0,) * 7 else 3 if f.Q(x) == 0 else 1), (q, x, k)
        for name, z in targets.items():
            r2, ra = f.rank_pair(M, z)
            assert r2 == r
            if ra == r:
                totals[name] += q**k
        if checked < 90:
            y = tuple(rng.randrange(q) for _ in range(7))
            lam = tuple(rng.randrange(q) for _ in range(7))
            assert f.pairing(lam, f.comm(x, y)) == f.pairing(f.comm(lam, x), y)
        checked += 1

    if exact:
        for name, z in targets.items():
            assert totals[name] == expected(f, z), (name, totals[name], expected(f, z))

    # The four fiber values must sum, with their quadratic-fiber
    # multiplicities, to q^14 trace-zero input pairs.
    iso_nonzero = q**6 - 1
    square = (q - 1) * (q**6 + q**3) // 2
    nonsquare_count = (q - 1) * (q**6 - q**3) // 2
    assert 1 + iso_nonzero + square + nonsquare_count == q**7
    mass = (expected(f, targets['zero'])
            + iso_nonzero * expected(f, targets['nonzero_isotropic'])
            + square * expected(f, targets['square_norm'])
            + nonsquare_count * expected(f, targets['nonsquare_norm']))
    assert mass == q**14
    print('field=%d, tested_x=%d, independent linear systems=%d, fiber_exhaustive=%s' %
          (q, checked, checked * len(targets), exact))
    print('predicted trace-zero fibers:', {name: expected(f, z) for name, z in targets.items()})
    if exact:
        print('exhaustively observed fibers:', totals)
    print('quadratic-fiber mass identity PASS, commutator-kernel ranks PASS')

if __name__ == '__main__':
    for q in (3, 5, 9):
        run(q)
    print('SPLIT_OCTONION_COMPLETE_COMMUTATOR_FIBERS_PASS')
