# Self-review

**Correctness — PASS.** The exact distance mixture is derived by conditioning on unit edges; each distinct-edge term is a shifted triangular density. The density at zero determines total edge count, and induction over adjacent unit intervals recovers every distance-histogram coefficient. The included standalone Python checker exhaustively builds unlabelled trees via leaf attachment and canonical center codes; all 7,741 fifteen-vertex trees are generated, and precisely 132 have no degree-two vertices. The checks find exactly three two-element collision classes and none below fifteen. Distinct codes prove the pair members nonisometric. These are finite exhaustive claims supported by a complete generator argument, not by random sampling.

**Originality — PASS with residual risk.** The known edge-Hosoya polynomial and earlier tree-distance noninjectivity are expressly not claimed as new. Mémoli–Needham, arXiv:1810.09646v5, Section 4.1 Example 4.3, provides a stronger local-indistinguishability construction, but not the reduced 15-vertex minimum or the classification of all three pairs. Ramane et al. (2013), doi:10.1155/2013/857908, studies terminal Hosoya polynomials of line graphs. Searches of earlier tree-Hosoya and shape-distribution literature and accessible published result records did not reveal the precise statement. Slater (1982) was accessible only as an abstract; an older catalogue could still contain these pairs.

**Value — PASS.** Removing degree-two vertices gives the natural intrinsic branch-node representation of a finite unit-length metric tree. The sharp first ambiguity at 15 true branch/leaf nodes and the exact three doubletons answer a meaningful inverse-geometric question distinct from the previously known 9-vertex unrestricted collisions. The finite nature of the theorem does not reduce the importance of a complete cutoff and collision catalogue for a canonical shape-distribution invariant.

**Limits.** Not claimed for unequal edge lengths, arbitrary metric graphs or n>15. Proof and computer enumeration have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
