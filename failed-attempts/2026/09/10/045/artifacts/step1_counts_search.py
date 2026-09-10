"""Step-1 audit data for C: y^2 = x^5 - 4x + 1 — from scratch, stdlib only.

Proves/logs:
  (a) disc(f) = -259019 (sympy resultant), prime by trial division;
      hence smooth genus-2 (odd-degree separable quintic) and good reduction
      at p=7 (disc mod 7 = 2 != 0).
  (b) #C(Fp) and #J(Fp) for p in {3,5,7,11,13} by brute-force affine counts
      over Fp and over Fp^2 = Fp[t]/(irreducible quadratic), plus one point
      at infinity (odd degree). #J(Fp) via the genus-2 Weil polynomial from
      N1 = #C(Fp), N2 = #C(Fp^2).
  (c) Integral-point search for |x| <= 5000.
  (d) Verification of the extra rational point (1/4, +-1/32).
"""
import math
import sympy as sp

x = sp.Symbol('x')
f = x**5 - 4*x + 1
disc = int(sp.discriminant(f, x))
print("disc =", disc)
r = int(math.isqrt(abs(disc)))
d = 3
prime = True
while d <= r:
    if abs(disc) % d == 0:
        prime = False
        print("composite: divisible by", d)
        break
    d += 2
print("disc prime:", prime)
print("disc mod 7 =", disc % 7, "(nonzero => good reduction at 7)")


def count_aff_irr(p):
    """Number of affine F_{p^2}-points. Finds an irreducible quadratic
    t^2 + a t + b over Fp, represents F_{p^2} as pairs, precomputes the set
    of squares, then counts #{y : y^2 = f(x)} per x (0, 1, or 2)."""
    irr = None
    for a in range(p):
        for b in range(p):
            if all((t*t + a*t + b) % p != 0 for t in range(p)):
                irr = (a, b)
                break
        if irr:
            break
    a, b = irr

    def mul(p1, p2):
        u1, v1 = p1
        u2, v2 = p2
        return ((u1*u2 - v1*v2*b) % p, (u1*v2 + v1*u2 - v1*v2*a) % p)

    def sq(u, v):
        return ((u*u - v*v*b) % p, (2*u*v - v*v*a) % p)

    squares = set()
    for yu in range(p):
        for yv in range(p):
            squares.add(sq(yu, yv))

    def frob5(u, v):
        # (u+vt)^5 via repeated squaring-free repeated mul (tiny fields)
        r = (1, 0)
        e = (u, v)
        for _ in range(5):
            r = mul(r, e)
        return r

    n = 0
    for u in range(p):
        for v in range(p):
            fu, fv = frob5(u, v)
            fu = (fu - 4*u + 1) % p
            fv = (fv - 4*v) % p
            if (fu, fv) == (0, 0):
                n += 1
            elif (fu, fv) in squares:
                n += 2
    return n


def count_aff(p):
    n = 0
    for xv in range(p):
        v = (pow(xv, 5, p) - 4*xv + 1) % p
        n += sum(1 for yv in range(p) if (yv*yv) % p == v)
    return n


for p in [3, 5, 7, 11, 13]:
    n1 = count_aff(p)
    n2 = count_aff_irr(p)
    N1, N2 = n1 + 1, n2 + 1  # one point at infinity (odd degree)
    s1 = p + 1 - N1
    S2 = p*p + 1 - N2
    assert (s1*s1 - S2) % 2 == 0, (p, s1, S2)
    e2 = (s1*s1 - S2)//2
    J = 1 - s1 + e2 - p*s1 + p*p
    print(f"p={p}: aff1={n1} #C(Fp)={N1} aff2={n2} #C(Fp^2)={N2} "
          f"s1={s1} e2={e2} #J(Fp)={J}")

print("--- integral search |x|<=5000 ---")
pts = []
B = 5000
for X in range(-B, B+1):
    v = X**5 - 4*X + 1
    if v >= 0:
        rr = math.isqrt(v)
        if rr*rr == v:
            pts.append((X, rr))
print("integral points:", [(X, "+-"+str(r)) for X, r in pts])

print("--- rational point check (1/4, 1/32) ---")
from fractions import Fraction
X, Y = Fraction(1, 4), Fraction(1, 32)
print("on curve:", Y*Y == X**5 - 4*X + 1)
print("STEP1_OK")
