# Mathematical review

## Correctness — PASS
The graph polytope is exactly the one-corner truncation of a product of simplices, not a relabeled polar or lattice-rescaled body. Orthogonal block Gram determinants give the removed \(d\)-simplex's Euclidean volume. Computing the areas of original facets that lose their vertex corners and the new oblique facet establishes the surface-area formula in all dimensions, including the two-vertex factor cases. The isoperimetric comparison reduces exactly to a scalar inequality; a symbolic lower bound proves the infinite region with \(p\ge3\), and a separate Taylor bound proves the narrow region \(p=2,q\ge7\). Seven remaining signs are enclosed by exact integer-rational arithmetic using the provided standalone program, rather than inferred from decimal output. Eleven independently projected convex-hull calculations corroborate the area and volume formulas. Infinite assertions rest on the analytic proof, not on the computations.

## Originality — PASS (historical priority provisional)
Almousa, Dochtermann and Smith's graph-root polytope construction treats arbitrary bipartite graphs and product-of-simplices subpolytopes but focuses on subdivisions, ideals, and homological invariants rather than ordinary Euclidean surface area or a sharp edge-deletion isoperimetric classification [1]. Korotov and Vatne's Euclidean product-polytope paper concerns dihedral-angle sums and facet numbers for uncut products [2]. A related complete-minus-diagonal (crown) graph result analyzes volume, Hausdorff distance and random widths [3], and cannot imply the surface quotient's one-edge threshold. These are claim-to-claim comparisons, not a conclusion from nonmatching titles. The exact elementary face-area identities by themselves are not claimed as a substantial novelty. The potentially new content is the exhaustive four-exception classification and distinct asymptotic response regimes. Unindexed equivalent sources and alternate isoperimetric formulations remain an explicit priority risk.

## Mathematical value — PASS
The graph operation is a canonical single edge deletion in the complete bipartite family; normalized surface area is a natural Euclidean quality invariant, stable under uniform scaling. Deletion always reduces volume and raw area here, yet does not have a uniform effect on their dimensionless quotient. The complete sharp finite transition, including four exceptional pairs and a polynomial-versus-exponential scale separation, gives a nontrivial global answer not supplied by classical facet-by-facet volume arithmetic alone.

## Scientific limits and literature
The result is restricted to single missing edges and the intrinsic standard Euclidean metric. The corner-cut construction is elementary, the infinite strict threshold is the substantive content, and the literature search is not a proof of absolute historical novelty.

References: [1] https://arxiv.org/abs/2209.09851; [2] https://doi.org/10.1007/s00022-024-00732-7; [3] https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-rare-exponential-directional-loss-despite-constant-hausdorff-dis--771379f5fcb8/RESULT.md.

Self-review: passed. Independent audit: not yet performed.
