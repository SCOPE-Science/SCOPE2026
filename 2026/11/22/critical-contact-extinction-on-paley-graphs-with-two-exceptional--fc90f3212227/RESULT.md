# Exact attraction basins and entry times on the two exceptional Paley graphs

## Finding

Run synchronous three-state Greenberg–Hastings excitation on the Paley graphs \(P(5)\) and \(P(9)\), at exactly half the graph degree. On \(P(5)\), each of the two primitive five-cycles attracts 45 labelled configurations, including its five states; the all-rest basin has size 153. On \(P(9)\), each of the four primitive three-cycles attracts only its own three states, and the other 19,671 configurations flow to rest. Thus the two graphs both support recurrent waves, but only the five-vertex graph has wave basins containing transient states. The sharp first-periodic-entry cutoffs are four and five updates, respectively.

| First periodic entry \(t\) | \(P(5)\), eventual rest | \(P(5)\), period five | \(P(9)\), eventual rest | \(P(9)\), period three |
|---:|---:|---:|---:|---:|
| 0 | 1 | 10 | 1 | 12 |
| 1 | 31 | 30 | 511 | 0 |
| 2 | 51 | 40 | 5641 | 0 |
| 3 | 40 | 10 | 9990 | 0 |
| 4 | 30 | 0 | 3438 | 0 |
| 5 | 0 | 0 | 90 | 0 |
| **Total** | **153** | **90** | **19671** | **12** |

## Assumptions and scope

The Paley graph of order \(q\) has vertex set \(\mathbb F_q\); distinct vertices are adjacent if their difference is a square. At each update, states 1 and 2 advance to 2 and 0, respectively. A resting vertex (state 0) enters state 1 if and only if at least \((q-1)/4\) of its neighbors were excited (state 1) before the update. This is one contact for \(P(5)\) and two for \(P(9)\). A primitive cycle has least temporal period equal to its stated period. Entry time is zero for an already recurrent configuration. The census is labelled; no spatial identifications are made.

## Proof and reproducibility

The square differences in \(\mathbb F_5\) are \(\pm1\), giving a pentagon. Writing \(\mathbb F_9=\mathbb F_3[i]\) with \(i^2=-1\), the four nonzero squares are \(\pm1,\pm i\); thus the nine-vertex graph has row and column edges on a three-by-three grid.

An exhaustive classification follows by listing every ternary assignment on each graph and computing its unique successor by the stated update. In a finite functional graph, the suffix between a state's first and second appearances is the temporal cycle if the path is stopped at its first repetition. The length of the prefix before that suffix is precisely the first-periodic-entry time. Using the least state encoding on a cycle as its identifier permits counts separately for each cycle, not just each period. In a memoized implementation an already classified state can be used as a stopping point, inheriting its cycle identifier and adding its known entry time to the path length. On paths ending in a new cycle, first assign entry zero to the members of the cycle and then propagate distances backward, adding one per predecessor.

The full base-three implementation `verify_forward.py` constructs the complete successor arrays of sizes \(243\) and \(19683\) and uses that memoized procedure. The separate tuple implementation `verify_independent.py` generates the row/column or cycle edges, follows each labelled assignment until its first repeated state, and computes entry times and per-cycle basin sizes. The outputs `forward.out` and `independent.out` give all the counts in the table; checking the counts at the largest nonempty times establishes sharpness. Both programs require only Python 3's standard library.

There is also a direct reason the nonzero basins on the grid cannot have transient states. Each order-three Latin square, viewed as a state assignment, rotates its three colors at every step: every vertex has exactly two neighbors of each other color. These are 12 distinct states (six first rows and two choices for each second row, with the third forced), accounting for all nonzero recurrent states in the census. In any predecessor of such a state, vertices of target colors 1 and 2 have forced prior colors 0 and 1, respectively. A vertex of target color 0 already has two neighbors of target color 2, which were previously excited. It could not have been resting, since that would have caused excitation. Thus its prior color was 2. This forces the predecessor to be the other Latin-square phase, and excludes any transient first step into a wave cycle.

## Relationship to prior work and limitations

The contribution is the exact attraction and entry-time census, not the all-order dichotomy for existence of waves or the characterization of balanced period-three colorings. The general triangle-locking theorem [1] already supplies the latter characterization for recurrent configurations on every triangle-covered connected graph at rounded half-degree. In a Paley graph of order \(q\ge9\), every vertex belongs to a triangle, since adjacent pairs have \((q-5)/4>0\) common neighbors. A balanced three-coloring on a Paley graph would give an adjacency eigenvalue \(-\theta\), where \(\theta=(q-1)/4\): assign the three cube roots of unity to its color classes, and use the \(\theta\) neighbors of each other color at every vertex. For \(q\ge13\) neither of the nonprincipal eigenvalues \((-1\pm\sqrt q)/2\) equals \(-\theta\). Thus the all-order exclusion for \(q\ge13\) follows directly from the general theorem. It gives no transient census. The earlier half-degree rigidity theorem [2] already characterizes states initially on a primitive three-cycle and, on the nine-vertex grid, gives the Latin-square wave criterion. Threshold-one graph results [3,4] give recurrence and activity criteria that apply to the pentagon's update; they do not extend unchanged to the threshold-two grid or supply the two period-resolved labelled entry tables here.

Only the basin and entry-time counts for orders five and nine are claimed. No general relaxation bound for larger graphs or for other thresholds follows. An earlier equivalent finite census outside the cited sources could change the priority assessment.

## References

1. *Triangle-locked critical excitation and the Johnson-graph extinction dichotomy*, [Finding and proof](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-triangle-locked-critical-excitation-and-the-johnson-graph-extinc--76b9562220e5/RESULT.md).
2. *Half-degree rigidity and a sharp contact-threshold collapse on squared cycles*, [Finding and proof](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-half-degree-rigidity-and-a-sharp-contact-threshold-collapse-on-s--7c3fe196f42d/RESULT.md).
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, [arXiv:1610.07320](https://arxiv.org/abs/1610.07320).
4. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, *Complex Systems* 27 (2018), [doi:10.25088/ComplexSystems.27.2.101](https://doi.org/10.25088/ComplexSystems.27.2.101).
5. A. N. Elsawy, *Paley Graphs and Their Generalizations*, [arXiv:1203.1818](https://arxiv.org/abs/1203.1818), for the strongly regular parameters and spectrum.
