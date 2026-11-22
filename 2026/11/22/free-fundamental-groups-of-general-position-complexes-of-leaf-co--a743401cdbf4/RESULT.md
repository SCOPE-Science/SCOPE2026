# Free fundamental groups of general-position complexes of leaf coronas over two-connected graphs

## Finding

Let \(G\) be a finite simple graph with \(v=|V(G)|\ge3\) such that \(G-w\) is connected for every vertex \(w\). Let \(G\circ K_1\) mean the graph made by adjoining a private pendant leaf \(\ell_w\) to every vertex \(w\) of \(G\). Define \(\operatorname{GP}(H)\) to be the simplicial complex of all vertex subsets with no three vertices on one geodesic of the unweighted graph \(H\). A triple is forbidden whenever one of its vertices lies on **any** shortest path between the other two.

For each edge \(uv\in E(G)\), call it *unbalanced* when no third vertex \(w\in V(G)\setminus\{u,v\}\) has equal graph distances to its ends: \(d_G(w,u)=d_G(w,v)\). Let \(b(G)\) be the number of unbalanced edges. Then

\[
\boxed{\pi_1(|\operatorname{GP}(G\circ K_1)|)\cong F_{v+b(G)},\qquad H_1(|\operatorname{GP}(G\circ K_1)|;\mathbb Z)\cong\mathbb Z^{v+b(G)},}
\]

where \(F_r\) is the free group of rank \(r\). The realization is connected and the group is independent of the chosen basepoint up to inner automorphism. In particular, for the sunlet \(S_v=C_v\circ K_1\), \(\pi_1(|\operatorname{GP}(S_v)|)\cong F_v\) if \(v\) is odd and \(F_{2v}\) if \(v\) is even. If \(G\) is bipartite and satisfies the stated vertex-deletion condition, then every edge is unbalanced and the rank becomes \(v+|E(G)|\).

## Assumptions and scope

All graphs are finite, simple, unweighted and undirected. The hypothesis that every vertex deletion leaves \(G\) connected is essential to the proof: it makes a certain auxiliary leaf-link component connected. No assertion is made for a graph with a cut vertex, for the entire homotopy type, or for any integral homology group above degree one. All graph distances are computed in \(G\), not in the corona, when evaluating \(b(G)\). The result concerns the full simplicial complex, not just the graph-theoretic general-position number or polynomial.

## Proof

Write the original vertices as \(r_i\) and their leaves as \(\ell_i\), with labels \(i\in V(G)\). Put \(X=\operatorname{GP}(G\circ K_1)\), and let \(L\subset X\) be the simplex on all pendant leaves. Indeed, a leaf cannot be the interior of a graph path, so any set of leaves is in general position. Every two distinct vertices of \(X\) span an edge because the forbidden configurations have size three.

**1. A cone union with exactly \(v\) free fundamental generators.** For each original vertex \(i\), let \(L_i\) be the simplicial complex consisting of those faces of \(L\) that can be joined to \(r_i\) inside \(X\). The leaf \(\ell_i\) is an isolated vertex in \(L_i\): any other leaf \(\ell_j\) has every shortest path to \(\ell_i\) passing through \(r_i\). On the other hand, all other leaves belong to one connected component of \(L_i\). To see this, if \(jk\) is an edge of \(G-i\), the triple \(\{r_i,\ell_j,\ell_k\}\) is in general position: the path from \(\ell_j\) to \(\ell_k\) goes through the adjacent roots \(j,k\), with no interior occurrence of \(i\); neither leaf can be interior to another path. Thus the edge \(\ell_j\ell_k\) is in \(L_i\). Connectivity of \(G-i\) proves connectivity of the nonisolated part of \(L_i\).

Let \(Y=L\cup\bigcup_i(r_i*L_i)\), the subcomplex with at most one original vertex in any simplex. The cones have pairwise intersections wholly inside the contractible simplex \(L\). Collapsing \(L\) to a point is a homotopy equivalence of the connected CW complex \(Y\), and the result is a wedge, over \(i\), of the suspensions of the two-component complexes \(L_i\). Van Kampen (or the suspension fundamental-group calculation) therefore gives \(\pi_1(Y)\cong F_v\). Explicitly, one generator for site \(i\) traverses the edge from \(r_i\) to its own leaf, travels through \(L\), and returns to \(r_i\) through a leaf in the other component of \(L_i\). The particular leaf chosen in that other component does not change the homotopy class of this generator.

**2. Exactly which original-original edges cannot be paired with a triangle.** For distinct roots \(r_i,r_j\), a leaf \(\ell_k\) completes an allowable simplex \(\{r_i,r_j,\ell_k\}\) if and only if \(k\notin\{i,j\}\) and neither of \(i,j\) lies on a shortest path from \(k\) to the other root. Indeed, the length-one leaf segment cancels when the two possible geodesic equalities are compared in \(G\). If \(ij\notin E(G)\), choose an internal vertex \(k\) on a shortest \(i\)-to-\(j\) path; both relevant triangle inequalities are strict, so such a leaf exists. If \(ij\in E(G)\), the inequalities are strict precisely when \(d_G(k,i)=d_G(k,j)\), since adjacent vertices have distances differing by at most one. Thus \(r_ir_j\) has no allowable leaf triangle exactly when \(ij\) is one of the \(b(G)\) unbalanced edges.

An unbalanced root-root edge lies in **no** triangle of \(X\) of any kind. We have just excluded triangles containing a leaf. For a third original vertex \(k\), the adjacent endpoints have distances from \(k\) differing by one (because equality is excluded), hence one of \(i,j\) lies on a shortest path from \(k\) to the other. Consequently, \(\{r_i,r_j,r_k\}\) is forbidden. These \(b(G)\) root-root edges are therefore maximal one-dimensional simplices.

**3. All remaining attachments preserve the free fundamental group.** For each root-root edge \(r_ir_j\) other than the \(b(G)\) unbalanced ones, choose one allowed leaf \(\ell_k\), and adjoin both the edge \(r_ir_j\) and the triangle \(\{r_i,r_j,\ell_k\}\) to \(Y\). Attaching the pair has the homotopy type of attaching a 2-simplex along the two pre-existing sides; the new edge and triangle cancel as a relative elementary expansion. This leaves the fundamental group \(F_v\) unchanged. Now adjoin the \(b(G)\) unbalanced edges, which connect pairs of vertices already joined in the connected complex \(Y\). With no triangles yet attached to these edges, each contributes one additional free circle generator. This intermediate complex has fundamental group \(F_{v+b(G)}\).

It remains to examine other two-dimensional faces. All allowed triangles of the form \(\{r_i,r_j,\ell_h\}\) have \(h\ne i,j\). The chosen leaf \(\ell_k\) for the same root pair and the new leaf \(\ell_h\) are therefore in the **same connected nonisolated component** of each of \(L_i\) and \(L_j\). Paths between them inside these link components, coned to \(r_i\) and \(r_j\), together with paths inside the contractible \(L\), nullhomotope the remaining triangle boundary. More uniformly, after contracting \(L\), all paths from a root \(r_i\) to a leaf \(\ell_h\) with \(h\ne i\) represent one fixed fundamental-groupoid arrow \(p_i\); every paired root edge \(r_ir_j\) represents \(p_i p_j^{-1}\). Thus every remaining two-root/one-leaf boundary is nullhomotopic.

For a triangle on three roots, all its three root-root edges are paired edges, since an unbalanced edge occurs in no such triangle. Its boundary then represents \((p_i p_j^{-1})(p_j p_k^{-1})(p_k p_i^{-1})=1\). Hence none of the remaining two-cells changes the fundamental group by van Kampen. Higher-dimensional faces do not change \(\pi_1\). This proves \(\pi_1(X)\cong F_{v+b(G)}\). Abelianizing gives the integral first homology statement, including torsion-freeness.

**4. Corollaries.** In any bipartite graph, the two endpoints of an edge belong to opposite color classes and their distances from a third vertex have opposite parity. Thus no edge has an equidistant witness, and \(b(G)=|E(G)|\). For \(C_v\), every edge is unbalanced when \(v\) is even, whereas for odd \(v\) each edge has the uniquely antipodal cycle vertex equidistant from its endpoints. Therefore \(b(C_v)=v\) or \(0\) according to parity, proving the displayed sunlet specialization.

## Verification

The standalone program `verify_general.py` builds each sampled or exhaustively enumerated two-vertex-connected base graph, forms its actual leaf corona, recomputes graph distances by breadth-first search, independently enumerates every permissible triangle, and obtains the dimension of first homology over \(\mathbb F_2\) by binary boundary-matrix elimination. It verifies the predicted \(v+b(G)\) for all 249 labeled graphs of orders three through five satisfying the hypothesis, and for 220 additional seeded samples of orders six through eight (65, 98, and 57 respectively). The graph-order-four and five counts include all labeled examples, not just isomorphism representatives.

`verify_sunlet.py` separately verifies the corollary by fresh graph-distance calculations over all triples, by elimination modulo \(2,3,5\) for cycle lengths three through fourteen, and modulo \(2\) at lengths fifteen, sixteen, eighteen, and twenty. It directly checks the exceptional-root-edge characterization and link connectivity. The exact recorded outputs are `verification_general_output.txt` and `verification_sunlet_output.txt`. These finite homology calculations do not, by themselves, prove freeness of the fundamental groups; that conclusion follows from the all-graph van Kampen argument above.

## Relationship to prior work

The general-position polynomial and the corona operation are established graph-theoretic objects. Rather's 2026 study of general-position polynomials treats corona graph classes and explicitly gives the six-cycle sunlet polynomial. The October 2026 sunlet study *General-position polynomials of sunlet graphs via cyclic gaps* obtains the full face enumeration for all cycle coronas; its entire published `RESULT.md` was inspected. Neither numerical enumeration nor the cyclic-gap criterion determines the fundamental group. The theorem here treats **every graph whose vertex deletions remain connected**, extracts an edge-equidistance invariant, and obtains the nonabelian free-group isomorphism and integral first homology, including a parity discontinuity for cycle coronas and the rank \(v+|E(G)|\) for two-connected bipartite bases.

The distinction is the nonabelian topological invariant: polynomial coefficients, even when known exactly, do not alone determine the fundamental group. A differently indexed or implicit earlier group classification may exist; publication priority is not asserted as a theorem.

## Limitations

The theorem makes no higher-homotopy, full homotopy-wedge, or high-degree integral homology claim. For graphs with a cut vertex the nonisolated part of a root's leaf link need not be connected and the argument does not apply. The finite verifier checks first homology only; it cannot certify an infinite family or a nonabelian presentation. Unindexed equivalent literature is a residual originality risk. Independent mathematical validation has not been carried out.

## References

1. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (first posted 2026-03-06), https://arxiv.org/abs/2603.06930 .
2. *General-position polynomials of sunlet graphs via cyclic gaps*, published 2026-10-12, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-general-position-polynomials-of-sunlet-graphs-via-cyclic-gaps--eea66c0e3a48 . The full published `RESULT.md` supplies the cyclic-gap characterization and all-order enumerator.
3. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General position polynomials*, arXiv:2401.05696 (2024), https://arxiv.org/abs/2401.05696 .
4. U. Chandran S. V., S. Klavžar, J. Tuite, *The General Position Problem: A Survey*, arXiv:2501.19385 (first posted 2025-01-31), https://arxiv.org/abs/2501.19385 .
