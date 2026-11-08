#!/usr/bin/env python3
"""Elementary cross-checks for quadratic-residue bispectral phase rigidity.

No external Python packages are required. Tests are finite corroboration, not the
all-prime proof. The rank calculation is performed over two unrelated prime
coefficient fields, and an exact rational rank is checked for the small cases.
"""
from fractions import Fraction
from math import cos, sin, pi
from random import Random


def primes_through(n):
    return [p for p in range(3, n + 1, 2)
            if all(p % d for d in range(3, int(p**0.5) + 1, 2))]


def system(p):
    H = sorted({(x * x) % p for x in range(1, p)})
    where = {a: i for i, a in enumerate(H)}
    D = sorted(x for x in H if (1 - x) % p in where)
    rows = []
    for t in H:
        for x in D:
            row = [0] * len(H)
            row[where[t * x % p]] += 1
            row[where[t * (1 - x) % p]] += 1
            row[where[t]] -= 1
            rows.append(row)
    return H, D, rows


def modular_rank(rows, n, prime):
    basis = {}
    for row0 in rows:
        row = [x % prime for x in row0]
        while True:
            first = next((j for j, x in enumerate(row) if x), None)
            if first is None:
                break
            if first not in basis:
                inv = pow(row[first], -1, prime)
                basis[first] = [(x * inv) % prime for x in row]
                break
            old = basis[first]
            z = row[first]
            row = [(row[j] - z * old[j]) % prime
                   for j in range(n)]
    return len(basis)


def rational_rank(rows, n):
    basis = {}
    for row0 in rows:
        row = [Fraction(v) for v in row0]
        while True:
            first = next((j for j, x in enumerate(row) if x), None)
            if first is None:
                break
            if first not in basis:
                pivot = row[first]
                basis[first] = [x / pivot for x in row]
                break
            old = basis[first]
            z = row[first]
            row = [row[j] - z * old[j] for j in range(n)]
    return len(basis)


def predicted_rank(p):
    m = (p - 1) // 2
    if p in (3, 5):
        return 0
    if p == 13:
        return m - 2
    return m


def test():
    pts = primes_through(101)
    for p in pts:
        H, D, rows = system(p)
        m = len(H)
        expected_d = (p - 5) // 4 if p % 4 == 1 else (p - 3) // 4
        assert len(D) == expected_d, (p, D)
        assert len(rows) == m * len(D)
        expect = predicted_rank(p)
        for field in (1000003, 1000033):
            rank = modular_rank(rows, m, field)
            assert rank == expect, (p, field, rank, expect)
        if p <= 31:
            assert rational_rank(rows, m) == expect, p
        # The additive character phases are always in the kernel of each
        # bispectrum ratio relation (checked through exact F_p arithmetic).
        for row in rows:
            assert sum(coeff * h for coeff, h in zip(row, H)) % p == 0
    # Explicit two-parameter circle family for p=13.
    H, D, rows = system(13)
    assert D == [4, 10]
    theta, phi = 0.37, 1.13
    A = complex(cos(theta), sin(theta))
    B = complex(cos(phi), sin(phi))
    phases = [A, B, B / A, 1 / A, 1 / B, A / B]
    labels = [pow(4, j, 13) for j in range(6)]
    u = dict(zip(labels, phases))
    for t in H:
        for x in D:
            assert abs(u[t*x%13] * u[t*(1-x)%13] - u[t]) < 1e-12
    # Three independent random torus pairs, to avoid a single example.
    rng = Random(12345)
    for _ in range(3):
        aa = rng.uniform(-pi, pi)
        bb = rng.uniform(-pi, pi)
        a = complex(cos(aa), sin(aa))
        b = complex(cos(bb), sin(bb))
        u = dict(zip(labels, [a,b,b/a,1/a,1/b,a/b]))
        assert all(abs(u[t*x%13]*u[t*(1-x)%13]-u[t])<1e-12
                   for t in H for x in D)
    print('PALEY_BISPECTRAL_LOCAL_RIGIDITY_CHECK_PASS')
    print('primes:', len(pts), 'range:', pts[0], '..', pts[-1])
    print('modular ranks: two coefficient fields, every prime tested')
    print('exact rational ranks: all primes through 31')
    print('p=13: two-dimensional phase family verified')


if __name__ == '__main__':
    test()
