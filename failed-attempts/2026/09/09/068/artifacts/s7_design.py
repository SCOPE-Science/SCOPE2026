"""Step 7 (target deepening): Assmus-Mattson 5-design lambda integrality.
For putative extremal Type-II [72,36,16]: dual distance 16, nonzero weights
16..56 step 4 plus 72. Weights <= n-5=67: 11 values <= d-t = 11 (t=5).
AM equality holds => codewords of EACH nonzero weight w must form a 5-design,
so λ_5(w) = A_w * C(w,5)/C(72,5) and all λ_i (i<=5) must be integers.
Non-integral λ => genuine coefficient-level exclusion of W72* (target win).
All-exact integer arithmetic.
"""
from math import comb
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
print("Assmus-Mattson design check (t=5, dual distance 16, extremal):")
print("nonzero weights <= 67:", [w for w in range(73) if A[w] and w > 0])
NFAIL = []
for w in range(1, 73):
    if not A[w]:
        continue
    row = []
    for i in range(0, 6):
        num = A[w] * comb(w, i)
        den = comb(72, i)
        ok = (num % den == 0)
        row.append((i, num // den if ok else f"{num}/{den}", ok))
        if not ok and w <= 67:
            NFAIL.append((w, i))
    flag = "" if w > 67 else ("  <-- AM t=5 REQUIRES integral" if any(not r[2] for r in row) else "  AM-ok")
    print(f"  w={w}: " + ", ".join(f"lam{i}={v}{'!' if not o else ''}" for (i, v, o) in row) + flag)
print("AM t=5 violations among w<=67:", NFAIL if NFAIL else "NONE — all integral, no obstruction")
json.dump({"am_violations": NFAIL},
          open(os.path.join(HERE, "s7_design.json"), "w"), indent=1)
print("wrote s7_design.json")
