# Matched excitation-period basins on the Herschel graph despite unequal recurrent clocks

## Finding
Let \(G\) be the eleven-vertex, eighteen-edge Herschel graph in the vertex labelling below. Start synchronous three-color cyclic successor-contact dynamics (CCA) and three-state Greenberg–Hastings dynamics (GHM) from **the same** labelled initial coloring \(x\in\{0,1,2\}^{11}\). Write \(p_C(x),p_H(x)\) for the eventual least temporal periods and \(\tau_C(x),\tau_H(x)\) for the first times at which the full configuration is already on its eventual orbit.

The following complete finite classification holds:

\[
 \boxed{p_C(x)=p_H(x)\in\{1,3,4\}\quad\text{for every one of the }3^{11}=177147\text{ initial colorings}.}
\]

The three **common, pointwise identical period basins** and the distinct immediately recurrent populations are:

| Eventual least period | Initial colorings in common basin | GHM recurrent states | CCA recurrent states |
|:--:|--:|--:|--:|
| \(1\) | 17,397 | 1 | 3 |
| \(3\) | 23,346 | 3,060 | 3,060 |
| \(4\) | 136,404 | 1,200 | 4,752 |

Thus GHM has \(1020\) primitive three-orbits and \(300\) primitive four-orbits; CCA has the same \(1020\) three-orbits but \(1188\) four-orbits. Every GHM recurrent state is also CCA recurrent, and **both update maps agree on this common recurrent set**. In particular the two models have exactly the same temporal three-cycle configurations and transitions, whereas CCA contains \(3552\) additional temporal-four recurrent configurations.

First-periodic-entry times differ sharply:
\[
 \boxed{\max_x\tau_H(x)=10,\qquad\max_x\tau_C(x)=8.}
\]
Exactly \(36\) GHM starts attain time ten; exactly \(108\) CCA starts attain time eight. All these maximally delayed states ultimately have least period three. The attached exact integer census includes the populations of every pair \((\tau,p)\) for each dynamics (27 nonzero GHM classes, 21 nonzero CCA classes).

## Assumptions and scope
The graph is the standard, undirected, simple Herschel graph with vertices labelled \(1,\ldots,11\). Its complete neighbor lists are

```
1: 2 4 5
2: 1 3 6 7
3: 2 4 8
4: 1 3 9 10
5: 1 6 10
6: 2 5 11
7: 2 8 11
8: 3 7 9
9: 4 8 11
10: 4 5 11
11: 6 7 9 10
```

This list has eleven vertices, eighteen undirected edges, three vertices of degree four and eight of degree three; it is the Herschel graph in the cited University of Washington labelled drawing. There are no self-loops, random updates, external inputs or threshold-two contacts. CCA advances color \(c\) to \(c+1\pmod3\) exactly when at least one neighbor has that successor color; otherwise it retains \(c\). GHM advances \(1\to2\to0\) unconditionally; it advances \(0\to1\) exactly when a neighbor is excited (color one) and otherwise retains zero. All eleven vertices update in parallel. Initial states, transient layers, and periodic states retain vertex labels; spatial automorphisms do not identify different states. Temporal orbit counts divide recurrent population by the **least** temporal period.

## Proof
**Exact finite state representation.** Encode every configuration \(x\) as
\[
 s(x)=\sum_{i=1}^{11}x_i3^{i-1}\in\{0,\ldots,177146\}.
\]
This is a bijection; the displayed graph list and local rule uniquely prescribe one successor \(F_C(s)\) and \(F_H(s)\) for each of the \(177147\) integers. The packaged `verification/exhaustive_graph.py` constructs both complete successor arrays with integer arithmetic and no external datasets.

**Complete orbit resolution.** In either array, build the directed functional graph \(s\to F(s)\), with outdegree exactly one. Repeatedly delete every zero-indegree vertex and decrement its successor's indegree. The surviving vertices are precisely the disjoint directed cycles: any noncycle directed tree has a source that is eventually removed, and a directed cycle has no zero-indegree vertex. Give each remaining vertex transient depth zero and the length of its directed cycle as eventual least period. Process deleted vertices in **reverse deletion order**; for each deleted \(s\), put \(\tau(s)=1+\tau(F(s))\) and \(p(s)=p(F(s))\). This is a finite induction that assigns **all** states, not a sample. The code independently checks that no state is unassigned and all histogram counts total \(177147\).

The resulting exact period-basin vector in the order \(1,3,4\) is \((17397,23346,136404)\) in **both** arrays, and the pointwise mismatch count \(\#\{x:p_C(x)\ne p_H(x)\}\) is exactly zero. The immediately recurrent vectors are \((3,3060,4752)\) for CCA and \((1,3060,1200)\) for GHM. The program explicitly forms the GHM period-three and period-four recurrent sets, verifies their inclusions in the corresponding CCA sets and compares both successor maps on every member. The period-three sets coincide. Its exhaustive histogram shows \(\tau_H\le10\) and \(\tau_C\le8\), and exhibits respectively \(36\) and \(108\) states at the final depth, with least period three, proving both maxima sharp.

**Independent exhaustive proof by a different algorithm.** The separately implemented C++17 program `verification/independent_trajectories.cpp` defines both local maps directly from the same mathematical adjacency list, without reading the Python successor arrays. For every start state, Floyd's tortoise-and-hare algorithm finds the cycle by meeting two iterates, aligns a fresh walker from the start to recover the first cycle-entry index, and traverses one complete return to obtain the least cycle length. It independently accumulates all \((\tau,p)\) classes, verifies the pointwise period equality and the recurrent inclusion/transition checks, and reproduces all totals above. This proof is exhaustive over the **entire finite domain**. Its correctness uses only elementary cycle detection for finite maps; it does not infer an infinite-family statement from numerical experiments.

## Verification
The two source files and their recorded standard-output results are embedded at `verification/exhaustive_graph.py`, `verification/exhaustive_graph.out`, `verification/independent_trajectories.cpp`, and `verification/independent_trajectories.out`. Run `python3 verification/exhaustive_graph.py` and check its final marker `HERSCHEL_EXHAUSTIVE_OK`. Independently compile and run the C++ code with `g++ -std=c++17 -O2 verification/independent_trajectories.cpp -o verify && ./verify`, checking for final marker `HERSCHEL_FLOYD_OK`. The two generated complete first-entry/period histograms coincide cell for cell. Both computations were executed from the actual packaged source files. The physical graph's adjacency and nonHamiltonian extremal motivation are documented by the independent Herschel graph sources in References.

## Relationship to prior work
The original Greenberg–Hastings and cyclic-contact models, as well as their three-color graph evolution, predate this result. Gravner, Lyu and Sivakoff (2016, Lemma 1 and Theorem 3) prove a walk-based description and an exact synchronization criterion on arbitrary finite graphs, and determine limiting excitation rates from cycle circulation. These results explain the **common consensus-versus-activity dichotomy**, but do not determine the least temporal periods, exact numbers of periodic states, or depth histograms in the present eleven-vertex system. A further general result on three-color graph automata establishes that GHM's eventual period divides CCA's period for each initial coloring; divisibility does **not** imply equality. A published counterexample on the Petersen graph includes 4800 initial states with CCA period eight and GHM period four, while a previously classified complete-bipartite family does have matching periods. Neither case is the Herschel graph, which is neither complete bipartite nor the Petersen graph. The period-basin match on this natural irregular polyhedral graph, together with its unequal recurrent populations and sharp depth clocks, is the claim here.

Doba (2018) proves a maximum-cycle-density criterion for GHM and derives qualitative periodic behavior on finite graphs. Its all-graph results do not provide the exact matched-initial-state CCA/GHM Herschel census. The published Herschel graph adjacency and polyhedral properties identify the mathematical object, rather than providing these dynamical counts.

## Limitations
This is an exact finite classification for the stated Herschel graph and the two specified three-state, threshold-one synchronous rules. It does not establish any all-graph or all-polyhedral family statement, nor does it attribute the observed equality causally to nonHamiltonicity. Period-basin coincidence does not mean the two trajectories agree before recurrence, that their entire attractor sets coincide, or that individual **attractor-orbit basins** are identical. It is possible that additional unindexed historical computations contain part of this census; no exhaustive historical priority claim is made. Two exact exhaustive implementations support the numerical finite proof, but no independent external scientific audit has been performed.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, first publicly available preprint 1993-03-22, https://arxiv.org/abs/patt-sol/9303002 .
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first posted 2016-10-24, https://arxiv.org/abs/1610.07320 (especially Lemma 1, Theorem 3).
3. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), 101–126, https://doi.org/10.25088/ComplexSystems.27.2.101 ; https://wpmedia.wolfram.com/sites/13/2018/09/27-2-1.pdf .
4. *Herschel Graph*, labelled eleven-vertex drawing, University of Washington, https://faculty.washington.edu/moishe/hanoi-2011/DO-2011/Week-8/Supplements/Herschel%20Graph.pdf ; E. W. Weisstein, *Herschel Graph*, MathWorld, https://mathworld.wolfram.com/HerschelGraph.html .
5. *Exact excitation-clock reconstruction and period divisibility for three-color graph automata*, publicly available finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-excitation-clock-reconstruction-and-period-divisibility-fo--6edafe27dc02 .
6. *Petersen-specific period doubling between cyclic and refractory excitation dynamics*, publicly available finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-petersen-specific-period-doubling-between-cyclic-and-refractory--85df9829d668 .
7. *Matched eventual periods but different transient clocks for three-state excitable dynamics on bicliques*, publicly available finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-matched-eventual-periods-but-different-transient-clocks-for-thre--29320e9e89df .
