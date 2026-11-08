# Scientific review

## Correctness — PASS

Conditional on the complete fractional Brownian path, independent within-panel signs yield an unbiased quadrature and additive conditional variances. The bivariate Gaussian sign-disagreement identity, exact self-similar scaling, and a uniform local-covariance expansion derive the finite-sample series and the panel asymptotics. Power-sum trichotomy and a derivative calculation then give all three regimes and the unique minimizer. The accompanying script checks selected special cases and asymptotic predictions; numerical agreement is not the proof. Hypotheses exclude the degenerate \(H=0,1\) endpoints and require fixed positive \(\gamma\).

## Originality — PASS, qualified

The strongest predecessor is Abramowicz–Seleznjev (arXiv:1104.4920): their general stratified Monte Carlo formula and optimal density formally anticipate the smooth-interior optimization, but their theorems assume quadratic-mean continuity with positive Hölder regularity at the endpoint. The fBM positivity indicator violates that assumption (its squared distance from the value at time zero remains 1/2), and their paper does not state the exact non-Hölder three-regime power-grid classification. The optimal-density principle is not novel. Additional inspected sources are Altmeyer (arXiv:1706.03418), on deterministic equispaced Riemann estimators for occupation times including fractional Brownian motion; Altmeyer–Le Guével (arXiv:2108.11632), on stable-process deterministic sample observations; Cui–Chronopoulou (arXiv:2304.07661), on optimal trajectory reconstruction sample timing; and Aurzada–Döring–Pitters (arXiv:2406.09886), on occupation-time distributions via random sampling. Their relevant methods and main statements do not yield the exact independently randomized *graded-panel* error series, the three-regime transition, and the all-Hurst optimal power exponent together. Source and formulation searches in published research records found no statement covering the present claim. The absence of a match is not proof of absolute precedence, and historical probabilistic quadrature literature may contain an implicit general formula; publication priority therefore remains unverified.

## Value — PASS

The time-zero singularity of fractional Brownian sign crossings makes the choice of quadrature nodes consequential. The result converts this singular geometry into an exact optimization rule: overly concentrated meshes lose the polynomial convergence rate, a critical mesh suffers logarithmic loss, and the unique optimal power mesh improves the leading error constant for every Hurst exponent. This is a mathematically motivated guide for stochastic occupation-time quadrature, not merely a relabeling or a finite numerical observation. It does not claim an arbitrary-partition or full-information estimator optimum.

Self-review: passed. Independent audit: not yet performed.
