# Six symmetry types and two sharp consensus clocks for minimal pinned majorities on the Franklin graph

## Finding

On the twelve-vertex Franklin graph, permanently fixing a set \(S\) of vertices to opinion one, while every other vertex repeatedly takes the strict majority of its three neighbors, guarantees eventual all-one agreement **from every initial configuration consistent with the pins** if and only if the graph induced by the unpinned vertices is a forest. The minimum possible number of pinned vertices is **four**, and precisely **144** of the \(\binom{12}{4}=495\) four-vertex sets work. Every successful four-vertex placement forces consensus by the sharp bound **four synchronous updates** from every compatible initial state. Exactly \(72\) optimal placements attain consensus from the worst starting state after three updates and the other \(72\) after four.

Under the full graph automorphism group of order \(48\), these \(144\) optimal placements form **six** symmetry classes:

| Representative pinned vertices | Number of sets | Worst consensus time | Edges among pins |
|---|---:|---:|---:|
| \(\{0,2,4,6\}\) | 24 | 3 | 0 |
| \(\{0,2,6,9\}\) | 12 | 3 | 0 |
| \(\{0,1,3,6\}\) | 24 | 3 | 1 |
| \(\{0,1,3,9\}\) | 12 | 3 | 1 |
| \(\{0,2,4,7\}\) | 48 | 4 | 1 |
| \(\{0,2,5,9\}\) | 24 | 4 | 1 |

Among the optimal pinned sets, \(36\) are independent and leave a two-component forest; the other \(108\) induce exactly one edge and leave an eight-vertex tree. The exact enumeration and the two convergence clocks are finite facts about this specific canonical network; no all-graph classification is asserted.

## Assumptions and scope

Label the Franklin graph's vertices by \(0,\ldots,11\). Take the Hamiltonian edges \(\{i,i+1\}\) modulo twelve and the chords \(\{2j,2j+5\}\) modulo twelve for \(j=0,\ldots,5\). This is the standard cubic graph with LCF notation `[5,-5]^6`. It is simple, undirected, bipartite, with twelve labelled vertices and eighteen edges. All counts distinguish the labels; only the six-class column quotients by graph automorphisms.

For a pinned set \(S\), the configuration space consists of every binary vertex assignment \(x\) with \(x_v=1\) for \(v\in S\). Write \(F_S(x)_v=1\) for pinned vertices and, otherwise, exactly when at least two of the three graph neighbors of \(v\) have value one in \(x\). Updates occur synchronously. The forced-consensus time \(T(S)\) is the least \(t\ge0\) such that \(F_S^t(x)\) is all-one for **every** such initial state \(x\); set it to infinity if no such time exists. The graph is finite; no majority ties occur. The result concerns permanent pins and does not equate them with ephemeral initial minority/majority seeds in the unmodified dynamics.

## Proof

**1. All-compatible-state reduction.** The map \(F_S\) preserves the coordinatewise order. Let \(\mathbf1_S\) denote the least compatible state, whose ones are precisely the pinned vertices. Since \(F_S(\mathbf1_S)\ge\mathbf1_S\), induction shows that the iterates from \(\mathbf1_S\) are increasing. For every compatible \(x\ge\mathbf1_S\), monotonicity gives \(F_S^t(x)\ge F_S^t(\mathbf1_S)\). Thus universal consensus is equivalent to the least-state trajectory reaching the all-one state, and whenever this happens \(T(S)\) is exactly its first hitting time.

**2. The forest criterion and sharp lower bound.** In this least-state trajectory, an unpinned zero becomes one at the next update precisely when it has at most one presently zero neighbor. Therefore the subgraph induced by zero vertices is stripped of every vertex of current degree at most one in each round. A finite graph is completely eliminated by this simultaneous leaf-stripping process if and only if it has no cycle. This proves the forest characterization.

Suppose \(|S|=k\), and let \(e(S)\) be its induced edge count. Because the Franklin graph is cubic with eighteen edges, the complement on \(12-k\) vertices contains \(18-3k+e(S)\) edges. A forest on \(12-k\) vertices has at most \(11-k\) edges, so
\[
18-3k+e(S)\le11-k,\qquad 7+e(S)\le2k.
\]
For \(k\le3\) this is impossible. Hence four pins are necessary. When \(k=4\), the complement has \(8\) vertices and \(6+e(S)\) edges; if it is a forest, it follows that \(e(S)\) is zero or one. If zero, its number of components is two; if one, it is a tree. These are structural necessities, not empirical extrapolations.

**3. Exact 144-set and six-orbit classification.** The graph has only \(\binom{12}{4}=495\) possible four-element pinned sets. The following complete integer enumeration is an exact finite proof: for each increasing quadruple of vertex labels, form the complement's induced adjacency lists; run depth-first search and reject a set if any explored edge closes a cycle. Exactly 144 quadruples survive, of which 36 have zero pin-internal edges and 108 have one. The complete, explicitly reproducible enumeration is `VERIFY_FORESTS.py`; the 144 surviving labelled sets, with their times, are also listed in `min_forcing_sets.csv`. No probabilistic sampling is involved.

To quotient by symmetry without assuming a library automorphism table, the same verifier enumerates all bijections \(\sigma:\{0,\ldots,11\}\to\{0,\ldots,11\}\) consistent with both adjacency and nonadjacency. The backtracking enumerator obtains precisely 48 automorphisms. Applying them to the 144 valid quadruples partitions those sets into six pairwise disjoint orbits, with the representatives and sizes tabulated above. The orbit sizes sum to 144, proving completeness. Each representative can be checked directly against the displayed edge rule; each orbit consists entirely of forest-complement pins because graph automorphisms preserve cycles.

**4. Exact convergence times.** On a forest complement, each round simultaneously removes all vertices of degree zero or one, as proved in step 2. Computing these rounds on the six canonical representatives gives respective leaf-stripping depths \(3,3,3,3,4,4\). Since all placements within one automorphism orbit have identical depths, the orbit sizes give exactly \(24+12+24+12=72\) three-update placements and \(48+24=72\) four-update placements. The witness \(S=\{0,2,4,7\}\) needs all four rounds, showing sharpness. Starting from any compatible state cannot be slower than starting from \(\mathbf1_S\), so the same values are the worst-case all-initial-state times.

## Verification

The standalone standard-library `VERIFY_FORESTS.py` constructs the graph by the Hamiltonian-plus-chords rule, exhaustively checks all 495 four-pin complements for cycles, enumerates all 48 automorphisms without a graph package, constructs their six orbits, verifies every reported orbit size and forest geometry, and exports the 144 optimal placements. `VERIFY_DYNAMIC.py` independently constructs the original graph by adding all 12 rim edges and only the six even-to-odd chords, simulates all pinned-set starts of sizes zero through four, and independently obtains the same 144 successful four-pin sets and three/four-update histogram. It additionally simulates every one of the \(144\cdot2^8=36{,}864\) initial configurations compatible with the optimum four-pin sets and checks consensus no later than their asserted sharp time. Reproduce from these actual files using `python3 VERIFY_FORESTS.py min_forcing_sets.csv` and `python3 VERIFY_DYNAMIC.py`.

The analytic order/forest equivalence and degree bound apply without code. The six orbit counts, the 144-set total, and the representative stripping depths are complete finite calculations with exact code and explicit labelled certificate; no infinite-family extrapolation or hidden external computation is used.

## Relationship to prior work

The general theory of strict-majority dynamic monopolies and threshold-two bootstrap activation establishes the relevant irreversible seed interpretation. In particular, the 2012 study *On dynamic monopolies of graphs: the average and strict majority thresholds* supplies graph-wide bounds, not the Franklin graph's exact set census. The 2016 paper *Dynamic Monopolies for Degree Proportional Thresholds in Connected Graphs of Girth at least Five and Trees* explains the duality between dynamic monopolies and generalized-degenerate complements; its girth-at-least-five main scope does not include the Franklin graph, whose girth is four. The universal equivalence with feedback vertex sets, and the cubic edge-count bound, are elementary and are **not** presented as original.

A published Heawood-graph classification counts seventy minimum feedback-vertex sets in two symmetry orbits; it concerns a different fourteen-vertex graph, and its conclusion does not imply the six Franklin classes. Earlier unpinned majority classifications of twelve-vertex cubic bipartite graphs determine recurrence and attraction basins without pinning, so they do not determine the minimum guaranteed-consensus intervention or the two sharp forcing clocks. The previously established graph identification and paired-domination invariant for Franklin are likewise distinct. General convergence theory for synchronous majorities guarantees eventual periods at most two, without specifying the optimum pinned sets on this graph.

## Limitations

This theorem is an exact finite classification for the Franklin graph, not a novel general feedback-vertex-set principle or a claim of superior complexity bounds. It does not count attractor basins for suboptimal pinned sets or determine the transient dynamics when consensus is not forced. The 2012 dynamic-monopoly paper was available as an abstract but not inspected in complete text. Database and bibliographic searching cannot rule out an unindexed historical Franklin decycling-set table. The result has not undergone independent mathematical validation.

## References

1. K. Khoshkhah, H. Soltani, M. Zaker, *On dynamic monopolies of graphs: the average and strict majority thresholds*, arXiv:1202.1146v1 (first public February 6, 2012), https://arxiv.org/abs/1202.1146.
2. M. Gentner, D. Rautenbach, *Dynamic Monopolies for Degree Proportional Thresholds in Connected Graphs of Girth at least Five and Trees*, arXiv:1601.02099v1 (January 9, 2016), https://arxiv.org/abs/1601.02099.
3. I. Benjamini et al., *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (May 11, 2014), https://arxiv.org/abs/1405.2486.
4. E. W. Weisstein, *Franklin Graph*, MathWorld, https://mathworld.wolfram.com/FranklinGraph.html; identification with LCF `[5,-5]^6` and the original P. Franklin 1934 reference.
5. *All seventy minimum feedback-vertex sets of the Heawood graph*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-all-seventy-minimum-feedback-vertex-sets-of-the-heawood-graph--83a003d33b54.

