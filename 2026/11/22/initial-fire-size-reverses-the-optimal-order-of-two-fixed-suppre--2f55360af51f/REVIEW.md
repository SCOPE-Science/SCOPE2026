# Scientific review: initial-size suppression-order reversal

## Correctness — PASS
The state space, absorbing boundary, natural death rates, suppression convention, row-vector orientation, common final horizon, and initial mixtures are explicitly specified. Cayley–Hamilton gives the exact two-eigenvalue semigroup decomposition, and positivity of the split eigenvalue coefficient is established from the strictly positive discriminant. Direct multiplication gives the nonstandard commutator identity; multiplying by the survival vector proves the exact extinction-difference formula with a strictly positive prefactor. The sign classification includes the cases \(d>m\), \(d=m\), and \(d<m\), as well as equality at the sharp initial-mixture threshold. A scalar one-active-state model proves minimality. The companion checker reproduced 7,208 diagnostic assertions; the all-parameter result follows from the proof, not finite testing.

## Originality — PASS, with provisional historical priority
The 2023 first-public Hulsey–Alderson–Carlson paper provides the underlying additive-suppression birth–death model and primarily constant-intensity population and footprint results. The 2025 follow-up studies multistage control, resource allocations, finite-time remaining activity and footprint numerically, but the inspected sections and equations do not give this particular two-state all-duration high/low ordering identity with the initial-state sign change. Ross–Pollett (2006) treats *population-triggered* phase switching instead of exchanging predetermined time intervals. Generic two-by-two matrix exponential and commutator algebra are standard and are not claimed new. The specific complete initial-mixture threshold and minimal-capacity interpretation were not found in the material examined. This is a best-knowledge statement, not a proof of literature uniqueness. Earlier general phase-dependent birth–death literature may contain implied cases; the material available for one older potentially relevant article was abstract-level only.

## Value — PASS
The statement gives a complete, exact and minimal counterexample to an unqualified 'stronger suppression earlier always improves short-term extinction' heuristic: with natural per-unit mortality and fixed total episode exposure, one active unit always favors strong-first and two active units always favors strong-last. A single closed-form initial-state threshold classifies every mixture *uniformly over all positive durations and intervention strengths*. This is a motivated mathematical boundary in temporal risk assessment rather than an arbitrary numerical slice. The conclusion pertains to extinction probability only; minimizing footprint, protecting life, optimal real-fire deployment, and unbounded-state models remain outside scope.

## Closest literature and outstanding risks
- Hulsey, Alderson, Carlson (2023), https://arxiv.org/abs/2307.11726: source model, including the fixed absolute suppression term.
- Hulsey, Alderson, Carlson (2025), https://doi.org/10.1103/PhysRevE.111.024318: closest temporal-allocation work and finite-time risk context; no exact classification found in inspected relevant full-text portions.
- Ross and Pollett (2006), https://doi.org/10.1016/j.mbs.2006.02.004: two-phase birth–death process, but the phase is triggered by state thresholds.
- Historical priority risk: phase-dependent population models and general positive-matrix rearrangement principles might imply this finite-state identity indirectly; expert exhaustive literature audit has not occurred.
- Scientific scope risk: a two-active-site ceiling and equal-additive removal are idealizations; nothing here supports delayed fire response in practice.

Self-review: passed. Independent audit: not yet performed.
