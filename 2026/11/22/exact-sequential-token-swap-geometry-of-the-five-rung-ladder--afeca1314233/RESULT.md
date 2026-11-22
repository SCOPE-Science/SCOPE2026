# Exact sequential token-swap geometry of the five-rung ladder

## Finding

For the ten-vertex ladder \(G=P_2\square P_5\), let \(\mathcal T(G)\) be the graph of placements of ten distinct tokens, with an edge for each single swap along an edge of \(G\). The graph \(\mathcal T(G)\) has \(10!=3{,}628{,}800\) vertices, is connected and vertex-transitive, has degree \(13\), and has **radius and diameter exactly \(21\)**. Exactly four configurations lie at distance \(21\) from each configuration, yielding \(7{,}257{,}600\) unordered diametral pairs.

For any two placements \(\pi,\sigma\), put
\[
B(\pi,\sigma)=\frac12\sum_{t=0}^9d_G\bigl(\pi^{-1}(t),\sigma^{-1}(t)\bigr),\qquad
\Delta(\pi,\sigma)=d_{\mathcal T(G)}(\pi,\sigma)-B(\pi,\sigma).
\]
The maximum displacement-bound shortfall is exactly \(8\). For every \(\pi\), exactly one \(\sigma\) has \(\Delta(\pi,\sigma)=8\), namely \(\sigma=\pi\circ R\), where \(R\) reverses the order of the five sites in **each** rail separately. These partners form exactly \(1{,}814{,}400\) unordered pairs. Their token-swap distance is \(20\), not the diameter \(21\).

The complete distance-shell counts from any placement, for distances \(0,1,\ldots,21\), are
\[
(1,13,100,552,2396,8476,25029,62341,132095,239871,376349,
509721,594050,589996,491625,333203,175340,67892,17247,2331,168,4).
\]

## Assumptions and scope

This is an **exact finite classification for \(P_2\square P_5\) only**, not an all-length formula for ladders. Label its vertices \(0,\ldots,9\) with top rail \(0,1,2,3,4\), lower rail \(5,6,7,8,9\), horizontal edges within each rail, and rungs \(\{i,i+5\}\) for \(0\le i\le4\). A placement \(\pi\) is a bijection from vertex positions to token labels. Swaps are sequential, not simultaneous. Distances count individual adjacent-edge swaps.

The identity placement \(\mathrm{id}=(0,1,2,3,4,5,6,7,8,9)\) places token \(i\) at site \(i\). Its four distance-\(21\) placements, in row-major position-to-token notation, are
\[
\begin{aligned}
&(4,8,7,6,0,9,3,2,1,5),\\
&(9,8,7,5,6,3,4,2,1,0),\\
&(9,8,7,6,5,4,3,2,1,0),\\
&(8,9,7,6,5,4,3,2,0,1).
\end{aligned}
\]
The unique placement attaining shortfall \(8\) from identity is
\[
R=(4,3,2,1,0,9,8,7,6,5).
\]

## Proof

**1. Configuration-state metric.** Every legal swap is the transposition of the two position entries corresponding to one of the thirteen edges of \(G\). Since \(G\) is connected, its edge transpositions generate all permutations of ten tokens. Relabelling all tokens by the same permutation acts transitively on configurations and preserves legal swaps. Consequently, all distance shells and all eccentricities equal those from identity; in particular \(\operatorname{rad}(\mathcal T(G))=\operatorname{diam}(\mathcal T(G))\).

**2. Exhaustive breadth-first certificate for the metric.** The included `verification/lehmer_bfs.cpp` uses an explicit Lehmer bijection between permutations and ranks \(0,\ldots,10!-1\), generates exactly the thirteen legal successors of every dequeued configuration, and assigns an unvisited successor the current distance plus one. Its queue is FIFO and has the identity as its only initial element. Standard BFS induction shows that the assigned integer equals the true shortest-swap distance, not merely the length of a found path. An explicit round-trip assertion checks rank/unrank on every possible rank. The traversal reaches **all** \(3{,}628{,}800\) ranks and reports the full shell vector above, with its last nonzero shell at \(21\), of size four. The four rank-decoded representatives are printed explicitly above; therefore no hidden states can be farther. A second implementation, `verification/packed_bfs.cpp`, uses packed four-bit token encoding and a hash-based visited set instead of Lehmer ranks and an indexed distance array. It independently reproduces the entire distance vector and four extremal placements. This is a finite exhaustive proof whose complete enumeration can be replayed, not a sample of paths.

**3. Displacement lower bound.** For every placement pair, each swap changes the sum of token-to-destination graph distances by at most two. Thus the minimum swap count is at least \(B\). The ladder is bipartite. The parity of each token's distance equals the parity change of its endpoint bipartition, so the sum across all ten tokens is even and \(B\) is always an integer. To evaluate the bound from identity to any permutation \(p\), the graph distance between vertex labels \(i,j\) is the Manhattan distance
\[
d_G(i,j)=|i\bmod5-j\bmod5|+\mathbf1_{\lfloor i/5\rfloor\ne\lfloor j/5\rfloor}.
\]
For each of the \(10!\) permutations, each independent verifier computes \(d_{\mathcal T(G)}(\mathrm{id},p)-\tfrac12\sum_i d_G(i,p(i))\) and tallies it. The shortfall counts for values \(0,1,\ldots,8\) are exactly
\[
(424974,1197510,1259762,598260,132969,14518,790,16,1).
\]
Their sum is \(3{,}628{,}800\). The only value-eight placement is \(R\), for which the graph-distance sum is \(24\), the lower bound is \(12\), and the true distance is \(20\).

**4. All-pair conclusions.** Given source \(\pi\), relabelling tokens by \(\pi^{-1}\) sends its placement to identity and sends target \(\sigma\) to \(\pi^{-1}\circ\sigma\). This preserves graph distance, token displacement, and hence shortfall. It follows that the unique shortfall-eight target of \(\pi\) is \(\pi\circ R\). As \(R\ne\mathrm{id}\) and \(R^2=\mathrm{id}\), these targets partition all placements into \(10!/2=1{,}814{,}400\) unordered pairs. Similarly, the four antipodes per state give \(10!\cdot4/2=7{,}257{,}600\) unordered diameter pairs.

## Verification

All required sources and data are local to this package. From its root, with a C++17 compiler and Python 3 installed, execute:

```sh
python3 verification/check.py
```

The checker compiles and independently runs both exhaustive implementations, compares the complete shell vectors, the four antipode permutations, the entire displacement-shortfall histogram and its unique maximizer, and checks smaller ladders as calibrations. The checked \(2\times5\) enumeration covers every one of the \(10!\) configurations. The manifest `verification/expected.json` contains the exact finite data.

## Relationship to prior work

The legal-swap model and its permutation-Cayley formulation are standard; neither is claimed as new. Aichholzer et al. [1] examine the complexity of sequential and parallel token swapping on trees, not this cyclic ladder. Bonnet, Miltzow and Rzążewski [2] give general algorithms and the half-sum-distance lower bound, but not this finite exact ladder metric. Sadanandan and Chitturi [3] solve certain transposition-tree sorting problems, a graph class that does not include the ladder. Bansal, Günlük and Shapley [4] study **parallel** token swapping on ladder grids and obtain an approximation bound in number of synchronous rounds; their bound cannot determine the minimum **total number of individual swaps** or the exact shortfall distribution here. Published indexed findings on token swapping of the Petersen graph concern a different underlying edge-generator set and do not imply this ladder result. The present claim is the specific complete metric, four-antipode census and unique sharp displacement deficit on the ten-site ladder.

## Limitations

This is one finite graph, not a general formula for all \(P_2\square P_n\), nor an asymptotic result. The proof relies on exhaustive finite computation plus verifiable BFS correctness, not an illuminating non-computational closed-form derivation of the numbers. Reproduction requires C++17 and Python 3. Historical novelty cannot be established merely from the absence of a matching indexed source; an unindexed exact computation or different Cayley-network terminology could predate this classification. The parallel-swap round metric is outside scope. Independent external validation has not been performed.

## References

1. O. Aichholzer, E. D. Demaine, M. Korman, J. Lynch, A. Lubiw, Z. Masárová, M. Rudoy, V. Vassilevska Williams, and N. Wein, *Hardness of Token Swapping on Trees*, arXiv:2103.06707, first submitted 2021-03-11, https://arxiv.org/abs/2103.06707.
2. É. Bonnet, T. Miltzow and P. Rzążewski, *Complexity of Token Swapping and Its Variants*, *Algorithmica* (online 2017), https://doi.org/10.1007/s00453-017-0387-0.
3. I. T. Sadanandan and B. Chitturi, *Optimal Algorithms for Sorting Permutations with Brooms*, *Algorithms* 15 (2022), 220, https://doi.org/10.3390/a15070220.
4. I. Bansal, O. Günlük and R. Shapley, *Parallel Token Swapping for Qubit Routing*, arXiv:2411.18581, first submitted 2024-11-27, https://arxiv.org/abs/2411.18581.
