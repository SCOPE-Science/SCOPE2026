# Scientific review

**Correctness — PASS.** The covariance identity follows directly from the unbiased coordinate-map moment transfer operator. The equal-diagonal energy drift yields a necessary and sufficient threshold, including divergence exactly at the endpoint. The two-coordinate criterion is the exact positive-definiteness condition for a self-adjoint transformed moment operator, reduced through a Sylvester inverse to the displayed symmetric matrix. The sharp gain ceiling follows from a rank-one Loewner monotonicity and a one-variable maximization. The checker independently passed 427 assertions using exact rational matrices and a few explicitly marked numerical threshold checks. These checks supplement, and do not establish, the all-parameter proof.

**Originality — PASS, with residual risk.** Ding and Li (2020; JMLR 2021) introduce and analyze the identical full-noise RCD-O-LMC update. Their Theorem 3 provides general sufficient Wasserstein bounds; Section 4.3 studies an underdamped counterexample, not the exact sharp quadratic stability or invariant covariance identity. Ding, Li, Lu and Wright (2020–2021) analyze a distinct coordinate-local-noise chain. Actual semantic searches of published mathematical records found related underdamped Langevin-covariance and stochastic-gradient optimization records but not these exact claims; the nearest findings and implication comparisons are detailed in `AUDIT.json`. A historical specialist equivalent may still exist.

**Value — PASS.** This supplies a tight analytical benchmark for the effect of choosing only one gradient coordinate while retaining independent full-dimensional Langevin noise. Correlation-independent covariance inflation for constant diagonal and a strict, sharp correlated-curvature stability gain for unequal two-dimensional diagonals are practically meaningful diagnostics unavailable from purely sufficient small-step bounds. It does not guarantee mixing speed or Gaussian stationary distributions.

**Scientific limitations.** Strictly positive definite constant Hessians only. Sharp anisotropic result only in dimension two. Results concern finite-second-moment stability. Stationary distributions beyond the threshold with infinite moments are not analyzed. Invariant numerical laws need not be Gaussian. No independent scientific audit has occurred.

**Primary references.** Ding and Li, arXiv:2006.06068v1 (2020); Ding and Li, JMLR 22 (2021), 205; Ding, Li, Lu and Wright, arXiv:2010.01405v1 (2020).

Self-review: passed. Independent audit: not yet performed.
