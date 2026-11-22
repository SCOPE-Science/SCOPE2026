# Scientific review

## Correctness

PASS. The natural-spline tridiagonal Green function gives exact cardinal signs and a two-tail negative-mass formula. A tensor-product Bernstein certificate with nine explicitly listed, nonnegative algebraic coefficients proves the dimension-free finite-boundary inequality. Sharpness follows from centered cells receding from both endpoints, and positive-data extremizers are chosen according to the signs of the cardinal weights. The standalone symbolic checker reproduces the algebra and 315 independent finite-grid instances. Finite computation is supplemental to the analytic all-integer proof.

## Originality

PASS on the stated all-finite-boundary claim, subject to independent priority review. Beatson–Chacko (1990) explicitly acknowledges the previously known infinite-cardinal norm \((1+3\sqrt3)/4\) and numerically tabulates finite natural cubic norms approaching it; neither the infinite constant nor their finite table is proposed as new. Their inspected full report does not give a proof of the sharp *all finite natural-boundary* upper bound or a necessary-and-sufficient all-grid positive-data contrast. Bogdanov–Volkov (2019) covers positivity conditions for classical cubic splines but the inspected natural-type criteria are sufficient local comparisons, not this exact global threshold. Aràndiga–Baeza–Yáñez (2021) modifies Hermite slopes to retain monotonicity, rather than classifying positive data for unmodified natural splines. The closest existing numerical database results concern fixed small knots, other norms, or monotone secant ratios rather than arbitrary-length positive nodal contrasts. Unlocated earlier finite-boundary inequalities remain possible; literature comparison is not an independence proof.

## Value

PASS. Without changing an established spline method, a user can certify that strictly positive sampled values remain positive everywhere on any equispaced grid using only their maximum-to-minimum contrast. The exact limiting constant, finite-grid strictness, and constructed failure for any larger ratio explain a practical safety boundary and distinguish the finite natural endpoint condition from the infinite cardinal calculation. This is a natural all-length shape-preservation classification, not an arbitrary numerical slice.

## Limits

Uniform grids and natural end conditions only. The result is not a monotonicity guarantee or approximation-error estimate, and the historic infinite-cardinal constant is prior knowledge. Final historical-priority review and independent proof audit are not performed.

Self-review: passed. Independent audit: not yet performed.
