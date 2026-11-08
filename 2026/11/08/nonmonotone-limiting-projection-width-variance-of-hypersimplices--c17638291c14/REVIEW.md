# Self-review: hypersimplex width fluctuations

## Correctness — PASS
The claim concerns intrinsic Haar-uniform directions of uniform-matroid base polytopes, with a fixed fractional rank. The support function is exactly the sum of the largest coordinate scores; the width is the top-minus-bottom trimmed sum. An empirical-quantile substitution leaves an integrable order-one error, and the centered Gaussian radial normalization contributes the essential quadratic-score correction. A classical iid central limit theorem proves the asserted law; spherical concentration supplies uniform integrability to pass to variances. Recomputed moments give the stated variance, and independent rational interval arithmetic proves the nonmonotonicity inequalities. The degree of proof extends to all fixed fractions in the specified interval, not only the five tested points.

Risk: The steps involving empirical quantiles and uniform moment control require the fixed-quantile, positive-density hypothesis. They do not cover rank fractions approaching zero as dimension grows. Sampling alone would be insufficient, but the supplied analytical proof and exact-rational certificates do not rely on simulated extrapolation.

## Originality — PASS (provisional historical priority)
The closest relevant full-text publication on projection-width moments, Kabluchko–Litvak–Zaporozhets (2015), treats the cube, regular simplex and cross-polytope, not the variable-rank hypersimplex profile. Its cube limiting variance agrees with the half-rank endpoint here and is expressly excluded from the claimed novelty. Casabella–Joswig–Kastner (2024) study hypersimplex subdivisions rather than widths. The existing nearby geometrical records concern other projection or matroid-polytope invariants. There is no identified stronger result implying the new variance profile and its two certified interior extrema.

Risk: Classical results on trimmed sums and Gaussian order statistics can furnish the main asymptotic machinery, and a mathematically equivalent hypersimplex formula may have appeared under statistical terminology. Failed database searches cannot prove absolute priority; an independent literature review remains outstanding.

## Mathematical value — PASS
Random projection lengths measure an intrinsic geometric invariant, and uniform-matroid base polytopes form a canonical infinite family. The mean projection width increases as rank approaches half dimension, but the limiting variance has a rigorously established interior dip followed by a rebound. That contrast is a structural, parameter-resolved geometric fluctuation phenomenon, not an arbitrary finite numerical table, a renaming, or merely a CLT for a preselected scalar variable. The half-rank value recovers an established cube benchmark and situates the new profile between known standard polytope limits.

Risk: A complete classification of stationary points and finite-dimensional error rates remain open within this result; no such conclusions are claimed.

## Sources examined and scientific limits
- L. Casabella, M. Joswig and L. Kastner, *Subdivisions of Hypersimplices: With a View Toward Finite Metric Spaces*, arXiv:2402.17665v1, PDF introduction and the stated main-results outline. This gives the precise uniform-matroid polytope family but no width formula in the inspected material.
- Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479, abstract, Gaussian-width framework, projection-width formulas, and Section 6 including the cube CLT. The half-rank boundary is known; an entire rank-dependent hypersimplex result is not given there.
- Supplements: `hypersimplex_width_check.py`, exact rational Machin, exponential and Gaussian-integral alternating-series enclosures; `hypersimplex_sample_check.py`, independent finite-dimensional sampling. Both ran successfully, with measured values in VERIFICATION.md.

Self-review: passed. Independent audit: not yet performed.
