# Arithmetic rigidity at the minimal eight-face face-neighbourly level
## Finding
Let \(P\) be a closed connected orientable polyhedral surface with exactly eight faces \(F_1,\ldots,F_8\). Assume that every face is a simple \(k\)-gon, exactly three faces meet at every vertex, and every two distinct faces share at least one edge. For \(i<j\), let \(e_{ij}\) be the number of edges common to \(F_i\) and \(F_j\).

Then
\[
3\mid k,\qquad k\ge 9,\qquad E=4k,\qquad V=\frac{8k}3,
\]
and the orientable genus is
\[
g=\frac{2k}3-3.
\]
Moreover the total repeated-adjacency surplus is
\[
D:=\sum_{1\le i<j\le8}(e_{ij}-1)=4k-28\ge 8.
\]
Thus the smallest possible equivelar face size is \(k=9\), and this happens exactly when
\[
(F,E,V,g)=(8,36,24,3),\qquad D=8.
\]
In that minimal case every face satisfies the local identity
\[
\sum_{j\ne i}(e_{ij}-1)=2.
\]

If, in addition, every pair of faces shares at most two edges, define the doubled-pair graph \(G_2\) on the eight faces by joining \(i\) and \(j\) exactly when \(e_{ij}=2\). Then every vertex of \(G_2\) has degree \(2\). Hence \(G_2\) is a disjoint union of simple cycles, and the only possible cycle-size partitions of eight are
\[
8,\qquad 5+3,\qquad 4+4.
\]
Röst and Vígh's 2026 polyhedron has doubled-pair graph consisting of two \(4\)-cycles, while Mizhaev's 2026 integer realization has one \(8\)-cycle. Therefore \(5+3\) is the unique remaining doubled-pair cycle type permitted by these minimal incidence constraints among the three possibilities. No existence claim for the \(5+3\) type is made.

## Assumptions and scope
A closed polyhedral surface is used in the standard incidence sense: every edge belongs to exactly two distinct faces and the vertex links are circles. Equivelar type \(\{k,3\}\) means all faces have \(k\) edges and exactly three faces meet at every vertex. Orientability is used only to translate the Euler characteristic into a genus.

The doubled-pair classification assumes \(e_{ij}\le2\) for every face pair. Without that extra hypothesis the same counting still forces weighted excess degree \(2\) at every face when \(k=9\), but a pair sharing three edges would contribute multiplicity two and the simple-cycle conclusion would no longer follow.

The theorem is combinatorial. It does not claim that every admissible cycle type has a realization by planar polygonal faces in \(\mathbb R^3\), and it does not classify embeddings or geometric symmetries.

## Proof
Counting face-edge incidences gives
\[
8k=2E,
\]
so \(E=4k\). Counting vertex-edge incidences in a trivalent surface gives
\[
3V=2E=8k,
\]
so \(V=8k/3\). Since \(V\) is an integer, \(3\mid k\).

There are \(\binom82=28\) unordered pairs of distinct faces. Face-neighbourliness gives \(e_{ij}\ge1\) for every pair. Every edge belongs to exactly one unordered pair of incident faces, hence
\[
E=\sum_{i<j}e_{ij}\ge28.
\]
Thus \(4k\ge28\), so \(k\ge7\). Combined with \(3\mid k\), this forces \(k\ge9\).

Euler's formula and orientability now give
\[
2-2g=V-E+F=\frac{8k}3-4k+8=8-\frac{4k}3,
\]
whence
\[
g=\frac{2k}3-3.
\]

Subtracting one mandatory shared edge for each of the \(28\) face pairs yields
\[
D=\sum_{i<j}(e_{ij}-1)
 =\sum_{i<j}e_{ij}-28
 =E-28
 =4k-28.
\]
Because \(k\ge9\), \(D\ge8\), with equality if and only if \(k=9\). At \(k=9\), the preceding formulas give \(E=36\), \(V=24\), and \(g=3\).

Fix a face \(F_i\) in the minimal case. Its \(9\) boundary edges are each paired with exactly one other face, so
\[
\sum_{j\ne i}e_{ij}=9.
\]
There are seven other faces and each contributes at least one. Hence
\[
\sum_{j\ne i}(e_{ij}-1)=9-7=2.
\]
If every \(e_{ij}\le2\), each summand is either \(0\) or \(1\). Therefore every vertex in the doubled-pair graph has ordinary degree \(2\). A finite simple \(2\)-regular graph is a disjoint union of cycles, each of length at least three. The partitions of eight into integers at least three are exactly \(8\), \(5+3\), and \(4+4\).

The primary 2026 comparison paper records that its new realization has doubled-pair graph two \(4\)-cycles and that Mizhaev's has one \(8\)-cycle. Thus those two examples realize two of the three arithmetically possible minimal cycle types.

## Verification
The displayed identities are exact incidence counts. The standalone checker `verify.py` recomputes the admissible \(k\)-values, the minimal face-vector and genus, the global and local excess identities, and the integer partitions of eight that can occur as cycle sizes of a simple \(2\)-regular graph.

The finite enumeration of integer partitions is exhaustive for the last graph-theoretic step, but it is not used to infer geometric realizability. The proof of the universal statements is the counting argument above.

## Relationship to prior work
Röst and Vígh construct a second embedded eight-faced genus-three face-neighbourly polyhedron. Their Theorem 1 proves that it has eight nonagonal faces, \(36\) edges, \(24\) vertices, trivalence, and exactly eight doubly adjacent face pairs. Their comparison table further records doubled-pair graph type \(4+4\) for their example and type \(8\) for Mizhaev's. Their introduction contains the standard exact-one-adjacency count for a trivalent face-neighbourly polyhedron, but it does not derive the minimality theorem above for the at-least-one-edge setting or classify all doubled-pair graph types forced at the minimal eight-face equivelar level.

Mizhaev independently supplies an exactly checkable integer realization of the earlier \(\{9,3\}\) genus-three incidence type and records its complete face adjacency. That paper establishes one realization, not the universal lower bound \(k\ge9\), the surplus identity \(D=4k-28\), or the three-way cycle-type classification.

Targeted searches using face-neighbourly, equivelar, nonagon, doubled-pair, surplus, and cycle-type terminology did not locate a published statement equivalent to the combined arithmetic rigidity theorem. Nearby indexed results concern either coordinate optimization for Mizhaev's realization or Euler-excess counts in unrelated graph-embedding problems and do not imply this result.

## Limitations
The result is an incidence theorem, not an embedding theorem. In particular, the \(5+3\) cycle type is shown only to be combinatorially admissible under the necessary counting constraints; no planar-faced realization in \(\mathbb R^3\) is proved.

The originality assessment is based on the inspected primary texts and targeted statement-level searches. An older unindexed map-theory observation could contain the same counting refinement.

## References
1. G. Röst and V. Vígh, *A second eight-faced polyhedron in which every two faces share an edge*, arXiv:2609.32998v1, first public 26 September 2026.
2. R. Mizhaev, *Integer Realization of an Equivelar Octahedron of Genus 3*, arXiv:2609.17700v1, first public 15 September 2026.
