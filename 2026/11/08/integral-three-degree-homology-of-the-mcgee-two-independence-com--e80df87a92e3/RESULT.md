# Integral three-degree homology of the McGee two-independence complex

## Finding
Let \(M\) be the McGee graph, the unique smallest cubic graph of girth seven. For its first higher-independence complex \(X=\operatorname{Ind}_2(M)\), the reduced integral homology is
\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z^5,&j=7,\\
\mathbb Z,&j=8,\\
\mathbb Z^2,&j=9,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular the three adjacent positive-dimensional groups are torsion-free and the ordinary Euler characteristic is \(\chi(X)=-5\). This is an exact integral **homology** classification; it does not assert that the space is a wedge of spheres.

## Assumptions and scope
Use vertex set \(\{0,1,\ldots,23\}\), all cyclic edges \(\{i,i+1\pmod{24}\}\), and the undirected chords \(\{i,i+s_i\pmod{24}\}\) with the repeating offset sequence \((s_i)=(12,7,-7)^8\). Duplicate undirected descriptions count as one edge. The code checks that this is a simple graph with \(24\) vertices, \(36\) edges, degree three throughout and girth seven. The offset \(12\) is the same as \(-12\) modulo \(24\), agreeing with the classical LCF specification.

A face of \(X\) is a vertex set \(F\) for which the induced subgraph \(M[F]\) has every connected component of order at most two. Equivalently, every induced degree is at most one, or the induced subgraph contains no three-vertex path as a subgraph. The empty face belongs to the simplicial complex but is not included as a vertex of its ordinary nonempty face poset for discrete Morse matching. All homology groups are reduced and taken over the integers.

## Proof
First enumerate every nonempty face by inserting vertices in ascending order. Inserting \(v\) is valid if it has no previously inserted neighbor, or exactly one previously inserted neighbor whose current induced degree is zero. This is a necessary and sufficient inductive condition for the induced maximum degree to stay at most one. The enumeration produces exactly \(553301\) nonempty faces, with face vector (dimension zero through twelve)
\[
(24,276,1952,9306,31080,73624,122944,141457,107504,50448,13112,1542,32).
\]
An independently written degree-count predicate checks each face; every positive-dimensional face has all codimension-one faces in the enumeration.

Apply sequential elementary vertex matchings. For any fixed permutation \(v_1,\ldots,v_{24}\), at step \(k\) pair every currently unmatched face \(F\) avoiding \(v_k\) with \(F\cup\{v_k\}\), whenever the latter remains unmatched. The union is an acyclic face-poset matching (the sequential element-matching proposition), and the attached verifier additionally establishes its acyclicity directly by examining **every** oriented covering incidence and completing a topological sort.

For the order visiting the residue classes modulo three in turn (\(0,3,\ldots,21,1,4,\ldots,22,2,5,\ldots,23\)), there are \(276632\) matched pairs and only \(37\) critical faces: one vertex, five dimension-seven faces, fifteen dimension-eight faces and sixteen dimension-nine faces. By Forman's discrete Morse theorem, \(X\) has the homotopy type of a CW complex with exactly these cells and no other positive-dimensional cells.

The signed cellular Morse boundary is calculated **over \(\mathbb Z\)** by eliminating each matched codimension-one incidence, which has coefficient \(\pm1\). The recursive gradient-reduction rule, with signs determined by ascending vertex order, is implemented explicitly in `verify_mcgee.py`. The resulting boundary \(\partial_8:\mathbb Z^{15}\to\mathbb Z^5\) is zero. The boundary \(\partial_9:\mathbb Z^{16}\to\mathbb Z^{15}\) has Smith normal form with fourteen unit diagonal entries and the remaining entries zero. Thus \(\operatorname{rank}\partial_9=14\), its image is a primitive sublattice, and there is no torsion. The exact homology ranks are consequently \(5\) in degree seven, \(15-14=1\) in degree eight, and \(16-14=2\) in degree nine.

The independent ascending vertex order yields another acyclic matching with critical counts \((1,7,21,20)\) in degrees \((0,7,8,9)\). Its integer boundaries have Smith invariant lists \((1,1)\) for \(\partial_8\) and eighteen unit entries for \(\partial_9\). Thus it separately reproduces the same reduced integral homology, including torsion freeness. The original simplicial Euler characteristic is \(-5\), agreeing with the homology alternating sum. These two exact integral reductions prove the assertion. A finite enumeration is a complete proof here because the theorem concerns one explicitly specified finite graph.

## Verification
Run `python3 verify_mcgee.py` with Python and SymPy. It reconstructs the graph and simplicial complex rather than reading a precomputed face list; verifies all \(553301\) face memberships independently; verifies all face-down closures; constructs two complete acyclic matchings; examines all \(4268208\) codimension-one incidences for each matching; topologically sorts the oriented diagram; computes the signed Morse boundaries; and checks their integer Smith normal forms and the chain relation. The separately embedded `verification_output.txt` records both proofs and concludes `ALL_CHECKS_PASS`. The verification script is a standalone reproducible finite certificate; it invokes no network service.

## Relationship to prior work
Taylan's archive-era work on matching trees and graph-devoid complexes (first public version January 27, 2015) studies path-, cycle- and forest-based devoid complexes and general Morse methods. The present face condition is its three-vertex-path-devoid instance on a cubic girth-seven cage, not a covered graph family. Deshpande and Singh later formalized general higher-independence complexes and proved the sequential element-matching proposition used here, while their classifications concern complete multipartite, fully whiskered, path, cycle and perfect-tree graphs.

A published earlier computation for the **same McGee graph** establishes \(\operatorname{Ind}_1(M)\simeq S^5\). That ordinary independence complex excludes every edge, whereas \(\operatorname{Ind}_2(M)\) permits isolated edges. Its five-sphere homotopy type therefore does not determine this larger complex's three-degree integral homology. The indexed prior item has opaque identifier `5daca7995d97` and title *The McGee graph independence complex is a five-sphere*. Searches of the graph name, cubic-cage aliases, dissociation-complex and three-vertex-path-devoid terminology, and published mathematical records found no prior theorem computing these groups; absence of a match is not a proof of universal novelty.

## Limitations
The statement treats only the first higher-independence parameter for the McGee graph, not arbitrary cubic cages, other graph-complex functors or the full homotopy type. A wedge decomposition is **not** claimed: integral homology and a small CW model alone do not rule out unstable attaching maps. The lack of an identified covering result does not exclude equivalent work in unindexed or inaccessible sources. The scientific review is not independent validation.

## References
- D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1, publicly submitted 2015-01-27. https://arxiv.org/html/1501.06754v1
- P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first public 2020-01-15; especially Proposition 2.10. https://arxiv.org/html/2001.05448v2
- W. F. McGee, *A Minimal Cubic Graph of Girth Seven*, Canadian Mathematical Bulletin 3 (1960), 149–152, doi:10.4153/CMB-1960-018-1.
- E. W. Weisstein, *McGee Graph*, MathWorld; the classical LCF representation. https://mathworld.wolfram.com/McGeeGraph.html
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
