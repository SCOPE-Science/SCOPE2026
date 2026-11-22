# Scientific assessment: boundary-cluster Korobov quadrature

## Correctness — PASS

The Bernoulli kernel polynomial, periodic sine density Fourier series and the analytic kernel mean establish the needed coefficients independently. The two-site sum/difference equations have bounded limits. The three-site averaged Gram subsystem has a determinant of order three in the mesh width and numerator of order two; the calculated nonzero positive residue yields the claimed A(1,-2,1) vector law. Exact norm and variance identities give the sharp growth coefficients. The 113 standalone high-precision checks reproduce sample Gram solves and Fourier identities, not the infinite-dimensional analytical proof.

## Originality — PASS, with residual risk

The source by Bartel, Gilbert, Griebel, Kuo and Sloan defines this quadrature mechanism and discusses conditioning and positivity but does not state the sharp boundary-cluster weight law. Closest published findings concern complete-lattice higher-order Korobov positivity, two-node random collision noise tails, first-order full-grid sine-periodized thresholds, or a three-node Gaussian-kernel sign diagram. Their hypotheses do not imply this fixed-size, smoothness-two, three-consecutive-node asymptotic, but their full papers were not all accessible. Exhaustive historical priority is not claimed.

## Value — PASS

This is a structurally motivated and explicitly quantified warning about a particular legitimate subsampling choice: a third nearby lattice node destabilizes optimal weights where a two-node cluster stays bounded. It computes the precise signed-weight and independent-noise amplification scales, rather than merely observing poor conditioning.

## Scientific limitations

The construction is deterministic and intentionally unfavorable, not representative of randomized or well-separated subsets; it does not contradict established convergence guarantees. Only α=2, γ=1, sine periodization, unregularized weights and one dimension are proved; no other parameters or empirical noise models are implied. No independent mathematical audit has taken place.

Self-review: passed. Independent audit: not yet performed.
