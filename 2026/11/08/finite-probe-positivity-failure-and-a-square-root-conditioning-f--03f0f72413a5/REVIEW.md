# Scientific review

## Correctness — PASS

The one-step Lanczos reduction gives the explicit compressed and Schur blocks, while the source construction's boundary moments and deterministic trace correction cancel exactly. Full two-dimensional projected Lanczos quadrature yields the two independent chi-square terms. The finite-\(N\) probability follows by convolution; the sharp joint limit uses a chi-square CLT, a law of large numbers, and Chebyshev concentration. The irreducibility extension follows by continuity on a full-measure set of probe vectors. The standalone checker tests exact-rational identities and representative finite cases; the proof, not simulation, establishes the quantifiers.

## Originality — PASS, with residual priority risk

The 2026 primary method proves consistency and supplies equations for the corrected isotropic variance but does not itself give its finite-sample non-PSD probability or the sharp \(N/\kappa^2\) condition. The 2022 and 2016 primary stochastic-quadrature and trace-estimation studies address spectral-sum accuracy, without the same subtracted Schur-complement covariance. Targeted published-record and accessible prior-claim searches uncovered no stronger statement whose implication directly establishes this full algorithm-specific law. General chi-square concentration is classical; a historical derivation combining those tools with covariance subtraction cannot be ruled out.

## Value — PASS

Positive semidefiniteness is necessary for a real Gaussian covariance and its square root. This exact small-dimensional counterexample exposes a failure of an otherwise consistent matrix-free covariance sampler, isolates it from quadrature error, proves it robust under irreducible perturbations, and quantifies how probes must grow with the complement condition number. It is a specific actionable risk benchmark, not merely a normalization check or a general statement that Monte Carlo estimators fluctuate.

## Scope and remaining limitations

The theorem is limited to exact arithmetic, Gaussian probes, the particular Schur-subtracted P-SLQ completion, and the explicit matrix family. In particular, it does not preclude clipping, deflation, or separate positive estimators. Existing broader probability inequalities may yield conservative bounds, and historical priority is not guaranteed.

Self-review: passed. Independent audit: not yet performed.
