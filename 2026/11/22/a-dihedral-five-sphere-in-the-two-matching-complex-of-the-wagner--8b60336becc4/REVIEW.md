# Review: Wagner degree-two matching sphere and dihedral action

## Correctness — PASS

The eight-vertex graph is defined by the eight cyclic edges and four opposite chords; the degree-two constraint is exactly exclusion of the full three-edge star at each vertex. All 4096 possible subsets are tested. The resulting face vector is \((12,66,212,423,516,352,108,7)\) and there are 1696 nonempty faces. An explicit repeated-toggle pairing on the augmented face set has 848 pairs and one unmatched six-edge face. Removing the empty-face pair leaves one critical vertex, one critical five-cell, and 847 ordinary pairs. The complete oriented nonempty Hasse graph on 1696 vertices is topologically sorted, directly certifying acyclicity. Discrete Morse theory then proves a genuine integral homotopy equivalence with \(S^5\), rather than extrapolation from homology.

The rim-versus-opposite-edge four-cycle incidence separates the two orbits, proving that the graph automorphism group is precisely the sixteen-element \(D_8\). Independent of the Morse pairing, signed permutation traces on all faces give reduced Lefschetz number \(+1\) for each of the rotation and reflection generators; because the only reduced homology is \(\mathbb Z\) in degree five, both act by \(-1\). The rational orbit-space conclusion follows from finite-group averaging after subdivision. The supplied standard-library checker was executed from its extracted source, and every assertion passed. Its complete, finite enumeration covers the exact stated domain.

## Originality — PASS against inspected evidence

Julianne Vega, *2-Matching Complexes*, arXiv:1909.10406 (first public September 23, 2019), supplies terminology and important earlier homotopy classifications; the inspected primary text does not contain the eight-vertex Wagner degree-two matching calculation, and its induced-claw hypotheses do not cover this cubic Wagner graph. A separately indexed calculation \(M_2(Q_3)\simeq\bigvee^3S^5\) concerns the cube graph, not the Wagner graph. Published Wagner results for its ordinary matching, ordinary discrete-Morse, four-cut, and vertex two-independence complexes concern different mathematical objects, not an implication of the stated new homotopy/character classification. The recent Agarwal–Basak paper on independence and perfect-matching complexes of Möbius ladders (arXiv:2608.30601) is a plausible family-level source; only its public abstract could be inspected, and its stated subjects are different from the degree-two matching complex. The comparison does not claim that this inaccessible full text has been read.

The queries and named implication comparisons are detailed in AUDIT.json. Residual risk is an equivalent unpublished, unindexed, or inaccessible calculation, not an identified covering result. Absence of a database hit alone has not been taken as proof of originality.

## Value — PASS

The Wagner graph is the smallest twisted cubic circular ladder with eight vertices and its natural untwisted eight-vertex cubic counterpart is the cube. The known degree-two matching complex of the cube is three five-spheres, whereas this graph's complex is one five-sphere. This is a sharply motivated twist-sensitive finite homotopy classification, not an arbitrary graph parameter. Moreover the nontrivial integral orientation character and rational acyclicity of the full dihedral quotient are not implied merely by the sphere homotopy type. These data can constrain future calculations for longer twisted ladders and their symmetry quotients. Nothing is claimed for uncomputed larger graphs or integral torsion of the orbit space.

## Closest sources and limitations

- Julianne Vega, *2-Matching Complexes*, https://arxiv.org/abs/1909.10406 (primary full text inspected).
- *The two-matching complex of the three-cube is a wedge of three five-spheres*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-two-matching-complex-of-the-three-cube-is-a-wedge-of-three-f--17687c557e9f (indexed public summary, different cubic graph).
- *The Wagner graph matching complex and its two edge-orbit splittings*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-wagner-graph-matching-complex-and-its-two-edge-orbit-splitti--1b0ec7f839cb (indexed public summary, ordinary matching instead of degree-two).
- Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (abstract inspected only; complete text inaccessible in this examination).

Self-review: passed. Independent audit: not yet performed.
