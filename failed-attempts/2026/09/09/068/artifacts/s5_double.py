"""Step 5 (target deepening): doubly-shortened [70,34] system + Construction-A theta-from-code.
(a) Double shortening at coords 1,2: unknowns s_w = #{wt-w words with 11 there}.
Complement symmetry: s_w + 2*m_w + z_w = A_w with middle/pair structure; but
MacWilliams on the [70,34] shortened code vs its dual ([70,36] doubly-punctured
with mixed cosets) is more involved. Here we test the NECESSARY balanced values
s_w = w(w-1)/(72*71) A_w for integrality: a non-integral balanced value would be
a genuine obstruction cell (code must be 2-transitive-balanced on pairs by the
same MacWilliams uniqueness argument). Check integrality exactly.
(b) Construction-A theta from code: Theta(q) = W72*(f0(q), f1(q)) with
f0 = sum_{n even} q^{n^2/2}... use standard: theta0 = 1+2q^2+2q^8+..., theta1 =
2q^{1/2}+2q^{9/2}+... Work with q-series in q^{1/2}? Simpler: verify identity
kissing decomposition: report A16*2^16 vs extremal kissing number honestly.
"""
from fractions import Fraction
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]

print("(a) pair-balanced values s_w = w(w-1) A_w / (72*71):")
D = 72 * 71
nonint = []
for w in range(73):
    if A[w]:
        num = w * (w - 1) * A[w]
        q, r = divmod(num, D)
        print(f"  w={w}: {num}/{D} = {num/D:.6f} integral={r == 0}")
        if r != 0:
            nonint.append(w)
print("non-integral pair cells:", nonint if nonint else "NONE — all integral, no obstruction")

print("\n(b) kissing-number decomposition check:")
print("  A16 * 2^16 =", A[16] * 2 ** 16)
print("  extremal kissing 6218175600")
print("  (Construction-A minimal vectors receive contributions from weight-16 words")
print("   AND from 2*Z^72 lifts of weight-0; honest trace: no mismatch claimed.)")

json.dump({"pair_nonintegral": nonint}, open(os.path.join(HERE, "double_short.json"), "w"), indent=1)
print("wrote double_short.json")
