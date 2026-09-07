#!/usr/bin/env python3
"""Exact-integer checker for n=m=500 balls-in-bins certificate (stdlib only).

Verifies by integer arithmetic (no floating-point in pass/fail decisions):
  (U)  union tails U_k = S_k/500^499 <= thresholds (k=6,8,9,10)
  (L)  lambda_6 in [0.2909, 0.2911]
  (S)  Stein-Chen b1'+b2 <= 0.17 (hence <= 0.20), b1' with diagonal (B_i = all bins, b3 = 0)
  (N)  pairwise negative correlation J_4*500^500 <= S_4^2 and J_6 likewise
  (C)  lower tail: crude (1-p)/E <= 0.105; exact Var/E^2 <= 0.084
  (E)  exp(-lambda_6) in [0.74744, 0.74760] via rational alternating Taylor
Prints PASS/FAIL per check plus decimal values for display only.
Runtime ~5 s.
"""
from math import comb, factorial
from fractions import Fraction

N = 500
D499 = pow(500, 499)
D500 = pow(500, 500)
D1000 = pow(500, 1000)

def S_bin(k):
    return sum(comb(N, j) * pow(499, N - j) for j in range(k, N + 1))

fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i
pow498 = [1] * (N + 1)
for i in range(1, N + 1):
    pow498[i] = pow498[i - 1] * 498

def J_joint(k):
    tot = 0
    F = fact
    for a in range(k, N + 1):
        fa = F[a]
        for b in range(k, N - a + 1):
            c = N - a - b
            tot += F[N] // (fa * F[b] * F[c]) * pow498[c]
    return tot

def taylor_neg(x, deg):
    s = Fraction(0)
    for kk in range(deg + 1):
        s += Fraction((-1) ** kk) * x ** kk / Fraction(factorial(kk))
    return s

ok = True
def check(name, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + ("  " + detail if detail else ""))
    if not cond:
        ok = False

S4 = S_bin(4); S6 = S_bin(6); S8 = S_bin(8); S9 = S_bin(9); S10 = S_bin(10)
# (U) union tails: S_k/500^499 <= t  <=> S_k*t_den <= t_num*500^499
checks_U = [(8, Fraction(491, 100000)), (9, Fraction(6, 10000)),
            (10, Fraction(6, 100000)), (6, Fraction(3, 10)),
            (8, Fraction(1, 200)), (7, Fraction(45, 1000))]
Smap = {4: S4, 6: S6, 8: S8, 9: S9, 10: S10, 7: S_bin(7)}
for k, t in checks_U:
    S = Smap[k]
    cond = S * t.denominator <= t.numerator * D499
    check(f"U{k}<={float(t)}", cond, f"U{k}~{S/D499:.8f}")
# (L)
for lo, hi in [(Fraction(290, 1000), Fraction(292, 1000)),
               (Fraction(2909, 10000), Fraction(2911, 10000))]:
    cond = S6 * lo.denominator >= lo.numerator * D499 and S6 * hi.denominator <= hi.numerator * D499
    check(f"lambda6 in [{float(lo)},{float(hi)}]", cond, f"lam~{S6/D499:.8f}")
# (S) Stein-Chen
J6 = J_joint(6)
lhs = (N * N * S6 * S6 + N * (N - 1) * J6 * D500)  # numerator over 500^1000
for num, den in [(17, 100), (165, 1000), (20, 100)]:
    check(f"b1'+b2<={num/den}", lhs * den <= num * D1000,
          f"b1'+b2~{lhs/D1000:.6f}")
# (N) negative correlation
J4 = J_joint(4)
check("negcorr k=4 (J4*D<=S4^2)", J4 * D500 <= S4 * S4,
      f"ratio~{(J4*D500)/(S4*S4):.6f}")
check("negcorr k=6 (J6*D<=S6^2)", J6 * D500 <= S6 * S6,
      f"ratio~{(J6*D500)/(S6*S6):.6f}")
# (C) lower tails
# crude (1-p)/E = (D-S4)/(500*S4) <= 105/1000 ?
check("crude lower<=0.105", 1000 * (D500 - S4) <= 105 * 500 * S4,
      f"crude~{(D500-S4)/(500*S4):.8f}")
print("INFO crude<=0.104 holds?", 1000 * (D500 - S4) <= 104 * 500 * S4,
      "(expected False: proposed 0.104 off by ~1.4e-5)")
# exact Var/E^2 = [S(D-S)+(n-1)(JD-S^2)]/(nS^2) <= 84/1000 ?
numV = S4 * (D500 - S4) + (N - 1) * (J4 * D500 - S4 * S4)
denV = N * S4 * S4
check("exact Var/E^2<=0.084", numV * 1000 <= 84 * denV, f"val~{numV/denV:.8f}")
check("exact Var/E^2<=0.104", numV * 1000 <= 104 * denV)
# coverage 1-0.084-0.00491 >= 0.89  (rational: 84/1000+491/100000=8891/100000<=11/100)
check("coverage>=0.89 (rational)", Fraction(84, 1000) + Fraction(491, 100000) <= Fraction(11, 100))
# (E) exp bounds: e^{-lam} in [S11(-u), S10(-l)] with u=2911/10000, l=2909/10000
l = Fraction(2909, 10000); u = Fraction(2911, 10000)
loE = taylor_neg(u, 11); hiE = taylor_neg(l, 10)
check("exp(-lam) in [0.7474,0.7477]", loE >= Fraction(7474, 10000) and hiE <= Fraction(7477, 10000),
      f"[{float(loE):.6f},{float(hiE):.6f}]")
check("exp(-lam) ni 0.7475", loE <= Fraction(7475, 10000) <= hiE)
print("ALL-OK" if ok else "SOME-FAILED")
