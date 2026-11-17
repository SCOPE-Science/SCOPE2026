# A mixed-dimensional integral sphere wedge in the Chvátal perfect-matching complex

## Finding

Let \(G\) be the classical twelve-vertex Chvátal graph, and let \(\mathcal P(G)\) be the perfect-matching extendability simplicial complex on its twenty-four edges: a set of edges is a face if and only if it is contained in some perfect matching. Then the geometric realization has the **integral homotopy type**

\[
|\mathcal P(G)|\simeq \left(\bigvee^{17}S^2\right)\vee S^3.
\]

In particular, its only nonzero reduced integral homology groups are \(\widetilde H_2\cong\mathbb Z^{17}\) and \(\widetilde H_3\cong\mathbb Z\), and \(\pi_1\) is trivial. The complex is pure of dimension five but is not shellable, since a pure shellable simplicial complex can have reduced integral homology only in its top dimension.

## Assumptions and scope

Define a labeled simple graph on vertices \(\{0,1,\ldots,11\}\) with edges, in this exact order (the integers in this displayed data are vertex labels):

```
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

This is the standard labeled twelve-vertex, four-regular Chvátal graph. Perfect matching means a collection of six pairwise disjoint edges covering all twelve graph vertices. A face of \(\mathcal P(G)\) is any subset of one of these six-edge collections, including the empty face. It is not the **ordinary matching complex**, because a partial matching that does not extend to a perfect matching is excluded.

The finite graph was introduced in Chvátal's 1970 paper as a minimal triangle-free four-chromatic four-regular example. The present claim concerns the topology of its perfect-matching complex, not its graph coloring and not the ordinary matching complex.

## Proof

**Exhaustive face model.** Every six-element subset of the twenty-four graph edges is inspected. Exactly fifty-two use every graph vertex once; these are *all* perfect matchings. Taking every subset of these matching facets yields the full abstract simplicial complex, with face counts indexed by cardinality

\[
(f_0^{\emptyset},f_1,f_2,f_3,f_4,f_5,f_6)
=(1,24,204,612,675,312,52).
\]

(The first coordinate counts the empty face; the last counts six-element facets.) Thus the complex contains 1,880 faces including the empty face, and every facet has dimension five.

**Explicit acyclic partial matching.** Number the edges from zero through twenty-three in the order displayed above. Process the edge coordinates in the following order:

```
15 17 5 10 19 13 1 11 8 3 7 6 23 2 14 0 16 18 12 20 9 4 21 22
```

At the coordinate \(j\), pair each *currently unpaired nonempty* face \(\sigma\) not containing that edge with \(\sigma\cup\{j\}\) when both faces are currently unpaired, then remove both from consideration. This is a sequence of element-toggle matchings of the form used in combinatorial discrete Morse theory. It yields exactly 930 pairs and nineteen critical faces: one vertex, seventeen triangles (two-cells), and one tetrahedron (three-cell).

Acyclicity can be checked without relying only on the toggle theorem: reverse matched cover arrows in the nonempty-face Hasse diagram and orient every other cover arrow downward. The resultant directed graph has exactly 1,879 nodes and 6,816 arrows, and an exhaustive topological sort visits all 1,879 nodes. Hence there is no closed discrete gradient path. Forman's discrete Morse theorem gives a homotopy-equivalent CW complex with precisely one 0-cell, seventeen 2-cells and one 3-cell.

**Exact integral attaching calculation.** Use ascending edge indices for simplex orientations, so deleting the \(k\)-th listed vertex contributes \((-1)^k\). For a noncritical oriented 2-simplex \(\tau\) paired *upward* with a 3-simplex \(\upsilon\), let \(\epsilon\in\{\pm1\}\) be its coefficient in \(\partial\upsilon\). Eliminate \(\tau\) by replacing it with \(-\epsilon\) times the sum of the other oriented faces of \(\upsilon\). A 2-simplex paired downward with a 1-simplex contributes zero in degree two; a critical 2-simplex contributes itself. Iterating this recurrence terminates because the directed matching graph is acyclic and computes the exact integer cellular Morse boundary. Applied to the one critical 3-simplex, all seventeen resulting boundary coefficients are zero.

The 2-skeleton of the resulting CW complex is \(\bigvee^{17}S^2\). The Hurewicz homomorphism \(\pi_2\big(\bigvee^{17}S^2\big)\to H_2\big(\bigvee^{17}S^2;\mathbb Z\big)\) is an isomorphism because the wedge is simply connected. Therefore the zero integer attaching-degree vector implies that the unique 3-cell is attached by a nullhomotopic map. This proves the asserted **integral homotopy equivalence**, not merely the Betti numbers.

## Verification

The supplied standalone `verify.py` uses only the Python standard library. Running `python verify.py` enumerates the exact fifty-two perfect matchings, all 1,880 simplices, every one of the 930 matching pairs, and every directed Hasse incidence. It evaluates the complete integer Morse boundary vector and requires it to vanish. Independently of the Morse projection, it computes direct simplicial boundary ranks over \(\mathbb F_2\) of \((23,181,414,260,52)\) in dimensions one through five, confirming mod-two Betti numbers \((17,1)\) in dimensions two and three. The mod-two check alone would not establish integral torsion-freeness: that follows from the integral homotopy argument above. `verify_output.txt` records the actual execution output.

## Relationship to prior work

Chvátal's 1970 paper introduced the underlying extremal graph. Bayer, Jelić Milutinović and Vega define the perfect-matching complex in their 2022 preprint (Definition 1) and use element-toggle discrete Morse theory (Theorem 8), but their substantive classifications concern honeycomb graphs. The Chvátal graph is neither a honeycomb graph nor a case of their theorems. A separate indexed calculation determines the **ordinary** Chvátal matching complex as a wedge of three-spheres and a three-primary Moore space; its faces include nonextendible partial matchings, so its statement does not give the present perfect-matching homotopy type. Other known perfect-matching-complex classifications concern different graphs and do not imply this result.

## Limitations

This is one exact twelve-vertex graph, not a general theorem about all triangle-free four-chromatic graphs or all four-regular graphs. The calculation does not determine symmetry representations of the homology, or the homotopy type of arbitrary graph covers or minors. The earliest day-dated public-source metadata used is the reported July 1, 1970 date for Chvátal's graph paper; journal-index date precision may not identify the literal day of public release. Publication priority cannot be guaranteed from an indexed literature search; unindexed or inaccessible equivalent results remain possible. No independent mathematical audit has been performed.

## References

1. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, Journal of Combinatorial Theory 9 (1970), 93–94. DOI: 10.1016/S0021-9800(70)80057-6.
2. M. Bayer, M. Jelić Milutinović, and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803 (first preprint September 6, 2022), especially Definition 1 and Theorems 6, 8, 14 and 15.
3. Related indexed research: *Three-torsion and a Moore summand in the Chvátal matching complex* (ordinary matching-complex result, different simplicial complex), record identifier `2026/10/25/SCOPE-three-torsion-and-a-moore-summand-in-the-chv-tal-matching-comple--ee4a503ae424`.
