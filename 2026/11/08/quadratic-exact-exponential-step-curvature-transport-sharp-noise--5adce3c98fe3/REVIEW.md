# Scientific review

## Correctness — PASS

The theorem is completely quantified for a real Hilbert-valued \(C^1\) curvature path with \(\|h'\|_\infty\le L\) and exponential steps of positive mean. The proof reconstructs each estimator and the realized path integral, shows both unbiasedness statements, and computes the two quadratic error kernels by conditioning and exponential memorylessness. The kernels are absolutely integrable, and their direct integrals are exactly \(2\eta^4\). Affine curvature paths attain the bound, smooth positive derivative bumps on either side of the step mean prove risk incomparability, and test-function separation proves uniqueness of endpoint weights. The standalone exact-rational checker passed 19,525 polynomial configurations; it is corroboration, not an infinite proof. No independent audit is claimed.

## Originality — PASS, with residual priority risk

The 2026 RanSOM paper establishes the exponential Stein identity and a single-endpoint correction; Appendix B.10 expressly observes nonvanishing path residual noise for quadratic objectives. Zhang et al. (2020) establish random-uniform interior Hessian evaluation, and Tran–Cutkosky (2022) establish endpoint Hessian momentum updates under second-order smoothness. None of the examined relevant passages establishes the present *two-endpoint, quadratic-exact exponential control variate*, its sharp \(2L^2\eta^4\) error, both exact kernels, the strict ordering reversal, and the endpoint uniqueness assertion as a single result. Existing control-variate principles are acknowledged, not claimed novel. The possibility of an equivalent general random-quadrature or Stein-control-variate result remains a material historical-priority risk; search absence does not prove novelty.

## Mathematical value — PASS

The 2026 method deliberately trades an auxiliary evaluation for an endpoint-only Hessian product, but its pathwise stochastic error remains order \(\eta\) even for quadratic objectives. The theorem identifies the exact extra information needed to remove that obstruction, quantifies the sharp \(\eta^2\) root-mean-square curvature-variation error, and establishes how this endpoint-based alternative compares to unbiased interior probing. The strict nonordering prevents a misleading blanket recommendation. This is a theoretically motivated oracle-cost/error tradeoff, not a claim of superior training convergence. The added initial Hessian product and Lipschitz-curvature requirement are important limits.

## Sources and remaining risks

Closest primary sources: *RanSOM*, arXiv:2602.06824, Sections 3.1 and B.10; *One Sample Stochastic Frank-Wolfe*, PMLR 108 (2020), Section 3.2; *Better SGD Using Second-Order Momentum*, NeurIPS 2022, Section 2. A broader quadrature theorem or prior use of the particular endpoint control variate may subsume some or all of this contribution; no exhaustive historical uniqueness is asserted. Stochastic-oracle noise, random-direction correlations, and full-optimizer rates are not addressed.

Self-review: passed. Independent audit: not yet performed.
