"""Step 8 (target stress-test): higher balanced-moment integrality + LP sanity.
(a) k-fold balanced values m_w^{(k)} = C(w,k)/C(72,k) * A_w for k=4,5,6:
record integrality (necessary for k-transitive-averaged profiles; informative
gap values even though only k=1 is forced by MacWilliams uniqueness).
(b) Delsarte LP sanity for shortened [71,35,16] A': verify all Krawtchouk dual
moments B'_j >= 0 (already exact) and document dual distance 15.
"""
from math import comb
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
out = {}
for k in [4, 5, 6]:
    den = comb(72, k)
    ni = []
    print(f"(a) k={k}, C(72,{k})={den}:")
    for w in range(73):
        if A[w]:
            num = comb(w, k) * A[w]
            ok = (num % den == 0)
            if not ok:
                ni.append(w)
    print(f"  non-integral weights: {ni if ni else 'NONE'}")
    out[k] = ni
Bp = [0] * 72
t = {w: (w * A[w]) // 72 for w in range(73)}
for j in range(72):
    Bp[j] = (A[j] - t[j]) + (t[j + 1] if j + 1 <= 72 else 0)
print("(b) dual distance of punctured [71,36]:",
      next(j for j in range(1, 72) if Bp[j] != 0))
print("all B'_j >= 0:", all(b >= 0 for b in Bp))
json.dump({str(k): out[k] for k in out}, open(os.path.join(HERE, "s8_moments.json"), "w"), indent=1)
print("wrote s8_moments.json")
