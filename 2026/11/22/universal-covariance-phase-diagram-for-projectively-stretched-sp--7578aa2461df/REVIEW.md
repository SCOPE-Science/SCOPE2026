# Scientific assessment

## Correctness: PASS

The claim is an exact sign classification of pairwise coordinate covariances of the explicitly defined projectively rescaled spherical-Dirichlet law. Independence of Gamma totals and Dirichlet proportions gives exact within-block factorization; formula (1) reduces every within-block sign to one scalar ratio. Differentiation gives formula (2), and strict moment log-convexity proves strict monotonicity for every finite positive scale. A complete beta-prime asymptotic trichotomy proves the large-scale crossing for **all** positive complement shapes, including the nonintegrable cases. Gamma log-convexity proves the baseline and strict limiting gaps. The opposite block follows by inversion of scale, and opposing monotonic functions give strictly negative cross-block covariance. The proof uses no numerical extrapolation, finite enumeration, or unproved special-function bound.

The standalone program `verify_covariance.py` passed 96 deterministic high-precision integral and sign checks. This supplementary program tests examples; it does not certify the theorem's universal quantifiers. No independent mathematical audit was performed.

## Originality: PASS on inspected evidence

Guardiola's 2025 source (updated in 2026) establishes strict negativity of undeformed spherical-Dirichlet coordinates and their exact moments, but does not study blockwise projective deformation or a two-boundary phase diagram. The 2020 original reports undeformed moments only. Furman, Kye, and Su (2019) and Lakhani (2026) study ordinary scaled Dirichlet compositions with unequal Gamma scales, including positive-covariance examples or general mixed moments, but do not supply simultaneous unique reversals of the square-root directional covariances. Geneyro and Núñez-Antonio (2022) project independent Gamma variables instead of coordinatewise Gamma square roots and focus on density modeling and inference. Targeted statement-level searches in mathematical research records found no matching stronger phase classification.

The full 2024 dissertation on alternative hyperspherical Dirichlet-type laws was not accessible; only its abstract was reviewed. That is a genuine historical-priority uncertainty, not evidence of noncoverage. Related literature could contain an unlocated equivalent result. No claim of exhaustive global novelty is made.

## Mathematical value: PASS

The negative off-diagonal dependence familiar in the spherical-Dirichlet model is not stable under a natural coordinate reweighting followed by normalization. The theorem supplies a complete, sharp, globally valid classification for all positive parameters, including two distinct critical scales, synchronization across heterogeneously shaped coordinates, and persistence of negative cross-block dependence. In the area-uniform four-dimensional positive sphere, the thresholds numerically equal approximately \(0.234848401276\) and \(4.258066031391\). This structural phase diagram is useful for designing and interpreting correlated nonnegative directional models and is stronger than an isolated sign example.

## Scope and residual risks

The theorem is restricted to two blocks with a common scale inside each; it is not an arbitrary multi-scale covariance classification. Critical scales are implicit. The inaccessible dissertation and potential unindexed equivalent Gamma-direction results remain priority risks; the proof has received no independent validation.

Self-review: passed. Independent audit: not yet performed.
