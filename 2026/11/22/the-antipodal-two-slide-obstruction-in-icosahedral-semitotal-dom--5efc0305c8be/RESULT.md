# The antipodal two-slide obstruction in icosahedral semitotal domination

## Finding
Let \(I\) be the ordinary 12-vertex icosahedral graph. A *semitotal dominating set* \(S\) is a dominating set such that every vertex of \(S\) has another selected vertex at graph distance at most two. Let \(\mathcal M\) be the family of all minimum-cardinality semitotal dominating sets. The token-jump graph \(J\) has vertex set \(\mathcal M\), with an edge when one selected vertex is replaced by any unselected vertex; the token-slide graph \(T\) permits such replacement only along an edge of \(I\). Every intermediate configuration must lie in \(\mathcal M\).

**Exact classification.** The minimum size is \(\gamma_{t2}(I)=3\), and the \(80\) sets in \(\mathcal M\) are *exactly*:

1. \(60\) triples containing an antipodal vertex pair (two vertices at distance three), together with any one of the other ten vertices;
2. \(20\) triples whose three pairwise distances are all two.

These are two orbits under the full 120-element automorphism group. Their sorted pair-distance signatures are respectively \((1,2,3)\) and \((2,2,2)\).

**Exact relocation geometry.** The graphs \(J\) and \(T\) are connected and have respectively \(480\) and \(300\) edges. In the order of the two types above, their degrees are \((13,9)\) in \(J\) and \((7,9)\) in \(T\); their eccentricities are \((3,3)\) in \(J\) and \((4,3)\) in \(T\). Thus \(J\) is self-centered with radius and diameter three, whereas \(T\) has radius three and diameter four.

Across the \(\binom{80}{2}=3160\) unordered pairs \(\{S,U\}\), the exact multiplicities of \(d_T(S,U)-d_J(S,U)\) are \(2440\), \(690\), and \(30\), for differences zero, one, and two respectively. **The 30 pairs with the maximum difference two are exactly**
\[
S=\{a,\bar a,x\},\qquad U=\{a,\bar a,\bar x\},
\]
where bars denote the unique antipodal involution on \(I\), \(\{a,\bar a\}\) is one of the six antipodal pairs, and \(\{x,\bar x\}\) is one of the other five antipodal pairs. Every such pair has \(d_J(S,U)=1\) but \(d_T(S,U)=3\).

## Assumptions and scope
The graph is *simple, undirected, unweighted, and labelled*, and graph distance is shortest-path distance in \(I\). An explicit presentation fixes vertices \(a,b,p_0,\ldots,p_4,q_0,\ldots,q_4\), indices modulo five, with edge families
\[
\{ap_i,bq_i,p_ip_{i+1},q_iq_{i+1},p_iq_i,p_iq_{i-1}\ :\ i\in\mathbb Z/5\mathbb Z\}.
\]
This has 12 vertices, 30 edges, degree five, and is isomorphic to the regular icosahedral graph. Distinct tokens are not labelled: a configuration is a *set*, not a sequence. The claim concerns minimum semitotal sets of this one graph, not arbitrary dominating sets or larger-cardinality feasible sets. Every configuration counted is a global minimum.

## Proof
**Minimum size.** Every closed neighborhood has six vertices. In the displayed icosahedral presentation, two closed neighborhoods are disjoint if and only if their centers are antipodal; then they partition the 12 vertices. A dominating pair must therefore be antipodal, with selected pair distance three. No dominating pair can satisfy the semitotal witness rule, and sizes zero or one cannot satisfy it. The displayed antipodal-pair triples do satisfy the rule, giving \(\gamma_{t2}(I)=3\).

**Exhaustive classification.** The finite predicate for a three-set \(S\) is
\[
\bigl(\forall v\in V(I),\;N[v]\cap S\neq\varnothing\bigr)
\ \land\
\bigl(\forall u\in S,\;\exists w\in S\setminus\{u\}:d_I(u,w)\le2\bigr).
\]
The certificate `verify_geometry.py`, using exactly the adjacency rule above, evaluates this predicate for all \(\binom{12}{3}=220\) distinct triples. It independently identifies the sorted pair-distance signatures and tests the asserted equivalence for *every* triple that satisfies the predicate. This yields exactly 60 triples of signature \((1,2,3)\) and 20 of signature \((2,2,2)\), and excludes every other triple. The first count also follows directly from six disjoint antipodal pairs and ten choices for the remaining vertex. The second class consists of all triangles in the graph formed by distance-two pairs of the icosahedron, whose full finite enumeration gives 20.

**Moves and distances.** For every enumerated state \(S\), every \(u\in S\), and every \(v\notin S\), the certificate constructs the candidate \((S\setminus\{u\})\cup\{v\}\) and retains it exactly when this candidate belongs to the certified 80-state family. The candidate gives an edge of \(J\); it gives an edge of \(T\) precisely when \(uv\in E(I)\). This enumerates the complete symmetric adjacency relations, not a sampled subgraph. Breadth-first search from *all 80 roots* in each graph computes 80 complete distance vectors, proving connectivity, all degrees, eccentricities, edge counts, and the all-pairs difference distribution. Finally, a separate predicate checks for each of the 3160 unordered state pairs whether they retain an antipodal pair and exchange the other member of a second antipodal pair. It is equivalent, for every pair, to a distance difference of exactly two. There are six choices for the retained pair and five for the exchanged pair, yielding precisely 30 extremal unordered pairs.

These are finite exact proof steps: the exhaustive domains are explicitly bounded and the supplied executable certificates implement each claimed quantifier. No probability, asymptotic inference, or conjectural extrapolation is used. A second, independently built NetworkX verification reconstructs the icosahedron through a separate graph generator, reevaluates the feasibility predicate, uses separate graph-building and BFS implementations, and checks the 120-element automorphism group and both orbit sizes.

## Verification
Run `python verify_geometry.py` with Python 3 (standard library only) and `python check_networkx.py` with Python 3 and NetworkX 3.x. Both scripts assert every headline count and the full 3160-pair distance and antipodal-exception characterization. The first generates the five-cycle adjacency presentation directly; the second uses `networkx.icosahedral_graph()` and `networkx.single_source_shortest_path_length`. Both completed successfully from the packaged file bytes. `VERIFICATION.md` records the exact tested assertions, execution and limitations.

## Relationship to prior work
Tripathi, Pandey, and Maheshwari (2021; arXiv:2109.02142) study a linear-time algorithm for semitotal domination on strongly chordal graphs. The icosahedral graph contains induced five-cycles and is not in that class; their optimization theorem neither enumerates these icosahedral minima nor handles their relocation graph. Bousquet, Mouawad, Nishimura, and Siebertz (2022; arXiv:2204.10526) survey token jumping and sliding for independent, dominating, and connected dominating sets, not this semitotal solution space or its distances. Křišťan and Svoboda (2023; arXiv:2307.10847) establish shortest dominating-set sliding algorithms on trees and interval graphs, not exact semitotal relocation on an icosahedron. Hemalatha and Jeyanthi (2016) give the already-known ordinary icosahedral domination number two; that numerical fact is not claimed as new here. The icosahedral paired-domination and resolving-set relocation classifications in the published mathematical record concern different feasibility conditions, not the 80 semitotal minima described above.

## Limitations
This is a theorem for one canonical twelve-vertex graph, not a general complexity bound, infinite-family classification, or proof that every similar polyhedral graph shares the behavior. Its reliability rests on transparent exhaustive finite checking; no independent mathematical audit has been completed. The literature comparison cannot exclude unindexed historical equivalents. The value lies in a natural optimal-sensor criterion, its two intrinsic geometric configuration classes, and the sharp *antipodal-only* two-move obstruction to physically local relocation; it does not claim an application-specific deployment improvement or a general downstream theorem.

## References
- V. Tripathi, A. Pandey, A. Maheshwari, *A linear-time algorithm for semitotal domination in strongly chordal graphs*, arXiv:2109.02142, first posted 2021-09-05. https://arxiv.org/abs/2109.02142
- N. Bousquet, A. E. Mouawad, N. Nishimura, S. Siebertz, *A survey on the parameterized complexity of the independent set and (connected) dominating set reconfiguration problems*, arXiv:2204.10526, first posted 2022-04-22. https://arxiv.org/abs/2204.10526
- J. M. Křišťan, J. Svoboda, *Shortest Dominating Set Reconfiguration under Token Sliding*, arXiv:2307.10847, first posted 2023-07-20. https://arxiv.org/abs/2307.10847
- G. Hemalatha, P. Jeyanthi, *Results on Domination Number and Bondage Number for Some Families of Graphs*, International Journal of Pure and Applied Mathematics 107 (2016), 565–577, Lemma 2.8. https://doi.org/10.12732/ijpam.v107i3.5
