# Open-packing complexes of bipartite prisms and the exceptional pure six-rung ladder

## Finding

Let \(G\) be any finite simple bipartite graph (including disconnected graphs and isolated vertices), and let \(G^2\) be the graph obtained by joining distinct vertices at distance one or two in \(G\). Write \(\mathcal{OP}(H)\) for the simplicial complex of vertex subsets \(S\subseteq V(H)\) such that the open neighborhoods of distinct vertices in \(S\) are disjoint. Write \(\operatorname{Ind}(H)\) for the independence complex of \(H\), and \(\mathcal N(H)\) for the graph joining two distinct vertices precisely when they have a common neighbor in \(H\).

**Structural theorem.** There is a bipartition-dependent graph isomorphism
\[
\mathcal N(G\square K_2)\cong G^2\sqcup G^2.
\]
Consequently there is an isomorphism of simplicial complexes
\[
\mathcal{OP}(G\square K_2)\cong \operatorname{Ind}(G^2)*\operatorname{Ind}(G^2).
\]
If \(I_G(z)\) counts all distance-three packings of \(G\), including the empty one, and \(J_G(z)\) counts its inclusion-maximal distance-three packings, then the all-open-packing and inclusion-maximal-open-packing polynomials of the prism are **both exact squares**:
\[
O_{G\square K_2}(z)=I_G(z)^2,\qquad
M_{G\square K_2}(z)=J_G(z)^2.
\]
Here a distance-three packing means a set of vertices with pairwise graph distance at least three (equivalently, an independent set in \(G^2\)). The graph-level isomorphism also implies that the number of injective colorings with a specified palette of \(k\ge1\) labels is \(\chi_{G^2}(k)^2\), where \(\chi_{G^2}(k)\) is the usual chromatic polynomial evaluated at \(k\); thus \(\chi_i(G\square K_2)=\chi(G^2)\). This last color relationship is an immediate consequence of the structural theorem, not a separate priority claim.

**Complete ladder specialization.** Let \(L_n=P_n\square K_2\), for each \(n\ge1\). Define
\[
f_n(z)=\sum_{k=0}^{\lfloor(n+2)/3\rfloor}\binom{n-2k+2}{k}z^k,
\qquad
q_n(z)=[x^n]\frac{xz(1+x+x^2)^2}{1-z(x^3+x^4+x^5)}.
\]
Then the all-open-packing polynomial of \(L_n\) is \(f_n(z)^2\), and its inclusion-maximal-open-packing polynomial is \(q_n(z)^2\). The possible inclusion-maximal cardinalities form **every integer** in the interval
\[
2\left\lceil\frac n5\right\rceil
\ \le k\le\
2\left\lfloor\frac{n+2}{3}\right\rfloor.
\]
In particular, \(\mathcal{OP}(L_n)\) is pure if and only if \(n\in\{1,2,3,6\}\). The six-rung ladder is pure even though the four- and five-rung ladders are not, and no larger ladder is pure.

## Assumptions and scope

Graphs are finite, undirected, simple and labelled. Graph distance between vertices in different components is infinite. The square \(G^2\) has edges between **distinct** vertices at distance at most two; it has no loops. The Cartesian product has vertex set \(V(G)\times\{0,1\}\), with the usual horizontal edges from \(G\) and a vertical matching edge at each base vertex. In the disconnected case, choose any bipartition of each component; the claimed isomorphism need not be canonical before that choice. Polynomials count labelled vertex subsets. The simplicial join uses disjointly labelled copies of its two factors. The purity statement refers to all inclusion-maximal faces, not only maximum-size faces.

## Proof

**Step 1: compute the common-neighbor relation.** Fix distinct prism vertices \((u,i)\) and \((v,j)\). If \(i=j\), a shared neighbor can only be in that same layer and be a common neighbor of \(u\) and \(v\) in \(G\); the vertical neighbor of \((u,i)\) is \((u,1-i)\) and cannot be a neighbor of \((v,i)\) unless \(u=v\), which has been excluded. Thus for equal layers the common-neighbor condition is exactly that \(u,v\) have a common neighbor in \(G\). If \(i\ne j\), a shared neighbor exists precisely when \(uv\in E(G)\): then \((u,j)\) and \((v,i)\) are common neighbors, while if \(uv\notin E(G)\), the two possible vertical-horizontal intermediates cannot occur. This also shows that the vertical pair \((u,0),(u,1)\) is not an edge in the common-neighbor graph.

**Step 2: use bipartition parity.** Choose a bipartition map \(c:V(G)\to\{0,1\}\) such that every edge reverses \(c\). Relabel the prism vertex \((u,i)\) by \((u,i\oplus c(u))\). For fixed new layer \(h=i\oplus c(u)\), vertices \((u,i)\), \((v,j)\) have a common neighbor exactly when either their base vertices are adjacent (opposite colors, opposite original layers) or have a common neighbor (same colors, same original layer). These two alternatives are exactly \(d_G(u,v)\in\{1,2\}\). If their new layers differ, the two preceding alternatives are both impossible. Thus the relabeling identifies the common-neighbor graph with two disjoint copies of \(G^2\); isolated base vertices cause no exception.

**Step 3: transfer the complete complexes and all cardinalities.** A set is an open packing precisely when it is independent in the common-neighbor graph, by definition. The independence complex of a disjoint union is the simplicial join of the component independence complexes. Its full face polynomial is the product of their full face polynomials. Moreover, a face in a join is inclusion-maximal if and only if its restriction to each factor is inclusion-maximal. Hence both polynomial-square identities follow. Proper \(k\)-colorings of a disjoint union count multiplicatively; injective colorings are precisely proper colorings of the common-neighbor graph. This proves the color consequence, including the minimum number of colors.

**Step 4: count all path distance-three packings.** Label \(P_n\) by \(1,\dots,n\). An independent set of \(P_n^2\) has indices \(1\le s_1<\cdots<s_k\le n\) satisfying \(s_{i+1}-s_i\ge3\). Map them to \(t_i=s_i-2(i-1)\). This bijects the \(k\)-sets with ordinary \(k\)-subsets of \(\{1,\dots,n-2k+2\}\). Therefore their number is \(\binom{n-2k+2}{k}\), giving \(f_n(z)\) and the all-open-packing formula.

**Step 5: characterize path facets.** A distance-three packing \(S=\{s_1<\cdots<s_k\}\) of \(P_n\) is inclusion-maximal exactly when the closed radius-two neighborhoods of its vertices cover \(\{1,\dots,n\}\). Necessity follows because any uncovered vertex can be added while retaining pairwise distance at least three; sufficiency is immediate. In terms of positions, maximality is exactly
\[
0\le s_1-1\le2,\qquad 3\le s_{i+1}-s_i\le5,\qquad 0\le n-s_k\le2.
\]
For \(k\ge1\), write the initial and final offsets as \(a,b\in\{0,1,2\}\) and each of the \(k-1\) internal gaps as an element of \(\{3,4,5\}\). The length is
\[
n=1+a+b+\sum_{i=1}^{k-1}(s_{i+1}-s_i).
\]
Thus the ordinary generating function for these maximal sets, with \(x\) recording path order and \(z\) recording cardinality, is
\[
\sum_{n\ge1}q_n(z)x^n=
\frac{xz(1+x+x^2)^2}{1-z(x^3+x^4+x^5)}.
\]
This proves the maximal-polynomial formula for the ladder by Step 3.

**Step 6: determine the facet spectrum and purity without extrapolating finite data.** For a fixed cardinality \(k\ge1\), the smallest path order represented by the offsets and gaps is \(3k-2\), and the largest is \(5k\). Every intermediate order is represented because the offsets and gaps independently range through consecutive integer intervals. Hence a maximal distance-three packing of \(P_n\) has cardinality \(k\) if and only if
\[
\left\lceil\frac n5\right\rceil\le k\le \left\lfloor\frac{n+2}{3}\right\rfloor.
\]
Joining two independent copies gives all pairwise sums of these sizes, exactly the integer interval stated in the finding. The endpoints agree precisely for \(n\in\{1,2,3,6\}\). Explicitly, equality holds for \(n=1,2,3,6\); it fails for \(n=4,5,7,8,9\); and for \(n\ge10\) one has \(\lceil n/3\rceil>\lceil n/5\rceil\). The criterion gives the announced purity classification. This ends the proof.

## Verification

The companion standalone standard-library Python program `check_prism.py` directly builds the prism and its common-neighbor graph and compares **every adjacency** with the proposed two-copy square graph after the explicit parity relabeling. It enumerates independent sets and checks both sides' full coefficient vectors for every bipartite labelled simple graph of order at most five, allowing disconnected graphs and isolated vertices. The program also constructs paths through order twelve, tests both closed formulas by enumeration, checks all possible maximal-set cardinalities, and independently enumerates maximal open packings of prism ladders through seven rungs. A five-cycle is used as an essential negative boundary check (its prism common-neighbor graph is connected). All checks completed successfully with `VERIFY_OK`; these finite calculations support but do not constitute the infinite proof.

## Relationship to prior work

Brešar, Klavžar and Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963v1 (first submitted 2023-09-10), Theorem 2.2, proved the **scalar** identity \(\rho^{\mathrm o}(G\square K_2)=2\rho_2(G)\) for bipartite \(G\). Their full Section 2 was examined; the factorization of all feasible sets and all maximal sets is a strictly stronger statement than this scalar equality, and their transformation argument does not state the two-copy common-neighbor graph isomorphism. Mojdeh, Peterin, Samadi and Yero, arXiv:1901.06813 (2019), studied scalar packing numbers of graph products but not these complete complexes. Brešar, Samadi and Yero, arXiv:2106.09823 (2021), established general uses of the common-neighbor graph for injective coloring, and Samadi, Soltankhah and Yero, arXiv:2306.01488 (2023), studied injective coloring of other products; neither paper's inspected full sections supplied the prism factorization or ladder maximal-open-packing classification. Basic facts identifying open packings with independent sets of the two-step graph, and injective colorings with its proper colorings, are prior knowledge and are not separately claimed as new.

## Limitations

The theorem requires a bipartite base graph for the two-copy square decomposition. For example, the common-neighbor graph of \(C_5\square K_2\) is connected, so the claimed decomposition fails for that nonbipartite base. No claim is made about nonbipartite bases, about uniqueness of the bipartition choice on disconnected graphs, or about independent external verification. The exact ladder formulas are structural consequences of a general decomposition, not new extremal values alone. Publication priority is provisional: the 2015 article *Injective coloring of some graph operations* by Song and Yue, DOI 10.1016/j.amc.2015.03.124, was located but its relevant full text could not be accessed; it may contain overlapping scalar coloring results. An equivalent full-family decomposition could also appear under different terminology. These are originality risks, not exceptions to the proof.

## References

1. B. Brešar, S. Klavžar and D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963v1, 2023-09-10. https://arxiv.org/abs/2309.04963
2. D. A. Mojdeh, I. Peterin, B. Samadi and I. G. Yero, *(Open) packing number of some graph products*, arXiv:1901.06813, 2019-01-21. https://arxiv.org/abs/1901.06813
3. B. Brešar, B. Samadi and I. G. Yero, *Injective coloring of graphs revisited*, arXiv:2106.09823v1, 2021-06-17. https://arxiv.org/abs/2106.09823
4. B. Samadi, N. Soltankhah and I. G. Yero, *Injective coloring of product graphs*, arXiv:2306.01488v1, 2023-06-02. https://arxiv.org/abs/2306.01488
5. J. Song and J. Yue, *Injective coloring of some graph operations*, Applied Mathematics and Computation 264 (2015), 279–283. DOI:10.1016/j.amc.2015.03.124. Relevant full text inaccessible at the time of comparison.
