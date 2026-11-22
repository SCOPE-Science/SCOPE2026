# Local tie favoritism suppresses consensus on the Herschel graph

## Finding
On the eleven-vertex Herschel graph, independently biasing any chosen subset of the three degree-four vertices to choose opinion \(1\) at neighbor-count ties changes synchronous binary neighbor-majority dynamics in a counterintuitive way: as the number \(k\) of biased vertices grows from zero to three, the number of initial configurations attracted to *either* unanimous equilibrium strictly decreases, even though the basin of unanimous \(1\) strictly increases. The entire finite orbit census, including non-unanimous equilibria, primitive two-cycles and the sharp entrance-time cutoff, depends only on \(k\), not on the chosen vertices.

All counts below are of labelled configurations, out of \(2^{11}=2048\). The row \(k=0\) is an existing, previously studied reference system and is used only for comparison; the new result is the complete, independently verified local tie-intervention response for \(k=1,2,3\).

| Biased vertices \(k\) | Fixed configurations | Primitive two-cycle orbits | Basin of \(0^{11}\) | Basin of \(1^{11}\) | Combined unanimous basin | Total fixed-point basin | Maximum entrance time |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 20 | 61 | 501 | 501 | 1002 | 1092 | 6 |
| 1 | 16 | 48 | 285 | 567 | 852 | 906 | 6 |
| 2 | 13 | 44 | 171 | 624 | 795 | 822 | 6 |
| 3 | 11 | 55 | 91 | 672 | 763 | 772 | 4 |

In particular, applying the \(1\)-favoring tie policy at all three even-degree vertices increases the unanimous-\(1\) basin by \(171\) configurations but decreases the total unanimous basin by \(239\) configurations, relative to tie retention. The number of primitive two-cycles responds nonmonotonically: \(61,48,44,55\). All trajectories enter a fixed point or a primitive two-cycle.

## Assumptions and scope
The simple undirected graph has vertices \(1,\ldots,11\), with open neighborhoods

```
1: 2 4 5        2: 1 3 6 7       3: 2 4 8
4: 1 3 9 10     5: 1 6 10        6: 2 5 11
7: 2 8 11       8: 3 7 9         9: 4 8 11
10: 4 5 11      11: 6 7 9 10
```

It has \(18\) edges and exactly three degree-four vertices \(H=\{2,4,11\}\); all other degrees are three. For \(B\subseteq H\), state \(x\in\{0,1\}^{11}\), and \(a_i(x)=\sum_{j\sim i}x_j\), define the synchronous update \(F_B\) by

\[
(F_B(x))_i=\begin{cases}
1,&2a_i(x)>\deg(i),\\
0,&2a_i(x)<\deg(i),\\
1,&2a_i(x)=\deg(i)\text{ and }i\in B,\\
x_i,&2a_i(x)=\deg(i)\text{ and }i\notin B.
\end{cases}
\]

The *entrance time* of an initial state is the smallest \(t\ge0\) such that \(F_B^t(x)\) belongs to its eventual periodic orbit. An attraction basin includes the periodic states themselves. A primitive two-cycle orbit consists of two distinct states, and is counted once. The graph labels and update convention are essential for numerical reproducibility; the final numerical totals are invariant under any graph isomorphism.

## Proof
**Graph symmetry.** The following two permutations, specified as images of vertices \(1,\ldots,11\), preserve every edge of the above adjacency list:

```
rotation:    [10,4,9,11,5,1,3,8,7,6,2]
reflection:  [ 1,4,3, 2,5,10,9,8,7,6,11]
```

On \(H\), the first acts as the three-cycle \((2\ 4\ 11)\), and the second transposes \(2\) and \(4\). These two permutations induce the full symmetric group on \(H\). Therefore all \(k\)-element intervention subsets are conjugate for each \(k\), and it suffices to compute one representative of each size. The executable verification additionally checks every one of the eight subsets independently.

**Exhaustive finite certificate.** Encode a state by the eleven-bit integer \(s=\sum_{i=1}^{11}x_i2^{i-1}\), so the domain is exactly \(\{0,1,\ldots,2047\}\). For each of the eight subsets \(B\), evaluate the displayed Boolean formula at *every* integer in that range, giving an explicit successor table of \(2048\) entries. This is not sampling or a truncation of an infinite search: the entire mathematical state space is evaluated.

A finite directed graph in which every state has one successor is a union of directed cycles with directed rooted trees feeding into those cycles. In `scripts/peeling_certificate.py`, count the incoming edges of each state and iteratively remove vertices with zero remaining indegree. This leaves exactly the recurrent cycles; following the remaining successor edges gives their least periods and canonical representatives. Reverse propagation through the deleted vertices determines, for every initial state, its first entrance time, eventual period, and attracting orbit. Consequently, counting the assigned states gives the exact basin of each recurrent orbit. This finite graph algorithm is justified by induction over the removal order, and makes no assumptions about eventual period or maximum entrance time.

An independently organized verifier (`scripts/direct_walk.py`) follows each of the \(2048\) starting states to the first repeated state, identifies the repeated segment as its eventual periodic orbit, and counts first-entry steps and basins without relying on indegree peeling. `scripts/build_census.py` performs a field-by-field equality check of both outputs for all \(8\) interventions and produces `certificates/census.json`. They agree on the complete entrance-time/least-period joint distribution and every orbit-basin-size frequency. In particular the only observed and *exhaustively certified* recurrent lengths are \(1\) and \(2\), and the sharp entrance-time maxima are those in the table. Every reported count is obtained from the specified finite update formula and these exhaustive operations.

For the intervention sizes \(k=1,2,3\), the exact fixed-orbit basin-size histograms (basin size : number of fixed points) are respectively

```
k=1: 1:4, 2:4, 7:6, 285:1, 567:1
k=2: 1:5, 2:4, 7:2, 171:1, 624:1
k=3: 1:9, 91:1, 672:1
```

The remaining initial states belong to the basins of primitive two-cycles. Thus, all entries in the main table follow by finite exhaustive partition, not by extrapolation from partial experiments. Complete orbit-basin histograms and entrance-time/period distributions are present in the certificate.

## Verification
With Python 3 from the directory containing this document, run:

```
python scripts/peeling_certificate.py
python scripts/direct_walk.py
python scripts/build_census.py
```

The first script checks adjacency symmetry, evaluates each of the eight update rules, peels the entire functional graph and checks the four \(k\)-classes. The second independently traces every starting trajectory. The third checks equality of the two complete censuses, reproduces `certificates/census.json`, and outputs a PASS line only if every comparison succeeds. No nonstandard Python packages, external data files, or network services are needed. The additional small direct summary shows the sharp entrance values (and the complete machine-readable certificate includes all time-layer counts).

## Relationship to prior work
The general framework of synchronous finite graph dynamical systems is covered by Aledo, Martínez and Valverde (2015). Gärtner and Zehmakan (2017) analyze homogeneous tie favoritism for majority dynamics, primarily on two-dimensional tori, and Zehmakan (2024) compares deterministic incumbent ties with random ties and discusses general stabilization. These sources motivate examining tie rules, but the inspected material does not enumerate spatially *localized* deterministic bias on the Herschel graph or imply the specific eight exact basin and orbit censuses.

An existing majority census for the Herschel graph under incumbent tie retention establishes the \(k=0\) row; that row is baseline evidence rather than the novel theorem. Prior published exact studies of altered graph edges or majority voting on other graphs do not determine how changing the local tie rule at the three fixed degree-four vertices reorganizes these basins. The graph itself is classical; no novelty is claimed for the graph, graph automorphisms, or the general finite-functional-graph counting algorithm. The new claim is the precise, complete intervention-specific dynamical response and the strict decrease of the combined unanimity basin despite expansion of the favored opinion's basin.

## Limitations
This is a rigorous finite exact result for the specified eleven-vertex graph and four intervention-size classes. It is *not* a theorem that arbitrary networks exhibit the same monotonicity, nonmonotonicity, or entrance times. The proof uses fully exhaustive finite enumeration and two independent methods, rather than a closed analytic basin formula for all graph sizes. A search of accessible literature and prior mathematical claims did not find a covering result, but unindexed or unexamined historical equivalents remain possible. Independent mathematical review has not been performed.

## References
1. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (first published 24 March 2015), DOI: https://doi.org/10.1155/2015/594294.
2. B. Gärtner and A. N. Zehmakan, *(Biased) Majority Rule Cellular Automata*, arXiv:1711.10920v1 (24 November 2017), https://arxiv.org/abs/1711.10920.
3. A. N. Zehmakan, *Majority opinion diffusion: when tie-breaking rule matters*, Autonomous Agents and Multi-Agent Systems 38 (2024), article 21, https://doi.org/10.1007/s10458-024-09651-y.
4. Herschel graph labelled diagram, University of Washington combinatorics handout, https://faculty.washington.edu/moishe/hanoi-2011/DO-2011/Week-8/Supplements/Herschel%20Graph.pdf (day-level publication date not established; graph labels independently explicit above).
