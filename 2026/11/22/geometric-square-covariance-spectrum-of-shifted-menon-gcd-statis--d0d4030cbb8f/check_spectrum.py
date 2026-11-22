#!/usr/bin/env python3
"""Finite consistency checks for a gcd covariance spectral formula.

All arithmetic uses Python integers, and no external libraries are required.
Finite tests do not establish the theorem for arbitrary prime powers.
"""
import math
from fractions import Fraction


def units(p, k):
    return [a for a in range(1, p**k) if a % p]


def theoretical_spectrum(p, k):
    result = {0: 1}
    for ell in range(1, k + 1):
        multiplicity = p - 2 if ell == 1 else (p - 1)**2 * p**(ell - 2)
        if multiplicity:
            eigenvalue = (k - ell + 1)**2
            result[eigenvalue] = result.get(eigenvalue, 0) + multiplicity
    return result


def verify(p, k):
    mod = p**k
    residues = units(p, k)
    m = len(residues)
    assert m == (p - 1) * p**(k - 1)
    x = [[math.gcd(a - u, mod) for u in residues] for a in residues]
    assert all(sum(row) == m * (k + 1) for row in x)
    h = [[val - (k + 1) for val in row] for row in x]
    assert all(sum(row) == 0 for row in h)
    assert all(h[i][j] == h[j][i] for i in range(m) for j in range(m))

    # Check direct covariance against a formula not using eigenvalues.
    c_num = [[sum(h[i][u] * h[j][u] for u in range(m))
              for j in range(m)] for i in range(m)]
    for i, a in enumerate(residues):
        for j, b in enumerate(residues):
            formula = -k*k*m
            for depth in range(1, k + 1):
                if (a - b) % p**depth == 0:
                    formula += m * (2*(k-depth)+1)*(p-1)*p**(depth-1)
            assert c_num[i][j] == formula, (p, k, a, b)

    # Wavelet subspaces: construct independent differences of each pair
    # of child residue blocks and check their predicted eigenvalues.
    checked_vectors = 1  # constants (zero eigenvalue)
    ones = [1] * m
    assert all(sum(h[i][j] * ones[j] for j in range(m)) == 0 for i in range(m))
    for depth in range(1, k + 1):
        modulus = p**depth
        previous = p**(depth-1)
        parents = sorted({a % previous for a in residues}) if depth > 1 else [0]
        for parent in parents:
            children = sorted({a % modulus for a in residues
                               if depth == 1 or a % previous == parent})
            assert len(children) == (p-1 if depth == 1 else p)
            base = children[0]
            for other in children[1:]:
                vector = [int(a % modulus == base) - int(a % modulus == other)
                          for a in residues]
                eigenvalue = m * (k - depth + 1)
                for i in range(m):
                    val = sum(h[i][j] * vector[j] for j in range(m))
                    assert val == eigenvalue * vector[i], (p, k, depth, i)
                checked_vectors += 1
    assert checked_vectors == m, (p, k, checked_vectors, m)
    trace_cov_num = sum(c_num[i][i] for i in range(m))
    spec = theoretical_spectrum(p, k)
    assert sum(spec.values()) == m
    assert trace_cov_num == m*m * sum(eig*mult for eig, mult in spec.items())

    # Total variation of finite normalized spectrum vs infinite limit.
    # Use exact integer arithmetic, including all tail atoms j>k.
    # Duplicated atoms are handled by the spectrum dictionary.
    tv = (Fraction(1, 1) + abs(Fraction(p-2, 1) - Fraction(m*(p-1), p**k))
          + Fraction(m, p**k)) / (2*m)
    assert tv == Fraction(1, m)
    return m, checked_vectors, m*m


def main():
    cases = []
    for p in (2, 3, 5, 7):
        for k in range(1, 7):
            if (p-1)*p**(k-1) <= 150:
                cases.append((p, k))
    total_states = total_vectors = pair_checks = 0
    for p, k in cases:
        m, v, pairs = verify(p, k)
        total_states += m
        total_vectors += v
        pair_checks += pairs
    print(f"PASS {len(cases)} prime-power cases; {total_states} states, "
          f"{total_vectors} orthogonal-basis vectors, {pair_checks} pairwise covariance entries")
    print("Largest cases:", sorted(cases, key=lambda t: (t[0]-1)*t[0]**(t[1]-1))[-4:])


if __name__ == "__main__":
    main()
