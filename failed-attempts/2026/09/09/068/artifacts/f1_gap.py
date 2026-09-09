"""Step F1: fallback shadow-gap integer g for the designated residual cell.
Designated residual cell = the unique MacWilliams-compatible balanced shortened
profile (s2b: uniqueness proved, rank 5/5). g is the puncture excess B'-A'
(with A'_odd=0), NOT the Conway-Sloane shadow enumerator of the shortened code.
Lemma: for any genuine binary Type-II parent A_odd=0 so t_odd=0 by 0<=t<=A and
complement symmetry; then for the shortened/punctured pair Q_j=B'_j-A'_j
satisfies Q_even=t_odd=0 and Q_odd=B'_odd>=0 because A'_odd=0; hence Q>=0 and
g:=sum_{j=3 mod 4} Q_j>=0. On the putative extremal cell Q is supported on odd
weights {15,19,...,55,71} (all 3 mod 4 plus 71) and g=2^35 with g_1mod4=0.
Since g>0 is satisfied, no exclusion is claimed (consistent with non-exclusion).
Writes fallback_gap.json with g and its decomposition.
"""
from fractions import Fraction
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
t = {w: Fraction(w * A[w], 72) for w in range(73)}
Ap = {w: A[w] - t[w] for w in range(72)}
Bp = {j: (A[j] - t[j]) + t[j + 1] for j in range(72)}
assert all(v.denominator == 1 for v in list(Ap.values()) + list(Bp.values()))
Q = {j: Bp[j] - Ap.get(j, Fraction(0)) for j in range(72)}
assert all(A[w] == 0 for w in range(73) if w % 2 == 1), "Type-II parent: A_odd=0"
assert all(t[w] == 0 for w in range(73) if w % 2 == 1), "t_odd=0 from 0<=t<=A"
assert all(Ap[w] == 0 for w in range(72) if w % 2 == 1), "A'_odd=0"
assert all(Q[j] == Fraction(0) for j in range(72) if j % 2 == 0), "Q_even=t_odd=0"
assert all(Q[j] >= 0 for j in range(72)), "Q_odd=B'_odd>=0"
assert all(Q[j] == t[j + 1] for j in range(72)), "Q_j = t_{j+1} check"
# Q supported on odd weights only?
assert all(Q[j] == 0 for j in range(72) if j % 2 == 0), "Q must live on odd weights"
g = sum(Q[j] for j in range(72) if j % 4 == 3)
g0 = sum(Q[j] for j in range(72) if j % 4 == 1)
print("coset excess Q = B' - A' nonzero (j: value):")
for j in range(72):
    if Q[j]:
        print(f"  Q[{j}] = {Q[j]}")
print("g = sum Q over 3-mod-4 =", g, "=", int(g))
print("g0 = sum Q over 1-mod-4 =", g0, "=", int(g0))
print("Q total =", sum(Q.values()), "=", int(sum(Q.values())), "(= 2^36 - 2^35 = 2^35:", sum(Q.values()) == 2 ** 35, ")")
assert g.denominator == 1 and g >= 0
# lemma: for any genuine binary Type-II parent A_odd=0 so t_odd=0 by 0<=t<=A
# and complement symmetry; then Q_even=t_odd=0 and Q_odd=B'_odd>=0 because
# A'_odd=0; hence Q>=0 and g=sum_{j=3 mod 4} Q_j>=0; here g takes the fixed
# logged value on the putative cell (g>0 satisfied, so no exclusion claimed).
json.dump({"g": int(g), "g_1mod4": int(g0), "Q_total": int(sum(Q.values())),
           "Q": {str(j): int(Q[j]) for j in range(72) if Q[j] != 0},
           "theorem": "Lemma: for any genuine binary Type-II parent A_odd=0 so "
                      "t_odd=0 by 0<=t<=A and complement symmetry; then for the "
                      "shortened/punctured pair Q_j=B'_j-A'_j satisfies "
                      "Q_even=t_odd=0 and Q_odd=B'_odd>=0 because A'_odd=0; "
                      "hence Q>=0 and g=sum_{j=3 mod 4} Q_j>=0 (puncture "
                      "excess, not the Conway-Sloane shadow enumerator of the "
                      "shortened code). On the putative extremal cell "
                      f"g = {int(g)} with g_1mod4 = {int(g0)}.",
           "non_exclusion_note": "g > 0 is satisfied (no violation); the gap value "
                                 "serves as the obstruction baseline per fallback."},
          open(os.path.join(HERE, "fallback_gap.json"), "w"), indent=1)
print("wrote fallback_gap.json")
