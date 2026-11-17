# Spanning-tree bijection and minimum paired domination in two-subset Kneser graphs

## Finding
For every integer \(n\ge4\), let \(K(n,2)\) be the Kneser graph whose vertices are the unordered pairs of \([n]\), adjacent precisely when disjoint. A paired dominating set is a dominating vertex set whose induced graph has a perfect matching. Let \(\gamma_{\mathrm{pr}}(K(n,2))\) be the smallest cardinality of such a set, and let \(b_n\) count all paired dominating sets of that minimum size.

The exact answer is
\[
\gamma_{\mathrm{pr}}(K(n,2))=\begin{cases}6,&n=4,5,\\4,&n\ge6,\end{cases}
\qquad
b_n=\begin{cases}1,&n=4,\\125,&n=5,\\180\binom n6+315\binom n7+105\binom n8,&n\ge6.\end{cases}
\]
Binomial coefficients with lower index exceeding the upper index are zero. In particular, the \(125=5^3\) optimal configurations in the Petersen graph \(K(5,2)\) are in canonical bijection with the labeled spanning trees on five vertices. For \(n\ge6\), the auxiliary edge graphs of all minimum paired dominating sets are precisely \(P_4\sqcup K_2\), \(P_3\sqcup2K_2\), or \(4K_2\), with any unused labels isolated.

## Assumptions and scope
Graphs are finite, simple, undirected, and vertex labels are distinct. A dominating set covers itself by closed neighborhoods. A perfect matching of the selected induced Kneser subgraph pairs every selected vertex with a **different**, adjacent selected vertex. The formulas count selected vertex sets, not choices of their perfect matchings. The graphs \(P_k\) and \(K_k\) have \(k\) vertices. The disjoint union symbol \(\sqcup\) is used in the auxiliary graph, which has vertex set \([n]\); isolated auxiliary vertices may be omitted in naming its components.

## Proof
**1. An exact cover translation.** Given a selected Kneser vertex set \(S\), construct \(H=([n],S)\), treating each selected two-element subset as an edge. For any two-element set \(e\), a selected vertex adjacent to \(e\) exists precisely when \(H\) has an edge disjoint from \(e\). This fails exactly when the two endpoints of \(e\) form a vertex cover of \(H\). If \(K(n,2)[S]\) has a perfect matching, each selected \(e\in S\) has a disjoint selected partner, so a two-element vertex cover of \(H\) cannot be selected. Hence, for a set whose Kneser-induced subgraph has a perfect matching,
\[
S\text{ is dominating}\quad\Longleftrightarrow\quad\tau(H)\ge3,
\tag{1}
\]
where \(\tau(H)\) is the vertex-cover number. The condition \(\tau(H)\ge3\) is also sufficient for total domination, but no total-domination result is assumed here.

**2. Every feasible four-set.** A paired set has even cardinality; no two-edge graph has vertex-cover number three, so no paired dominating set has size two. Suppose \(|S|=4\) and \(\tau(H)\ge3\). If \(H\) contains a triangle, the fourth edge must be disjoint from the triangle, since otherwise two vertices would cover all four edges. Thus \(H\cong K_3\sqcup K_2\). Its four corresponding Kneser vertices induce the star \(K_{1,3}\), which has no perfect matching. Therefore a four-vertex paired dominating set has a triangle-free auxiliary \(H\). A triangle-free simple graph having at most four edges is bipartite, because an odd cycle would need at least five edges. By König's theorem, \(\tau(H)=\nu(H)\), so \(\tau(H)\ge3\) forces three pairwise disjoint edges. The fourth auxiliary edge either misses all three, meets just one, or connects distinct edges of the three-edge matching. Accordingly,
\[
H\cong 4K_2,\qquad P_3\sqcup2K_2,\qquad P_4\sqcup K_2.\tag{2}
\]
Conversely, each graph in (2) contains three disjoint edges, so \(\tau(H)\ge3\). Its four Kneser vertices admit a perfect matching: for \(4K_2\), all selected vertices are pairwise adjacent; for \(P_3\sqcup2K_2\), pair the two edges of \(P_3\) separately to the two isolated edges; for \(P_4\sqcup K_2\), pair the two end edges of \(P_4\), then pair its middle edge to the isolated edge. Equation (1) proves they are paired dominating. Their auxiliary support sizes are respectively eight, seven and six. Hence no four-set exists for \(n=4\) or \(n=5\), but four-sets exist for every \(n\ge6\).

Counting the three labeled shapes on their support gives
\[
\frac{8!}{2^4 4!}\binom n8=105\binom n8,\qquad
\binom73\cdot3\cdot3\binom n7=315\binom n7,\qquad
\binom64\cdot\frac{4!}{2}\binom n6=180\binom n6.
\]
The counts are disjoint because the component types differ, and together prove the formula for \(n\ge6\).

**3. The Petersen graph is a Cayley-tree case.** Fix \(n=5\). Let \(|S|=6\), so the auxiliary graph \(H\) has six of the ten edges of \(K_5\), and let \(B=K_5-E(H)\) have the remaining four edges. Since \(\tau(H)=5-\alpha(H)\), the inequality \(\tau(H)\ge3\) is equivalent to \(B\) being triangle-free. Any triangle-free graph with five vertices and four edges is either a spanning tree or a four-cycle together with an isolated vertex: if connected it is a tree; if disconnected it must contain a cycle of length at least four, forcing the latter case.

For the four-cycle case, label the cycle `01,12,23,30` and the isolated vertex `4`. The selected auxiliary edges include `04` and `24`; in the induced Kneser subgraph both selected vertices `04` and `24` have just one available neighbor, `13`, so no perfect matching exists. For each of the three unlabeled types of five-vertex trees, a perfect matching can be given explicitly. Here `ij` denotes the auxiliary edge \(\{i,j\}\); a parenthesized pair lists two disjoint auxiliary edges, hence an edge of the Kneser graph:

- If \(B\) is the star with edges `01,02,03,04`, the three Kneser matching edges are `(12,34), (13,24), (14,23)`.
- If \(B\) is the fork with edges `01,02,03,34`, the matching is `(04,12), (13,24), (14,23)`.
- If \(B\) is the path with edges `01,12,23,34`, the matching is `(02,14), (03,24), (04,13)`.

Each displayed pair consists of disjoint edges of \(K_5\) and together the three pairs use exactly the six edges of \(H=K_5-E(B)\). Since a tree is triangle-free, \(\tau(H)\ge3\), and (1) proves paired domination. Thus the six-element paired dominating sets correspond bijectively to spanning trees \(B\) of \(K_5\). Cayley's formula gives \(5^{5-2}=125\) such sets. No smaller paired dominating set exists by step 2; hence these are exactly the minimum sets.

**4. The four-label exception.** The graph \(K(4,2)\) is the disjoint union of three ordinary edges: each two-element subset has exactly its complementary subset as a neighbor. A paired dominating set must select both endpoints of each component, giving one minimum set of size six. This proves every stated case.

## Verification
The included source file `verify_min_paired_kg2.cpp` uses a direct Kneser adjacency construction and an independent backtracking perfect-matching test. It exhaustively tests every nonempty vertex subset for \(n=4,5,6,7\), a total of \(2{,}131{,}004\) subsets. It confirms minimum-set counts \(1,125,180,1575\), identifies the tree complement for every minimum set at \(n=5\), and confirms the three auxiliary configurations for every four-set at \(n=6,7\). It also independently tests all \(\binom{28}{4}=20475\) four-subsets of \(K(8,2)\), finding \(7665\) minimum sets, as predicted by the formula. Build with `c++ -O2 -std=c++17 verify_min_paired_kg2.cpp -o verify && ./verify`. The unrestricted argument is the proof above, not finite extrapolation.

## Relationship to prior work
Haynes and Slater (1998) introduced paired domination, including the perfect-matching requirement. Sheng and Lu (2020) discuss the Petersen graph as the extremal cubic equality graph for a known paired-domination bound; its minimum value six is therefore prior knowledge, **not a claimed novelty here**. Cornet and Torres (first preprint August 29, 2023; revised April 2024) classify \(k\)-tuple domination on Kneser graphs and give an incidence-degree criterion for \(K(n,2)\). Ordinary and \(k\)-tuple closed-neighborhood domination do not impose a perfect matching on the selected induced subgraph. The present contribution is the complete enumeration and auxiliary-graph classification of **minimum paired dominating sets**, including the tree bijection at \(n=5\). No claim is made concerning the counts of all paired dominating sets or inclusion-minimal nonminimum sets.

## Limitations
The result is confined to two-subset Kneser graphs with \(n\ge4\). No formula for larger Kneser set size is established. Publication priority is provisional: broad databases and the most relevant accessible primary documents were examined, but a differently named or unindexed classification may exist. The original 1998 paper was available as an abstract in this review, not as a full inspected article. The included computations cover only stated finite orders. An independent mathematical audit has not been performed.

## References
1. T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks 32 (1998), 199–206. DOI `10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F`.
2. B. Sheng and C. Lu, *The Paired Domination Number of Cubic Graphs*, arXiv:2011.12496, first public November 25, 2020. https://arxiv.org/pdf/2011.12496
3. M. G. Cornet and P. Torres, *k-tuple domination on Kneser graphs*, arXiv:2308.15603, first public August 29, 2023. https://arxiv.org/pdf/2308.15603
4. A. Cayley, *A theorem on trees* (1889), yielding the labeled-tree count \(n^{n-2}\).
