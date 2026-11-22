# Scientific review

## Correctness — PASS

The finite-window decomposition in `RESULT.md` is an exact algebraic identity for all odd cycle sizes. Every coefficient is strictly positive by the explicit geometric Green function, every window has a sharp parity-dependent lower bound, and the minimum-gap witness achieves equality at every required term. The separate exact-rational verifier tested all binary partitions through thirteen vertices at three screening strengths, but the proof does not rely on finite enumeration. Risks: the conclusion assumes precisely the stated independent two-class probing estimator and positive screening.

## Originality — PASS, qualified

The 2020 Kerimov long-range convex Ising analysis and earlier Hubbard-style ordering results materially cover the broad idea that evenly spaced/alternating ground states minimize convex repulsive interactions. That broad fact is expressly NOT the contribution. The new theorem computes the exact first excited variance above the ground state over *all* nonoptimal binary partitions, proves strict positivity for each odd order and each screening parameter, and supplies an explicit attaining pair of flips. The closest published screened-cycle trace-probing comparison concerns **even** cycles; no inspected source states or implies the quantitative odd-cycle next-best gap. An undiscovered finite-size Ising excitation theorem could cover the new claim; independent publication-priority review is needed. The online even-cycle record was available as a search summary and was not read in full.

## Value — PASS

On odd periodic meshes a proper two-coloring is impossible; a sharp second-best penalty measures the exact cost of the next nearest feasible design, which cannot be inferred merely from ground-state uniqueness. The exact gap depends on screening and curvature of squared Green weights, yielding concrete robustness information for a standard two-solve trace-estimation family. The scope is deliberately narrow, not a claim about every trace estimator or arbitrarily correlated probes.

## Boundaries and primary comparisons

Kerimov (2020), DOI 10.1063/5.0001423, covers general antiferromagnetic ground-state structures and was examined in text. Switzer et al. (2021), arXiv:2106.01275, develops stochastic probing and lattice coloring but not this odd-cycle sharp first gap. The 2026 screened-cycle checkerboard result covers even cycles, while complete-bipartite probing has different geometry. Exact-source originality must still be independently assessed, including literature not fully retrievable in this review.

Self-review: passed. Independent audit: not yet performed.
