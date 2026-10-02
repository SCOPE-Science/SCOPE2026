"""Minkowski-bound certificate h(Q(sqrt29)) = 1 (no PARI needed).

Minkowski bound M = (1/2) sqrt(29) < 2.7, so every ideal class contains an
integral ideal of norm <= 2. Norm-2 ideals <-> prime(s) above 2.
x^2 - x - 7 mod 2 = x^2 + x + 1, irreducible over F2 (values 1,1 at 0,1).
So 2 is INERT: no ideal of norm 2; the only norm-<=2 integral ideal is (1).
Hence every class is trivial: h = 1, A0 = 0.
"""
import json
D = 29
import math
M = 0.5 * math.sqrt(D)
print(f"Minkowski bound = sqrt(29)/2 = {M:.6f} < 2.7")
vals = {a: (a * a - a - 7) % 2 for a in (0, 1)}
print("x^2-x-7 mod 2 values:", vals)
assert all(v == 1 for v in vals.values())
print("=> irreducible mod 2 => 2 INERT in Q(sqrt29).")
print("=> no integral ideal of norm 2; Minkowski: every class has repr of norm <= 2 => only (1).")
print("=> h(Q(sqrt29)) = 1, A0 (5-part) = 0.")
with open("minkowski_h1.json", "w") as f:
    json.dump({"disc": 29, "minkowski_bound": M,
               "mod2_values": vals, "inert_2": True, "class_number": 1}, f, indent=1)
print("saved minkowski_h1.json")
