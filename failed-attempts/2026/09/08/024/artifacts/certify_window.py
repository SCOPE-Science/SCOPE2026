"""Exact-rational (stdlib-only) certificate for an index-1 non-meridional
closed-geodesic length window on the triaxial ellipsoid (a,b,c)=(1,23/20,27/20).

Object: the z=0 principal ellipse (semiaxes a=1, b=23/20). It is an exact
closed geodesic by the reflection isometry (x,y,z)->(x,y,-z).

Method (fully rigorous, no floating point):
  * pi enclosure via Machin  pi = 16*arctan(1/5) - 4*arctan(1/239)
    with Leibniz alternating-series remainders (Fractions).
  * Ellipse perimeters P = 4*q*E(m), m = 1-p^2/q^2, via the power series
      E(m) = (pi/2)*[1 - sum_{n>=1} C(2n,n)^2 m^n/(16^n (2n-1))]
    with the explicit tail bound  m^{N+1}/((2N+1)(1-m))  (every series
    coefficient is <= 1 since C(2n,n) <= 4^n).
  * Gaussian-curvature bounds along the loop are exact rationals:
      Kmin = a^2/(b^2 c^2),  Kmax = b^2/(a^2 c^2).
  * Square roots bounded rigorously by integer arithmetic (math.isqrt).
  * Conjugate-point count by classical Sturm comparison:
      d1 (first zero) in [pi/sqrt(Kmax), pi/sqrt(Kmin)],
      d2 (second zero) in [2 pi/sqrt(Kmax), 2 pi/sqrt(Kmin)].
    d1_hi < L_lo  =>  at least one conjugate point in (0,L) (based index>=1).
    d2_lo > L_hi  =>  at most one (based index<=1). Hence based index = 1.
  * Free-loop (periodic) index = 1 by the constant test field (index>=1,
    since K>0) and the sharp Wirtinger bound (index<=1, using L < 2pi/sqrt(Kmax)).

Comparison meridian M: perimeter of the (1,27/20) ellipse = meridian length
of the revolution spheroid obtained by rotating the y=0 section about the
z-axis. The loop (in plane z=0) is transverse to that meridian foliation,
hence non-meridional.

Replay:  python3 certify_window.py   (stdlib only, seconds)
"""
from fractions import Fraction
from math import comb, isqrt


def arctan_inv_window(q, N):
    """Two-sided window for arctan(1/q), integer q>=1, Leibniz remainder."""
    q = int(q)
    S = Fraction(0)
    for n in range(N + 1):
        S += Fraction((-1) ** n, (2 * n + 1) * q ** (2 * n + 1))
    R = Fraction(1, (2 * (N + 1) + 1) * q ** (2 * (N + 1) + 1))
    return S - R, S + R


def pi_window():
    a5_lo, a5_hi = arctan_inv_window(5, 8)
    a239_lo, a239_hi = arctan_inv_window(239, 3)
    return 16 * a5_lo - 4 * a239_hi, 16 * a5_hi - 4 * a239_lo


def enorm_window(m, N):
    """Window for En(m) = E(m)/(pi/2) = 1 - sum_{n>=1} c_n m^n/(2n-1),
    0<m<1, where 0<c_n=(C(2n,n)/4^n)^2<=1. Tail<=m^{N+1}/((2N+1)(1-m))."""
    assert Fraction(0) < m < Fraction(1)
    S = Fraction(1)
    for n in range(1, N + 1):
        S -= Fraction(comb(2 * n, n) ** 2, 16 ** n) * m ** n / (2 * n - 1)
    tail = m ** (N + 1) / ((2 * N + 1) * (1 - m))
    return S - tail, S + tail


def sqrt_window(f):
    """Two-sided window for sqrt(f), f a positive Fraction, via isqrt."""
    assert f > 0
    p, q = f.numerator, f.denominator
    r = isqrt(p * q)  # floor(sqrt(p*q)); sqrt(p/q) = sqrt(pq)/q
    return Fraction(r, q), Fraction(r + 1, q)


def perimeter_window(p_num, p_den, q_num, q_den, pi_lo, pi_hi, N=25):
    """Perimeter of the ellipse with semiaxes 0<p<q: P = 4 q (pi/2) En(m)."""
    from fractions import Fraction as F
    p, q = F(p_num, p_den), F(q_num, q_den)
    assert p < q
    m = 1 - p * p / (q * q)
    e_lo, e_hi = enorm_window(m, N)
    assert e_lo > 0
    return 4 * q * (pi_lo / 2) * e_lo, 4 * q * (pi_hi / 2) * e_hi


def main():
    pi_lo, pi_hi = pi_window()
    print("pi in [%.15f, %.15f], width = %.3g"
          % (float(pi_lo), float(pi_hi), float(pi_hi - pi_lo)))

    # z=0 equatorial ellipse, semiaxes (1, 23/20): exact closed geodesic.
    L_lo, L_hi = perimeter_window(1, 1, 23, 20, pi_lo, pi_hi)
    # meridian section (y=0 plane), semiaxes (1, 27/20).
    M_lo, M_hi = perimeter_window(1, 1, 27, 20, pi_lo, pi_hi)
    print("L in [%.12f, %.12f], relwidth = %.3g"
          % (float(L_lo), float(L_hi), float((L_hi - L_lo) / L_lo)))
    print("M in [%.12f, %.12f]"
          % (float(M_lo), float(M_hi)))

    # Exact curvature bounds along z=0: Kmin=a^2/(b^2c^2), Kmax=b^2/(a^2c^2).
    a = Fraction(1)
    b = Fraction(23, 20)
    c = Fraction(27, 20)
    Kmin = a * a / (b * b * c * c)
    Kmax = b * b / (a * a * c * c)
    print("Kmin = %s = %.9f" % (Kmin, float(Kmin)))
    print("Kmax = %s = %.9f" % (Kmax, float(Kmax)))
    skmin_lo, skmin_hi = sqrt_window(Kmin)
    skmax_lo, skmax_hi = sqrt_window(Kmax)

    d1_lo, d1_hi = pi_lo / skmax_hi, pi_hi / skmin_lo
    d2_lo, d2_hi = 2 * pi_lo / skmax_hi, 2 * pi_hi / skmin_lo
    print("d1 in [%.6f, %.6f]" % (float(d1_lo), float(d1_hi)))
    print("d2 in [%.6f, %.6f]" % (float(d2_lo), float(d2_hi)))

    checks = []
    # (T1) length window relative width <= 0.5%
    checks.append(("T1 width<=0.5%", (L_hi - L_lo) / L_lo <= Fraction(1, 200)))
    # (T2) beating margin, conservative: (Mlo-Lhi)/Mhi >= 2%
    checks.append(("T2 margin>=2%", (M_lo - L_hi) / M_hi >= Fraction(1, 50)))
    # (T3) first conjugate point strictly inside: d1_hi < L_lo (index>=1)
    checks.append(("T3 d1<L (idx>=1)", d1_hi < L_lo))
    # (T4) second zero strictly outside: d2_lo > L_hi (idx<=1, +Wirtinger hyp.)
    checks.append(("T4 d2>L (idx<=1)", d2_lo > L_hi))
    # (T5) strict window separation
    checks.append(("T5 Lhi<Mlo", L_hi < M_lo))
    # (T6) sanity vs crude circle bounds: 2pi*1 < L < 2pi*1.15
    checks.append(("T6 circle sandwich",
                   2 * pi_lo < L_lo and L_hi < 2 * pi_hi * b))
    for name, ok in checks:
        print("%s : %s" % (name, "PASS" if ok else "FAIL"))
    margin = (M_lo - L_hi) / M_hi
    print("certified conservative margin (Mlo-Lhi)/Mhi >= %.6f (%.3f%%)"
          % (float(margin), 100 * float(margin)))
    print("based-loop Morse index = 1; free-loop (periodic) Morse index = 1.")
    assert all(ok for _, ok in checks), "CERTIFICATE FAILED"
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
