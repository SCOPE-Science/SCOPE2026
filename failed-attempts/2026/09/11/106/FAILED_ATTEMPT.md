# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Factorial-weighted expected-signature decay across levels 2-4-6 for 2D fBm at H=3/8
- **Round:** 2026-09-07-first-light-01
- **Lane:** 954
- **Disposition:** NO_RESULT
- **Domain:** Stochastic Analysis
- **Method:** Wiener chaos and expected-signature estimates

## Problem

Decide whether the expected Stratonovich signature of two-dimensional fractional Brownian motion at Hurst index 3/8 exhibits strictly faster factorial-weighted decay across levels 2, 4, 6 than the semimartingale regime, via two explicit monotone inequalities.

## Attempted claim

Let B be standard 2D fractional Brownian motion with H=3/8 on [0,1] and S its canonical Stratonovich rough-path signature. With e_{2m}=||E[S_{2m}]||_{HS}, the factorial-weighted sequence satisfies e_4*(2!)^{3/4} < e_2*(1!)^{3/4} and e_6*(3!)^{3/4} < e_4*(2!)^{3/4}, i.e. strictly decreasing factorial-compensated decay across levels 2, 4, 6.

## Research outcome

Target blocked: H=3/8 pairing singularity gives Monte Carlo infinite variance and divergent absolute bounds, so the level-6 factorial inequality could not be rigorously closed; clean exit with diagnostics archived.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Monte Carlo point estimates suggest the inequalities hold (e6~=0.10 vs threshold 0.132) but carry infinite variance at H=3/8 and no rigorous error bars; the Beta closed form covers only one pairing; certified singular quadrature with signed cancellation was not achieved within the pass.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Monte Carlo point estimates suggest the inequalities hold (e6~=0.10 vs threshold 0.132) but carry infinite variance at H=3/8 and no rigorous error bars; the Beta closed form covers only one pairing; certified singular quadrature with signed cancellation was not achieved within the pass.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
