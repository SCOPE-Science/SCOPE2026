# Self-review

## Correctness — PASS

The claim is a finite, exact all-split statement. The proof conditions on the first pivot, counts every ordered permutation with a binomial interleaving factor, verifies total mass \(n!\) and conditional mass \((n-1)!\), and calculates all cumulative gaps at every possible integer cost through eight keys. Every applicable adjacent move toward balance has a nonnegative gap; this proves the universal small-size half. The exact nine-key crossing has CDF values \(1/9<1/4\) at 16 and \(19/45>5/12\) at 17, with the means separately verified. The program implements both an exhaustive recurrence and a distinct BST insertion enumeration of all 80,640 relevant nine-key permutations. Neither routine assumes a stochastic comparison beyond the certified range.

## Originality — PASS, with specified residual risk

The full text of Fill and Janson's 2001 arXiv preprint gives the distributional recurrence and limiting-law analysis; the full arXiv text of Iliopoulos and Penman (2010) studies exact comparison moments, not conditional first-pivot CDF ordering. Dennert and Grübel's accessible full 2010 paper analyzes subtree-size profiles, with a different response variable. A published result about covariance of root imbalance with binary-search-tree path length is weaker than the claimed stochastic ordering; the counterexample demonstrates this distinction. Searches for root-rank-conditioned stochastic dominance and CDF crossings did not yield an explicit nine-key minimality theorem. Generic coefficient recurrences make the certificate computable in principle, so a previously unpublished or unlocated exact evaluation remains a real priority risk; search absence alone is not treated as a proof of novelty.

## Value — PASS

Moving pivot choice toward balance is a natural algorithm-design question. First-order stochastic order would control **all** increasing loss functions or tail-probability criteria, whereas mean comparisons control only one aggregate. The exact first counterexample at nine keys establishes a sharp limit on this tempting generalization and has a visibly small sign-reversal margin \(1/180\), making a rigorous exact certificate mathematically worthwhile rather than a random isolated sample.

## Closest literature and limitations

Primary references: Fill–Janson, arXiv:math/0105246; Iliopoulos–Penman, arXiv:1006.4063; Dennert–Grübel, DOI 10.1017/S0963548309990630. The claim does not assert anything about comparison-cost tails for all sizes beyond nine or more realistic partitioning overheads. This review verifies only the new claim; it does not independently establish priority or perform an external audit.

Self-review: passed. Independent audit: not yet performed.
