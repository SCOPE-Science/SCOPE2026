# Scientific review

## Correctness — PASS

A greedy complete arch is the shortest prefix containing both symbols; its last letter first occurs at that endpoint. The missing-symbol construction shows that the number of complete arches equals the scattered-subsequence universality index. Exactly \(k\) letters \(b\) and exactly \(k\) complete arches force each arch to contain precisely one \(b\), so the unique shapes are \(ba\) and \(a^{u+1}b\), with an \(a\)-only suffix. The scattered \(ab\) statistic is \(\binom{k}{2}+\sum_i\epsilon_i(1+(k-i+1)u_i)\). Independent geometric-series sums in the excess-letter variable give the claimed coefficient product, valid as a formal identity for every \(k\ge4,r\ge0\). Reversal, letter-swap plus reversal, and direct low-degree product expansion prove the remaining claims. The standalone checker directly enumerated 6,441 binary words across 25 finite parameter pairs and matched every coefficient. This finite testing does not replace the arbitrary-parameter proof.

## Originality — PASS with residual risk

The nearest 2026 study, Fazekas–Huang–Mercaş, gives \(\exists\)- and \(\forall\)-universality criteria for binary Parikh classes and an approximation scheme for a fixed pattern's containment probability, not this uniform exact \(k,r,C\) census of maximally universal representatives. Adamson's exact counting and ranking algorithms work at fixed total word length but do not state the joint letter and scattered-pair distribution. Richomme describes equivalence classes via partitions, and the q-Parikh-matrix deformation concerns q-weighting of subsequence embeddings inside one word. Published database and literature comparisons did not reveal this precise coefficient product; exhaustive global novelty or an unindexed identity cannot be guaranteed. The existing classical arch characterization is explicitly treated as a premise, not new.

## Value — PASS

The 2026 work poses exact/probabilistic questions on universality *inside* fixed binary Parikh-matrix languages. For every saturated multiplicity class, the theorem gives the full exact distribution over the defining third Parikh coordinate, including all empty/nonempty counts and boundary strata, rather than only existence. It has a short constructive factorization, reciprocal symmetry, and coefficient formulas uniformly for unbounded \(k,r\). It identifies a structurally natural tractable regime of a more general joint distribution. This is stronger than recomputing a known aggregate count or an arbitrary small numerical case.

## Closest literature and limitations

Primary comparisons: Fazekas, Huang, Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices* (arXiv:2610.06717, 2026-10-05), Sections 2–5; Duncan Adamson, *Ranking and Unranking k-Subsequence Universal Words* (arXiv:2304.04583, 2023), counting/ranking results; Gwenaël Richomme, *On some 2-binomial coefficients of binary words* (arXiv:2510.07159, 2025), partition models; Renard, Rigo, Whiteland, *q-Parikh Matrices and q-deformed binomial coefficients of words* (arXiv:2402.05657, 2024), q-deformation. There is a residual possibility of equivalent older partition enumeration not indexed under subsequence universality. General unsaturated binary contents are not claimed. No independent external validation was performed.

Self-review: passed. Independent audit: not yet performed.
