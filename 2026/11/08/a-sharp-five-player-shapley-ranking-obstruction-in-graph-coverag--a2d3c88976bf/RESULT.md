# A sharp five-player Shapley-ranking obstruction in graph coverage games

## Finding
Let \(G=(V,E)\) be a finite simple undirected graph with \(n=|V|\ge1\). Its graph-coverage cooperative game is
\[
v_G(S)=|\{e\in E:e\cap S\ne\varnothing\}|\qquad(S\subseteq V).
\]
For a vertex ordering \(\pi\), define its inclusion area
\[
\mathcal A_G(\pi)=\sum_{t=1}^{n}v_G(\{\pi(1),\ldots,\pi(t)\}).
\]
A *Shapley ranking* is any ordering nonincreasing in the ordinary Shapley values of this game; ties may be broken in whichever way gives the largest inclusion area. Define \(\mathcal A_*(G)\) as the maximum over every ordering and \(\mathcal A_{\mathrm{Sh}}(G)\) as the maximum over Shapley rankings.

**Theorem (structure, first obstruction, and persistent loss).**

1. If \(G\) is a disjoint union of cliques, including possible isolated vertices, then \(\mathcal A_{\mathrm{Sh}}(G)=\mathcal A_*(G)\) if and only if all clique components of order at least two have the same order (the empty set or a singleton set of distinct orders is allowed).
2. For *every* simple graph on at most four vertices, \(\mathcal A_{\mathrm{Sh}}(G)=\mathcal A_*(G)\). Among the \(2^{10}=1024\) labeled simple graphs on five fixed vertices, the inequality \(\mathcal A_{\mathrm{Sh}}(G)<\mathcal A_*(G)\) holds for exactly ten, all isomorphic to \(K_3\sqcup K_2\). For this unique five-vertex obstruction type, \(\mathcal A_*(G)=17\) and \(\mathcal A_{\mathrm{Sh}}(G)=16\).
3. More generally, for all integers \(k,q\ge1\), put \(G_{k,q}=kK_3\sqcup qK_2\). Then
\[
\boxed{\mathcal A_*(G_{k,q})-\mathcal A_{\mathrm{Sh}}(G_{k,q})=kq},
\]
with the explicit optimum
\[
\mathcal A_*(G_{k,q})=\frac{13k^2+14kq+3k+3q^2+q}{2}.
\]
If \(k\to\infty\) and \(q/k\to r>0\), the relative loss \((\mathcal A_*-\mathcal A_{\mathrm{Sh}})/\mathcal A_*\) tends to
\[
\frac{2r}{13+14r+3r^2}.
\]
Its largest possible limit within this family is \(1/(7+\sqrt{39})\), attained as \(q/k\to\sqrt{13/3}\).

## Assumptions and scope
All edge-features have unit positive weight, each feature is activated by either of its two endpoint players, and different edges are distinct features. Consequently \(v_G(\varnothing)=0\), and every such game is monotone and submodular. The graph may be disconnected or edgeless, but has no loops or multiple edges. Inclusion area is the *unnormalized* sum over all nonempty prefixes, including the full vertex set; dividing all areas by \(n\) would leave every ranking comparison and relative loss unchanged. Shapley values are computed from all player permutations, and a Shapley tie may be resolved optimally. The five-vertex uniqueness statement ranges over all labeled simple graphs, not only clique unions. The infinite formula applies only to the stated \(k,q\) family.

## Proof
**Shapley and ranking reduction.** For each edge \(e=\{u,v\}\), its component game is \(1\) when the coalition contains either endpoint and \(0\) otherwise. The first of the two endpoints to join contributes its unit worth; each endpoint has probability \(1/2\) of being first in a uniform random player permutation. By linearity of Shapley values,
\[
\phi_x(v_G)=\frac{\deg_G(x)}2.
\]
Hence Shapley rankings are precisely the nonincreasing-*original-degree* orderings, including all tie resolutions.

For any ordering \(\pi\), let \(g_t\) count edges whose first endpoint appears at position \(t\). An edge so covered contributes one to each of the \(n-t+1\) prefixes from \(t\) onward, so
\[
\mathcal A_G(\pi)=\sum_{t=1}^{n}(n-t+1)g_t.
\]
Equivalently, writing \(c_\pi(e)\) for the first endpoint position,
\[
\mathcal A_G(\pi)=(n+1)|E|-\sum_{e\in E}c_\pi(e).
\]
Thus maximizing inclusion area is exactly the same ordering problem as minimizing the total first-cover time of edges (minimum-sum vertex cover), but with an additional original-degree ordering constraint for the Shapley benchmark.

**Disjoint-clique classification.** Within a component \(K_s\), the successive vertices of that component, regardless of their names or interleaving with other components, have newly covered edge counts \(s-1,s-2,\ldots,1,0\). Across the components the multiset of the \(g_t\) values is therefore fixed. Sorting these values nonincreasingly maximizes their weighted sum by the rearrangement inequality, and such a sorted merge is feasible because each component's own marginal sequence is already decreasing. This also gives the exact optimal area for any disjoint clique union: sort all the marginal counts from every component into \(b_1\ge\cdots\ge b_n\), and evaluate \(\sum_{t=1}^{n}(n-t+1)b_t\).

If all clique components with at least two vertices have the same size, they have identical positive original degrees. A sorted merge of their marginal sequences is an allowed Shapley tie-breaking (isolated vertices have degree zero and can come last); hence a Shapley ranking is optimal. Conversely, suppose there are two nontrivial clique components of sizes \(s>t\ge2\). Every Shapley ordering must put *all* \(s\) vertices of the larger component before *any* vertex of the smaller one, since \(s-1>t-1\). Its gain sequence therefore includes a zero (the last larger-clique vertex) before the positive gain \(t-1\) of the first smaller-clique vertex. The sequence is not nonincreasing; exchanging an inverted zero-positive pair in the abstract gain sequence strictly increases its weighted sum, and a sorted feasible merge realizes the improved value. No Shapley ordering is optimal. This proves the if-and-only-if statement.

**Sharp first order among all graphs.** For an arbitrary graph and a selected prefix \(S\subseteq V\), set \(u(S)=|E[V\setminus S]|\). The sum of edge cover times of an ordering with prefixes \(S_0=\varnothing,S_1,\ldots,S_n=V\) is \(\sum_{i=0}^{n-1}u(S_i)\). Consequently the exact unrestricted minimum is given by the finite recurrence
\[
D(V)=0,\qquad D(S)=u(S)+\min_{x\in V\setminus S}D(S\cup\{x\}),
\]
and the exact Shapley-constrained minimum by the same recurrence with \(x\) restricted to the remaining vertices having maximum *original* degree. The supplied independent implementations enumerate, for every \(1\le n\le5\), all \(2^{\binom n2}\) edge sets, and compute both optima once by these subset recurrences and again by explicit enumeration of every vertex permutation. They agree on every case. The counts of graphs with a strict gap are respectively \(0,0,0,0,10\) for \(n=1,2,3,4,5\). Each of the ten five-vertex cases has the exact graph type \(K_3\sqcup K_2\), as verified from the full edge sets, not inferred solely from a degree sequence. There are exactly \(\binom53=10\) labelings of that isomorphism type. Direct first-cover times for this type give optimal total cover time \(7\) and best degree-sorted cover time \(8\), so the corresponding inclusion areas are \(6\cdot4-7=17\) and \(6\cdot4-8=16\). Because the computational search is exhaustive over finite sets and the two objective implementations agree, it establishes the claimed finite first-order classification, not merely sampled evidence.

**Persistent gap.** In \(G_{k,q}\), the marginal-gain multiset is \(k\) copies of \(2\), \(k+q\) copies of \(1\), and \(k+q\) copies of \(0\). A globally optimal ordering takes all \(k\) two-gain vertices first, then all \(k+q\) one-gain vertices, then all zero-gain vertices. Every Shapley ranking instead places all degree-two triangle vertices before every degree-one matching vertex. Its best tie-breaking has marginal sequence
\[
\underbrace{2,\ldots,2}_{k},\underbrace{1,\ldots,1}_{k},\underbrace{0,\ldots,0}_{k},\underbrace{1,\ldots,1}_{q},\underbrace{0,\ldots,0}_{q}.
\]
Relative to the optimum, the \(k\) premature zero-gain choices delay each of the \(q\) later unit-gain choices by \(k\) positions. The inclusion-area loss is exactly \(kq\). Summing the weighted gains of the optimal ordering, or equivalently computing its first-cover cost \((5k^2+4kq+3k+q^2+q)/2\) and subtracting it from \((3k+2q+1)(3k+q)\), yields the stated optimum. Dividing \(kq\) by this optimum, letting \(q/k\to r\), and maximizing the resulting rational function gives the claimed ratio and its unique maximizing positive \(r=\sqrt{13/3}\).

## Verification
Run `python3 verify_coverage.py` with the Python standard library. The checker compares two independent exhaustive algorithms on every simple labeled graph of orders one through five, totaling \(1099\) graphs: a subset dynamic program and direct examination of every permutation. It confirms ten and only ten strict failures at order five, all of type \(K_3\sqcup K_2\). It additionally tests the analytic family formulas by exact subset dynamic programming on nine pairs of parameters with \(1\le k,q\le3\), and checks the disjoint-clique structural classification and sorted-gain formula for all \(138\) integer component-size partitions of orders up to ten. These are exact finite cross-checks; the general disjoint-clique criterion, all-parameter family formulas, and limiting ratio are proved above analytically.

## Relationship to prior work
Li, Liu, Yu, and Low (2026, arXiv:2607.09869) motivate the inclusion-area objective and prove that Shapley rankings can be misleading in unrestricted cooperative games, including a four-player pathological example. Their construction uses general utility functions and Shapley-nullspace perturbations. It does not provide the sharp boundary within *unit-edge graph coverage games*, the classification of all five-player cases in that restricted domain, or the persistent tie-robust loss here.

Biniaz, De Carufel, Maheshwari, Odak, and Smid (2026, arXiv:2609.27117) study minimum-sum vertex cover and give a general subset dynamic program and approximation algorithms. The present proof explicitly acknowledges and uses that standard equivalence; no new general-purpose vertex-cover algorithm is claimed. Their results do not state the graph-coverage Shapley ranking criterion, five-player uniqueness or the stated loss formula. A separately available result on *complete multipartite* graphs gives a minimum first-cover formula on that class; the complement of a clique union is complete multipartite, but minimizing cover time on a complement concerns *maximizing* cover time on the original graph, not the minimization needed here. That result therefore does not imply the present formulas.

## Limitations
The structural if-and-only-if applies to disjoint clique unions and does not classify all larger graph coverage games. The universal first-order census stops at five vertices; the infinite family is proved independently. Unit edge weights and ordinary Shapley rankings are essential. The theorem is about inclusion-area optimality, not coalition stability, core membership, or causal attribution validity. An older or unindexed study of degree-priority minimum-sum vertex cover could contain an equivalent special case; the accessed sources did not establish such coverage.

## References
1. W. Li, Z. Liu, Y. Yu, and B. K. H. Low, *Nonlinear Axiomatic Attribution for Cooperative Games*, arXiv:2607.09869, first submitted 10 July 2026. https://arxiv.org/abs/2607.09869
2. A. Biniaz, J.-L. De Carufel, A. Maheshwari, S. Odak, and M. Smid, *Minimum Sum Vertex Cover via Minimum Vertex Cover*, arXiv:2609.27117, first submitted 22 September 2026. https://arxiv.org/abs/2609.27117
3. *Minimum-sum vertex cover on complete multipartite graphs*, published mathematical research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-minimum-sum-vertex-cover-on-complete-multipartite-graphs--0406c3406a18
