"""Replayable tilt-wall enumeration for lane-366.
Conventions (Bayer et al. 1703.10839 tilt setup for cubic threefold Y):
  ch = (r, kH, xH^2, y pt), pt = H^3/3, H^3 = 3.
  Use integer-friendly coordinates (r, d1, d2) with d1 = H^2.ch1 = 3k, d2 = H.ch2 = 3x.
  H-discriminant: Delta_H = d1^2 - 6 r d2 (= 9(k^2 - 2 r x)).
  Tilt central charge Z_{a,b}: with A2 = a^2:
    num(E) = d2 - b d1 + 1.5 r (b^2 - A2)
    den(E) = d1 - 3 r b
    mu_{a,b} = -num/den.
  Wall W(E0,F): numE*denF - numF*denE = 0 (polynomial in A2,b).
Model lift of v=2a: E0 = 2[I_line], (r,d1,d2) = (2,0,-2), Delta = 12.
Lifts of a: F_{m,n} = a0 + m[O] + n[O(1)], a0=(1,0,-1), [O]=(1,0,0), [O(1)]=(1,3,3/2).
Stdlib only. Writes wall_log.txt.
"""
from fractions import Fraction

def E0():
    return (2, Fraction(0), Fraction(-2))

def Fmn(m, n):
    r = 1 + m + n
    d1 = Fraction(3 * n)
    d2 = Fraction(-1) + Fraction(3 * n, 2)
    return (r, d1, d2)

def delta(t):
    r, d1, d2 = t
    return d1 * d1 - 6 * r * d2

def wall_coeffs(m, n):
    """Return (cA, cB2, cB, c0) with wall: cA*A2 + cB2*b^2 + cB*b + c0 = 0."""
    rE, d1E, d2E = E0()
    rF, d1F, d2F = Fmn(m, n)
    # numE*denF - numF*denE; num = d2 - b d1 + 1.5 r b^2 - 1.5 r A2
    # Collect coefficients as Fractions in basis {A2, b^2, b, 1}.
    # numE = e2 + e1 b + eA A2 + eq b^2 ; denE = f1 b + f0
    eA = Fraction(-3, 2) * rE
    eq = Fraction(3, 2) * rE
    e1 = -d1E
    e0 = d2E
    gA = Fraction(-3, 2) * rF
    gq = Fraction(3, 2) * rF
    g1 = -d1F
    g0 = d2F
    hb1, hb0 = Fraction(-3) * rE, d1E   # denE = hb1 b + hb0
    kb1, kb0 = Fraction(-3) * rF, d1F   # denF = kb1 b + kb0
    # numE*denF = (eA A2 + eq b^2 + e1 b + e0)(kb1 b + kb0)
    # contributes A2: eA*kb1 b + eA*kb0 ; b^2: eq*kb0 ; b: (eq*kb1) b^3?? careful: b^2*b = b^3 term!
    # General product has b^3 terms: eq*kb1 b^3. But E-wall differences cancel b^3 iff ...?
    # Instead collect full polynomial and check b^3 cancellation explicitly.
    # Represent polynomial in (A2*b, A2, b^3, b^2, b, 1).
    from collections import defaultdict
    P = defaultdict(Fraction)
    # numE*denF terms
    P[('A2b',)] += eA * kb1
    P[('A2',)] += eA * kb0
    P[('b3',)] += eq * kb1
    P[('b2',)] += eq * kb0
    P[('b2',)] += e1 * kb1
    P[('b',)] += e1 * kb0
    P[('b',)] += e0 * kb1
    P[('c',)] += e0 * kb0
    # minus numF*denE terms
    P[('A2b',)] -= gA * hb1
    P[('A2',)] -= gA * hb0
    P[('b3',)] -= gq * hb1
    P[('b2',)] -= gq * hb0
    P[('b2',)] -= g1 * hb1
    P[('b',)] -= g1 * hb0
    P[('b',)] -= g0 * hb1
    P[('c',)] -= g0 * hb0
    return P

def circle_data(m, n):
    P = wall_coeffs(m, n)
    nz = {k: v for k, v in P.items() if v != 0}
    return nz

if __name__ == "__main__":
    lines = []
    lines.append("E0=(2,0,-2) Delta=12 mu_H=0")
    lines.append("F_{m,n}: r=1+m+n d1=3n d2=-1+3n/2")
    for m in range(-2, 3):
        for n in range(-2, 3):
            r, d1, d2 = Fmn(m, n)
            D = delta((r, d1, d2))
            P = wall_coeffs(m, n)
            nz = {k: v for k, v in P.items() if v != 0}
            lines.append(f"m={m} n={n} r={r} d1={d1} d2={d2} Delta={D} poly={dict(nz)}")
    # slope-sign check at (A2=1,b=-1) for E0 vs F_{-1,1}
    def mu(t, A2, b):
        r, d1, d2 = t
        num = d2 - b * d1 + Fraction(3, 2) * r * (b * b - A2)
        den = d1 - 3 * r * b
        return Fraction(-1) * num / den if den != 0 else None
    lines.append("slope check A2=1 b=-1:")
    lines.append(f"  mu(E0)={mu(E0(), 1, Fraction(-1))}")
    lines.append(f"  mu(F_-1,1)={mu(Fmn(-1, 1), 1, Fraction(-1))}")
    lines.append(f"  mu(F_0,1)={mu(Fmn(0, 1), 1, Fraction(-1))}")
    lines.append(f"  mu(F_1,1)={mu(Fmn(1, 1), 1, Fraction(-1))}")
    open("wall_log.txt", "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
