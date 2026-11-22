# Mixed-period cyclic dominance on the cuboctahedron at critical two-contact threshold

## Finding

Consider the cuboctahedral graph \(G=L(Q_3)\), the line graph of the ordinary three-dimensional cube. Every vertex of \(G\) has degree four. On three-color states \(x\in\{0,1,2\}^{V(G)}\), consider two synchronous maps at contact threshold two:

* Cyclic cellular automaton (CCA): a vertex of color \(c\) becomes \(c+1\pmod 3\) if at least two neighbors have color \(c+1\pmod 3\); otherwise it retains \(c\).
* Three-state Greenberg–Hastings map (GHM): a vertex of color zero becomes one if at least two neighbors have color one; otherwise it remains zero. Vertices of colors one and two become two and zero, respectively, regardless of their neighbors.

For **all** \(3^{12}=531441\) labelled common initial states, the eventual least periods and their joint populations are exactly:

| CCA least period | GHM least period | Initial states |
|---:|---:|---:|
| 1 | 1 | 512505 |
| 3 | 3 | 24 |
| 6 | 1 | 48 |
| 8 | 1 | 15984 |
| 12 | 1 | 2880 |

There are no other joint period classes. Thus precisely \(18912\) initial states have different eventual least periods. CCA has \(18936\) oscillatory initial states, whereas GHM has only \(24\): a factor of \(789\) in attraction probability under uniform initial states. The GHM oscillating states coincide exactly with the CCA period-three states.

The complete temporal-orbit and attraction-basin census is:

| Rule | Least period | Number of temporal orbits | Basin sizes and multiplicities |
|---|---:|---:|---|
| CCA | 1 | 81 | 18 of size 116; 36 of size 1300; 24 of size 4989; 3 of size 114627 |
| CCA | 3 | 8 | 8 of size 3 |
| CCA | 6 | 8 | 8 of size 6 |
| CCA | 8 | 36 | 18 of size 416; 18 of size 472 |
| CCA | 12 | 8 | 8 of size 360 |
| GHM | 1 | 1 | 1 of size 531417 |
| GHM | 3 | 8 | 8 of size 3 |

A basin counts every starting state whose forward orbit eventually enters that particular *temporal* orbit, including the orbit's own states. In particular every CCA primitive three-cycle and six-cycle is isolated from transient predecessors, while all CCA primitive eight- and twelve-cycles have nontrivial transient basins.

The first periodic-entry time is at most eight for CCA (attained by \(72\) initial states) and at most six for GHM (attained by \(72\) initial states), both sharp. Consequently their global map identities include

\[
F_{\mathrm{CCA}}^{32}=F_{\mathrm{CCA}}^8,\qquad
F_{\mathrm{GHM}}^{9}=F_{\mathrm{GHM}}^6.
\]

Under the 48 cube isometries inducing vertex permutations on \(L(Q_3)\) and the global cyclic color shifts that commute with CCA, the CCA periodic orbits form exactly ten geometric/color classes. Their \((\text{period},\text{class-size})\) pairs are \((1,3),(1,18),(1,24),(1,36),(3,2),(3,6),(6,8),(8,18),(8,18),(12,8)\). Class size counts temporal orbits, not states. The two eight-cycle classes have distinct individual basin sizes, 416 and 472.

## Assumptions and scope

Let the vertices of the cube be integers \(0,1,\dots,7\), with integers adjacent if their binary encodings differ in exactly one bit. Label the twelve edges lexicographically as

```
(0,1) (0,2) (0,4) (1,3) (1,5) (2,3)
(2,6) (3,7) (4,5) (4,6) (5,7) (6,7)
```

These edge labels are the twelve vertices of \(G\); two such vertices are adjacent precisely when the corresponding cube edges share an endpoint. No loops, self-interactions, randomized updates, or boundary vertices are included. The two maps use the same labels and the same initial coloring. All statements concern these **finite** deterministic maps, not infinite cubic lattices, other thresholds, or arbitrary regular graphs.

An initial coloring is encoded in base three by the integer

\[
s(x)=\sum_{j=0}^{11}x_j3^j,\quad 0\leq s(x)<3^{12}.
\]

The first periodic-entry time of \(x\) is the least \(t\geq0\) for which \(F^t(x)\) belongs to a cycle of the functional graph. The least period is the length of that eventual cycle, not necessarily the time it first becomes periodic from update zero.

## Proof

The proof is an exact, complete finite-state classification. The finite verification algorithm is part of the proof, and is small enough to be reproduced from the accompanying standalone source code. It does not infer an infinite statement from experiments.

**Transition calculation.** The cube-edge list defines exactly twelve vertices, each with four line-graph neighbors. For any integer state \(s\) in the stated interval, extract its twelve base-three digits. For each digit \(x_i\), independently count its neighbors equal to \(x_i+1\pmod3\); apply the stated CCA or GHM update condition, and reassemble the next integer state using the same powers of three. Every computed successor is in the same interval. Both source programs implement this complete transition function directly. The Python implementation constructs the twelve cube edges from the Hamming-distance-one condition and evaluates all states vectorially; the C++ implementation hard-codes the cube edges, decodes each state separately, and follows its trajectories one at a time.

**Functional-graph lemma.** For an arbitrary finite set with a deterministic self-map, its directed functional graph has exactly one directed cycle in every weak component. Repeated removal of indegree-zero vertices leaves precisely the cycle vertices. To prove this, a cycle vertex can never have zero remaining indegree because of its predecessor on the cycle. Conversely, if a remaining vertex were not on a cycle, its backwards-predecessor chain in the finite remaining subgraph would repeat and create a cycle feeding it, which would contradict the unique outgoing-edge structure unless it too lay on that cycle. Every removed vertex has a later vertex on its forward path; processing removed vertices in reverse order gives its eventual cycle, period, and exact entry depth by adding one to its successor's entry depth.

**Exhaustive certificate.** In `verify_vectorized.py`, `transition` produces every successor on the complete interval of \(531441\) state integers. `census` removes zero-indegree vertices, walks all residual cycles, and propagates cycle identifiers, periods and entry depths backwards over the removed list. Its counter of temporal orbits gives CCA counts \(81,8,8,36,8\) for periods \(1,3,6,8,12\), and GHM counts \(1,8\) for periods \(1,3\). For CCA the full basin histogram is exactly that stated above; its weighted sum is \(531441\). GHM similarly has one fixed basin of \(531417\) states and eight period-three basins of size three. All omitted period counts are zero because every state has been assigned a cycle identifier. The period arrays for the two maps yield the five rows of the joint table directly.

**Independent enumeration.** The other program, `verify_direct.cpp`, does not use indegree peeling or NumPy. It starts trajectories from every as-yet-unclassified integer, and uses a current-trail index to detect a new cycle or a previously classified state. It labels the discovered cycle and works backwards through the trail to assign period, depth and basin. Its outputs exactly match all temporal-orbit counts, basin-size multiplicities and depth-by-period populations of the first program. The different graph construction, update evaluation and cycle-finding algorithm reduce shared implementation risk; the complete code, not only printed logs, is supplied.

**Sharp clocks and geometric classification.** Both implementations find maximum entry depths eight (CCA) and six (GHM), with exactly 72 starting states achieving each. Independently replayable witnesses are encoded states `31727` for CCA depth eight and `16188` for GHM depth six. For CCA the witness periodic-state encodings `84774`, `37134`, `455`, and `8638` have least periods three, six, eight, and twelve, respectively. The Python certificate also generates all \(3!2^3=48\) permutations of cube coordinates and bit flips; these induce the complete cube isometry group on the twelve edge labels. The global color-cycle \(c\mapsto c+1\pmod3\) also commutes with CCA. Acting on one state per temporal orbit and identifying all cyclic time shifts gives the ten geometric/color classes and their sizes. The same color-shift action is **not** used for GHM, where it would not preserve the update rule.

Because the largest CCA period is twelve and the other nontrivial periods are three, six, and eight, their least common multiple is 24. Thus every state at update eight recurs after 24 more steps. For GHM, after update six the only possible periods are one and three, proving the stated map identities. The 72 sharp witnesses prove the asserted entrance bounds cannot be lowered.

## Verification

Run the following in a directory containing the two supplied source files:

```sh
python3 verify_vectorized.py
g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_direct.cpp -o verify_direct
./verify_direct
```

The full reference outputs are embedded separately as `verification_output.txt` and `verification_direct.txt`. Each program enumerates all \(3^{12}\) labelled states without sampling. The vectorized certificate also checks cube symmetry groups, cycle-period classes, exact joint period counts, and sums of basin populations. The independent compiled certificate verifies all individual basins and entry depths using direct trajectories. The numerical witnesses can be replayed using either program's transition function.

The CCA first-entry distribution for periods one, three, six, eight and twelve is specified exactly by the code; in particular the only nonperiodic states whose eventual period is twelve enter at depths one or two, and every transient that enters an eight-cycle does so by depth three. The deepest transients are attracted to fixed points.

## Relationship to prior work

The three-color cyclic cellular automaton and Greenberg–Hastings dynamics are classical excitable-media models. Fisch, Gravner and Griffeath (1993) discuss threshold-dependent behavior on lattice neighborhoods. Gravner, Lyu and Sivakoff (2016) analyze three-color CCA/GHM on arbitrary finite graphs **at the one-neighbor threshold**, describing eventual activity through cycle integrals, not the critical two-contact map on this finite cuboctahedral graph. Bello and Sivakoff (2021) analyze threshold-two and higher CCA/GHM on **infinite regular trees**, focusing on random fixation/fluctuation thresholds, without a finite cuboctahedron orbit or attraction-basin census.

The previously known Greenberg–Hastings threshold-two census on the same graph is treated as contextual comparison, not as the novel component. The distinct exact CCA census, the five-cell joint period table, the isolated-short-clock versus attracting-long-clock split, and their symmetry classes are the asserted finding. Related threshold-two cyclic-competition calculations on complete multipartite graphs and other graph families do not imply this line-graph-of-a-cube computation: the neighborhoods overlap in triangles and squares and are not globally complete multipartite.

## Limitations

The classification is exact only for the twelve-vertex cuboctahedral graph, the three colors, synchronous updates and a two-neighbor successor threshold. It makes no claim for larger line graphs, other thresholds or generic degree-four graphs. This is a finite exhaustive proof with independently reproducible programs, not a closed-form structural classification for all graphs. External independent audit has not been performed. The historical literature comparison may miss unindexed computations, especially older threshold-model studies whose complete primary text was not accessible in this investigation.

## References

1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-Range Scaling of Excitable Cellular Automata* (public preprint, 1993-04-02). https://arxiv.org/abs/patt-sol/9304001
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs* (arXiv v1, 2016-10-24), https://arxiv.org/html/1610.07320v1
3. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees* (arXiv v1, 2021-08-13), https://arxiv.org/html/2108.06404v1
4. E. W. Weisstein, *Cuboctahedron*, MathWorld, https://mathworld.wolfram.com/Cuboctahedron.html (graph identification background).
