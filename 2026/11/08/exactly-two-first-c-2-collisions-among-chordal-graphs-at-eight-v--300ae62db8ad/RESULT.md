# Exactly two first \(C^2\)-collisions among chordal graphs at eight vertices

## Finding
Let \(\mathcal C_n\) be the isomorphism classes of finite simple undirected chordal graphs on \(n\) vertices; here chordal means no induced cycle of length at least four. Let \(G\equiv_{C^2}H\) mean that two graphs satisfy the same sentences of unrestricted two-variable first-order logic with counting quantifiers, equivalently that simultaneous ordinary color refinement does not distinguish them.

**Theorem.** For every \(1\le n\le7\), \(G,H\in\mathcal C_n\) and \(G\equiv_{C^2}H\) imply \(G\cong H\). The set \(\mathcal C_8\) consists of exactly \(2119\) isomorphism classes, which form exactly \(2117\) classes under \(\equiv_{C^2}\). Precisely two equivalence classes contain two distinct graph isomorphism classes, and each of the other \(2115\) equivalence classes is a singleton. All four exceptional graphs are connected. One exceptional pair has \(13\) edges and consists of two \(2\)-trees; the second has \(14\) edges and consists of two split graphs.

Exact graph6 encodings of representatives are:

| Type | First graph | Second graph | Edges | Coarsest degree-quotient |
| --- | --- | --- | ---: | --- |
| \(2\)-tree pair | `G}pOgg` | `G}TdC_` | 13 | `((0,1,1),(2,0,2),(2,2,1))` |
| Split-graph pair | ``G}r`HG`` | `G}VSGg` | 14 | `((0,2),(2,3))` |

Here quotient rows and columns are ordered by increasing degree. Each paired quotient is equitable, explaining the two collisions; nonisomorphism follows from exact adjacency-preserving backtracking in the verifier.

## Assumptions and scope
All graphs are finite simple undirected graphs, with no vertex colors, loops, or parallel edges. Disconnected chordal graphs are included. An isomorphism class is counted once, irrespective of labeled presentations. Comparison is *class-relative*: both graphs in a compared pair are chordal. No statement is made about distinguishing a chordal graph from an arbitrary nonchordal graph.

## Proof
**1. Exhaustive connected generation.** Every nontrivial connected chordal graph has a simplicial vertex, a vertex whose neighborhood is a nonempty clique. Removing such a vertex leaves a connected chordal graph: any paths passing through the removed vertex can be shortcut through its mutually adjacent neighbors. Conversely, adjoining a vertex with neighborhood a nonempty clique preserves both connectedness and chordality. Thus, inductively, all connected chordal graphs on \(n\) vertices arise by adjoining a clique-neighbor vertex to some connected chordal graph on \(n-1\) vertices. The algorithm starts from the unique one-vertex graph, visits every nonempty clique, and removes duplicate labeled presentations with an **exact** graph-isomorphism backtracker. The backtracker uses degrees and neighbor-degree multisets only to prune candidates; it then checks all adjacencies under a complete bijection, so neither a heuristic hash nor the pruning decides nonisomorphism.

**2. Exhaustive disconnected generation.** Every chordal graph decomposes uniquely into a multiset of connected chordal components. Enumerating nondecreasing lists of component isomorphism-type indices with total order \(n\) gives every disconnected isomorphism class exactly once. The verifier constructs and counts these lists explicitly. Connected totals for \(n=1,\ldots,8\) are \(1,1,2,5,15,58,272,1614\); all-chordal totals are \(1,2,4,10,27,94,393,2119\). These totals independently agree with Brendan McKay's connected-chordal catalogue and OEIS A048193, respectively. The totals support, but do not replace, the preceding generation-and-deduplication completeness argument.

**3. Exact logical-equivalence test.** All graphs of a fixed order are refined using a **shared** palette. Initially all vertices have one color. In every round the new color is assigned to the pair consisting of the old color and the multiset of neighbor colors; the global collection of signatures receives distinct canonical integer names. Each graph's multiset of colors is recorded. Color refinement is exactly the equivalence relation of \(C^2\) on finite uncolored graphs (Immerman–Lander correspondence). It is enough to compare \(2n\) rounds: color refinement on the disjoint union of a pair of graphs of order \(n\) stabilizes by then. The verifier actually computes 18 rounds for all orders through eight. Different color multisets imply different \(C^2\)-theories, while identical stabilized multisets imply the same \(C^2\)-theory.

**4. Census and exceptions.** The standalone program `verify.py` carries out the finite, exhaustive loops in steps 1–3. For orders one through seven no color-signature class has size greater than one. At order eight there are \(2117\) classes among \(2119\) nonisomorphic chordal graphs; precisely two have size two. Both are connected. Exact adjacency testing confirms nonisomorphism within each pair and verifies the four graph6 encodings. For the \(13\)-edge pair, a recursive degree-two simplicial deletion reduces each graph to a triangle, proving that both are \(2\)-trees. For the \(14\)-edge pair, a direct search finds a clique–independent-set partition, establishing that both are split graphs. Degree-quotient checks separately confirm each pair's indistinguishability by refinement. This proves all parts of the theorem.

## Verification
Run `python3 verify.py` using only the Python 3 standard library. It prints a complete one-through-eight census and ends with `VERIFY_OK`. The recorded deterministic output is in `verification_output.txt`; independent small-order confirmation using NetworkX's graph atlas reproduced the chordal totals through seven vertices. The verifier asserts the connected counts, all-graph counts, exact nonisomorphism of four witnesses, size of every logical-equivalence class, edge totals, graph-family memberships, graph6 representations, and the equitable degree-quotients. Counts for order eight are finite exhaustive results, **not** an extrapolation.

## Relationship to prior work
The 2015 works of Arvind, Köbler, Rattan, and Verbitsky and of Kiefer, Schweitzer, and Selman establish foundational color-refinement and \(C^2\) identification theory. Their general classifications do not report this exact chordal order-eight census. Earlier explicit results separately identify the \(13\)-edge \(2\)-tree pair and the \(14\)-edge split-graph pair. Those examples establish existence but do **not** establish that these are the only collisions across **all** chordal graphs on eight vertices, nor that none occur on smaller orders. The present contribution is that complete first-obstruction layer. In the standard chordal terminology, \(2\)-trees and split graphs are subclasses of chordal graphs, but neither subclass exhausts all chordal graphs. McKay's catalogue and OEIS A048193 supply independent reference counts, not logical-equivalence classifications.

## Limitations
This proves a sharp **finite** first-collision result only; it does not determine \(C^2\)-equivalence classes of chordal graphs on nine or more vertices. It establishes relative identification within chordal graphs, not global \(C^2\)-identification among all graphs. Historical-priority searches are bounded; hidden or unindexed classifications may exist. The verification is not an independent mathematical audit.

## References
1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness* (first public arXiv:1502.01255, 2015-02-04), https://arxiv.org/abs/1502.01255.
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting* (arXiv:1503.08792, 2015), https://arxiv.org/abs/1503.08792.
3. B. McKay, *Combinatorial Data: Chordal graphs* (catalogue of nonisomorphic connected chordal graphs), https://users.cecs.anu.edu.au/~bdm/data/graphs.html.
4. OEIS A048193, *Number of chordal graphs (or triangulated graphs) on n vertices*, https://oeis.org/A048193.
5. *Graphclasses.org*, chordal perfect-elimination-order characterization, https://graphclasses.org/classes/gc_32.html.
