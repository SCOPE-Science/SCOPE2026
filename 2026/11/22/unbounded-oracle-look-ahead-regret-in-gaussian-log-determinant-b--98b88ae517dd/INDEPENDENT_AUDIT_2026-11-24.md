# Independent mathematical audit

## correctness

PASS

The integer ranks follow from ell=m q^2 j, and D=ell-r1 is a positive multiple of m, so rank r1 with K=1+D/m probes and rank ell with one probe both cost ell+m. The low plateau has total Frobenius mass m a^2/2. For the two pilot ranks the Frobenius residual decreases by delta a^2; the logarithmic residual decreases by delta log^2(1+a), with low-plateau mass L1=N log^2(1+b)<=m a^2/2<m log^2(1+a) since log(1+a)>=4a/5. Thus the weighted earlier residual minus the later residual is positive in each diagnostic. The direction indeed selects one probe in the reduced comparison. At both full-budget allocations the residual log is t times an orthogonal projector, t=log(1+b)>0, of ranks N-D and N. Its Gaussian quadratic form is t times a chi-square variable of the corresponding rank; the determinant correction is exact and the sample mean is unbiased. The preconditioned matrix spectra lie in {1,1+b}, giving exact quadrature by two Lanczos steps or earlier breakdown. The risk ratio is K(1-D/ell^2); it exceeds one for every member because ell^2>m+D (ell>=4m), diverges at fixed beta and m, and equals 635/128 when beta=3/4, m=2 and j=1. The original line 73 says the preconditioner is identity on the captured modes; it is the preconditioned matrix M_r that is identity there, as used by all formulas. RESULT.md lines 55–112 give the analytic replay path; the frozen verify.py and VERIFICATION.md are finite supplementary evidence inspected, not executed. The proof does not require a numerical certificate.

## originality

PASS

Best-of-knowledge pass for the explicit two-plateau counterexample and unbounded full-budget loss for both deterministic short-rank oracles at every fixed rational beta and fixed m>=2. The primary article already supplies pointwise Gaussian risk and the heuristic, and the closest distinct record supplies an exact optimizer test at the true budget, not failure of the reduced-rank test.

## value

PASS

This counterexample isolates extrapolation error from error in Frobenius proxies and in Lanczos. Even exact logarithmic pilot data can cause an arbitrarily worse Gaussian allocation at the same modeled budget, including the recommended fraction and arbitrarily well-conditioned systems. This is a useful limitation on robustness of a mathematically motivated allocation test, not a claim that the practical implementation fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
