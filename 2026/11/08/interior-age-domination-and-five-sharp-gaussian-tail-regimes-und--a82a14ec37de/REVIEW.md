# Scientific review

## Correctness: PASS

The stationary Poisson renewal decomposition gives the exact Gaussian covariance segment \(C(y)=Q+y(S-Q)\) with a Beta age weight. Direct matrix differentiation yields \(f'=-u^{\mathsf T}Bu\) and \(f''=2(Bu)^{\mathsf T}C^{-1}(Bu)\), proving strict convexity unless the rate is exactly flat. Standard one- and two-sided Laplace integrals give five explicit constants and the conditional reset-age limits, including both derivative-zero boundaries. The exact two-dimensional witness is verified algebraically, while the standalone checker independently evaluates 130 diagnostic assertions. Restrictions and uniformity limits are explicit.

## Originality: PASS (qualified)

The closest complete primary source is Olsen (2023, arXiv:2310.04840, DOI:10.1103/PhysRevE.108.044120). Its Sections II–IV and conclusions give renewal equations and one-dimensional moment hierarchies, so that foundation is explicitly prior. Its statements do not supply the anisotropic point-density minimizer, the possibility of *intermediate* optimal reset ages, or the five power-law prefactors and conditional-age limits. Trajanovski et al. (2023, DOI:10.1103/PhysRevE.107.054129) concern OU resetting on comb constraints, while the 2026 viscoelastic resetting study (DOI:10.1088/1367-2630/ae868c) has an endpoint-dominated one-dimensional variance mixture. Closely related but unindexed multivariate Gaussian scale-mixture tail asymptotics could establish broader coverage, so publication priority is not asserted absolutely.

## Mathematical value: PASS

A natural physical question not resolved by a stationary moment hierarchy is: which last-reset ages generate extremely unlikely *joint* observations? The answer has a genuinely multivariate interior-age regime impossible for monotone scalar conditional variances, plus sharp critical angular boundaries and different polynomial tail exponents. This determines both the rare-observation spatial decay and the inferred history of a particle; the \(Q=I_2\), \(S=\operatorname{diag}(4,1/4)\) witness gives a strict rate improvement over **both** endpoint Gaussian laws. These are structural classifications, not isolated numerical constants.

## Scope and uncertainty

Only pointwise ray density under scalar harmonic relaxation and centered SPD Gaussian reset locations is proved. The formulas are not claimed uniform near angle thresholds or for arbitrary drift matrices, and no independent scientific audit has taken place. The analytical proof establishes the infinite-distance statements; finite numerical quadrature only diagnoses implementation and constants. Unindexed broader Gaussian-mixture results remain a priority risk.

Self-review: passed. Independent audit: not yet performed.
