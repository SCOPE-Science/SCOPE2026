# Independent mathematical audit

## correctness

PASS

The intermediate Euclidean projection has spatial direction x/||x|| and radial size (κt+||x||)/(1+κ²). Its derivative depends affinely on the projected radial fraction in (0,1): the two limits are the radial rank-one projector and the complementary tangent projector, with the same axial row. Each absolute row sum is convex in this fraction, so its maximum is at a limit. Maximizing the axial row uses ||u||₁≤√d; fixing |uᵢ|=s for a spatial row yields equality in the remaining Cauchy–Schwarz bound by taking the other coordinate magnitudes equal. To pass from derivatives to the global coefficient, integrate on generic translated segments (the boundaries have measure zero), then pass to the desired segment by continuity. Row-sign directions at smooth points give the reverse inequality, including endpoint limits. For the lower uniform bound, put Δ=√d−√(d−1)<1. At s=1/√2 the B excess after multiplying by 1+κ² is κ/√2+(1−Δ)/2, and the C excess is 1+κ/√2+κ²(1−Δ)/2; A also exceeds its leading term. For the upper bound use s√(1−s²)≤1/2 and κ/(1+κ²)≤1/2; the respective additive errors are at most 1, (1+√2)/2 and 3/2. Thus the signed uniform bound is correct. The three profile branches have minima at the two switches, both 2/5, and the endpoint limits at κ→0 and κ→∞ are 1/2, giving the claimed confinement. This is an analytic audit of RESULT.md lines 44–90. The supplementary verify.py was inspected, not executed.

## originality

FAIL

The earlier 2026-11-17 Resultary record d5fc2548a47f states the identical exact finite-dimensional optimization for every κ and d and the identical limiting profile and three regimes. The uniform error statement is not verbatim there, but is a direct bound on those already-published scalar objectives using the same maximizing test coordinate and denominator; the optimization and confinement follow immediately. The frozen finding cannot be credited as distinct on these additions. This is demonstrated coverage, not failure to establish historical priority due to inaccessible literature.

## value

FAIL

The coordinate stability question and the moving-aperture optimization are mathematically natural. However, the principal exact optimization and regimes were already established, and the displayed quantitative increment is a routine bound on that same exact formula, not a new finite-dimensional extremal result. The 3/2 error is not claimed or shown to be the best uniform constant, and the record gives no new finite-dimensional crossover or optimizer. No independently valuable surviving claim is established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
