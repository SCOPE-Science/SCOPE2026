# Scientific review

## Correctness — PASS
The exact common-scalar epoch map gives iid offsets for fresh reshuffling and a single persistent offset for shuffle-once. For positive \(A\), normalization of the geometric coefficients produces a convex combination and Jensen's inequality. For negative \(A\), the alternating geometric sum satisfies \(0<S_m<1\) for every \(m\ge2\); its leading normalized weight is larger than one and its coefficient vector majorizes a coordinate basis vector, which reverses the multivariate convex order by the standard Schur-convexity lemma for exchangeable draws. Direct covariance identities establish strictness and limiting results. Exact-rational support-level checks and the two-component objective calculation independently validate the nontrivial boundary illustration. The proof is not inferred from computational tests.

## Originality — PASS with qualification
The primary works inspected analyze convergence bounds, fixed-permutation strategies, or noise-spectrum stationary variance, rather than the sign-sharp convex-order comparison of full-epoch endpoints under a fixed aggressive component stepsize. Safran–Shamir derive a scalar sweep product but no convex-order classification. Mishchenko–Khaled–Richtárik assume stepsize ranges that exclude a negative product. Rajput–Lee–Papailiopoulos introduce FlipFlop and compare rates, not arbitrary convex losses. Domingo-Enrich's iteration-time/phase-averaged stationary variance differs from the epoch-endpoint observable, and its zero-th-order model does not establish this signed-product theorem. The key majorization lemma is classical, so this is an exact application-level stochastic optimization classification rather than a novel general inequality. Specialist literature may contain an equivalent affine-iteration specialization; independent review is required to settle precedence.

## Value — PASS
The all-convex-risk reversal is a sharp structural boundary for two standard data-ordering strategies. It shows that stability of every component step does not ensure the customary ordering of random reshuffling and shuffle-once, and provides a quantitative strongly convex quadratic witness and stationary covariance ratio. Because it covers all dimensions with isotropic curvature, all finite epoch counts and the stationary limit, it is not a one-off numerical counterexample or a low-value parameter substitution. It makes no assertion about within-epoch or general-Hessian performance.

## Closest literature and residual risk
- Safran & Shamir (2019), arXiv:1908.00045: common epoch product, strong-convexity shuffling lower bounds.
- Mishchenko et al. (2020), arXiv:2006.05988: RR and SO rates with standard small-step restrictions.
- Rajput et al. (2021), arXiv:2102.09718: permutation strategies and FlipFlop.
- Domingo-Enrich (2022), arXiv:2206.00632: power spectral variance and experimentally smaller SO iterate-time risk in certain small-step regimes; not the same epoch-boundary metric.
- Residual: generic exchangeable majorization and random affine-iteration literature could include an unrecognized equivalent stochastic-optimization corollary. No independence claim is made.

Self-review: passed. Independent audit: not yet performed.
