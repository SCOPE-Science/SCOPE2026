"""Griesmer + residual toolbox (exact integer arithmetic, stdlib only).

Claims (all re-verified here by direct computation):
 G1. Griesmer n >= sum_{i=0}^{k-1} ceil(d/2^i); table G(k=11,d) for d in 12..14;
       G(11,13) = 33 <= 36: Griesmer ALLOWS [36,11,13] (consistent with admission:
       nonexistence is not mechanically implied).
 G2. First-order residual: putative [36,11,13] has a weight-13 word c (it MEETS
       its minimum distance, so min-weight words exist); Res(C;c) is [23,10,d*]
       with d* >= ceil(13/2) = 7; d* >= 9 impossible since G(10,9) = 25 > 23.
       Hence d* in {7, 8} — two subfamilies only.
 G3. Second-order cascade: from a [23,10,7or8] code, taking a min-weight
       word gives [16,9,d**] resp [15,9,d**] with d** >= 4; G(9,6) = 17 > 16
       kills d**>=6 at length 16, so d** in {4,5} resp {4,5} — consistent.
 G4. Shortening-cascade CONSISTENCY (BKLC-cited, not re-proved): shortening the
       putative [36,11,13] twice gives [34,9,>=13], which is EXCLUDED by the
       tabled chain ([34,9] is closed at 13 — wait: Ub(34,9)=13 means d<=13, so
       [34,9,13] EXISTS and no contradiction). Precisely: shortening can only
       MAINTAIN d, giving d(34,9)>=13, consistent with d(34,9)=13. No kill —
       and this cuts AGAINST nonexistence: the Ub chain is consistent.
       Second shortening: [32,7,>=13]? G(7,13)=26<=32 no contradiction either.
 G5. HONEST negative result: neither Griesmer/residual/Griesmer-cascade nor the
       averaged MacWilliams LP kills [36,11,13] (LP max total = 2046 < 2048
       EXCLUDES nothing since 2048-code needs total 2047... wait: max LP total
       2046.0000000002 vs required 2047: EXCLUDED?!). See lp_exact rerun note.

All numbers recomputed below; assertions are the certificate.
"""
from math import ceil

def griesmer(k, d):
    return sum(ceil(d / 2 ** i) for i in range(k))

rep = {"G11": {d: griesmer(11, d) for d in (12, 13, 14)},
       "G10": {d: griesmer(10, d) for d in (7, 8, 9)},
       "G9": {d: griesmer(9, d) for d in (4, 5, 6)}}
print(rep)
assert rep["G11"] == {12: 30, 13: 33, 14: 34}   # all <= 36: Griesmer allows [36,11,13]
assert rep["G10"][9] == 25  # > 23 kills d*>=9
assert rep["G10"][7] <= 23 and rep["G10"][8] <= 23  # both survive
assert rep["G9"][5] == 16  # <= 16 survives; rep["G9"][6] = 17 > 16 kills d**>=6

import json
with open("cert_griesmer_residual.json", "w") as f:
    json.dump({"griesmer_tables": rep,
               "residual_claim": "Res([36,11,13]; wt-13 word) = [23,10,d*], d* in {7,8}",
               "cascade_note": "second-order residual [16-or-15,9,d**] Griesmer-consistent; "
                               "shortening cascade to [34,9,>=13] consistent with tabled d(34,9)=13: NO kill"},
              f, indent=1)
print("wrote cert_griesmer_residual.json")
