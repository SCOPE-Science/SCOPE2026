# Exact agreement of cyclic and refractory period selection on the Chvátal graph

## Finding

Let \(G\) be the labelled twelve-vertex Chvátal graph specified in the edge list below. For every one of the \(3^{12}=531441\) labelled three-color initial configurations \(x\), synchronous three-color cyclic cellular-automaton dynamics (CCA) and synchronous threshold-one three-state Greenberg–Hastings dynamics (GHM), both initialized at \(x\), have **exactly the same eventual least temporal period**. The only possible periods are \(1,3,4,7,10,11\).

The complete initial-state period census is:

| Eventual least period | Matched initial states | CCA primitive orbits | GHM primitive orbits |
|---:|---:|---:|---:|
| 1 | 24,249 | 3 | 1 |
| 3 | 134,184 | 4,768 | 4,768 |
| 4 | 183,108 | 882 | 294 |
| 7 | 159,876 | 3,036 | 1,012 |
| 10 | 28,344 | 1,512 | 504 |
| 11 | 1,680 | 48 | 8 |

CCA reaches its eventual cycle within a sharp eight updates, with exactly 192 configurations attaining this entry time. GHM reaches its eventual cycle within a sharp ten updates, with exactly 64 configurations attaining this time. Thus matched **outcome period** does not mean matched **relaxation time or recurrent-orbit population**.

## Assumptions and scope

The vertex set is \(\{0,1,\ldots,11\}\), and the 24 undirected edges are:

```text
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7)
(2,3) (2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8)
(5,10) (5,11) (6,10) (6,11) (7,8) (7,11)
(8,10) (9,10) (9,11)
```

All updates are synchronous, use **open neighborhoods**, and have states \(0,1,2\). In CCA, a vertex in color \(a\) advances to \(a+1\pmod3\) if any neighbor has the successor color, and otherwise retains \(a\). In GHM, \(1\to2\), \(2\to0\) unconditionally, and \(0\to1\) precisely when some neighbor is excited (color 1); otherwise \(0\to0\). There is no stochastic assumption. The eventual least period of a state is the smallest positive period on its eventual recurrent orbit; its first periodic-entry time is the least nonnegative iterate already belonging to that orbit.

These are exact **finite-graph** statements, not assertions for all triangle-free or four-regular graphs. No statement about uniqueness of the Chvátal graph's period-concordance property is made.

## Proof

The proof is a complete finite-state enumeration with two algorithms using different representations of the transition and eventual periodicity; both are included as independently executable source files.

Encode each initial coloring bijectively as the integer \(s=\sum_{i=0}^{11}3^i x_i\), \(0\le s<531441\). The explicit 24-edge list determines the four-element neighborhood of every vertex and hence uniquely determines both successor maps \(F_C,F_H\). In `verify.cpp`, `next_state` extracts every base-three digit, applies the stated local rule, and returns the successor's base-three integer. For each of the exactly 531441 states, form its successor and increment the indegree of that successor. Repeatedly remove every indegree-zero vertex from the resulting directed functional graph. This process exhausts the nonrecurrent states because every finite functional graph consists of disjoint directed cycles with in-trees; precisely the cycle vertices remain. Walk every remaining cycle to determine its least period, then traverse the removed vertices in reverse deletion order, propagating the successor's period and increasing its entry time by one. This assigns **one and only one** entry time and eventual least period to every state. Counting cycles gives the orbit columns of the table; counting states by their eventual period gives its initial-state column. The code asserts that the two period values agree separately for every state, not just in aggregate. It also asserts the exact extremal entry times and their populations.

Independently, `verify.py` constructs the same successor maps by vectorized trit arrays and neighbor predicates. For each update rule and each input it materializes consecutive actual iterates through step 24. The first pair \((t,p)\), ordered by increasing \(t\) then positive \(p\), satisfying \(F^{t+p}(s)=F^t(s)\) with \(0\le t\le12\), \(1\le p\le12\), is the true entry time and least period: equality forces the orbit to repeat, and the search visits all smaller entries and periods first. All 531441 inputs are found within these ranges. Their period counts and orbit counts equal those from the functional-graph algorithm. The cross-rule comparison finds **zero mismatches**. This procedure does not assume a priori that the period list is complete; it directly tests all periods 1 through 12.

Consequently all claimed counts and bounds are finite integer identities verified exhaustively on the explicitly supplied domain. No extrapolation from a proper sample is used.

## Verification

`verify.cpp` is a standalone C++17 program with no nonstandard dependencies. A reproducible invocation is `g++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. `verify.py` is an independent NumPy implementation (tested with NumPy 2.x); invoke `python verify.py`. Both must report the listed primitive-orbit counts, matching period populations, maximum entry times, and zero period mismatches. `JOINT_CENSUS.csv` gives all 165 nonzero cells of the joint first-entry-time/period table; its weights total \(531441\). The program code and graph edge list, rather than a precomputed log, are the actual finite proof certificates.

## Relationship to prior work

Chvátal's 1970 graph is a canonical smallest triangle-free, four-chromatic, four-regular example. Fisch, Gravner and Griffeath (1993) study the broader class of cyclic and refractory excitable automata. Gravner, Lyu and Sivakoff (2016), in their definitions and Theorem 3, prove a general characterization of synchronization and activity on finite graphs, not a Chvátal-specific equality of every initial state's **least temporal period**, nor these orbit and entry-time populations. Previously indexed same-graph work gives the GHM-only period and entrance-time census; that alone does not determine the CCA map at each initial coloring. An existing general comparison of excitation clocks gives period divisibility, which likewise does not imply equality. Indexed same-initial-state comparisons on the Petersen, Frucht and Heawood graphs show that strict period division can actually occur, so equality on the Chvátal graph is not a universal formal consequence of sharing the initial colors.

## Limitations

The result is a computer-assisted **exhaustive theorem about one fixed finite graph**, not a structural classification of graphs on which CCA and GHM select equal periods. Although two algorithmically different checkers agree, neither check is an independent external mathematical audit. The full text of some indexed same-graph and same-model research records could not be inspected from the search interface; this leaves historical-priority risk for an earlier equivalent joint classification. The material reviewed did not establish such prior coverage. A graph relabelling preserves the conclusions, but the certificate uses exactly the supplied labels.

## References

- V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, Journal of Combinatorial Theory **9** (1970), 93–94, DOI: 10.1016/S0021-9800(70)80057-6.
- R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata*, arXiv:patt-sol/9304001 (first publicly posted 1993-04-02), https://arxiv.org/abs/patt-sol/9304001.
- J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016-10-24), https://arxiv.org/abs/1610.07320.
