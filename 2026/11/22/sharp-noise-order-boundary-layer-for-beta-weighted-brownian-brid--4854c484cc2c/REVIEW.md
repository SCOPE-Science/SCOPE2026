# Self-review

## Correctness: PASS

Independent rational integration verifies \(\operatorname{Cov}(A_n,B_t)=t(1-t^n)/(n+1)\) and \(\operatorname{Var}(A_n)=n^2/((n+1)^2(2n+1))\). Gaussian conditioning gives the exact squared-error Bayes risk. The derivative sign polynomial has exactly one interior root: Descartes' rule plus endpoint signs for positive noise; factorization and a simple endpoint root for zero noise. The optimizer is genuinely global because explained variance is positive inside and zero at the endpoints. The implicit-sign argument gives strict noise monotonicity for \(n>1\). The root identity and bounded scaled location establish the noise/order crossover and information asymptotics. The included exact-arithmetic and numerical reproductions passed; finite numerical grids are not used as uniqueness proofs.

## Originality: PASS (historical-priority qualified)

Compared the full Brownian polynomial approximation from Foster–Lyons–Oberhauser (arXiv:1904.06998), Cai–Lam–Scarlett's Bayesian quadrature bounds (arXiv:2202.10615), Santin's bridge-kernel interpolation analysis (arXiv:2210.15959), and Karvonen–Kanagawa–Särkkä's quadrature-weight theory (doi:10.1007/s11222-019-09901-0). These works supply the basic bridge operator, polynomial moments, Gaussian conditional projection, generic noise bounds, or stability conditions, but their inspected statements do not imply the exact unique Beta-weighted one-point optimizer plus all three order/noise limits. Related research-record searches found two-node uniform-target and deterministic Beta-stratification results, not equivalent theorems. Residual risk: an obscure single-sample weighted Wiener-quadrature result or a broader yet unlocated optimal recovery theorem could contain this specialization. Publication priority remains unverified by an independent expert.

## Value: PASS

The Beta-weight family is a normalized natural sequence of polynomial test functionals concentrating at the terminal endpoint. It tests whether the optimal sensor should follow that concentration under a measurable noise floor. The exact solution reveals two non-interchangeable limit orders, establishes a logarithmic location boundary layer, identifies the narrow \(n\eta\) transition, and quantifies information collapse. These results matter for the placement of severely resource-constrained sensors estimating higher polynomial path moments; they are more informative than re-evaluating a known covariance formula for one arbitrary weight. This is not a claim about arbitrary weights or multipoint designs.

## Closest prior science and limitations

Foster et al. (2019), Cai et al. (2022), Santin (2022), and Karvonen et al. (2019) are identified by primary URLs in RESULT.md. A broader exact theorem from inaccessible or older literature remains a priority risk. All claims concern only one noisy nonadaptive point, known Gaussian covariance and Beta polynomial weighting. Numerical verification supports but does not certify the infinite-parameter argument.

Self-review: passed. Independent audit: not yet performed.
