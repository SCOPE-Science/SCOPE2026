# Scientific review: Erlang-run support-edge asymptotics

## Correctness
**PASS.** The position-at-reversal perpetuity follows exactly from the linear deterministic flow. Its critical inverse moment is finite by an iterative negative-moment estimate using Gamma small-time and exponential-tail integrability. The equilibrium-age survivor is an explicitly integrated Gamma tail, yielding the full logarithmic prefactor by dominated convergence. Negative-orientation contributions are of one higher power in edge distance. The fixed-mean ordering follows by comparing distinct power exponents. The packaged `check.py` passed 98 finite checks; they support, but do not replace, the analytical limit proof.

## Originality
**PASS under the inspected literature and published-claim comparisons.** Farago–Smith (arXiv:2401.01576, full text) provides general non-Markovian confinement integral equations, but its studied running-time examples are exponential, semi-Gaussian and half-Student, not Erlang. Its edge-rate discussion does not imply the sharp logarithmic multiplier and entrance-moment prefactor. Guéneau–Majumdar–Schehr (arXiv:2306.09453) introduce affine recursions for harmonic active dynamics; the distinct 2026 generalized-velocity result (arXiv:2602.08436, full text) uses exponential intervals explicitly. Published findings for heavy-tailed alternating-run confinement describe power-of-log edges, which do not cover the light-tailed Erlang law. Semantic searches for equivalents, broadened phase-type laws, endpoint tables and indirect stronger implications found no covering theorem. Residual risk: specialized non-Markovian phase-type literature may contain an unindexed equivalent; related published-result full texts were not all accessible.

## Mathematical value
**PASS.** The fixed-mean Erlang-shape ordering identifies a rare-event observable sensitive to the temporal regularity of propulsion even when mean persistence is controlled. The exact polynomial-logarithmic correction and positive computable entrance-moment constant sharpen the leading edge exponent of generic stationary-current analysis. The result is neither a relabeling of the Markovian beta density nor a fixed-parameter numerical curiosity. It addresses the experimentally interpretable occupancy of a thin band near the propulsion-supported turning point.

## Scientific limits
Only integer Erlang shapes at fixed positive parameters, strict sign reversal, no translational Brownian noise. The prefactor is an exact invariant-moment expression, not an elementary closed form. Simulated prefactors are estimates. No claim of independent confirmation or absolute publication priority.

Self-review: passed. Independent audit: not yet performed.
