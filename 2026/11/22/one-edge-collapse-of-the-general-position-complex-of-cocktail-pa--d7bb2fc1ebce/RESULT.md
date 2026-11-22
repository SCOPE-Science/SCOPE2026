# One-edge collapse of the general-position complex of cocktail-party graphs

## Finding

For every integer \(n\geq 3\), let \(C_n\) be the cocktail-party graph on the disjoint pairs \(\{p_i,q_i\}\), \(1\leq i\leq n\): distinct vertices are adjacent except for the \(n\) pairs \(p_iq_i\). Delete the single existing edge \(p_1p_2\) to obtain \(G_n\). Define \(\operatorname{GP}(G)\) as the abstract simplicial complex whose faces are sets containing no three vertices on one shortest graph path. Then

\[
\operatorname{GP}(G_n)\simeq\bigvee^{n-1}S^1.
\]

In contrast, the unmodified cocktail-party graph satisfies

\[
\operatorname{GP}(C_n)\simeq S^{n-1}\vee\bigvee^n S^1.
\]

Thus deletion of exactly one graph edge destroys an integral top-dimensional sphere class in an unbounded dimension and reduces the fundamental-group rank by one. The two complexes do not have a natural inclusion relation, so this is a comparison of homotopy types, not a claim about an inclusion-induced map.

## Assumptions and scope

All graphs are finite, simple, connected, unweighted and undirected, and every shortest path is measured in the graph under discussion. The vertices \(p_i\) and \(q_i\) are distinct for all \(i\); the only nonedges of \(C_n\) are the \(p_iq_i\), and the additional nonedge of \(G_n\) is \(p_1p_2\). The theorem quantifies over every integer \(n\geq3\). Homotopy is ordinary homotopy of geometric realizations, with integral conclusions. No case \(n=2\) is included, because its modified graph has diameter three.

## Proof

**Metric characterization.** For \(n\geq3\), every nonedge of \(G_n\) has distance exactly two: for \(p_1p_2\), any vertex belonging to a third pair is a common neighbor; each \(p_iq_i\) also has a common neighbor outside its pair. All edges have distance one. Consequently, a three-element set is forbidden precisely when it contains a nonadjacent pair and a third vertex adjacent to both endpoints.

If a selected pair is \(\{p_i,q_i\}\) with \(i\geq3\), every third vertex is adjacent to both endpoints, so this pair cannot occur in any face of size at least three. If the pair is \(\{p_1,q_1\}\), the only third vertex which is not adjacent to both is \(p_2\); analogously \(\{p_2,q_2\}\) may only occur with \(p_1\). If the selected pair is the newly missing edge \(\{p_1,p_2\}\), the only possible third vertices are \(q_1,q_2\). The four-set \(\{p_1,p_2,q_1,q_2\}\) fails the criterion, so the only exceptional three-element faces are

\[
T_1=\{p_1,p_2,q_1\},\qquad T_2=\{p_1,p_2,q_2\}.
\]

**Exact simplicial decomposition.** Write \(D_i\) for the zero-sphere consisting of vertices \(p_i,q_i\) with no edge, and set

\[
J=D_3*D_4*\cdots*D_n.
\]

Let \(A\) be the three-edge path on \(p_1,q_2,q_1,p_2\), in that order. The face classification above gives the exact equality of simplicial complexes

\[
\operatorname{GP}(G_n)=
(A*J)\cup e_{12}\cup\bigcup_{i=1}^{n}e_i\cup T_1\cup T_2,
\]

where \(e_{12}=\{p_1,p_2\}\) and \(e_i=\{p_i,q_i\}\), and all edges/faces on the right include their proper subfaces. Indeed, \(A*J\) encodes all subsets containing no matched pair and not containing both \(p_1,p_2\). The other listed cells exhaust the cases with such a pair. This equality includes all empty and singleton faces.

**Two elementary collapses.** The edge \(e_1\) belongs to the unique two-simplex \(T_1\) and to no other two-simplex or higher-dimensional face. Therefore \((e_1,T_1)\) is a free face/coface pair; similarly \((e_2,T_2)\) is a free pair. Collapsing both yields the complex

\[
Y=(A*J)\cup e_{12}\cup\bigcup_{i=3}^{n}e_i.
\]

**Homotopy type.** The path \(A\) is contractible and nonempty, so \(A*J\) is nonempty, path connected and contractible (indeed collapsible because a path collapses onto a vertex and join preserves such a collapse). All endpoints of the \(n-1\) added edges \(e_{12},e_3,\ldots,e_n\) lie in \(A*J\), while none of these edges is in that subcomplex. Thus \(Y\) is obtained from a connected contractible CW complex by attaching \(n-1\) distinct one-cells along maps \(S^0\) to it. Collapsing its contractible subcomplex to one point is a homotopy equivalence for this CW pair and produces a bouquet of \(n-1\) circles. This proves the claimed integral homotopy equivalence for every \(n\geq3\), not just a homology calculation.

**Unmodified comparator.** In \(C_n\), a face either contains at most one vertex from each matched pair, or consists of a single matched pair. The first part of the complex is \(D_1*\cdots*D_n\cong S^{n-1}\), the boundary of an \(n\)-cross-polytope. Its \(n\) additional matched edges attach by their endpoints to a connected sphere. For \(n\geq3\), the result is \(S^{n-1}\vee\bigvee^n S^1\). The comparison is now complete.

## Verification

The included standalone `check.py` constructs the graph explicitly, recomputes all shortest-path distances using breadth-first search, enumerates all vertex subsets, tests every triple independently of the face formula, and compares the resulting complex to the exact decomposition for each \(3\leq n\leq8\). It also checks the exact face-counting polynomial

\[
\psi(G_n;z)=(1+2z)^n+n z^2-z^2\big((1+2z)^{n-2}-1\big)+2z^3,
\]

and computes simplicial homology over \(\mathbb F_2\) from full boundary matrices. Every test passes; see `expected-output.txt`. This finite enumeration corroborates, but does not replace, the all-parameter proof. Run with `python3 check.py` using Python 3.9 or later; no third-party dependencies are required.

## Relationship to prior work

Rather (2026, arXiv:2603.06930v1, first public March 6, 2026) describes all general-position sets and the enumerating polynomial for complete multipartite graphs, including the unmodified cocktail-party graphs. Iršič, Klavžar, Rus and Tuite (2024) develop general-position polynomials and give a counting formula for graph joins. Neither result states a homotopy classification of the present one-edge-defective family. The deleted-edge graph is not complete multipartite: nonadjacency fails transitivity among \(p_1,q_1,p_2\). Although the join-polynomial theorem can assist in enumerating faces, it does not identify the explicit free-face collapses or the resulting fundamental group. The unmodified comparator is included as a derivation, not claimed as a new result. The new claim concerns exactly the edge-deleted graph and its all-order homotopy transition.

## Limitations

This classification covers only deletion of one edge between vertices belonging to distinct two-vertex parts of \(C_n\). Automorphisms make all such deleted edges equivalent; it does not classify deletion of multiple edges, other complete multipartite part sizes, or any weighted geodesic convention. There is no assertion of an equivariant homotopy equivalence or natural inclusion map. An equivalent result not indexed by the searched literature remains a possible priority risk. Independent mathematical validation has not been performed.

## References

- Bilal Ahmad Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930v1 (2026-03-06), https://arxiv.org/abs/2603.06930.
- Vesna Iršič, Sandi Klavžar, Gregor Rus, James Tuite, *General Position Polynomials*, Results in Mathematics 79, article 110 (2024), https://doi.org/10.1007/s00025-024-02133-3.
