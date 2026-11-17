# All-scale homotopy of axis-deformed cross-polytope Vietoris–Rips complexes

## Finding
For every integer \(d\ge2\), every ordered tuple of positive real lengths \(0<a_1\le\cdots\le a_d\), and every real threshold \(r\ge0\), let \(P=\{\pm a_i e_i:1\le i\le d\}\subset\mathbb R^d\) with its **ambient Euclidean** metric. The inclusive Vietoris–Rips complex \(K_r=\operatorname{VR}_{\le r}(P)\) is homotopy equivalent to a finite wedge of spheres of possibly different dimensions, including zero-dimensional spheres. Its complete integral homotopy type is given by the explicit recurrence below.

Set \(w_i=a_i^2\), \(t=r^2\), and let \(T_t\) be the graph on the axis indices \(\{1,\ldots,d\}\) with \(ij\) an edge precisely if \(w_i+w_j\le t\). For any nonempty subset \(I\) of indices, let \(E(I)\) be the edges of the induced graph \(T_t[I]\). Define a polynomial \(F_t(I;z)\) with nonnegative integer coefficients recursively:

- If \(E(I)=\varnothing\), put \(F_t(I;z)=2|I|-1\).
- Otherwise, let \(A(I)\) be the set of endpoints of \(E(I)\), put \(s=|I\setminus A(I)|\), take \(v\in A(I)\) with minimum weight (ties broken by index), and put
  \[F_t(I;z)=2s+zF_t(A(I)\setminus\{v\};z).\]
  The recursive argument is nonempty because every edge has two endpoints.

**Before the shortest antipodal threshold**, \(t<4w_1\), if \(F_t(\{1,\ldots,d\};z)=\sum_{q\ge0}b_qz^q\), then
\[K_r\simeq\bigvee_{q\ge0}\bigvee^{b_q}S^q.\]
Here the usual based-wedge convention for \(S^0\) gives \(b_0+1\) connected components; \(\bigvee^0S^q\) is omitted.

**At and beyond the shortest antipodal threshold**, \(t\ge4w_1\), let \(A\) be the set of nonisolated vertices of \(T_t\), \(I=\{1,\ldots,d\}\setminus A\), and let
\[c=\mathbf1_{\{A\ne\varnothing\}}+\sum_{i\in I}\bigl(1+\mathbf1_{\{t<4w_i\}}\bigr).\]
Then \(c\ge1\) and \(K_r\) is homotopy equivalent to exactly \(c\) discrete points, or \(\bigvee^{c-1}S^0\). In particular, **all positive-dimensional integral homology vanishes at every scale \(r\ge2a_1\)**.

Every reduced integral homology group at every stage is free. No persistence-map or barcode classification is asserted.

## Assumptions and scope
The \(2d\) points are distinct, \(a_i>0\), distances are ordinary Euclidean rather than graph or Hamming distances, and the threshold is inclusive. Equal lengths, tied pairwise distances, and threshold equalities are fully included. The theorem concerns stagewise homotopy types; it does not identify inclusion-induced homology maps.

## Proof
**1. Exact distance graph.** Distinct vertices on different coordinate axes have squared distance \(w_i+w_j\), independent of their signs; the antipodal pair on axis \(i\) has squared distance \(4w_i\). Therefore the Rips graph is obtained by replacing every axis vertex \(i\) of \(T_t\) by a two-vertex fiber \(F_i\). This fiber is a discrete \(S^0\) if \(t<4w_i\), or a filled edge \(\Delta^1\) if \(t\ge4w_i\); adjacent axes have complete bipartite cross-edges, and nonadjacent axes have none. The Rips complex is the clique complex of this graph.

**2. The unique active component.** In any nonempty induced subgraph \(T_t[J]\), if there is an edge and \(A(J)\) is its set of nonisolated vertices, choose a minimum-weight \(v\in A(J)\). For any \(j\in A(J)\setminus\{v\}\), there is an edge \(jk\). Since \(w_v\le w_j,w_k\), one has \(w_v+w_j\le w_j+w_k\le t\), so \(vj\) is an edge. Thus all nonisolated vertices lie in one connected component, and its minimum-weight axis is adjacent to every vertex of that component. This remains true recursively for all induced subgraphs. Ties do not change the argument.

**3. The pre-antipodal recurrence.** If \(t<4w_1\), every fiber is \(S^0\). Write \(J_t(I)\) for the clique complex of the two-point independent-fiber replacement of \(T_t[I]\). If \(T_t[I]\) has no edges, \(J_t(I)\) is \(2|I|\) separate points, i.e. \(\bigvee^{2|I|-1}S^0\). Otherwise the \(s\) isolated axes give \(2s\) separate points, while the active component has universal axis \(v\) by Step 2. The clique complex of that component is *simplicially equal* to
\[S^0*J_t(A(I)\setminus\{v\})=\Sigma J_t(A(I)\setminus\{v\}).\]
The reduced suspension of a space with homotopy type a finite wedge of spheres has sphere multiplicities shifted up by one, including when the original space is disconnected: the \(S^0\)-summands become \(S^1\)-summands. Reattaching \(2s\) isolated points adds \(2s\) copies of \(S^0\) to the wedge. This is precisely \(F_t(I;z)=2s+zF_t(A(I)\setminus\{v\};z)\). The recursion terminates because it removes at least one vertex. Induction proves both the asserted wedge homotopy type and its integral Betti multiplicities.

**4. The post-antipodal reduction.** For \(t\ge4w_1\), if \(T_t\) has an edge, axis \(1\) is active and adjacent to every active axis by Step 2. Its fiber is now the full edge \(\Delta^1\). Therefore the entire active-component clique complex is the join \(\Delta^1*L\) for a simplicial complex \(L\), and is contractible. An isolated axis \(i\) contributes independently one contractible edge if \(t\ge4w_i\), or two singleton components if \(t<4w_i\). If \(T_t\) has no edges, only these isolated fibers occur. Counting them gives exactly \(c\) contractible connected components, and hence the claimed discrete homotopy type. These arguments hold at equality because every edge test is weak.

**5. A genuinely mixed-dimensional stage.** Take \(d=4\), squared axis lengths \((100,113,212,218)\), and \(t=325\). The active threshold graph has edges \(12,13,14,23\), and no others. It consists of a triangle together with a pendant edge. Since \(325<400=4w_1\), the recurrence gives
\[F_{325}(\{1,2,3,4\};z)=z(z+2)=z^2+2z,\qquad K_{\sqrt{325}}\simeq S^2\vee S^1\vee S^1.\]
Thus unequal axes can create homology simultaneously in distinct positive dimensions. Conversely, for equal lengths the intermediate graph is complete and the only nontrivial connected stage is \(S^{d-1}\), recovering the classical regular-cross-polytope case.

## Verification
A standalone Python program `VERIFY.py` independently enumerates all cliques of the exact Euclidean Rips graphs at critical squared scales and computes reduced mod-two homology by explicit boundary-matrix reduction. The program checks 570 stages in dimensions \(1\) through \(7\), across 82 positive integral squared-axis-length vectors, including repeated lengths and scale equalities. These finite checks corroborate but do not prove the all-real, all-dimensional statement; Steps 1–4 above are the infinite proof. Run `python VERIFY.py`; successful completion prints `VERIFY_OK`. A complete recorded run is in `VERIFY_OUTPUT.txt`.

## Relationship to prior work
Saleh, Titz Mite and Witzel (arXiv:2302.14388, initial version February 28, 2023), Theorem and Lemma 2.2, calculate the regular octahedron and antipodal extremal complexes for regular Platonic solids; those are special symmetric instances, not this arbitrary-axis classification. Carnero Bravo (arXiv:2307.14321, first posted July 26, 2023), Theorem 7 and Corollary 8, develops broad suspended polyhedral-join decompositions and related graph constructions. Those tools are relevant context but neither state nor supply the exact Euclidean parameter inequalities and the unstabilized wedge recursion above. Adamaszek and Adams (arXiv:2103.01040) use shortest-path/Hamming distances on hypercube vertices, not the ambient Euclidean metric of deformed orthoplexes.

The graph substitution here is elementary and not claimed as a new general construction. The claimed contribution is the all-scale Euclidean identification, exact homotopy recurrence, sharp first-antipodal vanishing boundary, and mixed-degree phase in a natural dimension-independent deformation family. No novelty is claimed for the regular special case or for the basic join identity.

## Limitations
The classification is of individual filtered stages, not of all persistence intervals or maps. It is not an equivariant homotopy classification. Computational tests are finite and use mod-two coefficients, while the integral conclusion follows from the independent homotopy proof. Literature searches cannot rule out unindexed equivalent classifications; the most plausible overlap is a specialization of general polyhedral-join machinery, whose published statements were compared and do not explicitly assert this result.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (first posted 2023-02-28), especially the theorem and Lemma 2.2. https://arxiv.org/abs/2302.14388
2. A. Carnero Bravo, *Polyhedral joins and graph complexes*, arXiv:2307.14321 (first posted 2023-07-26), especially Theorem 7 and Corollary 8. https://arxiv.org/abs/2307.14321
3. M. Adamaszek, H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first posted 2021-03-01). https://arxiv.org/abs/2103.01040
