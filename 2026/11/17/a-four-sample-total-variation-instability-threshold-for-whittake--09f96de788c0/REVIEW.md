# Scientific assessment

## Correctness — PASS
The induced-gradient norm equality follows from step reconstruction and constant preservation. The first-difference inverse is a strictly positive substochastic gradient matrix, hence is strictly variation-contracting. For the second-difference smoother, the affine-fixed-space obstruction proves a monotone jump amplifier for every \(n\ge4\) and \(\lambda>0\). Exact symbolic inversion and a two-case absolute-value comparison establish the sharp four-point formula. The exact-rational diagnostics in `check.py` were run successfully at 105 dimension/parameter combinations; finite checking is corroborative rather than a substitute for the all-length proof.

## Originality — PASS (best-knowledge)
The closest publicly available claim is *Only first-difference Whittaker–Henderson smoothing is universally range-preserving* (2026), whose second-difference three-point range undershoot does not imply an increase in path total variation: at three points the induced gradient matrix is doubly stochastic and variation norm remains exactly one. Cornea-Madeira's deposited finite-sample formula concerns entries of the HP filter, while McElroy (2008) concerns bi-infinite spectral factorization. A highly relevant 2016 source by de Jong–Sakarya was available through its abstract but not full primary text, with no full text obtainable for inspection; this is an explicitly unresolved bibliographic risk. No equivalent BV norm statement was found in the queried mathematical records or accessible sources. This is not a uniqueness certificate.

## Value — PASS
The theorem resolves a natural path-variation stability boundary for the standard quadratic difference-penalty filters. It makes the four-sample threshold, exact first instability factor, monotone binary witness, and the difference between affine-preserving and constant-preserving smoothing structurally explicit. It is applicable to arbitrary lengths and strengths without dimension-specific searches, and provides a diagnostic reason that curvature regularization does not guarantee TV contraction.

## Scope and limitations
The closed sharp norm is asserted only at four sites; for longer paths a strict inequality and explicit finite choice of a binary amplifier are proved. The model is unweighted, equally spaced, real, finite and nonperiodic. No higher-order, weighted, or nonsymmetric stability result is claimed. Accessible published sources were compared at the implication level; unindexed antecedents and inaccessible primary full text remain risks.

Self-review: passed. Independent audit: not yet performed.
