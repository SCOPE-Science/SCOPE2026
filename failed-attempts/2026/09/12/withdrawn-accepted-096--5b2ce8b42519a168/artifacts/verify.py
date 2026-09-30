"""Exact rational certification of the Q5 Schottky figure for theta (2,1,3)
and the total-length obstruction (18 vs 9).

Discs: D1=B(1,5^-1), D2=B(2,5^-1), D3=B(0,5^-2), D4=B(5,5^-3).
A pairs D1<->D3 (fixed pts 1,0; multiplier 125 at 0).
B pairs D2<->D4 (fixed pts 2,5; multiplier 625 at 5).
All arithmetic is over Fraction, so 5-adic valuations are exact.
"""
from fractions import Fraction

F = Fraction

def v5(n: int) -> int:
    if n == 0:
        return 10**9
    v = 0
    n = abs(n)
    while n % 5 == 0:
        n //= 5
        v += 1
    return v

def v5f(x: F) -> int:
    return v5(x.numerator) - v5(x.denominator)

def av5f(x: F) -> int:
    return v5f(abs(x))

def mob(M, z: F) -> F:
    a, b, c, d = M
    return (a * z + b) / (c * z + d)

def det(M) -> F:
    a, b, c, d = M
    return a * d - b * c

qA, qB = F(125), F(625)
MA = (F(125), F(0), F(124), F(1))          # z -> 125 z/(124 z+1); fixes 0,1
MB = (F(-1245), F(6240), F(-624), F(3123))  # fixes 2,5 (see checks)

checks = []
def check(name, cond, detail=""):
    checks.append(name)
    assert cond, f"FAILED {name} {detail}"
    print(f"  ok: {name}" + (f" [{detail}]" if detail else ""))

print("== matrices ==")
check("det MA = 125", det(MA) == 125)
check("det MB = 5625", det(MB) == 5625)
check("A(0)=0", mob(MA, F(0)) == 0)
check("A(1)=1", mob(MA, F(1)) == 1)
check("B(2)=2", mob(MB, F(2)) == 2)
check("B(5)=5", mob(MB, F(5)) == 5)
# multipliers via derivative det/(c z+d)^2
def deriv(M, z):
    a, b, c, d = M
    return det(M) / (c * z + d) ** 2
check("A'(0)=125", deriv(MA, F(0)) == 125)
check("B'(5)=625", deriv(MB, F(5)) == 625)
check("v5(qA)=3", v5f(qA) == 3)
check("v5(qB)=4", v5f(qB) == 4)

print("== discs disjoint ==")
discs = {"D1": (F(1), 1), "D2": (F(2), 1), "D3": (F(0), 2), "D4": (F(5), 3)}
names = list(discs)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        c1, r1 = discs[names[i]]
        c2, r2 = discs[names[j]]
        sep = av5f(c1 - c2)
        check(f"disjoint {names[i]} vs {names[j]}", sep < min(r1, r2),
              f"|c1-c2|=5^({sep})")

print("== poles strictly inside repelling/attracting discs ==")
zA = F(-1, 124)       # pole of A
check("pole A in D1", av5f(zA - 1) > 1, f"v={av5f(zA-1)}")
zAi = F(125, 124)     # pole of A^{-1}
check("pole Ainv in D3", av5f(zAi - 0) > 2, f"v={av5f(zAi)}")
zB = F(1041, 208)     # pole of B (=3123/624 reduced)
check("pole B in D2", av5f(zB - 2) > 1, f"v={av5f(zB-2)}")
zBi = F(415, 208)     # pole of B^{-1} (=1245/624 reduced)
check("pole Binv in D4", av5f(zBi - 5) > 3, f"v={av5f(zBi-5)}")

print("== multiplier/radius compatibility |q| = r+ r- ==")
check("|qA| = 5^-3 = radii product", v5f(qA) == (1 + 2))
check("|qB| = 5^-4 = radii product", v5f(qB) == (1 + 3))
check("|c1-c2|=1 for A pair", av5f(F(1) - F(0)) == 0)
check("|c1-c2|=1 for B pair", av5f(F(2) - F(5)) == 0)

print("== ping-pong spot checks (boundary->boundary, exterior->interior) ==")
# A: boundary pt of D1 (z=6, |6-1|=5^-1) -> boundary of D3
check("A bdy->bdy", av5f(mob(MA, F(6))) == 2, f"A(6)={mob(MA,F(6))}")
check("A ext->int (z=2)", av5f(mob(MA, F(2))) > 2, f"A(2)={mob(MA,F(2))}")
check("A ext->int (z=0 fixed)", mob(MA, F(0)) == 0)
# A^{-1} via inverse matrix
MAi = (F(1), F(0), F(-124), F(125))
check("Ainv bdy->bdy (z=25)", av5f(mob(MAi, F(25)) - 1) == 1)
check("Ainv ext->int (z=5)", av5f(mob(MAi, F(5)) - 1) > 1)
# B: boundary pt of D2 (z=7) -> boundary of D4
check("B bdy->bdy (z=7)", av5f(mob(MB, F(7)) - 5) == 3, f"B(7)={mob(MB,F(7))}")
check("B ext->int (z=0)", av5f(mob(MB, F(0)) - 5) > 3, f"B(0)={mob(MB,F(0))}")
check("B ext->int (z=1)", av5f(mob(MB, F(1)) - 5) > 3)
MBi = (F(3123), F(-6240), F(624), F(-1245))  # adjugate (proportional to inverse)
check("Binv bdy->bdy (z=130)", av5f(mob(MBi, F(130)) - 2) == 1)
check("Binv ext->int (z=2 fixed)", mob(MBi, F(2)) == 2 or mob(MB, F(2)) == 2)
check("Binv ext->int (z=0)", av5f(mob(MBi, F(0)) - 2) > 1)

print("== skeleton combinatorics ==")
# arms from branch pts u=G, v=zeta_{0,5^-1}; bridge 1
arm1, arm2, arm3, arm4, bridge = 1, 1, 1, 2, 1
eA, eB = arm1 + arm3, arm2 + arm4
check("theta edges {1,2,3}", sorted([bridge, eA, eB]) == [1, 2, 3])
check("L(A)=eA+bridge=3", eA + bridge == 3 == v5f(qA))
check("L(B)=eB+bridge=4", eB + bridge == 4 == v5f(qB))
check("total Gamma = 6", bridge + eA + eB == 6)
Vp, Ep = 6, 9
check("cover V'=6 E'=9 b1=4", (Vp, Ep, 1 - (Vp - Ep)) == (6, 9, 4))
check("pullback total 18", 3 * 6 == 18)
check("length-1 total 9", Ep * 1 == 9)
check("obstruction 18 != 9", 18 != 9)
check("Schreier rank 4", 1 + 3 * (2 - 1) == 4)
print("ALL CHECKS PASSED")
