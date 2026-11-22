# A sharp five-update majority clock and complete attraction basins on the Tietze graph

## Finding

On the twelve-vertex Tietze graph, synchronous binary open-neighbor strict-majority dynamics has exactly **16 fixed configurations** and **137 primitive temporal two-cycle orbits**. Every one of the \(2^{12}=4096\) labelled binary starting configurations first enters a periodic orbit within five synchronous updates, and the bound is sharp:

\[
F^{7}=F^{5},\qquad F^{6}\ne F^{4}.
\]

The complete first-periodic-entry census, stratified by eventual least temporal period, is:

| First periodic entry \(t\) | Eventual period one | Eventual period two | Total |
| ---: | ---: | ---: | ---: |
| 0 | 16 | 274 | 290 |
| 1 | 136 | 994 | 1130 |
| 2 | 492 | 708 | 1200 |
| 3 | 360 | 252 | 612 |
| 4 | 432 | 144 | 576 |
| 5 | 216 | 72 | 288 |
| **Total** | **1652** | **2444** | **4096** |

Moreover, every individual temporal-orbit basin is determined. The following entries \((s,c)\) mean that precisely \(c\) different temporal orbits have basin size \(s\), with their periodic states included:

| Least temporal period | Basin size \(s\) | Orbit multiplicity \(c\) |
| ---: | ---: | ---: |
| 1 | 2 | 12 |
| 1 | 38 | 2 |
| 1 | 776 | 2 |
| 2 | 2 | 6 |
| 2 | 4 | 12 |
| 2 | 6 | 18 |
| 2 | 8 | 36 |
| 2 | 12 | 18 |
| 2 | 14 | 18 |
| 2 | 40 | 18 |
| 2 | 70 | 6 |
| 2 | 76 | 5 |

The two unanimous fixed configurations each have basin size **776**. The graph has exactly twelve automorphisms; they merge the 16 fixed configurations into **six** spatial classes and the 137 primitive two-cycles into **29** spatial classes. All counts refer to indexed initial states, not configurations identified under graph symmetry or complementation.

## Assumptions and scope

Define the Tietze graph concretely by replacing one vertex of the Petersen graph with a triangle and attaching each triangle vertex to a distinct former neighbor. To fix all indices, use vertices \(\{0,1,\ldots,11\}\) and the following 18 undirected edges:

```
(0,1) (0,5) (0,9) (1,2) (1,6) (2,3)
(2,7) (3,8) (3,10) (4,6) (4,7) (4,11)
(5,7) (5,8) (6,8) (9,10) (9,11) (10,11)
```

Every vertex has exactly three neighbors. For \(x\in\{0,1\}^{12}\), the synchronous map \(F\) is defined componentwise by

\[
(F(x))_i=\begin{cases}1,&\displaystyle\sum_{j\in N(i)}x_j\ge2,\\0,&\text{otherwise}.\end{cases}
\]

There is no tie, self-vote, random update or asynchronous ordering. Each binary vector is encoded by the unique integer \(s=\sum_{i=0}^{11}2^i x_i\) between 0 and 4095. A primitive two-cycle is an unordered pair of distinct masks \(\{a,b\}\) satisfying \(F(a)=b\), \(F(b)=a\). A basin of an orbit is the set of all labelled initial masks whose trajectories eventually visit that orbit. First periodic entry is the smallest \(t\ge0\) for which \(F^t(x)\) is on a periodic orbit.

## Proof

**The state space and update are finite and exhaustive.** The displayed edge set specifies all three neighbors of each labelled vertex. `check_direct.py` computes each next state by independently testing the three bits at every vertex; it processes every integer mask from 0 to 4095. For each mask it follows the deterministic trajectory, recording the first index at which a state repeats. The portion before that repeat is the unique transient path, and the repeated suffix is the unique eventual periodic orbit. The code asserts that every suffix has length one or two, counts both the transient length and orbit length, and adds one initial configuration to that orbit's basin. Since all 4096 masks are visited and each path must eventually repeat in the finite state space, no configurations or orbits can be omitted.

**A second decomposition checks the entire classification.** `check_indegree.py` constructs the same graph by a different description: start with the standard outer-pentagon/inner-pentagram Petersen graph, remove its outer vertex zero, and attach three new triangle vertices to its old neighbors. This separately yields the stated 18-edge graph. It evaluates every next state using integer bit intersections and population counts (not the direct checker's three indexed votes). It then forms the whole 4096-vertex functional digraph, removes indegree-zero vertices iteratively, identifies every remaining cycle, and propagates orbit identities and distances backwards through the removed vertices. This establishes the same first-entry/period table and the same orbit-by-orbit basin histogram by a logically different enumeration. The scripts include explicit assertions of every published count and terminate with distinct pass markers only if they all hold.

**Sharpness and identities.** Direct iteration of the concrete mask 31 gives

\[
31\longmapsto198\longmapsto22\longmapsto192\longmapsto16\longmapsto0\longmapsto0.
\]

Thus mask 31 first enters its fixed-point orbit at update five. Both exhaustive decompositions find no transient longer than five and identify exactly 288 masks with first-entry time five. Since all eventual periods divide two and every entry time is at most five, \(F^7=F^5\) everywhere. Mask 31 has \(F^4(31)=16\) but \(F^6(31)=0\), so \(F^6\ne F^4\).

**Individual basins and arithmetic checks.** The two algorithms group all 4096 initial masks by their terminal orbit. They independently obtain the basin histogram displayed above. The fixed-basin weighted sum is \(12\cdot2+2\cdot38+2\cdot776=1652\), and the two-cycle-basin weighted sum is \(6\cdot2+12\cdot4+18\cdot6+36\cdot8+18\cdot12+18\cdot14+18\cdot40+6\cdot70+5\cdot76=2444\). These total 4096. Their basin multiplicities sum to 16 fixed and 137 two-cyclic orbits, giving 290 immediately periodic masks.

**Spatial symmetries.** `check_symmetry.py` verifies that the three vertices numbered 9, 10 and 11 form the graph's unique triangle. Every graph automorphism must permute this triangle; its mapping then forces the three external neighbors, while all six remaining vertices are exhaustively permuted. Testing edge preservation across these \(6\cdot6!\) candidates produces exactly twelve automorphisms, all checked. Each automorphism is independently checked to commute with the majority update on all 4096 states. Applying those twelve permutations to every fixed state and every unordered temporal two-cycle gives precisely six and 29 spatial classes.

The three complete, reproducible standard-library certificates together prove the finite claims without sampling graph sizes or inferring global behavior from observed trajectories of a proper subset of states.

## Verification

From a directory containing the packaged scripts, run:

```
python3 check_direct.py
python3 check_indegree.py
python3 check_symmetry.py
```

Compare their complete terminal outputs with `direct_output.txt`, `indegree_output.txt` and `symmetry_output.txt`. The first checker independently follows 4096 whole trajectories, the second constructs a complete transition table and peels the functional graph by indegrees, and the third exhaustively determines the graph automorphism group and recurrent spatial orbit classes. All three use only the Python standard library. Each contains its own positive-count assertions; the second and third also check the whole set of map identities or equivariances claimed here. The graph is indexed by the explicit edge list, not by an unverified drawing. The execution of these exact finite enumeration algorithms is the computational part of the proof, with complete source included rather than only a reported run log.

## Relationship to prior work

The general eventual-period-at-most-two theorem for synchronous finite symmetric threshold maps is classical (Goles and Olivos, 1980); neither that theorem nor the later study by Benjamini and collaborators (first posted 2014-05-11) gives the present exact finite basins, settling time or symmetry classes. The Tietze graph itself, a canonical twelve-vertex cubic non-Hamiltonian graph obtained by inflating one Petersen vertex into a triangle, is standard and is not a newly introduced graph. MathWorld and earlier graph-theory literature describe its structure.

A published exact majority classification on the Petersen graph, with 14 fixed states, 55 primitive two-cycles and a sharp four-step entry, concerns the ten-vertex graph *before* the triangle inflation. The expansion changes the local vote structure, and the Petersen result does not imply the displayed 4096-state classification. Published work on Tietze's perfect-matching complex concerns topology and group actions on a simplicial complex, not the binary majority map or its attraction basins. Other exact published cubic-graph majority censuses address different underlying graphs. These comparisons establish differences of hypotheses and conclusions, not an absolute proof of historical priority.

## Limitations

This result concerns exactly the specified Tietze graph and synchronous binary strict-open-neighbor-majority rule. It is not a theorem for all cubic non-Hamiltonian graphs, all triangle-inflated graphs, other thresholds, or random initial conditions with nonuniform weights. Counts are complete for the finite labelled state space; no infinite-family generalization is claimed. The numerical classification is supported by included exhaustive programs and an explicit sharp witness, but no independent external mathematical audit has yet occurred. An equivalent unindexed earlier finite computation may exist.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11, https://arxiv.org/abs/1405.2486 .
3. E. W. Weisstein, *Tietze's Graph*, MathWorld, https://mathworld.wolfram.com/TietzesGraph.html .
4. *A four-step Petersen majority projection and the Desargues double-cover basin spectrum*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-four-step-petersen-majority-projection-and-the-desargues-doubl--b8bcbb0b4dff .
5. *The Tietze perfect-matching complex: six circles and its full rational symmetry character*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-tietze-perfect-matching-complex-six-circles-and-its-full-rat--66b3f7013d3d .
