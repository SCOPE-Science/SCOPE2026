# Scientific review: even-cycle dynamical information volume

## Correctness — PASS
The result is a precise full-state theorem for even cycles and exactly two sensors. Fourier eigenmodes split into two singleton modes and repeated \(\pm k\) modes. The determinant is an alternating sum of two products of size-\(M\) Vandermonde determinants, multiplied by the singleton sensor separation and each repeated-eigenmode sine factor. The trigonometric product and the elementary adjacent-sensor walk triangulation prove all claimed exact formulas, their boundary cases, and unimodularity. The dependency-free exact checker independently reproduces 185 integer determinant calculations. No finite enumeration is represented as a proof for all \(M\).

## Originality — PASS relative to inspected evidence
The two-node coprimality *observability condition* is already known from Parlangeli--Notarstefano (2011) and is not presented as novel. The claim instead supplies a universal closed determinant for the **minimal square time horizon**, exact equality across all admissible sensor offsets for every injective spectral filter, and the adjacency \(\pm1\) determinant. The fully inspected two-sensor cycle low-pass frame result concerns spectrally demixed measurements and condition numbers, while the fully inspected normalized-path result concerns one-sensor trajectories. The closest September 2026 graph-Paley--Wiener paper could be inspected at the abstract level only; complete text could not be reached. That is a meaningful unresolved originality risk, not evidence of novelty by failed search.

## Value — PASS
Exact minimal-time D-optimal placement is a natural sampling-design invariant, and the invariance under every injective spectral evolution is structurally informative. Unit integer determinant for adjacency dynamics gives stronger reconstruction arithmetic than ordinary real injectivity. The theorem does not claim best lower singular value, noisy recovery or optimality for unequal weights.

## Closest literature and limitations
Relevant comparisons: Parlangeli--Notarstefano (arXiv:1109.3556); Bulai et al. (arXiv:2609.25472v1, abstract only); *Sharp spectral-demixed two-sensor frame bounds on finite cycles* (published RESULT.md); and *Universal endpoint optimality for dynamical sampling on normalized paths* (published RESULT.md). Detailed claim-to-implication checks and residual risks are in AUDIT.json. No independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
