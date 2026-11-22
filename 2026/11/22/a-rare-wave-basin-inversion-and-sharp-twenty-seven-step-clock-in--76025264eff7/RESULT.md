# A rare-wave basin inversion and sharp twenty-seven-step clock in four-state Frucht excitation

## Finding

For synchronous threshold-one four-state Greenberg–Hastings (GH) excitation on the canonically labelled twelve-vertex Frucht graph, all \(4^{12}=16{,}777{,}216\) initial configurations are classified by eventual least temporal period and first entry time. The **complete** periodic-orbit and attracting-population census is:

| Least period \(p\) | Primitive temporal orbits | Periodic configurations | Initial configurations in their basins | Maximum entry time |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 6,520,408 | 9 |
| 4 | 1,024 | 4,096 | 3,302,146 | 27 |
| 5 | 10 | 50 | 5,168,039 | 17 |
| 6 | 2 | 12 | 1,786,623 | 15 |

The period-five waves exhibit a basin inversion: there are only ten primitive five-cycles versus 1,024 primitive four-cycles, yet **every individual five-cycle attracts more initial states than every individual four-cycle**. The ten five-cycle basin populations, in increasing order, are

\[385193,\ 412210,\ 415203,\ 438221,\ 447904,\ 538807,\ 549118,\ 635632,\ 672639,\ 673112.\]

The 1,024 four-cycle basins range from \(9\) to \(373631\) initial states, establishing the strict separation \(385193>373631\). The two six-cycle basins have sizes \(880674\) and \(905949\). The sole fixed state is the all-rest configuration, attracting \(6520408\) initial states.

The sharp first-periodic-entry time is \(27\) updates, attained by exactly \(18\) initial states, each entering a four-cycle. In particular, the finite-state map satisfies \(F^{87}=F^{27}\), and no smaller uniform entry-time bound than \(27\) is possible. The complete \(72\)-cell entrance-time/period histogram is provided in `joint_census.csv`.

## Assumptions and scope

The undirected graph has vertex set \(\{0,1,\ldots,11\}\) and precisely the eighteen edges

```text
(0,1) (0,6) (0,7) (1,2) (1,7) (2,3)
(2,8) (3,4) (3,9) (4,5) (4,9) (5,6)
(5,10) (6,10) (7,11) (8,9) (8,11) (10,11)
```

It is isomorphic to the Frucht graph with LCF offsets `(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)`. An explicit relabelling, from this edge-list order to the LCF order, is `(5,3,2,1,0,7,6,4,10,11,8,9)`; `verify_graph_witness.py` checks that it maps all eighteen edges bijectively.

Each vertex has a state in \(\{0,1,2,3\}\). At each *simultaneous* update, states \(1\), \(2\), \(3\) automatically advance to \(2\), \(3\), \(0\), respectively. State \(0\) advances to \(1\) if and only if at least one adjacent vertex is currently in state \(1\); otherwise state \(0\) remains at rest. There are no random updates or boundary conventions.

A configuration \(x=(c_0,\ldots,c_{11})\) is encoded injectively by \(\sum_{i=0}^{11}c_i4^i\), equivalently the integer with the twelve two-bit digits in vertex order. Let \(\tau(x)\) be the smallest nonnegative time when the trajectory first lies on a genuine directed cycle. Let \(p(x)\) denote that eventual cycle's **least** period. Thus \(\tau(x)=0\) for states initially on a cycle. Each *primitive temporal orbit* is a directed cycle, counting its phase states once.

## Proof

The state set has exactly \(4^{12}\) distinct elements, whose integer encodings are \(0,1,\ldots,2^{24}-1\). Each transition is explicitly specified by the displayed graph and deterministic rule; hence the functional digraph has precisely one outgoing arc from each state.

**Exhaustive finite certificate A.** The standalone `frucht4_a.cpp` constructs this transition for all \(2^{24}\) encodings. It first computes incoming degrees and repeatedly removes zero-indegree nodes. In a finite functional digraph, this process deletes precisely the transient states, leaving a disjoint union of genuine directed cycles. Traversing the surviving cycles computes their exact lengths and assigns distinct orbit identifiers. Traversing the deleted states in reverse removal order then computes their first periodic-entry time and eventual orbit identifier using the rigorous recursions \(\tau(x)=1+\tau(F(x))\) and \(p(x)=p(F(x))\). Counting every initial state exactly once yields the table, individual basin sizes, and complete `joint_census.csv`.

**Independent finite certificate B.** The standalone `frucht4_b.cpp` constructs the graph independently from the twelve Hamiltonian/LCF offsets, evolves configurations by decomposing the base-four word into digits, and uses a direct path-marking algorithm to find every first repeated state. The loop segment between a state's first occurrence and its return is its exact primitive cycle; reverse-path propagation calculates entry times, periods, and orbit basins for all states. The algorithms use different graph representations, state-update implementations, and functional-graph decompositions, yet agree on the complete \(72\)-cell entrance/period census and sorted individual basin sizes.

The finite enumeration proves that exactly the four periods in the displayed table occur, and their orbit counts sum to \(1037\), with \(4159\) periodic configurations. The four attraction-basin totals sum to \(16{,}777{,}216\), verifying that every state is accounted for. In particular, the smallest five-cycle basin is \(385193\), while the largest four-cycle basin is \(373631\), proving the stated individual-basin inversion rather than merely comparing totals.

The maximum first-entry cell is \((\tau,p)=(27,4)\), with population \(18\), and every cell with larger \(\tau\) is empty. The explicit integer-encoded initial state \(5999879\) reaches a primitive four-cycle at the first time \(27\), with its phase-zero periodic state encoded by \(3222501\); a separate trajectory-based witness check verifies the exact first-repetition time and cycle length. The least common multiple of the four observed periods is \(60\), so first entry by time \(27\) implies \(F^{87}=F^{27}\), while the witness proves sharpness of the entry-time bound. This proof is an exhaustive finite algorithmic proof on the specified graph; no extrapolation from small samples or unverified all-size induction is used.

## Verification

Using a C++17 compiler and Python 3, from this directory run:

```sh
g++ -std=c++17 -O3 frucht4_a.cpp -o frucht4_a
./frucht4_a > frucht4_a.replayed.out
g++ -std=c++17 -O3 frucht4_b.cpp -o frucht4_b
./frucht4_b > frucht4_b.replayed.out
python3 verify_graph_witness.py
python3 verify_census.py
```

`frucht4_a.out` and `frucht4_b.out` contain the reference results. The relevant sections `ORBITCOUNTS`, `MAX_STATES`, `BASIN_SIZES_BY_PERIOD`, and `HIST` must match across both implementations; each program enumerates all states independently, rather than loading the other's results. The histogram in `joint_census.csv` is extracted from the first output and checked against the second by `verify_census.py`, which also tests exact state/period sums, sharpness and the basin separation. The independent small witness script checks the graph relabelling and one explicitly maximal transient. The calculations depend only on the two source files, a standard C++17 compiler and Python 3, with no external network or database.

## Relationship to prior work

Fisch, Gravner and Griffeath (1991; first day-verified arXiv release 1993-04-02) describe four-state and more general Greenberg–Hastings rules on predominantly planar lattice domains, their periodic-wave organization, and parameter regimes; their rule definition is compatible with the present finite graph. Their analysis does not report the Frucht-graph labelled functional-graph, period, or individual-basin census. Durrett and Griffeath's arXiv manuscript released 1993-03-22 studies asymptotic excitable cellular automata and spiral thresholds, not this twelve-vertex finite classification. Gravner, Lyu and Sivakoff (2016) give synchronization and rate descriptions on arbitrary graphs explicitly for *three-color* GHM; their results do not imply four-color Frucht orbit counts or the sharp transient.

A publicly available three-state Frucht-graph census reports a twenty-one-step sharp transient, recurrent periods \(1,3,4,5,6,7,8\), and a different labelled basin census; changing the refractory-state count changes the actual phase space and the map. The published four-state Chvátal-graph census has 29,602 primitive four-cycles and no five/six-cycles, with sharp entry time twelve; that is a different 12-vertex graph and cannot imply the present values. The finite computations here complement these related results without claiming discovery of the graph, model, or general finite-state classification principle.

## Limitations

This is an exact, reproducible finite-state result for one canonical graph and one precisely specified four-state deterministic rule. It makes no claim about all asymmetric cubic graphs, universal monotonicity as the color count varies, or generic convergence-time bounds. Agreement of two different exhaustive programs substantially checks implementation error but is not independent mathematical certification. Earlier unindexed finite enumerations or inaccessible historical material remain an originality risk; independent external audit has not been conducted.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (first posted 1993-03-22), https://arxiv.org/abs/patt-sol/9303002 .
2. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, *Statistics and Computing* **1** (1991), 23–39; day-verified arXiv version 1993-04-02, https://arxiv.org/abs/patt-sol/9304001 ; lawful author copy https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf .
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (first posted 2016-10-24), https://arxiv.org/abs/1610.07320 .
4. E. W. Weisstein, *Frucht Graph*, MathWorld, https://mathworld.wolfram.com/FruchtGraph.html .
5. *A twenty-one-step excitation transient on the asymmetric Frucht graph*, published finite-graph research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-twenty-one-step-excitation-transient-on-the-asymmetric-frucht--7b215d08f374 .
6. *Four-state Chvátal excitation: period collapse and six extremal symmetry classes*, published finite-graph research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-four-state-chv-tal-excitation-period-collapse-and-six-extremal-s--924e4654e069 .
