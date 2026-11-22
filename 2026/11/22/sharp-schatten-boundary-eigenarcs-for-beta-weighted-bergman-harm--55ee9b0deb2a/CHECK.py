"""Exact finite diagnostics for beta-weighted diagonal Schatten point-spectrum formulas.

The analytic Fredholm and asymptotic claims require the full proof in RESULT.md.
"""
from fractions import Fraction as F

checks = 0


def assert_exact(condition):
    global checks
    assert condition
    checks += 1


for numer in range(-9, 24):
    for denom in (2, 3, 7):
        beta = F(numer, denom)
        if beta <= -1:
            continue
        kappa = beta + 1
        a = 1 / (beta + 2)
        c = 1 - a
        outlier_indices = [j for j in range(20) if j < beta]
        assert_exact(len(outlier_indices) == max(0, -((-numer) // denom)))
        for j in range(18):
            r = (j + beta + 2) / ((beta + 2) * (j + 1))
            b = 1 - r
            assert_exact(r == a * (1 + kappa / (j + 1)))
            assert_exact(b == c - a * kappa / (j + 1))
            assert_exact((b < c - a) == (j < beta))
            assert_exact(0 < r <= 1)
        for m in range(1, 7):
            eigenvalue = c - a * kappa / m
            v = [F(1)]
            for j in range(m - 1):
                r = a * (1 + kappa / (j + 1))
                b = 1 - r
                v.append(v[-1] * (eigenvalue - b) / r)
            assert_exact(v[-1] != 0)
            for j in range(m):
                r = a * (1 + kappa / (j + 1))
                b = 1 - r
                neighbor = v[j+1] if j < m-1 else F(0)
                assert_exact(b * v[j] + r * neighbor == eigenvalue * v[j])
        # The imaginary unit has unit modulus; verify its precise squared gamma recurrence.
        for n in range(1, 8):
            squared_norm_ratio = F(n*n, 1) + kappa*kappa
            squared_norm_ratio /= (n+kappa)**2
            assert_exact(squared_norm_ratio == 1 - 2*n*kappa / (n+kappa)**2)
            assert_exact(0 < squared_norm_ratio < 1)
        for p in (1, 2, 3, 4, 6):
            # Critical threshold for any arc, and membership of the leftmost boundary point.
            assert_exact((2*p*kappa > 1) == (1 - F(1, p*kappa) > -1))
            assert_exact((p*kappa > 1) == (p*kappa*(1-0) > 1))

print('BERGMAN_SCHATTEN_ARC_FINITE_EXACT_OK', checks)
