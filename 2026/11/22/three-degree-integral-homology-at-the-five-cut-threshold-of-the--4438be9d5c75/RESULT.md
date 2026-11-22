# Three-degree integral homology at the five-cut threshold of the \(3\times4\) rook graph

## Finding
Let \(R=K_3\square K_4\) be the twelve-vertex rook graph: vertices are \((a,b)\in\{0,1,2\}\times\{0,1,2,3\}\), with two distinct vertices adjacent precisely when they share a coordinate. Let \(\Delta_5(R)\) be the **ordinary** five-cut complex, with facets the complements of five-vertex subsets whose induced subgraphs are disconnected. Then its complete reduced **integral** homology is
\[
\widetilde H_i(\Delta_5(R);\mathbb Z)\cong
\begin{cases}
\mathbb Z^8,&i=4,\\
\mathbb Z^5,&i=5,\\
\mathbb Z^{36},&i=6,\\
0,&\text{otherwise}.
\end{cases}
\]
The complex is pure of dimension six but is neither shellable nor Cohen–Macaulay over any field. This is an additive integral homology classification; a sphere-wedge homotopy decomposition is **not** asserted.

## Assumptions and scope
The graph is simple, undirected, and unweighted. Give vertex \((a,b)\) the integer label \(4a+b\), from zero to eleven. An induced five-set is disconnected when breadth-first search on the five selected vertices finds at least two components. Each disconnected five-set \(D\) determines the seven-element facet \(V(R)\setminus D\) of \(\Delta_5(R)\). Thus the complex consists exactly of all subsets of these facets. All homology groups are those of its finite geometric realization, with coefficients in \(\mathbb Z\). No assumption of a particular geometric embedding of the graph is made.

## Proof
**1. Complete defining-facet enumeration.** There are \(\binom{12}{5}=792\) potential five-sets. An exhaustive, independently reproducible connectivity test finds exactly 264 disconnected induced five-sets. The complex, reconstructed from the complements of **these** sets rather than from the sets themselves, has a total of 2,489 faces including the empty face. Its face counts indexed by cardinality zero through seven are
\[
(1,12,66,220,492,768,666,264).
\]
In particular, every facet contains seven vertices; the complex is pure six-dimensional.

**2. An acyclic integral Morse reduction.** Encode each face by a twelve-bit mask. Perform successive single-vertex matchings using the fixed vertex sequence
\[
(8,7,0,10,5,1,6,9,3,2,11,4).
\]
For each vertex in that sequence, traverse the currently unmatched nonempty faces in increasing order of cardinality and then integer mask. When a face \(F\) and \(F\cup\{v\}\) are both unmatched and \(v\notin F\), match them as a codimension-one pair and remove both. This deterministic rule produces 1,218 pairs and leaves precisely one critical zero-cell, nine critical four-cells, six critical five-cells, and 36 critical six-cells. The prescribed orientation of the entire nonempty face-poset Hasse graph—downward on unmatched incidences and upward on matched incidences—has an explicit topological ordering of all 2,488 vertices, checked by the standalone program. Therefore no directed cycle exists, and the pairs form a valid acyclic discrete-Morse matching over \(\mathbb Z\).

**3. Signed integral boundary computation.** Orient a simplex by increasing vertex labels. Deleting its vertex in position \(j\), starting at zero, has incidence \((-1)^j\). For a face \(c\), define its projection \(P(c)\) onto the critical cells of its dimension recursively. If \(c\) is critical, set \(P(c)=c\); if it is an upper matched face, set \(P(c)=0\). If it is a lower matched face with upper partner \(h\), set
\[
P(c)=-[c:\partial h]^{-1}\!\sum_{\substack{d\subset h,\ |d|=|c|\\d\ne c}}[d:\partial h]P(d).
\]
All incidences used as denominators are \(\pm1\). Acyclicity makes this recursion terminate, and elementary cellular cancellation identifies the resulting signed boundary of each critical cell with the exact integral Morse differential. There are no critical cells in dimensions one, two, or three. The boundary from critical five-cells to critical four-cells, in the deterministically sorted critical bases, is
\[
B_5=\begin{pmatrix}
0&0&0&0&0&0\\
0&1&0&1&0&0\\
0&-1&0&-1&0&0\\
0&0&0&0&0&0\\
0&0&0&0&0&0\\
0&0&0&0&0&0\\
0&-1&0&-1&0&0\\
0&-1&0&-1&0&0\\
0&-1&0&-1&0&0
\end{pmatrix}.
\]
The boundary from the 36 critical six-cells to the six critical five-cells is the zero matrix. Thus the only nonzero integral Smith invariant factor is a single \(1\), in \(B_5\), and no torsion can occur. The Morse chain complex therefore has reduced homology of ranks \(9-1=8\), \(6-1=5\), and \(36\) in dimensions four, five and six respectively, with no other reduced homology. This proves the displayed classification.

**4. Independent consistency check and topological consequences.** Direct enumeration of the original simplicial boundary matrices over \(\mathbb F_2\), without use of Morse cancellation, gives ranks 11, 55, 165, 327, 433 and 228 in dimensions one through six. The resulting mod-two Betti numbers in positive degrees are exactly eight, five and 36 in degrees four, five and six. The face-vector Euler characteristic also gives \(8-5+36=39\), as required. These checks are independent corroboration; the integral acyclic matching and unit Smith invariant establish the integral assertion. Since a pure shellable six-complex has reduced homology concentrated in dimension six, its nonzero fourth homology rules out shellability. Reisner's necessary vanishing condition similarly rules out Cohen–Macaulayness over every field.

## Verification
Run `python3 evidence/verify.py` with standard Python 3 and no third-party packages. It constructs all 792 five-subsets, determines the 264 disconnected ones from the adjacency predicate, reconstructs every face of the **ordinary cut complex**, verifies the matching over every nonempty face-poset Hasse incidence, computes the signed integral Morse matrices from the matching, and independently calculates the complete original mod-two boundary ranks. The expected output is reproduced in `evidence/CHECK_OUTPUT.txt`. All finite cases defining this single graph and threshold are checked exhaustively; this is not a sample-based argument.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced ordinary cut complexes in *Topology of Cut Complexes of Graphs* (arXiv:2304.13675). Its graph families include complete multipartite graphs and clique prisms \(K_n\square K_2\); its clique-prism result (Theorem 7.18) concerns a two-row graph rather than the three-row, four-column rook graph. *Topology of Cut Complexes II* (arXiv:2407.08158) concerns disjoint unions, squared paths and Cartesian **path grids** \(P_m\square P_n\), not Cartesian products of two complete graphs. In particular, the induced triangles in \(K_3\square K_4\) are absent from the path grid \(P_3\square P_4\).

Related published rook-graph calculations determine ordinary **three-cut** homology for general boards and ordinary **four-cut** homology for the \(4\times4\) board. The latter has homology only in dimensions ten and eleven; neither result implies the five-cut groups for the different twelve-vertex board. The three-row four-cut classification concerns the preceding cut parameter and does not imply the five-cut boundary operators. A targeted source search under both rook-graph and line-graph/Hamming-graph terminology did not uncover an equivalent five-cut calculation; absence from inspected sources is not a uniqueness theorem.

## Limitations
The theorem covers only the ordinary five-cut complex of \(K_3\square K_4\). It does not provide the full homotopy type, Steenrod operations, an automorphism representation, or a uniform formula for all \(K_3\square K_n\). Nonzero ranks across three dimensions do not by themselves imply a wedge of spheres, and no such assertion is used. The originality assessment is relative to the inspected literature and searchable indexed records; an unindexed equivalent remains possible. No independent external mathematical audit is claimed.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public 26 April 2023, especially Sections 1 and 7.3. https://arxiv.org/abs/2304.13675
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first public 11 July 2024, especially Sections 1 and 5. https://arxiv.org/abs/2407.08158
3. *Integral four-cut homology separates the Shrikhande and rook graphs*, published 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-four-cut-homology-separates-the-shrikhande-and-rook-gra--de2f98e55b1f
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145. The acyclic matching theorem underpins the integral chain reduction.
