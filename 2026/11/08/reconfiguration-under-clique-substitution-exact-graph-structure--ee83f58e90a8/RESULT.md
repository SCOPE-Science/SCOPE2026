# Reconfiguration under clique substitution: exact graph structure and metric

## Finding

Let \(G\) be a nonempty finite simple graph. For each \(v\in V(G)\), fix an integer \(m_v\ge1\) and replace \(v\) with a clique \(F_v\cong K_{m_v}\), joining every vertex of \(F_u\) to every vertex of \(F_v\) precisely when \(uv\in E(G)\). Denote the resulting labelled clique substitution by \(H\). An **independent dominating set** is a maximal independent vertex set; an **\(i\)-set** is one of minimum possible size \(i(G)\). The **\(i\)-graph** \(\mathscr I(G)\) has the \(i\)-sets as vertices, joined when one token slides along an edge of \(G\) to another \(i\)-set.

Write \(\mathcal S\) for the \(i\)-sets of \(G\), and \(k=i(G)\). Every \(i\)-set of \(H\) is uniquely a pair \((S,\alpha)\), where \(S\in\mathcal S\) and \(\alpha(v)\in F_v\) for each \(v\in S\). In particular, \(i(H)=k\). The complete reconfiguration graph has the following structure.

* Over \(S\in\mathcal S\), its induced fiber is the Hamming graph \(\mathop{\square}_{v\in S} K_{m_v}\).
* For adjacent \(S,T\in\mathscr I(G)\), write \(S\setminus T=\{u\}\), \(T\setminus S=\{v\}\). The cross-edges between their fibers form \(\prod_{w\in S\cap T}m_w\) disjoint copies of \(K_{m_u,m_v}\), one for each common-label assignment; there are no cross-edges over nonadjacent base sets.
* The projection \(\mathscr I(H)\to\mathscr I(G)\) induces a bijection on connected components.

Consequently, the number of vertices and edges of \(\mathscr I(H)\) are respectively
\[
N(H)=\sum_{S\in\mathcal S}\prod_{v\in S}m_v,
\]
\[
E(H)=\sum_{S\in\mathcal S}\sum_{v\in S}\binom{m_v}{2}\prod_{w\in S\setminus\{v\}}m_w
+\sum_{\{S,T\}\in E(\mathscr I(G))}m_um_v\prod_{w\in S\cap T}m_w,
\]
where \(u\) and \(v\) in the second sum are the unique vertices in \(S\setminus T\) and \(T\setminus S\). For \((S,\alpha)\), its degree is independent of \(\alpha\) and equals
\[
\deg_{\mathscr I(H)}(S,\alpha)=\sum_{v\in S}(m_v-1)+\sum_{T\sim_{\mathscr I(G)}S}m_{v(T)},
\]
where \(v(T)\) is the unique element of \(T\setminus S\).

There is also an **exact shortest-path formula**. Let \(X=(S,\alpha)\) and \(Y=(T,\beta)\), and define \(B=\{v\in S\cap T:\alpha(v)\ne\beta(v)\}\). For a finite walk \(W=(S_0,\ldots,S_\ell)\) in \(\mathscr I(G)\) from \(S\) to \(T\), including walks of length zero, put \(P(W)=\bigcap_{j=0}^\ell S_j\). Then
\[
\boxed{d_{\mathscr I(H)}(X,Y)=\min_{W:S\leadsto T}\left(\ell+|B\cap P(W)|\right).}
\]
As usual, the minimum of the empty set is \(+\infty\). This formula is finite exactly when \(S\) and \(T\) lie in the same base reconfiguration component. In particular, for constant \(m_v=m\ge1\),
\[
\deg_{\mathscr I(H)}(S,\alpha)=k(m-1)+m\deg_{\mathscr I(G)}(S),
\]
so regularity of the two \(i\)-graphs is equivalent, and each connected component of the lift has diameter between the corresponding base diameter and that diameter plus \(k\).

As a concrete infinite family, let \(n\ge4\), \(m\ge2\), \(k=\lceil n/3\rceil\), and \(d=3k-n\). The clique blowup \(C_n[K_m]\) has an \(i\)-graph with precisely
\[
\boxed{b_nm^k\quad\text{vertices},\qquad b_n k\binom m2 m^{k-1}+e_nm^{k+1}\quad\text{edges},}
\]
where
\[
b_n=\frac nk\binom{k}{d},\qquad e_n=n\binom{k-2}{d-1}.
\]
Binomial coefficients with an inadmissible lower index are zero. In particular, the two components for \(C_4[K_m]\) are each \(K_m\square K_m\), while \(\mathscr I(C_5[K_m])\) has \(5m^2\) vertices and \(5m^2(2m-1)\) edges.

## Assumptions and scope

All graphs are finite, undirected, simple and labelled. Base graphs are nonempty but need not be connected; fiber sizes may vary and may equal one. Adjacency means a **token slide** along an actual edge, not token jumping or token addition/removal. The distance formula includes arbitrary finite base walks, not only geodesics. The cycle specialization is for \(n\ge4\); the triangle is exceptional because its \(i\)-sets are singletons.

## Proof

**Independent dominating sets.** An independent set of \(H\) contains at most one vertex from each fiber. Its set of represented base vertices is independent in \(G\); conversely every independent base set can be lifted with arbitrary one-per-fiber labels. Such a lifted set dominates every omitted fiber exactly when its support dominates \(G\): an omitted fiber \(F_u\) is dominated precisely if some adjacent fiber is represented, and a represented fiber is dominated by its selected vertex. Thus inclusion-maximal independent sets correspond exactly to labelled maximal independent base sets, and minimum cardinalities agree.

**Reconfiguration edges.** A token slide in \(H\) either stays within one selected clique \(F_v\), changing precisely its label, or traverses between two adjacent cliques \(F_u,F_v\), changing the support from \(S\) to \((S\setminus\{u\})\cup\{v\}\). In the second case this must be a base \(i\)-graph edge, and labels on all shared selected fibers remain unchanged. Conversely any such label change or base edge with shared labels held fixed is an actual legal slide. Hence the fibers are Cartesian products of cliques and each pair of adjacent fibers is joined by the claimed disjoint complete bipartite graphs.

**Components, counts and degrees.** Each product-of-cliques fiber is connected, including when it consists of a single vertex. Every base edge has at least one lifted cross-edge, and all lifted edges project either to a base edge or to a stationary step. This proves the component bijection. Counting all label assignments gives \(N(H)\). For fixed \(S\) and a selected base vertex \(v\), there are \(\binom{m_v}{2}\) ways to form an intrafiber edge while the other selected fibers have \(\prod_{w\ne v}m_w\) label assignments. For a base edge \(S,T\) there are \(m_um_v\prod_{w\in S\cap T}m_w\) cross-edges. These categories are disjoint and exhaustive. The same two categories, counted from one labelled configuration, give the degree formula.

**Shortest paths.** Project any lifted path from \(X\) to \(Y\), retaining precisely the steps that change the base support. This gives a base walk \(W\) of length \(\ell\). Every \(v\in B\cap P(W)\) is present throughout that walk: no cross-fiber step can change its label. Since its endpoint labels differ, at least one additional within-fiber slide must change that label. These changes concern distinct vertices and require distinct steps. Thus the lifted path has length at least \(\ell+|B\cap P(W)|\). Conversely, fix a base walk \(W\). First relabel each vertex of \(B\cap P(W)\) once. Follow every projected slide, assigning on a fiber's **last entry** the required target label whenever that fiber belongs to \(T\); labels in intermediate positions are arbitrary. Every vertex of \(S\cap T\) that is not persistent leaves and later re-enters, so its final label is free to choose. The result reaches \(Y\) in exactly \(\ell+|B\cap P(W)|\) steps. Taking the minimum proves the formula. The uniform degree equation follows immediately. For a connected base component, project paths for the diameter lower bound; for the upper bound lift a shortest base walk and recolor at most \(k\) persistent positions.

**Cycles.** In a minimum independent dominating set of \(C_n\), selected vertices have successive cyclic gaps of length two or three. Their number is \(k=\lceil n/3\rceil\), and exactly \(d=3k-n\) gaps have length two. Choosing a starting selected vertex and the \(d\) short-gap positions counts every set exactly \(k\) times, so the number of base \(i\)-sets is \(b_n=(n/k)\binom{k}{d}\). A legal slide interchanges an adjacent pair of gap lengths two and three. There are \(n\binom{k-2}{d-1}\) oriented occurrences of a \((2,3)\) pair and the same number of \((3,2)\) occurrences, counted by their starting selected vertex; division by two gives the number \(e_n\) of undirected base moves. Substitute \(b_n,e_n\) into the uniform formulas. For \(C_4\), the only two base \(i\)-sets have no slide between them, yielding two product fibers. For \(C_5\), \(b_5=e_5=5\), giving the claimed values.

## Verification

Run `python verify.py` with Python 3. The standalone verifier constructs each graph directly, enumerates minimum independent dominating sets by testing independence and domination, constructs slide graphs from actual adjacency, and compares with all predicted vertices, edges, components and counts. For a collection of small graphs it compares BFS shortest paths in the direct lift with a separate finite-state minimization of the displayed base-walk metric formula. It separately enumerates cyclic-gap words and verifies small cycle formulas by direct subset enumeration. The checked runs report `VERIFY_OK profiles=180 direct_i_graph_nodes=1216 direct_edges=2582 shortest_path_pairs=1870 cyclic_parameters=41 direct_cycles=11`. These finite checks support but do not replace the unrestricted proof.

## Relationship to prior work

Brewster, Mynhardt and Teshima introduced and structurally studied minimum-independent-domination reconfiguration graphs and their realizability in 2023 (arXiv:2303.06299). Their constructions include Cartesian products arising from disjoint unions and a different inflation that keeps the original \(i\)-graph unchanged; they do not give the variable-clique substitution graph, its weighted edge and degree formulas or its exact metric. Their companion work (arXiv:2303.08190) determines the \(i\)-graphs of ordinary paths and cycles. In particular, its cycle counts and bracelet-graph descriptions are **prior knowledge**, not being claimed as new; the cycle blowup formulas follow by the new lifting and counting equations. More general independent-set token-sliding literature treats true-twin reductions for reachability, so preservation of reachability by itself is **not** claimed as an independent discovery. The contribution assessed here is the entire labelled graph structure, weighted enumeration and exact shortest-path metric together, including varying clique sizes.

## Limitations

The result addresses minimum independent dominating sets only, not all independent sets of a fixed size, token jumping, or other graph reconfiguration rules. The shortest-path expression is an exact characterization by a minimum over base walks, not a claimed polynomial-time algorithm for arbitrary input graphs. Both the cardinality of the cycle base \(i\)-sets and their unexpanded reconfiguration structure are known. Publication priority of the strengthened substitution theorem remains provisional pending wider expert literature review; particularly, equivalent graph operations may be described using true twins or vertex replication. No independent audit has been performed.

## References

1. R. C. Brewster, C. M. Mynhardt and L. E. Teshima, *Reconfiguration of Minimum Independent Dominating Sets in Graphs*, arXiv:2303.06299, first public 2023-03-11. https://arxiv.org/abs/2303.06299
2. R. C. Brewster, C. M. Mynhardt and L. E. Teshima, *The \(i\)-Graphs of Paths and Cycles*, arXiv:2303.08190, first public 2023-03-14. https://arxiv.org/abs/2303.08190
3. C. M. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey*, arXiv:2003.05956, first public 2020-03-12. https://arxiv.org/abs/2003.05956
