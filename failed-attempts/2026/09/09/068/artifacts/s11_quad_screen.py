"""Step 11: quadruple-balanced integrality screen (exact).
e_i(w) = C(w,i)*C(72-w,4-i)/C(72,4) * A_w for all w,i.
If any non-integral, flag as candidate obstruction to test via full 4-point MW system.
"""
from math import comb
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
D = comb(72, 4)
print("C(72,4) =", D)
bad = []
for w in range(73):
    if not A[w]:
        continue
    for i in range(5):
        num = comb(w, i) * comb(72 - w, 4 - i) * A[w]
        if num % D != 0:
            bad.append((w, i, num % D))
            print(f"  NON-INTEGRAL w={w} i={i}: remainder {num % D}")
print("bad count:", len(bad))
json.dump({"bad": bad}, open(os.path.join(HERE, "s11_quad_screen.json"), "w"), indent=1)
print("wrote s11_quad_screen.json")
