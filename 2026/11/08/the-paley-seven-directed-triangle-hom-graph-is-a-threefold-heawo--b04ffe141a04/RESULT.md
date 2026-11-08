# The Paley-seven directed triangle Hom graph is a threefold Heawood cover

## Finding
Let \(T\) be the seven-vertex Paley tournament with vertices \(\mathbb Z/7\mathbb Z\) and arrows \(a\to b\) exactly when \(b-a\in\{1,2,4\}\) modulo seven. Let \(X=\operatorname{Hom}(\overrightarrow C_3,T)\) be the directed multihomomorphism complex, with source cycle \(0\to1\to2\to0\). The cyclic permutation of the three source coordinates is a free cellular \(C_3\)-action on \(X\). The complex is a connected cubic graph with 42 vertices and 63 edges, and its quotient by this action is exactly the Heawood graph, the point-line incidence graph of the Fano plane. The quotient map is a connected regular three-sheeted graph covering. Consequently
\[
X\simeq\bigvee^{22}S^1,\qquad H_1(X;\mathbb Z)\cong\mathbb Z^{22}.
\]
Writing \(\zeta_3\) for a primitive cube root of unity, the deck action on rational first homology has the exact decomposition
\[
H_1(X;\mathbb Q)\cong\mathbb Q^{8}\oplus\mathbb Q(\zeta_3)^{7}
\]
as a \(\mathbb Q[C_3]\)-module. The character at the identity and either nontrivial deck transformation is \((22,1,1)\).

## Assumptions and scope
The directed Hom complex is the regular polyhedral complex of triples \((A,B,C)\) of nonempty subsets of \(\mathbb Z/7\mathbb Z\) with every arrow \(A\to B\), \(B\to C\), and \(C\to A\); a cell is \(\Delta(A)\times\Delta(B)\times\Delta(C)\) of dimension \(|A|+|B|+|C|-3\). The deck generator is \((A,B,C)\mapsto(B,C,A)\). The homotopy and integral homology statements refer to the ordinary topological realization, while the representation statement is rational. No claim is made about all tournaments on seven vertices, higher Paley orders, or the full automorphism group of the covering graph.

## Proof
**Cell dimensions.** The Paley tournament has outneighborhoods \(a+\{1,2,4\}\). For any distinct \(a,b\), direct checking of the six nonzero differences shows that the two vertices have exactly one common outneighbor and one common inneighbor. If one coordinate set in a directed multihomomorphism has at least two elements, the next and preceding coordinate sets must therefore each be singletons. Hence no cell has dimension at least two. For any fixed directed edge \(b\to c\) there are exactly two possible values of \(a\) completing \(a\to b\to c\to a\); the same holds cyclically. There are six ordered triples of nonzero differences \((x,y,z)\in\{1,2,4\}^3\) summing to zero modulo seven: the permutations of \((1,2,4)\). For each of seven initial vertices this yields one vertex of \(X\). Thus there are 42 vertices, each of degree three (replace each of the three coordinates by its unique alternative), and therefore 63 edges.

**Heawood quotient.** Rotation of the source coordinates has order three and is free on vertices and edges. Each orbit of directed three-cycles is determined by the underlying three-element target set. There are two collections of seven sets, with \(a\) ranging over \(\mathbb Z/7\mathbb Z\):
\[
A_a=a+\{0,1,3\},\qquad B_a=a+\{0,1,5\}.
\]
Distinct sets in either collection intersect in exactly one point. Two cyclic triangles are adjacent in the quotient precisely when their target three-sets intersect in two points: their shared directed edge can be brought to the same two source coordinates by cyclic rotation, and the third coordinate is then the unique replacement. A direct difference-set check gives
\[
|A_a\cap B_b|=2\quad\Longleftrightarrow\quad b-a\in\{0,2,3\}\pmod7.
\]
The set \(\{0,2,3\}\) has six ordered nonzero differences, each nonzero residue occurring exactly once. Thus \(A_a\) can be regarded as the seven points and \(B_b\) as the seven lines of the cyclic Fano plane, with the displayed relation as incidence. Their bipartite incidence graph is the Heawood graph. Each vertex of \(X\) has three neighbors with different quotient images; consequently the quotient map is a three-sheeted graph covering, not merely a quotient of abstract graphs.

**Connectedness.** The standalone verifier constructs all 42 directed cyclic triples and the 63 adjacency edges using the all-arrows condition; a complete breadth-first search from \((0,1,3)\) produces 41 spanning-tree edges covering every vertex. Because this is an explicit finite graph defined above, the fully enumerated spanning-tree check proves connectedness (it is not a statistical sample). The deck-transformation group therefore acts as the full deck group of a connected regular three-sheeted cover.

**Homotopy and character.** A connected finite graph with 42 vertices and 63 edges has a spanning-tree collapse to \(63-42+1=22\) circles. For a free finite cellular action, rational transfer identifies the invariant homology of the cover with homology of its quotient. The Heawood graph has 14 vertices and 21 edges, so \(\dim H_1(X;\mathbb Q)^{C_3}=21-14+1=8\). Apart from the trivial representation, the only irreducible rational representation of \(C_3\) is \(\mathbb Q(\zeta_3)\), of dimension two. Dimension 22 consequently forces seven copies. Equivalently, neither nontrivial deck transformation fixes any cell of degree zero or one, so its Lefschetz number is zero and its trace on \(H_1\) is one, agreeing with the decomposition.

## Verification
Execute `python3 verify_cover.py` from the same directory. The standalone verifier checks all permissible Hom cells, the 42/63 face counts, every adjacency, the 41-edge spanning tree, the free rotation action and three-sheeted local covering condition, both seven-set difference systems, all 21 Heawood incidences, the quotient and homology-character arithmetic. `verification_output.txt` records an actual matching successful execution. Only Python's standard library is required.

## Relationship to prior work
Dochtermann and Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, first public version arXiv:2108.10948v1 (2021-08-24), define these directed Hom complexes and analyze examples and connectivity. Their Figure 4 presents a different seven-vertex tournament whose directed triangle Hom complex is a Möbius strip. They do not present a three-sheeted Heawood cover for the quadratic-residue tournament used here. The distinct published computation of \(\operatorname{Hom}(\overrightarrow C_3,R_9)\) concerns a different regular cyclic tournament, while the accessible Paley-eleven computation concerns a different target and has integral torsion. The quotient relation above explains the role of Fano's difference-set incidence more precisely than the raw first Betti number. No checked stronger statement implies this graph covering or its deck homology representation.

## Limitations
This result is a finite, exactly enumerated case; it does not establish an all-orders Paley theorem. The covering need not split equivariantly as a wedge of circles, and no integral decomposition of the \(C_3\)-lattice beyond its rank is asserted. Bibliographic searches cannot exclude all unpublished or unindexed equivalent results. Independent external validation has not been performed.

## References
- A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948v1 (2021-08-24), https://arxiv.org/abs/2108.10948.
- The Heawood graph is the incidence graph of the unique projective plane of order two (the Fano plane); its seven-point difference-set presentation is explicitly proved above.
