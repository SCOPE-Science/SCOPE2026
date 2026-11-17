# Scientific review of the dihedral permutation-complex theorem

## Correctness — PASS

The theorem concerns geometric realizations of ordered-word semisimplicial complexes, rather than ordinary abstract simplicial complexes. The unrestricted proof is reconstructed through four independently checkable steps: the cyclic-rotation attachments have exact contractible intersections after their second member; the opposite-orientation intersection has precisely all directed edges; two integral descent cocycles evaluate on a digon and a directed triangle with unimodular determinant; and the van Kampen and Mayer–Vietoris sequences force simple connectivity and free second homology, followed by the homological Whitehead theorem. The argument covers all integers \(n\ge3\) and does not extrapolate from enumerated cases. The attached executable independently checks complete face sets and boundary matrices at six dimensions. The critical risk is confusion between ordered two-cells and unordered simplices; the proof and checker preserve ordered words throughout.

## Originality — PASS with residual risk

Govc (arXiv:2611.11362, 2026-11-08) proves freeness of fundamental groups of *all* permutation complexes, but does not state the two-orientation sphere-bouquet classification. Chachólski–Levi–Meshulam (arXiv:1908.03394, Sections 1–3, 2019) determine homotopy types for *two* generating permutations and discuss arbitrary families, but their theorem does not imply the exact \(2n\)-generator dihedral formula without the new intersection-and-winding argument. Elizalde–Hanlon–Hersh (arXiv:2610.07303, introduction and relevant definitions, 2026-10-05) work with permutations avoiding given patterns, not with the dihedral orbit of a full word. Targeted searches for cyclically ordered injective-word complexes, dihedral permutation-complex homotopy, reversals, aliases and existing research claims found no equivalent theorem. This is evidence of no identified coverage, not a proof of global novelty. Unindexed equivalent combinatorial models are the main remaining risk.

## Mathematical value — PASS

The complete, uniform homotopy classification of a natural dihedral orbit family provides a concrete example in which two circle-shaped subcomplexes combine to a simply connected complex with quadratic second homology. The integral primitive winding calculation is essential: the Euler characteristic alone cannot determine the homotopy type or rule out torsion. The result addresses the gap between a global fundamental-group freeness theorem and exact higher-dimensional homotopy for structured families; it also supplies a tractable benchmark for ordered-cell and directed-flag computations. The family restriction and lack of an equivariant classification are material limitations, not hidden extensions.

## Literature comparisons and limitations

The closest accessible sources were inspected for definitions, main results and plausible implicit coverage, including the original 2019 multi-generator setup. No independent referee or external mathematical validation has reviewed this result. The conclusion is restricted to full rotations of both orientations for \(n\ge3\), with ordinary nonequivariant homotopy.

Self-review: passed. Independent audit: not yet performed.
