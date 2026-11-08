# Minimum global locating-dominating codes distinguish the Shrikhande and four-by-four rook graphs

## Finding

Let \(S\) be the Shrikhande graph with vertices \(\mathbb Z_4^2\), joining two vertices when their difference is one of \((\pm1,0),(0,\pm1),(1,1),(-1,-1)\) modulo four, and let \(R=K_4\square K_4\) be the four-by-four rook graph. Both have strongly regular parameters \((16,6,2,2)\). A *global locating-dominating code* \(C\) is a subset whose nonempty open-neighborhood traces \(N_G(v)\cap C\), for \(v\notin C\), are pairwise distinct, with the same condition holding in the complement of \(G\).

For both graphs, the location-domination number and global location-domination number are exactly five. Among their five-element locating-dominating codes, precisely 96 fail to be global, and those 96 are exactly the five-subsets of open neighborhoods. The complete minimum-code multiplicities differ:

| Exact statistic | Shrikhande \(S\) | Rook \(R\) |
|---|---:|---:|
| Locating-dominating five-sets | 1584 | 1968 |
| Non-global locating-dominating five-sets | 96 | 96 |
| Global locating-dominating five-sets | **1488** | **1872** |
| Automorphism-group order | 192 | 1152 |
| Automorphism orbits of global five-sets | 10 | 4 |
| Jump-exchange edges | 18432 | 27072 |
| Slide-exchange edges | 8160 | 11520 |

Under single-codeword token jumping (remove one codeword, add an arbitrary previously unselected vertex), both graphs of minimum global codes are connected, with radius and diameter five. Under token sliding (the replacement vertex must be adjacent to the removed one in the source graph), both are connected, with radius and diameter six. The automorphism orbit sizes are \(192\) six times, \(96\) three times and \(48\) once for \(S\), versus \(576\) three times and \(144\) once for \(R\).

Thus the common strongly regular parameters and adjacency spectrum do **not** determine the number of minimum global locating-dominating codes or their exchange edge counts.

## Assumptions and scope

All graphs are finite, simple and loopless. The rook graph uses vertices \((r,c)\) for \(r,c\in\{0,1,2,3\}\), with adjacency exactly when one coordinate is equal and the other differs. The Shrikhande connection differences are the six indicated elements of \(\mathbb Z_4^2\). A graph of minimum codes has a vertex for each five-element global code; edges represent one-element replacements that retain the five-element global-code property. Connectedness, radii and diameters refer to these finite exchange graphs, not to the original 16-vertex graphs. No infinite-family or uniqueness-across-all-graphs result is asserted.

## Proof

**Lemma (globality filter).** Let \(C\) locate-dominate \(G\). For \(v\notin C\), the complement-graph trace is \(C\setminus(N_G(v)\cap C)\). Complement traces are therefore automatically pairwise distinct. They are all nonempty if and only if no vertex outside \(C\) is adjacent to every vertex of \(C\). Hence \(C\) is global exactly when \(C\nsubseteq N_G(v)\) for all \(v\notin C\).

**Finite exact enumeration.** The complete elementary certificate is `verify_bitmask.py`; the independent set-based reconstruction is `verify_set_independent.py`. Both construct all 16 vertices, their 48 edges, and for each cardinality \(k\in\{0,1,2,3,4,5\}\) visit **every** \(k\)-subset. A subset passes the location-domination test precisely when all 16-minus-\(k\) exterior traces are nonempty and distinct, and passes the global test precisely when its traces also pass on the complement. Each implementation asserts that no smaller locating-dominating code exists, and the exact five-set counts are as stated. As \(\lambda_g\ge\lambda\), the existence of global five-sets establishes both minimum values.

For a 5-set, the globality filter fails precisely when it lies inside some 6-vertex open neighborhood, so it is that neighborhood with one vertex omitted. There are exactly \(16\binom65=96\) such sets and they are all distinct: otherwise one five-set would lie in two neighborhoods, while any two vertices of either \((16,6,2,2)\) graph have only two common neighbors. The explicit tests confirm all 96 are locating-dominating. This explains the identical 96-set obstruction across the two graphs without relying on a pattern extrapolated from samples.

The exchange checker enumerates all ordered pairs of a selected and unselected vertex for each feasible code, retains only exchanges leading to another code, and deduplicates unordered links. A separate connected-component checker establishes connectedness, and breadth-first search from **every** minimum code gives the stated exact radii and diameters. Every possible one-element exchange is examined, so the edge totals are exhaustive. For the orbit refinement, `verify_symmetry.py` constructs and checks 192 explicit automorphisms of \(S\) from its 16 translations and 12 difference-preserving linear transformations, and 1152 of \(R\) from independent row and column permutations and coordinate interchange. Each group acts on the full minimum-code family; the recorded orbit sizes sum to the exact total, establishing the displayed partition. The order of these explicitly constructed groups is the full automorphism-group order. In \(S\), the six neighbors of a fixed vertex induce a six-cycle, restricting their permutation stabilizer to at most twelve; in \(R\), they form two disjoint three-cliques, restricting their permutation stabilizer to at most \(3!^2\cdot2=72\). In each graph the nine vertices outside the closed neighborhood have **nine distinct** two-vertex traces on the six neighbors (an immediate finite check from the given adjacency rule), so an automorphism fixing the vertex and all six neighbors must fix the other nine vertices. Thus the neighborhood action is faithful and the complete group orders are bounded by \(16\cdot12=192\) and \(16\cdot72=1152\), attained by the displayed explicit groups.

## Verification

Run `python3 verify_bitmask.py`, `python3 verify_set_independent.py`, and `python3 verify_symmetry.py` with the standard Python library. The corresponding `.out` files record their expected exact outputs. The bitmask script checks all distances for both exchange graphs from every state; the independent script reconstructs both graphs from edge sets and validates all optimal codes and exchange components without reusing bitmask logic. The symmetry script verifies that each permutation preserves every source-graph edge before computing orbits. These programs make a complete finite proof for the two named graphs; they are not claimed to prove an arbitrary-order generalization.

## Relationship to prior work

Hernando, Mora and Pelayo introduced and studied global location-domination, including the complement criterion, in a manuscript first publicly available 2013-12-03 (arXiv:1312.0772v1). That definition and general theory are background, not claimed as new. Gravier, Parreau, Rottey, Storme and Vandomme (arXiv:1411.5275) study *identifying codes*, whose closed-neighborhood identification requirement differs; their general strongly regular graph bounds do not provide these global locating-dominating multiplicities. Hayat and coauthors (2023) examine binary locating-domination in regular and strongly regular graphs, but their rook-product bounds in Section 6.2 concern larger grid parameters rather than this complete four-by-four census. The 2015 ensemble study of optimal dominating and locating-dominating codes by Honkala, Hudry and Lobstein is pertinent generic theory; a complete text of that paper was not accessible for definitive statement-level exclusion.

## Limitations

The claim is a finite exact classification for two specified graphs. Reproducibility has been checked by executable independent enumerations, not by an external independent mathematical audit. The finite proof establishes these counts and moves, but not an abstract closed formula for all graphs with fixed strongly regular parameters. Inaccessible full text of one generic ensemble paper and unindexed older computations leave historical-priority uncertainty; no worldwide novelty guarantee is claimed.

## References

1. C. Hernando, M. Mora, I. M. Pelayo, *On global location-domination in graphs*, arXiv:1312.0772v1, first available 2013-12-03; later *Ars Mathematica Contemporanea* 8 (2015), 365–379. https://arxiv.org/abs/1312.0772
2. S. Gravier, A. Parreau, E. Rottey, L. Storme, E. Vandomme, *Identifying codes in vertex-transitive graphs and strongly regular graphs*, arXiv:1411.5275 (2014). https://arxiv.org/abs/1411.5275
3. S. Hayat et al., *On the binary locating-domination number of regular and strongly-regular graphs*, *Journal of Mathematical Inequalities* 17 (2023), DOI:10.7153/jmi-2023-17-105.
4. J. Honkala, O. Hudry, A. Lobstein, *On the ensemble of optimal dominating and locating-dominating codes in a graph*, *Information Processing Letters* (2015), DOI:10.1016/j.ipl.2015.04.005 (bibliographic/abstract-level access only).
