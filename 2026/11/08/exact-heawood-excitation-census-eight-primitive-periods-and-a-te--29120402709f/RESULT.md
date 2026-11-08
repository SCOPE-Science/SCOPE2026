# Exact Heawood excitation census: eight primitive periods and a ten-step maximal transient

## Finding

Let \(H\) be the Heawood graph, presented as the incidence graph of the seven-point Fano plane. Label points \(P_0,\ldots,P_6\) and lines \(L_0,\ldots,L_6\), with \(L_j\) incident to \(P_j,P_{j+1},P_{j+3}\), subscripts modulo seven. Thus \(H\) has fourteen vertices and twenty-one edges. For every vertex \(v\), its state belongs to \(\{0,1,2\}\) (resting, excited, refractory). Define the synchronous deterministic Greenberg--Hastings map \(F\) by

\[
F(x)_v=\begin{cases}
2,&x_v=1,\\
0,&x_v=2,\\
1,&x_v=0\text{ and some neighbor of }v\text{ has state }1,\\
0,&\text{otherwise}.
\end{cases}
\]

For a state \(x\), let \(T(x)\) be the smallest nonnegative time for which \(F^{T(x)}(x)\) lies on a periodic orbit; let \(P(x)\) be that orbit's least positive period. Set \(N_{t,p}=\#\{x:T(x)=t,\ P(x)=p\}\). An exhaustive finite-state classification establishes:

* The **complete** set of possible least periods is \(\{1,3,4,5,6,8,10,14\}\). The corresponding numbers of distinct primitive orbits, in this order, are \(1,5334,224,84,42,168,84,96\).
* Exactly \(21099\) of the \(3^{14}=4782969\) labelled configurations are already periodic. Exactly \(12096\) configurations have \(T=10\); **all** of them subsequently enter period-four orbits. No configuration has \(T>10\).
* The number of configurations at each exact entry time \(t=0,1,\ldots,10\), respectively, is
  \[
  (21099,305203,1303711,1272154,1100708,526918,168336,42840,17136,12768,12096).
  \]
* The **entire joint distribution** \(N_{t,p}\) consists of the fifty-five positive rows of `verification/census.csv`; for every pair absent from that table, the count is zero. This table, and not merely its marginals, is part of the finding.
* Consequently \(F^{850}=F^{10}\). Both parameters are optimal in the following sense: ten is the least global first-periodic-entry bound, and \(840\) is the least positive integer \(m\) satisfying \(F^{10+m}=F^{10}\), because all eight listed primitive periods occur.

## Assumptions and scope

The vertex order used for integer and string encodings is \(P_0,\ldots,P_6,L_0,\ldots,L_6\). Every configuration is a labelled fourteen-tuple, with the base-three integer encoding \(\sum_{i=0}^{13} x_i3^i\). No graph automorphism identifications are made in counts. All fourteen vertices update simultaneously, each using the other vertices' old states. The graph is loopless and all edges undirected. The claim is exactly for this finite graph and this three-state threshold-one rule; it does not assert the same period spectrum for other graphs or thresholds.

## Proof

**Finite functional-graph reduction.** There are exactly \(3^{14}\) possible configurations. The formula above determines exactly one successor of each configuration, yielding a finite directed functional graph. Every finite functional graph consists of directed cycles with rooted in-trees; hence each configuration has a well-defined preperiod \(T(x)\) and period \(P(x)\).

**Exhaustive algorithm with exact coverage.** `verification/census_indegree.cpp` loops through every integer from zero to \(3^{14}-1\) exactly once, decodes its fourteen ternary digits, constructs the incidence relation from the cyclic Fano difference set, computes its successor, and increments the target indegree. It repeatedly removes indegree-zero vertices and records their removal order. No cycle vertex is removed: every cycle retains its incoming predecessor within the cycle. Conversely, each noncycle vertex lies in a finite tree feeding a directed cycle and must eventually be removed from the leaves inward. Thus the surviving vertices are precisely the directed cycles. Traversing each surviving cycle gives its **true least period**; reversing the removal order assigns \(T(x)=1+T(F(x))\) and \(P(x)=P(F(x))\) to every other state. These observations prove the classification algorithm's correctness independent of the numerical values it returns.

**Exact arithmetic and output.** The program uses integer-only state transitions, array indexing, indegree counts and cycle lengths. It exhaustively counts the fifty-five positive \((T,P)\)-classes. Its complete deterministic output is `verification/census_indegree.out`; the recovered joint counts are `verification/census.csv`. The counts sum to \(4782969\), the periodic counts sum to \(21099\), and the largest recorded entry time is ten. The eight orbit totals multiply by their respective periods to sum to \(21099\). The row \((T,P)=(10,4)\) has count \(12096\), and there are no other rows with \(T=10\). The stated functional identity and optimality follow from these exhaustive facts.

**Independent computational cross-check.** `verification/census_paths.cpp` instead starts trajectories from individual states, memoizes their first encounters or previously classified successors, and reconstructs each path's cycle and entry time. It uses a distinct explicit seven-line description of the Fano plane; its fifty-five class counts agree exactly with the indegree algorithm (`verification/census_paths.out`). `verification/witness_check.py` separately checks one complete primitive cycle of each claimed length and a ten-step preperiod ending on a four-cycle, stored in `verification/witnesses.json`. This second algorithm is corroboration; the finite proof relies on the fully enumerated transition map and the functional-graph argument above.

## Verification

From the extracted package root, run `python3 verification/replay.py`. This compiles both C++17 census implementations with integer-only arithmetic, reruns all \(4782969\) states independently by both methods, compares their full results with the embedded joint table and captured outputs, and rechecks explicit witness trajectories. Python 3 and a C++17 compiler are sufficient; no network, external data or third-party Python packages are required. The captured result is `REPLAY_PASS 4782969 states, 55 entrance classes, 8 periods, maximum entry 10`.

The finite graph specification, transition rule, source implementations, full table and trajectory witnesses are all embedded. Merely observing the sample orbits would establish existence only; nonexistence of other periods and larger transients follows from the exhaustive enumeration covering all \(3^{14}\) states.

## Relationship to prior work

The Greenberg--Hastings rule is classical. Gravner, Lyu and Sivakoff proved a general conservative-circulation criterion for synchronization and a formula for asymptotic activity on finite graphs; the 2016 preprint is the dated archival source. Doba independently studied deterministic graph Greenberg--Hastings dynamics and maximum cycle density. Those general qualitative results distinguish eventual quiescence from excitation and constrain activity, but do not enumerate the Heawood graph's fifty-five entry/period classes, give its precise ten-step maximal entry time, or count each primitive orbit. The Heawood graph's distinguished status as the fourteen-vertex cubic girth-six cage motivates the exact benchmark.

## Limitations

This is a finite exhaustive classification, not an analytic formula for a growing graph family. Its numerical totals require running or independently reconstructing the fully specified finite-state algorithms; sample certificates alone cannot exclude other orbits. Claims of previously unreported exact counts are based on searched and inspected literature and remain subject to unindexed earlier computations. No independent external mathematical audit has been performed. The result does not identify graph-automorphism orbits of configurations or classify other cellular-automaton rules.

## References

1. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first posted 2016-10-24); later Annals of Applied Probability **28** (2018), 3324--3357. https://arxiv.org/abs/1610.07320 ; https://doi.org/10.1214/17-AAP1350 .
2. N. Doba, *The Time Evolution of a Greenberg--Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101--126. https://doi.org/10.25088/ComplexSystems.27.2.101 .
3. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (1993). https://arxiv.org/abs/patt-sol/9303002 .
4. E. D. Lawrence and R. T. Wilson, *The Structure of the Heawood Graph*, arXiv:1907.11978 (2019), graph-theoretic background only. https://arxiv.org/abs/1907.11978 .
