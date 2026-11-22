# Review of the two-node stochastic-variance revival

## Correctness

**PASS.** The monic global-Lanczos polynomials for the identity-started counting spectral measure are reconstructed from moments. The inverse Hermite remainder identity and the Rademacher off-diagonal variance formula yield the exact binomial distribution without asymptotic approximations. Orthogonality, all nonbreakdown cases, the perturbation derivative and the positive-definite condition-number estimate are proved explicitly in RESULT.md. The extracted exact-rational checker independently evaluates residual matrices and exhaustively enumerates finite sign configurations. Its 1360 passing assertions are supplementary, not an infinite proof.

## Originality

**PASS, qualified.** The closest primary source is Rinelli, Simunec and Vermeiren, arXiv:2611.18864v1, notably Theorem 2.6, Eq. (3.3), and Sections 4.1–4.2. It already establishes the Hermite residual and stochastic estimator; it does not state a monotonicity theorem or the present cross-depth reversal, exact sign law or irreducible unbounded ratio. Hallman–Troester (arXiv:2103.10516) uses multilevel Chebyshev approximations, and Chen–Hallman (arXiv:2205.01736) uses Krylov-based deflation, neither identical to this full-size Hermite correction. Related exact stochastic Lanczos probe laws and generic Hutchinson variance bounds do not imply the asserted two-depth construction. Incomplete indexing of related matrix-function/control-variate literature is a remaining originality risk.

## Value

**PASS.** This is a constructive obstruction to a plausible adaptive stopping principle: a smaller positive deterministic Gauss deficit does not guarantee a smaller stochastic-correction variance. The dimension-minimal binomial witness identifies the role of eigenvector orientation, while robust inflation under arbitrarily small irreducible perturbations rules out the explanation that an exact block-diagonal zero is the only reason for the phenomenon. It is a focused benchmark for depth-versus-sample allocation, not a claim about total runtime.

## Limits

Exact inverse action, exact inner residual correction, independent Rademacher probes, and small well-conditioned tridiagonal spectra only. No guarantee for Gaussian probe variances or approximate practical implementations. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
