# A unique twelve-vertex cubic bipartite network with two excitation-period halving channels

## Finding

The smallest connected simple cubic bipartite graph supporting **both** a period-eight-to-four and a period-ten-to-five discrepancy between the three-color cyclic cellular automaton (CCA) and the three-state Greenberg–Hastings model (GHM), started at the *same* initial coloring, has twelve vertices. There is **exactly one such graph up to graph isomorphism** at this minimum order.

For an explicit representative \(G_*\), precisely \(1{,}208\) of its \(3^{12}=531{,}441\) labeled initial colorings have eventual least periods \((p_C,p_H)=(8,4)\), and precisely \(4{,}784\) have \((p_C,p_H)=(10,5)\). Thus \(5{,}992\) colorings exhibit a period discrepancy, and **every remaining coloring has equal eventual least periods**. The two discrepancies both halve the cyclic period, but arise on disjoint sets of initial states.

An exact census of every connected cubic bipartite graph with at most twelve vertices gives the following numbers of initial colorings of each discrepancy type. Graphs are encoded by standard graph6 strings, which are machine identifiers, not graph-theoretic variables.

| Order | graph6 representative | \((8,4)\) | \((10,5)\) | Any other period discrepancy |
| ---: | --- | ---: | ---: | ---: |
| 6 | `EFz_` | 0 | 0 | 0 |
| 8 | `G?zTb_` | 0 | 0 | 0 |
| 10 | `I?BeeOwM?` | 0 | 0 | 0 |
| 10 | `I?BedPWM?` | 0 | 480 | 0 |
| 12 | `K??FFBOJ?wB_` | 176 | 0 | 0 |
| 12 | `K??FEbGL@WB_` | 0 | 0 | 0 |
| 12 | `K??FEagT@WB_` | 0 | 0 | 0 |
| 12 | `K??FEQoT@WB_` | **1,208** | **4,784** | 0 |
| 12 | `K??EUIo[@WB_` | 0 | 9,408 | 0 |

Every entry is a complete finite-state count, not a sample. The full joint-period distributions, including the equal-period classes, are recorded and reproducible in the accompanying verification data. The theorem concerns simultaneous presence of these **two specified** strict-divisibility channels, not a minimum for every conceivable kind of CCA/GHM period disagreement.

## Assumptions and scope

Let \(G=(V,E)\) be a connected finite simple undirected graph, cubic (every degree is three) and bipartite. A configuration is \(x\in\{0,1,2\}^V\), and vertices update simultaneously by the following deterministic rules.

For CCA, a vertex of color \(c\) changes to \(c+1\pmod3\) if a neighbor currently has that successor color; otherwise it retains \(c\). For GHM, excited color one changes to refractory color two, refractory color two changes to resting color zero, and resting color zero changes to color one if and only if a neighbor currently has color one. Both evolutions begin from the same \(x\); there are no thresholds above one or random updates. Write \(p_C(x)\) and \(p_H(x)\) for the least periods of their eventual temporal cycles. For a finite deterministic map this is well-defined after a finite transient, regardless of the transient's length.

The distinguished representative \(G_*\) has vertices \(0,\ldots,11\), with shores \(L=\{0,\ldots,5\}\) and \(R=\{6,\ldots,11\}\). Its six adjacency rows are, in ascending order of the left endpoint and using right-shore indices \(0,\ldots,5\),

```
{0,1,2}, {0,1,3}, {0,2,4},
{2,3,5}, {1,4,5}, {3,4,5}.
```

Thus, for example, left vertex zero is joined to right vertices six, seven and eight. Every left and right vertex has exactly three neighbors, and the graph is connected. The same graph in standard graph6 notation is `K??FEQoT@WB_`. All assertions count individually labeled colorings, not configurations modulo spatial symmetries or cyclic rotation of time.

## Proof

**Exhaustiveness of the small-graph catalog.** In a cubic bipartite graph, the two vertex classes have equal cardinality \(m\), since each class meets exactly \(3m\) edges. Simplicity requires \(m\ge3\). To classify orders at most twelve, it therefore suffices to consider \(m=3,4,5,6\). For each \(m\), every candidate bipartite adjacency matrix has exactly three ones in each row and column. Permuting the left class permits the rows to be ordered as a nondecreasing multiset of three-subsets of the right class. `verification/enumerate_bip.py` generates **all** such multisets, rejects matrices violating a column sum of three or connectivity, and uses an exact canonical form under arbitrary permutations of the right class, sorting the left rows, and swapping shores. In a connected bipartite graph the bipartition is unique up to such a swap; consequently equality of these canonical forms is equivalent to graph isomorphism. This gives respectively \(1,1,2,5\) isomorphism classes at orders \(6,8,10,12\), with the exact graph6 representatives listed in the table. No graph type is omitted by the enumeration.

**Exact finite-state classifier.** For a fixed representative on \(n\) vertices, encode every coloring as \(s=\sum_{v=0}^{n-1}x_v3^v\), an integer from zero through \(3^n-1\). Construct, for both update rules, the complete successor array on this integer interval. In a finite functional digraph, iteratively removing indegree-zero vertices removes precisely the nonperiodic points. Traversing each surviving directed cycle gives its exact least period. Reversing the removal order gives every eliminated point its successor's eventual least period. This argument handles *all* input states without a trajectory-length cutoff. `verification/verify_peel.cpp` implements this algorithm for all nine graph6 representatives and records the complete joint \((p_C,p_H)\) table for each.

**Independent classification.** `verification/verify_paths.cpp` constructs those same nine graphs from independent explicit biadjacency row masks rather than decoding graph6. Its classification algorithm follows each previously unclassified forward path until it reaches a known point or first repeats a point on its current path. A first repetition identifies an entire genuine directed cycle and its length; backward propagation assigns periods to incoming paths. This also classifies every state exactly once without assuming a bound on its period. The two independent programs produce byte-identical nine-graph tables, stored as `verification/verify_peel.out` and `verification/verify_paths.out`. The graph catalog is regenerated by the standalone enumeration script, rather than trusted from those tables.

**Sharpness and uniqueness.** In the nine complete joint tables, no graph with fewer than twelve vertices has both a positive \((8,4)\) count and a positive \((10,5)\) count. Among the five twelve-vertex types, exactly the row identified by `K??FEQoT@WB_` has both. Its joint-table entries are exactly \(1{,}208\) and \(4{,}784\), and no other unequal period pair occurs in that row. This proves the sharp minimum, uniqueness, the two populations and the absence of other period disagreements.

For concrete independent trajectory witnesses, the initial coloring with integer code `11002` has CCA preperiod one and period eight, versus GHM preperiod two and period four. Code `2939` is already CCA period ten and reaches a GHM period-five orbit after two updates. Both are verified by the separate direct stepper in `verification/witness.py`. Individual witnesses establish existence; the exact multiplicities and uniqueness require the complete enumerations above.

## Verification

All complete source files and expected integer outputs are included. Run `python3 verification/replay.py` from the package root using the Python 3 standard library and a C++17 compiler (`g++`). This checks the nine-graph isomorphism catalog, recompiles both functional-graph enumerators, compares their full recorded outputs byte-for-byte, checks the specified unique joint channels, and directly replays the two witnesses. No external database, other finding, hidden path, random sample, proprietary data or binary artifact is required for reproduction. Each program tests the entire finite state space for each of the nine graphs. The replay completed successfully with all checks passing.

The full output files also record each model's sharp maximum entry depth for each graph, but the novelty asserted here is the **minimal simultaneous presence and exact joint populations** of the two specified period-halving channels.

## Relationship to prior work

Durrett and Griffeath introduced and investigated the CCA and GHM models, originally on lattice settings. Gravner, Lyu and Sivakoff developed their general finite- and infinite-graph comparison framework, proving synchronization and long-run activity results. Those qualitative results do not tabulate exact joint least-period pairs for the small cubic bipartite graph census.

A separate all-graph result proves that, from matching initial colors, the eventual GHM period always divides the CCA period. The divisibility direction of the two channels is therefore **not** asserted as new. A previously available exact census on the Heawood graph shows both \((8,4)\) and \((10,5)\) discrepancies at order fourteen, but does not establish the sharp minimum or the unique twelve-vertex witness. Earlier exact comparisons on the Petersen, Frucht, and related graphs similarly cover different graph types or a single channel. A prior published count of the five connected cubic bipartite types at order twelve, in a study of majority dynamics and other graph properties, does not determine their CCA/GHM joint periods. The present contribution combines a complete small-graph isomorphism census with exact **paired** temporal classification to resolve the smallest-order and uniqueness questions.

## Limitations

This is a sharp theorem within the class of **connected simple cubic bipartite graphs** only. It does not claim the same minimum among arbitrary graphs or nonbipartite cubic graphs, nor a structural criterion for two-channel coexistence at every larger order. Counts are exact finite classifications, not an infinite-graph theorem. The originality comparison covers indexed records and materially inspected relevant primary work but cannot exclude an unindexed earlier equivalent classification. Independent external mathematical validation has not been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002v1, first submitted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 .
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1, first submitted 2016-10-24; *Annals of Applied Probability* 28 (2018), 3324–3357, https://arxiv.org/abs/1610.07320 .
3. *Exact excitation-clock reconstruction and period divisibility for three-color graph automata*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-excitation-clock-reconstruction-and-period-divisibility-fo--6edafe27dc02 .
4. *Two period-halving channels in Heawood cyclic and refractory excitation*, published exact finite-state result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-period-halving-channels-in-heawood-cyclic-and-refractory-exc--e74f89b4b1a2 .
5. *A 1,496-state period split between cyclic and excitable dynamics on the Frucht graph*, published exact finite-state result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-1-496-state-period-split-between-cyclic-and-excitable-dynamics--09b39afb00c7 .
6. *Petersen-specific period doubling between cyclic and refractory excitation dynamics*, published exact finite-state result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-petersen-specific-period-doubling-between-cyclic-and-refractory--85df9829d668 .
