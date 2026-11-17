# Collapsible alternating and full-symmetry quotients of Petersen two-point configurations

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph on the ten two-subsets of a five-element set, with disjointness as adjacency. Let \(D=\operatorname{UD}_{2}(P)\) be its cubical discretized unordered configuration space of two points. The natural action of the alternating and symmetric groups on the five labels preserves \(D\). **Both ordinary topological quotients of this canonical discrete model are collapsible:**
\[
\left|\operatorname{sd}(D)\right|/A_5\searrow\{*\},\qquad
\left|\operatorname{sd}(D)\right|/S_5\searrow\{*\}.
\]
Here a collapse on the orbit \(\Delta\)-complex is intended; equivalently, both geometric quotients have explicit elementary CW collapses to a single vertex. In particular both are contractible, integrally acyclic, and simply connected. This includes the index-two alternating subgroup, not only the full automorphism group.

## Assumptions and scope
The finite graph \(P\) has vertices \(\{a,b\}\subseteq\{0,1,2,3,4\}\), with an edge exactly when two vertex labels are disjoint. The cubical \(D\) has a cell for each unordered pair of closed graph cells whose closures are disjoint. Thus its zero-cells are unordered pairs of distinct graph vertices; its one-cells are graph-edge/vertex pairs with no incidence; and its two-cells are pairs of graph edges with no common endpoint. There are exactly \(45\), \(120\), and \(75\) cells of dimensions \(0\), \(1\), and \(2\), respectively.

The barycentric subdivision \(\operatorname{sd}(D)\) has vertices indexed by these cells, edges indexed by strict cell-face relations, and triangles indexed by chains of three cells of dimensions \(0<1<2\). Every group element preserves each cell dimension. Therefore the induced action on a simplex cannot permute its vertices nontrivially; the orbit cells define a regular geometric \(\Delta\)-complex, with possible distinct simplices sharing vertex data. We explicitly retain simplex orbits (rather than identifying them by vertex sets).

This theorem concerns the ordinary topological quotients of the *discretized* model. Prue and Scrimshaw's stable-equivalence theorem identifies the nonequivariant homotopy type of \(D\) with the continuous two-point configuration space (the Petersen graph satisfies the stated subdivision conditions). That nonequivariant fact alone does not justify passing the deformation retract to either symmetry quotient; no assertion about the quotients of the continuous configuration space is made here.

## Proof
1. Enumerate the ten graph vertices and fifteen edges by lexicographic pairs. Enumerate the \(45+120+75=240\) cubical cells, all \(240\) incidences between dimensions zero and one, all \(300\) incidences between dimensions one and two, and the \(300\) zero-to-two incidences. The chains of length three number \(600\). Thus the barycentric subdivision contains exactly \(240\) vertices, \(840\) edges, and \(600\) triangles.
2. Enumerate the \(120\) permutations of the five labels, including the \(60\) even ones. For each cubical cell, compute the induced image of its graph endpoints; propagate the group action to chains of nested cells. Take orbit representatives separately in each dimension, retaining their incidence data. For \(A_5\), the orbit \(\Delta\)-complex has \((f_0,f_1,f_2)=(8,17,10)\). For \(S_5\), it has \((6,10,5)\).
3. Order the barycentric face chains as in `verify.py`, which sorts the face relation indices. Number the orbit cells consecutively by first unvisited representative. In the \(A_5\) quotient, the ten (triangle, free edge) collapses are
\[
(0,4),(1,11),(2,0),(3,13),(4,10),(5,1),(6,14),(7,2),(8,15),(9,3).
\]
In the \(S_5\) quotient, the five collapse pairs are
\[
(0,6),(1,7),(2,0),(3,1),(4,2).
\]
In each step, `verify.py` recounts the surviving triangle cofaces and checks that the selected edge has exactly one, so the pair is an elementary collapse. Every face of the orbit triangles consists of **three distinct edge orbits**; all selected edges are different.
4. After the two-dimensional collapses the \(A_5\) quotient has eight vertices and seven edges, specifically indices \(5,6,7,8,9,12,16\). The \(S_5\) quotient has six vertices and five edges, specifically indices \(3,4,5,8,9\). Direct endpoint tracing verifies in each case that the residual graph is connected and cycle-free; it is a tree. Repeated leaf-edge collapses finish both quotients at one vertex.

The proof is finite and exhaustive: no appeal to random sampling or homology-rank inference is used.

## Verification
Execute `python verify.py` with Python 3 and the standard library. Its construction checks the cubical-cell counts, all four types of incidence counts, the complete \(A_5\) and \(S_5\) permutation actions, the orbit-cell counts, uniqueness of every triangle's three edge orbits, all free-edge collapses, and the connectivity and acyclicity of the final graphs. The recorded output is supplied in `verification_output.txt`.

## Relationship to prior work
Prue and Scrimshaw (arXiv:0909.5511, first public version 2009-09-30) define and study discretized configuration spaces and prove stable equivalence to ordinary graph configuration spaces under explicit subdivision conditions. Their theorem does **not** provide the present two equivariant orbit-cell collapses. Previously indexed calculations for Petersen two-particle configurations establish integral homology and rational symmetric-group characters of the original configuration space, and natural integral torus classes in its second homology. Neither rational representation invariants nor homology of the original space imply integral collapsibility of these orbit spaces. Known collapsible full-symmetry quotients of configuration spaces of complete or complete-bipartite graphs concern different graph families.

## Limitations
The result applies to two particles on this particular graph and its stated finite label-permutation groups. It does not classify other subgroup orbit spaces, provide an equivariant deformation retraction from the continuous two-point configuration space, or determine the fundamental groups of those different continuous quotients. Literature not accessible beyond indexed summaries remains a publication-priority risk; independent verification has not been performed.

## References
- P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511 (initial version 2009-09-30), especially the definition of discretized configuration spaces and Theorem 3.2.
- Published research record, *Two-particle Petersen configuration homology as an \(S_5\)-module* (summary inspected; full text inaccessible): underlying integral homology and rational symmetry modules, not an equivariant orbit-collapse statement in the available summary.
- Published research record, *Six pentagon tori determine the integral \(S_5\)-lattice of Petersen two-point configurations* (summary inspected): integral top-homology lattice of the original space.
- Published research record, *Alternating-symmetry exceptions in two-point complete-graph configuration quotients* (summary inspected): quotients for complete graphs rather than the Petersen graph.
