# Independent mathematical audit

## correctness

PASS

Elements outside the cyclic rotation subgroup have order four, so for N>=8 the subgroup is characteristic and checking images of the two generators gives the affine automorphism law. For odd u, exactly one of u-1,u+1 has 2-adic valuation one (interpreting zero as infinite valuation); the other must be divisible by N/2 when u^2=1. The four resulting multipliers with the translation condition (1+u)v=0 give exactly the listed pieces. In the commutation congruence, (h,1) commutes with everything; the two multiplier-(1+h) elements commute with each other and with exactly the even-translation piece besides that universal vertex. For even translations the h contributions vanish, so the remaining negative multipliers commute precisely at equal translation mod h. Odd reflection translations pair mod h; mod 4 already excludes commuting across the even and odd pieces for the negative multipliers. This gives the exact join. The maximal seven-cliques share a three-clique, with t more maximal three-cliques meeting the rest only at the universal vertex. This yields 35t+1 triangles, and degree sums give 21t+3 edges. A commuting pair generates its unique Klein four, which accounts for three edges. Independent generator-image permutation enumeration on quaternion groups of orders 16, 32 and 64 verified the graph and counted 15, 29 and 57 Klein-four subgroups. Replay: python3 /workspace/reproductions/frozen_checks.py 4.

## originality

PASS

The affine identification and pairwise congruence are standard ingredients. The exact induced graph and resulting incidence of maximal elementary abelian subgroups are the distinct claims; the strongest available broader commuting-graph theorem does not mechanically imply them. No independent exact indexed match was established.

## value

PASS

The naturally defined involution graph recovers intersections of maximal commuting involution families, not just the total number of involutions. The two maximal elementary abelian orders and their shared vertices explain how the 2-subgroup incidence changes by translation parity throughout the unbounded family. This exact structural invariant is not supplied by a whole-graph connectivity bound or by identifying the ambient group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
