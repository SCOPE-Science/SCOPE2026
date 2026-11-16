# Scientific review: Sharp dyadic Fourier gaps for complete rooted arborescences

## Correctness — PASS
The complete mathematical proof is in `RESULT.md`: signed matrix-tree expansion, parity and dyadic row-divisibility, two independently constructive sharpness arguments and exact even-order vanishing stars. The recursive skew-matrix Schur complement has a unit determinant and preserves the ±1 row-sum condition. The circulant resultant is exact because multiplication by the half-length permutes the nontrivial roots. Direct Prüfer-word signed sums and independent determinant evaluations agree on all reduced frequencies at orders three through five; the full order-six reduced census and higher-order extremizer checks provide further finite corroboration, not infinite proof.

## Originality — PASS under bounded comparison
Biane–Chapuy (arXiv:1505.04806) and De Leenheer (arXiv:1904.12221) cover the general weighted matrix-tree identity; their determinant representation is explicitly acknowledged prior art. Zeng–You (arXiv:2408.06992) discuss already-known unit determinants of even-order tournament matrices; this is also not claimed new. Closest published result on shattered arborescence arc supports (record 797c621a44d8) concerns VC shattering, while complete bipartite spanning-tree Walsh spectra (record 89f45551846c) concern a different undirected incidence space. No covering all-dimensional least-nonzero Fourier level or parity invertibility statement was identified in checked material. An unindexed or differently named theorem remains a historical-priority risk; a negative search is not an originality proof.

## Mathematical value — PASS
A natural inverse-problem invariant is determined *exactly for every graph order*: the smallest recoverable Walsh multiplier and therefore the sharp \(\ell^2\) reconstruction amplification. The parity transition in invertibility is accompanied by explicit cancellation witnesses and sharp sign patterns of two different algebraic types. These conclusions are not a routine small-instance census.

## Scientific limitations
Only complete rooted directed-graph arborescences with Boolean arc incidence are covered. No full general-order multiplier distribution or nullity is claimed, and no independent external mathematical audit has been performed. Verification software is finite-case reproducibility support.

Self-review: passed. Independent audit: not yet performed.
