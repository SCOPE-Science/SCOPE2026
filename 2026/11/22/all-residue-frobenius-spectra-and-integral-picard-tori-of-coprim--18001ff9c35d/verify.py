#!/usr/bin/env python3
"""Exact independent finite-field checks for nodal Chebyshev signed-orbit formulas."""
from collections import Counter
from itertools import product
from math import gcd


def node_orbits(m, n, q):
    assert 2 <= m < n and gcd(m, n) == 1
    modulus = 2 * m * n
    assert gcd(q, modulus) == 1
    rep = lambda a: min(a % modulus, (-a) % modulus)
    pairs = [tuple(sorted((rep(k * n + l * m), rep(l * m - k * n))))
             for k in range(1, m) for l in range(1, n)]
    unique = set(pairs)
    assert len(unique) == (m-1)*(n-1)//2
    assert all(pairs.count(pair) == 2 for pair in unique)
    assert all(len(set(pair)) == 2 for pair in unique)

    def forward(pair):
        return tuple(sorted(rep(q * a) for a in pair))

    assert {forward(pair) for pair in unique} == unique
    unseen = set(unique)
    counts = Counter()
    while unseen:
        root = min(unseen)
        pair = root
        length = 0
        while pair in unseen:
            unseen.remove(pair)
            length += 1
            pair = forward(pair)
        assert pair == root
        power = pow(q, length, modulus)
        evolved = tuple(rep(power * a) for a in root)
        if evolved == root:
            sign = 1
        else:
            assert evolved == root[::-1]
            sign = -1
        counts[(length, sign)] += 1
    assert sum(length * multiplicity for (length, _), multiplicity in counts.items()) == len(unique)
    return counts


def cheb(k, x, p):
    if k == 0:
        return 1
    a, b = 1, x
    for _ in range(2, k+1):
        a, b = b, (2*x*b-a) % p
    return b % p


def affine_count(m, n, p):
    # Count T_n(x)=T_m(y) over F_p without using node labels or the normalization.
    cx = Counter(cheb(n, x, p) for x in range(p))
    cy = Counter(cheb(m, y, p) for y in range(p))
    return sum(cx[t] * cy[t] for t in cx)


def predict(m, n, q, r=1):
    counts = node_orbits(m, n, q)
    correction = 0
    for (d, sign), multiplicity in counts.items():
        if r % d == 0:
            correction -= d * multiplicity * (sign ** (r // d))
    return q**r + correction


class Fp2:
    def __init__(self, p):
        self.p = p
        self.a = next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)
        self.Q = p * p
        # Elements a + b*sqrt(D) represented by a + p*b.

    def add(self, a, b):
        p = self.p
        return ((a % p + b % p) % p) + p * (((a // p + b // p) % p))

    def neg(self, a):
        p = self.p
        return (-(a % p) % p) + p * (-(a // p) % p)

    def mul(self, x, y):
        p = self.p
        a, b = x % p, x // p
        c, d = y % p, y // p
        return (a*c + self.a*b*d) % p + p * ((a*d+b*c) % p)

    def val(self, deg, x):
        if deg == 0: return 1
        a, b = 1, x
        for _ in range(2, deg+1):
            a, b = b, self.add(self.mul(self.mul(2,x),b), self.neg(a))
        return b

    def count(self, m, n):
        A=Counter(self.val(n,x) for x in range(self.Q))
        B=Counter(self.val(m,y) for y in range(self.Q))
        return sum(A[t]*B[t] for t in A)


def run():
    orbit_cases = 0
    prime_checks = 0
    quadratic_checks = 0
    for m in range(2, 12):
        for n in range(m+1, 15):
            if gcd(m, n) != 1:
                continue
            for q in range(3, 90, 2):
                if gcd(q, 2*m*n) != 1:
                    continue
                node_orbits(m, n, q)
                orbit_cases += 1
            for p in [3,5,7,11,13,17,19,23,29,31,37,41]:
                if gcd(p, 2*m*n) != 1:
                    continue
                actual = affine_count(m, n, p)
                assert actual == predict(m, n, p), (m,n,p,actual,predict(m,n,p))
                prime_checks += 1
            for p in [3,5,7,11,13]:
                if gcd(p, 2*m*n) != 1:
                    continue
                actual=Fp2(p).count(m,n)
                expect = predict(m,n,p,2)
                assert actual == expect, (m,n,p,actual,expect)
                quadratic_checks += 1

    assert node_orbits(3,8,7) == {(1,-1):3,(2,1):2}
    assert predict(3,8,7)==10
    assert predict(3,8,7,2)==7**2-3-4
    assert affine_count(3,8,7)==10
    assert Fp2(7).count(3,8)==42
    print('CHEBYSHEV_ALL_RESIDUES_ORBITS_AND_ZETA_OK')
    print('orbit_cases',orbit_cases,'prime_checks',prime_checks,'quadratic_checks',quadratic_checks)
    print('example (m,n,q)=(3,8,7):',dict(node_orbits(3,8,7)))


if __name__ == '__main__': run()
