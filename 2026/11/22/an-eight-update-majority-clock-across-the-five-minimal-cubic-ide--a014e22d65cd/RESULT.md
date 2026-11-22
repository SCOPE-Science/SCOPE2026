# An eight-update majority clock across the five minimal cubic identity graphs

## Finding

For the five explicit twelve-vertex cubic asymmetric graphs defined below, synchronous binary open-neighbor majority has only fixed points and primitive two-cycles. On each graph the map \(F\) satisfies the common sharp global identity \(F^{10}=F^8\). The bound of eight updates to the first periodic state is attained exactly on graph G5, by precisely two of its \(2^{12}=4096\) labelled initial configurations; for G1–G4 the sharp bound is seven updates. The five graphs are the catalogued minimum-order cubic identity graphs (graphs with no nonidentity automorphism). The all-state orbit and attraction-basin census is:

| Graph | Fixed configurations | Primitive two-cycle orbits | States eventually fixed | States eventually two-periodic | Sharp entry time | Largest fixed basin | Largest two-cycle basin |
|---|---:|---:|---:|---:|---:|---:|---:|
| G1 | 12 | 63 | 1062 | 3034 | 7 | 454 | 294 |
| G2 | 12 | 97 | 978 | 3118 | 7 | 425 | 310 |
| G3 | 12 | 134 | 1458 | 2638 | 7 | 620 | 261 |
| G4 | 12 | 73 | 1258 | 2838 | 7 | 572 | 294 |
| G5 | 14 | 95 | 1246 | 2850 | 8 | 568 | 238 |

The exact first-entry populations, with time counted from the initial state and a periodic initial state entering at time zero, are:

| Graph | Time 0 | Time 1 | Time 2 | Time 3 | Time 4 | Time 5 | Time 6 | Time 7 | Time 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| G1 | 138 | 1090 | 1478 | 782 | 390 | 154 | 56 | 8 | 0 |
| G2 | 206 | 1108 | 1500 | 768 | 344 | 118 | 46 | 6 | 0 |
| G3 | 280 | 1286 | 1238 | 770 | 422 | 86 | 12 | 2 | 0 |
| G4 | 158 | 1042 | 1438 | 726 | 500 | 176 | 54 | 2 | 0 |
| G5 | 204 | 986 | 1354 | 744 | 578 | 172 | 48 | 8 | 2 |

Each table row sums to 4096, and the exact individual orbit-basin size multiplicities, separately for fixed points and two-cycles, are recorded in `census.json`. Notice that G3 has the largest number of primitive two-cycles (134) but the *smallest* eventual two-cycle population (2638), whereas G2 has only 97 such orbits but the *largest* eventual two-cycle population (3118). Thus the recurrent-orbit count alone does not rank the oscillatory attraction probability in this natural class.

## Assumptions and scope

For each listed graph \(G\), take the labelled vertex set \(\{0,1,\ldots,11\}\). The edge set is constructed from the indicated LCF list of twelve offsets, by joining vertex \(i\) to \(i+1\pmod{12}\) and to \(i+d_i\pmod{12}\), ignoring duplicate undirected edge entries. Complete explicit edges are in `graph_catalog.json`. The five precise LCF lists are:

```text
G1: [-5, 2, -3, -2, 6, 4, 2, 5, -2, -4, 6, 3]
G2: [6, 3, -4, -4, -3, 3, 6, 2, -3, -2, 4, 4]
G3: [4, -2, 5, 2, -4, -2, 3, -5, 2, -3, -2, 2]
G4: [6, -5, 2, 6, -2, 6, 6, 3, 5, 6, -3, 6]
G5: [2, -5, -2, 6, 3, 6, 4, -3, 5, 6, -4, 6]
```

Every graph is connected, simple, three-regular and has exactly 18 edges. Exact adjacency-preserving backtracking establishes that each has only the identity automorphism and that no two are isomorphic. The identification of these five examples as the *complete minimum-order class* uses the published catalogue of simple cubic graphs and the classical minimum-order identity-graph literature; the reproduced computation checks the five named objects, not an independent exhaustive enumeration of all cubic graphs.

A configuration is \(x\in\{0,1\}^{12}\). At every vertex \(v\), the synchronous update is
\[
F(x)_v=\mathbf{1}\left\{\sum_{u\sim v}x_u\ge2\right\}.
\]
Because degrees equal three, there are no ties. A fixed point has \(F(x)=x\); a primitive two-cycle is an unordered pair \(\{x,F(x)\}\) with \(F^2(x)=x\ne F(x)\). The first periodic-entry time \(T(x)\) is the least nonnegative \(t\) for which \(F^t(x)\) is periodic. All counts refer to labelled configurations and temporal orbits; spatial isomorphisms do not identify configurations.

## Proof

**Finite exhaustive reduction and exact update.** Encode each binary configuration as \(s=\sum_{v=0}^{11}x_v2^v\), so that the integers \(0\le s<4096\) encode every labelled state exactly once. `verify_forward.py` independently constructs each graph from its LCF list and evaluates the majority expression using bit intersection and bit counts. For every one of the 4096 states of each graph it follows the unique forward trajectory until it meets an already classified state or closes a directed cycle. Directed-cycle detection is exact, and reversing the transient path assigns each state its precise orbit, least period, and least first-entry time. Hence every state is counted in exactly one first-entry, period, and orbit-basin class.

**Independent reverse functional graph.** `verify_reverse.py` constructs neighbors from a hard-coded explicit list of eighteen undirected edges per graph, rather than LCF construction; it separately evaluates the rule using arrays of vertex bits. It enumerates every transition, removes all indegree-zero vertices recursively, and traverses the remaining cycles. The remaining vertices of a finite functional graph are exactly the periodic states, since every non-cycle vertex eventually has indegree zero in the induced subgraph. Classifying in reverse removal order gives the correct first-entry depth and individual basin size. The independent programs produce exactly the same full five-graph data structures, including the full individual-basin-size histograms, all nine entry-time cells, and all sharp witnesses.

**Global identity and sharpness.** All five verified complete transition tables satisfy \(F^{10}(x)=F^8(x)\) for every \(x\). Consequently \(F^8(x)\) belongs to a fixed point or two-cycle for every initial state. The computed entry-time distribution proves that G5 has two states first reaching periodic states at time eight, with integer encodings 486 and 3609 in its listed LCF labelling. For example, the first trajectory is

```text
486, 467, 422, 339, 166, 337, 162, 336, 160, 80, 160
```

The last three entries exhibit the period-two pair (160,80), while the full transition function and first-entry checker certify no earlier periodic state; the second witness is its complemented counterpart. For the other graphs, each has positive time-seven population but no time-eight population. This proves both the global identity and its sharp uniform entry-time bound.

**Graph identity check.** `verify_catalog.py` reconstructs all five graph adjacencies from `graph_catalog.json`, verifies connectivity and three-regularity, and enumerates all adjacency-preserving bijections using complete constrained backtracking. Each automorphism count is one, and all ten between-graph isomorphism counts are zero. The finite graph classification relies only on the LCF catalogue for completeness; the theorem remains independently exact for the five explicitly presented graphs.

## Verification

Using Python 3 standard library only, in the same directory as the embedded files:

```sh
python3 verify_forward.py > forward_recomputed.json
python3 verify_reverse.py > reverse_recomputed.json
python3 verify_catalog.py > catalog_recomputed.txt
python3 -c 'import json; a=json.load(open("forward_recomputed.json")); b=json.load(open("reverse_recomputed.json")); c=json.load(open("census.json")); assert a==b==c; assert all(d["map_power_identity"] for d in c.values()); print("FULL_CENSUS_OK")'
```

All three checks have been run. The independent full-census JSON documents all \(5\cdot 4096=20480\) initial configurations, and `catalog_check.txt` contains each automorphism/isomorphism decision. The exact two G5 time-eight witness encodings were checked. A finite enumeration is an exhaustive proof for these five fixed graphs; it is not a theorem concerning every cubic graph on other orders.

## Relationship to prior work

General synchronous threshold dynamics is known to have eventual periods at most two; that qualitative theorem, attributed to Goles and Olivos, is not claimed as new. Benjamini and collaborators (arXiv:1405.2486v1, 2014-05-11) discuss majority dynamics and eventual two-periodicity on broader graph classes; Kaaser, Mallmann-Trenn and Natale (2016) provide general voting-time estimates. Neither inspected treatment provides these five finite-state tables or the sharp eight-update identity for these five graphs.

The already published finite-state catalogue for three-state excitation on the asymmetric Frucht graph (published-finding corpus identifier `2026/11/8/SCOPE-a-twenty-one-step-excitation-transient-on-the-asymmetric-frucht--7b215d08f374`) concerns a *different local update* with three states and can have periods above two; it does not imply the present binary-majority orbit or basin table. The independently inspected published dodecahedral binary-majority census (published-finding corpus identifier `2026/11/1/SCOPE-dodecahedral-majority-dynamics-an-exact-recurrent-basin-and-symm--095dfb0decea`) concerns a twenty-vertex cubic graph, and neither its exact statistics nor its seven-update bound determines the current five-graph data. Other published cubic-graph majority studies likewise give no verified exact implication to these five examples. An exact earlier enumeration under different labels, or in unindexed literature, cannot be ruled out.

## Limitations

The theorem is a complete *finite* classification of five explicitly labelled twelve-vertex graphs, with software-supported exhaustive proof, not a formula for an unbounded family of graphs. No general upper bound of eight is asserted for arbitrary cubic or asymmetric graphs. The catalogue's completeness relies on the cited literature rather than a fresh enumeration of all cubic graphs. Historical-priority uncertainty remains, and there is no independent external mathematical audit. The earliest exact-date public source used for archival eligibility is the 2014-05-11 preprint; earlier graph-theory sources are not assigned invented first-public day dates.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (2014-05-11), https://arxiv.org/abs/1405.2486 .
2. D. Kaaser, D. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, MFCS 2016, DOI 10.4230/LIPIcs.MFCS.2016.55, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2016.55 .
3. A. T. Balaban, F. Harary, P. Hill, R. Westwick, *Cubic identity graphs and planar graphs derived from trees*, *Journal of the Australian Mathematical Society* (1968), DOI 10.1017/S144678870000639X, https://doi.org/10.1017/S144678870000639X .
4. *Table of simple cubic graphs*, https://en.wikipedia.org/wiki/Table_of_simple_cubic_graphs , five twelve-vertex cubic examples with automorphism group of order one.
5. E. Goles and J. Olivos, *Periodic Behaviour of generalized threshold functions*, *Discrete Mathematics* (1980), DOI 10.1016/0012-365X(80)90121-1.
6. Published published-finding corpus Frucht-graph excitation classification, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-twenty-one-step-excitation-transient-on-the-asymmetric-frucht--7b215d08f374 .
7. Published published-finding corpus dodecahedral-majority classification, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-dodecahedral-majority-dynamics-an-exact-recurrent-basin-and-symm--095dfb0decea .
