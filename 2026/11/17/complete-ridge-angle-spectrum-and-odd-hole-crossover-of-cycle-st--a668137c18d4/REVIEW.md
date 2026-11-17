# Review: cycle stable-set ridge-angle spectrum

## Correctness — PASS
The proof identifies the exact irredundant facets using a self-contained argument for the unique half-integral vertex of the odd-cycle edge relaxation and its simple-vertex neighbors. It separately proves that the odd-hole facet is a simplex (circulant eigenvalue nonvanishing), classifies every facet-pair intersection by explicit relative-interior witnesses or forced extra equalities, and computes the three angles from outward normals. The pentagonal disjoint-edge obstruction is treated separately. Exact arithmetic, not floating-point thresholds, checks all facet-pair dimensions at cycle orders 4 through 13. No inference from the finite tests is needed for the infinite conclusion.

## Originality — PASS (historical priority provisional)
The 2018 1-skeleton paper (arXiv:1804.00360) classifies primal edges and does not give the metric facet-pair spectrum. The 2019 online 1-wheel formulation (DOI:10.1002/net.21906) develops odd-cycle inequalities and their optimization, not dihedral angles. The 2024 cycle graph-polytope face-polynomial article studies an edge relaxation, not the clipped odd-cycle stable-set polytope; the complete text was unavailable, so no exhaustive negative claim is made about it. The distinct published results on clique-joined odd-cycle inballs and odd-cycle integrality caps concern other invariants. Scientific novelty means the complete odd-cycle ridge-angle census, sharp \(n=5\) deficit, and angle-order crossover; not defining inequalities or an even-cycle face count. An equivalent earlier description remains a residual bibliographic risk.

## Mathematical value — PASS
The claim describes a complete, coordinate-normalized Euclidean invariant of an established infinite polytope family. The extremal angle switches between structurally different ridge orbits at a sharp order threshold; the exceptional smallest odd cycle loses exactly five ridge adjacencies; and conditioning on the rare obtuse ridges yields a nontrivial two-atom limit, one atom approaching a right angle from above. This is a motivated metric classification tied to the odd-hole facet, not a selected unmotivated numeric slice.

## Limitations
The theorem is specific to standard Euclidean coordinates and odd cycle orders at least five. The numerical checks are finite; independent mathematical verification has not been performed. Prior literature with another terminology may imply aspects of the result; the 2024 full text was not available for comprehensive comparison.

Self-review: passed. Independent audit: not yet performed.
