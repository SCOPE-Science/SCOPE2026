# Two-torsion and a Moore summand in the dodecahedral perfect-matching complex

## Finding
Let \(D=\operatorname{GP}(10,2)\) be the 20-vertex dodecahedral graph. Let \(\mathcal M_{\mathrm p}(D)\) be the simplicial complex whose maximal simplices correspond to perfect matchings of \(D\). There is an **integral homotopy equivalence**
\[
\boxed{\mathcal M_{\mathrm p}(D)\simeq M(\mathbb Z/2,2)\vee\bigvee^{20}S^3,}
\]
where \(M(\mathbb Z/2,2)=S^2\cup_{\deg 2}e^3\) is the mod-two Moore space. In particular,
\[
\widetilde H_i(\mathcal M_{\mathrm p}(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z/2&i=2,\\
\mathbb Z^{20}&i=3,\\
0&\text{otherwise}.
\end{cases}
\]
Thus a canonical cubic polyhedral graph has two-torsion in its **perfect-matching** complex; this is not an assertion about its ordinary matching complex.

## Assumptions and scope
Number vertices from zero through nineteen. Outer vertices are \(u_i=i\), inner vertices are \(v_i=10+i\), and the thirty edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\) for \(i\in\mathbb Z/10\mathbb Z\). Every edge is stored as a sorted integer pair, and the thirty pairs are then lexicographically sorted, giving bit positions zero through twenty-nine.

A perfect matching consists of ten pairwise vertex-disjoint edges covering all twenty graph vertices. The faces of \(\mathcal M_{\mathrm p}(D)\) are **exactly** the subsets of perfect matchings (including the empty face). We use the ordinary nonempty face poset to construct a discrete-Morse matching. The theorem applies to this specified finite graph and this particular subcomplex of the ordinary matching complex.

## Proof
**Exact enumeration.** Recursively choose the least uncovered graph vertex and pair it in every possible way with an uncovered neighbor. Each perfect matching arises along a unique recursion path, so exhaustive recursion produces exactly thirty-six perfect matchings. Forming every nonempty subset of those ten-edge matchings and deduplicating yields exactly 30,503 nonempty simplices. The simplex counts in dimensions zero through nine are
\[
(30,375,2180,5790,8352,7440,4320,1620,360,36).
\]
Consequently, there are thirty-six maximal nine-simplices and every nonempty face is represented by a 30-bit integer.

**Acyclic Morse matching.** Initially mark every nonempty face unpaired. For each sorted graph-edge index from zero through twenty-nine, pair each still-unpaired face not containing that edge with the larger face obtained by adding the edge, provided the larger face also remains unpaired. Remove both members immediately. Because the larger face uniquely adds the chosen bit, there are no conflicts at a fixed index. The exact stage counts are
\[
(5455,4610,4070,184,155,178,131,108,93,52,71,39,42,8,11,5,3,2,0,0,2,4,1,1,0,2,2,0,1,1).
\]
Their sum is 15,231 disjoint matched face pairs. Exactly forty-one critical faces remain: one vertex, ten two-simplices and thirty three-simplices. All 163,650 nonempty codimension-one face incidences are enumerated. Direct unmatched incidence arcs from upper to lower cells and each matched arc from lower to upper; Kahn's algorithm visits all 30,503 faces, establishing **global acyclicity**. Forman's discrete-Morse theorem therefore replaces the complex by a CW complex containing exactly those critical cells and no cells in any other dimension.

**Signed attaching degrees.** Order every simplicial face by its increasing edge bit positions; its oriented boundary has the usual alternating signs. To project a face onto critical faces of the same dimension, assign zero to cells paired downward, the corresponding basis vector to critical cells, and, for a lower face \(a\) paired upward with \(b\), recursively use
\[
P(a)=-[b:a]^{-1}\sum_{c\ne a,\ c\lessdot b}[b:c]P(c).
\]
Here \([b:a]\in\{+1,-1\}\) is the oriented incidence number. This recursion terminates by the certified acyclic gradient graph. Project the oriented boundaries of the thirty critical three-simplices into the ten critical two-simplex generators to obtain the exact integral \(10\times30\) Morse attaching-degree matrix \(B\). The included certificate records all ten rows and all thirty columns; exactly sixty-nine entries are nonzero and they are all \(+1\) or \(-1\).

**Integral Smith invariants without unverified heuristics.** Gaussian elimination of \(B\) over \(\mathbb F_2\) has rank nine. Its nine-by-nine submatrix indexed by zero-based rows \((0,2,3,4,5,6,7,8,9)\) and columns \((0,2,4,5,6,7,8,11,26)\) has integer determinant \(-1\). Its ten-by-ten submatrix on all rows and columns \((0,2,4,5,6,7,8,10,11,26)\) has determinant \(2\). These determinants are recomputed by exact integer Bareiss elimination, not floating-point arithmetic. The first forces the first nine Smith invariant factors to equal one. Since the mod-two rank is nine, every full-rank ten-by-ten minor is even; the exhibited determinant two forces the product of all ten nonzero invariant factors to equal two. Thus the Smith invariants of \(B\) are exactly
\[
(1,1,1,1,1,1,1,1,1,2).
\]

**Homotopy type.** The Morse CW complex has one zero-cell and no one-cells, so its two-skeleton is \(\bigvee^{10}S^2\). By Hurewicz, the group of attaching maps of each three-cell is \(\pi_2(\bigvee^{10}S^2)\cong\mathbb Z^{10}\), classified precisely by the corresponding column of \(B\). Elementary invertible integral row and column operations on \(B\) are realized by homotopy equivalences of the wedge of two-spheres and elementary changes of the attaching-cell basis. The above Smith form therefore yields nine degree-one cancelling pairs, one degree-two attachment \(S^2\cup_2e^3\), and twenty freely attached three-spheres. This proves the claimed integral homotopy equivalence.

## Verification
The attached `verify_dodecahedral_pm.py` runs with Python 3's standard library alone. Execute `python3 verify_dodecahedral_pm.py` or regenerate the exact certificate with `python3 verify_dodecahedral_pm.py --emit-certificate certificates/morse_boundary.json` from the package root. The program exhaustively reconstructs the thirty edges and all perfect matchings and faces, checks all face incidences and global matching acyclicity, recomputes the entire signed integral Morse boundary, verifies the unit and determinant-two minors, and independently computes the entire original simplicial boundary ranks modulo two. Its success marker is `DODECAHEDRON_PERFECT_MATCHING_MOORE_2_TORSION_20_S3_OK`.

The ranks of the original simplicial boundaries modulo two in degrees one through nine are
\[
(29,346,1833,3936,4416,3024,1296,324,36).
\]
Thus its mod-two Betti vector is \((1,0,1,21,0,0,0,0,0,0)\), in agreement with the universal coefficient theorem applied to the integral homology above. Mod-two ranks alone do not establish the Moore summand; the exact signed attaching-degree computation and integral minors do.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega introduced the systematic study of perfect-matching complexes and calculated homotopy types for specified planar **honeycomb** graphs; their theorems do not apply to the closed pentagonal dodecahedral graph. Chandrakar and Singh studied **polygonal line tilings** and narrow rectangular grids; the dodecahedral graph is not a line of polygons or a rectangular grid.

An existing publicly indexed **ordinary** dodecahedral matching-complex classification gives \(\mathcal M(D)\simeq\bigvee^5S^5\vee\bigvee^{117}S^6\). Its defining faces include matchings that cannot extend to a perfect matching. Since \(\mathcal M_{\mathrm p}(D)\subsetneq\mathcal M(D)\), the homotopy type of the full matching complex neither computes nor excludes torsion in the present subcomplex. A separate published classification of the perfect-matching complex of the **Heawood** graph gives a torsion-free wedge of sixteen two-spheres, but its different graph provides no implication here. Thus neither matching-complex variant nor prior perfect-matching example covers this result.

## Limitations
The result is a complete integral homotopy classification for one natural finite graph, not a classification of cubic graphs or all generalized Petersen graphs. Acyclicity, enumeration, and integral attaching degrees are established by a supplied exhaustive program and independently inspectable finite data rather than a short symbolic enumeration. The exact Smith computation determines the ordinary homotopy type but not an equivariant action on integral homology. The literature searches and inspected primary sources did not reveal an equivalent prior classification; unindexed or inaccessible equivalent results remain possible. No independent mathematical audit has been performed.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, first publicly submitted 2022-09-06, https://arxiv.org/abs/2209.02803, in particular Definition 1 and honeycomb homotopy classifications.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v1, first publicly submitted 2024-07-08, https://arxiv.org/abs/2407.05809, in particular Theorem 1.1 on line tilings and narrow grids.
3. Publicly indexed mathematical finding, *The dodecahedral matching complex is a wedge of five 5-spheres and 117 6-spheres*, identifier `2026/10/11/SCOPE-the-dodecahedral-matching-complex-is-a-wedge-of-five-5-spheres-a--07d4993d8316`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-dodecahedral-matching-complex-is-a-wedge-of-five-5-spheres-a--07d4993d8316.
4. Publicly indexed mathematical finding, *Perfect Morse reduction of the Heawood perfect-matching complex*, identifier `2026/10/11/SCOPE-perfect-morse-reduction-of-the-heawood-perfect-matching-complex--0994476b8c0d`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-perfect-morse-reduction-of-the-heawood-perfect-matching-complex--0994476b8c0d.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, discrete Morse theorem and cellular attaching maps.
