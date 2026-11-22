# Scientific assessment

## Correctness — PASS

The theorem concerns only reflection-symmetric site pairs and positive independent Gaussian observation noise. Its Gaussian conditioning formula reduces the posterior integral variance to an explicit scalar ratio. Exact differentiation gives the decision function \(T\); its derivative is strictly negative by the stated uniform hyperbolic-function inequalities. The exact endpoint values prove uniqueness and all equality cases, while a one-sided expansion proves the linear collision law. Both numerical and symbolic checkers were executed against the packaged sources. Risks: the finding is not a classification of asymmetric two-site designs, and the numerical grid is not an infinite proof.

## Originality — PASS, qualified

The relevant full-text inspections were Karvonen–Kanagawa–Särkkä (arXiv:1812.08509, particularly Sections 3.5 and 4.5) and Cai–Lam–Scarlett (arXiv:2202.10615, Sections 1–3 and problem setup). The first addresses quadrature weights and stability, including numerical Matérn examples, and the second establishes large-budget noisy kernel-quadrature rates; neither cited inspected result states or implies the specific two-site symmetric finite-noise threshold. Existing exact results for rougher exponential kernels imply no such collapse, because their covariance and scalar stationarity equation differ. Searches of published mathematical records found nearby quadrature topics but not the same statement; this is evidence of a gap, not a mathematical guarantee of novelty. Risks: older small-design Gaussian-process and optimal-experiment literature may contain an equivalent special case, while the broader Pronzato–Zhigljavsky paper was compared at abstract level only.

## Value — PASS

The natural smallest nontrivial noisy Matérn integration design exhibits a **sharp positive-noise transition from spatial coverage to replication**, and the collision is linear in the distance to critical noise, rather than the generic smooth pitchfork square-root picture. This addresses the concrete budget-versus-noise placement question with a complete scalar classification, unique minimizer and explicit posterior variance within the reflection-symmetric family. Its deliberate restriction prevents overstating global optimality; larger sample budgets and unrestricted pairs remain open for this result.

## Sources and scientific limits

- Karvonen, Kanagawa and Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509, https://arxiv.org/html/1812.08509v2.
- Cai, Lam and Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615, https://arxiv.org/html/2202.10615v2.
- Pronzato and Zhigljavsky, *Bayesian Quadrature, Energy Minimization, and Space-Filling Design*, https://doi.org/10.1137/18M1210332 (abstract comparison, not a full-text exclusion).

Self-review: passed. Independent audit: not yet performed.
