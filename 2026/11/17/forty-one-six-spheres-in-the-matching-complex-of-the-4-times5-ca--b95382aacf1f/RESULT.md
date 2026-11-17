# Forty-one six-spheres in the matching complex of the \(4\times5\) Cartesian grid

## Finding
For the Cartesian product of paths with four and five vertices,
\[
\mathcal M(P_4\square P_5)\simeq\bigvee^{41}S^6.
\]
Here \(\mathcal M(G)\) is the abstract simplicial complex on graph edges in which a set of edges is a face exactly when its members are pairwise vertex-disjoint. The equivalence is an integral, ordinary homotopy equivalence; in particular, the only nonzero reduced integral homology is \(\widetilde H_6\cong\mathbb Z^{41}\).

## Assumptions and scope
The grid graph \(G=P_4\square P_5\) has vertex set \(\{0,1,2,3\}\times\{0,1,2,3,4\}\), with edges connecting vertices whose Manhattan distance is one. It has 20 vertices and 31 edges. Both path factors are nonperiodic. This is the ordinary matching complex (independence complex of the line graph), not the perfect-matching subcomplex, the chessboard complex, or the categorical product of paths.

We enumerate the 31 grid edges deterministically. Visit cells lexicographically in row-major order, and at each cell append its downward edge (if present) followed by its rightward edge (if present). An edge set is encoded by a 31-bit integer with the corresponding edge-indices set. Its simplicial orientation uses increasing edge-indices. There are 120,465 matching faces including the empty face, so 120,464 nonempty simplices. The face counts, indexed by cardinality \(0\) through \(10\), are

`[1, 31, 395, 2696, 10769, 25835, 36771, 29580, 12181, 2111, 95]`.

## Proof
**1. Exhaustive acyclic matching.** List every matching by an increasing-index recursion: start from the empty set, and append only an edge disjoint from all currently selected endpoints. For each edge-index \(k=0,\ldots,30\), in order, pair each as-yet-unmatched nonempty face \(\sigma\) not containing edge \(k\) with \(\sigma\cup\{k\}\), whenever this also is a face and is as-yet-unmatched. Skip the empty face. The exact numbers of pairs made at successive indices are

`[31297,15629,0,0,4150,2839,1569,1624,973,0,0,632,91,172,0,266,185,204,260,54,49,29,59,23,26,12,29,15,3,6,9]`.

These total 60,205 pairs. To verify acyclicity, orient every cover in the *entire* face Hasse diagram upward if matched, otherwise downward. Enumerating all 120,465 faces, and all incidences obtained by removing one edge, a full topological sort visits every face. Thus the matching is acyclic. Its unpaired nonempty cells consist of one vertex, five 5-cells, 47 6-cells and one 7-cell. The empty augmented face is deliberately not counted as a cell of the topological Morse complex.

**2. Integral Morse boundary.** For increasing-edge orientations, the incidence from a face of cardinality \(r\) to the face with its \(j\)-th edge removed is \((-1)^j\), with \(j\) starting at zero. For a face \(\sigma\) that is the lower member of a matched pair with upper member \(\tau\), replace its formal generator by
\[
R(\sigma)=-[\tau:\sigma]^{-1}\sum_{\substack{\eta\subset\tau\\|\eta|=|\sigma|,\ \eta\ne\sigma}}[\tau:\eta]R(\eta).
\]
Set \(R(\sigma)=0\) when \(\sigma\) is the upper member, and \(R(\sigma)=\sigma\) on critical cells. This recursion terminates because the complete matching Hasse orientation is acyclic. Apply it to each critical cell's oriented simplicial boundary. The resulting integral Morse differentials are precisely a \(5\times47\) matrix \(D_6\) and a \(47\times1\) vector \(D_7\); all other positive-degree differentials vanish.

There are exactly 197 zero, 23 negative-unit, and 15 positive-unit entries of \(D_6\). In the sorted list of critical six-cells, its five columns at indices `0,1,2,15,19` form a \(5\times5\) minor with determinant \(-1\). Consequently, \(D_6\) is split surjective over \(\mathbb Z\). The vector \(D_7\) has just five nonzero coordinates: `(14,1),(34,-1),(36,1),(43,1),(44,1)`; it is therefore primitive. Exact matrix multiplication gives \(D_6D_7=0\). These facts are checked from scratch by the attached executable, not assumed from a recorded log.

**3. From Morse chains to homotopy.** Forman's acyclic discrete-Morse theorem gives a CW homotopy equivalent to the original complex with exactly the critical cells above. Because all cells have dimension zero or at least five, the attaching maps of the six-cells to the five-skeleton \(\bigvee^5S^5\) are classified by their integral degree vectors, since \(\pi_5(\bigvee^5S^5)\cong\mathbb Z^5\). The unimodular minor of \(D_6\) permits integral cellular changes of basis and the cancellation of all five 5-/6-cell pairs, yielding a CW homotopy equivalent to one vertex, 42 six-cells, and one 7-cell. Its 7-cell degree vector is primitive: it lies in the direct summand \(\ker D_6\subset\mathbb Z^{47}\), and its coordinates have greatest common divisor one. Again, \(\pi_6(\bigvee^{42}S^6)\cong\mathbb Z^{42}\). An invertible integral basis change sends the primitive degree vector to a standard generator, and one final 6-/7-cell cancellation leaves exactly 41 six-spheres wedged at a vertex.

## Verification
Run `python verify_grid_4x5.py` with Python 3.10+ and SymPy. This script independently computes the face polynomial via vertex-deletion recursion, enumerates all faces, constructs and globally checks every pair and every Hasse cover, computes signed integral Morse boundaries, checks the unimodular minor, the five-entry primitive vector, and the chain identity. Expected stdout is in `expected_grid_4x5.txt`. Its assertions reconstruct the counts, orientations, coefficients and finite certificate directly from the specified graph. The finite result is exhaustive for the stated 20-vertex graph, not a conjectural extrapolation to all grid sizes.

## Relationship to prior work
Chauhan, Sharma and Shukla (first public preprint 2026-09-23; arXiv:2609.27366) investigate the homology and connectivity of the \(3\times n\) Cartesian-grid matching complexes. Goyal, Shukla and Singh (arXiv:2106.09915; first public 2021-06-18) treat the same three-row family, as is explicit in their full-text definition of rectangular grid graphs, statement of scope, and Table 1 of the original version. Braun and Hough (2017) address small-grid matching complexes, in particular the two-row family. A previous recorded exact result for \(P_4\square P_4\) gives a different mixed-dimensional sphere wedge \(\bigvee^6S^4\vee\bigvee^2S^5\). None of these cited statements implies the specific \(4\times5\) homotopy type; neither a general four-row theorem nor an equivalent exact finite classification was identified in the completed searches.

## Limitations
This is a finite, computer-assisted exact homotopy computation for one nonperiodic four-by-five grid. No classification of arbitrary four-row widths, symmetry representations, or adjacent filtration objects is claimed. The 2026 three-row paper's full text was not available through the attempted sources, so exhaustive bibliographic priority is not guaranteed; its accessible stated results remain confined to three-row grids. The computation and proof have not received independent mathematical review.

## References
- P. Chauhan, A. Sharma and S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, first posted 2026-09-23. https://arxiv.org/abs/2609.27366
- S. Goyal, S. Shukla and A. Singh, *Matching complexes of \(3\times n\) grid graphs*, first posted 2021-06-18; full author-uploaded preprint text available at https://www.researchgate.net/publication/352559112_Matching_complexes_of_bf_3_times_n_grid_graphs and https://arxiv.org/abs/2106.09915
- B. Braun and W. Hough, *Matching and Independence Complexes Related to Small Grids*, Electron. J. Combin. 24 (2017), P4.18. https://doi.org/10.37236/6212
- Previous four-by-four exact classification: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-matching-complex-of-the-4-times4-cartesian-square-grid-is-a--f1b5ea641880
- R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
