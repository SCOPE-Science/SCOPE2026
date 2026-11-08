# Scientific review

## Correctness — PASS
A direct local-twin argument forces at least \(r-1\) selected clique vertices per attachment. For any initial forcing set \(S\), the projection \(B(S)\) is a genuine zero-forcing set of the base graph: an initially unactivated root has one white attached twin, and the twin cannot be colored before the root. This establishes the lower bound. Every prescribed choice for a base minimum forcing set yields a valid chronological forcing process, proving equality and a unique classification. Local subset adjacency proves connected Cartesian-product fibers; direct counting of their crossings along each base exchange edge proves component transfer and the edge formula. Standalone independent bitmask and set-based implementations passed the finite checks listed in the output logs. Exact general proof, not finite enumeration, establishes the unbounded claim.

## Originality — PASS with limitations
The relevant historical formula for the minimum zero-forcing *cardinality* of a corona is already given by Javaid et al. (arXiv:1607.04071, Section 2). The first posted date is 2016-07-14. The claim does not relabel this old formula as new. The inspected full relevant corona section provides no exact multiplicity of all minimum bases or component lifting. Geneson–Haas–Hogben (arXiv:2009.00220, relevant Sections 2–6) establish reconfiguration conventions and results including the disjoint-union Cartesian product, but no equivalent clique-corona component lift was found in the inspected text. Indexed research-record searches for clique-corona zero-forcing bases, reconfiguration, aliases, and connectedness found related graph families but no dominating equivalent statement. Searches do not prove absence of unindexed historical results. No independent priority certification is claimed.

## Value — PASS
The exact zero-forcing number alone does not specify how many optimal initial placements exist or whether one can exchange individual selected vertices to move between optima. The classification answers both for a broad corona operation on arbitrary connected base graphs. It proves component connectedness is preserved and gives the size of every reconfiguration component and the exact number of transitions from base invariants. The component-preservation phenomenon is a structurally useful transfer rule, not a numerical recomputation of the known minimum.

## Limitations and comparison risks
Only classical zero forcing, attached complete cliques of size at least two, and unrestricted one-token replacement are covered. The later reconfiguration literature and unindexed results could contain an equivalent theorem; searches cannot establish global priority. Finite code checks exhaust small graphs but are not used in place of the symbolic proof. The two principal papers are the comparison sources cited in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
