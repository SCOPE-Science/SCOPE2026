# Sharp six-vertex reconstruction failure for one-point type polynomials over 2-trees

## Finding

Let \(H_4\) be the countable homogeneous universal \(K_4\)-free graph. A **2-tree** is the graph starting from one edge and successively adding a vertex adjacent to exactly the endpoints of an existing edge. Thus a 2-tree is connected, chordal, and \(K_4\)-free. For each finite 2-tree \(G\) whose vertices are individually named as parameters in \(H_4\), let
\[
P_G(z)=\sum_{p\in S_1^{\rm na}(G)}z^{\#\{a\in G:p\models R(x,a)\}},
\]
where \(S_1^{\rm na}(G)\) consists of complete nonalgebraic one-point types over those named vertices. In this expression the superscript \({\rm na}\) indicates nonalgebraic, and \(R\) is adjacency.

**Sharp first collision.** For every pair of nonisomorphic 2-trees on at most five vertices, their polynomials \(P_G\) differ. Among all five isomorphism classes of six-vertex 2-trees there is exactly one unordered nonisomorphic pair with equal polynomials. Its two graphs \(A,B\), with vertices labelled \(0,1,2,3,4,5\), are specified by their complete lists of triangles:
\[
\begin{aligned}
\mathcal T(A)&=\{012,013,024,125\},\\
\mathcal T(B)&=\{012,013,024,135\}.
\end{aligned}
\]
Here \(ijk\) denotes \(\{i,j,k\}\), and edges are precisely the pairs occurring in listed triangles. These graphs have different degree sequences, \((2,2,2,4,4,4)\) and \((2,2,3,3,4,4)\), but
\[
P_A(z)=P_B(z)=1+6z+15z^2+16z^3+6z^4.
\]
In particular, each has exactly \(44\) nonalgebraic one-point types.

**An infinite family of connected collisions.** For each integer \(t\ge0\), form \(A_t\), respectively \(B_t\), by adding \(t\) new vertices, each adjacent to exactly vertices \(0\) and \(1\), to the corresponding graph. Then \(A_t\) and \(B_t\) are nonisomorphic 2-trees on \(6+t\) vertices, and
\[
\boxed{P_{A_t}(z)=P_{B_t}(z)
=z^2+2z^3+z^4+(1+z)^t(1+6z+14z^2+14z^3+5z^4).}
\]
Consequently their ungraded one-type counts agree and equal \(4+40\cdot2^t\) at every size \(6+t\). The equivalence is of cardinality-graded type *counts*, not of pointwise-labelled types or of parameter graphs.

## Assumptions and scope

All graphs are finite simple undirected graphs unless \(H_4\) is specified. The new point of a type is required distinct from every named parameter. Two types are distinguished by their full positive/negative adjacency formulas to every parameter, not merely by their adjacency degree. The generating polynomial is a coarsening of this complete type list, summing over degrees. A 2-tree with \(n\ge2\) vertices has \(2n-3\) edges when \(n\ge2\). The finite classification includes the unique two-vertex 2-tree.

## Proof

**Step 1 — identify the polynomial.** The extension property of the Fraïssé limit \(H_4\) says a prescribed adjacency set \(S\subseteq V(G)\) for a fresh vertex is realized precisely when adding that vertex creates no \(K_4\). This is equivalent to \(G[S]\) having no triangle: if \(u,v,w\in S\) span a triangle, they and the new vertex form a \(K_4\); conversely every new \(K_4\) has such a triangle. Each admissible set \(S\) gives exactly one complete nonalgebraic one-point type, realized infinitely often. Therefore
\[
P_G(z)=\sum_{S\subseteq V(G):G[S]\text{ triangle-free}}z^{|S|}.
\]
2-trees are chordal by induction: appending a simplicial vertex adjacent along an edge cannot create a chordless cycle of length at least four. A chordal graph has an induced cycle precisely when it contains a triangle. Hence for 2-trees the preceding sum is also the **induced-forest (acyclic) polynomial** \(\sum_{G[S]\text{ acyclic}}z^{|S|}\). This identification and the general notion of acyclic polynomials are established background, not claimed as new.

**Step 2 — the complete small census.** Each 2-tree with at least three vertices has a degree-two simplicial vertex whose deletion leaves a 2-tree; reverse such a deletion to generate all 2-trees by adjoining a vertex to an existing edge. At each size, identify graph isomorphisms using the lexicographically minimal edge-set encoding over all vertex permutations. From the unique two-vertex edge this yields \(1,1,1,2,5\) isomorphism classes at orders \(2,3,4,5,6\), respectively. The following exact census is complete; the displayed coefficient vector lists coefficients from degree zero upward and suppresses terminal zero coefficients.

| Order | Triangle sets for each isomorphism class | Nonzero coefficient vector |
|---|---|---|
| 2 | no triangles | \((1,2,1)\) |
| 3 | \(012\) | \((1,3,3)\) |
| 4 | \(012,013\) | \((1,4,6,2)\) |
| 5 | \(012,013,014\) | \((1,5,10,7,2)\) |
| 5 | \(012,013,024\) | \((1,5,10,7,1)\) |
| 6 | \(012,013,014,015\) | \((1,6,15,16,9,2)\) |
| 6 | \(012,013,014,025\) | \((1,6,15,16,7,1)\) |
| 6 | \(012,013,024,035\) | \((1,6,15,16,6,1)\) |
| 6 | \(012,013,024,125\) | \((1,6,15,16,6)\) |
| 6 | \(012,013,024,135\) | \((1,6,15,16,6)\) |

Every triangle set specifies an actual 2-tree, by the edge construction described above; the isomorphism test and the direct all-subsets count in `verify.py` prove that the table is exhaustive. The unique repeated coefficient vector at six vertices occurs in the last two rows. The degree sequences quoted in the finding prove the graphs are nonisomorphic. This argument proves sharpness through order six, with no claim of exhaustive classification beyond that order.

**Step 3 — a rooted edge collision.** For a fixed edge \(e=\{0,1\}\), define the restricted polynomial
\[
B_{G,e}(z)=\sum_{S\subseteq V(G):G[S]\text{ triangle-free},\ e\subseteq S}z^{|S|}.
\]
Direct inspection of the four displayed triangles in either \(A\) or \(B\) shows that when vertices \(0\) and \(1\) belong to \(S\), vertices \(2,3\) cannot belong to it; of the other vertices \(4,5\), each one is freely selectable. Hence
\[
B_{A,e}(z)=B_{B,e}(z)=z^2(1+z)^2=z^2+2z^3+z^4.
\]
For each of the \(t\) appended vertices, adding it to a chosen old set is forbidden exactly when both endpoints of \(e\) already belong to that set. Thus sets including \(e\) can include none of the new vertices and contribute \(B_{G,e}\); every other admissible old set can be combined with any subset of the new vertices and contributes \((1+z)^t(P_G-B_{G,e})\). This proves the boxed all-order identity.

**Step 4 — nonisomorphism persists.** The two endpoints of \(e\) have degree four in both original graphs. For \(A_t\) the degree multiset is
\[
\{4+t,4+t,4,\underbrace{2,\ldots,2}_{t+3}\},
\]
whereas for \(B_t\) it is
\[
\{4+t,4+t,3,3,\underbrace{2,\ldots,2}_{t+2}\}.
\]
They differ at every \(t\ge0\): \(B_t\) has degree-three vertices, while \(A_t\) does not. All graphs remain 2-trees because each newly attached vertex has precisely the endpoints of an old edge as its two neighbors. Finally substituting \(z=1\) gives \(4+40\cdot2^t\) types.

## Verification

The standalone `verify.py` script (Python standard library, no external dependencies) starts with an edge, generates every edge-attachment extension through six vertices, and uses all vertex permutations for isomorphism-free canonicalization. It calculates \(P_G\) in two independent ways: forbidding fully selected triangles, and testing every induced subgraph for a cycle using disjoint-set union. It compares every polynomial class and verifies that the only repeated six-vertex polynomial belongs to the displayed pair. It additionally checks both witness graphs, their degree sequences, the rooted-edge restricted polynomial, and the boxed formula against independently enumerated finite expansions for \(0\le t\le8\). Its actual output is embedded as `verification_output.txt`. Finite checks verify the base census and examples; the fan identity for all \(t\) follows from the bijective argument above, not extrapolation.

## Relationship to prior work

Henson's homogeneous \(K_4\)-free graph and the general finite extension condition are standard background; Conant's 2014 preprint studies model-theoretic independence and does not give a two-tree reconstruction threshold. Barton–Brown–Pike (arXiv 2020; 2022 publication) define and study the induced-forest/acyclic polynomial and prove general non-reconstruction examples among arbitrary graphs; their Section 1 does not establish either this unique six-vertex 2-tree collision or the edge-rooted infinite 2-tree family. Literature describing the triangle hypergraph of a 2-tree supports the reduction, not the claimed census. A published induced-forest result on crown graphs concerns a different graph class and does not imply this 2-tree threshold. The equivalence of our \(P_G\) with the acyclic polynomial on chordal graphs is fully acknowledged; **only the sharp restricted-class collision and its all-order rooted propagation are the claimed contribution**.

## Limitations

The census is exhaustive only through six vertices; the theorem does not assert that the exhibited pair is the only collision at any larger size. Acyclic polynomials are known not to reconstruct arbitrary graphs, and the general graph-nonuniqueness fact is not new. The classification concerns cardinality-graded nonalgebraic one-point type counts, not the complete labelled type set, not higher-arity types, and not every \(K_4\)-free parameter graph. The priority comparison cannot rule out unindexed earlier computations of the same two-tree family; independent mathematical and historical-priority assessment remains to be done.

## References

1. Gabriel Conant, *Forking and Dividing in Henson Graphs*, arXiv:1401.1570, first posted 2014-01-08. https://arxiv.org/abs/1401.1570
2. Caroline Barton, Jason I. Brown, David A. Pike, *Acyclic Polynomials of Graphs*, arXiv:2011.01735, first posted 2020-11-03; *Australasian Journal of Combinatorics* 82(2), 146–181 (2022), Sections 1.1–1.3. https://arxiv.org/abs/2011.01735 ; https://ajc.maths.uq.edu.au/pdf/82/ajc_v82_p146.pdf
3. *Improper sum-list colouring of 2-trees*, *Discrete Applied Mathematics*, https://doi.org/10.1016/j.dam.2019.07.004 (2019), Section 4, on the triangle hypergraph of a 2-tree.
4. Relevant published comparison: *Acyclic and maximal-forest polynomials of crown graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-acyclic-and-maximal-forest-polynomials-of-crown-graphs--6c5358dc2696
