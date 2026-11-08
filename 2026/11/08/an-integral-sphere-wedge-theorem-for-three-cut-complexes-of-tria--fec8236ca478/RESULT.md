# An integral sphere-wedge theorem for three-cut complexes of triangular graphs

## Finding

Let \(n\ge5\) be an integer, and let \(J(n,2)=L(K_n)\) be the triangular graph with vertex set \(E(K_n)\). Its vertices are adjacent exactly when their corresponding edges of \(K_n\) share an endpoint. Put \(N=\binom n2\). The **ordinary three-cut complex** \(\Delta_3(J(n,2))\) has facets \(V(J(n,2))\setminus U\) for disconnected induced three-vertex subsets \(U\) of \(J(n,2)\). Then

\[
\Delta_3(J(n,2))\simeq\bigvee^{\binom{n-1}{4}} S^{N-6}.
\]

The integral reduced homology is free of rank \(\binom{n-1}{4}\) in degree \(N-6\) and zero in every other degree. The complex is pure of dimension \(N-4\), but it is not shellable. In particular, for \(n=5,6,7\), the homotopy types are respectively \(S^4\), \(\bigvee^5 S^9\), and \(\bigvee^{15}S^{15}\).

## Assumptions and scope

All graphs are finite, simple and undirected. A three-vertex induced subgraph is connected if and only if it has at least two edges. Simplicial complexes include the empty face, and the Alexander dual of a complex \(\Delta\) on the fixed \(N\)-element vertex set is \(\Delta^\vee=\{F:V\setminus F\notin\Delta\}\). Equivalently, the Alexander dual \(D_n=\Delta_3(J(n,2))^\vee\) is the downward-closed complex characterized by connected triples: a face \(F\subseteq E(K_n)\) belongs to \(D_n\) if and only if **every** three-edge subset of \(F\) induces a connected three-vertex subgraph in the line graph. In particular all subsets with at most two edges lie in \(D_n\). The theorem is about the *ordinary* cut complex, not the total-cut complex or the flag/clique complex of the Johnson graph.

## Proof

**1. Facets of the dual.** For every original vertex \(i\), write \(A_i\) for the full simplex on all \(n-1\) edges incident to \(i\); for every original four-element vertex set \(S\), write \(B_S\) for the full simplex on the six edges of \(K_n[S]\). Then

\[
D_n=\bigcup_{i=0}^{n-1}A_i\;\cup\!\bigcup_{S\in\binom{[n]}4}B_S.
\]

Indeed, every three edges of a star have intersecting pairs, and every three edges supported on four vertices have at least two pairs of intersecting edges. Conversely, if a nonempty edge family \(F\in D_n\) contains disjoint edges \(ab\) and \(cd\), any third edge in \(F\) must intersect each, and thus belongs to the four cross edges between \(\{a,b\}\) and \(\{c,d\}\). So \(F\subseteq E(K_4[\{a,b,c,d\}])\). If no pair of edges in \(F\) is disjoint, then \(F\) is a pairwise-intersecting family of edges. Such a family is contained in a star, or consists of three edges of a triangle; a triangle lies inside one of the four-vertex simplices since \(n\ge5\). This proves the displayed description.

**2. An acyclic matching on the dual.** Distinguish original vertex \(0\), and define a support map on the nonempty face poset by

\[
\phi(F)=\bigcup_{\{a,b\}\in F,\ a,b\ne0}\{a,b\}\subseteq\{1,\ldots,n-1\}.
\]

The map is inclusion-order-preserving. We construct an acyclic matching within each fiber of \(\phi\), then invoke the patchwork (cluster) lemma for acyclic matchings on fibers of an order-preserving poset map.

For a fixed positive-edge subset \(P=F\cap E(K_{n-1})\) with support \(S=\phi(F)\), the only variable edges are incident to \(0\). If \(S=\varnothing\), all nonempty faces form the simplex on the \(n-1\) edges \(0i\); toggling \(01\) matches every face except the single vertex \(\{01\}\), the unique critical zero-cell.

If \(|S|=2\), then \(P\) is a single edge and the allowed incident-zero additions form a cone with apex \(0\min S\). If \(|S|=3\), then \(P\) is either a two-edge star, in which case take apex \(0c\) with \(c\) its center, or the three-edge triangle, in which case take apex \(0\min S\). If \(|S|\ge5\), the dual-facet description forces \(P\) to be the full star on \(S\) with a uniquely determined center \(c\); the allowed incident-zero additions are precisely the empty set and \(\{0c\}\). In each case toggling the indicated apex edge pairs every face in the subfiber with fixed \(P\). Joining these matchings over the inclusion-ordered positive-edge sets \(P\) is acyclic by the patchwork lemma.

The exceptional fibers have \(|S|=4\). Four positive stars (each three edges) admit the same cone matchings with apex \(0c\) and hence no critical faces. Every other positive face has no allowable incident-zero edge and lies in the relative family \(\mathcal R_S\) of nonstar edge subsets of the six edges of \(K_4[S]\), each with full support \(S\). There are exactly thirty-seven such faces: three of size two, twelve of size three, fifteen of size four, six of size five, and one of size six. Order those six edges lexicographically, say \(ab,ac,ad,bc,bd,cd\) for \(a<b<c<d\), and repeatedly pair any remaining face not containing the current edge with its coface obtained by adding that edge, whenever both remain. This relative element-matching procedure is acyclic: at each pivot, the directed matching cannot produce a directed cycle since the fixed-pivot matching is by one toggled coordinate, and the unmatched poset at the next stage is an induced remainder. An exhaustive, independently executable directed-Hasse check of this universal thirty-seven-face matching is also supplied. It yields precisely fourteen pairs at the first pivot, three at the second, and one at the third, leaving exactly the four-edge face \(\{ab,bc,bd,cd\}\), a critical three-cell. All incidence relations between nonstar faces and star faces point from nonstar down to star, and no matched arrow crosses those classes, so no directed cycle mixes the two classes. The full size-four fiber is acyclic.

Finally, the global support map is order-preserving and all matches preserve support. Patchwork therefore gives an acyclic matching on the full nonempty face poset of \(D_n\), with exactly one critical vertex and one critical three-cell for each four-subset of \(\{1,\ldots,n-1\}\). Forman's discrete Morse theorem supplies a CW model with only a zero-cell and \(\binom{n-1}{4}\) three-cells; because no one- or two-cells exist, every attaching map of a three-cell is nullhomotopic. Hence

\[
D_n\simeq\bigvee^{\binom{n-1}{4}}S^3.
\]

**3. Duality and integral homotopy.** Integral combinatorial Alexander duality, with the above convention on \(N\) vertices, gives

\[
\widetilde H_i(\Delta_3(J(n,2));\mathbb Z)\cong\widetilde H^{N-i-3}(D_n;\mathbb Z).
\]

Thus the only nonzero reduced homology is \(\mathbb Z^{\binom{n-1}{4}}\) in degree \(d=N-6\). All dual facets have at most \(M=\max\{n-1,6\}\) vertices, so the cut complex contains the full \((N-M-2)\)-skeleton of the \((N-1)\)-simplex: a subset of at most \(N-M-1\) vertices has complement too large to be a dual face. For every \(n\ge5\), \(N-M-2\ge2\), so the cut complex is simply connected. Since its integral homology is concentrated in degree \(d\ge4\) and is free, successive Hurewicz arguments give a map from a wedge of \(\binom{n-1}{4}\) \(d\)-spheres inducing an integral homology isomorphism; the homological Whitehead theorem for simply connected CW complexes upgrades this to a homotopy equivalence.

The ordinary cut complex's facets are complements of disconnected three-sets, and all have cardinality \(N-3\), so the complex is pure of dimension \(N-4\). Its nonzero reduced homology lies in lower dimension \(N-6\). A pure shellable complex has reduced homology only possibly in top dimension. Hence this complex is not shellable.

## Verification

The included standard-library-only program `verify_triangular_cut.py` independently generates dual faces as the union of star and four-vertex simplices, checks the dual definition on every subset for \(n=5,6\), reconstructs the support-fiber matching for \(5\le n\le9\), enumerates all Hasse incidences, and checks the resulting directed graphs are acyclic by topological sorting. It checks precisely one critical vertex and \(\binom{n-1}{4}\) critical three-cells; its exact output is supplied in `verification_output.txt`. This finite verification supplements rather than replaces the preceding proof for all \(n\ge5\).

## Relationship to prior work

The definition and general theory of ordinary cut complexes follow Bayer and collaborators, *Topology of Cut Complexes of Graphs* (arXiv:2304.13675; initially posted April 26, 2023), and the continuation by Chauhan, Shukla and Vinayak (arXiv:2406.01979; initially posted June 4, 2024). The inspected primary papers treat other graph families rather than this all-parameter triangular-graph formula. Previously recorded results concern the **four-cut** complex of \(J(5,2)\), the **scale-one Vietoris–Rips/clique** complexes of Johnson graphs, and three-cut complexes under triangle-free or four-cycle-free hypotheses. None implies this theorem: triangular graphs contain triangles and four-cycles, while the cut parameter and the definition of the simplicial complex differ in the other comparisons. The clique-complex calculations of Goyal, Shukla and Singh (arXiv:2009.12130) similarly concern a different object. The present assertion is an integral *homotopy* classification of ordinary three-cut complexes across an infinite family, not a statement of their Euler characteristics alone.

## Limitations

The result is limited to the Johnson graphs \(J(n,2)\), \(n\ge5\), and cut parameter three. The argument does not describe the natural symmetric-group representation on homology, higher cut parameters, or general Johnson graphs \(J(n,k)\). The finite executable checker directly exhausts only \(5\le n\le9\); uniform validity rests on the explicit symbolic argument. Comparisons with accessible indexed and primary literature reduce but cannot eliminate the risk of equivalent unindexed earlier work. Independent external review has not been performed.

## References

- Bayer et al., *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, https://arxiv.org/abs/2304.13675 (first public version April 26, 2023).
- Chauhan, Shukla and Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979, https://arxiv.org/abs/2406.01979 (first public version June 4, 2024).
- Goyal, Shukla and Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, https://arxiv.org/abs/2009.12130 (comparator for a distinct complex).
- Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145 (acyclic matchings and CW collapse).
- Björner, *Topological Methods*, in Handbook of Combinatorics, 1995 (simplicial topology and Alexander duality).
