"""Step F2: fallback table assembly + full replay gate.
Table = the COMPLETE list of MacWilliams-compatible shortened [71,35,>=15]
distributions at fixed coordinate 1 = exactly ONE distribution (uniqueness proved
in s2b: rank 5/5, zero free vars). Tabulate A' and B' exactly, with min-distance
and dual-distance certificates, plus gap g (f1). Emit fallback_table.json and
print the canonical table. Replay: verify.py replays everything bit-for-bit.
"""
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
gap = json.load(open(os.path.join(HERE, "fallback_gap.json")))
ss = json.load(open(os.path.join(HERE, "shorten_system.json")))
assert ss["consistent"] and ss["free"] == [] and ss["rank"] == 5
from fractions import Fraction
t = {w: Fraction(w * A[w], 72) for w in range(73)}
Ap = [(A[w] - t[w]) for w in range(72)]
Bp = [((A[j] - t[j]) + t[j + 1]) for j in range(72)]
assert sum(Ap) == 2 ** 35 and sum(Bp) == 2 ** 36
d = next(w for w in range(1, 72) if Ap[w] != 0)
dd = next(j for j in range(1, 72) if Bp[j] != 0)
assert d >= 15 and dd == 15
table = {"parent": "W72* (unique putative extremal Type-II [72,36,16])",
         "operation": "shorten coordinate 1",
         "n MacWilliams-compatible distributions": 1,
         "uniqueness_proof": "s2b_shorten.py: 68 nontrivial MW equations, rank 5 = #unknowns, consistent",
         "Aprime": [int(x) for x in Ap], "Bprime": [int(x) for x in Bp],
         "min_distance": d, "dual_distance": dd, "gap_g": gap["g"]}
json.dump(table, open(os.path.join(HERE, "fallback_table.json"), "w"), indent=1)
print("FALLBACK TABLE: exactly one MacWilliams-compatible shortened distribution:")
for w in range(72):
    if Ap[w]:
        print(f"  A'[{w}] = {Ap[w]}")
print(f"min distance {d} (>= 15 OK); dual distance {dd}; g = {gap['g']}")
print("wrote fallback_table.json")
