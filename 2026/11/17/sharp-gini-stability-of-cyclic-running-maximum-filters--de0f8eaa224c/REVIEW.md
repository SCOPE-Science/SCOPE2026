# Self-review

## Correctness — PASS

The exact domain is arbitrary real \(n\)-tuples with \(n\ge2\), cyclic windows \(1\le w\le n\), and unweighted Gini seminorm over all unordered pairs. Every local affine selection branch is covered. The cut-level formula is exact, not merely an estimate; for short windows the occupancy cap proves the quantitative upper bound, and for long windows the unique global peak supplies the stronger exclusion of middle cut sizes. The single-peak perturbation realizes the sharp ratio for each \((n,w)\). The quotient-by-constants and full-window zero case are handled explicitly. The finite exact checker corroborates but does not replace this proof.

## Originality — PASS, with historical risk

Inspected the 1987 primary max/min order-statistic paper, the accessible 2014 arXiv graph-morphology reader and the public primary RESULT.md on finite-path sliding extrema. The latter is an exact **adjacent-edge path** variation theorem with truncated endpoints; it is not a Gini all-pairs theorem on cycles. A previously accessible cyclic-max result computes centered-\(L^2\) rather than Gini stability. The claimed coefficient is not a corollary of generic norm comparisons. Searches for direct formulas and alternative aliases returned no equivalent. Unindexed prior art and incompletely inspected older literature remain risks, so independent priority validation is needed before any publication claim.

## Mathematical value — PASS

A running maximum can preserve order and obey strong one-input variation statements while amplifying the *difference of two signals* in a natural pairwise-dispersion geometry. The exact factor \(w(n-w)/(n-1)\) resolves the all-size/all-window stability problem, including a sharp four-site onset, two nontrivial nonexpansive widths and linear-in-\(n\) optimal amplification. The new occupancy-cut lemma and global-winner argument provide structural understanding and reusable methods for coordinate-selection filters.

## Sources, proof limits, and verification

Scientific evidence: Maragos–Schafer (1987), DOI 10.1109/TASSP.1987.1165254; Najman–Cousty (2014), arXiv:1404.7748; the fully read public adjacent-path-variation RESULT.md at https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-finite-window-morphology-sharp-two-input-variation-and-a-boundar--5f5f2cb7d7b2. Exact finite script `verify.py` exhausts strict selector chambers through eight sites, then tests integer occupancy inequalities and exact-rational pairs/witnesses in larger finite ranges. The unrestricted theorem is proved in `RESULT.md`, not inferred from testing. Only the uniform cyclic scalar case is claimed; neither the literature search nor the review constitutes independent audit.

Self-review: passed. Independent audit: not yet performed.
