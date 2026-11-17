# Scientific review

## Correctness
PASS. The local difference factorization is valid because median outputs select one of their three neighboring input coordinates on every strict-order chamber. A single input difference contributes only to three neighboring output differences, and the four indicator cases lead to column absolute sums of either one or \(\max\{1,3-8\theta/3\}\). Piecewise-affine continuity transfers this to arbitrary two-input comparisons. Two nonoverlapping strict-rank interfaces provide finite equality data in every dimension \(n\ge6\). Exact rational checks independently evaluate both factors and witnesses. All-dimensional validity rests on the analytical argument.

## Originality
PASS, subject to historical priority limitations. The mean–median blend is already defined in the 2001 work of Ben Hamza–Krim, which examines influence functions, asymptotic variance and root properties. The 2006 Arias-Castro–Donoho preprint investigates mean-squared risk rather than pairwise cyclic variation. The previously published pure-median variation result covers only the endpoint \(\theta=0\). Neither endpoint convexity nor the mean-only contraction yields the sharp cancellation threshold \(\theta=3/4\); in particular their convex bound \(3-2\theta\) remains larger than one for all \(\theta<1\). The 2014 hybrid-median-mean paper was identified, but full-text comparison remains unavailable. Novelty is therefore a best-knowledge claim rather than a historical uniqueness certificate.

## Mathematical value
PASS. For a standard robust/linear smoothing trade-off, the exact transition identifies the smallest linear-averaging proportion that guarantees stability of differences in a natural bounded-variation seminorm, uniformly over cycle lengths. The sharpness family reveals the local sign-cancellation mechanism and establishes attainment; a generic convex estimate would miss the threshold. This applies directly to repeated perturbation control and stability calibration, without claiming a denoising-risk optimum.

## Scope and limitations
The result is for uniform three-point cyclic filters in real finite dimensions \(n\ge6\) with fixed convex mixture weight. It does not classify shorter cycles, more general windows, or other boundary conventions. The 2014 improved-hybrid paper remains a non-decisive literature access risk, and independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
