"""Exact reproducibility checks for two-rung parallel-path network design.

Requires Python 3 and SymPy. Run: python verify_two_rungs.py
Finite tests corroborate, but do not replace, the all-order proof.
"""
from fractions import Fraction
from math import comb
import sympy as sp


def closed_kirchhoff(m, i, j):
    assert 2 <= m and 1 <= i < j <= m
    left, right, q = i - 1, m - j, j - i + 1
    return (Fraction(m * (5*m*m*q - 6*m*q*q + 12*m*q - 3*m
                         + 5*q**3 - 12*q*q + 2*q), 6*q)
            + Fraction(m * (left - right)**2, 2))


def predicted_pairs(m):
    k, residue = divmod(m, 5)
    if residue == 0:
        return {(k, 4*k), (k+1, 4*k+1)}
    return {(k+1, m-k)}


def matrix_kirchhoff(m, i, j):
    n = 2*m
    edges = [(z*m+t, z*m+t+1) for z in (0, 1) for t in range(m-1)]
    edges.extend([(i-1, m+i-1), (j-1, m+j-1)])
    L = sp.zeros(n)
    for u,v in edges:
        L[u,u] += 1
        L[v,v] += 1
        L[u,v] -= 1
        L[v,u] -= 1
    C = L + sp.ones(n, n)/n
    return sp.factor(n*C.inv().trace() - n)


def main():
    tested = 0
    # Independent exact inverse-Laplacian calculation on every small graph.
    for m in range(2, 8):
        for i in range(1, m):
            for j in range(i+1, m+1):
                expected = closed_kirchhoff(m, i, j)
                actual = matrix_kirchhoff(m, i, j)
                assert sp.Rational(expected.numerator, expected.denominator) == actual
                tested += 1
    # Independent brute-force minimizers for a substantial finite range.
    for m in range(2, 101):
        candidates = [(closed_kirchhoff(m,i,j), (i,j))
                      for i in range(1,m) for j in range(i+1,m+1)]
        best = min(z[0] for z in candidates)
        best_pairs = {pair for value,pair in candidates if value == best}
        assert best_pairs == predicted_pairs(m), (m, best_pairs)
        tested += len(candidates)
    print('VERIFY_OK', tested)


if __name__ == '__main__':
    main()
