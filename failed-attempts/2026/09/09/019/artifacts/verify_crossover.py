#!/usr/bin/env python3
"""Lane-320 verifier: transverse systole crossover on a Bolza-symmetric FN-twist arc.

Stdlib only (math, json, os, fractions). Two layers:
  (A) EXACT rational checks (fractions.Fraction): det=1 for all committed matrices,
      closed-form trace coefficients, mirror symmetry, tau=0 values.
  (B) OUTWARD-ROUNDED float intervals: every op padded outward by 5 ULPs via
      math.nextafter; libm transcendentals (exp/log/sqrt) get additional 2e-15
      relative padding (libm error is ~1-2 ULP ~ 5e-16 relative, so this is ~4x
      generous). All safety margins below exceed interval widths by >= 6 orders
      of magnitude, so conclusions do not depend on fine rounding analysis.

On success prints VERIFY_OK and writes certified_values.json next to itself.
"""
import math
import json
import os
from fractions import Fraction as Q

ULPS = 5
LIBM_REL = 2e-15


def pad(lo, hi, rel=0.0):
    if rel:
        m = max(abs(lo), abs(hi))
        lo -= rel * m
        hi += rel * m
    for _ in range(ULPS):
        lo = math.nextafter(lo, -math.inf)
        hi = math.nextafter(hi, math.inf)
    return lo, hi


class Iv:
    """Closed float interval with outward-rounded arithmetic."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        if hi is None:
            hi = lo
        lo, hi = float(lo), float(hi)
        assert lo <= hi, (lo, hi)
        self.lo, self.hi = lo, hi

    def __add__(s, o):
        o = o if isinstance(o, Iv) else Iv(o)
        lo, hi = pad(s.lo + o.lo, s.hi + o.hi)
        return Iv(lo, hi)

    __radd__ = __add__

    def __neg__(s):
        return Iv(-s.hi, -s.lo)

    def __sub__(s, o):
        o = o if isinstance(o, Iv) else Iv(o)
        lo, hi = pad(s.lo - o.hi, s.hi - o.lo)
        return Iv(lo, hi)

    def __mul__(s, o):
        o = o if isinstance(o, Iv) else Iv(o)
        ps = (s.lo * o.lo, s.lo * o.hi, s.hi * o.lo, s.hi * o.hi)
        lo, hi = pad(min(ps), max(ps))
        return Iv(lo, hi)

    __rmul__ = __mul__

    def __truediv__(s, o):
        o = o if isinstance(o, Iv) else Iv(o)
        assert o.lo > 0, "only strictly-positive denominators occur here"
        ps = (s.lo / o.lo, s.lo / o.hi, s.hi / o.lo, s.hi / o.hi)
        lo, hi = pad(min(ps), max(ps))
        return Iv(lo, hi)

    def exp(s):
        lo, hi = pad(math.exp(s.lo), math.exp(s.hi), LIBM_REL)
        return Iv(lo, hi)

    def log(s):
        assert s.lo > 0
        lo, hi = pad(math.log(s.lo), math.log(s.hi), LIBM_REL)
        return Iv(lo, hi)

    def sqrt(s):
        assert s.lo >= 0
        lo, hi = pad(math.sqrt(s.lo), math.sqrt(s.hi), LIBM_REL)
        return Iv(lo, hi)

    def width(s):
        return s.hi - s.lo

    def __repr__(s):
        return "[%r, %r]" % (s.lo, s.hi)


# ---------------------------------------------------------------- exact layer
def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def mul2(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


XA = [[Q(1), Q(1, 2)], [Q(-1), Q(1, 2)]]
YA = [[Q(-1, 2), Q(-2)], [Q(1), Q(2)]]
XB = [[Q(1), Q(1)], [Q(-1, 2), Q(1, 2)]]
YB = [[Q(-1, 2), Q(-1)], [Q(2), Q(2)]]

exact = {}
for name, M in (("XA", XA), ("YA", YA), ("XB", XB), ("YB", YB)):
    assert det2(M) == 1, name
exact["det_committed_generators"] = 1

ALPHA = mul2(XA, YA)   # A(0): expect [[0,-1],[1,3]]
BETA = mul2(XB, YB)    # B(0): expect [[3/2,1],[5/4,3/2]]
assert ALPHA == [[Q(0), Q(-1)], [Q(1), Q(3)]], ALPHA
assert BETA == [[Q(3, 2), Q(1)], [Q(5, 4), Q(3, 2)]], BETA
assert det2(ALPHA) == 1 and det2(BETA) == 1
assert ALPHA[0][0] + ALPHA[1][1] == 3 and BETA[0][0] + BETA[1][1] == 3
exact["alpha_entries"] = "[[0,-1],[1,3]]"
exact["beta_entries"] = "[[3/2,1],[5/4,3/2]]"
exact["trace_at_zero"] = 3


def trace_coeffs(X, Y):
    """tr(X Tw Y Tw^-1) with Tw=diag(t,t^-1): c0 + cz*z + ci/z, z=t^2=e^tau."""
    c0 = X[0][0] * Y[0][0] + X[1][1] * Y[1][1]
    cz = X[1][0] * Y[0][1]
    ci = X[0][1] * Y[1][0]
    return c0, cz, ci


c0A, czA, ciA = trace_coeffs(XA, YA)
c0B, czB, ciB = trace_coeffs(XB, YB)
assert (c0A, czA, ciA) == (Q(1, 2), Q(2), Q(1, 2)), (c0A, czA, ciA)
assert (c0B, czB, ciB) == (Q(1, 2), Q(1, 2), Q(2)), (c0B, czB, ciB)
exact["trA_closed_form"] = "1/2 + 2*e^tau + (1/2)*e^-tau"
exact["trB_closed_form"] = "1/2 + (1/2)*e^tau + 2*e^-tau"
exact["mirror_trB_tau_eq_trA_minus_tau"] = True
exact["D_zero_exact"] = True   # D(0)=0 by exact mirror symmetry
exact["dtrA_zero"] = "3/2"     # 2 - 1/2
exact["dD_zero"] = "3"         # (3/2) - (-3/2)


def exp_frac(x, N=12):
    """Rigorous exp(x) as a Fraction interval via Taylor + Lagrange tail."""
    assert abs(x) <= Q(1, 2)
    S, p = Q(0), Q(1)
    for n in range(N + 1):
        if n > 0:
            p = p * x / n
        S += p
    import math as _m
    t = abs(x) ** (N + 1) / Q(_m.factorial(N + 1))
    T = t / (1 - abs(x) / (N + 2))
    return S - T, S + T


# Wolpert-derivative finite-difference cross-check on traces (exact rationals).
h = Q(1, 1000)
eph_lo, eph_hi = exp_frac(h)
emh_lo, emh_hi = exp_frac(-h)
# trA(h) = 1/2 + 2 e^h + (1/2) e^-h ; interval arithmetic on Fraction pairs
trAh = (Q(1, 2) + 2 * eph_lo + emh_lo / 2, Q(1, 2) + 2 * eph_hi + emh_hi / 2)
trAmh = (Q(1, 2) + 2 * emh_lo + eph_lo / 2, Q(1, 2) + 2 * emh_hi + eph_hi / 2)
FD_A = ((trAh[0] - trAmh[1]) / (2 * h), (trAh[1] - trAmh[0]) / (2 * h))
# trB mirror: FD_B should equal -FD_A reflected; check against -3/2
trBh = (Q(1, 2) + eph_lo / 2 + 2 * emh_lo, Q(1, 2) + eph_hi / 2 + 2 * emh_hi)
trBmh = (Q(1, 2) + emh_lo / 2 + 2 * eph_lo, Q(1, 2) + emh_hi / 2 + 2 * eph_hi)
FD_B = ((trBh[0] - trBmh[1]) / (2 * h), (trBh[1] - trBmh[0]) / (2 * h))
TOL = Q(1, 10 ** 6)
for v in FD_A:
    assert abs(v - Q(3, 2)) < TOL, v
for v in FD_B:
    assert abs(v + Q(3, 2)) < TOL, v
exact["FD_residual_bound"] = "< 1e-6"
exact["FD_A_interval_about_3/2"] = [float(FD_A[0]), float(FD_A[1])]
exact["FD_B_interval_about_-3/2"] = [float(FD_B[0]), float(FD_B[1])]

# ------------------------------------------------------------- interval layer
T = 0.25
ARC = Iv(-T, T)
Tm, Tp = Iv(-T), Iv(T)
Bm, Bp = Iv(0.01 - 5e-18, 0.01 + 5e-18), None  # placeholder
Bm = Iv(-0.010000000000000002, -0.009999999999999998)
Bp = Iv(0.009999999999999998, 0.010000000000000002)


def trA(t):
    return Iv(0.5) + Iv(2) * t.exp() + Iv(0.5) * (-t).exp()


def trB(t):
    return Iv(0.5) + Iv(0.5) * t.exp() + Iv(2) * (-t).exp()


def dtrA(t):
    return Iv(2) * t.exp() - Iv(0.5) * (-t).exp()


def dtrB(t):
    return Iv(0.5) * t.exp() - Iv(2) * (-t).exp()


def len_of_tr(TR):
    hh = TR / Iv(2)
    return Iv(2) * (hh + (hh * hh - Iv(1)).sqrt()).log()


def dlen_of(TR, DTR):
    hh = TR / Iv(2)
    return DTR / (hh * hh - Iv(1)).sqrt()


def D_of(t):
    return len_of_tr(trA(t)) - len_of_tr(trB(t))


res = dict(exact)
res["T"] = T

# (1) Hyperbolicity + strict increase of trA (tr'' > 0 needs no dependency trick:
#     every term of tr'' is a positive interval).
d2 = Iv(2) * ARC.exp() + Iv(0.5) * (-ARC).exp()
assert d2.lo > 0, d2
trA_lo_pt, trA_hi_pt = trA(Tm), trA(Tp)
trB_lo_pt, trB_hi_pt = trB(Tp), trB(Tm)  # trB decreasing: mirror
assert trA_lo_pt.lo >= 2.6, trA_lo_pt
assert trB_hi_pt.lo >= 2.6, trB_hi_pt  # min of trB over arc, at +T
res["trace_min_over_arc"] = min(trA_lo_pt.lo, trB_hi_pt.lo)
res["trace_max_over_arc"] = max(trA_hi_pt.hi, trB_lo_pt.hi)

# (2) Twist-derivative sign intervals (Wolpert derivatives along the twist flow).
dtr_rng = Iv(dtrA(Tm).lo, dtrA(Tp).hi)      # trA' increasing (tr''>0)
den_rng = Iv(trA_lo_pt.lo, trA_hi_pt.hi)    # tight: monotonicity, no dependency
hh = den_rng / Iv(2)
denom = (hh * hh - Iv(1)).sqrt()
lpA_lo = dtr_rng.lo / denom.hi
lpA_hi = dtr_rng.hi / denom.lo
assert lpA_lo >= 0.6, (lpA_lo, lpA_hi)
res["lA_prime_range"] = [lpA_lo, lpA_hi]
res["lB_prime_range"] = [-lpA_hi, -lpA_lo]  # exact mirror symmetry
assert -lpA_lo <= -0.6
dmin = lpA_lo
assert 2 * dmin >= 1.2
res["D_prime_lower_bound"] = 2 * dmin

# (3) Endpoint-sign-reversal bracket: unique zero in [-0.01, 0.01].
Dm, Dp = D_of(Bm), D_of(Bp)
assert Dm.hi < 0 < Dp.lo, (Dm, Dp)
res["D_minus_0.01"] = [Dm.lo, Dm.hi]
res["D_plus_0.01"] = [Dp.lo, Dp.hi]
res["crossover_interval"] = [-0.01, 0.01]
res["crossover_width"] = 0.02

# (4) Tracked-systole intervals at -T, 0, +T (widths << 0.05) + leadership.
lA_m, lB_m = len_of_tr(trA(Tm)), len_of_tr(trB(Tm))
lA_0, lB_0 = len_of_tr(trA(Iv(0.0))), len_of_tr(trB(Iv(0.0)))
lA_p, lB_p = len_of_tr(trA(Tp)), len_of_tr(trB(Tp))
assert lA_m.hi < lB_m.lo, (lA_m, lB_m)   # A leads at -T
assert lB_p.hi < lA_p.lo, (lA_p, lB_p)   # B leads at +T
assert lA_0.lo <= lB_0.hi and lB_0.lo <= lA_0.hi  # tie at 0
for name, L in (("m(-T)", lA_m), ("m(0)", lA_0), ("m(+T)", lB_p)):
    assert L.width() <= 0.05, (name, L)
    res["systole_%s" % name] = [L.lo, L.hi]
res["systole_widths_max"] = max(lA_m.width(), lA_0.width(), lB_p.width())
res["leadership_margin_minus_T"] = lB_m.lo - lA_m.hi
res["leadership_margin_plus_T"] = lA_p.lo - lB_p.hi

# (5) Bolza separating length + gap vs tracked systole across the whole arc.
#     sqrt(2) in [1.4142, 1.4143]: integer-verified 14142^2 < 2*10^8 < 14143^2.
assert 14142 ** 2 < 2 * 10000 ** 2 < 14143 ** 2
s2 = Iv(1.4142, 1.4143)
ss = Iv(1) + s2
E = ss + (ss * ss - Iv(1)).sqrt()
l0 = Iv(2) * E.log()
assert 3.05 < l0.lo and l0.hi < 3.06, l0
# max over arc of tracked systole <= l(0): for tau<=0 winner is A (D<0 by
# monotonicity + exact D(0)=0) with lA increasing; mirror for tau>=0.
gap = l0.lo - lA_0.hi
assert gap >= 1.0, gap
res["l0_Bolza_separating"] = [l0.lo, l0.hi]
res["l_star_center"] = [lA_0.lo, lA_0.hi]
res["separating_gap_lower_bound"] = gap

# (6) McShane-type summand spot check: partial sums over Dehn orbits |k|<=6 at
#     tau in {-T, 0, T}, plus certified geometric tail < 1e-6.
E2 = E * E
assert E2.lo > 1


def E_pow(n):
    assert isinstance(n, int)
    if n == 0:
        return Iv(1)
    if n < 0:
        return Iv(1) / E_pow(-n)
    out = Iv(1)
    for _ in range(n):
        out = out * E
    return out


def trAk(k, t):
    u = E_pow(2 * k)
    return Iv(0.5) + Iv(2) * u * t.exp() + Iv(0.5) * (Iv(1) / u) * (-t).exp()


def trBk(k, t):
    u = E_pow(2 * k)
    return Iv(0.5) + Iv(0.5) * u * t.exp() + Iv(2) * (Iv(1) / u) * (-t).exp()


def summand(L):
    return Iv(2) / (Iv(1) + (L / Iv(2)).exp())


for tname, tv in (("minus_T", Tm), ("zero", Iv(0.0)), ("plus_T", Tp)):
    S = Iv(0)
    for k in range(-6, 7):
        S = S + summand(len_of_tr(trAk(k, tv)))
        S = S + summand(len_of_tr(trBk(k, tv)))
    res["MM_partial_sum_%s_K6" % tname] = [S.lo, S.hi]
    res["MM_partial_width_%s" % tname] = S.width()

Elo = E.lo
tail_up = (8 * math.nextafter(math.exp(0.25), math.inf) * (1 + 1e-12)
           * Elo ** -14 / (1 - Elo ** -2))
assert tail_up < 1e-6, tail_up
res["MM_tail_upper_bound"] = tail_up

res["status"] = "VERIFY_OK"

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "certified_values.json"), "w") as f:
    json.dump(res, f, indent=1)
print("VERIFY_OK")
print(json.dumps({k: res[k] for k in (
    "trace_min_over_arc", "lA_prime_range", "D_prime_lower_bound",
    "D_minus_0.01", "D_plus_0.01", "l0_Bolza_separating", "l_star_center",
    "separating_gap_lower_bound", "MM_tail_upper_bound")}, indent=1))
