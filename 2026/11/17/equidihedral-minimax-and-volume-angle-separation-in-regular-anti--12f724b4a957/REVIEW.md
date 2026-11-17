# Self-review

## Correctness — PASS
The exact facet-plane normals and their two adjacency types reconstruct all \(4n\) interior dihedrals. One normal angle increases and the other decreases strictly in positive height; their unique crossing yields the minimax formula. The volume argument explicitly fixes the circumsphere, and the edge-uniform formula and asymptotic comparisons follow algebraically. A separate standard-library verifier reconstructs the geometric facets and passed 261044 finite checks. These finite tests are not an infinite proof; the analytical derivation is supplied in the main result.

## Originality — PASS, historically provisional
Li–Wang–Yu (arXiv:2611.09021v1) solve a different *general polyhedral existence* question. Michon's regular-antiprism section and the accessible Rajpoot (2023) preview give edge-uniform geometry rather than minmax optimization across all heights. Closest published mathematics records concern antiprism shadow complexity, illumination, and ellipsoids; a nearby bipyramid theorem concerns another combinatorial type and has a different asymptotic bound. Search for equivalent equations and alternate names did not identify full prior coverage; the unavailable remainder of Rajpoot (2023) and other differently named historical literature remain risks.

## Mathematical value — PASS
The result gives a sharp all-order minimax angle barrier, its unique equidihedral equality case, and a nontrivial structural clash between equidihedral, equal-edge and fixed-circumsphere-volume optimality. The asymptotic aspect ratios lie in three distinct scales and the conventional choices lose a full \(\pi/3\) in maximum dihedral angle in the limit. These are meaningful comparisons of geometric quality measures, not simple recomputations of the regular octahedron's angles.

## Limitations
Only right equal-radius half-step regular antiprisms are covered. All conclusions are proved in ordinary Euclidean geometry. The numerical checker is finite and floating point; historical novelty, particularly unindexed papers, is not formally guaranteed.

Self-review: passed. Independent audit: not yet performed.
