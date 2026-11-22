# Scientific review

## Correctness (C): PASS

The exact Dirichlet–Gamma decomposition gives every normalized gap and explicitly separates the common denominator. A shared-exponential minimum produces a single nonstandard covariance constant, verified through a convergent double-survival integral and evaluated independently using the dilogarithm identity. The covariance matrix, Fourier spectrum, sign bounds, finite unbiased estimator variance, and Gaussian limit follow by explicit matrix algebra and a one-dependent central limit theorem. The \(n=2\) degeneracy is handled separately. The reproducible standard-library numerical checker passed direct quadrature comparisons, deterministic constant checks, and seeded simulation checks across several sample sizes and cyclic lags. These checks do not substitute for the analytical proof.

## Originality (O): PASS, qualified

The nearest-neighbor estimator itself, circular distance, asymptotic central limit methodology, and the previously reported dimension-one fixed-neighbor variance inflation around \(2.14\) are prior art. Delattre–Fournier (2016, Theorem 1 and Remark 2) and Berrett–Samworth–Yuan (2019, Section 3.4, Table 1) are the closest broader asymptotic coverage. Their general result does not imply the finite-sample circle covariance matrix, its sign pattern, or the exact variance at each integer sample size without additional analysis. Misra–Singh–Hnizdo (2010, Sections 2–3) establish a circular estimator and consistency but not that finite matrix; Jiao–Gao–Han (2017) prove nonasymptotic error-rate bounds rather than exact null second moments. A targeted semantic database search and accessible comparable claims did not reveal the same finite statement. Historical priority remains a risk and independent verification is outstanding.

## Value (V): PASS

The exact finite-null variance is a usable centering and standard-error benchmark for circular nearest-neighbor entropy statistics, whereas a generic \(O(1/n)\) bound or limiting variance does not give a finite-sample variance. The unexpected positive local versus negative nonlocal log-distance dependence and fully explicit covariance eigenspectrum diagnose where the estimator's sampling error originates. This is a natural invariant of a previously studied inferential procedure, not an arbitrary parameter slice. It does not supply exact tail probabilities or a new universal entropy estimator.

## Scope and residual risks

Only i.i.d. uniform circular arclength sampling with first-nearest neighbors is proved. Known numeric \(2.14\) asymptotics and general normality are acknowledged and excluded from originality claims. A relevant but unlocated earlier explicit finite-circle covariance could change the priority assessment. Numerical validation is not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
