# Vertex–edge resolving equivalence of crown graphs and complete prisms

## Finding

For every integer \(n\ge3\), let \(C_n=K_{n,n}\setminus M_n\) be the crown graph on vertices \(a_i,b_i\) (\(i\in[n]\)), with edges \(a_ib_j\) when \(i\ne j\). For any \(S\subseteq V(C_n)\), write
\[
J(S)=\{i\in[n]:\{a_i,b_i\}\cap S\ne\varnothing\}.
\]
**Theorem.** A set \(S\) resolves all vertices of \(C_n\) if and only if it resolves all edges of \(C_n\) (using vertex-to-edge distance). Both conditions hold exactly when \(|J(S)|\ge n-1\). For \(n\ge4\), under the natural vertex identification \(a_i\leftrightarrow(0,i)\), \(b_i\leftrightarrow(1,i)\), these are *also precisely all ordinary vertex-resolving sets* of the complete prism \(P_n=K_2\square K_n\).

Thus the two different resolving tasks on \(C_n\), and the vertex-resolving task on the nonisomorphic graph \(P_n\), have **identical families of feasible landmark subsets**, not merely equal optimum sizes. In particular, all three tasks share their size distribution and every feasible-set reconfiguration graph. The full cardinality polynomial for each is
\[
\mathcal R_n(z)=\bigl(2z+z^2\bigr)^n+n\bigl(2z+z^2\bigr)^{n-1}.
\]
The crown equality holds from \(n=3\), while the prism equality starts sharply at \(n=4\). The polynomial on the crown vertex side and the minimum edge metric basis count are already present in earlier work; the contribution assessed here is the unrestricted **vertex-versus-edge and cross-graph equivalence**.

**Reconfiguration consequence.** For \(n\ge4\), consider token addition/removal (TAR) on any of these three feasible-set families, subject to budget \(k\). The three resulting labeled graphs coincide. Their number of connected components is
\[
c_n(k)=\begin{cases}0,&k<n-1,\\n2^{n-1},&k=n-1,\\1,&k\ge n.\end{cases}
\]
(The empty state graph is assigned zero components.) Each family has exactly \(n2^{n-1}\) inclusion-minimal sets, all of size \(n-1\).

## Assumptions and scope

All graphs are finite, simple, and connected, and \(n\ge3\) except where the prism condition requires \(n\ge4\). A vertex-resolving set distinguishes each pair of distinct vertices by distances to some selected vertex. An edge-resolving set distinguishes each pair of distinct edges by \(d(s,uv)=\min\{d(s,u),d(s,v)\}\). Vertex subsets are understood as unlabeled sets of *labeled vertices*, and the generating polynomial counts each subset once. Feasibility is upwards closed.

## Proof

**1. Crown vertex signatures.** Distances within either shore of \(C_n\) are \(0\) at the same vertex and \(2\) between distinct vertices. Across shores they are \(1\) except between \(a_i,b_i\), whose distance is \(3\) (there is a three-edge route because \(n\ge3\)). Any chosen landmark separates every pair containing one \(a\)-vertex and one \(b\)-vertex: its two distances have opposite parity. For \(a_i,a_j\) with \(i\ne j\), either selected endpoint separates them; when neither is selected, precisely \(b_i,b_j\) can distinguish them. Likewise for \(b_i,b_j\). Hence unresolved pairs occur exactly when two distinct indices \(i,j\) have both matched vertices unselected. The vertex-resolving criterion is \(|J(S)|\ge n-1\).

**2. Crown edge signatures.** The edges are the ordered incidence pairs \(e_{ij}=a_ib_j\), \(i\ne j\). For a chosen landmark \(a_k\), the distance to \(e_{ij}\) equals \(0\) if \(k=i\), \(2\) if \(k=j\), and \(1\) otherwise. At a chosen \(b_k\) it equals \(0\) if \(k=j\), \(2\) if \(k=i\), and \(1\) otherwise. Thus in either shore, a landmark of index \(k\) separates two edges precisely when their respective *roles* of index \(k\) (first endpoint, second endpoint, neither) differ. Represent the roles of \(e_{ij}\) by the vector \(e_i-e_j\in\mathbb Z^n\), where \(e_i\) is the standard basis vector. Two distinct edges give distinct vectors: if \(e_i-e_j=e_p-e_q\), the unique positive and negative positions imply \(i=p\) and \(j=q\). Their difference is a nonzero integer vector with coordinate sum zero, so it has at least two nonzero coordinates. Consequently, if at most one index is unselected, some chosen landmark has a differing role and resolves every edge pair.

Conversely, suppose indices \(u\ne v\) are both absent from \(J(S)\). Choose \(r\notin\{u,v\}\), possible for \(n\ge3\). The distinct edges \(e_{ru}\) and \(e_{rv}\) have identical roles at every selected index; they are not edge-resolved. This proves exact equivalence of vertex- and edge-resolution for the crown graph.

**3. Complete-prism vertex signatures.** A set in \(P_n=K_2\square K_n\) occupies the column indexed by \(i\) precisely when its corresponding crown set meets \(\{a_i,b_i\}\). With two omitted columns, the two cells in either fixed row of those columns have identical landmark distances, so a resolving set must occupy at least \(n-1\) columns. Conversely, suppose at least \(n-1\ge3\) columns are occupied. The 2005 characterization of rook-graph resolving sets (Cáceres et al., Lemma 6.2) requires at most one empty row, at most one empty column, at most one lonely landmark (alone in both its row and column), and forbids the joint occurrence of one empty row, one empty column and one lonely landmark. The column requirement is immediate. Since at least three columns are occupied, two lonely landmarks would require both rows to have exactly one chosen vertex, hence at most two occupied columns, impossible. If a row is empty, the other row has at least three chosen vertices, so no landmark is lonely. All characterization conditions hold; therefore \(S\) resolves \(P_n\). This derives the claimed three-family equivalence for \(n\ge4\).

The endpoint is sharp: at \(n=3\) the set \(\{a_1,b_2\}\) resolves vertices and edges of the six-cycle \(C_3\), but the corresponding two prism landmarks lie alone in distinct rows and columns and fail to resolve \(P_3\).

**4. Counting and irredundance.** Each occupied index can contribute \(a_i\), \(b_i\), or both, giving weight \(q(z)=2z+z^2\). A feasible set occupies all \(n\) indices or exactly \(n-1\) indices. The former contributes \(q(z)^n\); the latter contributes \(nq(z)^{n-1}\). Inclusion-minimality forces exactly one chosen vertex in each of \(n-1\) pairs and none in the remaining pair: there are \(n2^{n-1}\) such sets. The previously known scalar metric dimensions \(n-1\) follow, but are not separately claimed as new.

**5. TAR connectivity.** Below \(n-1\) there are no states. At \(n-1\), all states are the minimal sets just described, hence isolated. At budget \(n\), two minimal states that differ in the chosen shore within an occupied pair are joined by first adding the alternate vertex and then deleting the former vertex. To move the single empty index from \(i\) to \(j\), add a chosen vertex at \(i\), then delete the chosen vertex at \(j\). All minimal states therefore lie in one component. Any larger feasible set reduces by removing extra vertices in occupied pairs and, if necessary, one occupied pair, to some minimal set; the reductions remain feasible. Thus the whole TAR graph is connected at budget \(n\) and every higher budget. Since the feasible families are identical under the natural identification, the reconfiguration graphs are literally identical.

## Verification

The stand-alone Python 3 verifier `verify_crown_prism61.py` constructs graph-distance matrices independently by shortest-path relaxation, tests every landmark subset by its complete vertex and edge distance signatures for crowns of order \(n=3,4,5,6\), and checks the corresponding vertex signatures in complete prisms for \(n=4,5,6\). It tests \(5,440\) subsets, the formula coefficientwise, basis counts, and directly builds TAR components at budgets adjacent to the threshold for \(n=4,5\). It reports `VERIFY_OK`. This is finite corroboration, not the proof for unbounded \(n\).

## Relationship to prior work

Cáceres et al. (first public version 2005) already gave a complete resolving-set characterization for Cartesian products of complete graphs (Lemma 6.2), and the exact metric dimension, so these are explicitly **not** new. Saputro et al. (2011) already determined the vertex metric dimension of \((n-1)\)-regular bipartite graphs, which include crowns. Knor et al. (2020) study how vertex and edge metric dimensions differ across graph families; they do not identify equality of the entire resolving-set families for crowns. Hakanen et al. (2020) analyze a stronger \(\{2\}\)-resolving task for rook graphs, not this three-way equivalence. A related earlier database result classifies only *minimum edge metric bases* of crowns, with count \(n2^{n-1}\); that minimum count and the crown vertex resolving polynomial have prior coverage and are not presented as independently new facts. The new point is equality for **every subset of all sizes**, including different resolution tasks and nonisomorphic graphs, and resulting identical full TAR state spaces.

## Limitations

The prism assertion fails at \(n=3\) and is not asserted there; crown graph connectedness excludes \(n=2\). No result is asserted for higher-dimensional rook graphs or multi-vertex resolution. The nonisomorphic graphs have the same feasible landmark subsets only under the specified labeling; their actual metric distance matrices are different. External independent review has not been performed. Publication priority remains provisional because unindexed equivalents and publications not fully accessible here may exist.

## References

1. J. Cáceres, C. Hernando, M. Mora, I. M. Pelayo, M. L. Puertas, C. Seara, D. R. Wood, *On the Metric Dimension of Cartesian Products of Graphs*, arXiv:math/0507527 (first public 2005-07-26), especially Theorem 6.1 and Lemma 6.2.
2. S. W. Saputro, E. T. Baskoro, A. N. M. Salman, D. Suprijanto, M. Baca, *The Metric Dimension of Regular Bipartite Graphs*, arXiv:1101.3624 (2011-01-19), especially Theorem 1.
3. M. Knor, S. Majstorović, A. T. M. Toshi, R. Škrekovski, I. G. Yero, *Graphs with the edge metric dimension smaller than the metric dimension*, arXiv:2006.11772 (first public 2020-06-21).
4. A. Hakanen, V. Junnila, T. Laihonen, M. L. Puertas, *On the Metric Dimensions for Sets of Vertices*, arXiv:2003.02048 (2020-03-04), Section 4.1.
