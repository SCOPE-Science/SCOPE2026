# A sharp diametral-pair transition in rectangular total-matching polytopes

## Finding
Let \(2\le p<q\) be integers. Let \(G=K_{p,q}\), with color classes \(L\) and \(R\) of respective sizes \(p\) and \(q\). A **total matching** is a subset \(T\subseteq V(G)\cup E(G)\) whose members are pairwise nonadjacent or nonincident (two edges of \(T\) share no endpoint; selected vertices are nonadjacent; and no selected vertex is incident to a selected edge). Write
\[
P_{p,q}=\operatorname{conv}\{\mathbf1_T:T\text{ is a total matching of }K_{p,q}\}\subseteq\mathbb R^{p+q+pq}.
\]
Equip this fixed incidence-coordinate realization with its ordinary Euclidean metric. Then
\[
\boxed{\operatorname{diam}_2(P_{p,q})^2=q+\min\{q,2p\}.}
\]
All diametral endpoints are distinct \(0\)-\(1\) vertices, and every unordered diametral pair is obtained by the following rules, with the two colors interchanged considered the same pair.

1. Choose two edge matchings \(M_1,M_2\) in \(K_{p,q}\), with no common edge. Each is a partial injection from right vertices to left vertices. Write \(R_i\subseteq R\) for the right vertices covered by \(M_i\).
2. If \(p<q\le2p\), require \(R_1\cup R_2=R\). Put each right vertex of \(R_2\setminus R_1\) in total matching \(T_1\), and each right vertex of \(R_1\setminus R_2\) in \(T_2\). Add \(M_i\) to \(T_i\). Do not select any other vertex.
3. If \(q\ge2p\), require \(|M_1|=|M_2|=p\) and \(R_1\cap R_2=\varnothing\). Select the right vertices covered by exactly one edge matching in the *other* total matching, and assign each remaining right vertex independently to either total matching. Add the prescribed edge matchings; select no left vertices.

At \(q=2p\), these descriptions coincide. They produce all, and only, the diametral pairs.

The number \(D_{p,q}\) of unordered diametral pairs exhibits a sharp change of counting mechanism:
\[
\boxed{D_{p,q}=\frac{q!\,2^{q-2p}}{2(q-2p)!}\qquad(q\ge2p).}
\]
For \(p<q<2p\), put \((u)_k=u(u-1)\cdots(u-k+1)\), with \((u)_0=1\), and define
\[
F_p(a,b,t)=\sum_{s=0}^{t}(-1)^s\binom ts(p)_a(p-s)_{b-s}.
\]
Then the exact finite formula is
\[
\boxed{D_{p,q}=\frac12\sum_{\substack{0\le a,b\le p\\a+b\ge q}}
 \frac{q!}{(a+b-q)!(q-a)!(q-b)!}\,F_p(a,b,a+b-q).}
\]
Thus the entire diameter graph (its vertices are polytope vertices, its edges join diametral pairs) is explicitly classified and counted for every unequal pair of shore sizes. In particular, for fixed \(p\) and \(q>2p\),
\[
D_{p,q}=2^{q-2p-1}(q)_{2p},
\]
while the squared diameter is \(q+2p\), strictly below the elementary \(2q\) bound derived from maximum total-matching cardinality. The transition occurs at \(q=2p\).

## Assumptions and scope
The graph is a simple complete bipartite graph with \(2\le p<q\), and edge and vertex indicator coordinates have unit Euclidean weights. The theorem excludes equal shores, weighted coordinates, noncomplete bipartite graphs, and the graph-theoretic one-skeleton diameter of a polytope. The enumerative formulas count unordered **pairs** of polytope vertices, not isolated vertices or distinct supporting directions.

## Proof
**Reduction to disjoint total matchings.** Each \(0\)-\(1\) incidence vector \(\mathbf1_T\) is a vertex of \(P_{p,q}\): a convex combination of other \(0\)-\(1\) vectors cannot produce it, coordinate by coordinate. If \(T_1\cap T_2\ne\varnothing\), deleting one common element from \(T_1\) preserves feasibility and strictly raises the squared distance, which equals \(|T_1\triangle T_2|\). Hence every diametral pair of vertices comprises disjoint total matchings. Squared Euclidean distance is strictly convex in each argument, so a nonvertex point cannot be an endpoint of a diametral pair: a nontrivial convex combination yields a strict inequality against the maximum.

**Exhaustive upper bounds by vertex shore.** Within either total matching, its selected graph vertices all lie in one shore, since every left vertex is adjacent to every right vertex. For two disjoint total matchings, if one selects left vertices and the other selects right vertices, write \(m_1,m_2\) for their edge counts. The former chooses at most \(p-m_1\) left vertices and the latter at most \(q-m_2\) right vertices, so the union contains at most \(p+q\) elements. If both select left vertices, each left vertex can contribute at most two selected objects in total, counting its two possible differently colored incident edges and/or the vertex itself; thus the union size is at most \(2p\). If both select right vertices, the total number of selected right vertices is at most \(q\), and the total number of selected edges at most \(2p\); therefore the union has size at most \(q+2p\). Moreover, at each right vertex there are at most two selected objects altogether: with two differently colored incident edges the right vertex cannot be selected, with one selected edge its right vertex can be selected in the opposite color only, and with no edge its right vertex can be selected in at most one color. Hence the union size is at most \(2q\). A color class containing no graph vertices can be assigned to whichever shore is needed in this case split. Since \(p<q\), both mixed-shore and both-left alternatives fall strictly below \(q+\min\{q,2p\}\).

**Sharpness and rigidity.** For \(q\ge2p\), choose two size-\(p\) edge matchings with disjoint right endpoint sets. Each right vertex used by just one of the edge matchings may be chosen in the other total matching, and each unused right vertex may be selected in either. The union then has \(2p+q\) elements. Conversely equality in the upper bound \(q+2p\) requires \(2p\) selected edges and \(q\) selected right vertices: both edge matchings have cardinality \(p\) and their right endpoint sets must be disjoint, otherwise the shared endpoint could be in neither color's selected vertices. This gives exactly the stated case, including \(q=2p\).

For \(p<q<2p\), choose two size-\(p\) edge matchings whose sets of right endpoints cover \(R\), with no common edge. Such a pair exists: choose right endpoint sets of size \(p\) with union \(R\); then select distinct injective left assignments, avoiding agreement on their overlap (the overlap has size \(2p-q<p\), and an injective assignment avoiding all conflicting shared edges exists: fix any bijection of \(R_2\) onto the \(p\) left vertices, label those vertices cyclically, and compose with one of the \(p\) cyclic shifts. Each of the fewer than \(p\) overlapping right endpoints forbids only one shift, leaving at least one allowable shift). At every right vertex covered in exactly one edge matching choose its right vertex in the opposite color; at every right vertex covered twice select no vertex. Every right vertex then contributes two selected objects, and the squared distance is \(2q\). Equality with the columnwise \(2q\) bound forces every right vertex to be covered by at least one edge matching, and forces the corresponding right-vertex selection whenever it is covered exactly once. The two edge matchings must be distinct on any overlapping right endpoint. This is precisely the asserted classification. No extra cases arise from a color with no selected right vertex because each \(|R_i|\le p<q\), whereas \(R_1\cup R_2=R\); both set differences must be nonempty.

**Counting.** For \(q\ge2p\), ordered edge matchings with disjoint right endpoints can be chosen in \((q)_{2p}=q!/(q-2p)!\) ways. The \(q-2p\) unused right vertices independently choose one of two colors. Interchanging the two total matchings gives a fixed-point-free involution on these ordered choices, yielding \(D_{p,q}=2^{q-2p-1}(q)_{2p}\).

For \(p<q<2p\), put \(a=|R_1|\), \(b=|R_2|\), and \(t=|R_1\cap R_2|=a+b-q\). The number of ordered right-endpoint subset pairs with prescribed sizes and union \(R\) is \(q!/[t!(q-a)!(q-b)!]\). For a fixed such pair, there are \((p)_a\) injections of \(R_1\) into the left shore. Inclusion-exclusion over the \(t\) common right endpoints, disallowing an identical edge in both matchings, gives \(F_p(a,b,t)\). The right-vertex choices are forced. Sum over \(a,b\le p\) with \(a+b\ge q\), then divide by two for unordered pairs. This completes the proof.

## Verification
The accompanying self-contained Python 3 program `check_exact.py` independently enumerates all total matchings and all pairs for \((p,q)=(2,3),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)\), checks the exact integer diameter and count, constructs witnesses for thousands of larger integer pairs, and verifies positivity and integrality of the counting formulas on further ranges. Run with `python3 check_exact.py`. Exhaustive finite computations are corroboration, not the proof for arbitrary orders; the preceding combinatorial arguments prove the infinite-parameter statements.

## Relationship to prior work
Ferrarini (arXiv:2111.15528v1, 2021) introduced complete facet descriptions of rectangular total-matching polytopes; Faenza and Ferrarini (arXiv:2303.00328v1, 2023) supply an extended formulation and a nonredundant facet description for complete bipartite instances. Their polyhedral frameworks are the starting point, but the inspected work concerns facets and linear optimization, not the two-point Euclidean metric, its sharp larger-shore/smaller-shore phase at \(q=2p\), or the diametral pair enumerator. The general maximum total-matching cardinality bound \(q\) yields only \(\operatorname{diam}_2^2\le2q\), which is not sharp for \(q>2p\). General induced-bipartite-subgraph results apply to a related graph-theoretic reduction but do not give this two-parameter extremal-pair classification. An undiscovered equivalent formulation remains possible.

## Limitations
The theorem is specialized to unequal complete bipartite shores and the canonical unit-weight incidence embedding. It does not assert independent mathematical validation, a new polytope facet characterization, or a metric statement about other embedded realizations. Bibliographic priority is provisional: specialist graph-theoretic terminology for maximum pairs of total matchings may conceal an earlier equivalent result.

## References
- L. Ferrarini, *Facets of the Total Matching Polytope for bipartite graphs*, arXiv:2111.15528v1 (first submitted 2021-11-30), https://arxiv.org/html/2111.15528v1.
- Y. Faenza and L. Ferrarini, *The Total Matching Polytope of Complete Bipartite Graphs*, arXiv:2303.00328v1 (first submitted 2023-03-01), https://arxiv.org/abs/2303.00328.
- J. M. Byskov, B. A. Madsen, B. Skjernaa, *On the number of maximal bipartite subgraphs of a graph*, J. Graph Theory 48 (2005), 127–132, DOI:10.1002/jgt.20041 (general graph-theoretic context, not an exact result for these polytopes).
