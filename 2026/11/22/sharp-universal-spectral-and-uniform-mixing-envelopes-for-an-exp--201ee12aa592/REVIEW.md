# Scientific review

## Correctness — PASS

The result has an exact domain: all real shape parameters, finite dependence parameters, and integer Markov lags. Differentiation of the source copula produces the centered rank-one kernel. Its admissibility bound is necessary and sufficient because the score function takes both extreme signs. Repeated kernel composition proves the lag density, and an explicit single eigenvalue proves maximal correlation without assuming the rank score is optimal. The global-parameter question reduces to the ratio of a squared \(L^2\) norm and a squared uniform norm. A strict derivative argument for the auxiliary integral establishes one and only one maximizer, including all boundary cases; this is not inferred from numerical optimization. The density and eigenvalue equality cases were checked. The reproducible numerical checker confirms the arithmetic, quadrature and two-step convolution. Risk: numerical probes alone cannot certify a continuum, so correctness rests on the displayed analytic proof.

## Originality — PASS (qualified)

The 2023 originating preprint and its extended presentation in the 2025 thesis provide the construction, exact parameter-domain restrictions, Spearman and Gini statistics, and some positive-dependence properties. They do not claim the global maximal-correlation optimizer or sharp Markov transition-density envelope. Longla (2024) proves more general spectral formulas for symmetric square-integrable copulas, so the rank-one lag formula is prior structural technology rather than a new abstract spectral theorem; substituting this specific score still requires the explicit global shape optimization, whose unique root and simultaneously sharp uniform envelope were not found there. The 2026 finite-dependence construction concerns nilpotent operators, whereas the present nontrivial reversible kernel has a nonzero rank-one eigenvalue. Search and relevant textual source inspection found no directly covering optimization. Risk: absence from inspected works cannot establish universal historical priority; possible unindexed equivalent bounds remain a residual risk.

## Value — PASS

This two-parameter dependence family was introduced specifically to improve the attainable strength of association compared with classical FGM copulas. A sharp attainable bound on *all* measurable nonlinear correlations and on transition-density convergence answers a distinct structural question: how strongly dependent can the corresponding stationary Markov chain remain, even at an admissibility boundary? The optimal nonlinear strength \(0.632579805061989\ldots\) is attained at shape \(4.567563049978093\ldots\), different from the source's largest tabulated Spearman value (at shape \(3.8\)). The proof supplies an exact same-parameter worst-case envelope at every lag, not a small numerical improvement to a known correlation table. Risk: this is a within-family classification, not a universal copula or Markov-chain bound.

## Closest literature and limitations

- Zachariah, Arshad and Pathak, *A new class of copulas having dependence range larger than FGM-type copulas* (arXiv:2304.02231; https://doi.org/10.1016/j.spl.2023.109988), Sections 2--3 and rank-correlation table.
- Longla, *New copula families and mixing properties* (https://doi.org/10.1007/s00362-024-01559-9), especially spectral and mixing results in Section 3.
- Longla, *Copulas, m-dependence, and Markov chains* (https://doi.org/10.1007/s11749-026-01003-0), Sections 2 and 4 on nilpotent eigenfunction constructions.
- Zachariah, *Dependence and Uncertainty: A Copula-Based Framework* (IIT Indore dissertation, 2025), Chapter 2, which restates the model and source dependence analyses.

The exact root defining the constant is proved unique; displayed decimals are not definitions. Numerical tests are auxiliary, and scientific priority needs independent verification.

Self-review: passed. Independent audit: not yet performed.
