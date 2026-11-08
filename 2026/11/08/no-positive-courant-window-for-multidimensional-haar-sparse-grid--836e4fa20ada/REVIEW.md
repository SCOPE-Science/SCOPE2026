# Scientific review

## Correctness — PASS

The theorem is an all-level algebraic calculation, not a finite-dimensional extrapolation. The dyadic quadrant is in the degree-zero Haar sparse space as soon as total level two is present. A transverse first-level Haar factor truncates the longitudinal update to its one-level coarser average, yielding an exact positive projected difference of one quarter on a zero-input fine cell. Every positive Euler step therefore produces a negative value. Adding a sufficiently small positive constant proves failure for strictly positive data. The level-one positive cone has an exact coefficient representation and gives an if-and-only-if Courant restriction. The one-dimensional and level-zero cases are also exact.

The independent-from-formula standard-library implementation in `verify.py` checks exact rational projections in dimensions two and three at several levels. It is finite validation; the general proof is symbolic and supplied in RESULT.md.

## Originality — PASS (best-knowledge, qualified)

Huang (arXiv:2609.17312, Theorem 4.3) establishes an exact \(L^2\) stability limit, but does not analyze order preservation. Guo and Cheng (arXiv:1602.02124) establish sparse DG stability and conservation, not the all-level positivity classification. Gong et al. (arXiv:2405.16117) use a different locally conservative full DG framework; Zeiser (2023) uses a different implicit and stabilized sparse Galerkin method.

Published-record and literature searches, including equivalent cone-tangency, non-Metzler, maximum-principle and projected-upwind formulations, found no covering theorem. The closest records concern local simplex projections, positivity of unrelated numerical time integrators, or a distinct function-space SBP CFL. The absence of an indexed match is not proof of historical priority. An unindexed generic projection/semigroup treatment remains a residual risk.

## Value — PASS

This completes a natural preservation-versus-failure classification for the lowest-order periodic Haar sparse-grid method, including exact spatial-level and dimension boundaries. It reveals that the scheme's sharp Hilbert-norm CFL guarantee and its fine-cell positivity guarantee separate maximally: past the first mixed Haar level **no positive timestep works**, even for one-dimensional motion on a multidimensional sparse grid. This is an actionable mathematical obstruction for transport of nonnegative densities and distinguishes shrinking a step size from changing the spatial projection or adding limiting.

## Limits

Exact periodic dyadic grids, total-level sparse Haar space, nonnegative constant speeds and unmodified forward Euler only. No assertion about nonlinear limiters, other sparse index sets, variable velocities or complete higher-order DG discretizations. Full historical-priority confirmation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
