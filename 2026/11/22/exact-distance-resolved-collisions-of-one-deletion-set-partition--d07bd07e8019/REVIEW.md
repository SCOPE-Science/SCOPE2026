# Scientific review

## Correctness
PASS. Equality of the induced deletion partitions is translated to equivalence-relation comparisons inside and outside the deletion interval. The shift invariance forces a periodic list of distinct block identities, while exterior comparisons force isolation for nonconstant periods. Contracting a constant interval and partitioning the complement of an isolated-periodic interval give the exact Stirling and Bell counts. The package verifier independently checks every set partition and deletion-position pair up to length nine and 11,800 additional larger random cases. The stated probability bounds follow from counting exceptional pairs; the asymptotic estimate uses a standard Bell-number ratio bound.

## Originality
PASS (qualified). Sagan (2006, arXiv:math/0604292) and Bloom–Saracino (2015, arXiv:1511.00192) develop standardization and avoidance on set partitions but not the equivalence of two specified one-deletion readouts, the isolated-periodic classification, or distance-refined Bell/Stirling counts. The unrestricted labeled-word single-deletion run rule cannot imply the isolated-block phenomenon without accounting for relabeling. Equivalent unindexed work remains possible. The literature searches do not constitute proof of priority.

## Mathematical value
PASS. A source under an unlabeled-alphabet deletion channel has intrinsically different duplicate-read behavior from the usual labeled-word channel. The all-length collision classification is the structural tool needed to count duplicate reads at any separation and prescribed block richness; the high-probability theorem identifies precisely when the simpler local-run approximation becomes reliable. These are exact reconstruction invariants, not a mere finite sequence or a reparameterization of ordinary runs.

## Limits and closest literature
These are same-source duplicate deletions, not collisions between distinct sources, and no optimum code sizes are claimed. The adjacent-run approximation is asymptotic, with an explicit finite-length upper bound. The closest inspected sources are Sagan (2006) and Bloom–Saracino (2015), covering partition-pattern enumeration rather than read-identity multiplicities. A comprehensive priority review beyond the accessed sources remains desirable.

Self-review: passed. Independent audit: not yet performed.
