#!/usr/bin/env python3
"""Certified P2(HN) interval via maximal-subgroup union bound (stdlib only).

Inputs (transcribed from the online ATLAS page for HN, v3 spor/HN):
  |G| = |HN| = 273030912000000 (the 1A centralizer = group order).
  14 maximal-subgroup rows: (name, order, index) with order*index == |G|.

Route:
  Union bound: for each maximal H_i with index m_i=[G:H_i] and n_i conjugates,
    n_i <= m_i, P(pair lies in some conjugate of H_i) <= n_i*(1/m_i)^2 <= 1/m_i.
  So Q = P(non-generating) <= S := sum_i 1/m_i.
  Lower bound on Q: one fixed conjugate H_0 (A12, m_1=1140000) gives
    Q >= P(both entries in H_0) = 1/m_1^2.
  Hence P2 = 1-Q lies in [1-S, 1-1/m_1^2].

All arithmetic exact (Fractions); decimals rounded outward for the certificate.
"""
from fractions import Fraction

G = 273030912000000
# (name, order, index) in ATLAS page order
MAXIMALS = [
    ("A12", 239500800, 1140000),
    ("2.HS.2", 177408000, 1539000),
    ("U3(8):3", 16547328, 16500000),
    ("2^1+8.(A5xA5).2", 3686400, 74064375),
    ("(D10xU3(5)).2", 2520000, 108345600),
    ("5^1+4.2^1+4.5.4", 2000000, 136515456),
    ("2^6.U4(2)", 1658880, 164587500),
    ("(A6xA6).D8", 1036800, 263340000),
    ("2^3+2+6.(3xL3(2))", 1032192, 264515625),
    ("5^2+1+2.4.A5", 750000, 364041216),
    ("M12:2 (I)", 190080, 1436400000),
    ("M12:2 (II)", 190080, 1436400000),
    ("3^4:2.(A4xA4).4", 93312, 2926000000),
    ("3^1+4:4.A5", 58320, 4681600000),
]

def main():
    # 1) order factorisation check
    n, fac = G, {}
    for p in (2, 3, 5, 7, 11, 19):
        c = 0
        while n % p == 0:
            n //= p
            c += 1
        fac[p] = c
    assert n == 1, f"|HN| has unfactored rest {n}"
    assert fac == {2: 14, 3: 6, 5: 6, 7: 1, 11: 1, 19: 1}, fac
    # 2) order*index == |G| for every row
    for name, o, m in MAXIMALS:
        assert o * m == G, (name, o, m)

    m1 = MAXIMALS[0][2]
    S = sum(Fraction(1, m) for _, _, m in MAXIMALS)
    assert S == Fraction(6979253, 4266108000000), S
    q_lo = Fraction(1, m1 * m1)   # 1/1140000^2
    L_exact, U_exact = 1 - S, 1 - q_lo
    width = S - q_lo            # == U_exact - L_exact
    assert L_exact < U_exact and width < Fraction(5, 100), width
    assert L_exact > Fraction(85, 100), L_exact

    # Outward-rounded 9-decimal certificate:
    # L_cert <= L_exact: truncate; U_cert >= U_exact: round up.
    from math import floor, ceil
    D = 10 ** 9
    L_cert = Fraction(floor(L_exact * D), D)
    U_cert = Fraction(ceil(U_exact * D), D)
    assert L_cert <= L_exact <= U_exact <= U_cert
    assert U_cert - L_cert < Fraction(5, 100) and L_cert > Fraction(85, 100)

    print(f"|HN| = {G} = 2^14*3^6*5^6*7*11*19")
    print(f"S = sum 1/m_i = {S} ~= {float(S):.6e}")
    print(f"[L,U]_exact = [{L_exact}, {U_exact}]")
    print(f"L_dec ~= {float(L_exact):.12f}   U_dec ~= {float(U_exact):.12f}")
    print(f"width ~= {float(width):.4e}")
    print(f"CERTIFIED: P2(HN) in [{L_cert} ] == "
          f"[{float(L_cert):.9f}, {float(U_cert):.9f}], "
          f"width {(float(U_cert - L_cert)):.3e}")
    assert L_cert == Fraction(999998364, 10 ** 9), L_cert
    assert U_cert == Fraction(1000000000, 10 ** 9), U_cert
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
