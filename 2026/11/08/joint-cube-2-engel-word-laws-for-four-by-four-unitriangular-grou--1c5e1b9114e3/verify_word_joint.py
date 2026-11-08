#!/usr/bin/env python3
"""Independent finite-field enumerations of two word maps on UT_4(q).

Only Python's standard library is required. Run: python verify_word_joint.py
The two test paths are (i) direct group multiplication and commutators and
(ii) six-coordinate polynomial/fiber enumeration over several finite fields.
"""
from collections import Counter
from itertools import product
from random import Random


class Field:
    def __init__(self, p, degree=1, modulus=None):
        self.p, self.degree = p, degree
        self.q = p ** degree
        self.modulus = tuple(modulus or ())
        if degree > 1:
            assert len(self.modulus) == degree + 1 and self.modulus[-1] == 1
        self.digits = [self._digits(a) for a in range(self.q)]
        self.add = [[self._from_digits([(u + v) % p for u, v in zip(self.digits[a], self.digits[b])])
                     for b in range(self.q)] for a in range(self.q)]
        self.neg = [self._from_digits([(-u) % p for u in self.digits[a]]) for a in range(self.q)]
        self.mul = [[self._multiply(a, b) for b in range(self.q)] for a in range(self.q)]
        for a in range(1, self.q):
            assert any(self.mul[a][b] == 1 for b in range(1, self.q))

    def _digits(self, a):
        out = []
        for _ in range(self.degree):
            out.append(a % self.p)
            a //= self.p
        return out

    def _from_digits(self, digits):
        return sum(c * self.p ** i for i, c in enumerate(digits))

    def _multiply(self, a, b):
        p, d = self.p, self.degree
        if d == 1:
            return (a * b) % p
        f = [0] * (2 * d - 1)
        for i, u in enumerate(self.digits[a]):
            for j, v in enumerate(self.digits[b]):
                f[i + j] = (f[i + j] + u * v) % p
        for k in range(2 * d - 2, d - 1, -1):
            z = f[k]
            for j in range(d):
                f[k - d + j] = (f[k - d + j] - z * self.modulus[j]) % p
        return self._from_digits(f[:d])

    def summ(self, *args):
        a = 0
        for b in args:
            a = self.add[a][b]
        return a


def group_mul(F, x, y):
    a, b, c, d, e, f = x
    A, B, C, D, E, H = y
    s, mul = F.summ, F.mul
    return (s(a, A), s(b, B), s(c, C), s(d, D, mul[a][B]),
            s(e, E, mul[b][C]), s(f, H, mul[a][E], mul[d][C]))


def group_inv(F, x):
    a, b, c, d, e, f = x
    n, s, mul = F.neg, F.summ, F.mul
    return (n[a], n[b], n[c], s(n[d], mul[a][b]),
            s(n[e], mul[b][c]),
            s(n[f], mul[a][e], n[mul[mul[a][b]][c]], mul[d][c]))


def commutator(F, x, y):
    return group_mul(F, group_mul(F, group_inv(F, x), group_inv(F, y)), group_mul(F, x, y))


def engel(F, x, y):
    return commutator(F, commutator(F, x, y), y)


def cubic(F, x):
    return group_mul(F, group_mul(F, x, x), x)


def polynomial(F, abc, ABC):
    a, b, c = abc
    A, B, C = ABC
    mul, n = F.mul, F.neg
    term1 = mul[mul[a][B]][C]
    term2 = mul[mul[b][A]][C]
    term3 = mul[mul[c][A]][B]
    return F.summ(term1, n[term2], n[term2], term3)


def expected(F):
    q = F.q
    t = 3 * q - 2 if F.p != 2 else q * q + q - 1
    eng0 = (q**3 + (q-1)*t) * q**2  # numerator over q^6
    engz = (q**3 - t) * q**2        # each nonzero z, over q^6
    if F.p == 3:
        joint0 = q * q * (6*q*q - 8*q + 3)
        jointz = 3 * q*q*(q-1)**2
    else:
        joint0 = None
        jointz = None
    return eng0, engz, joint0, jointz


def full_six_coordinate_check(F):
    q = F.q
    ctr = Counter()
    xyz = list(product(range(q), repeat=3))
    for x in xyz:
        cube = (F.p == 3 and F.mul[F.mul[x[0]][x[1]]][x[2]] == 0)
        for y in xyz:
            value = polynomial(F, x, y)
            ctr['total'] += 1
            ctr['engel', value] += 1
            if cube:
                ctr['cube'] += 1
                ctr['cube_and_engel', value] += 1
    assert ctr['total'] == q**6
    E0, E1, C0, C1 = expected(F)
    assert ctr['engel', 0] == E0, (q, ctr['engel', 0], E0)
    for z in range(1, q):
        assert ctr['engel', z] == E1
    if F.p == 3:
        assert ctr['cube'] == q**3*(3*q*q-3*q+1)
        assert ctr['cube_and_engel', 0] == C0
        for z in range(1,q):
            assert ctr['cube_and_engel', z] == C1
            assert ctr['engel', z]-ctr['cube_and_engel',z] == (q-1)**3*q*q
        assert ctr['engel',0]-ctr['cube_and_engel',0] == (q-1)**3*q*q
    return ctr


def direct_group_check(F, exhaustive, n_random=5000):
    q = F.q
    rng = Random(20261104+q)
    zero = (0,)*6
    if exhaustive:
        group = list(product(range(q), repeat=6))
        pairs = ((x,y) for x in group for y in group)
        n_pairs = q**12
    else:
        pairs = ((tuple(rng.randrange(q) for _ in range(6)),
                  tuple(rng.randrange(q) for _ in range(6))) for _ in range(n_random))
        n_pairs = n_random
    for x,y in pairs:
        w = engel(F,x,y)
        assert w[:5] == (0,)*5
        assert w[5] == polynomial(F,x[:3],y[:3]), (q,x,y,w)
        cube = cubic(F,x) == zero
        if F.p == 3:
            assert cube == (F.mul[F.mul[x[0]][x[1]]][x[2]] == 0)
        else:
            assert cube == (x == zero)
    return n_pairs


def main():
    cases = [(2,1,None),(3,1,None),(2,2,(1,1,1)),
             (5,1,None),(7,1,None),(2,3,(1,1,0,1)),(3,2,(1,0,1))]
    total_exhaustive = 0
    group_checked = 0
    for p,d,m in cases:
        F=Field(p,d,m)
        z = full_six_coordinate_check(F)
        total_exhaustive += z['total']
        n = direct_group_check(F, exhaustive=F.q <= 3, n_random=6000)
        group_checked += n
        print('FIELD q={} p={} six_coordinate_pairs={} direct_group_pairs={} engel_zero={} cube_and_engel_zero={}'.format(
            F.q, p, z['total'], n,z['engel',0], z.get(('cube_and_engel',0),'not_applicable')))
    print('VERIFY_OK six_coordinate_pairs={} direct_group_pairs={}'.format(total_exhaustive,group_checked))


if __name__=='__main__':
    main()
