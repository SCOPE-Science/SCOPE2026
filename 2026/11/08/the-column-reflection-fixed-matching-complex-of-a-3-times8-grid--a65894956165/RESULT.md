# The column-reflection fixed matching complex of a \(3\times8\) grid is a wedge of four four-spheres

## Finding
Let \(G=P_3\square P_8\) be the nearest-neighbor grid graph with vertices \((r,c)\), where \(r\in\{0,1,2\}\) and \(c\in\{0,\ldots,7\}\). Let \(\mathcal M(G)\) be its ordinary matching complex, whose simplices are sets of vertex-disjoint graph edges. The column reflection \(\tau(r,c)=(r,7-c)\) induces a simplicial involution on \(\mathcal M(G)\). Its **geometric** fixed-point space has the integral homotopy type
\[
\boxed{\left|\mathcal M(P_3\square P_8)\right|^{\langle\tau\rangle}\simeq \bigvee^4 S^4.}
\]
In particular, the only nonzero reduced integral homology is \(\widetilde H_4\cong\mathbb Z^4\); all other reduced integral homology groups vanish. This is a statement about the geometry of fixed points, not the invariant part of the homology of the entire matching complex.

## Assumptions and scope
Graphs are simple, finite, undirected, with the usual nearest-neighbor Cartesian-product edges. The reflection reverses eight columns while fixing each row. A geometric fixed point can be in the interior of a simplex whose individual vertices (edges of the grid) are interchanged; consequently the fixed-point set cannot be found by taking only pointwise-fixed vertices. The only grid size claimed here is \(3\times8\); no classification for arbitrary width, any other grid symmetry, or equivariant homotopy equivalence is asserted.

## Proof
**1. Exact fixed-point model.** The grid has 37 edges. Reflection partitions them into 20 orbits: 17 two-edge orbits and 3 one-edge orbits consisting of horizontal edges crossing the seam between columns 3 and 4. For any simplicial complex with a vertex-permuting involution, a geometric fixed point has constant barycentric coordinates on each orbit. A support is allowed exactly when the union of the orbits is an original simplex. Using one barycentric orbit-point for each allowed orbit gives a simplicial complex PL-homeomorphic to the geometric fixed locus; this is a direct affine simplex-by-simplex identification, not a homotopy approximation.

Denote by \(W\) the graph formed from \(P_3\square P_4\), with vertices \((r,c)\) for \(0\le r<3\), \(0\le c<4\), by attaching one new degree-one leaf \((r,4)\) to each \((r,3)\). An orbit of nonseam edges is identified with its unique member in the left four columns; each seam edge identifies with the corresponding leaf edge. This bijects the 20 orbits with the 20 edges of \(W\). Two orbits jointly form a matching of the original grid if and only if the corresponding edges of \(W\) are disjoint: left and reflected right halves have disjoint vertex sets, while a seam edge meets exactly the left boundary vertex encoded by its leaf edge. All higher matching constraints are pairwise. Therefore the fixed-orbit complex is exactly \(\mathcal M(W)\), establishing a PL homeomorphism
\[
\left|\mathcal M(G)\right|^{\langle\tau\rangle}\cong_{\mathrm{PL}}\left|\mathcal M(W)\right|.
\]

**2. A finite but complete acyclic matching.** Number the 20 edges of \(W\) by the following explicit convention: loop columns \(c=0,1,2,3\) in increasing order, and within each loop rows \(r=0,1,2\) in increasing order. For each \((r,c)\), append its vertical edge to \((r+1,c)\) if \(r<2\), followed by its horizontal edge to \((r,c+1)\) if \(c<3\). Finally append leaf edges from \((r,3)\) to \((r,4)\) in row order. The resulting 20 edges are indexed \(0,\ldots,19\).

A face is a sorted tuple of edge indices forming a matching, including the augmented empty face. The augmented face poset contains exactly 2,636 faces; its nonempty face vector in dimensions zero through six is
\[
(20,149,524,911,750,255,26).
\]
Use the fixed pivot order
\[
(4,11,1,18,15,5,8,12,13,10,14,2,17,6,9,0,3,7,16,19).
\]
For each pivot \(v\), traverse all still-unmatched faces \(S\) **not** containing \(v\) in decreasing cardinality and, for equal cardinality, increasing lexicographic order. Whenever \(S\cup\{v\}\) is still unmatched, pair the two and remove both. This algorithm is deterministic. It produces exactly 1,316 incident face pairs, including one that uses the augmented empty face; its only unmatched augmented faces are the following four five-element sets:
\[
\{0,6,7,14,15\},\quad\{0,7,13,17,19\},\quad
\{0,8,9,16,17\},\quad\{2,5,13,17,19\}.
\]
To test acyclicity, orient every face-containment Hasse arrow from a face to its codimension-one subface, except reverse the 1,316 paired arrows. The accompanying standalone `verify.py` constructs *all* such arrows and removes zero-indegree vertices in a complete topological sort. It visits exactly 2,636 vertices. Thus there are no directed cycles; both complete face enumeration and this finite directed-acyclicity test constitute an exact reproducible discrete-Morse certificate. This is not an unverified search heuristic or a numerical homology guess.

**3. Integral homotopy consequence.** Discard the augmented empty face and its unique pair. The ordinary face poset has exactly one unmatched 0-cell and four unmatched 4-cells; the restricted matching remains acyclic. Forman's discrete Morse theorem gives a CW complex with one 0-cell and four 4-cells and no other cells. Every attaching map of a 4-cell into this CW complex's 3-skeleton (a point) is null. Hence the CW complex is precisely homotopy equivalent to the wedge of four 4-spheres. Combining with Step 1 proves the theorem over the integers.

## Verification
Run `python3 verify.py` using only the Python standard library. The verifier separately constructs the 37 original grid edges and their reflection orbits; checks the 20-to-20 orbit/whiskered-edge correspondence; tests all 190 pairwise orbit conflicts; independently enumerates all 2,636 augmented faces; reconstructs all 1,316 face pairs using the stated pivot order; checks every Hasse arrow for acyclicity; counts the exact remaining critical dimensions; and independently computes reduced mod-two simplicial boundary ranks. It prints `VERIFY_OK` upon success. Its recorded output is `verification_output.txt`. The all-grid conclusion here is finite but exhaustive because the object itself is finite; no sample-to-infinite extrapolation is used.

## Relationship to prior work
Chauhan–Sharma–Shukla (2026) investigate nonequivariant homology and connectivity of \(3\times n\) grid matching complexes, not a homotopy type of a reflection fixed locus. The closest explicit symmetry calculation in published research, *Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes* (2026), identifies invariant matching orbits and computes alternating rational homology traces at all widths. For even width, its proof includes the equivalent three-seam-edge orbit count. That previous calculation yields a **reduced Euler/Lefschetz number**, not the exact integral homotopy type, homology concentration, or the acyclic matching certified here. A priori an Euler characteristic does not force the wedge-of-four-spheres conclusion. Other full-grid homotopy computations, including the \(4\times4\) Cartesian grid, involve nonisomorphic graphs and do not imply the fixed-locus result. The earlier claimed all-width nonequivariant classification in a 2021 paper was retracted and is not used.

## Limitations
Only the column reflection of the \(3\times8\) nearest-neighbor grid is covered. No homological representation of its full symmetry group, no higher or lower-width fixed-locus classification, and no PL homeomorphism to the sphere wedge are claimed. Literature uncertainty remains: the September 2026 primary preprint was verifiable by its public abstract but its full PDF was not accessible during comparison; related unindexed treatments of matching complexes with boundary leaves could contain an equivalent result. A self-review is not an independent mathematical audit.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366v1, first public 2026-09-23, https://arxiv.org/abs/2609.27366.
2. *Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes*, published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-orthogonal-reflection-lefschetz-formulas-for-3-times-n-grid-matc--c1da8c8f4653.
3. B. Braun, W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, Electronic Journal of Combinatorics 24(4), P4.18 (2017), https://doi.org/10.37236/6212.
4. S. Goyal, S. Shukla, A. Singh, *Matching Complexes of \(3\times n\) Grid Graphs*, Electronic Journal of Combinatorics 28(4), P4.16 (2021), https://doi.org/10.37236/10496. **Retracted; no theorem from it is used.**
