# Independent mathematical audit

## correctness

PASS

Replayed RESULT.md:33–70. For incidence D, the KKT identity is y−u=λDᵀq, with fixed signs on nonfused edges and |q|≤1 on fused edges F. The affine formula has derivative P_F, orthogonal averaging on fused components. For each F choose distinct block levels and q_F=0 at a base point. Under a small input increment η, the candidate output increment is P_Fη and the stationarity correction is obtained by solving λD_Fᵀδq=(I−P_F)η; the tree-block incidence map is an isomorphism onto the blockwise zero-sum space. Thus signs and strict bounds persist and every needed derivative actually occurs on an open input set. Finitely many affine polyhedral pieces and continuity give the upper bound by subdividing the input segment. On the quotient modulo constants the single-edge cut steps are an ℓ¹ basis because each has exactly one nonzero gradient coordinate. A block disjoint from the cut edge lies on only one side. If the cut edge lies in A, its only new variations are the exterior edges of A, with magnitudes |A_1|/|A| and |A_0|/|A| on the two sides. Taking nearby pairs in the realized cells attains each needed bound, including 1 in the no-fusion cell. Paths have t_i≤1; a star block containing k leaves gives (n−k)/(k+1); the full comb spine with a central cut gives the asserted lower bound, not an exact comb modulus. These checks cover every λ>0, including two-vertex trees. The finite tree enumeration and KKT examples in the supplied checker were inspected, not executed.

## originality

FAIL

The exact graph-variation modulus of the very same denoiser is covered by the general weighted-graph theorem b4b1357d8d1c. On a tree, its partition/cut maximum reduces exactly to this formula, with attainment and parameter independence inherited. The catalogue match is dated later than the frozen source; this is verified coverage at review, not a priority or dependency determination.

## value

FAIL

The two-input norm is mathematically meaningful and differs from ordinary variation reduction, but this tree restriction provides no independently distinct exact invariant beyond the general partition/cut formula. The comb amplification follows by an immediate choice of cut and block in that formula and is not a surviving additional theorem of this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
