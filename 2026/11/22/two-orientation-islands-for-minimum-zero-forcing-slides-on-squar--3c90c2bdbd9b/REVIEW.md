# Scientific review

## Correctness — PASS

The white-cell auxiliary graph is the bipartite incidence graph of rows and columns. A blue rook cell can force precisely when its two endpoints have white degrees zero and one. White cycles are unbreakable, and an isolate is necessary for any first force. Thus an optimal support with \(2n-2\) white cells is exactly one isolated bipartite vertex plus a spanning tree on the remaining \(2n-1\) vertices; a leaf on the opposite side initiates a complete peel. The proof exhibits concrete valid slides from every such tree to a fixed double star, a one-slide transfer of the missing row for \(n\ge3\), and a one-jump bridge between the two orientations. When a putative slide touches the missing row, the shared column cannot become isolated, so no orientation-crossing slide exists. The exception at \(n=2\) is separately checked. A direct forcing-rule checker and an independently implemented tree-pivot checker agree at \(n=2,3,4\), including all minimum configurations and moves; finite computation supports rather than replaces the proof.

## Originality — PASS with residual risk

The precise slide-component theorem is distinguished from the previously known zero-forcing cardinality, complete zero-forcing polynomial and extremal spanning-tree count. The antecedent 2026-10-12 note *Zero-forcing polynomials of rook graphs via bipartite forests* explicitly determines the feasible subsets and counts, but does not state slide/jump connectivity or give the shared-endpoint pivot construction. Benson et al. (arXiv:1510.02421) discuss product zero forcing, and Geneson–Haas–Hogben (arXiv:2009.00220) introduce reconfiguration results, without this exact theorem in the relevant inspected material. Searches of graph-product, rook-graph, Hamming-graph, bipartite-tree and token-slide formulations revealed no mathematical implication covering the new two-component result. Unindexed or inaccessible pivot/reconfiguration literature remains a live priority risk, and the new result is a constructive structural refinement of prior feasible-set classification rather than an independent enumerator.

## Value — PASS

Individual feasibility and counts do not determine whether optimal solutions can move while preserving feasibility. On this natural infinite family, the same optimum family is split by **all** legal local token slides into two topologically distinct orientation classes, although one unrestricted one-token jump bridges them. The new proof translates sensor mobility to a nontrivial constrained edge-pivot connectivity theorem for labeled bipartite spanning trees and gives the sharp \(n=2\) boundary. It is a general structural difference between local and global reconfiguration, not a restatement of a scalar invariant or an arbitrary finite census.

## Scope and remaining uncertainty

The theorem is not about larger forcing sets, rectangular non-square boards, skew forcing, or precise all-size slide diameters. The antecedent forest characterization and counts are credited explicitly, and equivalent non-indexed mathematical terminology could diminish originality. The two standalone source programs and verification output are included for reproducibility; no third-party independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
