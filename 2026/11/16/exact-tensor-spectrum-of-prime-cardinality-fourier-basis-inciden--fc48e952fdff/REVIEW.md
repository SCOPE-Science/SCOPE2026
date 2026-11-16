# Self-review

## Correctness — PASS
The cyclotomic-field proof of the short vanishing-sum lemma is valid because the least prime \(p\) is smaller than every other prime divisor \(q\), forcing an absent \(q\)-residue. It yields complete \(p\)-gons, the modulo-\(p\) transversal criterion, the local either-side-constant compatibility law, and exact tensor eigenvalues. Both roots per local block are nonzero; consequently the overall rank is precisely \(2^{\omega(N)-1}\). CHECK.py independently matched 379086 exact cyclotomic comparisons plus 1200 samples and numerical full-matrix eigenvalues. The finite computations are supporting tests, not proof for arbitrary orders.

## Originality — PASS relative to inspected literature
Lam–Leung's vanishing-sum theory, Malikiosis's spectral Fourier-zero criterion, Kiss–Malikiosis–Somlai–Vizer's squarefree cyclic methods, and Tan–Zhang's 2026 classification are prior foundations. The assessed statement is the **complete signed spectrum of the global prime-cardinality Fourier-basis incidence matrix**, with a rank-two tensor per additional prime, as opposed to known existence, pair classification, or single-spectrum counts. The closest published-finding corpus IDs were 2026/11/8/SCOPE-valuation-threshold-law-for-prime-cardinality-fourier-spectra-on--01969b44e8ca and 2026/11/8/SCOPE-period-rigidity-and-exact-spectrum-multiplicities-for-cyclic-pri--89015b0ebdf6; their domains/results do not state this invariant. The full Tan–Zhang paper was not available, leaving a material residual originality risk; the abstract alone is not evidence that its full content excludes this result.

## Mathematical value — PASS
The all-spectral-pairs operator is natural in Fourier basis design: rank collapses from \((N/p)^p\) to \(2^{\omega(N)-1}\) while all signed eigenvalues and exact pair counts remain computable without constructing the large matrix. The general tensor law gives information beyond individual transversals and provides a complete spectral benchmark across infinitely many squarefree orders.

## Closest literature and limitations
The group order must be squarefree and the set size its least prime factor. The closed formula does not handle larger Fourier spectral sets or repeated primes. Relevant sources are Tan–Zhang (arXiv:2610.02218; full text inaccessible), Malikiosis (doi:10.1017/fms.2022.14; full HTML inspected), Kiss et al. (doi:10.1007/s00041-022-09972-0; full HTML inspected), and Lam–Leung (doi:10.1006/jabr.1999.8089; classical background).

Self-review: passed. Independent audit: not yet performed.
