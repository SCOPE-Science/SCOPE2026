# Scientific review

## Correctness — PASS

The claim is an exact inverse-state-count theorem on the full real plane. Eliminating the memory coordinate reduces the problem to \(\sin(bx\cos(V-x))=(U-c)/a\). For fixed \(V\), the phase has at most one stationary point on each tangent continuity band outside a compact interval, so there are \(O(R)\) monotonicity pieces. On each piece, counting sine-level crossings differs from density times phase variation by at most a constant. Total phase variation is \(2bR^2/\pi+O(R)\) by the bounded primitive of the centered periodic function \(|\sin|\). This proves the two interior/exterior phase-level densities and their sharp constants with absolute \(O(R)\) remainders. The determinant formula supplies the critical-versus-regular distinction. The result is not inferred from numerical observations. The accompanying finite checker gives diagnostic agreement for three parameter/target samples.

## Originality — PASS within inspected evidence

The exact model is equation (5) of Ramadoss et al. (DOI: 10.3390/sym14102110), publicly dated 11 October 2022. Its readable sections on general construction, fixed points, bifurcations, symmetry and implementation do not present global image-strip inverse multiplicities or sharp quadratic inverse growth. Han et al. (DOI: 10.3389/fphy.2022.911144) study a different discretized-memristor cosine map. Zhang et al. (DOI: 10.1088/1674-1056/ac7294) study a different map whose first coordinate is affine in its current state with a cosine multiplier. The comparable inverse-valence results located for other nonlinear maps have different defining formulas and do not imply this coefficient or boundary transition. Search results are evidence of comparison, not a proof of mathematical uniqueness. A historical or unindexed equivalent result is a residual risk.

## Value — PASS

One-step predecessor multiplicity is a natural mathematical observable for state reconstruction of a noninvertible map. Here the distinction is substantial: the exact image is a strip, each attainable state has infinitely many possible predecessors, regular inverse sheets proliferate quadratically with window radius, and the entire inverse relation becomes critical at the image boundary, with the leading coefficient halved. This gives an explicit geometric invariant absent from qualitative forward-attractor studies and distinguishes this map from other models with finite or merely linearly growing inverse valence. No claim about chaotic strength or security follows.

## Limits and literature risk

The classification is for real inputs with fixed real target; it is not a finite-domain or modulo-\(2\pi\) state reconstruction statement. No claims concern forward stability or more than one inverse iteration. Accessible scientific full-text comparisons do not eliminate the possibility of equivalent work elsewhere. The finite computational run is not an infinite proof and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
