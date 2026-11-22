# Scientific review

## Correctness — PASS

The stated \(BV(\mathbb T)\)-to-\(L^2(\mathbb T)\) operator norm and its equality cases follow by Jordan-decomposing the signed derivative into probability measures, coupling positive and negative jumps, and applying strict convexity in the target Hilbert space. Parseval produces the exact all-time series. The real-line step response and Gaussian product estimates supply a **uniform** periodization error for all shorter arc lengths. The limiting profile has exactly one positive critical point because the ratio of complementary Gaussian error functions is strictly increasing; this is sufficient to localize **every** small-time maximizing arc. The standalone checker passed 52 finite assertions including independently evaluated Fourier sums and asymptotic-scale comparisons. Finite computations are not used as a proof of infinitely many times or arbitrary BV functions.

## Originality — PASS, with identified priority risk

The closest classical source, Miranda–Pallara–Paronetto–Preunkert (public preprint 2005-02-19), characterizes BV and perimeter through heat leakage and \(L^1\)-type quantities. Its fixed-volume \(L^2\) rearrangement discussion concerns a smoothed indicator, not the norm of the *residual* \(I-H_t\) subject only to variation. Bramanti–Miranda–Pallara (2011) generalize BV–heat characterizations to Carnot groups; Alonso-Ruiz et al. (2018) treat BV/Besov and Gaussian heat-kernel conditions on Dirichlet spaces. Neither inspected statement determines the exact residual constant, the microscopic arc separation or its complementary-error-function optimization.

Related results for Poisson mixtures and Fejér means use materially different multipliers. Poisson mixture coefficients must be Hausdorff moments and therefore log-convex; the Gaussian heat multiplier fails the necessary \(m_2\ge m_1^2\) condition. The Fejér cutoff yields a different limiting optimization law. No directly dominating result was found in the searches actually performed. An unindexed equivalent in older Gaussian approximation or shape-optimization literature remains a real, explicitly retained risk; failed search is not a proof of priority.

## Value — PASS

The exact sharp all-time operator norm is a natural, scale-sensitive measure of the difficulty of Gaussian smoothing of discontinuous periodic data. The non-obvious structural result is that the worst two discontinuities are **not** separated at a fixed macroscopic distance as time tends to zero: they coalesce at a uniquely determined multiple of the heat-diffusion scale. Their interaction increases the squared-error benchmark by about 20.01% against every fixed positive separation. This is a motivated, exact sharp boundary phenomenon rather than an arbitrary finite computation.

## Scope and residual risks

The theorem is one-dimensional, real-valued, periodic and uses the standard Gaussian heat generator. The precise finite-time maximizing arc lengths are not classified individually. An unindexed mathematically equivalent result cannot be excluded; no independent mathematical validation is claimed.

Self-review: passed. Independent audit: not yet performed.
