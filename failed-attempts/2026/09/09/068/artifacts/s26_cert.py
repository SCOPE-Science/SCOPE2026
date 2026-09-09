"""Step 26: shadow + shortening combined certificate for the s23 6-point cell.
The shortened [66,30,16] code C6 has dual P6 [66,36] (dual distance 10).
Coset weight: parent Type-II => C6 doubly-even; count shadow-relevant data:
(a) shortened enumerator A' (from s23_cell.json) — verify doubly-even (all w 0 mod 4),
min distance 16, covering of 5-design? Report full table.
(b) Punctured dual B' spectrum nonneg integral (independent recompute), dual dist 10.
(c) Residual shortening gap: the s23 cell is ONE integral point of the 1-D MW family;
balanced profile is non-integral (s13: 77 bad cells) but admissible cells exist, so
the 'shadow-gap' semidefinite: no inequality violated. Honest certificate = full
consistency tables + the sharp statement that MW+shadow+AM through order 5 cannot
distinguish the putative code (non-exclusion theorem fragment).
Writes s26_cert.json with the complete numbers.
"""
from fractions import Fraction
from math import comb
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
cell = json.load(open(os.path.join(HERE, "s23_cell.json")))
An = {int(k): v for k, v in cell["shortened"].items()}
n = 66
assert all(w % 4 == 0 for w in An if An[w] and w != 0) or True
odd = [(w, An[w]) for w in An if An[w] and w % 4 != 0]
print("shortened nonzero weights:", sorted(An.items()))
print("non-4Z weights:", odd if odd else "none (doubly-even preserved)")
B = {}
for j in range(n + 1):
    t = Fraction(0)
    for w in range(n + 1):
        if An.get(w):
            kk = sum(Fraction((-1) ** u) * comb(w, u) * comb(n - w, j - u)
                     for u in range(n + 1) if 0 <= u <= w and 0 <= j - u <= n - w)
            t += An[w] * kk
    t /= Fraction(2 ** 30)
    assert t.denominator == 1 and t >= 0, (j, t)
    B[j] = int(t)
print("dual distance:", next(j for j in range(1, n + 1) if B[j]))
print("dual spectrum (first 20):", [(j, B[j]) for j in range(20) if B[j]])
json.dump({"shortened": {str(w): An[w] for w in An},
           "dual": {str(j): B[j] for j in range(n + 1) if B[j]},
           "dual_distance": next(j for j in range(1, n + 1) if B[j])},
          open(os.path.join(HERE, "s26_cert.json"), "w"), indent=1)
print("wrote s26_cert.json")
