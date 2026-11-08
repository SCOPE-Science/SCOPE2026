# Integral multipath homology of the bidirected triangular prism

## Finding
Let \(P=C_3\square K_2\) be the triangular-prism graph. The bidirected digraph \(D=\overleftrightarrow P\) has both orientations of every undirected edge. Its multipath complex \(X(D)\) has reduced integral homology
\[
\widetilde H_i(X(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z^5,&i=2,\\
\mathbb Z^{22},&i=3,\\
\mathbb Z^6,&i=4,\\
0,&\text{otherwise}.
\end{cases}
\]
All groups are torsion-free. This computes the missing triangular-prism instance needed to distinguish multipath homology between the two connected cubic graphs on six vertices. No homotopy wedge decomposition is asserted.

## Assumptions and scope
Number the vertices of \(P\) by \(0,1,2,3,4,5\). Its nine edges are the three edges of each triangle on \(\{0,1,2\}\) and \(\{3,4,5\}\), together with the three rungs \(\{0,3\},\{1,4\},\{2,5\}\). Each edge supplies both directed arcs; sort the edges lexicographically within each of those groups and list each arc in the order \((u,v),(v,u)\). This fixes all chain signs and enumeration indexes in the certificate.

A multipath is an arc subset satisfying: every vertex has indegree and outdegree at most one, and the selected directed graph has no directed cycle, including two-cycles. Isolated vertices are permitted. Its nonempty arc subsets are simplices, and the empty arc set is the empty simplex. We use the augmented reduced simplicial chain complex over \(\mathbb Z\), with simplicial orientation induced by the listed arc order.

## Proof
**Finite enumeration.** Enumerate all \(2^{18}=262144\) subsets of the directed arcs. One test checks an explicit partial successor map for absence of repeated vertices; an independent test maintains in/out degrees and uses disjoint-set union to reject every cyclic edge addition. These tests agree on precisely \(687\) faces including the empty face. The nonempty face numbers in dimensions \(0,1,2,3,4\) are \(18,108,260,240,60\), respectively. Thus the complex has dimension four.

**Integral algebraic Morse reduction.** Process arc coordinates successively, matching each available face not containing an arc to its corresponding available coface containing the arc, and remove the pair before the next coordinate. For ascending-coordinate order the matching has \(323\) pairs. Orient unmatched Hasse edges downward and matched edges upward. Explicit topological sorting visits all \(687\) face nodes and certifies acyclicity among exactly \(2274\) Hasse incidences. Reversing the coordinate order gives a second independent matching with the same counts and complete acyclicity. These matching operations include the augmented empty face.

Apply signed algebraic elementary cancellations over \(\mathbb Z\) in the recorded pair order. Every pivot is \(+1\) or \(-1\); the resulting reduced chain complex has \(9\) cells in degree two, \(26\) in degree three and \(6\) in degree four, and no other critical cells. Both cancellations produce a zero map \(\partial_4\) and a rank-four map \(\partial_3:\mathbb Z^{26}\to\mathbb Z^9\). For the ascending order, the determinant of the submatrix with zero-indexed rows \(0,1,4,5\) and columns \(4,9,10,13\) is \(-1\). Because this is a maximal-rank integral minor, every nonzero Smith invariant factor equals one. Consequently, the cokernel is \(\mathbb Z^5\), the kernel is \(\mathbb Z^{22}\), and the fourth homology is \(\mathbb Z^6\); all other reduced groups vanish. Integral unit pivots make these homology isomorphisms valid over \(\mathbb Z\), not merely over a field.

**Natural comparison.** The complement of any simple cubic graph on six vertices is simple two-regular. A two-regular graph on six vertices is either \(C_6\) or two disjoint triangles. Taking complements yields exactly the triangular prism and \(K_{3,3}\). A separate already-known calculation for the bidirected \(K_{3,3}\) gives homology in degrees three and four but none in degree two; this comparison is not claimed as a new result. The prism's five degree-two classes distinguish the two instances.

## Verification
Run `python3 verify_six_cubic.py CERTIFICATE.json` using only the Python standard library. The script recomputes all faces using two predicates, both acyclic matchings and their signed integral Morse boundary matrices, exact rational ranks, the unit minor by fraction-free determinant, and ordinary (unreduced) simplicial boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\). It compares its entire reconstructed signed-matrix certificate to `CERTIFICATE.json`. The expected output is recorded in `VERIFY_OUTPUT.txt` and ends with `SIX_VERTEX_CUBIC_MULTIPATH_INTEGRAL_HOMOLOGY_VERIFIED`. The second graph is checked solely to safeguard the comparison; the triangular-prism assertion is the new finding.

The reduced Euler characteristic from the simplex counts is \(-11\), also equal to \(5-22+6=-11\).

## Relationship to prior work
Caputi, Collari, Di Trani and Smith define this complex and give homotopy and enumerative results for directed paths, polygons, certain grids, transitive tournaments, and alternating-oriented complete bipartite graphs [1]. Those graph families and orientations do not cover the bidirected triangular prism. The later bidirectional-path-and-polygon results [2] concern graphs of maximum degree two, whereas the prism is cubic. The quiver-minor matching comparison [3, Theorem 1.2] requires a directed graph without oriented cycles; here the two arcs on every undirected edge already form a directed two-cycle. The classical cycle-free chessboard complex [4] uses the complete directed graph; the present complex is its restriction to the prism's 18 arcs, for which the unrestricted homology does not determine the restriction's homology. The pre-existing bidirected \(K_{3,3}\) homotopy calculation is not included in this novelty claim. A graph discrete-Morse complex, despite sharing the name “triangular prism,” is a different simplicial complex from this directed-arc multipath complex.

## Limitations
This proves integral homology and torsion-freeness for one natural finite graph, not the full integral homotopy type, a homology representation under automorphisms, or a general formula for cubic graphs of arbitrary size. Finite computations are exhaustive for the specified 18 arcs only. Existing unindexed calculations may overlap; novelty is assessed against inspected primary literature and searched records, not asserted as an absolute literature theorem. Independent audit has not been performed.

## References
[1] L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (public 2022-08-09), https://arxiv.org/abs/2208.04656.

[2] L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, https://arxiv.org/abs/2601.05670.

[3] L. Caputi, C. Collari, E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1, https://arxiv.org/abs/2401.01248.

[4] S. T. Vrećica and R. T. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252, https://arxiv.org/abs/0710.5252.
