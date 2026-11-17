# Review of the dense graphical-zonotope third-intrinsic-volume theorem

## Correctness — PASS

The proof uses the standard zonotope wedge-volume theorem (Joós–Lángi, Corollary 1), then checks the incidence-Gram determinants for all three-edge graph types: weight \(2\sqrt2\) for a matching, \(\sqrt6\) for a two-edge path and isolated edge, \(2\) for a three-edge tree, and zero for a triangle. A triple-edge inclusion-exclusion expansion gives exact coefficients \(A_n\), \(B_\mathrm a(n)\), and \(B_\mathrm d(n)\). The increasing-difference argument establishes the strict inequality controlling all graph sizes, while pair-incidence counting proves the two extremizers and all equality cases. The checker directly verifies the formulas in 2,160 exhaustive deletion configurations and 400 larger deterministic cases; these finite tests are supporting evidence rather than an infinite proof.

## Originality — PASS (historical priority provisional)

Joós and Lángi (arXiv:2206.03204, Corollary 1) supply the general zonotope intrinsic-volume formula. Brazitikos and McIntyre (arXiv:2102.05900) prove related wedge inequalities. Padrol, Pilaud and Poullot (arXiv:2111.12422) study deformations of graphical zonotopes and the permutahedral case. The new discrete deletion-subgraph identity and unique two-sided extremal classification with the sharp gap are not stated or implied directly by the inspected results. Targeted searches for graph-deletion variants did not surface a prior exact theorem. An equivalent statement using weighted three-edge forest counts remains a genuine priority risk, so the result is not claimed to have independently established publication priority.

## Mathematical value — PASS

The theorem globally optimizes a natural Steiner intrinsic-volume invariant over every graph obtained by deleting a fixed small number of complete-graph edges, and distinguishes the opposite, uniquely attaining missing-edge patterns. The exact formula for arbitrary deletions and the explicit strict gap reveal how incident missing-edge pairs compete with three-edge forest geometry. This is a complete structural classification rather than an isolated numerical evaluation.

## Limitations

The proof concerns unweighted root-generated zonotopes and only \(n\ge4\), \(2\le k\le\lfloor n/2\rfloor\). The checker is finite. Historical priority should be independently verified against potentially equivalent graph-invariant formulations.

Self-review: passed. Independent audit: not yet performed.
