# Self-review

## Correctness — PASS

The claim concerns the multiplicative nucleon, not the additive nucleolus, for all ordinary unit-weight path matching games with at least three vertices. In the even case, the first-stage core is parameterized by ordered pair variables; \(m+1\) nonnegative gaps sum to one. The explicit coalitions for those gaps have value \(m-1\), proving a universal second-stage ratio upper bound of \(1+1/(m^2-1)\) with equality only at uniform gaps. The proposed arithmetic payoffs attain that bound for all proper positive-worth coalitions outside fixed base-pair unions: any positive excess is a multiple of \(1/(m+1)\), and every proper coalition has worth at most \(m-1\). This uniquely fixes the second lexicographic stage. On odd paths, a maximum matching can omit any odd vertex, forcing its payoff to zero in every core allocation, hence a unique core and nucleon. The finite checker (standalone `verify.py`) independently computes induced-matching worth and tests \(124293\) positive-coalition inequalities through \(16\) vertices, together with \(633\) exact-grid comparisons. All tests passed. The all-order conclusion comes from the proof, not from enumeration.

## Originality — PASS (qualified)

The October 2026 work of Aziz and Csáji (arXiv:2610.29731v1, Sections 2–4) computes the nucleon for *every* weighted ordinary matching game and includes a weighted four-vertex path example. This covers algorithmic computation of instances, but its inspected general stage algorithm and example do not state or derive the new explicit all-order unit-path parity formula or its exact second-level value. The 1998 paper of Faigle, Kern, Fekete and Hochstättler establishes nucleon foundations and a matching-game algorithm, but not the inspected unit-path formula. The accessible research index and record-specific searches found no equivalent named theorem; a separate one-edge-augmented complete-bipartite matching-game nucleon result is not logically dominating for paths. Residual risk: unindexed path specializations and proofs implicit in older general algorithms may exist; no claim of publication-priority certification is made.

## Value — PASS

An exact closed-form classification for every path order, including the odd/even discontinuity, is a natural structural question for the simplest connected matching market. The explicit second lexicographic ratio identifies the binding coalitions and certifies uniqueness within a nontrivial first-stage core, replacing general optimization with a direct formula and yielding a sharp all-order fairness certificate. This is stronger as a structural statement than an arbitrary small-case table and does not purport to improve the known general computational complexity.

## Closest literature and limitations

- Haris Aziz and Gergely Csáji, *Computing the Nucleon of Matching Games*, arXiv:2610.29731v1, first posted 2026-10-21; general polynomial-time combinatorial algorithm, full nucleon description and a **weighted** four-vertex path example. https://arxiv.org/abs/2610.29731
- U. Faigle, W. Kern, S. P. Fekete and W. Hochstättler, *The Nucleon of Cooperative Games and an Algorithm for Matching Games*, Mathematical Programming 83 (1998), 195–211; earlier general matching-game algorithm. https://www.ibr.cs.tu-bs.de/users/fekete/hp/publications/PDF/1998-The_Nucleon_of_Cooperative_Games_and_an_Algorithm_for_Matching_Games.pdf

Only ordinary unit paths with unit edge weights are classified. The literature check does not prove uniqueness against unindexed work; the checks do not constitute independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
