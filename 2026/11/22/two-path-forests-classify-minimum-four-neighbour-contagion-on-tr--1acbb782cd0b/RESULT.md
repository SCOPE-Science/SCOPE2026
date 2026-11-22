# Two path forests classify minimum four-neighbour contagion on triangular graphs

## Finding
Let \(T_n=L(K_n)\) be the triangular graph on the two-element subsets of \([n]\), where \(n\geq5\). In synchronous irreversible four-neighbour bootstrap percolation, the minimum number of initially active vertices is four. Identify any initially active vertex \(\{u,v\}\) with the edge \(uv\) in a root graph \(H\) on \([n]\). A four-vertex initial set percolates **if and only if** the four-edge graph \(H\), after isolated vertices are discarded, is isomorphic to either the five-vertex path \(P_5\) or the disjoint union \(P_3\sqcup P_3\).

Consequently, the exact number of minimum contagious sets is
\[
N(n)=60\binom n5+90\binom n6,
\]
with the second term interpreted as zero for \(n=5\). Every minimum set finishes in four parallel rounds, except that the \(P_5\) sets finish in three rounds at \(n=5\), and the \(P_3\sqcup P_3\) sets finish in three rounds at \(n=6\).

Let \(\mathcal R_n\) be the graph of these minimum sets, with adjacency when exactly one initially active vertex of \(T_n\) is replaced by another. The graph \(\mathcal R_n\) is connected for every \(n\geq5\). Its \(P_5\)-type vertices have degree \(8(n-4)\); its \(P_3\sqcup P_3\)-type vertices (present for \(n\geq6\)) have degree \(8n-28\). Thus
\[
|E(\mathcal R_n)|=240(n-4)\binom n5+90(4n-14)\binom n6.
\]
These degree classes differ by four whenever both types exist, so the exchange graph is connected but nonregular for \(n\geq6\).

## Assumptions and scope
All graphs are finite, simple, undirected, and labelled on \([n]\). At time zero precisely the chosen vertices of \(T_n\) are active. At each positive integer time, an inactive vertex activates if it has at least four active neighbours at the preceding time, and no active vertex deactivates. A set percolates if eventually every vertex is active. The completion time is the first time all vertices are active; no asynchronous timing convention is used. The exchange graph uses single-vertex *replacement* of initial sets, not token sliding and not token addition/removal.

## Proof
**Degree-sum rule.** Write \(H_t\) for the spanning subgraph of \(K_n\) corresponding to active vertices of \(T_n\) at time \(t\), and \(d_t(u)\) for a vertex degree in \(H_t\). An inactive edge \(uv\) has exactly \(d_t(u)+d_t(v)\) active neighbours in \(T_n\), since the two incident-edge collections are disjoint when \(uv\notin E(H_t)\). Therefore
\[
E(H_{t+1})=E(H_t)\cup\{uv\notin E(H_t): d_t(u)+d_t(v)\geq4\}.
\]
If \(|E(H_0)|\leq3\), then for every absent \(uv\), the incident edges at \(u\) and \(v\) are distinct and hence \(d_0(u)+d_0(v)\leq3\). No initial activation is possible. This gives a lower bound of four.

**Exhaustive structural classification of four-edge starters.** For a four-edge initial graph to change, there must be a missing edge \(uv\) for which \(d_0(u)+d_0(v)=4\). Every initial edge is thus incident with \(u\) or \(v\), and these two vertices are nonadjacent. Up to interchanging \(u,v\), their possible degree pairs are \((4,0)\), \((3,1)\), and \((2,2)\). In the first case the root graph is a four-star. In the second it is a three-star together with one edge that either attaches to one of the star's leaves or is disjoint from the star. In the third case the two nonadjacent degree-two centers have zero, one, or two common neighbours. These give, respectively, \(P_3\sqcup P_3\), \(P_5\), and a four-cycle \(C_4\).

The four-star closure is a larger star and never fills the missing leaf–leaf edges. In either \((3,1)\) case, after the first few updates every noncentral edge lies inside a single edge joining two leaves of a full star. Those two leaves both have degree two, and every other leaf has degree one; no further noncentral edge is eligible. A four-cycle adds its two diagonals to become \(K_4\), which cannot infect an outside vertex since its degrees are only three. Since \(n\geq5\), this also stalls. Thus none of these cases percolates.

For \(P_5\), the successive root-edge counts are \(4,5,7,2n,\binom n2\), with the last term omitted when \(n=5\), because \(2n=\binom n2\) there. This follows by applying the degree-sum rule to the labelled path \(1-2-3-4-5\): the first new edge is \(24\), the next two are \(14\) and \(25\), and at the third step the remaining pairs among the original five vertices and all edges from \(2,4\) to outside vertices activate. At the fourth step all remaining edges activate. Hence completion takes three rounds for \(n=5\), otherwise four.

For \(P_3\sqcup P_3\), start with \(12,13,45,46\). The successive root-edge counts are \(4,5,9,2n+3,\binom n2\), with the last term omitted at \(n=6\) since \(2n+3=\binom n2\). First \(14\) activates; next, the four edges from each center to the other component's leaves activate. The next round fills all missing edges among the six supported vertices and links the two centers to any outside vertices; a final round fills the remainder. Thus completion takes three rounds at \(n=6\), otherwise four. The two listed forests attain the lower bound and the classification follows.

**Counting.** On a fixed five-element support there are \(5!/2=60\) unoriented Hamilton paths. On a fixed six-element support, choose an unordered partition into two three-element blocks and a center in each: \(\tfrac12\binom63\cdot3^2=90\). Distinct supports or constructions give distinct sets. This yields \(N(n)\).

**Exchange degrees.** On a fixed five-element support, a path has eight single-edge replacements that are again a path: removing a terminal edge permits one alternative reconnection, while removing either internal edge permits three. For each outside label, four replacements yield another path and four yield a pair of three-vertex paths. Hence the path degree is \(8+8(n-5)=8(n-4)\). A two-path forest has twenty same-support replacements: removing any of its four edges permits four reconnections to a five-vertex path and one reconnection to a different two-path forest. Each outside label permits eight replacements to another two-path forest. Its degree is therefore \(20+8(n-6)=8n-28\). Summing degrees gives the edge-count formula.

**Exchange connectivity.** On a fixed five-element support, path exchanges that break an internal edge and reconnect the resulting components enact arbitrary prefix reversals of the path ordering; reversal of the entire path represents the same undirected path. These prefix reversals generate every ordering, so the paths on a fixed support are exchange-connected. Replacing one terminal edge of a path by an edge to an unused label allows any desired change of the five-element support after arranging the unwanted label as an endpoint. Thus all path-type configurations lie in one component. Finally every pair of disjoint three-vertex paths has a one-edge replacement yielding a five-vertex path: if their centers are \(a,b\), and \(x,y\) and \(u,v\) are their respective leaves, replace \(ay\) with \(au\) to obtain the path \(x-a-u-b-v\). All optima therefore lie in one connected component.

## Verification
The standalone program `verify_line_graph.cpp` builds \(T_n\) explicitly and enumerates every four-vertex initial set for \(5\leq n\leq10\), checking the final closure, support shape, and completion time. The separately implemented `verify_root_graph.py` uses the degree-sum closure on root edges, constructs both path families independently, enumerates all four-edge subsets for \(5\leq n\leq8\), and checks every exchange edge, degree, and connected component. These computations corroborate, but are not substituted for, the all-order arguments above.

## Relationship to prior work
Guggiola and Semerjian (2014) formulate the deterministic threshold-activation optimization problem and study minimum contagious sets and time constraints in random regular graphs. Their results concern a different host family and do not entail the triangular-graph classification. Bidgoli, Mohammadian and Tayfeh-Rezaie (2021) explicitly determine the minimum \(r\)-neighbour percolation number of \(L(K_n)\); the numerical minimum four is therefore credited to earlier work. The additional claim here is the *complete configuration classification*, all-order counts, exact synchronous completion times, and exchange-graph structure. The authors' accessible 2019 preprint (arXiv:1905.01942) was inspected in full, but it addresses only Hamming graphs; the full text of the expanded same-object 2021 journal paper could not be inspected, so the possibility of earlier implicit enumeration or a related description remains a priority risk. Studies of forts, geodetic bases and power domination on triangular graphs concern distinct activation or coverage rules and do not mathematically imply this four-neighbour theorem.

## Limitations
The theorem is for exactly four-neighbour irreversible bootstrap percolation on \(T_n\), \(n\geq5\). It does not classify larger inclusion-minimal seed sets, arbitrary thresholds, other line graphs, or weighted and stochastic activation. Exact all-order results follow from the proof, not from finite enumeration. Independent scholarly validation has not been performed. Priority remains subject to inspection of the inaccessible 2021 full text and unindexed literature.

## References
1. A. Guggiola and G. Semerjian, *Minimal contagious sets in random regular graphs*, arXiv:1407.7361, first public version 2014-07-28, https://arxiv.org/abs/1407.7361.
2. M. Bidgoli, A. Mohammadian and B. Tayfeh-Rezaie, *Percolating sets in bootstrap percolation on the Hamming graphs and triangular graphs*, European Journal of Combinatorics 92 (2021), article 103256, https://doi.org/10.1016/j.ejc.2020.103256.
3. M. R. Bidgoli, A. Mohammadian and B. Tayfeh-Rezaie, *Percolating sets in bootstrap percolation on the Hamming graphs*, arXiv:1905.01942, first public version 2019-05-06, https://arxiv.org/abs/1905.01942. This earlier preprint does not include triangular graphs.
4. B. Brešar and J. Hedžet, *Bootstrap percolation in strong products of graphs*, arXiv:2307.06623 (2023), https://arxiv.org/abs/2307.06623; distinct strong-product host setting.
