# Scientific review

## Correctness — PASS
The all-pair risk and decoder follow from (i) the standard bivariate-Gaussian sign identity, (ii) a fully evaluated split arcsine integral, (iii) the self-contained prior-variance calculation, and (iv) orthogonal projection onto the four possible sign outputs. Exact sign-reversal symmetry eliminates the interaction term, leaving a nonsingular two-by-two covariance system. For the reflection-symmetric optimizer, strictly concave \(\log a\) and strictly convex \(\log(1+c)\) imply strict concavity of the log explained variance, and its derivative changes sign from positive to negative exactly once. The numerical assertions from the standalone script corroborate the independent analytic proof; they are not used to infer an infinite-domain result.

## Originality — PASS (provisional historical priority)
The mathematically closest related material is the classical bridge and Gaussian sign machinery, one-sign occupation estimation, and one-bit conditional-mean theory for Gaussian signals. Swanepoel (2017) treats linear Brownian areas and the bridge last-sign-change law rather than estimating positive occupation from two signs. Salminen and Stenlund (2019) develop diffusion occupation-time moments, not the two-bit sensor/decoder design. Fesl, Koller, and Utschick (2022) work on quantized jointly Gaussian channel-estimation targets, not a pathwise non-Gaussian occupation functional. Related single-sign occupation formulas do not imply the two-bit conditional structure, general risk, or unique reflection-symmetric optimum without further analysis. Targeted literature searches found no claim implying this exact result. A previously unlocated equivalent treatment under sojourn-time regression or Gaussian sign sampling remains possible; the absence of a search hit is not a proof of novelty.

## Value — PASS
A continuous-time nonlinear path functional is reconstructed from two binary observations, yet the exact unrestricted Bayes decoder and risk reduce to elementary functions for **every** pair of interior sites. The theorem also provides a unique optimal placement in the time-reversal-symmetric design class and an exact, equal-probability three-level trisection calibration. These are natural finite-information benchmarks for occupation-time sensing rather than arbitrary numerical constants. The symmetric two-site optimum has not been proved globally optimal over asymmetric pairs, and the trisection improvement over that symmetric optimum is very small.

## Boundaries and residual risk
No optimality is asserted for arbitrary asymmetric locations, noisy measurements, nonzero thresholds, adaptive measurements, or more than two signs. The originality assessment is limited by possible historical reformulations in sojourn-time and excursion literature. The stated objective and model are exactly those used in the proof and verifier.

Self-review: passed. Independent audit: not yet performed.
