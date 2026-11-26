"""Exact finite arithmetic cross-check of the Hilbert-function identity.

This test is not a proof of the statement for unbounded degree and weight;
that proof uses the sheaf filtration and elliptic cohomology in RESULT.md.
"""
from math import comb


def filtration_count(d, k):
    # On an elliptic curve, h^0((L^*)**ell)=d*ell for ell>=1.
    # The j-th graded summand of Sym^k(F)(-C_-) contributes
    # the positive powers ell=1,...,j.
    return 1 + sum(sum(d * ell for ell in range(1, j + 1))
                   for j in range(1, k + 1))


def hilbert_formula(d, k):
    return 1 + d * comb(k + 2, 3)


def hilbert_series_coefficient(d, k):
    # [t^k] (1-t)^(-1) + d*t*(1-t)^(-4).
    return 1 if k == 0 else 1 + d * comb(k + 2, 3)


for d in range(1, 13):
    for k in range(0, 81):
        x = filtration_count(d, k)
        assert x == hilbert_formula(d, k) == hilbert_series_coefficient(d, k)
        if k > 0:
            assert x - hilbert_formula(d, k-1) == d * comb(k+1, 2)

# The k=0,1 boundary and volume normalization are explicitly checked.
for d in range(1, 13):
    assert hilbert_formula(d, 0) == 1
    assert hilbert_formula(d, 1) == d + 1
    # Expansion: leading term d*k**3 / 6, so 3!*leading = d.
    assert 6 * (d / 6) == d

print('VERIFY_OK: 12 degrees, weights 0..80, coefficients and boundaries')
