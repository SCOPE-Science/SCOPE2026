# Self-review

## Correctness — PASS
The pathwise two-colour decomposition is exact: membership is a two-colour Pólya urn started from one vertex per group, and internal parent choices remain uniform and independent conditional on the complete membership history. The induced complement root contributes a spurious size-\(k\) fringe count only when its induced size is \(k\). The expectation \(\mu_k(m)\) follows from explicitly stated leaf and general fringe-subtree recurrences and correct initial conditions. Uniformity of \(S\) and symmetry of the conditional mean leave precisely one boundary term. The result is valid for every \(n\ge2\) and \(1\le k<n\). The standalone exact verifier passed 14,728 assertions over exhaustive trees through nine vertices and independent recurrences through size 120.

## Originality — PASS (with historical-priority risk)
The nearest primary work is Feng–Mahmoud–Panholzer (2008) on global fringe-size counts, Holmgren–Janson (2014 preprint) on global fringe-count laws and covariances, and Seelbach Benkner–Wagner (2022) on global fringe-tree profiles. Holmgren–Janson's Theorems 1.4 and 1.15 supply, respectively, the mean needed here and covariance formulas for pairs of *global* count statistics. Neither is a covariance between the size of the individual birth-label-2 subtree and a global count. The new conditional boundary-correction identity isolates a different statistic, which cannot be recovered from an aggregate covariance without new vertex-specific information. Relevant published mathematical findings on root degrees, total leaves and path lengths likewise do not imply the claimed all-size profile. The full text of the 2008 paper was not fully available; a hidden historical specialization remains a genuine risk.

## Mathematical value — PASS
The theorem is a natural complete classification for the dependence of an early branch's mass on the fringe-size profile, both fundamental random-tree observables. It exhibits a sharp, parameter-free sign switch at \(n=2k\), including exact cancellation at equality, and derives the switch from a structural root-deletion principle rather than from a high-order moment computation. This can inform joint descriptions of early branch masses and global local-subtree statistics. The result is neither just a marginal-mean recomputation nor a trivial renaming of global-global covariance formulas.

## Limits and closest literature
The claim concerns uniform recursive trees and the second arrival only. It does not establish independence at zero covariance, the entire joint law, or later-label analogues. The 2014 and 2022 relevant primary text was materially inspected, while only partial text and secondary characterizations of the 2008 paper were available.

Self-review: passed. Independent audit: not yet performed.
