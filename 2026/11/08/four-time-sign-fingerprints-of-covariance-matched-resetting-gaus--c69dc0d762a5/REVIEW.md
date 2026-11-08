# Scientific review

## Correctness — PASS
The three stationary baths and their common covariance are explicitly defined. For the reset Brownian bath, the generator gives the stationary second and fourth moments; conditioning on reset/no reset gives the first three conditional polynomial moments. Backward iteration yields the exact all-four-time raw moment, and subtraction of the three covariance pairings yields the claimed connected fourth moment. Its bracket is bounded below by three. Direct two-state Markov conditioning gives the negative telegraph expression, and Gaussian Wick factorization gives zero. Absolute fourth-moment integrability follows from Minkowski's inequality for integrable probe kernels, and cumulant Fubini preserves strict pointwise signs. The independent generator/matrix checker passed 432 parameter/time configurations and a positive-filter quadrature, but these finite diagnostics are not substitutes for the proof.

## Originality — PASS, with limits
Guéneau, Majumdar and Schehr, *Active particle in a harmonic trap driven by a resetting noise* (arXiv:2306.09453), derive the same reset-Brownian driver covariance and probe two-time correlation. Examination of the public full text (not merely its abstract) covered the noise section containing their equation (37), the time-dependent moments section and Appendix G devoted to two-time correlations. None of these passages states the ordered four-point connected kernel or its strict sign under all nonnegative filters. Existing Brownian functional and resetting literature addresses other statistics and may provide related general tools. Gaussian and telegraph cumulant calculations are comparison premises, not priority claims. No search proves global novelty; unpublished and unindexed multipoint treatments are residual risks.

## Mathematical value — PASS
The formula resolves a nontrivial identifiability issue: three physically distinct persistent driving baths can have *exactly* the same autocovariance, including after stable linear confinement, yet a sign-definite fourth-order test separates them for any four observation times and any nontrivial positive probe kernels. This is a universal qualitative property beyond a particular parameter fit or single-time kurtosis. The allowed filter class is motivated by cooperative overdamped harmonic response; its nonnegativity is necessary for the claimed unconditional sign preservation.

## Closest literature and limitations
- Guéneau–Majumdar–Schehr (2023), arXiv:2306.09453: same underlying reset Brownian driver, one-time statistics and two-time correlation, not the stated four-time sign theorem in inspected text.
- Singh–Pal (2022), DOI:10.1088/1751-8121/ac677c: Brownian first-passage functionals with resetting, a related but distinct observable.
- Classical Gaussian and two-state Markov moment identities give comparison cases; no new claim to these identities alone.

This review is restricted to the displayed stationary Poisson-reset/no-reset-to-zero model and positive deterministic linear response kernels; it does not establish unique experimental identification in the presence of other unknown non-Gaussian drivers. Broader general frameworks could yield this special case without stating it explicitly.

Self-review: passed. Independent audit: not yet performed.
