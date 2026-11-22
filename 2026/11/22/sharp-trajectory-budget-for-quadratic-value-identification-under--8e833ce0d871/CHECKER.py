#!/usr/bin/env python3
"""Independent finite-field spot checks for the stated exact-arithmetic rank formula.

The analytic Vandermonde proof, not these finite checks, establishes the theorem.
Run from this directory: python3 CHECKER.py
"""
from collections import Counter
from itertools import combinations_with_replacement
from fractions import Fraction

PRIME = 1000000007


def rank_mod(matrix, prime=PRIME):
    if not matrix:
        return 0
    a = [[v % prime for v in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    p = 0
    for j in range(cols):
        idx = next((i for i in range(p, rows) if a[i][j]), None)
        if idx is None:
            continue
        a[p], a[idx] = a[idx], a[p]
        inv = pow(a[p][j], prime - 2, prime)
        a[p] = [(inv * v) % prime for v in a[p]]
        for i in range(p + 1, rows):
            if a[i][j]:
                factor = a[i][j]
                a[i] = [(x - factor*y) % prime for x, y in zip(a[i], a[p])]
        p += 1
        if p == rows:
            break
    return p


def as_mod(q):
    q = Fraction(q)
    return (q.numerator * pow(q.denominator, PRIME - 2, PRIME)) % PRIME


def check_case(eigs):
    n = len(eigs)
    pairs = list(combinations_with_replacement(range(n), 2))
    multiplicities = Counter(eigs[i] * eigs[j] for i, j in pairs)
    horizon = len(multiplicities)
    full = len(pairs)
    # Unique exponents for unordered pairs: 2^{i-1}+2^{j-1}.
    exponents = [2**i+2**j for i,j in pairs]
    assert len(set(exponents)) == full
    base = [pow(2, 2**i, PRIME) for i in range(n)]
    for r in range(1, max(multiplicities.values()) + 2):
        samples=[]
        for k in range(r):
            z0 = [pow(base[i], k, PRIME) for i in range(n)]
            z = z0[:]
            for t in range(horizon):
                samples.append([(z[i] * z[j]) % PRIME for i,j in pairs])
                z = [(z[i] * as_mod(eigs[i])) % PRIME for i in range(n)]
        predicted = sum(min(r, count) for count in multiplicities.values())
        actual = rank_mod(samples)
        assert actual == predicted, (eigs, r, horizon, actual, predicted)
        assert (actual == full) == (r >= max(multiplicities.values()))
        # Compare expanded quadratic features against direct symmetric-matrix evaluation.
        coeffs = [((i + 2)*(j + 3) + 1) % PRIME for i,j in pairs]
        qmat = [[0] * n for _ in range(n)]
        half = pow(2, PRIME - 2, PRIME)
        for (i,j), q in zip(pairs, coeffs):
            qmat[i][j] = q if i == j else (q * half) % PRIME
            qmat[j][i] = qmat[i][j]
        for k in range(r):
            z = [pow(base[i], k, PRIME) for i in range(n)]
            for t in range(horizon):
                row = samples[k * horizon + t]
                feature_form = sum(a*b for a,b in zip(row, coeffs)) % PRIME
                matrix_form = sum(z[i] * qmat[i][j] * z[j]
                                  for i in range(n) for j in range(n)) % PRIME
                assert feature_form == matrix_form, (eigs, r, k, t)
                z = [(z[i] * as_mod(eigs[i])) % PRIME for i in range(n)]
    return max(multiplicities.values()) + 1


def main():
    families = []
    for n in range(1, 10):
        families.append([Fraction(1,2)**(i+1) for i in range(n)])
        families.append([Fraction(2,3)**(i+1) for i in range(n)])
        families.append([Fraction(1,3)] * n)
        families.append([Fraction(0)] * n)
        families.append([Fraction((-1)**i * (i+1),i+3) for i in range(n)])
        families.append([Fraction(0) if i%3 == 0 else Fraction(1,2) for i in range(n)])
        families.append([Fraction(-1,2) if i%2 else Fraction(1,2) for i in range(n)])
    cases = sum(check_case(eigs) for eigs in families)
    assert len(families) == 63
    print(f"PASS: {len(families)} exact-rational-spectrum families, {cases} finite-field rank comparisons; all matched the proven formula")
    print("Finite-field computations supplement, and do not replace, the characteristic-zero proof.")

if __name__ == '__main__':
    main()
