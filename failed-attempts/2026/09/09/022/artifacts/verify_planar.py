#!/usr/bin/env python3
"""Rigorously enclose the three principal planar perimeters of E0 (stdlib only).

E0: x^2/1 + y^2/1.2^2 + z^2/1.5^2 = 1.
Coordinate-plane sections are ellipses with semi-axes pairs
  x=0: (1.2, 1.5),  y=0: (1.0, 1.5),  z=0: (1.0, 1.2).
Perimeter P = 4*Amax*E(m), E(m) = complete elliptic integral of 2nd kind,
m = k^2 = 1-(Amin/Amax)^2, an exact rational in each case (9/25, 5/9, 11/36).

E(m) = (pi/2) * (1 - sum_{n>=1} b_n m^n),
  b_n = ((2n-1)!!/(2n)!!)^2/(2n-1) > 0,  b_{n+1}/b_n < 1 (exact integer check).
Tail bound: sum_{n>N} b_n m^n <= b_{N+1} m^{N+1}/(1-m).
pi enclosed by Machin 16*atan(1/5)-4*atan(1/239) with alternating-series bounds.
All arithmetic in Fraction (exact); only printed floats are non-rigorous display.
Pass criteria: each width <= 1e-4 and ordering intervals disjoint.
"""
from fractions import Fraction

def atan_bounds(x: Fraction, last_even: int):
    """Return (lo,hi) enclosing atan(x) for 0<x<=1/5.
    Alternating series a_n=x^{2n+1}/(2n+1), verified decreasing; S_even>=L>=S_odd."""
    assert x > 0 and x <= Fraction(1, 5)
    terms = []
    for n in range(last_even + 2):
        a = x ** (2 * n + 1) / (2 * n + 1)
        terms.append(a)
    for n in range(len(terms) - 1):
        assert terms[n] > terms[n + 1] > 0  # decreasing -> Leibniz bounds valid
    s_hi = sum(terms[n] if n % 2 == 0 else -terms[n] for n in range(last_even + 1))
    s_lo = s_hi - terms[last_even + 1]
    return s_lo, s_hi  # last_even even -> S_even upper; minus next term -> lower

def pi_bounds():
    a1_lo, a1_hi = atan_bounds(Fraction(1, 5), 30)
    a2_lo, a2_hi = atan_bounds(Fraction(1, 239), 8)
    return 16 * a1_lo - 4 * a2_hi, 16 * a1_hi - 4 * a2_lo

def E_bounds(m: Fraction, N: int, pi_lo: Fraction, pi_hi: Fraction):
    b = Fraction(1, 4)  # b_1
    s = Fraction(1) - b * m
    assert N >= 2
    for n in range(1, N):
        # b_{n+1} = b_n * (2n+1)(2n-1)/(2n+2)^2 ; factor < 1 checked exactly
        num = (2 * n + 1) * (2 * n - 1)
        den = (2 * n + 2) ** 2
        assert num < den
        b = b * num / den
        s = s - b * m ** (n + 1)
    # one more term for tail
    num = (2 * N + 1) * (2 * N - 1)
    den = (2 * N + 2) ** 2
    assert num < den
    b_next = b * num / den
    assert b_next > 0
    tail = b_next * m ** (N + 1) / (1 - m)
    S_hi, S_lo = s, s - tail
    assert S_lo < S_hi and S_lo > 0
    return pi_lo / 2 * S_lo, pi_hi / 2 * S_hi

def main():
    pi_lo, pi_hi = pi_bounds()
    print("pi in [%.15f, %.15f]" % (float(pi_lo), float(pi_hi)))
    assert pi_hi - pi_lo < Fraction(10) ** -12
    cases = [
        ("x=0", Fraction("1.2"), Fraction("1.5")),
        ("y=0", Fraction(1), Fraction("1.5")),
        ("z=0", Fraction(1), Fraction("1.2")),
    ]
    results = {}
    ok = True
    for name, A, B in cases:
        Amax, Amin = max(A, B), min(A, B)
        m = 1 - (Amin / Amax) ** 2
        Elo, Ehi = E_bounds(m, 25, pi_lo, pi_hi)
        Plo, Phi = 4 * Amax * Elo, 4 * Amax * Ehi
        w = Phi - Plo
        passed = w <= Fraction(10) ** -4
        ok = ok and passed
        results[name] = (Plo, Phi)
        print("%s section axes (%s,%s) m=%s" % (name, A, B, m))
        print("  P in [%.10f, %.10f] width=%.3e %s" % (float(Plo), float(Phi), float(w), "PASS" if passed else "FAIL"))
    # ordering: z=0 shortest, then y=0, then x=0; disjointness
    z, y, x = results["z=0"], results["y=0"], results["x=0"]
    assert x[0] > y[1] and y[0] > z[1], "ordering/disjointness failed"
    gmin1 = y[0] - z[1]
    gmin2 = x[0] - y[1]
    print("minimizer: z=0; separation gaps >= %.6f and >= %.6f (both > 0)" % (float(gmin1), float(gmin2)))
    print("VERIFY_OK" if ok else "VERIFY_FAIL")

if __name__ == "__main__":
    main()
