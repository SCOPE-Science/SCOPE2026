#!/usr/bin/env python3
from itertools import combinations
from math import gcd


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def div_exact(a, b):
    a = a[:]
    b = trim(b[:])
    q = [0] * max(1, (len(a) - len(b) + 1))
    while len(a) >= len(b) and any(a):
        k = len(a) - len(b)
        assert b[-1] in (1, -1)
        c = a[-1] // b[-1]
        q[k] = c
        for j, bj in enumerate(b):
            a[k + j] -= c * bj
        trim(a)
    assert all(x == 0 for x in a), (a, b)
    return trim(q)


def remainder(a, b):
    a = trim(a[:])
    b = trim(b[:])
    while len(a) >= len(b):
        k = len(a) - len(b)
        c = a[-1] // b[-1]
        for j, bj in enumerate(b):
            a[k + j] -= c * bj
        trim(a)
    return tuple(a)


PHI = {1: [-1, 1]}

def cyclotomic(n):
    if n in PHI:
        return PHI[n]
    p = [-1] + [0] * (n - 1) + [1]
    for d in divisors(n):
        if d < n:
            p = div_exact(p, cyclotomic(d))
    PHI[n] = p
    return p


def actual_zero(A, N, d):
    if d % N == 0:
        return False
    g = gcd(N, d)
    m = N // g
    e = [(a * (d // g)) % m for a in A]
    coeff = [0] * m
    for x in e:
        coeff[x] += 1
    return all(v == 0 for v in remainder(coeff, cyclotomic(m)))


def invariant(A, N):
    a0, a1, a2 = A
    h = gcd(N, gcd((a1 - a0) % N, (a2 - a0) % N))
    n = N // h
    B = [((a - a0) // h) % n for a in A]
    return h, n, B


def predicted_spectral(A, N):
    h, n, B = invariant(A, N)
    return n % 3 == 0 and {b % 3 for b in B} == {0, 1, 2}


def predicted_zero_set(A, N):
    h, n, B = invariant(A, N)
    if not predicted_spectral(A, N):
        return set()
    q = n // 3
    return {d for d in range(1, N) if d % n in (q, 2 * q)}


def is_spectrum(A, B, N, zero_set=None):
    if zero_set is None:
        zero_set = {d for d in range(1, N) if actual_zero(A, N, d)}
    for x, y in combinations(B, 2):
        if (x - y) % N not in zero_set or (y - x) % N not in zero_set:
            return False
    return True


def predicted_spectrum(A, B, N):
    h, n, _ = invariant(A, N)
    if not predicted_spectral(A, N):
        return False
    q = n // 3
    residues = sorted({b % n for b in B})
    if len(residues) != 3:
        return False
    base = residues[0]
    return {(r - base) % n for r in residues} == {0, q, 2 * q}


def main():
    # Independent exact root checks through cyclotomic divisibility.
    sets_checked = 0
    zero_tests = 0
    for N in range(3, 31):
        for A in combinations(range(N), 3):
            actual = {d for d in range(1, N) if actual_zero(A, N, d)}
            zero_tests += N - 1
            pred = predicted_zero_set(A, N)
            assert actual == pred, (N, A, actual, pred)
            assert bool(actual) == predicted_spectral(A, N), (N, A, actual)
            sets_checked += 1

    spectrum_As = 0
    spectrum_tests = 0
    for N in range(3, 21):
        triples = list(combinations(range(N), 3))
        for A in triples:
            z = {d for d in range(1, N) if actual_zero(A, N, d)}
            if not z:
                continue
            spectrum_As += 1
            actual_count = 0
            predicted_count = 0
            for B in triples:
                a = is_spectrum(A, B, N, z)
                p = predicted_spectrum(A, B, N)
                assert a == p, (N, A, B, a, p)
                actual_count += int(a)
                predicted_count += int(p)
                spectrum_tests += 1
            h, n, _ = invariant(A, N)
            assert actual_count == predicted_count == N * h * h // 3, (N, A, h, actual_count)

    print(f"exact_zero_sets={sets_checked}")
    print(f"cyclotomic_zero_tests={zero_tests}")
    print(f"spectral_A_sets={spectrum_As}")
    print(f"spectrum_pair_tests={spectrum_tests}")
    print("VERIFY_OK")

if __name__ == '__main__':
    main()
