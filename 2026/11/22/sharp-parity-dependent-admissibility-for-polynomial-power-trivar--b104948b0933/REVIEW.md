# Review of sharp trivariate copula admissibility

**Correctness — PASS.** The mixed derivative factorizes as \(1-\lambda D_m(x,y)B_\theta(z)\). The proof calculates exact images of both factors for every positive integer \(m\) and all \(\theta\ge0\), including endpoint and parity cases. Positivity of the density is equivalent to three-increasingness because the prescribed function has the correct margins. A unique quadratic critical point handles the even-power negative extremum, and monotonicity of \(r_\theta\) proves the unique transition. The local checker passed 118 supporting assertions; its numerical optimizations do not replace the proof.

**Originality — PASS, with residual priority risk.** The 2024 primary paper proves a conservative sufficient bound for the exact same family, not a necessary-and-sufficient one. The exact odd/even dichotomy, the asymmetric negative boundary and the unique transition are not implied by that bound. The same article's second copula and the classical trivariate FGM construction have different polynomials. Search comparisons with relevant mathematical research records found related sharp-copula-domain work on other models, but no covering claim for this family. Unindexed sources remain possible.

**Value — PASS.** For a published three-dimensional dependence model, an exact parameter space determines when the proposed probability law actually exists. It materially enlarges the feasible negative-dependence region, with a rigorous example at \(m=2,\theta=1,\lambda=-2/5\). The parity transition gives a structural description across the entire natural exponent family rather than a selected numerical case.

The model, the original Proposition 2.1 and Table 1, and the new exact domain should not be confused: the new contribution is the global optimization needed to turn an earlier sufficient condition into an exact classification. The theorem has not undergone independent mathematical review. It does not assert estimation guarantees or results for the distinct second trivariate family.

Self-review: passed. Independent audit: not yet performed.
