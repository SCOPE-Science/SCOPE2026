# Scientific review: universal Poisson-mixture BV approximation

## Correctness — PASS

The exact domain is the real periodic distributional BV class with normalized Lebesgue L2, the periodic variation counting two jumps for an arc, and a positive probability distribution of radii with nonidentity mass. The derivative Jordan decomposition represents every nonconstant input, modulo constants, as an average of oriented arc indicators with the precise variation factor 1/2. Parseval reduces the squared optimal constant to an arc Fourier series. For two independently sampled Poisson radii, the corresponding angular sine-phase function is strictly convex in negative logarithmic radius; its nonnegative mixed second difference is strictly positive when both sampled radii are below one. This proves the uniquely optimal half-circle length for every admissible mixture, including endpoint atoms. Equality of the triangle bound forces both derivative-sign measures to be singleton antipodes. The dilogarithm identity is differentiated symbolically, and the three fractional small-time regimes follow from dominated convergence, a harmonic threshold split, and an integrable odd-mesh Riemann sum with explicit integral evaluation. Actual `check.py` replay supplies separate finite consistency checks. No finite computation substitutes for the preceding universal arguments. Boundary assumptions and all normalization factors are stated in RESULT.md.

## Originality — PASS, qualified

Relevant primary full material was inspected: Roncal–Stinga on the torus fractional Laplacian; Carneiro–Svaiter on heat/Poisson *maximal variation*; Gomilko–Tomilov on positive semigroup *subordination*; Prestin–Savchuk–Shidlich on Taylor–Abel–Poisson direct and inverse estimates. Those supply spectral/operator premises or nonsharp approximation bounds, but not the exact all-positive-mixture real BV-to-L2 error norm with every equality case. Two previously published results closest in objects and methods were inspected as complete RESULTS: *Exact optimal two-jump Poisson leakage and its logarithmic boundary law* solves an L1 binary-trace problem, not the full BV-to-L2 problem; *A sharp Lipschitz phase transition for fractional heat on the circle* gives the sharp Lipschitz-to-Lipschitz norm of the smoothing operator, not the error from BV into L2. The previously recorded sharp Fejér BV-to-L2 result concerns a different, non-Hausdorff multiplier and its optimal arc *shrinks* instead of being antipodal. Comparisons are of hypotheses and mathematical implications, not title matching. A comprehensive historical literature equivalence is not guaranteed: an unindexed rearrangement or moment-kernel approximation result could conceivably imply this theorem, so independent priority assessment remains valuable.

## Value — PASS

The all-positive-mixture classification supplies one exact operator-norm and equality theorem covering every Hausdorff-moment Fourier multiplier (as a smoothing operator), and resolves a robust, nontrivial sharp approximation-design question on the circular BV unit ball. The mechanism is an actual mixed-difference convexity obstruction to separating Fourier frequencies, not an individual-coefficient estimate. The fractional family identifies a sharp and fully normalized half-order asymptotic transition, including the logarithmic critical case; neither standard semigroup boundedness nor the separate known Lipschitz and L1 results determines these constants or their optimizers. The classification applies to a natural continuum of smoothing kernels and is mathematically usable as an optimal benchmark for discontinuous periodic signals.

## Closest sources, scientific checks and residual uncertainty

- Roncal–Stinga, *Fractional Laplacian on the torus*, arXiv:1209.6104v1, 2012-09-27: positive fractional-torus spectral context, not the sharp BV-to-L2 error norm.
- Carneiro–Svaiter, *On the variation of maximal operators of convolution type*, arXiv:1309.1529v1, 2013-09-06: Poisson maximal-variation contraction, not the fixed-time L2 approximation error.
- Gomilko–Tomilov, *On subordination of holomorphic semigroups*, arXiv:1408.1417v1, 2014-08-06: Bernstein subordination used as a premise, but no BV sharp constants.
- Prestin–Savchuk–Shidlich, *Direct and inverse approximation theorems of periodic functions by Taylor–Abel–Poisson means*, arXiv:1609.09615v1, 2016-09-30: full-text K-functional comparison gives approximation order, not sharp circular BV-to-L2 constants.
- *Exact optimal two-jump Poisson leakage and its logarithmic boundary law*, published 2026-11-01: binary L1 rather than whole-class L2.
- *A sharp Lipschitz phase transition for fractional heat on the circle*, published 2026-11-17: Lip-to-Lip smoothing rather than BV-to-L2 error.

The review has not independently ruled out every historical equivalent, and numerical replay does not independently certify the analytic proof.

Self-review: passed. Independent audit: not yet performed.
