# Review of angular recognition for Laplacian-column simplices

## Correctness

**PASS.** For a connected weighted graph Laplacian \(L\), the facet normal opposite \(Le_i\) is \(L^\dagger e_i\), since its product with \(Le_j\) is \(\delta_{ij}-1/n\). The unnormalized normal Gram is therefore \((L^\dagger)^2\); its positive-kernel vector consists of the facet-normal lengths. Positive-kernel rescaling recovers that Gram up to common scale, and the unique positive-semidefinite square root of its pseudoinverse recovers \(L\) up to the reciprocal scale. Conversely, a centered positive-semidefinite candidate root with nonpositive off-diagonals is exactly a connected weighted Laplacian, and recomputing its facet Gram reproduces the specified angles. The proof covers all \(n\ge3\) and does not infer the infinite theorem from finite computation. An analytic four-vertex-path example independently verifies the distinction from nonobtuse simplices.

## Originality

**PASS, subject to independent historical priority review.** Braun and Meyer (2017, arXiv:1706.07085) introduce exactly the Laplacian-column simplex but focus on lattice and Ehrhart properties. Devriendt and Van Mieghem (2018, arXiv:1807.06475) review a distinct Fiedler realization whose **vertex Gram** equals a graph Laplacian. Devriendt (2020, arXiv:2010.04521) establishes the general dihedral-angle/normal-Gram identity and the hyperacute-simplex characterization. The proposed theorem combines these mathematical ingredients in a different non-hyperacute class to obtain a sharp *image test* and a constructive inverse recovering the original weighted graph. The general angle/Gram identity and classical graph--simplex bijection are expressly attributed; they are not claimed as new. Previously treated fixed-family dihedral-angle spectra do not give the all-graph weighted inverse. A possible unpublished or unindexed equivalent criterion is the principal remaining priority risk. Full mathematical originality is not independently certified.

## Mathematical value

**PASS.** This is a natural complete classification, not merely a new invariant of one small graph: it decides precisely which complete Euclidean facet-angle matrices arise from the graph-constrained Laplacian-column realization and reconstructs graph edges plus all relative conductances. It distinguishes a metric property of the canonical embedding that is invisible under arbitrary lattice unimodular equivalence, and exposes why the classical hyperacute correspondence is insufficient. The exact nonpositive-off-diagonal spectral sign condition is directly usable for graph inverse questions. It does not assert noise stability or reconstruction from the unordered list of angles.

## Closest literature and limitations

The closest direct source of the *objects* is Braun--Meyer (2017); the closest source of the *normal Gram identity* and the strongest potential implication is Devriendt (2020, §2.2--2.3). Those ingredients are sufficient to motivate the derivation, but the checked relevant sections do not state the weighted inverse-and-image characterization for the Laplacian-**column** embedding. The 2018 correspondence treats vertex Gram matrices, not the square of the Laplacian as vertex Gram. The complete pair-indexed matrix is essential; global conductance scale is invisible; exact zero tests require exact arithmetic; the available literature search cannot rule out every unindexed equivalent statement.

Self-review: passed. Independent audit: not yet performed.
