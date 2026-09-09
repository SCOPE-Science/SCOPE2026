"""Step 28: order-2 (involution) shortening trace — Oleg Marichev?? no: fixed-point
subcode dimension screen. For putative [72,36,16] with involution sigma (no fixed
pts assumed first): C(sigma) = {(u,u)} has dim 36-? Standard: if sigma acts fixed-
point-freely, C(sigma) is a [36,18,?] code; Griesmer/Plotkin constraints on its
min distance d' >= 8 (halved weights). Verify the halved enumerator
H_w = n_{2w}^{(pairs)} ... : from pair-balanced data (s9): words constant on all
36 pairs. Under 2-transitive averaging the count of pair-constant words of pair-
weight p is determined by the 36-pair MW system? NOT computed here (needs full
orbit data). Instead: Griesmer feasibility table for [36,18,d>=8] as necessary
condition + state assumption explicitly. Gap values only.
"""
from math import comb
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))


def griesmer(k, d):
    return sum((d + (1 << i) - 1) // (1 << i) for i in range(k))

for d in [8, 10, 12]:
    print(f"[36,18,{d}]: Griesmer need {griesmer(18, d)} <= 36: "
          f"{'pass' if griesmer(18, d) <= 36 else 'VIOLATION'}")
json.dump({"note": "fixed-point-free involution subcode [36,18,d>=8]: Griesmer passes; "
                   "no exclusion; full orbit-count needs code, not enumerator."},
          open(os.path.join(HERE, "s28_involution.json"), "w"), indent=1)
print("wrote s28_involution.json")
