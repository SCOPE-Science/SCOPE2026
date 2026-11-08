# Scientific review

## Correctness — PASS

Under the exact synchronous conditional-independence rules, first-round recovery at the unique doubly infected vertex and all neighbor infection acquisitions are mutually independent. Since only one vertex initially carries either pathogen, no higher-order threshold with \(r=2\) is activated in the first round. The two outside-carrier fields at round one are independent and have the stipulated Bernoulli law. Conditioning on the source's four possible first-round states yields exact formulas for both round-two marginals and the joint co-carriage probability. Their algebraic difference factors into the claimed identity. Since \(U,V\in(0,1)\), the unique sign boundary follows. The code independently enumerates every intermediate labeled infection configuration for a genuine overlapping-triangle hypergraph and checks 97 exact-rational settings. Residual science risk: the formula relies on independent synchronous events and on excluding same-round recovery/reinfection; changing these rules invalidates the proof.

## Originality — PASS, qualified

The 2026 primary HyCo-SIS paper defines the same conditional probability mechanism and derives overlap representations and an illustrative one-step example, but the inspected sections do not provide the two-step source covariance or its sharp recovery-dependent sign reversal. Hébert-Dufresne, Scarpino and Young (2020) analyze macroscopic equivalences between interacting and complex contagions rather than this microscopic sign classification. Brian (2025) studies pre-/postinfection priority effects and population prevalence using a different asymmetric model. Accessible earlier related records were checked at the claim level: a single-pathogen mean-hazard closure is not a two-pathogen finite-state joint law. Searches for the symmetric two-step covariance, its source-seed conditional laws, and opposite-sign facilitation/association yielded no dominating result. This remains a best-knowledge originality assessment, not a priority or uniqueness certification; unindexed exact calculations and material outside inspected portions are residual risks.

## Mathematical value — PASS

The sign of cross-pathogen co-occurrence is often used as a heuristic indicator of facilitation versus competition, whereas this exact natural two-step finite-population theorem proves that the sign may be opposite even with strictly monotone secondary susceptibility at every individual exposure. It supplies the full admissible recovery threshold for *every* finite hypergraph, including active overlapping triangles, not an isolated ad hoc numerical counterexample. The pairwise specialization yields a degree-only closed form, and the hypergraph example proves the effect persists when genuinely higher-order channels contribute. These conclusions identify a concrete limit on mechanistic inference from co-carriage, and a specific sensitivity to synchronous update convention, without claiming empirical validation.

## Closest work and limitations

- Liu and Schaposnik, arXiv:2610.26072v1: exact HyCo-SIS update rule; disease-free linearization, group-overlap representation, finite-time outbreak simulations; no inspected two-step covariance sign theorem.
- Hébert-Dufresne, Scarpino and Young, Nature Physics (2020): macroscopic interacting-contagion equivalences rather than the finite-state local covariance threshold.
- Brian, Ecosphere (2025): different asymmetric infection-priority model and prevalence comparisons.
- A previously accessible mathematical result about the same model family addresses the **single-pathogen deterministic mean-hazard closure**, not the two-pathogen stochastic joint distribution. Another concerns a distinct aerosol/environmental SIS ODE.

The conclusion is restricted to the source at time two, independent pathogen-specific event streams, the single doubly infected initial seed, and positive pairwise transmission. The initial population law, update order and transmission channels matter; neither clinical relevance nor independent replication is asserted.

Self-review: passed. Independent audit: not yet performed.
