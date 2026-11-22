# Self-review

## Correctness — PASS

The product covariance integrations yield \(\operatorname{Var}(J)=3^{-d}\), \(\operatorname{Cov}(J,Y_x)=\prod_j(x_j-x_j^2/2)\), \(\operatorname{Var}(Y_x)=\prod_jx_j+\eta\). Gaussian regression reduces risk to one explicit nonnegative function. Its global maximum is interior; first-order equations enforce equality of all coordinates by strict monotonicity, and a one-crossing scalar equation gives unique global site. High-d bounds and log expansions yield the Lambert-W and crossover formulas. The standalone checker verifies finite covariance and root examples; those checks do not substitute for proof.

**Limit and risk:** Finite checks do not prove an infinite family; the proof's interior maximizer argument, unique root and asymptotic logarithmic expansions are essential. Numerical root calculations may underflow at very high dimension and are not used in the theorem.

## Originality — PASS, qualified

The claim is not the known Gaussian conditioning identity, the noiseless/one-dimensional Wiener case, tensor product formulas, or continuous Brownian-sheet filtering. The asserted new comparisons are the all-dimensional unrestricted noisy one-site optimizer and the sharp noncommuting dimension/noise asymptotics. Accessible primary material and semantic mathematical records were checked; no dominating statement was identified. Priority remains qualified, not independently certified.

Closest inspected primary literature: Pronzato–Zhigljavsky (2018), https://arxiv.org/abs/1808.10722 (known tensor kernel/quadrature-potential formulas); Karvonen–Kanagawa–Särkkä (2019), https://doi.org/10.1007/s11222-019-09901-0 (quadrature weights and tensor products); Agram–Øksendal–Proske–Tymoshenko (2024), https://arxiv.org/abs/2407.06386 (continuous noisy Brownian-sheet filtering). The noiseless and one-dimensional Wiener rules are already established premises, not new claims.

**Residual risk:** Published older average-case Wiener-sheet optimal-information literature might contain an equivalent scalar-noise case. The exact covariance criterion alone is not new and is not counted as the contribution. Search non-detection alone cannot establish historical priority.

## Value — PASS

High-dimensional Bayesian quadrature with measurement noise has a substantive scale-selection problem: the noiseless point stays at \(2/3\) in every coordinate, but any fixed positive noise pushes the global optimum to a logarithmic corner boundary layer and accelerates the relative information decay from \((8/9)^d\) to \((3/4)^d/\eta\). The precise exponential-noise crossover gives a calibration law that cannot be obtained by simply tensoring one-dimensional noisy optimizers; it separates two physically meaningful sensing regimes.

**Limit and risk:** Single point only; no result for adaptive sensors, more points, heteroscedastic noise or a more general kernel. The result is not asserted to be a general curse-of-dimensionality theorem for all quadrature methods.

Self-review: passed. Independent audit: not yet performed.
