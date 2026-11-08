# The Dyck graph from maximum induced matchings of the Shrikhande graph

## Finding
Let \(S\) be the Shrikhande graph on \(V=\mathbb Z_4^2\), with vertices adjacent when their coordinate difference lies in
\[
\{\pm(1,0),\pm(0,1),\pm(1,1)\}.
\]
A matching is **induced** when the subgraph on the endpoints of its selected edges has no edges other than those selected. There are exactly \(32\) maximum induced matchings of \(S\), each with three edges. In particular, the induced-matching number is \(3\).

For \(j\in\{1,2\}\), let \(R_j(S)\) have those 32 matchings as vertices, joining distinct matchings when they have exactly \(3-j\) edges in common. Thus one move replaces precisely \(j\) selected edges with \(j\) different edges and preserves maximum induced-matching size. Then
\[
R_1(S)\cong32K_1,\qquad R_2(S)\cong D_{\mathrm{Dyck}},
\]
where \(D_{\mathrm{Dyck}}\) is the cubic 32-vertex Dyck graph. The second graph has 48 edges, is connected and bipartite, and has radius and diameter five and girth six.

More precisely, each of the 48 edges of \(S\) occurs in exactly two of the 32 optimum induced matchings. Consequently each edge of \(R_2(S)\) is uniquely represented by the original edge shared by its two endpoints.

## Assumptions and scope
All graphs are finite, undirected and simple. Vertices of \(S\) are ordered pairs of residues modulo four, not an embedding of 16 anonymous vertices. A two-edge replacement is **not** required to be a sequence of individually legal one-edge replacements. It changes two of the three matching edges simultaneously, and both endpoints must be optimum induced matchings. The Dyck graph is specified independently as the graph of all triangles of \(S\), with two triangles adjacent exactly when they share one original graph edge.

## Proof
**Exhaustion and incidence.** There are 48 original edges. Fix the lexicographic edge order and test an index subset \(I\) by collecting its endpoints \(U\). It is an induced matching precisely when all endpoints are distinct and the number of edges of \(S[U]\) equals \(|I|\). The supplied finite checker executes this equivalence over all \(\binom{48}{3}=17296\) triples and all \(\binom{48}{4}=194580\) quadruples. Exactly 32 triples pass, while no quadruple passes. Any matching of size at least four would contain a passing quadruple, so size three is the global maximum. Each original edge occurs in exactly two passing triples, as the checker also verifies. No two different passing triples share two edges (checked for all \(\binom{32}{2}=496\) pairs). Hence \(R_1(S)\) is edgeless; the \(48\) original edges each yield one unique edge of \(R_2(S)\), so the latter is cubic and has 48 edges.

**Explicit Dyck correspondence.** We use braces for unordered edges and denote translation of every endpoint by \(+x\) modulo four. The following two maximum induced matchings represent the two size-16 translation orbits:
\[
\begin{aligned}
M_0&=\{\{(0,1),(3,0)\},\{(1,0),(1,3)\},\{(2,2),(3,2)\}\},\\
M_1&=\{\{(0,0),(0,1)\},\{(1,3),(2,0)\},\{(2,2),(3,2)\}\}.
\end{aligned}
\]
The 32 triangles likewise form two size-16 translation orbits represented by
\[
T_0=\{(0,0),(0,1),(3,0)\},\qquad T_1=\{(0,0),(0,1),(1,1)\}.
\]
The independent checker confirms each orbit size, disjointness and completeness. Within each matching orbit no pair of distinct members shares an original edge; within each triangle orbit no two distinct triangles share an edge. The translations \(M_0+x\) and \(M_1+y\) share an edge exactly if
\[
y-x\in A=\{(0,0),(1,3),(2,1)\}.
\]
Likewise, \(T_0+a\) and \(T_1+b\) share an edge exactly if
\[
b-a\in B=\{(0,0),(3,0),(3,3)\}.
\]
The matrix \(L=\begin{pmatrix}2&3\\1&1\end{pmatrix}\) has determinant \(-1\), invertible modulo four, and satisfies \(L(A)=B\). Therefore the mapping
\[
\Phi(M_i+x)=T_i+Lx\quad(i\in\{0,1\},\ x\in\mathbb Z_4^2)
\]
is a bijection of all 32 states and preserves adjacency in both directions. By the classical triangle-incidence construction, its target is the Dyck graph. The standalone program additionally checks all 48 mapped edges directly, rather than relying only on the orbit argument.

**Distances.** Breadth-first search from every one of the 32 states in the independently built two-exchange graph visits all 32 states and returns eccentricity five at every state. The checker also verifies the full explicit bijection to the Dyck graph. Thus the claimed connectivity, radius and diameter hold. A direct shortest-cycle calculation (or the standard Dyck construction) gives girth six; the Cayley checker independently verifies that a six-cycle exists and that no shorter cycle exists.

## Verification
Run the standard-library Python files in the same directory as the mapping certificate:
```
python3 verify_cayley.py
python3 verify_latin.py
python3 verify_equivariant.py
```
Each program prints only after all its assertions succeed. The first enumerates all three- and four-edge candidates in the Cayley model, checks the complete 32-vertex isomorphism certificate in `isomorphism.txt`, and computes every eccentricity. The second independently constructs the graph as the complement of the order-four cyclic Latin-square graph, uses edge-conflict masks and verifies all possible augmentations, then recomputes the 32-state exchange network. The third proves the two-translation-orbit correspondence, explicitly checks the voltage sets, and verifies the edge bijection. The accompanying text outputs are records of these actual runs; the programs, not the outputs alone, are the verification evidence.

## Relationship to prior work
Induced matchings and their connection to independent sets in squares of line graphs are standard; Basavaraju, Heggernes, van 't Hof, Saei and Villanger (first posted December 18, 2013) study enumeration bounds and algorithms, with a main theorem for triangle-free graphs. Since the Shrikhande graph has triangles, that bound does not classify its maximum induced matchings or their exchanges. The classical Shrikhande graph and the Dyck graph have well-known descriptions; in particular, the Dyck graph as the shared-edge adjacency graph of Shrikhande triangles is **not** claimed to be new. The new statement is that the graph of **two-edge exchanges of maximum induced matchings** realizes the same Dyck graph, with the explicit orbit map above.

Earlier investigations of ordinary independent-set exchanges on the Shrikhande graph, of its independence complex, and of perfect-matchings on the Dyck graph use different state families; those results do not by themselves imply this correspondence. Searches of induced-matching terminology, the exact counts and the graph-isomorphism formulation did not locate the stated result. This is not a proof of publication uniqueness; hidden historical work remains possible.

## Limitations
This is a fixed finite-graph classification, not an infinite-family theorem. The upper bound and the 32-state census use exhaustive finite enumeration, with no unproved extrapolation. The isomorphism also has a direct translation-orbit proof, but independent human or machine-formal validation has not been performed. A previously unindexed source or an equivalent combinatorial encoding could affect priority; the cited general results do not settle that possibility.

## References
1. M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei and Y. Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180v1 (first posted 2013-12-18), https://arxiv.org/abs/1312.5180.
2. Graph Tables, *Shrikhande graph*, https://jaanos.github.io/tables/graphs/Shrikhande.html (graph definition, symmetry and distinction from the rook graph).
3. Graph Tables, *Dyck graph*, https://jaanos.github.io/tables/graphs/Dyck.html (triangle-incidence construction and graph metrics).
4. K. K. Dabrowski, M. Demange and V. V. Lozin, *New results on maximum induced matchings in bipartite graphs and beyond*, Theoretical Computer Science 478 (2013), 33–40, DOI:10.1016/j.tcs.2013.01.027.
