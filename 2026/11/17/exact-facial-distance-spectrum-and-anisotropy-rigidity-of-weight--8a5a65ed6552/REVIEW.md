# Independent mathematical audit

## correctness

PASS

The definition uses the Euclidean distance between F and the convex hull of all vertices absent from F, rather than a supporting-hyperplane margin. Each proper face is a signed one-per-axis subset I. For |I|<d, a missing axis puts 0 in the complementary hull, and every complementary vertex has nonpositive signed coordinates along I; minimizing ||(a_i alpha_i)|| with sum alpha=1 yields 1/sqrt(sum_I a_i^-2), attained by alpha_i proportional a_i^-2. For facets complement=-F, convexity implies min ||x+z||=2 min_F||x||=2/sqrt(sum_all a_i^-2). Strict enlargement of I and the facet/nonfacet inequality show minimizers are exactly (d-1)-faces omitting an axis of maximal a_i, with 2^(d-1) sign choices for each such axis. Diameter 2 max a_i and normalized rigidity follow directly. I checked the inequalities at d=2 and tie cases and independently solved convex-pair quadratic programs for representative d=2,3,4 weights: 114 pairs in this run and further source checker face enumerations; largest residual of the independent QP run was under 5e-14. Finite QPs are corroboration, not proof of arbitrary d.

## originality

PASS

The regular cross-polytope is an established case; the audited final claim extends to arbitrary positive coordinate semiaxes and gives all face-rank distances, all minimizing supports, ties, and exact anisotropy penalty. The full accessible Peña–Wirth paper gives regular examples and norm-dependent bounds for general affine images, not the precise diagonal family. The universal Deza et al dimension bound does not evaluate this family. No exact covering mathematical implication was found in Resultary or the primary comparisons; priority remains provisional.

## value

PASS

This is a complete exact face-to-complement separation spectrum for a natural diagonally weighted cross-polytope family, not a scalar width substitution. The invariant is the sharp Euclidean facial distance used in conditional convergence analysis. Determining which faces attain it, precise tie multiplicities and the unique isotropic equality in a fixed ambient Euclidean metric are independent, mathematically usable geometric facts; the regular case is expressly known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
