# A matching-deletion law for dominant edge-metric generators of complete bipartite graphs

## Finding

Let \(m,n\geq3\), let \(0\leq t\leq\min(m,n)\), and let \(G_{m,n,t}\) be obtained from \(K_{m,n}\) by deleting a matching of \(t\) edges. Put \(N=m+n\), \(u=m-t\), and \(v=n-t\). A *dominant edge-metric generator* is a vertex cover that distinguishes every pair of edges by their distance vectors from its selected vertices.

For any dominant edge-metric generator \(S\), count its **omitted vertices** by \(z^{N-|S|}\). The complete polynomial is

\[
H_{m,n,t}(z)=\sum_{S\text{ dominant edge-metric}}z^{N-|S|}=(1+z)^t\bigl(2+(u+v)z\bigr)-1+t z^2.
\]

Thus the polynomial by the number of **selected** vertices is exactly \(z^N H_{m,n,t}(1/z)\), interpreted as a polynomial after cancellation.

The polynomial of *inclusion-minimal* dominant edge-metric generators, by selected cardinality, is

\[
M_{m,n,t}(z)=(u+v)z^{N-t-1}+t z^{N-2}+
\bigl(\mathbf{1}_{u=0}+\mathbf{1}_{v=0}\bigr)z^{N-t}.
\]

Here the indicator \(\mathbf{1}_{P}\) is one when statement \(P\) holds and zero otherwise. Therefore the dominant edge-metric dimension is

\[
\operatorname{Ddim}_e(G_{m,n,t})=
\begin{cases}
N-t-1,&u+v>0,\\
t,&u=v=0\quad(m=n=t).
\end{cases}
\]

The number of minimum generators is \(N\) when \(t=0\), \(N-1\) when \(t=1\), \(N-2t\) when \(t\geq2\) and \(u+v>0\), and \(2\) when \(u=v=0\). These count subsets of a fixed labeled graph, not vertex-isomorphism types.

## Assumptions and scope

The graph is simple, finite, unweighted and connected. Name the shores \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_n\}\), with precisely the nonedges \(a_i b_i\) for \(1\leq i\leq t\). The unmatched vertices in a shore are those with index larger than \(t\). An edge \(e=xy\) has distance \(d_G(w,e)=\min\{d_G(w,x),d_G(w,y)\}\) from a vertex \(w\). A set \(S\subseteq V(G)\) resolves edges when each distinct pair \(e,f\in E(G)\) has \(d_G(w,e)\ne d_G(w,f)\) for some \(w\in S\). A vertex cover contains at least one endpoint of every edge. *Inclusion-minimal* means that deleting any selected vertex destroys the combined property; it does not mean only minimum cardinality.

## Proof

**1. Independent omissions.** Write \(U=V(G)\setminus S\). The vertex-cover condition is equivalent to independence of \(U\). Since all cross-shore pairs are edges except the \(t\) disjoint pairs \(a_i b_i\), an independent set \(U\) is contained in a single shore or is exactly one of the cross-shore pairs \(\{a_i,b_i\}\), with \(i\leq t\). This is a complete classification, including \(U=\varnothing\).

**2. A one-shore omission criterion.** Suppose \(U\subseteq B\), so every \(a_i\) belongs to \(S\). The set \(S\) resolves all edges if and only if \(U\) contains at most one unmatched vertex of \(B\).

For necessity, if two distinct unmatched vertices \(b_j,b_k\in U\) exist, the present edges \(a_i b_j\) and \(a_i b_k\) have equal distance from every selected vertex, for any fixed row \(i\). At each selected \(a_\ell\), both distances are zero if \(\ell=i\) and one otherwise. At any selected \(b_h\), both distances equal \(\min\{d(b_h,a_i),2\}\), since distinct vertices of \(B\) are at distance two. Hence they cannot be resolved.

Conversely, take two different present edges. If their \(A\)-endpoints differ, the selected \(A\)-endpoint of one is a zero-distance witness. If their \(A\)-endpoints agree, say the edges are \(a_i b_j\) and \(a_i b_k\), then a selected endpoint among \(b_j,b_k\), if any, distinguishes them. If neither is selected, at least one, say \(b_j\), is a deleted-matching endpoint because there is at most one unmatched omission. Since \(a_i b_j\) is present, \(j\neq i\). The selected witness \(a_j\) has edge distances two and one to \(a_i b_j\) and \(a_i b_k\), respectively, using \(d(a_j,a_i)=2\), \(d(a_j,b_j)=3\), and \(d(a_j,b_k)=1\). Thus the edges are distinguished. The same criterion holds with \(A,B\) interchanged.

For all the preceding distance calculations, \(m,n\ge3\) guarantees common neighbors for distinct vertices in one shore and three-edge shortest paths between deleted matched pairs.

**3. Mixed omissions are feasible.** If \(U=\{a_i,b_i\}\) for \(i\leq t\), then every present edge meets \(S\), and different edges have different intersections with \(S\). Indeed, a present edge with just one selected endpoint must contain exactly one of the omitted pair; such selected endpoints identify the other endpoint uniquely, and are on opposite shores in the two possible types. All other edges have two selected endpoints. Therefore some selected vertex belongs to one edge but not the other, witnessing edge distances zero and positive. Hence every such \(S\) is a dominant edge-metric generator.

**4. Full counting polynomial.** For omissions in \(A\), choose freely from the \(t\) matched vertices, and choose zero or one of the \(u\) unmatched vertices: this contributes \((1+z)^t(1+uz)\). Omissions in \(B\) contribute \((1+z)^t(1+vz)\). Their only overlap is the empty omission, counted twice; subtract one. Finally add the \(t\) mixed omitted pairs of size two. This gives \(H_{m,n,t}\) exactly.

**5. Inclusion-minimal classification.** Since admissible selected sets are upward closed, their inclusion-minimal members are precisely complements of inclusion-maximal admissible omission sets. In a single shore the maximal admissible omissions contain all its \(t\) matched vertices and additionally one unmatched vertex, if any; when no unmatched vertex exists they contain precisely the entire shore. For the two shores these give \(u+v\) sets omitting \(t+1\) vertices and the indicated zero-unmatched shore terms omitting \(t\) vertices. Each mixed omitted pair is also maximal and contributes \(t\) sets omitting two vertices. There are no other types by Steps 1–3. Hence \(M_{m,n,t}\) follows. The largest exponent in \(H\), and its leading coefficient, give the dimension and exact minimum counts stated above. At \(t=1\), the \(t z^2\) cross term adds one to the coefficient of the top-degree term; for a fully deleted balanced matching, both entire shores are the only largest admissible omissions.

## Verification

Two standalone programs are supplied. The Python program constructs the graph, computes vertex-to-edge distances by breadth-first search, enumerates every vertex subset and checks both vertex cover and distinct edge-distance codes. It matches both the omission polynomial and inclusion-minimal polynomial for all \(71\) parameter cases \(m,n\ge3\), \(m+n\le11\). Independently, the C++ program constructs for each edge pair a bitmask of its distinguishing vertices, and checks every sensor mask against all coverage and witness constraints. It matches all \(108\) cases with \(m,n\ge3\), \(m+n\le12\). Both include every admissible value of \(t\), and both passed from the included source files.

For example, at \(m=n=5\), the minimum sizes as \(t\) ranges from zero to five are \(9,8,7,6,5,5\); the respective numbers of minimum sets are \(10,9,6,4,2,2\). The general theorem is proved by Steps 1–5; the finite checks are not substituted for that proof.

## Relationship to prior work

Tavakoli, Korivand, Erfanian, Abrishami and Baskoro introduced dominant edge-metric generators (vertex covers that resolve all edges) and proved \(\operatorname{Ddim}_e(K_{m,n})=m+n-1\). The current formula recovers this exact known endpoint at \(t=0\), but describes every sensor set, not only the minimum, across every possible deleted matching. Kelenc, Tratnik and Yero studied edge-metric resolution without the vertex-cover requirement. Other work on vertex-edge dominating edge-metric generators imposes a weaker domination condition than vertex cover; results for that different parameter do not establish the present polynomial. The previously published complete resolving-set polynomials for matching-deleted bicliques concern *vertex-pair* resolution rather than edge-pair resolution; a published edge-metric basis classification of crown graphs does not additionally require vertex covers. Neither statement implies the combined all-generator and minimal-set polynomials here.

The striking structural distinction here is that deleting matched edges permits arbitrarily many matched-endpoint omissions on one shore but never two unmatched omissions on the same shore. It also produces two possible sizes of inclusion-minimal sensor sets with gaps growing with the matching size; the balanced full-deletion endpoint is exceptional.

## Limitations

This result requires \(m,n\ge3\) and the deleted edges to form a matching; arbitrary deletion patterns, smaller shores, and different notions of vertex-edge domination are not included. The matching-deleted formula is proved here but no claim of exhaustive historical priority or independent external certification is made. In particular, existing closely related resolving-polynomial research addresses a different vertex-resolution property, and further unindexed literature may exist.

## References

1. M. Tavakoli, M. Korivand, A. Erfanian, G. Abrishami, E. T. Baskoro, “The dominant edge metric dimension of graphs,” *Electronic Journal of Graph Theory and Applications* **11** (2023), 197–208. DOI: https://doi.org/10.5614/ejgta.2023.11.1.16 (public posting recorded 2023-04-08).
2. A. Kelenc, N. Tratnik, I. G. Yero, “Uniquely identifying the edges of a graph: the edge metric dimension,” arXiv:1602.00291 (first posted 2016-01-31). https://arxiv.org/abs/1602.00291
3. H. M. Ikhlaq, S. Hayat, H. M. A. Siddiqui, “Unique identification and domination of edges in a graph: The vertex-edge dominant edge metric dimension,” arXiv:2211.09327 (first posted 2022-11-17). https://arxiv.org/abs/2211.09327
