# A sharp edge-girth law for exchanging two saturated labelled-token stacks

## Finding

Let \(G\) be a finite connected simple graph with at least three vertices, let \(uv\in E(G)\), and let \(s\ge 2\) be an integer. In the graph of \(2s\) distinguishable tokens with capacity \(s\) at each host vertex, let \(x\) place all \(s\) tokens of group \(A\) at \(u\) and all \(s\) tokens of group \(B\) at \(v\), and let \(y\) exchange the two groups. Write \(g_G(uv)\) for the length of a shortest simple cycle through \(uv\), with \(g_G(uv)=\infty\) if no such cycle exists. Then

\[
 d_{F^s_{2s\times1}(G)}(x,y)=2s+\min\{4,g_G(uv)-2\}.
\]

Thus exchanging two initially full adjacent stacks incurs a surcharge of one move on a triangular edge, two on a square edge not in a triangle, three on a shortest five-cycle edge, and four on every other edge, including bridges. The surcharge is independent of \(s\). In particular the exact distance on an edge of \(C_n\) is \(2s+\min\{4,n-2\}\) for every \(n\ge3\).

## Assumptions and scope

The host \(G=(V,E)\) is finite, undirected, loopless, simple and connected, with \(|V|\ge3\). Its capacity-\(s\) distinguishable-token graph \(F^s_{k\times1}(G)\) has as vertices the ordered token-position tuples \((p_1,\ldots,p_k)\in V^k\) in which no vertex occurs more than \(s\) times. An edge of the configuration graph moves exactly one token across one edge of \(G\), subject to that capacity. The tokens in the two initial stacks are distinct, so the terminal tuple specifies every token's exact destination, not merely the multiset of occupied sites. Here \(k=2s\), and \(s\ge2\). The graph must have a vertex outside \(\{u,v\}\): the two-vertex host with both sites full admits no first move and is excluded.

## Proof

**Lower bound.** Every one of the \(2s\) labelled tokens starts at one of \(u,v\) and must end at the other. Thus its walk has at least one edge, giving a baseline of \(2s\) moves. Call a maximal subwalk with internal vertices outside \(\{u,v\}\) an *external excursion*. Each excursion is either a *crossing excursion*, connecting distinct endpoints \(u,v\), or a *return excursion*, starting and ending at the same endpoint.

If some external excursion crosses between \(u\) and \(v\), that token traverses a \(u\)-to-\(v\) walk avoiding the edge \(uv\) and of length at least \(g_G(uv)-1\). This token alone therefore requires at least \(g_G(uv)-2\) moves beyond its baseline one, and the whole sequence has length at least \(2s+g_G(uv)-2\). Such an excursion cannot exist when \(uv\) is a bridge.

Otherwise every external excursion is a return. Each return excursion uses at least two host-edge moves not crossing \(uv\). Every token still needs to cross \(uv\) at least once, so the length is at least \(2s\) plus twice the number of return excursions. Initially both endpoints are full, so the first legal move must leave \(\{u,v\}\), beginning an excursion. Suppose, seeking a contradiction, that the entire move sequence has *only one* external excursion. Its first return brings the initially departed token back to the very endpoint where it started, rather than its required opposite endpoint. No other token is then outside \(\{u,v\}\), so both endpoints are full again and no further move is legal. Thus one excursion cannot suffice: there must be at least two return excursions, costing at least \(2s+4\). Together the two cases give the claimed lower bound.

**Universal construction of length \(2s+4\).** Since \(G\) is connected and has at least three vertices, some endpoint of \(uv\), say \(q\), has a neighbor \(w\notin\{u,v\}\). Rename the other endpoint \(p\). Name the tokens starting at \(p\) by \(A_1,\ldots,A_s\) and those starting at \(q\) by \(B_1,\ldots,B_s\). Perform the following ordered moves:

1. \(B_1:q\to w\); \(A_1:p\to q\); \(A_1:q\to w\).
2. For each \(i=2,\ldots,s\), move \(A_i:p\to q\), then \(B_i:q\to p\).
3. \(B_1:w\to q\); \(B_1:q\to p\); \(A_1:w\to q\).

The temporary site \(w\) holds two tokens and thus respects \(s\ge2\). All moves preserve the capacities at \(p,q\), and the final labels are correct. Their number is \(3+2(s-1)+3=2s+4\).

**Cycle construction of length \(2s+g_G(uv)-2\).** Suppose \(uv\) lies on a cycle. Let \(v=w_0,w_1,\ldots,w_\ell=u\) be a shortest \(v\)-to-\(u\) path in \(G-uv\), so \(\ell=g_G(uv)-1\). First move \(B_1\) along that path from \(v\) to \(w_{\ell-1}\), leaving it one edge from \(u\). Its \(\ell-1\) moves use previously empty vertices. Next, for \(i=1,\ldots,s\), move \(A_i:u\to v\) and, when \(i<s\), immediately move \(B_{i+1}:v\to u\). Finally move \(B_1:w_{\ell-1}\to u\). Each direct move first fills a currently vacant place, then frees the opposite site; at termination both sites contain their prescribed stacks. The total is \((\ell-1)+(2s-1)+1=2s+\ell-1=2s+g_G(uv)-2\). Taking the shorter of the two valid constructions matches the lower bound. \(\square\)

## Verification

Run the supplied standalone `verify.py` with Python 3. It constructs the complete legal configuration graph implicitly, performs an exact breadth-first search from each specified full-stack initial state to its exact exchanged-label target, and independently computes the shortest cycle through the chosen edge by breadth-first search in \(G-uv\). It checks forty-six graph/edge/capacity cases on cycles, paths, a complete graph and graphs with both bridge and cycle edges, including cycle lengths three through eight and \(s=2,3\). It finishes with `VERIFY_OK`. This finite replay is corroborating evidence; the preceding argument proves the theorem for all allowed \(G\) and \(s\).

## Relationship to prior work

Song, Dalfó, Fiol, Mora and Zhang introduced the relevant labelled-capacity token family and studied basic properties. Cai, Dalfó, Fernández and Fiol subsequently proved general connectivity and several diameter formulas, including exact distances for complete hosts and a conjecture about odd-cycle diameters. Their complete-host metric already entails the triangular-edge instance here, which is **not** separately claimed as new. The present edge-local formula for arbitrary connected host graphs, including four-, five- and longer-cycle edges and bridges, does not follow from those global diameter results. It measures the exact rearrangement overhead of exchanging two *fully occupied* adjacent sites, not the unrestricted diameter or an indistinguishable-token metric.

## Limitations

This formula treats one specific pair of saturated-stack configurations, not all configuration pairs or the full diameter. It does not settle the published odd-cycle diameter conjecture. The assumption \(s\ge2\) is essential for the two-token temporary buffer construction. The first-move argument excludes the two-vertex host. Literature comparisons cannot rule out an unindexed equivalent earlier identity; independent mathematical and historical review remain outstanding.

## References

- X. Song, C. Dalfó, M. À. Fiol, M. Mora and S. Zhang, *On Generalized Token Graphs*, arXiv:2604.04845, first posted 2026-04-06, https://arxiv.org/html/2604.04845.
- Y. Cai, C. Dalfó, B. Fernández and M. À. Fiol, *On generalized \(k\)-token graphs with distinguishable tokens and a maximum capacity of \(s\) tokens per vertex*, arXiv:2611.06275, first posted 2026-11-04, sections 1 and 4, https://arxiv.org/abs/2611.06275.
