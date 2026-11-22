# Edge-endpoint whisker defects and primitive matching-homology inclusions

## Finding
Let \(H=(V,E)\) be **any finite simple graph** with \(N=|V|\ge2\), and fix a distinguished edge \(e=\{u,v\}\in E\). Make \(W_e(H)\) by attaching one distinct pendant leaf to every original vertex except \(u\) and \(v\). For a graph \(F\), let \(p(F)\) be its number of perfect matchings, with \(p(\varnothing)=1\). Write \(\mathcal M(F)\) for the **ordinary** simplicial matching complex of \(F\), whose vertices are graph edges and whose faces are pairwise disjoint edge sets. Then:

1. **Even order.** For \(N=2m\), \(m\ge1\),
\[
\mathcal M(W_e(H))\simeq\bigvee^{p(H-e)}S^{m-1}.
\]
If \(W(H)\) is the graph with leaves attached at **all** original vertices, the natural simplicial inclusion \(\mathcal M(W_e(H))\hookrightarrow\mathcal M(W(H))\) induces a split-injective map on reduced integral homology in degree \(m-1\), with primitive, free cokernel of rank \(p(H-\{u,v\})\). In particular, the defect complex is contractible precisely when every perfect matching of \(H\) uses \(e\) (or there is no perfect matching at all).

2. **Odd order.** For \(N=2m+1\), \(m\ge1\),
\[
\mathcal M(W_e(H))\simeq\bigvee^{p(H-u)+p(H-v)}S^{m-1}.
\]
Thus the partial-leaf defect can have nonzero integral homology even though the fully whiskered matching complex is contractible at odd base order.

The wedge of zero spheres means a point; a wedge of \(r\) zero-spheres means \(r+1\) points, so the boundary cases \(m=1\) are included.

For the cycle \(H=C_N\), choose any rim edge \(e\). The graph obtained from the sunlet by deleting the two pendant edges at the endpoints of \(e\) has matching complex \(S^{m-1}\) when \(N=2m\ge4\), and \(S^{m-1}\vee S^{m-1}\) when \(N=2m+1\ge3\). This changes the fully whiskered cycle's two-sphere wedge (even \(N\)) or contractibility (odd \(N\)).

## Assumptions and scope
All graphs are finite, simple and undirected. Connectivity of \(H\) is **not** assumed, and no upper bound on degrees is imposed. Graph deletion \(H-e\) removes only the distinguished edge, while \(H-u\), \(H-v\) and \(H-\{u,v\}\) are induced vertex deletions. Original edges and newly attached leaf edges are distinct vertices in the matching complex. Denote the simplicial vertex corresponding to original edge \(f\) by \(b_f\), and one corresponding to the new leaf edge at \(x\in V\setminus\{u,v\}\) by \(w_x\). An empty complex is not being used: the matching complex contains the empty face, and nonempty graph-edge vertices exist because \(e\in E\). Reduced integral homology is used throughout. Every statement quantifies over all \(H\) and all choices of their edge \(e\).

## Proof
**A. A two-stage acyclic matching.** Consider the augmented face poset, including the empty face. Each simplex \(\sigma\) has a unique decomposition \(\sigma=B\sqcup A\), where \(B\subseteq E(H)\) is a base-graph matching, and \(A\) consists of pendant edges at vertices of \(V\setminus\{u,v\}\) left uncovered by \(B\). Define \(\phi(B)=1\) if \(B\) contains an original edge different from \(e\) incident with \(u\) or \(v\); otherwise put \(\phi(B)=0\). For \(\phi(B)=0\), toggle the simplicial vertex \(b_e\). This is always legal: no base edge except \(e\) touches \(u\) or \(v\), and there are no pendant edges at these two vertices. The operation reverses itself and stays within \(\phi=0\).

For \(\phi(B)=1\), necessarily \(e\notin B\). Let \(U(B)= (V\setminus\{u,v\})\setminus V(B)\), where \(V(B)\) is the set of original endpoints covered by \(B\). If \(U(B)\ne\varnothing\), toggle the leaf vertex \(w_{x(B)}\) at its least member \(x(B)\) under a fixed total order of \(V\). This is also legal and stays in \(\phi=1\). If \(U(B)=\varnothing\), the simplex is unpaired; it contains no leaf edges, since all leaf-bearing original vertices are covered by \(B\). Thus the **only** unpaired faces are original base matchings \(B\) covering all vertices other than \(u,v\), and containing an original edge (other than \(e\)) incident with \(u\) or \(v\).

To check acyclicity, orient every matched Hasse arrow upwards and every other cover arrow downwards. A downward move cannot increase \(\phi\); matched upward moves preserve \(\phi\), since the first stage toggles only \(e\) and the second toggles only a leaf. Hence a directed cycle would lie entirely in one fiber of \(\phi\). In the \(\phi=0\) fiber, every upward move inserts \(b_e\), which cannot be removed by an unmatched downward move in the fiber. In the \(\phi=1\) fiber, original base edges can only be removed, never inserted, so a directed cycle would have constant \(B\). Within a fixed \(B\), every upward step inserts the fixed pivot \(w_{x(B)}\), which cannot be removed by a downward unmatched move. Therefore no directed cycle exists. This reasoning also applies to the augmented empty face.

**B. Enumerating all critical faces.** If \(N=2m\), a matching covering \(N-2\) prescribed original vertices must cover an even number of original vertices, and the condition that it touches at least one of \(u,v\) forces it to cover **both**. Consequently it is exactly a perfect matching of \(H\) avoiding \(e\). If \(N=2m+1\), a matching covering the \(N-2\) prescribed original vertices must cover exactly one of \(u,v\): it is a perfect matching of \(H-u\) or \(H-v\), and the two families are disjoint. In both cases each unpaired base matching contains \(m\) edges, so the corresponding critical simplex is of dimension \(m-1\).

The empty face was paired with the singleton \(\{b_e\}\). Remove that matched pair, restoring \(\{b_e\}\) as one critical zero-simplex and omitting the empty face. The remaining partial matching is an ordinary acyclic face-poset matching. Hence the matching complex has a CW model with one zero-cell and precisely the stated number of \((m-1)\)-cells, and no other cells. If \(m\ge2\), all attaching maps are forced to be null because there are no intervening cells, yielding the sphere wedge. If \(m=1\), the model is a discrete set of the required number of points, equivalently a wedge of zero-spheres. Zero unpaired faces gives a contractible complex.

**C. Integral inclusion and primitive cycles, even \(N\).** For every perfect matching \(P\) of \(H-e\), enumerate its \(m\) base edges \(f_1,\ldots,f_m\). Choose for each \(f_i\) an endpoint \(x_i\in f_i\setminus\{u,v\}\). This is possible because \(P\) avoids \(e\). In the augmented simplicial chain complex of \(\mathcal M(W_e(H))\), the join
\[
z_P=([b_{f_1}]-[w_{x_1}])*\cdots*([b_{f_m}]-[w_{x_m}])
\]
is well defined and is a reduced integral \((m-1)\)-cycle. Each factor is a reduced zero-cycle, and every edge choice from different factors is graph-vertex-disjoint. Replacing \(x_i\) by the other endpoint when both are leaf-bearing changes \(z_P\) by a boundary: the difference \([w_y]-[w_{x_i}]\) is the boundary of the oriented one-simplex \([w_{x_i},w_y]\). Exchanging two factors changes orientation by a minus sign.

The perfect base-edge simplex \(P\) is maximal, so extracting its oriented coefficient defines an integral cocycle \(\delta_P\). The matrix of pairings \(\langle\delta_P,z_Q\rangle\) for perfect matchings avoiding \(e\) is the identity. Step B shows that these cycles account for the entire rank of the free top homology, hence they form a primitive \(\mathbb Z\)-basis. In the fully whiskered complex, the analogous cycles for **all** perfect matchings of \(H\) form the integral basis established by the known fully-whiskered classification. The inclusion sends \([z_P]\) to the identically labelled \([z_P]\). Thus its matrix is an inclusion of a coordinate sublattice and is split-injective over \(\mathbb Z\); the missing coordinates are exactly the perfect matchings containing \(e\), in bijection with perfect matchings of \(H-\{u,v\}\). This proves the precise cokernel formula. No equivariant homotopy equivalence is asserted.

## Verification
The standalone `check.py` enumerates all graphs with distinguished edge \(\{0,1\}\) through four original vertices, plus deterministically sampled graphs of orders five and six. It independently enumerates all matching simplices, explicitly constructs the two-stage face-poset matching, verifies the absence of directed cycles in the complete oriented nonempty Hasse diagram, enumerates the prescribed perfect/near-perfect base matchings and calculates all reduced mod-two Betti numbers by simplicial boundary reduction, and checks the exact integer alternating-cycle boundaries and unit perfect-base-face coefficient pairings for even base orders. `expected_output.json` holds the actual output, which can be reproduced with `python3 check.py`. These tests do **not** replace the symbolic proof for arbitrarily many vertices, nor do mod-two ranks alone establish integral primitivity; the explicit cycle-cochain pairings in step C supply the latter.

## Relationship to prior work
Barik, Mondal and Mukherjee (first publicly available on 14 April 2026, arXiv:2604.12606v1) develop recursive acyclic matchings for independence complexes with simplicial vertices. Their full article describes chordal and grid-comparability applications, not these exact partial whisker defects or their integral inclusion maps. The ordinary matching complex is the independence complex of the line graph, so their framework motivates this construction.

An earlier exact theorem, *Perfect matchings govern the integral topology of fully whiskered matching complexes* (2026), already classifies \(\mathcal M(W(H))\) for **all** base graphs, including its primitive basis indexed by perfect matchings; that theorem is used and credited in step C. It does not determine the homotopy of deleting two *pendant graph edges* at the endpoints of a fixed original edge, or the resulting inclusion image. General outerplanar matching-complex wedge theorems do not cover arbitrary \(H\), and the perfect-matching extendibility complex is a different construction.

## Limitations
The defect deletes exactly the two pendant edges at the endpoints of an existing **original** edge. Arbitrary sets of missing leaves, higher matching capacities, and homotopy-equivariant splittings are not classified. The inclusion theorem concerns **integral homology**, not a claimed homotopy retraction. The parity-zero-sphere convention is explicit. Search cannot rule out an unindexed equivalent theorem; no independent mathematical audit has been performed.

## References
1. S. Barik, A. Mondal and S. Mukherjee, *A recursive construction of an acyclic matching on the independence complex of a graph with a simplicial vertex*, arXiv:2604.12606v1, 14 April 2026, https://arxiv.org/html/2604.12606v1 .
2. *Perfect matchings govern the integral topology of fully whiskered matching complexes*, published 25 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-perfect-matchings-govern-the-integral-topology-of-fully-whiskere--8c80f796f478 .
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, 7 November 2024, https://arxiv.org/abs/2411.04601 .
