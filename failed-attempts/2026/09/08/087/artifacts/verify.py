"""Stdlib-only replay certificate for DRAFT.md (lane-254, curve 389a1).

Verifies, by exact integer/Fraction arithmetic and finite-field enumeration:
  (1) model invariants: Delta=389 (prime), c4=112 coprime to Delta
      -> bad reduction only at 389, multiplicative (I1), conductor 389;
  (2) exact Q-arithmetic: P1+P2=S, P1-P2=D, all claimed points on E(Q);
  (3) |E(F5)|=9, |E(F7)|=13 -> E(Q)[tors] = {O};
  (4) mod 11: |E(F11)|=16, doubling image = {O,(3,5),(6,4),(6,6)},
      reductions r1=(0,0), r2=(1,0), rS=(9,10) all NON-doubles
      -> [P1],[P2] F2-independent in E(Q)/2E(Q) -> rank >= 2.
Exit nonzero on any failure. No third-party packages.
"""
from fractions import Fraction
import sys

A1, A2, A3, A4, A6 = 0, 1, 1, -2, 0
FAIL = []

def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" [" + str(detail) + "]") if detail else ""))
    if not cond:
        FAIL.append(name)

# ---------- (1) invariants ----------
b2 = A1 * A1 + 4 * A2
b4 = 2 * A4 + A1 * A3
b6 = A3 * A3 + 4 * A6
b8 = A1 * A1 * A6 + 4 * A2 * A6 - A1 * A3 * A4 + A2 * A3 * A3 - A4 * A4
Delta = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
c4 = b2 * b2 - 24 * b4

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1 if i == 2 else 2
    return True

import math
check("Delta==389", Delta == 389, Delta)
check("389 prime", is_prime(389))
check("c4==112", c4 == 112, c4)
check("gcd(c4,Delta)==1 (=> I1, conductor 389)", math.gcd(c4, Delta) == 1)

# ---------- (2) exact Q group law ----------
def onQ(P):
    x, y = P
    return y * y + A1 * x * y + A3 * y == x ** 3 + A2 * x ** 2 + A4 * x + A6

def negQ(P):
    if P is None:
        return None
    x, y = P
    return (x, -y - A1 * x - A3)

def addQ(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2:
        if y1 + y2 + A1 * x1 + A3 == 0:
            return None
        lam = (3 * x1 * x1 + 2 * A2 * x1 + A4 - A1 * y1) / (2 * y1 + A1 * x1 + A3)
    else:
        lam = (y2 - y1) / (x2 - x1)
    x3 = lam * lam + A1 * lam - A2 - x1 - x2
    y3 = lam * (x1 - x3) - y1 - A1 * x3 - A3
    return (x3, y3)

F = Fraction
P1 = (F(0), F(0))
P2 = (F(1), F(0))
S = addQ(P1, P2)
D = addQ(P1, negQ(P2))
check("P1 on E(Q)", onQ(P1))
check("P2 on E(Q)", onQ(P2))
check("P1+P2==(-2,-1)", S == (F(-2), F(-1)), S)
check("P1-P2==(-1,-2)", D == (F(-1), F(-2)), D)
check("S on E(Q)", onQ(S))
check("D on E(Q)", onQ(D))
H1 = addQ(P1, P1)
H2 = addQ(P2, P2)
check("2P1==(3,5) on curve", H1 == (F(3), F(5)) and onQ(H1), H1)
check("2P2==(6,-16) on curve", H2 == (F(6), F(-16)) and onQ(H2), H2)

# ---------- finite-field machinery ----------
def aff_pts(p):
    r = []
    for x in range(p):
        b = (A1 * x + A3) % p
        c = (-(x ** 3 + A2 * x ** 2 + A4 * x + A6)) % p
        for y in range(p):
            if (y * y + b * y + c) % p == 0:
                r.append((x, y))
    return r

def addm(P, Q, p):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if (x1 - x2) % p == 0:
        if (y1 + y2 + A1 * x1 + A3) % p == 0:
            return None
        num = (3 * x1 * x1 + 2 * A2 * x1 + A4 - A1 * y1) % p
        den = (2 * y1 + A1 * x1 + A3) % p
        if den == 0:
            return None
        lam = num * pow(den, -1, p) % p
    else:
        lam = ((y2 - y1) % p) * pow((x2 - x1) % p, -1, p) % p
    x3 = (lam * lam + A1 * lam - A2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1 - A1 * x3 - A3) % p
    return (x3, y3)

# ---------- (3) torsion via F5, F7 ----------
n5 = len(aff_pts(5)) + 1
n7 = len(aff_pts(7)) + 1
check("Delta not 0 mod 5 (good reduction)", Delta % 5 != 0)
check("Delta not 0 mod 7 (good reduction)", Delta % 7 != 0)
check("|E(F5)|==9", n5 == 9, n5)
check("|E(F7)|==13", n7 == 13, n7)
# prime-divisor argument: any ell|#T with ell not p divides |E(Fp)|.
# ell not in {5,7} -> ell | gcd(9,13)=1 impossible; ell=5 -> 5|13 no; ell=7 -> 7|9 no.
gg = math.gcd(9, 13)
check("gcd(9,13)==1 (forces T trivial)", gg == 1)
check("5 does not divide 13", 13 % 5 != 0)
check("7 does not divide 9", 9 % 7 != 0)

# ---------- (4) mod-11 F2-independence ----------
p = 11
check("Delta not 0 mod 11 (good reduction)", Delta % p != 0)
pts = aff_pts(p)
check("|E(F11)|==16", len(pts) + 1 == 16, len(pts) + 1)
allp = pts + [None]
doubles = sorted(set(addm(P, P, p) for P in allp), key=str)
check("doubling image has 4 elts", len(doubles) == 4, doubles)
expect = sorted([None, (3, 5), (6, 4), (6, 6)], key=str)
check("doubling image == {O,(3,5),(6,4),(6,6)}", doubles == expect, doubles)
r1, r2, rS = (0, 0), (1, 0), (9, 10)
for nm, R in [("r1=(0,0)", r1), ("r2=(1,0)", r2), ("rS=(9,10)", rS)]:
    check(nm + " lies on E(F11)", R in pts)
    check(nm + " is NOT a double mod 11", R not in doubles)
check("rS == r1+r2 mod 11 (homomorphism instance)", addm(r1, r2, p) == rS,
      addm(r1, r2, p))

print()
if FAIL:
    print("VERIFY_FAIL:", FAIL)
    sys.exit(1)
print("VERIFY_OK: torsion trivial + [P1],[P2] F2-independent mod 2E(Q) => rank(E/Q) >= 2.")
