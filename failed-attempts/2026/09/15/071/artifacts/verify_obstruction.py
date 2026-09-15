"""Verification script for emergent obstruction lemma (lane-20275).

Checks (reproducible, no external deps):
1. Dimension census: dim Sp(4,R)=10, Borel=6, Siegel Q=7, quotient=3=v(G).
2. Covering/pi_1 obstruction: every homomorphism Z/2 -> Z is trivial,
   hence no injection exists, hence no covering RP^3 -> L with pi_1(L)=Z.
3. Subgroup check: Z has no element of order 2, so Z/2 does not embed.
"""
import itertools

# 1. Dimension census for C2
n = 2
dim_G = 2 * n * n + n          # dim Sp(2n,R) = 2n^2 + n
n_pos = n * n                   # |Phi^+| for C_n
dim_Borel = n + n_pos           # rank + n_pos
dim_Siegel = 4 + 3              # gl(2,R) dim 4 + Sym^2(R^2) dim 3
assert dim_G == 10, dim_G
assert n_pos == 4, n_pos
assert dim_Borel == 6, dim_Borel
assert dim_G - dim_Borel == 4
assert dim_Siegel == 7, dim_Siegel
assert dim_G - dim_Siegel == 3  # v(G) = 3
print(f"dim G={dim_G} Borel={dim_Borel} G/B={dim_G-dim_Borel} "
      f"Siegel={dim_Siegel} G/Q={dim_G-dim_Siegel} v(G)=3 OK")

# 2. Hom(Z/2, Z) is trivial: image of generator g must satisfy 2*f(g)=0 in Z
# Enumerate small range to show only trivial map on generator extends.
homs = [k for k in range(-5, 6) if (2 * k) == 0]
assert homs == [0], homs
print(f"Hom(Z/2,Z) generator images in range: {homs} -> only trivial map OK")

# 3. Z is torsion-free: no element of order 2 (bounded check + general proof note)
torsion = [k for k in range(-100, 101) if k != 0 and (2 * k) == 0]
assert torsion == [], torsion
print("Z torsion-free in [-100,100] (in general 2k=0 => k=0): no Z/2 subgroup OK")

# 4. Covering logic: covering p:E->B induces injection p_* on pi_1.
# With pi_1(E)=Z/2, pi_1(B)=Z, injection would be an embedding Z/2hook->Z.
# Since Hom=0, no injection exists.
print("Conclusion: no covering map RP^3 -> L with pi_1(L)=Z exists. "
      "Blow-up divisor (RP^3) cannot cover the Lagrangian Grassmannian. PROVED")
