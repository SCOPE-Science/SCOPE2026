# Scientific assessment

## Correctness — PASS
The Wiener stochastic-integral representation and Itô isometry yield the exact Gaussian linear-estimation risk, while the conditional estimator is linear by joint Gaussianity. Cauchy–Schwarz reduces joint choice of observation precisions to a total-variation-penalized step approximation problem. Clipping and nondecreasing rearrangement preserve or improve the objective. A strictly beneficial insertion of an intermediate step proves all sensors are active. Stationarity yields a single decreasing scalar equation, whose one admissible solution determines every site and every precision; no boundary or repeated-site design can tie. The direct rational \(n=2,P=1\) covariance calculation and standalone symbolic and numerical checks confirm the formulas. Finite tests do not themselves prove global optimality.

## Originality — PASS, qualified
The closest directly read published Wiener-integral result establishes precisely the *noiseless* grid and risk, which the new result credits as prior work. Karvonen–Kanagawa–Särkkä (arXiv:1812.08509) treats Brownian-kernel quadrature weights; Cai–Lam–Scarlett (arXiv:2202.10615) obtains broad noisy-kernel integration bounds; Pathiraja–Schillings–Wacker (2026) treats sensor-budget filtering rather than this integrated-path target. Accessible database claims and full-text comparisons did not yield a dominating theorem for jointly chosen, heteroscedastic, fixed-total-precision Wiener observations. Unindexed older Wiener-information and free-knot approximation literature remains a genuine priority risk.

## Value — PASS
An exact optimal time-and-precision law for every integer sensor count and finite total precision resolves a natural Bayesian quadrature resource-allocation problem. The optimal nodes converge to a *terminal subinterval*, leaving a strictly positive initial interval unobserved even with infinitely many sensors at fixed total precision; the limit risk is explicit. This sharp boundary behavior is a structural departure from classical noiseless equally spaced sampling, not a merely improved numerical constant.

## Sources and limitations
Inspected relevant primary text: https://arxiv.org/html/1812.08509v2 ; https://arxiv.org/abs/2202.10615 ; https://doi.org/10.1007/s11222-026-10855-3 ; and the closest original noiseless Wiener-kernel result at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-design-loss-and-gaussian-fluctuations-for-stratified-brown--f119d713d36c . The exact theorem is restricted to Brownian-motion covariance, independent Gaussian point-observation noise, and total precision cost. Independent priority and mathematical review are not performed.

Self-review: passed. Independent audit: not yet performed.
