# Scientific review: dihedral phylogenetic tree-link quotients

## Correctness — PASS

The finite object is specified as the **all-compatible-splits** phylogenetic link with nontrivial unordered splits; it is not a single planar noncrossing tree complex. Barycentric subdivision eliminates inversions and makes dihedral orbit chains an actual cellular model of the ordinary quotient. The exact enumerator checks the original-face and quotient-cell totals, every integer boundary composition, and the 4 and 95 actual elementary collapses for the five- and six-leaf quotients. For seven leaves, the mod-two and mod-seven ranks \((231,1429,1643)\), together with invariants of the classical simply connected 120-sphere wedge away from primes dividing 14, prove integral vanishing of all lower homology. The reflection-fixed split and Armstrong theorem prove simple connectivity. Euler characteristic and Whitehead finish the wedge classification. The independent signed Burnside computation gives the same Euler characteristic. Critical computations are replayable from the two bundled stand-alone scripts. Residual risk: a programming or modeling error undetected by two enumeration methods, or an incorrect application of a classical theorem; no independent audit is claimed.

## Originality — PASS relative to the inspected literature

The foundational papers classify the unquotiented tree link or its polyhedral models, rather than its ordinary polygon-group quotient. A relevant paper on symmetric trees treats fixed-space conditions, not geometric orbit spaces. Closest public indexed comparisons involve the six-point proper partition complex under \(D_6\) or the seven-point noncrossing-partition complex under \(D_7\), whose face relations and group actions differ. Neither statement implies the exact geometric split-quotient homotopy classification, and neither resolves both small-case collapses and the seven-leaf primary torsion check. The comparisons considered root choices, equivalent Bergman-complex formulations and the distinction between module invariants and orbit topology, not merely keyword matches. Publication-priority uncertainty remains from unindexed or inaccessible work.

## Value — PASS

Tree-space links encode all compatible internal splits and retain canonical leaf-relabeling symmetries. Quotienting by rotation and reflection models forgetting the orientation and distinguished starting point of a circularly labeled leaf set. The first four nontrivial cases show a structurally informative transition from disconnected to contractible to a genuinely three-dimensional torsion-free sphere wedge; the seven-leaf result classifies the full homotopy type, not just a Betti number. No unproven extrapolation to more leaves or practical biological application is asserted.

## Evidence and limitations

Sources: Billera–Holmes–Vogtmann (2001); Ardila–Klivans (2003 preprint); Devadoss–Huang–Spadacene (2013 preprint); Armstrong (1965); Hultman (2007). Computational verification: `verify_dihedral_tree_links.py` and `verify_tree_burnside.py`. The first computes exhaustive quotient cellular structures and two independent modular rank tests; the second computes signed face Lefschetz traces. The result is restricted to \(4\le n\le7\). These are same-review findings, not an independent certification.

Self-review: passed. Independent audit: not yet performed.
