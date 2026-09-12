"""Attempt: prove the 4-periodic condensation recurrence
  Z_n Z_{n-2} = Z_{n-1}^2 R_{n mod 4}, R={0:1+a^2, 1:2a^2, 2:(1+a^2)/a^2, 3:2a^2}
via Kuo condensation (Balancedtailed?) applied to Aztec diamond.
Kuo's condensation for Aztec: Z(G) Z(G - {corners}) = ... For uniform weights this gives Z_n Z_{n-2} = 2 Z_{n-1}^2? Check: uniform Z_n=2^{n(n+1)/2}: S_n = Z_nZ_{n-2}/Z_{n-1}^2 = 2^{...}: exponent (n^2+n+(n-2)(n-1)-2(n-1)n)/2 = (n^2+n+n^2-3n+2-2n^2+2n)/2 = 2/2=1 → S_n=2 for all n. And our R at a=1: R_0=2,R_1=2,R_2=2,R_3=2 ✓ consistent!
So the two-periodic version is a genuine generalization of the uniform Kuo recurrence with 4-periodic coefficients.
Kuo (2004) "Graphical condensation for enumerating perfect matchings": for Aztec diamond with general weights, Z_n Z_{n-2} relates to Z_{n-1}^2 times ratio of edge weights? The general Kuo formula involves the four corner edge weights.
For the two-periodic Aztec, corners cycle with period 4 as n grows → R periodic. This is very plausible as the rigorous backbone!
Kuo condensation (Theorem for Aztec region): Let G = Aztec_n with edge weights w. Let a,b be opposite outer corners... Z(G)Z(G_{center}) = ... hmm need exact statement.
Alternative: Ciucu's complementation theorem. Either way, the proof reduces to: one application of Kuo gives Z_n Z_{n-2} = Z_{n-1}^2 * (explicit monomial in corner weights); evaluate corner weights for CJ convention → R table.
We must determine the corner edge weights in CJ convention as function of n mod 4, and verify the Kuo factor.
Let's compute: in CJ coords, what are the four corner edges of Aztec_n and their weights?
"""
import numpy as np
from kasteleyn import build_K
# Instead of analytic corners, verify Kuo factor numerically: check S_n equals predicted monomial.
# First, let's understand the Kasteleyn matrix block structure and try Dodgson condensation directly?
# Simpler: verify recurrence to high precision for random a (done). For the PROOF, cite Kuo + compute corner weights.
# Let's extract corner structure: list W/B vertices and boundary edges for small n.
def graph_info(n):
    W = [(i, j) for i in range(1, 2*n, 2) for j in range(0, 2*n+1, 2)]
    B = [(i, j) for i in range(0, 2*n+1, 2) for j in range(1, 2*n, 2)]
    print(f"n={n}: W corners region: min/max")
    print("  W:", min(W), max(W), " count", len(W))
    print("  B:", min(B), max(B), " count", len(B))
for n in [2,3,4,5]:
    graph_info(n)
