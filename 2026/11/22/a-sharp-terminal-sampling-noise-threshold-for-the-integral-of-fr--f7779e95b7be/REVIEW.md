# Scientific review

## Correctness — PASS

Gaussian conditioning gives the exact scalar-integral Bayes risk. Cauchy–Schwarz excludes early observation times at the critical variance; explicit rational derivative bounds exclude all remaining subterminal times, with strictness through the boundary. The covariance monotonicity comparison extends endpoint optimality to every higher variance. A negative endpoint directional derivative guarantees an interior optimizer below the cutoff. The proof treats noiseless observation and the deterministic time-zero reading correctly. The standalone script checks symbolic identities, rational inequalities, and independent numerical integrations; the analytic inequalities, not discrete tests, prove the theorem.

## Originality — PASS, with historical-priority risk

Abundo–Pirozzi (2019, DOI 10.3390/math7100991) gives the integrated fractional Brownian moments, not this noisy-observation design theorem. Cui–Chronopoulou (2023, arXiv:2304.07661), whose one-sample section was inspected, solves *causal path reconstruction* under integrated pointwise squared error, not squared error of the complete time integral and not additive-noise calibration. The older noisy-fBm spline interpolation work uses fixed integer-lattice samples; only its indexed material was accessible, leaving residual risk. Related Gaussian Volterra one-site results assume a different, nonstationary-increment process and cannot imply the fractional Brownian threshold by parameter relabeling. Comparisons with published fractional Brownian occupation-quadrature and other Gaussian integration claims did not identify a covering result. No search proves historical priority.

## Value — PASS

Single-site sensing of a time-integrated long-memory Gaussian process is a natural low-information quadrature problem. For the persistent-memory case \(H=3/4\), the result resolves an exact global endpoint-versus-interior choice and pins the switch at variance \(1/2\), distinguishing long-memory behavior from Brownian sampling. The rational global certificate is reusable as a sharp test case for numerical design methods. This is a specific canonical Hurst-index benchmark rather than a claimed full-Hurst classification.

## Boundaries and risks

Uniqueness of the interior optimizer and sufficient cutoffs at other Hurst parameters remain open here. Multiple, adaptive, or non-Gaussian measurements are outside scope. A historically equivalent theorem could remain in unexamined literature. The evidence and reproduced code are not independent validation.

Self-review: passed. Independent audit: not yet performed.
