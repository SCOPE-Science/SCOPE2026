"""Step 13: sextuple-balanced screen (exact) — s8 showed k=6 moment failures,
so expect non-integral cells here; enumerate them precisely as gap values.
e_i(w) = C(w,i)*C(72-w,6-i)/C(72,6) * A_w.
"""
from math import comb
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
D = comb(72, 6)
print("C(72,6) =", D)
bad = []
for w in range(73):
    if not A[w]:
        continue
    for i in range(7):
        num = comb(w, i) * comb(72 - w, 6 - i) * A[w]
        q, r = divmod(num, D)
        if r != 0:
            bad.append((w, i, r))
            print(f"  w={w} i={i}: {num}/{D} = {num/D:.6f} (remainder {r})")
print("bad count:", len(bad))
json.dump({"bad": bad}, open(os.path.join(HERE, "s13_sext_screen.json"), "w"), indent=1)
print("wrote s13_sext_screen.json")
