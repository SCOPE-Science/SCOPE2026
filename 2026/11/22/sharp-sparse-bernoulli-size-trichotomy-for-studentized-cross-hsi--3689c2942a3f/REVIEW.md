# Scientific review: sharp sparse-Bernoulli size trichotomy for studentized cross-HSIC

## Correctness (C): PASS

The theorem is defined for independent scalar Bernoulli margins with \(p_n\to0\), \(np_n\to\infty\) and the published equal-half linear-kernel cross-HSIC studentizer. Exact four-cell algebra produces \(f_r=(nC_r-A_rB_r)/(n(n-1))\), \(Q_n=\sum(g_i-f_1)^2\), and, if \(C_1=0\), \(Q_n=AB[(A+B)/4-AB/n]/(n-1)^2\). These yield the subcritical rate \(T_n/\sqrt{np_n/2}\to1\). For \(np_n^2\to\theta>0\), the joint-overlap counts converge to independent Poisson variables; the first-half jackknife quadratic converges to \(k/4\) on \(C_1=k\ge1\), but vanishes at rate \(np_n^3/2\) for \(C_1=0\). The induced extended-real law and exact critical null rejection probability follow. The published theorem covers the high-intensity Gaussian regime, under its verified moment condition. The packaged independent count/enumeration checker passed 6,638 assertions, but computations are supporting evidence rather than the proof.

## Originality (O): PASS, qualified

Shekhar–Kim–Ramdas (2022 preprint; JMLR 2023) provide the exact test, Gaussian theorem, and **the same critical Bernoulli example**, explicitly identifying its **sign** through two Poisson counts. Those facts are credited, and no novelty is asserted for a generic Poisson approximation. The comparison was at the level of the statistic and implied claims: the accessible primary Sections 3–5 and Appendix B.3 give neither the first-half jackknife's complete extended-real limit nor the explicit 5%-level rejection calculation, and do not establish the subcritical 100%-false-rejection regime. General cross-U theory addresses a related Gaussian mechanism but not this specific boundary. A published record on *Gaussian* linear cross-HSIC addresses a finite-sample heavy-tail phenomenon rather than independent *Bernoulli* sparsity. No directly dominating prior statement was identified in the checked primary texts and scientific records; search failure is not a proof of global novelty. Residual risks: alternative historical formulations or unexamined follow-up literature may contain some of the quantitative limits.

## Value (V): PASS

This is a motivated testing-calibration gap: a widely used permutation-free, normally calibrated independence test can have asymptotic type-I error \(1\) for exactly independent distributions when the rare cross-cell vanishes, not merely a modest variance defect. The explicit value \(0.3685686509430986\ldots\) at nominal 5% in the natural critical window and two infinite limit atoms quantify the actual effect and identify its mechanism. The boundary matters for interpreting population-tail or rare-binary data and for selecting a calibration method. These are genuine quantitative facts beyond the source's already known Poisson sign example.

## Sources and risks

Primary: S. Shekhar, I. Kim, A. Ramdas, *A Permutation-Free Kernel Independence Test*, arXiv:2212.09108 (first posted 18 December 2022); *JMLR* 24 (2023), paper 369, especially Sections 3–5 and Appendix B.3. Supporting: I. Kim and A. Ramdas, *Dimension-agnostic inference using cross U-statistics*, arXiv:2011.05068, and D. Rindt et al., *Consistency of permutation tests of independence using distance covariance, HSIC and dHSIC*, *Stat* 10 (2021), e364. Limitations: linear kernels, equal halves, common shrinking Bernoulli bias, independent coordinates, noninteger critical intensity, and Gaussian rather than permutation calibration. No independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
