# Scientific review

## Correctness — PASS

The claim is derived from the exact two-state transfer matrix for nearest-neighbor exclusion on a cycle. The occupancy-projector formula reconstructs all first-, second- and third-order moments, yielding a rational expression whose numerator is explicitly factored. The sign of the factored expression is determined by a single polynomial; endpoint derivatives establish signs at small and large fugacity, while direct evaluation at the special activity establishes the parity law. Uniform convergence with derivatives on a fixed neighborhood of the midpoint gives local existence, uniqueness for sufficiently large systems, and a quantified asymptotic. The independent enumerator and exact-rational checker passed 64 comparisons; computations are supporting checks, not an infinite-size proof.

## Originality — PASS on examined evidence

Scott and Sokal, arXiv:cond-mat/0309352, Section 3.2, contain the classical exact cycle partition function used as an input. It does not state the sign reversal of the specified three-point connected cumulant, the exact parity test at activity two, or the exponential alternating displacement. The full accessible Tokar–Dreyssé preprint concerns canonical cluster-length statistics rather than the stated finite grand-canonical three-point response. The 1986 Tanaka–Morita–Hiroike correlation paper was relevant by title and abstract, but only its accessible abstract and metadata could be checked; this is a residual risk rather than evidence of negative coverage. Earlier results on cycle two-point monomer correlations and precision operators do not imply the third connected moment because their input does not determine a three-point joint probability. Unindexed equivalent finite-ring cumulant calculations remain possible; absence from search is not a novelty proof.

## Mathematical value — PASS

This theorem identifies an infinite, natural family of finite periodic hard-core gases where a connected three-body response necessarily reverses sign. More than a worked transfer-matrix example, it establishes an exact odd-even diagnostic at a shared positive fugacity and resolves the parity-alternating exponential finite-size drift of a distinguished zero. That quantitative law separates a global ring effect from the usual infinite-chain decay of correlations. The observable and evenly distributed sites are natural probes of nonlocal collective response. The result claims neither an infinite-volume singularity nor global uniqueness of finite-size roots.

## Closest literature and limitations

Primary comparison: Scott–Sokal, arXiv:cond-mat/0309352 (cycle partition identities), Tokar–Dreyssé, arXiv:cond-mat/0210582 (different canonical cluster problem), Tanaka–Morita–Hiroike, DOI 10.1143/PTPS.87.214 (two-point direct/total correlations; full article not inspected). Remaining risks include unindexed exact computations, global zero counts outside the fixed neighborhood, and extension to nonuniform activities.

Self-review: passed. Independent audit: not yet performed.
