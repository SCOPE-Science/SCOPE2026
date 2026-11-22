# Self-review

## Correctness: PASS

The exact formula follows from two distinct backward constructions: complete-reset renewal with the gate stationary law, and a coupled three-state Poisson-reset boundary-value equation. The three spectral roots and boundary normalizations have been worked through explicitly, with positive reset and gate rates throughout. The sign classification follows from an exact nonzero cosine amplitude and strict phase bounds, not finite enumeration. Independent matrix and spatial finite-difference implementations reproduce the formulas; these computations are corroborative rather than an infinite proof.

## Originality: PASS (qualified)

Bressloff (2020) treats a two-state absorbing/reflecting gate with joint position/gate resetting. Mercado-Vásquez and Boyer (2021), Appendix B equation (49), explicitly compare it with position-only resetting and prove a strict same-direction ordering. The three-conformation irreversible gate instead produces infinitely many strict distance-order reversals for every positive rate triple. Scher and collaborators (2022/2024) develop a broader gated-first-passage framework without the directed three-state resetting comparison. Bressloff (2026) provides a broader gated-renewal framework but its half-line resetting calculation remains two-state; no claim of novelty is made for the underlying renewal or matrix methods. A complete priority search across all unindexed literature was not possible, and general formulas could implicitly cover this special case.

## Mathematical value: PASS

The closed-form reversal lattice gives a global classification of a natural choice—whether to refresh an independently switching target at the same time as a Brownian searcher—where the familiar two-state result fails to generalize. The exact spacing and damping expose the role of nonreal relaxation modes in a minimal irreversible gate and provide explicit benchmarks for controlled gated-search protocols. It is a qualitative full-parameter theorem, not a selected numerical coincidence.

## Limitations and literature

Only one fully cyclic three-conformation gate with one perfectly absorbing state is treated. The theorem does not imply universal three-state classification, distribution-level stochastic ordering, or practical observability of every remote crossing. Closest references: Bressloff (2020), arXiv:2009.02739; Mercado-Vásquez and Boyer (2021), arXiv:2107.02148, especially Appendix B; Scher et al. (2022/2024), arXiv:2211.09164; Bressloff (2026), arXiv:2601.01588, sections 2–3. An independent scientific review and more exhaustive publication-priority assessment remain outstanding.

Self-review: passed. Independent audit: not yet performed.
