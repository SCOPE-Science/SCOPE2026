# Self-review

## Correctness — PASS

For fixed strictly interior target values, the second sine-square inverse equation produces finitely many limiting phase sheets. The first equation has two exact quadratic-root inverse branches per sheet per sufficiently high period. Differentiating the published map yields a nonzero targetwise Jacobian; summing inverse Jacobians gives the normalized density coefficient and a second-order pointwise remainder. Change of variables on regular inverse charts proves that these are actual pushforward densities. Both the approximating and limiting densities integrate to one, and Scheffé's lemma proves convergence in total variation. The half-integer arithmetic criterion follows by counting monotone sine-square half-lobes. The packaged symbolic and finite-annulus tests passed; tests are not substituted for proof of an infinite limit.

## Originality — PASS (within inspected evidence)

Zhu et al. (2023, DOI: 10.3390/math11143171) introduce the exact map and examine its numerical dynamical indicators, without a singular thin-strip output law. An earlier exact inverse-count analysis of this same map already establishes its unweighted preimage counts, phase staircase and equal-weight inverse-coordinate distributions; these are acknowledged and excluded from the novel claim. The independently published *Two fixed-point saddles per reciprocal phase band in a coupled sine-square map* describes a local fixed-point spectrum, not arbitrary-target inverse-Jacobian weighting. The new assertion is the normalized pushforward law, strong total-variation convergence and the sharp half-integer resonance, not the old preimage count. Existing general area and change-of-variables theory is used as standard background; no uniqueness of publication is certified, and unindexed equivalent limit laws remain a risk.

## Value — PASS

A numerical chaotic-map and pseudo-random-number-generator study naturally motivates the distribution of a one-step output under explicitly specified input initialization. The theorem supplies an exact limiting density and distinguishes strong probabilistic output convergence from a purely combinatorial inverse-branch census. The half-integer parameter resonance where both coordinates become exactly independent arcsine in the limit, for **any** positive reciprocal gain, is a structural, checkable boundary phenomenon. This is mathematically meaningful without claiming statistical quality of iterated or discretized encryption streams.

## Scope and residual risks

All limits require fixed positive parameters and exact real arithmetic. Output density convergence does not imply an invariant or stationary law. The endpoint phase count differs at at most finitely many levels, which does not affect probability convergence. Unindexed same-model mathematical literature may contain overlapping statements.

Self-review: passed. Independent audit: not yet performed.
