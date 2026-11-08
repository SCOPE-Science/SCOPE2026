# Complete edge-metric basis mobility of the Chvátal graph

## Finding
Let \(G\) be the twelve-vertex, four-regular, triangle-free, four-chromatic Chvátal graph, with its 24 undirected edges specified in the verification programs. For \(e=uv\), define the vertex-to-edge distance \(d(w,e)=\min\{d(w,u),d(w,v)\}\). An *edge-metric basis* is a minimum set of vertex landmarks whose vectors of vertex-to-edge distances distinguish all edges of \(G\).

**Theorem.** The edge metric dimension of \(G\) is \(5\), and exactly \(192\) five-vertex sets are bases. Define the *jump graph* by joining two bases when one landmark is replaced by any unselected vertex, and the *slide graph* by requiring the replacement to be adjacent to the removed landmark in \(G\). Both networks are connected. The jump graph has \(1152\) undirected edges and every one of its \(192\) vertices has eccentricity \(5\): its radius and diameter are both \(5\). The slide graph has \(428\) edges, radius \(6\), diameter \(7\), and eccentricity distribution \(6:120,\ 7:72\).

The slide network has no isolated vertices. Its complete degree distribution is \(2:28,\ 3:32,\ 4:48,\ 5:32,\ 6:32,\ 7:8,\ 8:8,\ 10:4\). Thus adjacency-constrained relocation preserves reachability between **every** pair of optimal edge-sensing configurations on this canonical chromatic obstruction graph, but requires as many as two additional replacements compared with unrestricted jumping.

## Assumptions and scope
The Chvátal graph is defined by the labeled edge list in `artifacts/verify_masks.py`, independently represented as an upper-triangular adjacency dictionary in `artifacts/verify_signatures.py`. Both use vertices \(\{0,\ldots,11\}\), no loops or multiple edges. The graph has degree four at every vertex and has 24 edges. Moves change exactly one of the five distinct selected vertices. A slide must use an **edge of the original graph**, not an edge of the jump or line graph. Edge-metric resolution distinguishes 24 graph edges, not 12 graph vertices. Claims concern this specific finite graph, not every four-regular graph.

## Proof
This is an exhaustive finite proof using two separately written integer programs. The graph's 12-vertex edge list is explicit and requires no graph-library dependency. Graph adjacency and all vertex-to-edge distances are computed from scratch.

First, the bitmask implementation calculates the 276 unordered pairs among the 24 graph edges. A landmark \(v\) distinguishes an edge pair precisely when its two edge distances differ; the program encodes the resulting distinctions in a 276-bit integer \(M_v\). A set \(B\) is edge resolving if and only if \(\bigvee_{v\in B}M_v\) has all 276 bits set. Exhaustively testing all \(\sum_{k=0}^5\binom{12}{k}=1586\) subsets yields no resolving set of cardinality below five and exactly 192 of cardinality five. The independent program directly calculates the 24 edge-distance signatures for every four- and five-landmark subset; it reaches the same result without mask operations.

Second, one program constructs the reconfiguration edges by removing each of five chosen landmarks and trying each of seven unselected vertices against the complete basis lookup. It keeps a move as a slide exactly when removed and inserted vertices are adjacent in the original graph. The second program instead examines each unordered pair of the 192 bases, checks whether their intersection has cardinality four, and then checks graph adjacency of the unique swapped pair. Both procedures exactly exhaust all possibilities, giving 1152 jump links and 428 slide links and the same slide degree distribution.

Third, both implementations run an exact breadth-first search from **every** basis of each network. Every search reaches all 192 bases. The jump eccentricity of all 192 bases is 5, while 120 slide bases have eccentricity 6 and the other 72 have eccentricity 7. These values prove the asserted connectivity, radius and diameter and show that no optimal edge-metric configuration is frozen under adjacent slides.

Every state and transition is either enumerated or excluded by an exact finite predicate, so this is a complete finite proof. No finite-to-infinite extrapolation or probabilistic experiment is involved.

## Verification
From the directory containing this file run `python3 artifacts/verify_masks.py` and `python3 artifacts/verify_signatures.py`. Both use only the Python 3 standard library and have no file or network input. Each prints `PASS` after asserting the graph size, lower bounds, basis count, link counts, degree distribution, connectivity and graph distances. Their captured outputs are `artifacts/masks_output.txt` and `artifacts/signatures_output.txt`.

## Relationship to prior work
Chvátal introduced his small triangle-free four-chromatic four-regular graph in 1970, and Kelenc, Tratnik and Yero defined the edge-metric dimension in their publicly posted January 31, 2016 paper. Neither source gives the minimum **edge-resolving** configurations or their constrained-mobility graph. Previous investigations of proper-coloring reconfiguration on the same Chvátal graph concern entirely different state spaces, and results for edge-metric bases of crown, half and complete multipartite graphs do not cover the Chvátal graph. Similarly, ordinary vertex-metric bases use distances between graph vertices, not edges. No covering prior statement or equivalent exact network census was identified in the inspected literature and mathematical-result searches. These searches cannot prove historical uniqueness.

## Limitations
The result is a complete finite invariant for one graph; it does not assert a general connection between chromatic number and mobility of edge-metric bases. It rests on reproducible exhaustive programs rather than a shorter closed-form structural characterization. Independently authored scholarly validation has not been carried out. Unindexed previous calculations or databases may contain equivalent numerical results.

## References
1. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, J. Combinatorial Theory 9 (1970), 93–94, DOI:10.1016/S0021-9800(70)80057-6.
2. A. Kelenc, N. Tratnik, and I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291v1 (2016-01-31), https://arxiv.org/abs/1602.00291 .
3. E. W. Weisstein, *Chvátal Graph*, MathWorld, https://mathworld.wolfram.com/ChvatalGraph.html .
