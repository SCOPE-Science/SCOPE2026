# Scientific review: fixed-weight Zeckendorf residue counts

## Correctness — PASS
The proof is a finite-event inclusion–exclusion argument with an exact full-period product law. Equality of two chosen index positions and adjacency of two positions are the only first-order forbidden events; their intersections have codimension at least two. The Fibonacci identity \(F_j+F_{j+1}=F_{j+2}\) gives the adjacent-pair term. Independent exact rational cycle calculations and exact integer counts corroborate the first two coefficients. The infinity statement rests on the proof, not on numerical runs.

## Originality — PASS (historical-priority risk retained)
The June 2026 Zeckendorf–Niven progression study (Lao et al., arXiv:2606.24006v1, June 22 first posting) proves infinitude in arithmetic progressions and bounds on runs, not the two-term law for fixed-weight subsequences. Wagner's earlier general residue theorem (Ramanujan J., 2007, Theorem 12) provides a discrepancy bound depending on the fixed digit weight and does not imply explicit nonuniform Pisano probabilities or the second-order adjacency term. Full source inspection covered the key published theorems. Exact-equivalence or broader-transfer-matrix priority remains possible; the original Ray–Cooper text was not available in full. Lack of a search hit is not proof of uniqueness.

## Mathematical value — PASS
The conditional distribution of Zeckendorf–Niven integers within the mathematically natural fixed-number-of-summands slices quantifies a gap in recent arithmetic-progression results. The full finite-period formula works for every fixed modulus and weight; the second coefficient isolates the first dependency caused by Zeckendorf adjacency, rather than merely repeating a straightforward leading count. The nonuniform \(5/9\), \(85/256\), and \(7/27\) proportions demonstrate that the fixed-weight model is not simply uniform over residue classes.

## Scientific limitations
The expansion is nonuniform as the weight or modulus grows. For unaligned cutoffs the first-order limit holds, but the second coefficient can have boundary oscillations. Positive conditional density does not imply positive natural density among all integers. The exact constants and their checked values are finite-cycle calculations; independent historical-priority and mathematical audit have not been performed.

## Closest literature
- Lao et al., *On Zeckendorf-Niven numbers and arithmetic progressions*, arXiv:2606.24006v1 (June 22, 2026).
- S. G. Wagner, *Numbers with fixed sum of digits in linear recurrent number systems*, Ramanujan J. 14 (2007), 43–68, DOI:10.1007/s11139-006-0001-6, especially Theorem 12.
- M. Drmota and W. Steiner, *The Zeckendorf expansion of polynomial sequences*, J. Théor. Nombres Bordeaux 14 (2002), 439–475.

Self-review: passed. Independent audit: not yet performed.
