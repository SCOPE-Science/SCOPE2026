# Scientific review

**Correctness — PASS.** The finite-sample maximum-likelihood score constraints annihilate the frequency-zero and frequency-first coefficients, and the second coefficient is an explicit odd empirical function. The method-of-moments zero-frequency coefficient has a nonzero influence-function variance. A uniform-on-compact stochastic Taylor bound and a bandwidth-independent polynomial integrated-tail envelope establish the limits without restricting the rate at which the Gaussian precision diverges. Logistic beta-integral identities give the two explicit positive variances. The packaged numerical checker passes 15 assertions; the proof, not the checker, establishes the infinite limit.

**Originality — PASS, with historical-priority qualification.** The originating 2021 preprint and 2023 journal version establish the statistic and fixed-weight Gaussian null process; neither inspected argument supplies the arbitrary-rate diverging-weight collapse and both exact constants. Related Cauchy Stein work uses another score and non-Gaussian frequency weighting; earlier exponential and inverse-Gaussian large-bandwidth laws are on distinct Stein kernels and cannot imply this estimator-specific theorem. Research-record searches did not identify a covering exact statement. Unindexed sources and independently undiscovered results remain possible.

**Value — PASS.** The Gaussian-precision bandwidth is a natural tuning parameter in an existing goodness-of-fit test. The theorem proves that different conventional parameter estimators impose two mathematically distinct smoothing orders, including a sharp rate separation and calibration constants. This identifies the appropriate asymptotic normalization of the null statistic at extreme smoothing. No bootstrap size or power conclusion is claimed.

**Scope and limitations.** IID logistic null; deterministic bandwidth tending to infinity; ordinary logistic ML and moment fitting. The result does not address power, estimated critical values or data-adaptive bandwidths, and historical novelty is not independently certified.

Self-review: passed. Independent audit: not yet performed.
