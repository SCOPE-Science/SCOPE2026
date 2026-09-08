#!/usr/bin/env python3
"""Lane 96 verifier: certified local data, torsion, rank>=2, bounded integral search
for 4006a1 (Ea) and 4006b1 (Eb). Stdlib only, exact integer/Fraction arithmetic."""
import math
from fractions import Fraction

Ea = dict(name="4006a1", a=(1, -1, 0, 4, -2),
          P1=(Fraction(1), Fraction(1)), P2=(Fraction(3), Fraction(4)))
Eb = dict(name="4006b1", a=(1, 0, 0, -87, 361),
          P1=(Fraction(6), Fraction(5)), P2=(Fraction(22), Fraction(85)))
CURVES = [Ea, Eb]
out = {"curves": {}}


def inv(a):
    a1, a2, a3, a4, a6 = a
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    c4 = b2 * b2 - 24 * b4
    c6 = -b2 ** 3 + 36 * b2 * b4 - 216 * b6
    D = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
    return dict(b2=b2, b4=b4, b6=b6, b8=b8, c4=c4, c6=c6, D=D)


def on_curve(a, P):
    a1, a2, a3, a4, a6 = a
    x, y = P
    return y * y + a1 * x * y + a3 * y - (x ** 3 + a2 * x * x + a4 * x + a6) == 0


def neg(a, P):
    if P is None:
        return None
    a1, a2, a3, a4, a6 = a
    x, y = P
    return (x, -y - a1 * x - a3)


def add(a, P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    a1, a2, a3, a4, a6 = a
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2:
        if y1 + y2 + a1 * x1 + a3 == 0:
            return None
        lam = (3 * x1 * x1 + 2 * a2 * x1 + a4 - a1 * y1) / (2 * y1 + a1 * x1 + a3)
    else:
        lam = (y2 - y1) / (x2 - x1)
    nu = y1 - lam * x1
    x3 = lam * lam + a1 * lam - a2 - x1 - x2
    y3 = -(lam + a1) * x3 - nu - a3
    return (x3, y3)


def count_modp(a, p):
    a1, a2, a3, a4, a6 = a
    n = 1
    for x in range(p):
        for y in range(p):
            if (y * y + a1 * x * y + a3 * y - (x ** 3 + a2 * x * x + a4 * x + a6)) % p == 0:
                n += 1
    return n


def sing_pt_modp(a, p):
    a1, a2, a3, a4, a6 = a
    F = lambda x, y: (y * y + a1 * x * y + a3 * y - (x ** 3 + a2 * x * x + a4 * x + a6)) % p
    Fx = lambda x, y: (a1 * y - (3 * x * x + 2 * a2 * x + a4)) % p
    Fy = lambda x, y: (2 * y + a1 * x + a3) % p
    return [(x, y) for x in range(p) for y in range(p)
            if F(x, y) == 0 and Fx(x, y) == 0 and Fy(x, y) == 0]


def split_modp(a, p, pt):
    a1, a2, a3, a4, a6 = a
    x0, y0 = pt
    cXX = (-3 * x0 - a2) % p
    cXY = (a1) % p
    if p == 2:
        # binary quadratic cXX X^2 + cXY XY + Y^2 over F2: node is split iff it
        # has 2 projective zeros, nonsplit iff 0 (anisotropic, e.g. X^2+XY+Y^2)
        nroots = sum(1 for X, Y in [(1, 0), (0, 1), (1, 1)]
                     if (cXX * X * X + cXY * X * Y + Y * Y) % 2 == 0)
        assert nroots in (0, 2), "degenerate tangent cone at 2"
        return nroots == 2
    disc = (cXY * cXY - 4 * cXX) % p
    assert disc != 0, "cusp unexpected"
    return pow(disc, (p - 1) // 2, p) == 1


def short_model(a):
    a1, a2, a3, a4, a6 = [Fraction(v) for v in a]
    b2 = a1 * a1 + 4 * a2
    C2 = b2 / 4
    C1 = (2 * a4 + a1 * a3) / 2
    C0 = (a3 * a3 + 4 * a6) / 4
    s = b2 / 12
    A = C1 - 2 * C2 * s + 3 * s * s
    B = C0 - C1 * s + C2 * s * s - s ** 3

    def mp(P):
        x, y = P
        return (x + s, y + (a1 * x + a3) / 2)

    return A, B, mp


def has_rational_root_quartic(coeffs):
    """coeffs [1,c3,c2,c1,c0] Fractions. Sieve mod primes, then exact divisors."""
    for m in (3, 5, 7, 11):
        ok = False
        for u in range(m):
            r = (Fraction(u) ** 4 + coeffs[1] * Fraction(u) ** 3
                 + coeffs[2] * Fraction(u) ** 2 + coeffs[3] * Fraction(u) + coeffs[4])
            if r.numerator % m == 0:
                ok = True
                break
        if not ok:
            return False, "no-root-mod-%d" % m
    L = 1
    for c in coeffs:
        L = L * c.denominator // math.gcd(L, c.denominator)
    I = [int(c * L) for c in coeffs]
    lead, const = I[0], I[4]
    if const == 0:
        return True, "u=0-is-root"

    def divisors(n):
        n = abs(n)
        d = set()
        i = 1
        while i * i <= n:
            if n % i == 0:
                d |= {i, n // i}
            i += 1
        return d

    dc, dl = divisors(const), divisors(lead)
    if len(dc) * len(dl) > 300000:
        return None, "enumeration-too-large"
    for p in dc:
        for q in dl:
            for sgn in (1, -1):
                r = Fraction(sgn * p, q)
                if (r ** 4 + coeffs[1] * r ** 3 + coeffs[2] * r ** 2
                        + coeffs[3] * r + coeffs[4] == 0):
                    return True, "root-%s" % r
    return False, "divisor-sieve-lead%d-const%d" % (lead, const)


def rat_roots_cubic(A, B, C, D):
    found = []

    def divisors(n):
        n = abs(n)
        d = set()
        i = 1
        while i * i <= n:
            if n % i == 0:
                d |= {i, n // i}
            i += 1
        return d

    if D == 0:
        found.append(Fraction(0))
    dc, dl = divisors(D if D else 1), divisors(A)
    for p in dc:
        for q in dl:
            for sgn in (1, -1):
                x = Fraction(sgn * p, q)
                if A * x ** 3 + B * x ** 2 + C * x + D == 0 and x not in found:
                    found.append(x)
    return found


def integral_scan(a, lo, hi):
    a1, a2, a3, a4, a6 = a
    assert a1 == 1 and a3 == 0
    xs = []
    for x in range(lo, hi + 1):
        D = x * x + 4 * (x * x * x + a2 * x * x + a4 * x + a6)
        if D >= 0:
            r = math.isqrt(D)
            if r * r == D and ((r - x) & 1) == 0:
                xs.append(x)
    return xs


for C in CURVES:
    a = C["a"]
    I = inv(a)
    r = out["curves"][C["name"]] = {}
    r["invariants"] = {k: I[k] for k in ("b2", "b4", "b6", "b8", "c4", "c6", "D")}
    r["on_curve"] = {"P1": bool(on_curve(a, C["P1"])), "P2": bool(on_curve(a, C["P2"]))}
    r["minimality"] = {str(p): {"p4_divides_c4": I["c4"] % p ** 4 == 0,
                                "p6_divides_c6": I["c6"] % p ** 6 == 0}
                       for p in (2, 2003)}
    # reduction
    loc = {}
    for p, e in ((2, 0), (2003, 1)):
        vp = 0
        d = I["D"]
        while d % p == 0:
            d //= p
            vp += 1
        sg = sing_pt_modp(a, p)
        loc[str(p)] = {"ord_Delta": vp, "ord_conductor": 1,
                       "n_singular_pts": len(sg),
                       "singular_pt": sg[0] if len(sg) == 1 else None,
                       "kodaira": "I_%d" % vp if vp >= 1 else "good",
                       "split": bool(split_modp(a, p, sg[0])) if len(sg) == 1 else None,
                       "tamagawa": vp if (len(sg) == 1 and split_modp(a, p, sg[0])) else 1}
    r["local"] = loc
    # torsion
    n3, n5, n7 = count_modp(a, 3), count_modp(a, 5), count_modp(a, 7)
    a1, a2, a3, a4, a6 = a
    r2 = None  # computed below
    # 2-torsion cubic: 4x^3 + (4a2+a1^2)x^2 + ... derive by y=-(a1x+a3)/2 substitution
    # F: y^2+a1xy+a3y - x^3-a2x^2-a4x-a6 with y=-(a1x+a3)/2:
    # constant part: (a1x+a3)^2/4 - (a1x+a3)^2/2 = -(a1x+a3)^2/4
    A3, B3 = Fraction(4), Fraction(4 * a2 + a1 * a1)
    # -(a1x+a3)^2/4 - x^3 - a2 x^2 - a4 x - a6 = 0  ->  multiply by -4:
    # 4x^3 + (4a2+a1^2)x^2 + (4a4+2a1a3)x + (4a6+a3^2) = 0
    C3 = Fraction(4 * a4 + 2 * a1 * a3)
    D3 = Fraction(4 * a6 + a3 * a3)
    r2 = rat_roots_cubic(4, B3, C3, D3)
    r["torsion"] = {"E(F3)": n3, "E(F5)": n5, "E(F7)": n7,
                    "two_torsion_cubic": [4, int(B3), int(C3), int(D3)],
                    "two_torsion_rational_x": [str(t) for t in r2]}
    # independence mod 2 (rank >= 2): images in E(Q)/2E(Q) distinct & nonzero
    A, B, mp = short_model(a)
    X1 = mp(C["P1"])[0]
    X2 = mp(C["P2"])[0]
    X12 = mp(add(a, C["P1"], C["P2"]))[0]
    halves = {}
    for tag, Xi in (("P1", X1), ("P2", X2), ("P1+P2", X12)):
        c = [Fraction(-4) * Xi, Fraction(-2) * A,
             Fraction(-4) * (A * Xi + 2 * B), A * A - Fraction(4) * B * Xi]
        halves[tag] = has_rational_root_quartic([Fraction(1)] + c)
    r["halving"] = {t: {"has_Q_half": h, "cert": c} for t, (h, c) in halves.items()}
    r["short_model"] = {"A": str(A), "B": str(B),
                        "X(P1)": str(X1), "X(P2)": str(X2), "X(P1+P2)": str(X12)}
    # integral scan
    r["integral_scan_1e6"] = integral_scan(a, -10 ** 6, 10 ** 6)

print(__import__("json").dumps(out, indent=1, default=str))
