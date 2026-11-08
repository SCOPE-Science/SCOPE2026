# Review: convex ridge circle perimeter monotonicity

## Correctness (PASS)
For every pair of nested positive-radius planar disks, the signed projected-center motion is bounded by the radius increase. The exact three-case ReLU perimeter formula and the inequality \(2\tan(\alpha/2)\ge\alpha\) certify all directional derivatives, including touching thresholds. Positive hinge decomposition proves the arbitrary finite nonnegative convex ridge result; rotational averaging proves the power-weight corollary for every real \(p\ge1\). The explicit cap-angle expansion proves square-root failure for a radial step, and bounded convergence produces smooth increasing weights. The standalone checker passed 2,703 numerical diagnostics; these are not substitutes for proof.

## Originality (PASS, provisional)
Csató–Giovagnoli (arXiv:2610.11677v1), Theorem 1.3, requires the smaller convex body to contain the origin and supplies a triangle-inside-square counterexample to dropping that assumption. Saracco–Stefani (arXiv:2306.07770) show that no nonconstant isotropic weight is monotone over *all* convex-body inclusions. Neither statement implies the new disk-specific positive result or its ridge-weight mechanism. Separate semantic and web searches for nested circles, arcsine convex order, boundary power moments, and convex-ridge weighted monotonicity found no exact equivalent; historical priority against specialized circle-measure literature remains a residual risk.

## Mathematical value (PASS)
A broad, nonconstant functional class has unconditional inclusion monotonicity on every pair of planar disks, even when the origin lies outside both. The simultaneous positive theorem and quantitative radial-step counterexample isolate a meaningful structural restriction on weights, refining the boundary between geometric and weight assumptions that governs weighted-perimeter monotonicity.

## Limitations
Planar positive-radius disks only; power weights covered for real exponents at least one; no global claim for arbitrary convex bodies, all increasing radial weights, or powers below one. An independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
