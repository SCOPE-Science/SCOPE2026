"""Step 27 (corrected): derived-design chain from putative 5-(72,16,78) (exact).
Derived at a point: 4-(71,15,78), 3-(70,14,78), ..., 1-(68,12,78).
Block counts b'_t = 78*C(v-1,t-1)/C(k-1,t-1); cross-check b'_4 = t16 = 55522.
All exact Fractions.
"""
from math import comb
from fractions import Fraction
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
print("chain from 5-(72,16,78):")
rows = []
v, k, lam, t = 72, 16, 78, 5
rows.append((t, v, k, lam, A[16]))
print(f"  {t}-({v},{k}) lam={lam} blocks={A[16]}")
while t > 1:
    b = Fraction(lam * comb(v - 1, t - 1), comb(k - 1, t - 1))
    v, k, t = v - 1, k - 1, t - 1
    rows.append((t, v, k, lam, b))
    print(f"  {t}-({v},{k}) lam={lam} blocks={b} integral={b.denominator == 1}")
assert rows[1][4] == Fraction(55522) == Fraction(16 * A[16], 72), "b' must equal t16"
print("cross-check b'(4-design) == t16 == 55522: PASS")
json.dump([{"t": t, "v": v, "k": k, "lam": lam, "blocks": str(b)} for (t, v, k, lam, b) in rows],
          open(os.path.join(HERE, "s27_derived.json"), "w"), indent=1)
print("wrote s27_derived.json")
