# Two period-halving channels in Heawood cyclic and refractory excitation

## Finding

Consider the Heawood graph, realized as the fourteen-vertex point–line incidence graph of the Fano plane. Start two deterministic, synchronous, three-color dynamics from the **same** labelled coloring: cyclic successor-contact updating (CCA) and Greenberg–Hastings excitation (GHM), both at contact threshold one. Let \(p_C(x)\) and \(p_H(x)\) denote the eventual **least** temporal periods of the corresponding trajectories from coloring \(x\).

For all \(3^{14}=4{,}782{,}969\) initial colorings, the complete joint-period classification is:

| \(p_C(x)\) | \(p_H(x)\) | Number of labelled initial colorings |
|---:|---:|---:|
| 1 | 1 | 240,039 |
| 3 | 3 | 705,474 |
| 4 | 4 | 507,024 |
| 5 | 5 | 105,084 |
| 6 | 6 | 1,283,436 |
| 8 | 4 | 275,520 |
| 8 | 8 | 448,224 |
| 10 | 5 | 237,216 |
| 10 | 10 | 626,136 |
| 14 | 14 | 354,816 |

Every unlisted ordered period pair has count zero. **Exactly 512,736** initial colorings exhibit different eventual least periods, consisting exclusively of the 275,520 colorings with \((p_C,p_H)=(8,4)\) and the 237,216 with \((p_C,p_H)=(10,5)\). In particular, on this graph the GHM eventual period always divides the CCA eventual period, and a discrepancy always halves it; neither assertion is claimed for arbitrary graphs.

## Assumptions and scope

The Fano plane has points \(P_0,\dots,P_6\) and lines indexed by seven distinct triples

```
{0,1,2}, {0,3,4}, {0,5,6}, {1,3,5},
{1,4,6}, {2,3,6}, {2,4,5}.
```

Join point \(P_i\) to line vertex \(L_j\) precisely when the corresponding triple contains \(i\). This describes a simple cubic bipartite graph with fourteen labelled vertices. Each pair of points lies in exactly one triple, so it is the Fano incidence graph, isomorphic to the conventional Heawood graph. Each state is a vector \(x\in\{0,1,2\}^{14}\). All vertices update from old states simultaneously. Counts do not identify states under spatial symmetries.

For CCA, a vertex of color \(c\) becomes \(c+1\pmod3\) if some neighbor already has that successor color; otherwise it retains \(c\). For GHM, colors \(1\mapsto2\mapsto0\) unconditionally, and a resting vertex of color zero becomes one exactly when at least one neighbor is color one. The eventual least period is defined using the smallest preperiod \(t\ge0\) followed by the least \(p\ge1\) for which \(F^{t+p}(x)=F^t(x)\). This specifies both models completely.

## Proof

**Exhaustive finite-state lemma.** For any deterministic self-map \(F\) of a finite state set, the directed graph of arrows \(x\mapsto F(x)\) is a disjoint union of directed cycles with directed trees leading into them. Iteratively removing every vertex of indegree zero, with its outgoing arrow, removes exactly the nonperiodic vertices. Any vertex on a directed cycle cannot be removed because its predecessor on that cycle is never removed; every tree vertex is eventually removed starting at its leaves. For each surviving cycle, traversing successive distinct vertices until the start repeats determines its true least period. Reversing the removal order assigns the period of each vertex from its successor and adds one to its entry depth. This procedure therefore obtains the exact eventual least period for **every** state, without numerical approximation.

**First complete classifier.** The file `verification/census_indegree.cpp` encodes a coloring as the integer \(\sum_{v=0}^{13}x_v3^v\). It constructs the displayed seven point triples and the corresponding incidence adjacency, then enumerates every integer in \(\{0,\ldots,3^{14}-1\}\). It constructs both update maps exactly and applies the indegree-removal lemma separately to each. Its recorded output `verification/census_indegree.out` contains the full joint table, both models' first-entry/least-period marginals, and the discrepancy's pair of entry-time distributions. No sampling or finite-size extrapolation enters this calculation: the finite state space is completely covered.

**Independent path classifier.** The file `verification/census_paths.cpp` constructs the Heawood graph independently from the seven nonzero three-bit vectors on each shore: a point and line are incident when their binary dot product is zero. Each vertex has three incident neighbors; the resulting incidence structure is the Fano plane. This classifier does not use indegree elimination. Instead it explores each previously unseen trajectory, identifies a repeated state on its active path or enters an already classified path, and propagates true least periods backward. For an active path, the first repeated vertex marks the start of a directed cycle; earlier path vertices lead into it. Each state is classified exactly once. Its output is saved as `verification/census_paths.out`.

**Exact integer agreement.** Both programs obtain the ten joint classes displayed above. Their totals add exactly to \(3^{14}\), their discrepancy counts add to \(275{,}520+237{,}216=512{,}736\), and neither yields any other ordered pair. The second classifier also identifies representatives (in its three-bit-dot-product vertex order) encoded by integers `10976` and `8885` for the two distinct discrepancy types. The standalone `verification/replay.py` checks these representatives by a third implementation using the cyclic Fano lines \(L_j=\{j,j+1,j+3\}\pmod7\), with an explicitly computed incidence-preserving relabeling. It also recompiles both finite-state classifiers and compares their complete recorded outputs to the provided files. `verification/replay.out` records the successful replay.

The exhaustive finite-set argument and independent computations establish the stated universal quantifier over all labelled initial colorings. Trajectory witnesses alone would show only existence; the period-exclusion and multiplicity assertions rely on complete enumeration.

## Verification

The package includes all source code and exact output text. From its root run `python3 verification/replay.py` with a C++17 compiler providing `g++`. The replay recompiles both programs, checks both recorded outputs byte-for-byte, checks exact agreement of the ten joint populations and their total, and verifies one witness for each discrepancy class under a third incidence presentation. All calculations use integer arithmetic. The observed terminal output is in `verification/replay.out`.

The first classifier reports CCA maximal first-periodic-entry time eight; the second reports GHM maximal first-periodic-entry time ten, consistent with the previously published GHM-only Heawood census. These are verification context, not additional independent claims of novelty.

## Relationship to prior work

The rules themselves originate in classical studies of excitable media. Durrett and Griffeath studied CCA and GHM in 1993. Gravner, Lyu and Sivakoff established qualitative finite-graph criteria for synchronization and a circulation formula for asymptotic activity; their results do **not** give this labelled Heawood joint-period distribution or count the two period-halving channels. The exact GHM-only Heawood period and entry-time census, including the ten-step maximum, is already available and is explicitly credited here. It does not determine which particular initial colorings have particular CCA eventual periods, and therefore does not imply the joint table. A published biclique theorem proves pointwise equality of CCA and GHM eventual periods for all bicliques; its hypothesis fails for the Heawood graph. Earlier comparisons on the ten-vertex Petersen graph and twelve-vertex Frucht graph give other finite examples of an eight-to-four discrepancy, but not the additional ten-to-five channel or the Heawood counts.

## Limitations

This is a complete finite-graph classification, not a theorem about all cubic graphs, all projective planes, or all temporal orbits under arbitrary color numbers. Exactness relies on the explicitly reproducible exhaustive integer programs; a list of sampled trajectories would not suffice. The result classifies **eventual least periods**, not pairwise equality of ultimate configurations or an orbit-by-orbit conjugacy. The primary literature comparison does not certify absolute historical priority, and only an accessible abstract—not the full 1993 preprint—was inspected. No independent external mathematical audit has been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first publicly submitted 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002 .
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (first posted 2016-10-24); *Annals of Applied Probability* 28 (2018), 3324–3357, https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf .
3. *Exact Heawood excitation census: eight primitive periods and a ten-step maximal transient*, accessible scientific result with complete GHM-only census, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-heawood-excitation-census-eight-primitive-periods-and-a-te--29120402709f .
4. *Matched eventual periods but different transient clocks for three-state excitable dynamics on bicliques*, scientific result giving all-size biclique comparison, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-matched-eventual-periods-but-different-transient-clocks-for-thre--29320e9e89df .
5. J. M. Greenberg and S. P. Hastings, *Spatial patterns for discrete models of diffusion in excitable media*, *SIAM Journal on Applied Mathematics* 34 (1978), 515–523, https://doi.org/10.1137/0134040 .
