# Self-review

## Correctness: PASS

The exact statement concerns ordinary unrooted 1-WL distinguishing **nonisomorphic graphs**, not recovery of vertex-orbit partitions. Its domain is all simple biconnected outerplanar graphs of order 3 through 10. Biconnectivity and outerplanarity give a unique Hamiltonian cycle; every graph is therefore a cycle plus noncrossing chords. The complete chord inclusion/exclusion recursion, dihedral canonicalization, adjacency reconstruction and exact common 1-WL refinement all appear in standalone `verify.py`. Running it yields 1117 graph isomorphism types and precisely five two-member 1-WL classes at order ten, with none at orders 3--9. Each of the five pairs is independently confirmed by direct two-graph refinement. No sampling or hash-equivalence conjecture is used to complete the finite proof.

## Originality: PASS (historical priority qualified)

The direct motivating arXiv paper, Coste--Csikós--Viennot (2026, arXiv:2611.18391v1), already contains a ten-vertex nonisomorphic biconnected outerplanar 1-WL collision. The known example and rooted positive theorem are credited and are not claimed as new. The new sharp lower-order exhaustion and five-doublet boundary classification are not consequences of either. Bause--Jogl--Welke--Thiessen (2023) study a transformation to raise expressivity, and Bodirsky--Fusy--Kang--Vigerske (2007) enumerate ordinary outerplanar graph isomorphism types; neither gives the asserted untransformed 1-WL equivalence census in the inspected relevant content. A published note about the first order-eight failure to recover vertex **automorphism orbits** addresses a different claim, not equivalence between two nonisomorphic graphs. Searches for aliases, broader theorems and exact tables did not locate an equivalent census. The archived note's full text was inaccessible, leaving an explicitly recorded historical-priority risk.

## Value: PASS

The exact first collision threshold for a natural graph isomorphism heuristic is mathematically motivated by the recent positive rooted theorem and previously displayed unrooted obstructions. Completely classifying all sharp boundary pairs is a natural finite extremal classification, not a random small graph invariant. The theorem adds five canonical doublets and the sharp nine-vertex nonexistence statement, while acknowledging ordinary graph-type counts as prior knowledge. It does not require a new general structural theorem to be useful in this concrete classification.

## Closest literature and limits

Relevant full-text material examined: the direct primary 2026 arXiv preprint, including its unrooted Figure 1 and rooted theorem; opening sections of the 2023 open-access outerplanar GNN study; an earlier graph-refinement presentation's ambiguity figure; and indexed outerplanar enumeration. The related archived orbit-partition note was read only as a public title/abstract; it cannot be certified absent from its inaccessible full text, so historical priority is provisional. The conclusion is strictly finite for 3 through 10 vertices. Independent audit and separate external validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
