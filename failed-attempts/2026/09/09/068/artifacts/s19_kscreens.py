"""Step 19: k-subset balanced integrality screens for k=7..16 (exact).
e_i(w) = C(w,i)*C(72-w,k-i)/C(72,k) * A_w. Report per-k bad counts (gap values).
"""
from math import comb
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
out = {}
for k in range(7, 17):
    D = comb(72, k)
    bad = 0
    for w in range(73):
        if not A[w]:
            continue
        for i in range(k + 1):
            if (comb(w, i) * comb(72 - w, k - i) * A[w]) % D != 0:
                bad += 1
    out[k] = bad
    print(f"k={k}: C(72,{k})={D}, non-integral (w,i) cells: {bad}")
json.dump(out, open(os.path.join(HERE, "s19_kscreens.json"), "w"), indent=1)
print("wrote s19_kscreens.json")
