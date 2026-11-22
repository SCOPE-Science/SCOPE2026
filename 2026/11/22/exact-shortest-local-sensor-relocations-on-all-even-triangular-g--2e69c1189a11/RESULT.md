# Exact shortest local sensor relocations on all even triangular graphs

## Finding

For an integer \(k\ge1\), put \(n=2k+2\) and let \(T_n=L(K_n)\) be the triangular graph: its vertices are two-element subsets of \([n]\), adjacent when they intersect. Let \(R_n\) be the graph of **minimum power-dominating sets** of \(T_n\), joined when one selected vertex is replaced by an adjacent vertex of \(T_n\) and all intermediate sets remain minimum power dominating.

Every configuration is a size-\(k\) matching of \(K_n\), leaving precisely two vertices (*holes*) unmatched. For any two such matchings \(M,N\), let \(r=|N\setminus M|=k-|M\cap N|\). The graph with edges \(M\mathbin\triangle N\) consists of disjoint alternating paths and nontrivial even alternating cycles. Let \(c(M,N)\) be the number of cycle components, and put \(\delta(M,N)=1\) if the two holes of \(M\) belong to the **same nontrivial path component** of \(M\mathbin\triangle N\); otherwise put \(\delta(M,N)=0\). These quantities are defined directly from the two endpoint configurations.

**Exact all-pairs slide metric:**
\[
\boxed{d_{R_n}(M,N)=r+c(M,N)+\delta(M,N).}
\]
The formula gives the true distance in the **entire** reconfiguration graph, where hole positions may change arbitrarily along the path. In particular, for equal endpoint hole pairs, \(\delta=0\) and the extra distance beyond the number of differing edges is exactly the number of nontrivial alternating cycles.

**Exact global geometry:** The graph is connected, vertex-transitive and \(4k\)-regular, and
\[
\boxed{\operatorname{diam}(R_n)=\operatorname{rad}(R_n)=\left\lceil\frac{3k}{2}\right\rceil.}
\]
Moreover, the neighbors of every configuration induce exactly \(k\) disjoint four-cycles, and
\[
|V(R_n)|=\frac{(2k+2)!}{2^{k+1}k!},\qquad
|E(R_n)|=2k|V(R_n)|,\qquad
\#\{\text{triangles in }R_n\}=\frac{4k}{3}|V(R_n)|.
\]

The power-domination predicate and minimum matching enumeration are already known and **are not claimed as new**. The contribution is the all-pairs **local** reconfiguration metric, sharp global diameter and associated local geometry, including the proof that extra edges available in the complete-graph matching model cannot shorten these prescribed routes.

## Assumptions and scope

All graphs are finite, labeled, simple and undirected. A nonempty set \(S\) of vertices of \(G\) is power dominating if, after observing its closed neighborhood, the rule that an observed vertex with precisely one unobserved neighbor observes that neighbor eventually observes the entire graph. Each vertex of \(T_n\) corresponds to an edge of \(K_n\). A valid token slide in \(T_n\) exchanges one selected edge of \(K_n\) for an intersecting edge, while maintaining a size-\(k\) matching; it is **not** an arbitrary token jump or a temporary token addition. The holes in a configuration are unmatched vertices of \(K_n\).

For \(M,N\), the symmetric difference \(M\triangle N=(M\setminus N)\cup(N\setminus M)\) is an ordinary simple graph; common matching edges are not included. Every nontrivial component is an alternating path or even cycle. An isolated vertex is not a nontrivial path, and the two source holes are distinct. The indicator \(\delta=1\) precisely when the same path has both source holes as endpoints. This necessarily entails a second path whose endpoints are the two target holes, since \(|M|=|N|\).

## Proof

**1. The optimum sensor states (known characterization, reconstructed).** Interpret a set \(S\subseteq V(T_n)\) as an edge set of the auxiliary \(K_n\), and let \(U\) be the original vertices untouched by these edges. Immediately after observation of the closed neighborhood, exactly the edges internal to \(K_U\) remain unobserved. If \(|U|\le1\), none remain; if \(|U|=2\), exactly one remains and is forced by a cross edge incident with one of its endpoints. If \(|U|\ge3\), an observed edge has either zero or at least \(|U|-1\ge2\) unobserved neighbors, and no force can begin. Thus a nonempty set power dominates exactly when it leaves at most two original vertices uncovered. At least \(n-2=2k\) labels must be covered, requiring \(k\) selected edges; equality requires those edges to have pairwise disjoint endpoints. Conversely every size-\(k\) matching leaves two holes and power dominates. Hence there are \(\binom n2(2k)!/(2^kk!)=n!/(2^{k+1}k!)\) minimum states.

**2. Four-cycles and connectivity.** For a selected edge \(ab\) and holes \(u,v\), the only allowed replacements are \(au,av,bu,bv\). These four neighbor configurations form a chordless four-cycle (successive replacement edges share a label, opposite ones do not). Configurations obtained by changing different selected edges are not adjacent. Hence the neighbors induce \(kC_4\), so \(R_n\) is \(4k\)-regular, and counting edges and triangles gives the stated expressions. A permutation of \([n]\) sends any matching configuration to any other, so the graph is vertex-transitive.

For connectivity, freeze each target edge as soon as it is installed. With two holes among the remaining unfrozen labels, any outstanding target edge \(xy\) can be installed using at most two slides: if one endpoint is a hole, slide the edge incident with the other endpoint to \(xy\); if neither is a hole, slide the edge at \(x\) to a hole to free \(x\), then slide the edge at \(y\) to \(xy\); if both are holes, use any remaining matched edge \(ab\) and slide \(ab\to ax\to xy\). The last case necessarily has an unfrozen matched edge when a target edge remains. No frozen target edge is altered. Repeating reaches every target matching and proves connectivity.

**3. All-pairs lower bound.** Put \(r=|N\setminus M|\). Each of the \(r\) absent target edges must be inserted on a distinct slide. Call a slide *nontarget* if the edge it inserts does not belong to \(N\). Consider any component \(C\) of \(M\triangle N\) that is either a nontrivial alternating cycle or an alternating path whose two endpoints are both **holes of \(N\)** (so its first and last edges belong to \(M\)). Until an original \(M\)-edge of \(C\) is removed, every vertex of \(C\) is covered by a distinct original \(M\)-edge of \(C\). In particular its first original-edge removal cannot insert an \(N\)-edge of \(C\): every such target edge connects endpoints of two different still-present original matching edges. It cannot insert an \(N\)-edge of another component either, because a slide must share an endpoint with the removed edge and the components are disjoint. Consequently the first removal of an original \(M\)-edge of \(C\) is necessarily a nontarget slide. Distinct such components require distinct nontarget moves.

There are exactly \(c(M,N)\) nontrivial cycles. If \(\delta=1\), the two source holes lie at the endpoints of an alternating path starting and ending in \(N\), with one more \(N\)-edge than \(M\)-edge. The equal total cardinalities force a second path starting and ending in \(M\), with the two target holes as endpoints. This contributes one additional component of the preceding *fully initially matched* kind; when \(\delta=0\) no such extra component exists. Hence every path from \(M\) to \(N\) has at least \(r\) target insertions and \(c+\delta\) distinct nontarget slides, establishing
\[d_{R_n}(M,N)\ge r+c+\delta.\]
The argument allows paths through any configurations of \(R_n\); it does not assume the holes or a bipartition stay fixed.

**4. Sharp constructive upper bound.** First resolve the disjoint nontrivial alternating cycles using one currently available hole \(h\). For a cycle with \(q\ge2\) old matching edges \(a_i b_i\) and new edges \(b_i a_{i+1}\) (cyclic indices), perform
\[
 a_1b_1\to a_1h;\quad
 a_i b_i\to b_{i-1}a_i\quad(2\le i\le q);\quad
 a_1h\to b_q a_1.
\]
This installs all \(q\) desired edges in \(q+1\) slides, restores \(h\) as a hole, and never alters another symmetric-difference component. Repeating over all cycles uses exactly their number of target insertions plus \(c\) nontarget slides. Thus only the alternating path components remain, with the two original source holes still free.

If \(\delta=0\), every nontrivial alternating path has one source hole at an endpoint and one target hole at its other endpoint. Starting at the source hole, successively slide each old matching edge onto the next target edge along the path. Each step moves the hole one position along and installs a target edge; the number of steps equals the number of desired edges on that path. Components with a hole that belongs to both configurations require no move. This achieves exactly \(r+c\) slides.

If \(\delta=1\), there are exactly two remaining path components. Write the alternating path \(B\) between the two source holes \(h_L,h_R\) so that its old edges are \(a_i b_i\) for \(1\le i\le m\), and its desired edges are \(h_La_1\), \(b_i a_{i+1}\) for \(1\le i<m\), and \(b_mh_R\). The degenerate case \(m=0\) means that \(B\) consists of the single desired edge \(h_Lh_R\). Write the other path \(C\), whose endpoints \(p_0,q_{\ell+1}\) are the two target holes, so that its old edges are \(p_{j-1}q_j\) for \(1\le j\le\ell+1\) and its desired edges are \(q_jp_j\) for \(1\le j\le\ell\), with \(\ell\ge0\). Both paths have disjoint vertex sets. Make **one** nontarget cross-path slide \(p_0q_1\to p_0h_L\), leaving \(h_R,q_1\) as holes. Starting at \(h_R\), slide the edges of \(B\) in reverse order onto its desired edges, finally replacing \(p_0h_L\) by \(h_La_1\) (or \(h_Lh_R\) when \(m=0\)); the holes are then \(p_0,q_1\). Starting with the hole \(q_1\), slide the remaining old edges \(p_jq_{j+1}\to p_jq_j\) for \(1\le j\le\ell\). This installs every remaining desired edge and leaves exactly the target holes \(p_0,q_{\ell+1}\). Each move is a genuine incident-edge slide preserving the matching size. The one cross-path nontarget step plus exactly one step for each desired path edge therefore realizes \(r+c+1\) total slides.

The constructions in both cases match the lower bound; this proves the exact all-pairs formula. Each route can moreover be confined to a suitable spanning complete balanced bipartite subgraph of \(K_{2k+2}\): two-colored alternating components can be oriented independently, with the two original holes on opposite sides, and the temporary cycle/hole and cross-path edges can be made to cross that bipartition. Thus, despite the additional available complete-graph slides, each pair has a shortest route in a balanced bipartite subgraph containing both endpoints.

**5. Sharp diameter.** Every nontrivial alternating cycle uses at least two matching edges, so \(2c\le r\le k\). If \(\delta=1\), at least one target edge occurs on the source-hole-to-source-hole path outside the cycles, so \(2c\le r-1\). Therefore in either case
\[
 d(M,N)\le\max\bigl\{k+\lfloor k/2\rfloor,\ k+\lfloor(k-1)/2\rfloor+1\bigr\}
 =\left\lceil\frac{3k}{2}\right\rceil.
\]
For even \(k=2m\), take \(m\) disjoint alternating four-cycles on all \(2k\) covered labels, with the same two holes in both matchings. This gives \(r=k,c=m,\delta=0\) and distance \(3m\). For odd \(k=2m+1\), take \(m\) disjoint alternating four-cycles together with one more old edge \(ab\) and two source holes \(u,v\); replace \(ab\) by \(uv\) in the target and reverse the matching on each four-cycle. Here \(r=k,c=m,\delta=1\), so the distance is \(3m+2\). Both constructions achieve the bound, even when \(k=1\). Vertex-transitivity makes radius equal diameter.

## Verification

Two self-contained Python 3 standard-library programs test the theorem using different representations. `verify_slide.py` generates every size-\(k\) matching with two holes for \(n=4,6,8,10,12\), explicitly builds the complete slide graph, and breadth-first searches all states from a canonical starting matching. It independently obtains path/cycle components from the symmetric difference, checks **every target state** against the all-pairs distance formula, and verifies connectedness, degree, edge count and sharp diameter. By vertex-transitivity, one exhaustive starting state represents every ordered endpoint pair under a relabeling. Its largest instance has \(62{,}370\) states and \(623{,}700\) undirected transitions.

`verify_predicate.py` independently builds triangular-graph adjacency from intersecting two-subsets, exhaustively simulates observation and zero-forcing propagation for every sensor set through the minimum cardinality at \(n=4,6,8,10\), verifies that precisely the selected matchings succeed, and checks all local degrees and triangles. At \(n=10\) it checks \(148{,}995\) candidate four-sensor sets. Run `python3 verify_slide.py` and `python3 verify_predicate.py`; their passing outputs are recorded in `verification_output.txt`. The unrestricted theorem depends on the proof above, not finite testing.

## Relationship to prior work

The public *Power domination of triangular graphs: star-forest rigidity and full enumerators* establishes the criterion and optimum state counts for \(L(K_n)\); those inputs are explicitly credited. *Exact component profiles for power-domination reconfiguration of triangular graphs* concerns the **TAR** model, where an intermediate extra sensor is permitted, not constant-cardinality adjacent sliding.

Bousquet, Hatanaka, Ito and Mühlenthaler, *Shortest Reconfiguration of Matchings* (2018), develop exact **token-jump** matching distances; their stated sliding equivalence concerns **maximum-cardinality** matchings, whereas these configurations have cardinality one below the maximum of \(K_n\). Their Lemma 5 allows a jump surcharge of at most one for nonmaximal matchings, while the present slide formula has an unbounded cycle surcharge.

A particularly close prior finding is *An exact cycle-potential metric for sliding near-perfect bipartite matchings* (2026). It determines an exact distance formula for size-\(k\) matchings of the balanced complete bipartite graph \(K_{k+1,k+1}\), and its formula gives an **upper bound** for the distance here after choosing a bipartition containing both endpoint matchings. However the present graph has **all** edges of \(K_{2k+2}\), including within-part shortcuts, so its all-pairs distances could be shorter. The bipartite theorem does not furnish the essential complete-graph lower bound proved in Step 3, nor by itself the pairwise isometry or exact full-graph diameter. These are the present mathematical contributions. The full primary results and relevant public record texts were compared for implication, not only for matching terminology.

Bjorkman and coauthors, *Power domination reconfiguration* (2022), introduce general TAR and TJ concepts but no constant-cardinality TS metric of these graphs. Ito and coauthors (ESA 2019) allow whole alternating-cycle flips of perfect matchings, a different operation.

## Limitations

The power-domination feasibility characterization and counts are previously known. The all-pairs distance claim concerns the even triangular graphs and this particular adjacency-restricted reconfiguration rule. It does not establish a diameter for other graph families, nor shortest-path multiplicities. A very close complete-bipartite distance theorem supplies a matching upper-bound mechanism, but does not directly establish that extra nonbipartite slides yield no shortcuts. An unindexed historical complete-graph equivalent remains a publication-priority risk. No independent mathematical audit has been performed.

## References

1. N. Bousquet, T. Hatanaka, T. Ito, M. Mühlenthaler, *Shortest Reconfiguration of Matchings*, arXiv:1812.05419v1, first public 2018-12-13, https://arxiv.org/html/1812.05419v1 .
2. B. Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798v1, first public 2022-01-05, https://arxiv.org/html/2201.01798v1 .
3. *Power domination of triangular graphs: star-forest rigidity and full enumerators*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-power-domination-of-triangular-graphs-star-forest-rigidity-and-f--b7c1b689a10e .
4. *Exact component profiles for power-domination reconfiguration of triangular graphs*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-component-profiles-for-power-domination-reconfiguration-of--69bbf2c2096e .
5. *An exact cycle-potential metric for sliding near-perfect bipartite matchings*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-cycle-potential-metric-for-sliding-near-perfect-biparti--df80d3d712a4 .
6. T. Ito et al., *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, ESA 2019, https://doi.org/10.4230/LIPIcs.ESA.2019.61 .
