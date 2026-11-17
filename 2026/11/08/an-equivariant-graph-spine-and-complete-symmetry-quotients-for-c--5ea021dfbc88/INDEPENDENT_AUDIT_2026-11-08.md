# Independent mathematical audit

## correctness

PASS

Every independent set of categorical K_m x K_n lies in a single full row or column simplex; distinct maximal simplices meet only in individual grid vertices. On a d-simplex, let t=(largest barycentric coordinate)-(second largest); the continuous order-statistic map (1-t)u+t e_j (or u on ties) is equivariant under vertex relabeling and fixes its star-shaped image, while the straight-line homotopy stays inside the simplex. It glues over singleton intersections into a strong equivariant deformation retraction onto sd(K_m,n), including coordinate swap. The spine has no edge inversions, so each quotient is a graph with first Betti o_E-o_V+1, and subgroup fixed sets are its pointwise-fixed subgraphs; for swap, only n isolated diagonal grid points. Integral 1-cycles are zero-row/zero-column matrices, canonically U_m tensor U_n, and coordinate swap negates tensor flip by reversing edge orientations. I inspected Python tests of 60 small quotient cases, 104384 local rational retraction evaluations and 872 swap traces; proof is symbolic.

## originality

PASS

Best-of-knowledge PASS only for the *explicit embedded group-equivariant strong deformation retraction* and the resulting concrete all-subgroup fixed/quotient computation; the ordinary wedge-of-circles count is prior work. Fernós–Futer–Hagen (2024) Theorem 2.8 provides an abstract G~homotopy nerve equivalence for equivariant covers, but its statement does NOT assert an embedded equivariant strong deformation retraction, and its G~ (homotopy-commuting) conclusion alone cannot be restricted to fixed loci or naively passed to orbit quotients. This is serious related broader theory, explicitly acknowledged rather than ignored.

## value

PASS

A canonical, piecewise-linear symmetry-commuting deformation *inside* the original complex is a structural refinement of its known ordinary graph homotopy. It makes every natural subgroup fixed locus and orbit quotient computable directly, produces explicit free fundamental group ranks (including diagonal permutation orbitals and swap) and identifies the integral action with its orientation sign; useful concrete geometry not just a new count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
