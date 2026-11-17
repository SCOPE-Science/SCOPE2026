# Integral multipath homology of the bidirected three-cube

## Finding

Let \(Q_3\) be the graph on the eight binary triples, with two vertices adjacent when they differ in exactly one coordinate. Replace each undirected edge by both directed arcs, obtaining the digraph \(D=\overleftrightarrow{Q_3}\). Write \(X(D)\) for the multipath complex: its vertices are the 24 arcs of \(D\), and its simplices are arc sets inducing vertex-disjoint directed simple paths (isolated graph vertices are allowed).

Its complete reduced **integral** homology is
\[
\widetilde H_i(X(D);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{6},& i=3,\\
\mathbb Z^{45},& i=4,\\
\mathbb Z^{36},& i=5,\\
\mathbb Z^{12},& i=6,\\
0,&\text{otherwise}.
\end{cases}
\]
Every integral homology group is torsion-free. This natural 24-arc, three-dimensional cubical example has nonzero homology in four consecutive degrees. Its reduced Euler characteristic is \(15\).

## Assumptions and scope

The graph is the *ordinary* undirected three-cube with all edges replaced by two opposite arcs, not an acyclic orientation of the cube and not the cube's matching or graph-Morse complex. An allowed arc subset must have indegree at most one and outdegree at most one at every vertex, and it must contain **no directed cycle** (including a directed two-cycle). These conditions are equivalent to every component being a directed simple path. All chain complexes are augmented simplicial chains over \(\mathbb Z\), so the degree-minus-one generator is the empty face and degree-zero boundaries are augmentations. Every result here concerns this single eight-vertex digraph; no infinite family is classified.

## Proof

Index graph vertices by integers \(0,\ldots,7\), interpreted as three-bit binary strings. Order arcs lexicographically by their ordered endpoints, retaining \((a,b)\) precisely when \(a\oplus b\) has Hamming weight one. There are 24 arcs. Encode an arc set by the corresponding 24-bit mask. Every admissible arc set is a disjoint union of directed paths, so it has at most seven arcs. Thus examining every choice of at most seven arcs exhausts the complex, with no unexamined larger faces.

An independent combination-by-combination validity test and a recursive path-extension enumerator agree on the full set of \(6{,}497\) faces, including the empty face. The counts in dimensions \(-1,0,1,2,3,4,5,6\) are respectively
\[
(1,24,216,928,2016,2160,1008,144).
\]
There are \(534\) facets: \(6\), \(48\), \(336\), and \(144\) in respective dimensions \(3,4,5,6\). In particular, the complex is nonpure.

Construct an augmented acyclic face pairing by scanning the 24 arc coordinates in ascending order and pairing every still-unpaired face not containing the current arc with its still-unpaired extension containing that arc. Each pair has codimension one. Exhaustively orienting all \(29{,}160\) Hasse incidences downward except the paired incidences (oriented upward), and topologically sorting the resulting digraph, visits all \(6{,}497\) faces. Thus the pairing is acyclic. It has exactly \(3{,}193\) pairs and leaves the critical chain ranks
\[
\operatorname{rank} C^{\mathrm M}_3=8,\qquad
\operatorname{rank} C^{\mathrm M}_4=51,\qquad
\operatorname{rank} C^{\mathrm M}_5=40,\qquad
\operatorname{rank} C^{\mathrm M}_6=12.
\]
There are no other critical cells, including no negative-dimensional critical cell, because the empty face is paired. The resulting algebraic Morse chain complex computes the reduced integral simplicial homology.

Build the *signed* simplicial differential, using the increasing arc order and coefficient \((-1)^j\) upon deleting the arc in position \(j\). For each matched pair \((\ell,u)\), the coefficient of \(\ell\) in \(\partial u\) is a unit \(\pm1\). Apply exact integral chain cancellation: for every other boundary column containing \(\ell\), subtract the appropriate multiple of \(\partial u\), and then remove the paired generators from the adjacent chain degrees. All cancellation pivots are verified to remain units. After cancellation the only potentially nonzero reduced differentials are
\[
\partial^{\mathrm M}_4:\mathbb Z^{51}\to\mathbb Z^{8},\qquad
\partial^{\mathrm M}_5:\mathbb Z^{40}\to\mathbb Z^{51},\qquad
\partial^{\mathrm M}_6:\mathbb Z^{12}\to\mathbb Z^{40}.
\]
Exact unimodular row/column elimination leaves precisely two unit Smith factors for \(\partial^{\mathrm M}_4\), four unit factors for \(\partial^{\mathrm M}_5\), and a zero \(\partial^{\mathrm M}_6\). The other differentials vanish. No nonunit invariant factor survives; therefore all homology is torsion-free, and the group ranks in dimensions \(3,4,5,6\) are respectively \(8-2=6\), \(51-2-4=45\), \(40-4=36\), and \(12\).

The same complete argument is independently repeated with the **reverse arc order** for selecting matching coordinates; the two matchings have the same critical ranks and exact Smith data. In addition, an unrelated direct sparse simplicial-boundary elimination over each of \(\mathbb F_2\) and \(\mathbb F_3\) gives boundary ranks \((1,23,193,735,1275,840,132)\) from degrees zero through six. The field ranks agree with the integral Morse calculation and exclude errors in face enumeration or boundary indexing at those primes. The integral unimodular calculation, not the finite-field comparisons, is what excludes torsion at *every* prime.

## Verification

Run the accompanying Python 3 standard-library script `verify_cube_multipath.py` from a clean directory, without any input files. It builds both face lists from the graph definition, proves they coincide by exhaustive comparison, checks the directed Hasse graph for each matching, reconstructs every signed differential and exact cancellation, checks that each residual differential squares to zero, and diagonalizes its integer boundary matrices exclusively via unimodular pivots. The exact recorded stdout is in `verification_output.txt`. The last line must be `INTEGRAL_CUBE_MULTIPATH_HOMOLOGY_VERIFIED`.

The script separately enumerates \(12\) directed Hamiltonian cycles of the cube, corroborating the twelve top-degree homology generators. The novel lower-degree computation is unaffected by that independent top-dimensional count.

## Relationship to prior work

Caputi–Collari–Di Trani–Smith, *On the homotopy type of multipath complexes* (first posted 2022-08-09; arXiv:2208.04656), defines the multipath complex and computes specific directed paths, polygons, oriented strips, and transitive tournaments; the explicit theorems inspected do not calculate this fully bidirected three-cube. Caputi–Collari–Ramos (arXiv:2401.01248) proves general finiteness and bounded-torsion phenomena under minor restrictions and obtains matching-complex identifications for **acyclic** digraphs, not this digraph, which has directed two-cycles. Caputi–Collari–Smith (arXiv:2601.05670) computes bidirectional paths and polygons, a different graph family. Vrećica–Živaljević (arXiv:0710.5252) introduces cycle-free chessboard complexes and broad connectivity methods; its complete-digraph and generalized chessboard statements do not furnish these lower-degree cube groups.

Results about the ordinary edge-matching complex of the undirected cube or the graph's discrete-Morse matching complex concern different simplicial complexes. A known general Hamiltonian-cycle description accounts for the top degree, but not for the three lower groups or their integral torsion-freeness. The claim of additional information here is the **complete integral homology in degrees three through five**, together with the full fixed-object classification.

## Limitations

No assertion is made about a wedge-of-spheres homotopy type, higher attaching maps, equivariant homology representations, or other cube dimensions. Equality of homology groups does not establish homotopy equivalence. The proof uses a finite exhaustive certificate rather than a uniform formula in cube dimension. The literature comparison includes primary text and research-record searches, but unindexed equivalent calculations cannot be excluded without independent specialist review.

## References

1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first posted 2022-08-09), DOI 10.1112/mtk.12235.
2. L. Caputi, C. Collari, E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248 (first posted 2024-01-02).
3. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (first posted 2026-01-09).
4. S. T. Vrećica, R. T. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252 (2007).
