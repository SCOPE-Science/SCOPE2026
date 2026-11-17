# A 1,496-state period split between cyclic and excitable dynamics on the Frucht graph

## Finding

On the canonical 12-vertex Frucht graph, start both the three-color cyclic cellular automaton (CCA) and the three-state Greenberg–Hastings model (GHM) at **the same** labeled coloring. For an initial configuration \(x\), write \(p_C(x)\) and \(p_H(x)\) for the eventual least temporal periods of the CCA and GHM trajectories. For the standard synchronous, threshold-one rules specified below, the **complete exact joint-period table** is

| \((p_C,p_H)\) | Number of initial colorings |
| ---: | ---: |
| \((1,1)\) | 52,563 |
| \((3,3)\) | 282,990 |
| \((4,4)\) | 62,952 |
| \((5,5)\) | 90,432 |
| \((6,6)\) | 24,636 |
| \((7,7)\) | 12,840 |
| \((8,8)\) | 3,532 |
| \((8,4)\) | **1,496** |

There are no other joint-period classes. Thus **exactly 1,496 of the \(3^{12}=531441\) labeled starting configurations have different eventual least periods** in the two dynamics. Every discrepancy consists of a primitive period-eight CCA outcome versus a primitive period-four GHM outcome. In particular, pointwise period equality known on complete bipartite graphs does not extend to all connected cubic graphs. This split occurs **despite the complete absence of nontrivial spatial symmetries**: the Frucht graph is one of the smallest asymmetric cubic graphs. Earlier Petersen-graph data already exhibited the same eight-versus-four period type on a highly symmetric cubic graph; the novelty here is the exact asymmetric-graph counterexample and its complete joint census, not discovery of the first such period type. Both dynamics have possible eventual periods exactly \(\{1,3,4,5,6,7,8\}\), but their period-four and period-eight attracting populations differ.

The CCA has respectively \(3,1912,66,60,20,84,36\) primitive orbits of periods \(1,3,4,5,6,7,8\); the GHM has respectively \(1,1912,22,10,2,28,4\). Every state is eventually periodic. The sharp maximum first-periodic-entry times are \(19\) (CCA, attained by nine states) and \(21\) (GHM, attained by three states).

## Assumptions and scope

The graph is the simple undirected Frucht graph on vertices \(V=\{0,\ldots,11\}\), with the following **complete** edge list, taken in the listed labeling:

```
(0,1) (0,6) (0,7) (1,2) (1,7) (2,3)
(2,8) (3,4) (3,9) (4,5) (4,9) (5,6)
(5,10) (6,10) (7,11) (8,9) (8,11) (10,11)
```

An independent graph construction uses the 12-cycle and LCF offsets `(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)`. The vertex permutation from LCF to this edge-list labeling is `(4,3,2,1,7,0,6,5,10,11,8,9)`; its 18 induced edges agree exactly with those listed above. The graph has twelve vertices, eighteen edges, degree three everywhere, and no nontrivial graph automorphism.

Color \(0\) means resting, \(1\) excited, \(2\) refractory for GHM; in CCA the same values are cyclic colors. For each vertex \(v\) with current color \(c\), **CCA** replaces \(c\) by \(c+1\pmod3\) if and only if at least one neighbor currently has that successor color; otherwise \(c\) stays. **GHM** sends \(1\mapsto2\), \(2\mapsto0\), and sends \(0\mapsto1\) if and only if at least one neighbor is currently color \(1\), retaining \(0\) otherwise. All vertices update simultaneously. The contact threshold is one, with no stochasticity or externally forced sites.

A state already on a temporal orbit has first-periodic-entry time zero. For any initial state \(x\), its eventual least period is the least positive integer \(p\) such that \(F^{t+p}(x)=F^t(x)\) for all sufficiently large integers \(t\); finite determinism guarantees existence. States are counted with individually labeled vertices, not modulo symmetry or cyclic color changes.

For reproducibility encode \(x=(c_0,\ldots,c_{11})\) as the integer \(s=\sum_{i=0}^{11}c_i3^i\). This is a bijection between configurations and the integers from 0 to 531440, inclusive. One explicit mismatch witness is code `4234`: CCA follows the eight distinct states `4234, 199214, 286560, 427458, 121345, 203258, 439785, 171624`, then returns to `4234`; GHM follows `4234, 201401, 459333, 132213, 4219, 201395, 459333`, reaching the period-four orbit at step two. This witness alone proves that pointwise equality fails; the full table requires the exhaustive certificate below.

## Proof

For each of the \(3^{12}\) base-three state codes, construct its successor under both local rules by (a) decoding the twelve trits, (b) reading the three neighbors at each vertex in the fixed graph, (c) applying the specified simultaneous rule, and (d) encoding the resulting twelve trits. Both programs include this procedure explicitly and examine the entire input interval, rather than sample states.

Each successor map is a function on a finite set. In its functional digraph every weak component has exactly one directed cycle. In `verify_indegree_peel.cpp`, the indegree-zero vertices are iteratively removed; the unremoved vertices are exactly the periodic vertices. A complete traversal around every remaining directed cycle determines its **primitive** temporal period. Reverse traversal through the removed vertices labels every remaining state with its successor's primitive period and assigns first-entry time one plus that of the successor. This is exact because the reverse-removal order puts each successor before its removed predecessor. The code asserts that all 531441 states are classified for each rule.

The independent `verify_memory_walk.cpp` builds the graph from its LCF offsets rather than the listed edges. For every previously unclassified state it follows successive states until encountering the active path or a classified state; a repeated active state closes one exact cycle, with the remaining path states assigned predecessor depths. The procedure marks each state once, so it also classifies all 531441 states, including every transient, without truncating trajectories. It counts the joint least-period pair for each corresponding **common initial coloring**. The graph permutation makes the two labelings conjugate; the multiset of paired least periods is invariant under that simultaneous relabeling.

The two complete enumerations yield independently the same eight joint-period multiplicities, whose sum is exactly \(531441\). No omitted input codes or possible period pairs remain. Every counted period is an actual directed cycle length, not a return observed before an arbitrary timeout. The orbit and entrance-time claims follow from the same exhaustive digraph decomposition. The displayed witness can also be checked by eight and six direct rule applications.

## Verification

With any C++17 compiler, in the directory of the two included source files run:

```
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_memory_walk.cpp -o memory_walk
./memory_walk

g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_indegree_peel.cpp -o indegree_peel
./indegree_peel
```

Outputs recorded in `memory_walk_output.txt` and `indegree_peel_output.txt` agree. The second program asserts the complete eight-class table, the separate orbit counts, the maxima and populations of first-entry times, and the exact graph isomorphism. The first uses a different graph representation and a different cycle-classification algorithm. No external libraries, datasets, hidden certificates, previous computations, or random sampling are required. Both proofs are finite and exact for this fixed twelve-vertex graph; they do not prove claims about arbitrary graphs or larger graph orders.

## Relationship to prior work

Durrett and Griffeath (1993) describe both excitable automaton families. Gravner, Lyu, and Sivakoff (2016), particularly the model definitions and their circulation-based synchronization and activity theorems, study these rules on arbitrary graphs. Their general theory does not tabulate the **joint eventual least-period pairs** on the Frucht graph; a synchronization criterion or an asymptotic activity rate does not determine a primitive temporal period.

A prior exact comparison of CCA and GHM on the **Petersen graph and pentagonal prism** had already established 4,800 period-eight/period-four discrepancies for the highly symmetric Petersen graph, but none for the prism. That record does not imply an analogous mismatch on a graph with trivial automorphism group; the present Frucht classification shows the phenomenon does not require spatial automorphisms. The eight-versus-four mismatch mechanism is therefore not claimed as newly discovered.

A previously available complete **GHM-only** Frucht graph classification, *A twenty-one-step excitation transient on the asymmetric Frucht graph*, counts GHM eventual periods and transient depth on the same graph. Those GHM counts and its 21-step maximum match exactly here and are not new. The additional data requiring independent analysis here are the CCA dynamics and their alignment on each common initial coloring. Another publicly available study, *Matched eventual periods but different transient clocks for three-state excitable dynamics on bicliques*, proves pointwise CCA/GHM period equality for all complete bipartite graphs; that family excludes the Frucht graph. The present exact table is therefore an asymmetric-graph boundary to generalizing biclique coincidence and a symmetry-free counterpart to the Petersen mismatch, not an assertion that the eight-versus-four split itself was previously unknown.

## Limitations

The conclusion is restricted to this graph and the stated synchronous threshold-one three-color dynamics. It does not imply that every asymmetric graph, cubic graph, or graph containing an odd cycle has such a discrepancy, nor does it establish a sharp minimum graph order for a discrepancy. Exact finite exhaustive computation establishes the counts but does not provide a uniform parameterized formula for other graphs. Relevant older literature and mathematical indexes cannot establish absolute priority; an unindexed earlier complete joint census remains possible. Independent external mathematical validation has not been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first public 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 .
2. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first public 2016-10-24, https://arxiv.org/abs/1610.07320 .
3. R. Frucht, *Herstellung von Graphen mit vorgegebener abstrakter Gruppe*, Compositio Mathematica 6 (1939), 239–250; historical graph construction. No day-precise publication date is asserted.
4. E. W. Weisstein, *Frucht Graph*, MathWorld, https://mathworld.wolfram.com/FruchtGraph.html .
5. *A twenty-one-step excitation transient on the asymmetric Frucht graph*, publicly available exact GHM census, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-twenty-one-step-excitation-transient-on-the-asymmetric-frucht--7b215d08f374 .
6. *Matched eventual periods but different transient clocks for three-state excitable dynamics on bicliques*, publicly available complete-bipartite result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-matched-eventual-periods-but-different-transient-clocks-for-thre--29320e9e89df .

7. *Petersen-specific period doubling between cyclic and refractory excitation dynamics*, earlier exact finite computation on the Petersen graph and pentagonal prism; full publication status not established. The scientific claim, not an external certificate, was compared for overlap.
