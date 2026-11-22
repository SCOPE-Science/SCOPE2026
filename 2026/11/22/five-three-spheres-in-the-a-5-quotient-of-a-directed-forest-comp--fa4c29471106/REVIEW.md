# Scientific assessment: an alternating-group directed-forest quotient

## Correctness — PASS

The definition is the full directed-forest complex of the complete loopless bidirected five-vertex graph, not the multipath or undirected graphic forest complex. Barycentric whole-flag orbit cells rigorously model the ordinary nonfree group quotient because the action is without inversions after subdivision. `verify.py` reconstructs 1,295 original nonempty faces and 53,845 flags, reduces them to 908 even-label quotient cells, checks every signed integral boundary square, executes 451 unit-pivot cancellations, and obtains one zero-cell and five zero-differential three-cells. An independent signed Burnside–Lefschetz calculation gives quotient Euler characteristic \(-4\). The complete-source shellability theorem establishes simple connectivity of the original complex, and every three-cycle fixes an arc supported on its two untouched labels; Armstrong therefore makes the orbit fundamental group trivial. The Hurewicz and homological Whitehead theorems yield the five-three-sphere wedge. No computation is mistaken for an infinite theorem.

## Originality — PASS relative to inspected evidence

Kozlov's 2001 Section 6 treats the identical complete directed-forest complex but the **full \(S_5\) quotient**, not the intermediate \(A_5\) quotient; the alternating-group symbols inside his proof concern edge-label orders. Engström (2005) and Jojić (2011) establish the original complex and shellability but no even-permutation geometric quotient homotopy type. The closest publicly recorded five-label calculation establishes only the full symmetric quotient \(S^3\vee S^3\), which cannot imply the integral homotopy type of its branched index-two predecessor. The difference is verified directly, not inferred from missing title hits. Residual risk: equivalent unpublished or unindexed parity-quotient calculations.

## Value — PASS

The five-label case is the first with the nonabelian simple rotational group \(A_5\). It yields a natural parity-sensitive refinement of the complete symmetric orbit problem studied by Kozlov. The result shows that passing from the icosahedral even-label group to all permutations identifies three of five rational top classes with their negatives; this is a full **integral homotopy** classification, including fundamental group and torsion exclusion, not only a rational character count. The precise \(A_5\) comparison is mathematically motivated, unlike an arbitrary graph slice or an increment in the number of labels.

## Limits and closest material

The result does not extend to arbitrary \(n\), does not assert geometric collapse, and does not characterize an integral residual-involution lattice. Relevant materials read include Kozlov (2001) Section 6, Engström (2005) Section 2, Jojić (2012) Sections 1–2, the public full-symmetric five-label result and its companion review/verification, and Armstrong's orbit-space theorem statement. All finite computations are reproducible from source with standard-library Python. There is no independent external mathematical audit.

Self-review: passed. Independent audit: not yet performed.
