"""Step 12: quintuple-balanced integrality screen (exact).
e_i(w) = C(w,i)*C(72-w,5-i)/C(72,5) * A_w. AM 5-design integrality (s7) already
implies divisibility patterns; this is the joint (5-subset x weight) screen.
"""
from math import comb
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
D = comb(72, 5)
print("C(72,5) =", D)
bad = []
for w in range(73):
    if not A[w]:
        continue
    for i in range(6):
        num = comb(w, i) * comb(72 - w, 5 - i) * A[w]
        if num % D != 0:
            bad.append((w, i, num % D))
            print(f"  NON-INTEGRAL w={w} i={i}: remainder {num % D}")
print("bad count:", len(bad))
json.dump({"bad": bad}, open(os.path.join(HERE, "s12_quint_screen.json"), "w"), indent=1)
print("wrote s12_quint_screen.json")
