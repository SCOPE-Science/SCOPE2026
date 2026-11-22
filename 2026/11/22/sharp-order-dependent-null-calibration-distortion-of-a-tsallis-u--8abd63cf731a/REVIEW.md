# Scientific review

## Correctness: PASS

Under the fully specified uniform null, the complete spacing vector is Dirichlet with nonzero negative covariances. The exact variance formula follows by direct quadratic expansion. The exponential representation and a bounded-weight triangular-array Lindeberg argument give the true Gaussian scale; elementary power integrals then give the rational variance and its sharp order-wise ratio. At the integer Tsallis order \(\theta=2\), rational finite-sample formulas and the source's own Monte Carlo table provide separate cross-checks. The bundled standard-library checker passed 1607 deterministic assertions and generated 25000 raw uniform observations for a supplementary variance comparison. The numerical experiment is not used as proof.

## Originality: PASS, with priority qualifications

The primary 2022 paper was read through its full-text rendering, including its equation (8), Theorem 7, equation (11), simulation quantiles in Table 1 and references. It prints the marginal-beta variance sum but does not state the covariance-corrected formula, sharp factor \(4<\rho(\theta)<32/5\), or the actual limiting null size of the printed-variance normal cutoffs. The 2021 fractional-entropy predecessor and the relevant sections of the 2024 fractional-generalized successor use distinct score functions and do not state this source-specific theorem. The classical general theory of linear combinations of uniform spacings (including Huffer, 1988) covers the underlying joint-spacing methodology and is expressly excluded from the originality claim. Its full text was not available; generic-statistic coverage, including possible unrecognized earlier applications, remains a residual priority risk. Published claims and mathematical implications, rather than title resemblance alone, were compared.

## Value: PASS

The finding gives the exact sample-size correction and quantifies how the reported normal approximation changes its null size across every fixed admissible Tsallis order. At nominal \(5\%\), order \(2\) produces limiting actual rejection probability \(1.57944924\times10^{-6}\). At \(n=100\), the corrected normal cutoffs closely match the source's independent Monte Carlo critical values, whereas the printed ones are substantially wider. This is a practically consequential calibration result, not a generic warning about dependence or a small improvement to an arbitrary coefficient. It applies only to printed-variance normal calibration, not to Monte Carlo quantiles.

Self-review: passed. Independent audit: not yet performed.
