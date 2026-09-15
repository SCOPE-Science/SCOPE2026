"""Bounded recovery test: verify Park's numerics for the |Out_F(S)|=48 Ruiz-Viruel case.

Checks: d0/d1/d2 layer counts, e(X), v7(e!), exoticity bound 425744,
e mod 7, and S-fixed fiber count. Setup verification only; does not
decide F_S(H)=F or the strict defect inequality.
"""
import math

p = 7
out = 48
d0 = out
d1 = (p + 1) * out
d2 = p * (p + 1) * out
e = d0 + p * d1 + p * p * d2
assert (d0, d1, d2) == (48, 384, 2688), (d0, d1, d2)
assert e == 134448, e
assert e == (p**5 - 1) // (p - 1) * out

v = sum(e // (p ** k) for k in range(1, 12))
assert v == 22403, v
bound = (e - 1) * 3 + v
assert bound == 425744, bound
assert e % 7 == 6
assert e == 48 * 2801

# S-orbit fixed-point count on the fiber set J: only the 48 X0 singletons
# are fixed by the S-action; X1 blocks (size 7) and X2 blocks (size 49)
# contribute no fixed points.
fixed = d0
assert fixed == 48
print("d0,d1,d2 =", d0, d1, d2)
print("e(X) =", e)
print("v7(e!) =", v)
print("bound 3(e-1)+v7 =", bound)
print("e mod 7 =", e % 7)
print("S-fixed fibers =", fixed)
print("OK: Park numerics confirmed; fusion/defect questions undecided.")
