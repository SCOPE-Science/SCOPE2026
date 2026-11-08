# Scientific assessment: Gaussian quadratic OLS Monte Carlo moment frontier

## Correctness — PASS

The all-\(q>0\) statement is based on an explicit Gaussian mean/residual decomposition and a partial-regression formula. Its sharp upper bound uses the independent \(\chi_{n-d}\) residual norm, and its necessity uses a positive-probability open witness that forces a nonzero linear numerator in the otherwise singular OLS slope. The independent sample mean transfers every such divergence to the integration intercept, while the remaining terms have all moments. The proof separately handles the integrable bias threshold, exact MSE decomposition, \(d=1\) exception, and excluded affine case. The packaged Python/SymPy checker passed 509 exact assertions. These finite checks are not presented as proving the moment cutoff.

## Originality — PASS with bounded historical risk

Compared with arXiv:1801.01797 (OLS control-variate general formulation and asymptotic CLTs), arXiv:1906.10920 (method selection and finite-sample risk under different assumptions) and arXiv:2006.07487 (stochastic optimization of control variates), the evaluated statement is a fixed-dimensional Gaussian *quadratic-integrand* theorem with a sharp \(n-d\) absolute-moment threshold for every \(q>0\) and every nonzero symmetric quadratic matrix. The comparison is about logical coverage, not title matching. Earlier exact regression formulas and inverse-Wishart principles are acknowledged rather than presented as new. The closest accessible records examined concern related but distinct Gaussian regression or one-dimensional cubic control-variate questions. Historical priority cannot be conclusively established by a finite literature search.

## Value — PASS

This is a motivated boundary of a commonly used same-sample regression-based integration method. The theorem identifies a genuine transition from undefined mean to infinite MSE to finite MSE as sample size exceeds the number of fitted controls. Its proof exposes the geometric residual rank responsible for the failure, while the complete one-dimensional exception and exact bias distinguish it from an arbitrary small numerical counterexample. It has immediate implications for the design and benchmarking of near-interpolating Monte Carlo control-variate schemes; it does not assert superiority of a particular remedy.

## Scientific limitations

Only unregularized OLS, iid standard Gaussian inputs and a nonzero quadratic are covered; no independent testing or publication-priority certification is claimed. The sharpness lower bound depends on the explicit conditional nondegeneracy witness and a Gaussian radial small-ball integral. Related general inverse-Wishart literature might contain a specialization which has not been fully ruled out.

Self-review: passed. Independent audit: not yet performed.
