# Scientific review

## Correctness: PASS

The claim is limited to real rank-one-spiked positive-semidefinite Gram matrices, deterministic unit starts of positive gap, fresh isotropic tangent directions, and exact two-plane Ritz optimization. The equality for the gap ratio follows from optimal projection of the leading eigenvector, conditional isotropy yields independent Beta factors, and the finite-dimensional gamma moment formula follows by the Beta integral. Dimension-scale gamma ratios produce a differentiable scaled cumulant generating function with steep upper boundary; exponential tilting and concentration prove matching lower exponents and exponential tightness supplies the full large-deviation upper bound. The Legendre transform and the one-sided monotonicity give the exact stated rate and tails. The independent numerical script checks 320 direct Ritz updates, 12 moments, and 12 analytic limiting identities, but finite tests are not substituted for proof.

## Originality: PASS (with residual priority risk)

The closest comparison is Bresch–Melnyk (2026), Algorithm (2), Example 2.4, and Proposition 2.5. Their exact spiked ascent identity, expected contraction factor, and Beta spherical-cap probabilities establish the building blocks, and the elementary iid Beta reduction is not represented as a separate fundamental discovery. Their displayed results do not assert the simultaneous dimension-and-iteration large-deviation rate \(I_c\), or both sharp success/failure exponents. Earlier Bresch et al. (2024; 2025) cover the algorithm and almost-sure/sublinear convergence in broader settings, rather than this dimension-scale rate. The independently identified historical comparison of random sections of spiked ellipsoids concerns a one-shot geometric radius law, not the iterative logarithmic-gap sum. Literature and published-record searches are not a proof of absence; an unlocated equivalent application of a generic Gamma/Beta-product LDP is a residual risk.

## Value: PASS

The question answers how many random tangent-plane steps are reliable in dimensions growing with the budget. Expected-error convergence does not give the probability of meeting a prescribed spectral tolerance. The sharp rate gives exponential success and failure thresholds on both sides of the natural \(k\sim cd\) scale, and a concrete log-rate/mean-rate separation in dimension three. This is a natural algorithm-specific reliability invariant, not an arbitrary low-dimensional parameter slice or a routine numerical recomputation.

## Scientific limits

Single spectral spike; real sphere; exact independent Haar tangent sampling; exact Ritz maximization; dimension-linear iteration scaling. No extension to general eigenvalue spectra, numerical inexactness, or complex tangent geometry is asserted. Independent verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
