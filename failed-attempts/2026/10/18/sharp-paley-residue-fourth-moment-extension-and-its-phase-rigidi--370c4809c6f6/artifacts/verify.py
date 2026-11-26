#!/usr/bin/env python3
"""Exact Paley difference-set checks and independent Fourier identity tests."""
import cmath
import itertools
import math
import random


def residues(p):
    return sorted({(x * x) % p for x in range(1, p)})


def determinant(rows):
    """Fraction-free integer determinant."""
    A = [list(r) for r in rows]
    n = len(A)
    sign = 1
    prev = 1
    for i in range(n - 1):
        if A[i][i] == 0:
            j = next(j for j in range(i + 1, n) if A[j][i] != 0)
            A[i], A[j] = A[j], A[i]
            sign *= -1
        pivot = A[i][i]
        for j in range(i + 1, n):
            for k in range(i + 1, n):
                num = A[j][k] * pivot - A[j][i] * A[i][k]
                assert num % prev == 0
                A[j][k] = num // prev
        for j in range(i + 1, n):
            A[j][i] = 0
        prev = pivot
    return sign * A[-1][-1]


P11 = [1, 3, 4, 5, 9]
RELATIONS = [(1, 1, 4, 9), (1, 5, 3, 3),
             (1, 9, 5, 5), (3, 4, 9, 9)]


def check_p11_certificate():
    assert residues(11) == P11
    matrix = []
    for a, b, c, d in RELATIONS:
        assert (a + b - c - d) % 11 == 0
        row = [int(a == x) + int(b == x) - int(c == x) - int(d == x)
               for x in P11]
        assert sum(row) == 0
        matrix.append(row[1:])
    assert determinant(matrix) == -11, determinant(matrix)
    for j in range(11):
        phase = {x: cmath.exp(2j * math.pi * j * (x - 1) / 11) for x in P11}
        assert all(abs(phase[a] * phase[b] - phase[c] * phase[d]) < 1e-12
                   for a, b, c, d in RELATIONS)
    return 11


def direct_group(q):
    if q != 27:
        return list(range(q)), lambda a, b: (a + b) % q, residues(q), \
            lambda a: a % q

    def digits(x):
        return [x % 3, (x // 3) % 3, x // 9]

    def encode(v):
        return sum((v[i] % 3) * (3 ** i) for i in range(3))

    def add(a, b):
        return encode([(x + y) % 3 for x, y in zip(digits(a), digits(b))])

    def mul(a, b):
        aa, bb = digits(a), digits(b)
        z = [0] * 5
        for i in range(3):
            for j in range(3):
                z[i + j] += aa[i] * bb[j]
        # Irreducible T^3-T-1 over F_3: T^3 = T+1.
        for i in (4, 3):
            coeff = z[i]
            z[i] = 0
            z[i - 2] += coeff
            z[i - 3] += coeff
        return encode(z[:3])

    def power(a, n):
        out = 1
        while n:
            if n & 1:
                out = mul(out, a)
            a = mul(a, a)
            n //= 2
        return out

    def trace(a):
        s = add(add(a, power(a, 3)), power(a, 9))
        assert s in (0, 1, 2)
        return s

    sq = sorted({mul(x, x) for x in range(1, 27)})
    return list(range(27)), add, sq, trace


def check_paley_group(q):
    els, add, D, trace = direct_group(q)
    k = (q - 1) // 2
    lam = (q - 3) // 4
    assert len(D) == k
    Dset = set(D)
    neg = {a: next(b for b in els if add(a, b) == 0) for a in els}
    intersections = {}
    for shift in els:
        pts = [a for a in D if add(a, neg[shift]) in Dset]
        assert len(pts) == (k if shift == 0 else lam)
        intersections[shift] = pts
    mintriple = min(
        len([x for x in D if add(x, neg[a]) in Dset and
             add(x, neg[b]) in Dset])
        for a in els if a != 0 for b in els if b not in (0, a))
    if q >= 19:
        assert mintriple >= 1
    rng = random.Random(731 + q)
    tests = 12
    for _ in range(tests):
        f = {a: complex(rng.randint(-4, 4), rng.randint(-4, 4)) for a in D}
        M = sum(abs(t) ** 2 for t in f.values())
        autocorr = {}
        phase_dispersion = 0.0
        for d, indices in intersections.items():
            z = [f[x] * f[add(x, neg[d])].conjugate() for x in indices]
            autocorr[d] = sum(z)
            if d != 0:
                for i in range(len(z)):
                    for j in range(i + 1, len(z)):
                        phase_dispersion += abs(z[i] - z[j]) ** 2
        Q = sum(abs(z) ** 2 for z in autocorr.values())
        R = 1 + lam * (1 - 1 / k)
        variance = lam * sum((abs(v) ** 2 - M / k) ** 2 for v in f.values())
        assert math.isclose(R * M * M - Q, variance + phase_dispersion,
                            rel_tol=2e-12, abs_tol=2e-8), q
        Fs = []
        for xi in els:
            val = sum(f[x] * cmath.exp(2j * math.pi * trace(
                # Multiplication xi*x in F27 uses the field multiplier below.
                ((xi * x) % q if q != 27 else field27_mul(xi, x))) / (3 if q == 27 else q))
                      for x in D)
            Fs.append(val)
        moment = sum(abs(v) ** 4 for v in Fs)
        assert math.isclose(moment, q * Q, rel_tol=2e-11, abs_tol=1e-7), (q, moment, q * Q)
    # Any restricted additive character times a scalar attains equality.
    for xi in els[:min(q, 9)]:
        f = {x: cmath.exp(2j * math.pi * trace((xi * x) % q if q != 27 else field27_mul(xi, x))
                         / (3 if q == 27 else q)) for x in D}
        C = {}
        for d, indices in intersections.items():
            C[d] = sum(f[x] * f[add(x, neg[d])].conjugate() for x in indices)
        Q = sum(abs(z) ** 2 for z in C.values())
        expected = (1 + lam * (1 - 1 / k)) * k * k
        assert math.isclose(Q, expected, abs_tol=1e-8), q
    return mintriple, tests, len(els) * tests


def field27_mul(a, b):
    aa = [a % 3, a // 3 % 3, a // 9]
    bb = [b % 3, b // 3 % 3, b // 9]
    c = [0] * 5
    for i in range(3):
        for j in range(3):
            c[i + j] += aa[i] * bb[j]
    for i in (4, 3):
        t = c[i]
        c[i] = 0
        c[i - 2] += t
        c[i - 3] += t
    return sum((c[i] % 3) * (3 ** i) for i in range(3))


def main():
    assert check_p11_certificate() == 11
    totaltests, totalfreq = 0, 0
    out = {}
    for q in [3, 7, 11, 19, 23, 27, 31, 43]:
        if q == 27 or all(q % t for t in range(2, math.isqrt(q) + 1)):
            m, n, f = check_paley_group(q)
            out[q] = m
            totaltests += n
            totalfreq += f
    assert out[19] == 1 and out[23] == 1 and out[27] == 2
    # Hasse bound gives (q-15-2sqrt(q))/8>0 for all q>=27.
    assert (27 - 15 - 2 * math.sqrt(27)) / 8 > 0
    assert (31 - 15 - 2 * math.sqrt(31)) / 8 > 0
    print('VERIFY_OK p11_determinant=-11 small_triple_minima=', out,
          'complex_inputs=', totaltests, 'Fourier_samples=', totalfreq,
          'exact_deficit=PASS additive_character_extremizers=PASS')


if __name__ == '__main__':
    main()
