# Three nonzero integral homology degrees in the perfect-matching complex of the \(4\times6\) grid

## Finding
Let \(G=P_4\square P_6\) be the simple Cartesian grid on 24 vertices, with 38 horizontal or vertical edges and no periodic identification. Write \(\mathcal P(G)\) for its **perfect-matching extendibility complex**: an edge subset is a face if and only if it is contained in a perfect matching of \(G\). Its maximal faces are precisely perfect matchings, each having 12 edges.

The complex is 2-connected. Its **complete reduced integral homology** is
\[
\widetilde H_j(\mathcal P(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z&j=3,\\
\mathbb Z^7&j=4,\\
\mathbb Z&j=5,\\
0&\text{otherwise}.
\end{cases}
\]
In particular this natural grid complex has integral homology in three consecutive dimensions. This is a homology classification, not a claim of an explicit homotopy wedge decomposition.

## Assumptions and scope
Number vertices by \(v_{r,c}=6r+c\) for \(0\le r<4\) and \(0\le c<6\). Enumerate edges by increasing \(r,c\), listing the downward edge first if it exists, followed by the rightward edge if it exists. A face is encoded as a 38-bit integer with bit \(i\) representing edge \(i\). Orient each nonempty face by increasing edge index, making each codimension-one deletion carry sign \((-1)^j\) when its deleted vertex has index \(j\) in this ordered list. The statement is over \(\mathbb Z\) and includes all homology degrees, with no field restriction.

## Proof
**Perfect matchings and face enumeration.** Start with the full uncovered-vertex bit set, choose its least vertex \(a\), and branch over every neighboring uncovered vertex \(b\), recording the edge \(ab\) and recursing after deleting \(a,b\). The branches are disjoint and exhaustive, because every perfect matching pairs \(a\) with exactly one such \(b\). This gives exactly 281 perfect matchings. Enumerate every subset of their 12 edge bits and deduplicate; this gives 511,338 nonempty faces. The face counts in dimensions \(0\) through \(11\) are
\[
(38,603,4966,22798,63018,111481,130738,102785,53540,17718,3372,281).
\]
The resulting reduced Euler characteristic is \(5\).

**Acyclic matching.** Initially mark every nonempty face unmatched. For edges \(i=0,1,\ldots,37\) in order, pair each as-yet-unmatched face \(\sigma\) omitting \(i\) with \(\sigma\cup\{i\}\), whenever that larger face is also unmatched; process lower faces using their integer-bitmask set membership, with the empty face excluded. This gives exactly 255,663 pairs, leaving precisely 12 critical faces: one in dimension zero, two in dimension three, eight in dimension four and one in dimension five. For every cover relation in the complete face Hasse graph orient a matched incidence upward and every other incidence downward. A complete Kahn topological sort of all 511,338 vertices removes every vertex. It therefore certifies the absence of a directed cycle, so this is an acyclic discrete-Morse matching.

**Integral Morse boundaries.** Choose critical faces in increasing integer-bitmask order in each dimension. Use signed oriented simplex boundaries and the elementary elimination rule: when a face \(f\) is paired upward with \(h=f\cup\{i\}\), replace \(f\) by minus the other boundary terms of \(h\) divided by the unit incidence sign of \(f\). Recursion terminates because the full gradient graph is acyclic. Critical faces paired downward contribute zero to the corresponding target group. This computes the exact integer Morse differentials, not just field ranks. With the eight critical 4-cells listed as columns and the two critical 3-cells as rows, the degree-four boundary is
\[
\partial_4=\begin{pmatrix}-1&0&0&0&0&0&0&0\\0&0&0&0&0&0&0&0\end{pmatrix},
\qquad\partial_5=\begin{pmatrix}0\\0\\0\\0\\0\\0\\0\\0\end{pmatrix}.
\]
All other positive-dimensional Morse boundary maps are zero for dimensional reasons. Hence the three surviving nontrivial reduced chain groups have homology \(\mathbb Z\), \(\mathbb Z^7\), \(\mathbb Z\) in dimensions \(3,4,5\), respectively, with no torsion. The Morse complex has one 0-cell and no cells in dimensions one and two, making it 2-connected; homotopy equivalence transfers this property to \(\mathcal P(G)\).

## Verification
The companion `check_grid46_homology.py` is standalone Python 3 source, with no third-party dependencies. Running `python3 check_grid46_homology.py` independently enumerates the matching facets, all faces and all pairing incidences; checks the complete directed Hasse graph for acyclicity; then computes integral Morse matrices by signed gradient-path substitution. It asserts exactly 281 facets, 511,338 nonempty faces, 255,663 matched pairs, the 12 critical-cell distribution, and the displayed complete Morse matrices. All assertions passed on the actual included source.

## Relationship to prior work
Chandrakar, Chau, Goyal, Karki and Subhash (arXiv:2611.18058v1, 13 November 2026) give a sphere-wedge classification for the **three-row** even-column grids. The present claim has **four rows**, and its three separate integral homology degrees cannot be inferred by specializing their three-row theorem. Earlier investigations by Chandrakar and Singh (arXiv:2407.05809) concern polygonal-line and two-row tilings; the honeycomb results of Bayer, Jelić Milutinović and Vega concern a different graph family. Existing finite grid computations for the four-by-four perfect-matching complex and a four-by-five perfect-matching complex do not supply the six-column chain calculation. Ordinary matching complexes must not be confused with the perfect-matching extendibility complex studied here.

## Limitations
This is a finite, exact integral-homology and connectivity classification for the nonperiodic four-by-six grid only. It does **not** establish a homotopy wedge decomposition or a uniform formula for all four-row grids, and the 5-cell could have a homotopically nontrivial attaching map despite its zero cellular boundary. The enumeration certificate is exhaustive for this finite graph but is not a proof for larger grids. Independent mathematical validation has not been performed. Unindexed equivalent literature remains a priority uncertainty.

## References
- H. Chandrakar, T. Chau, S. Goyal, R. Karki and B. Subhash, *Perfect Matching Complexes of 3×2n Grid Graph*, arXiv:2611.18058v1, first public 13 November 2026. https://arxiv.org/abs/2611.18058
- H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first public 2024. https://arxiv.org/abs/2407.05809
- M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, Electronic Journal of Combinatorics 30(2), #P2.45 (2023). https://doi.org/10.37236/11525
