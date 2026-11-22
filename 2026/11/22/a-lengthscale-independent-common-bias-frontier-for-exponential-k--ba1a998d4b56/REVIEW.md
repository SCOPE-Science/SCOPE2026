# Scientific review

## Correctness — PASS
The claimed posterior weights are defined by the invertible covariance system \((K+\tau\mathbf1\mathbf1^\mathsf T)w=m\). The exact tridiagonal precision, geometric kernel mean, and rank-one inverse give the formulas for every \(n\ge2\), \(\lambda>0\), and \(\tau\ge0\), without numerical extrapolation. The sign boundary follows from a single linear factor. The weak signed-measure limit follows from two endpoint limits and a Riemann sum. The independent-nugget comparison follows from strict diagonal dominance of an \(M\)-matrix. Exact rational and numerical tests substantiate algebra but are not infinite proofs.

## Originality — PASS, provisional
Karvonen, Kanagawa and Särkkä, arXiv:1812.08509, define Bayesian quadrature weights and investigate their positivity for noiseless evaluations; their full open-access article includes a specific discussion of Matérn positivity as open to further work. Cai, Lam and Scarlett, arXiv:2202.10615, study randomized/noisy quadrature with independent Gaussian noise and average-case error bounds. Their inspected results do not entail the rank-one shared-error sign law. The closest accessible related numerical designs with a stationary exponential covariance assume noiseless or independent-noise readings; those neither give the threshold \(1/(n-2)\) nor its signed-measure limit. Search failure is not proof of priority. Uninspected historical correlated-error kriging and quadrature literature remain a residual risk.

## Value — PASS
A shared calibration offset is qualitatively different from independently vanishing measurement errors. The exact frontier reveals a non-obvious, lengthscale-independent transition, increasingly restrictive with sensor count. Negative endpoint weights mean nonnegative sampled data can yield negative integral estimates; the sharp negative mass measures this instability. The persistent endpoint atoms make the distinction substantive even under dense sensing. These are structural stability results for a natural numerical-integration and sensor-calibration model, not merely a numerical sample or reparameterization.

## Scientific limitations and comparison risks
The covariance amplitude and uniform integration measure are normalized; nodes include both boundaries. The conclusion applies only to a common additive observation error and the exponential Markov covariance. It does not extend by assertion to a kernel constant component, nonuniform grids, independent-plus-shared errors, or other kernels. The closest inspected full texts do not claim the same frontier, but exhaustive historical priority and independent proof verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
