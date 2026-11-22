# Self-review

## Correctness — PASS

The result concerns a fixed zero-start Gaussian OU process, one observation, and scalar-integral conditional MSE. Stochastic Fubini and Itô isometry give explicit covariance/variance and Gaussian conditioning reduces design to maximizing a scalar ratio. For positive times, factorization gives derivative \(-2QF/D^2\), with \(Q,D>0\); the cubic has exactly one admissible crossing by strict convexity and exact endpoint signs, with a separate zero-noise factorization. Comparing the root to exact zero- and infinite-noise roots proves strict monotonicity and strictly interior placement. A uniform sandwich proves the stiff-limit expansion. A Brownian functional limit yields the small-damping root. The original theorem is analytic; the finite standard-library checker independently tests the covariance integrals and sampled loss. Remaining scientific risk: algebraic transcription and the Brownian-limit argument require external review, but all steps were reconstructed and the finite tests pass.

## Originality — PASS, with publication-priority risk

Actual semantic searches compared the claim and aliases against published mathematical-result records, the accessible earlier mathematical ledger, and primary literature. Pronzato–Zhigljavsky provides a general posterior-variance/energy principle but does not assert this explicit zero-start OU noisy optimal-time cubic and uniform damping law. Cai–Lam–Scarlett develops noisy Bayesian quadrature error-rate bounds, not an exact one-site minimizer for this covariance. Existing stationary OU quadrature designs use a different covariance and do not algebraically imply this result. Mukherjee's 2003 integral-design publication and dissertation constitute the closest historical priority risk: full article text was inaccessible after public-source attempts, so the accessible abstract cannot exclude an equivalent special case. All novelty conclusions are best-knowledge and subject to independent publication review.

## Value — PASS

This is a natural complete one-observation design classification for the scalar time integral of a nonstationary Markov Gaussian process with measurement noise. The unique explicit cubic avoids nonconvex search, strict monotonicity shows how noise moves the sensor, and a uniform large-damping law provides a robust placement rule. These facts are not merely numerical fits or arbitrary parameter slices. A one-site exact design is modest, but it resolves a meaningful finite-budget optimization question with exact boundaries. It does not generalize to multi-site or unknown-parameter designs.

Self-review: passed. Independent audit: not yet performed.
