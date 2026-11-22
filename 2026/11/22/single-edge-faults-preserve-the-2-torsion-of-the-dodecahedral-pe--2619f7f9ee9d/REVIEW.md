# Scientific assessment: single-edge dodecahedral perfect-matching faults

## Correctness — PASS

The theorem concerns the fully specified graph \(\operatorname{GP}(10,2)\) and all its thirty edges, reduced to three cyclic edge types. Every perfect matching is enumerated by exact recursion (thirty-six intact, twenty-four after any deletion), and all faces are obtained as complete downward closures. On each of the three deleted-edge complexes, a fully enumerated oriented Hasse graph is acyclic under the specified face pairing. The critical two/three-cell counts are \((4,8)\), \((5,9)\), and \((7,11)\); the reconstructed signed integer attaching matrices have Smith diagonals \((1,1,1,2)\), \((1,1,1,1,2)\), and \((1,1,1,1,1,1,2)\). The two-skeleton has no one-cells, so this determines the full homotopy type by the Hurewicz theorem and integer changes of attaching bases. A concrete eight-triangle mod-two two-cycle for each orbit is nonzero in both the faulty and intact complexes, and thus proves the integral torsion inclusion is an isomorphism. The standalone script is complete, reproducible and was executed against the included input-free construction; the recorded output alone is not treated as proof.

## Originality — PASS against inspected evidence

The 2022 Bayer–Jelić Milutinović–Vega paper defines the object and classifies certain honeycomb families, not a single-edge fault on the dodecahedral graph. The 2024 Chandrakar–Singh paper classifies polygonal line tilings and two-row grids, which are not the present graph. Previously published dodecahedral perfect-matching-complex calculations identify the intact Moore summand and twenty three-spheres; they do not determine any damaged graph or its inclusion map. A published icosahedral edge-fault result concerns the **ordinary** matching complex of a different graph. published-finding corpus searches for perfect-extendible, fault, dodecahedral, Moore and generalized-Petersen formulations did not locate a stronger covering claim. Full RESULT texts for two close intact-graph findings were compared, and both primary 2022/2024 papers were inspected at their definitions, theorem statements and scopes. No search establishes universal priority; unindexed or inaccessible equivalent work remains a residual risk.

## Value — PASS

The dodecahedral graph is a canonical cubic polyhedral object whose intact perfect-matching complex has unusual two-primary torsion. Its behavior under loss of a single matching edge is a natural robustness question, not a free parameter slice. The uniform result is a full integral **homotopy** classification and establishes a nonzero induced torsion map: it separates persistence of a Moore-space class from the substantial loss of free third homology. Merely knowing the number of surviving matchings, the intact homotopy type, or mod-two ranks would not yield this conclusion. It supplies a useful exact benchmark for matching-extendibility topology under graph faults.

## Limits and closest literature

The computation is finite, albeit exhaustive and fully reproducible; there is no claimed classification of arbitrary fullerene edge faults. The induced map on free third homology is uncomputed. Exact priority outside the inspected sources is not certified; full text was not available for some older matching-enumeration literature, which is not known to cover the present topological claim. The detailed source-implication comparisons and residual risks are in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
