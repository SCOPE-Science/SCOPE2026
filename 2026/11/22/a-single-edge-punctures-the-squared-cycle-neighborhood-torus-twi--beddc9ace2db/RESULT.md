# A single edge punctures the squared-cycle neighborhood torus twice

## Finding
Let \(n\ge9\), let \(G_n=C_n^2\) be the graph on \(\mathbb Z/n\mathbb Z\) with edges joining vertices of cyclic distance one or two, and let \(e\) be **any** graph edge. For the open Lovász neighborhood complex \(\mathcal N\), there is an integral homotopy equivalence
\[
\boxed{\bigl|\mathcal N(G_n-e)\bigr|\simeq S^1\vee S^1\vee S^1.}
\]
Both inequivalent edge types, cyclic distance one and cyclic distance two, have this homotopy type. In contrast, the intact complex \(\mathcal N(G_n)\) has the homotopy type of a torus, a result already present in the literature. Thus either single-edge fault eliminates the integral degree-two fundamental class and increases the first integral Betti rank from two to three.

## Assumptions and scope
Graphs are finite, simple, and undirected; deleting an edge retains both endpoints. The *open* neighborhood complex of a graph \(G\) is the simplicial complex
\[
\mathcal N(G)=\{\sigma\subseteq V(G):\text{some vertex }v\text{ is adjacent to every }w\in\sigma\}.
\]
Its facets are maximal open-neighbor sets, and all indices below are modulo \(n\). The theorem covers every integer \(n\ge9\) and every edge of \(G_n\), with no claim for smaller orders or multiple faults. The cyclic and reversal automorphisms reduce the two types to \(e=\{0,1\}\) and \(e=\{0,2\}\).

## Proof
**The universal torus core.** For \(n\ge9\), the \(n\) maximal simplices of the intact neighborhood complex are the distinct tetrahedra
\[
Q_i=\{i-2,i-1,i+1,i+2\}.
\]
Any two distinct tetrahedra intersect in at most two vertices, and every two-element face of cyclic difference two is supported by the unique relevant triple after the following first stage. Put
\[
\begin{aligned}
U_i&=\{i-2,i-1,i+1\},&V_i&=\{i-1,i+1,i+2\},\\
E_i&=\{i-1,i+1\},&A_i&=\{i-2,i-1,i+2\},\\
B_i&=\{i-2,i+1,i+2\}.&&
\end{aligned}
\]
For every \(i\), the face \(U_i\) is free in \(Q_i\). Remove the elementary pairs \((U_i,Q_i)\) for all \(i\). Now \(E_i\) is free in the triangle \(V_i\); remove \((E_i,V_i)\) for all \(i\). The surviving complex \(T_n\) has exactly the \(2n\) triangles \(A_i,B_i\). Its edges have cyclic differences one, three or four; there are \(3n\) of them, each in exactly two triangles. At the vertex zero the six link edges, written using integer representatives, form the six-cycle
\[
-4\;\text{--}\;-3\;\text{--}\;1\;\text{--}\;4\;\text{--}\;3\;\text{--}\;-1\;\text{--}\;-4.
\]
The complex is connected via edges of difference one. The orientations \([i-2,i-1,i+2]\) on \(A_i\) and \([i-2,i+2,i+1]\) on \(B_i\) cancel along every shared edge. Hence \(T_n\) is a closed connected orientable surface with
\[
\chi(T_n)=n-3n+2n=0,
\]
so it is a triangulated torus. These elementary collapses are included only to establish a convenient explicit core; the intact torus homotopy type is prior work.

**Deleting a distance-one edge.** Take \(e=\{0,1\}\). The affected neighborhoods become the triangles \(A_0\) and \(B_1\), while every other \(Q_i\) is unchanged. For \(i\notin\{0,1\}\), perform the same elementary pairs \((U_i,Q_i)\) and then \((E_i,V_i)\). The surviving complex is exactly \(T_n\) with the open interiors of \(B_0\) and \(A_1\) removed, retaining their boundary edges. These two triangles have disjoint vertex sets when \(n\ge9\). It is therefore a torus minus two disjoint open disks, a compact orientable surface of genus one with two boundary circles. This surface deformation retracts onto a wedge of \(2\cdot1+2-1=3\) circles.

**Deleting a distance-two edge.** Take \(e=\{0,2\}\). The affected neighborhoods become \(U_0\) and \(V_2\), whereas the remaining \(Q_i\) are unchanged. Execute the usual pairs \((U_i,Q_i)\), \((E_i,V_i)\) for every \(i\notin\{0,2\}\), then collapse \((E_0,U_0)\) and \((E_2,V_2)\). These are free pairs at their respective stages. The resulting subcomplex of \(T_n\) is obtained by deleting the four triangles \(A_0,B_0,A_2,B_2\) together with the two internal diagonals \(\{-2,2\}\) and \(\{0,4\}\). Each pair \(A_0\cup B_0\) and \(A_2\cup B_2\) forms a triangulated disk whose diagonal is removed. The disk interiors are disjoint, although their boundaries share the vertex \(1\). The resulting complex remains connected because all cycle edges \(\{i,i+1\}\) survive; its face vector is
\[
(f_0,f_1,f_2)=(n,3n-2,2n-4),\quad\chi=-2.
\]
Moreover every triangle can be removed by elementary triangle-edge collapses. Indeed, the dual adjacency graph of the triangles of the closed triangulated torus \(T_n\) is connected. Every connected component of the dual graph on the *remaining* triangles consequently has an edge to one of the four removed triangles. Root a spanning tree of each component at such an adjacent removed triangle, and remove remaining triangles in increasing tree distance from the removed root. For each triangle, use the shared edge with its previously removed parent; that edge is free, since every edge of \(T_n\) originally belonged to exactly two triangles and the parent was removed using another edge. The remaining connected one-dimensional complex has Euler characteristic \(-2\), and hence is homotopy equivalent to three circles wedged at one point.

The two edge orbits exhaust all edges of \(G_n\), completing the integral homotopy classification.

## Verification
The self-contained `verify_cycle_fault.py` reconstructs the open-neighborhood complex directly from the graph for each \(9\le n\le64\) and both edge types, checks every listed elementary free pair and the exact final subcomplex, verifies the oriented closed torus and its six-cycle vertex links, peels every remaining triangle, and independently computes the complete mod-two Betti numbers from the original boundary matrices. All 112 finite instances passed with the marker `CYCLE_SQUARE_EDGE_FAULT_VERIFY_OK`. The faulted face vector is \((n,4n-2,4n-6,n-2)\), and the independent homology calculation yields reduced mod-two Betti ranks \((0,3,0,0)\) in dimensions zero through three. The infinite statement rests on the explicit all-order free-face and dual-graph argument, not on extrapolation from these finite checks.

## Relationship to prior work
Shukla's 2018 preprint (2019 journal publication) classifies neighborhood complexes of four-regular circulant graphs and includes the intact case \(C_n(1,2)\); it does not classify the nonregular edge-deleted graphs. Published results titled *A sphere quotient and equivariant torus retraction for square-cycle neighborhood complexes* and *Sphere mapping-tori in neighborhood complexes of every stable cycle power* likewise treat the intact complexes, their symmetry or their higher-power analogues, not either of the two single-edge-fault complexes. The present conclusion is not inferred from the intact torus theorem: deleting an edge changes two distinct neighborhood facets, and the two edge orbits require different collapse sequences. A separate published vertex-deletion result for squared cycles has different graph objects and no implication for edge deletion. The searches and source comparisons were not exhaustive across unindexed material.

## Limitations
No statement is made about \(n\le8\), two or more edge deletions, equivariant actions on the faulted complexes, or naturality of the homotopy equivalences with respect to graph inclusion. Homotopy equivalence does not assert homeomorphism of the three-dimensional original complexes to a graph; the equivalence is certified by elementary collapses. Some exact comparable result could exist outside indexed literature. Independent mathematical audit has not been performed.

## References
- S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first publicly submitted 2018-02-13, https://arxiv.org/abs/1802.04526. *Electronic Journal of Combinatorics* 26(2) (2019), P2.4, https://doi.org/10.37236/7549.
- *A sphere quotient and equivariant torus retraction for square-cycle neighborhood complexes*, publicly available mathematical result, 2026-11-01; its complete scientific result statement was compared for prior implication.
- *Sphere mapping-tori in neighborhood complexes of every stable cycle power*, publicly available mathematical result, 2026-10-25; its complete scientific result statement was compared for prior implication.
