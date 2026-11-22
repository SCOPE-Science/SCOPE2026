# Self-review

**Correctness — PASS.** The exact Jacobian gives a contiguous triangular array. The exact centered Hoeffding pair kernel has eigenvalues \(\lambda_k=((-1)^k-1)/(2\pi^2k^2)\); an independent canonical remainder is negligible at the \(n^2\) scale. Joint Gaussian Fourier limits give the noncentral first harmonic; the uniformly controlled Hoeffding projections give the outer Gaussian regime. The exact population-depth integral agrees with the limit drift. All 924 standalone verification assertions passed. Limitation: finite checks do not independently certify weak convergence.

**Originality — PASS, with priority risk.** The central null law is already known and excluded. Liu (1988) establishes the depth concept and general consistency, Killeen–Hettmansperger (2020/2021) the null central depth distribution, and Jentsch–Nagy–Wendler (2026) the fixed-query degeneracy dichotomy. None of the accessible statements or closely relevant fully inspected texts gives the shrinking-query noncentral first-harmonic limit or sharp Gaussian crossover constant. A potential unstated local-alternatives specialization in the inaccessible full text remains a priority risk; search absence is not proof of uniqueness.

**Value — PASS.** The movement of the evaluation point is a natural calibration problem in depth-based location testing, where known central and off-center limit theories have different normalizations. The result provides the missing sharp crossover scale, complete limiting family and explicitly quantifiable variance and bias, rather than a generic U-statistic restatement.

Independent validation has not been performed. General U-statistic theory alone does not determine the circle-specific local parameters; the theorem is restricted to exact uniform circular sampling.

Self-review: passed. Independent audit: not yet performed.
