# Scientific review: Gaussian state synthesis by distributed resetting

## Correctness — PASS

For all finite dimensions, the stationary Fokker--Planck equation fixes the reset source as \(p-r^{-1}\mathcal L^*p\). Direct Gaussian differentiation yields a quadratic polynomial whose positivity is equivalent to the stated semidefinite, range and sharp-rate conditions. The proof covers singular semidefinite defects, nonzero means, equality at the threshold, and the thermal zero-threshold exception. Existence and uniqueness follow from the Poisson-renewal resolvent. The exact-rational checker independently verifies 55 polynomial stationary identities for a noncentral example and the specified sharp examples. Its finite checks are corroboration, not an infinite-dimensional proof.

## Originality — PASS (qualified)

Olsen (2023), arXiv:2310.04840, gives distributed-resetting renewal/master equations and forward moment formulas for scalar harmonic confinement. These identities are explicitly credited. The present all-dimensional theorem is an inverse statement about which prescribed joint Gaussians arise from any nonnegative reset probability, with the minimal rate, singular-defect range obstruction and a noncommuting covariance counterexample. Trajanovski et al. (2023), arXiv:2301.12304, study point resetting and comb-constrained OU processes; Evans--Majumdar (2011) and Rose et al. (2018) establish broader reset resolvents, not this explicit Gaussian positivity classification. Searches found no covering statement in inspected sources or accessible research records. Residual risk: a general inverse stationary-density design theorem, including an unindexed one, could subsume this Gaussian specialization even without matching terminology. Independent literature adjudication remains outstanding.

## Mathematical value — PASS

Specifying an exact Gaussian stationary distribution with resets is a natural inverse-control problem. The classification is globally sharp for every mean and covariance in any finite dimension and identifies a physical impossibility independent of reset frequency. Its semidefinite cone differs from the naive equilibrium-covariance ordering when the trap has unequal relaxation directions; the explicit positive-covariance-difference but negative-defect counterexample provides a substantive boundary. The minimal-rate formula supplies an exact feasibility/design threshold rather than a moment-matching heuristic.

## Limitations and risks

Assumptions: isotropic thermal diffusivity, symmetric positive-definite fixed confinement, globally uniform Poisson rate and memory-erasing random-position resets. The result is about exact joint Gaussian stationary laws, not robust inference or cost-optimal resetting. It uses an established stationary master equation; this limits the level of methodological novelty, and an uninspected stronger inverse-design paper could change publication priority.

Self-review: passed. Independent audit: not yet performed.
