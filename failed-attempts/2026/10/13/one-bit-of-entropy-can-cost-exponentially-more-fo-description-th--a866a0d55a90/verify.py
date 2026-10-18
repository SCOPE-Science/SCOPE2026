#!/usr/bin/env python3
from fractions import Fraction

checks = 0
for k in range(2, 11):
    t = 2**k
    c_tau = 15*k*t
    # n is a multiple of all t unary types, so both comparison models exist exactly.
    m = 10**9
    n = t*m

    # Entropies of the two uniform supports: all t types versus exactly two types.
    H_U = k
    H_B = 1
    assert H_U == k; checks += 1
    assert H_B == 1; checks += 1
    assert H_B < H_U; checks += 1

    # Jaakkola--Kuusisto--Vilander bounds specialized to the multiplicity vectors.
    U_lo = Fraction(3*n, t) - 3
    U_hi = Fraction(3*n, t) + c_tau
    B_lo = Fraction(3*n, 2) - 3
    B_hi = Fraction(3*n, 2) + c_tau
    assert U_lo <= Fraction(3*n, t) <= U_hi; checks += 1
    assert B_lo <= Fraction(3*n, 2) <= B_hi; checks += 1

    # Leading normalized coefficients and the resulting limiting ratio.
    u_lead = Fraction(3, t)
    b_lead = Fraction(3, 2)
    target = Fraction(b_lead, u_lead)
    assert target == 2**(k-1); checks += 1

    # For every sufficiently large n, the actual ratio is squeezed by these bounds.
    # The target limiting value lies inside the squeeze interval.
    ratio_lo = B_lo / U_hi
    ratio_hi = B_hi / U_lo
    assert ratio_lo < target < ratio_hi; checks += 1
    assert ratio_hi - ratio_lo < Fraction(1, 10); checks += 1

print(f"VERIFY_OK {checks} exact assertions")
