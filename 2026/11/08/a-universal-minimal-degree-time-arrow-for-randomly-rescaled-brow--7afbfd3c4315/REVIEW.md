# Scientific review

## Correctness

**PASS.** The uniformly contractive marked Poisson construction defines a unique stationary law with finite polynomial moments. Its generator preserves the subspaces of first and third powers, permitting an exact semigroup computation. The sign-driving coefficient reduces to the pointwise factor \(-r(1-A)^2(1-A^2)/2\), hence is strict under the assumptions. Positivity and differentiability of the resulting convolution of exponentials give the unique positive optimal lag, including a rate collision. Symmetry and stationarity exclude all lower-degree polynomial antisymmetric witnesses. The standalone rational/numerical checker recorded 1,896 passing diagnostic assertions; its finite coverage is not substituted for the proof.

## Originality

**PASS, qualified.** Dahlenburg et al. (arXiv:2104.14866, 2021) study random resetting amplitudes; Biroli et al. (arXiv:2406.08387, 2024) study fixed signed rescaling and stationary densities and first-passage times. Their inspected texts did not identify the asserted minimal-degree two-time antisymmetry with a universal strict sign or unique maximizing lag. Zanin et al. (2024) address irreversibility diagnostics in a different reset geometric Brownian process; Rose et al. (2018) address fixed-location resets and relaxation spectra. Broader general polynomial semigroup techniques could conceivably subsume parts of the calculation. The assertion is a comparison-based originality judgment, not a global priority certificate.

## Mathematical value

**PASS.** One-time spatial symmetry and ordinary covariance cannot reveal time orientation, while the constructed degree-four correlation is a parameter-uniform strict witness and supplies an analytically optimal observation lag. This sharp measurement hierarchy is natural for a resetting process already known to have a nonequilibrium steady state, and the result covers arbitrary signed random contraction marks rather than just one tuned example. The value is structural, not merely a numerical discrepancy.

## Scope and residual risks

Assumes uniform strict contraction and independent stationary diffusion. It makes no assertion about entropy-production rates, finite-data distinguishability, or absolute novelty against inaccessible research. The self-review establish the mathematical claims under the stated assumptions; independent verification is outstanding.

Self-review: passed. Independent audit: not yet performed.
