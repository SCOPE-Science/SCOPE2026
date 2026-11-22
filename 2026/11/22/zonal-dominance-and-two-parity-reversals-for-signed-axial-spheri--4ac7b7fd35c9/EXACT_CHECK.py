#!/usr/bin/env python3
"""Exact rational certificates for parity reversals of axial spherical heat covariance.

Uses only Python's standard library. No floating-point decisions are made.
"""
from fractions import Fraction as Q

L = 16
CASES = (
    (Q(13, 5), 1, Q(14, 5), 0, Q(16, 5)),
    (Q(3), 0, Q(3, 2), 1, Q(9, 5)),
    (Q(5), 1, Q(7, 10), 0, Q(6, 5)),
)


def upper_link_sq(l, b):
    """Squared C_{l+1,l} in the zonal (m=0) block."""
    assert l >= 0 and b > 2
    return Q((l + 1) ** 2, (2 * l + 1) * (2 * l + 3)) * Q(2) ** ((l + 1) * (l + 2)) / b ** (l * (l + 1))


def lower_link_sq(l, b):
    """Squared C_{l-1,l}; zero at l=0."""
    if not l:
        return Q(0)
    return Q(l ** 2, (2 * l - 1) * (2 * l + 1)) * Q(2) ** ((l - 1) * l) / b ** (l * (l + 1))


def jacobi_data(b, parity):
    """Rational diagonal and squared off-diagonal of C_p^* C_p, columns l<L."""
    indices = list(range(parity, L, 2))
    diag = [upper_link_sq(l, b) + lower_link_sq(l, b) for l in indices]
    off2 = [upper_link_sq(indices[i], b) * lower_link_sq(indices[i + 1], b)
            for i in range(len(indices) - 1)]
    return diag, off2


def exact_positive_definite(b, parity, bound):
    """Sylvester test via rational LDL pivots for bound*I - C_p^*C_p."""
    diag, off2 = jacobi_data(b, parity)
    pivots = []
    for i, x in enumerate(diag):
        pivot = bound - x if i == 0 else bound - x - off2[i - 1] / pivots[-1]
        pivots.append(pivot)
    return all(x > 0 for x in pivots), tuple(1 if x > 0 else -1 if x < 0 else 0 for x in pivots)


def tail_bound_exact(b):
    """Squared Hilbert-Schmidt error of the truncation is <4*U_L."""
    u_l = Q(2) ** ((L + 1) * (L + 2)) / b ** (L * (L + 1))
    ratio = Q(2) ** (2 * L + 4) / b ** (2 * L + 2)
    assert ratio < Q(1, 2)  # ratio decreases with index since b>2
    assert 4 * u_l < Q(1, 10 ** 18)
    return 4 * u_l


def main():
    for b, upper_parity, upper_pre, lower_parity, lower_cut in CASES:
        assert b > 2
        tail_bound_exact(b)
        ok, signs = exact_positive_definite(b, upper_parity, upper_pre)
        assert ok, (b, upper_parity, signs)
        # True infinite upper bound is < (sqrt(upper_pre) + 10^-9)^2.
        # Because upper_pre<4, this is < upper_pre + 4*10^-9 + 10^-18.
        assert upper_pre < 4
        upper_full = {Q(13,5):Q(3), Q(3):Q(8,5), Q(5):Q(4,5)}[b]
        assert upper_pre + Q(4, 10 ** 9) + Q(1, 10 ** 18) < upper_full
        _, lower_signs = exact_positive_definite(b, lower_parity, lower_cut)
        assert -1 in lower_signs, (b, lower_parity, lower_signs)
        # For the first negative LDL pivot, a leading principal minor is not positive.
        assert lower_cut > upper_full
        print('b=%s: parity %s norm^2 < %s; parity %s norm^2 > %s; tail^2 < 10^-18'
              % (b, 'odd' if upper_parity else 'even', upper_full,
                 'odd' if lower_parity else 'even', lower_cut))
    # Compact independent lower certificates for the selected witnesses:
    b = Q(13,5)
    a0 = upper_link_sq(0,b) + lower_link_sq(0,b)
    a2 = upper_link_sq(2,b) + lower_link_sq(2,b)
    det = (Q(16,5) - a0)*(Q(16,5) - a2) - upper_link_sq(0,b)*lower_link_sq(2,b)
    assert det == -Q(48529856,120670225)
    assert upper_link_sq(1,Q(3)) + lower_link_sq(1,Q(3)) > Q(9,5)
    assert upper_link_sq(0,Q(5)) == Q(4,3) > Q(6,5)
    print('All exact rational certificates passed.')

if __name__ == '__main__':
    main()
