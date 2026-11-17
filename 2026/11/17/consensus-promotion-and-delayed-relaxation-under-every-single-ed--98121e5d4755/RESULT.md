# Consensus promotion and delayed relaxation under every single-edge deletion of the Chvátal graph

## Finding

For synchronous binary strict-neighbor-majority dynamics with incumbent-tie retention on the twelve-vertex Chvátal graph, deleting **any one** of its 24 edges strictly enlarges the attraction basin of the two unanimous equilibria, although the maximum transient may increase from seven to eleven steps. The complete 25-map finite-state classification has five distinct edge-deletion classes under the eight automorphisms of the original graph.

For each graph, the ordered census below records: number of fixed configurations; number of primitive period-two **orbits** (each orbit has two phase states); maximum entrance time to periodicity; number of initial states attaining that maximum; and number of initial states eventually reaching unanimity (of \(2^{12}=4096\) initial states).

| Deleted edge (representative) | Orbit multiplicity | Fixed | Two-cycle orbits | Sharp entrance time | Maximally delayed inputs | Unanimity basin | Change in unanimity basin |
|---|---:|---:|---:|---:|---:|---:|---:|
| none | 1 | 234 | 136 | 7 | 32 | 2906 | 0 |
| (0,1) | 4 | 118 | 82 | 11 | 24 | 3164 | +258 |
| (0,6) | 8 | 130 | 106 | 8 | 2 | 3094 | +188 |
| (2,3) | 4 | 126 | 118 | 7 | 20 | 3032 | +126 |
| (2,6) | 4 | 106 | 78 | 7 | 8 | 2996 | +90 |
| (2,8) | 4 | 144 | 128 | 8 | 4 | 3080 | +174 |

In particular all 24 single-edge deletions strictly reduce the number of fixed states and period-two orbits while strictly increasing the two-consensus basin. The effects are not consequences of a general edge-deletion monotonicity law (see Limitations).

## Assumptions and scope

Vertices are labelled \(0,1,\ldots,11\). The undirected edge set is specified exactly by the following sorted vertex pairs, without multiple edges:

```
(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),
(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),
(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11)
```

This is the standard Chvátal graph: the supplied checker verifies twelve vertices, twenty-four edges, degree four, no triangles and chromatic number four. It exhaustively computes all eight label-permutation automorphisms.

For a binary state \(x\in\{0,1\}^{12}\), the synchronous map \(F_G\) satisfies, for each vertex \(i\), with \(d_i\) its degree and \(s_i=\sum_{j\sim i}x_j\),

\[
(F_G(x))_i=\begin{cases}1,&2s_i>d_i,\\0,&2s_i<d_i,\\x_i,&2s_i=d_i.\end{cases}
\]

The initial time is \(t=0\); the entrance time is the least \(t\ge0\) for which \(F_G^t(x)\) is periodic, without counting the next transition. The *unanimity basin* is the set of initial states eventually reaching either all-zero or all-one, not the full basin of every fixed state.

## Proof

This is a finite exhaustive proof with two independent executable implementations, not an inference from sampled trajectories. Each of the \(25\) graphs has exactly \(4096\) labelled binary states; there is no other parameter range in the statement.

**Step 1: reduction to five deletions.** Enumerate all adjacency-preserving permutations by extending an injective partial vertex map and checking adjacency and nonadjacency against already mapped vertices. This finite backtracking visits all possibilities; the final complete permutations are exactly eight. Their action on the 24 edges partitions edges into orbits with representatives and sizes \((0,1):4\), \((0,6):8\), \((2,3):4\), \((2,6):4\), and \((2,8):4\). An automorphism conjugates the respective majority functional graphs upon deleting edges in the same orbit. The complete checked 24-deletion enumeration independently reproduces each class multiplicity.

**Step 2: exhaustive transition maps.** Encode a binary state as the twelve-bit integer \(x=\sum_{i=0}^{11}x_i2^i\). For each intact or edge-deleted graph, compute the exact deterministic majority image of each integer from \(0\) through \(4095\) using the displayed local rule and integer bit counts. This constructs the complete map, not a subset of inputs.

**Step 3: classify the functional graphs.** One implementation follows all successor paths, detects and marks directed cycles, then propagates entrance depths and eventual periods backwards. A separate C++ implementation computes the indegree of every state, removes nonperiodic states with the zero-indegree queue, classifies all remaining cycles, and then reconstructs entrance depths in reverse elimination order. Both reject any encountered least period exceeding two and verify that their partition covers all \(4096\) states. The tables above are the resulting exact integer sums. Each two-cycle is counted as one orbit, hence its two phase states are halved.

**Step 4: verify the sharp clocks.** The largest entrance depths and numbers of attaining states are read from the complete depth arrays, so no longer paths are unexamined. For the edge \((0,1)\), one eleven-step witness begins at integer-coded state \(496\); the complete sequence through the first periodic state is

```
496,3347,1008,3355,1012,3359,1020,3487,1022,3519,4094,4095
```

The last state is the all-one equilibrium. Both checkers report maximum depth eleven in this class and at most eleven across all deletions.

**Step 5: conclude the strict inequalities.** The five positive census differences are \(258,188,126,90,174\). Since the five automorphism orbits partition all 24 edges, every deletion strictly enlarges the unanimity basin. The same exact table gives the reductions in the counts of both fixed states and primitive two-cycle orbits.

## Verification

Run `python3 check_chvatal.py` and `g++ -std=c++17 -O2 check_chvatal.cpp -o check_chvatal && ./check_chvatal` from the directory containing these two standalone source files. `python_output.txt` and `cpp_output.txt` record their actual independently obtained outputs. The Python implementation additionally verifies the graph is four-chromatic, independently enumerates the automorphism group and recovers the base-graph first-entry histogram. The C++ implementation counts all 25 transition maps by an algorithmically different approach. Neither checker reads the other's outputs or needs third-party modules.

For the original graph, the full number of initial states with first periodic entry at depth \(t\), partitioned by eventual periods one and two, is:

| \(t\) | Period one | Period two |
|---:|---:|---:|
| 0 | 234 | 272 |
| 1 | 754 | 80 |
| 2 | 1764 | 16 |
| 3 | 640 | 0 |
| 4 | 136 | 0 |
| 5 | 136 | 0 |
| 6 | 32 | 0 |
| 7 | 32 | 0 |

The two unanimity basins each have size \(1453\), totalling \(2906\).

## Relationship to prior work

Chvátal introduced this minimal triangle-free four-chromatic quartic graph. Goles and Olivos proved the general eventual fixed-point-or-two-cycle phenomenon for symmetric Boolean threshold dynamics; that theorem alone provides none of these specific orbit, basin or sharp transient numbers. Björklund and coauthors explicitly tabulated the Chvátal graph's Tutte polynomial, a distinct graph invariant, in an accessible full-text appendix (arXiv:0711.2585, Appendix D.3). Related indexed exact research treats *three-state excitation* on the Chvátal graph, which has a different state alphabet and local update from binary majority, and treats majority on other graphs. These results do not imply the stated complete deletion census. Historical precedence beyond the inspected sources remains uncertain.

## Limitations

This theorem concerns exactly the displayed labelled twelve-vertex graph, its 24 individual one-edge deletions, and synchronous deterministic tie-retaining majority; it does not claim an all-graph monotonicity theorem. For example, removing an edge from the triangle can reduce its unanimity basin: the triangle's eight binary states all reach unanimity, while the three-vertex path admits a two-cycle between the nonunanimous states \(010\) and \(101\). An unindexed prior calculation of the Chvátal-specific numbers might exist. The result is an exhaustive finite classification rather than a large-graph asymptotic theorem. Independent mathematical audit has not occurred.

## References

1. V. Chvátal, “The smallest triangle-free 4-chromatic 4-regular graph,” *Journal of Combinatorial Theory* **9** (1970), 93–94. DOI: 10.1016/S0021-9800(70)80057-6.
2. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* **30** (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
3. A. Björklund, T. Husfeldt, P. Kaski, and M. Koivisto, “Computing the Tutte polynomial in vertex-exponential time,” arXiv:0711.2585, initially submitted 2007-11-16. Full text: https://arxiv.org/html/0711.2585v4, Appendix D.3.
