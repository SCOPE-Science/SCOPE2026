# Isolated oscillators versus broad two-cycle basins in two twelve-vertex Archimedean majority networks

## Finding

Let \(T\) be the truncated-tetrahedral graph and \(C\) the cuboctahedral graph, both with twelve vertices. Under synchronous open-neighbor binary majority (ties retain the incumbent opinion), **every nonfixed two-cycle of \(C\) has no transient predecessors**, whereas two-cycles of \(T\) collectively attract \(2366\) initial states, of which only \(478\) are themselves initially periodic. For a uniformly random binary initial configuration the eventual two-cycle probabilities are therefore exactly \(2366/4096\) for \(T\) and \(40/4096\) for \(C\).

The complete exact functional-graph comparison is:

| Invariant | Truncated tetrahedron \(T\) | Cuboctahedron \(C\) |
|---|---:|---:|
| Fixed states | 16 | 146 |
| Primitive temporal two-cycle orbits | 239 | 20 |
| Initial states eventually in a fixed point | 1730 | 4056 |
| Initial states eventually in a two-cycle | 2366 | 40 |
| Nonperiodic states eventually in a two-cycle | 1888 | 0 |
| Initial states eventually in either unanimous state | 1360 | 2064 |
| Sharp first periodic-entry time | 5 | 4 |
| Full-symmetry classes of fixed states | 5 | 14 |
| Full-symmetry classes of primitive two-cycles | 26 | 3 |

In particular, every binary state on \(T\) satisfies \(F_T^7(x)=F_T^5(x)\), and every binary state on \(C\) satisfies \(F_C^6(x)=F_C^4(x)\). Both bounds are sharp in the sense that some states require respectively five and four updates to enter a cycle.

## Assumptions and scope

The twelve vertices of \(T\) are the ordered pairs \((a,b)\) with distinct \(a,b\in\{0,1,2,3\}\), in lexicographic order. Vertex \((a,b)\) is adjacent to \((b,a)\) and the two vertices \((a,c)\) for \(c\notin\{a,b\}\). Thus every degree is three. The graph \(C=L(Q_3)\) has vertices the twelve unordered edges of the standard three-dimensional Boolean cube. Two of its vertices are adjacent when the corresponding cube edges share an endpoint; every degree is four. Cube vertices are the integers \(0,\ldots,7\), with an edge for each pair differing in one binary position, and cube edges are sorted lexicographically.

A labelled configuration \(x\) belongs to \(\{0,1\}^{12}\). The update at vertex \(v\) is one if strictly more than half its neighbors have color one, zero if strictly fewer, and remains \(x_v\) exactly on a tie. All updates are simultaneous. The entry time \(\tau(x)\) is the smallest \(t\ge0\) for which \(F^t(x)\) is periodic; its eventual least period is \(\ell(x)\). One primitive two-cycle orbit comprises two distinct configurations \(x,y\) with \(F(x)=y,F(y)=x\), counted without distinguishing temporal phase. A spatial class consists of cycles modulo the full graph automorphism group.

The finding is a finite, exact classification for these **two specified graphs** and this specific update rule; it claims no general law for other Archimedean polyhedra or edge perturbations.

## Proof

**1. Complete state-space reduction.** Encode a binary coloring as \(s=\sum_{i=0}^{11}x_i2^i\), ranging over every integer \(0\le s<4096\). The neighbor sets above define a deterministic successor array \(f(s)\). The attached `archimedean_majority.py` enumerates each successor using the strict-inequality/tie test and follows every state until its first repeated or previously classified state. It assigns the exact eventual cycle length, cycle representative and minimal entry time to all 4096 input states, propagating distances backward from the discovered cycle. This is an exhaustive finite proof because every state appears in the array, the successor of every state is constructed, and the first-repeat argument classifies every path of a finite functional graph.

A separate C++17 program, `archimedean_independent.cpp`, independently reconstructs the two graphs and all successors. It repeatedly removes vertices of indegree zero from the functional graph, leaving precisely disjoint directed cycles; it identifies cycle lengths and propagates periodic-entry times in reverse removal order. **The two algorithms agree** on all outcome and first-entry populations. In particular, no period longer than two occurs, and all stated counts are direct exact sums over the exhaustively classified domain rather than extrapolations from examples.

**2. Explicit first-entry certificate.** The exact numbers of initial states, indexed by \(t=\tau(x)\), are:

| Graph and eventual period | \(t=0\) | \(t=1\) | \(t=2\) | \(t=3\) | \(t=4\) | \(t=5\) |
|---|---:|---:|---:|---:|---:|---:|
| \(T\), fixed | 16 | 238 | 468 | 720 | 216 | 72 |
| \(T\), two-cycle | 478 | 1264 | 528 | 96 | 0 | 0 |
| \(C\), fixed | 146 | 1606 | 1200 | 1008 | 96 | 0 |
| \(C\), two-cycle | 40 | 0 | 0 | 0 | 0 | 0 |

Each graph's table totals \(4096\); the number of length-two periodic states is twice its temporal two-cycle count. Every two-cycle of \(C\) has just its own two periodic states in its basin; otherwise the last row would contain a positive entry at some \(t>0\). This proves the isolation statement. Concrete initial witness integers \(310\) for \(T\) and \(348\) for \(C\) attain the largest entry times, so the cutoffs cannot be reduced.

**3. Spatial symmetry.** The four triangular faces of \(T\) are the four intrinsic maximal triangles, and each reverse-pair edge joins a unique pair of triangles; hence any automorphism permutes the four triangle labels and is completely determined by that permutation. Every permutation acts by \((a,b)\mapsto(\pi(a),\pi(b))\), giving \(\operatorname{Aut}(T)\cong S_4\) of order \(24\). For \(C\), its eight intrinsic triangles are exactly the three-edge stars at cube vertices. Their pairwise intersection graph reconstructs \(Q_3\), so every automorphism of \(C\) is induced by a cube automorphism; all translations and coordinate permutations act, giving \(\operatorname{Aut}(C)\) of order \(8\cdot 6=48\). Applying those complete groups to all fixed configurations and all unordered temporal two-cycle pairs gives respectively \((5,26)\) and \((14,3)\) geometric classes. The supplied checker confirms the orbit sizes sum to the labelled counts and checks the Burnside fixed-point identity independently.

**4. Consensus basins and sharp periodicization.** Among all 4096 states, exactly 680 lead to each unanimous fixed point on \(T\), whereas 1032 lead to each unanimous fixed point on \(C\). The independent indegree-peeling computation confirms both totals. The nonzero time-five and time-four classes in the table give the sharpness of the global identities stated above: for period-dividing-two dynamics, all entry times at most \(r\) are exactly the identity \(F^{r+2}=F^r\) on every state.

## Verification

The complete reproducibility bundle includes `archimedean_majority.py`, `archimedean_independent.cpp`, `reference_census.json`, and `verify.py`. Run `python3 verify.py` in the directory containing all four files, with Python 3.9+ and a C++17 compiler (`g++`). It reconstructs the state space, checks graph symmetry and complementation, compares the independent functional-graph traversal to indegree-peeling, checks every stated aggregate and the full frozen reference census, and prints `VERIFY_OK` on success. It does not trust or execute a precompiled binary.

The C++ program emits `INDEPENDENT_CERTIFICATE_OK`, with fixed-point, two-cycle, basin and entry-time counts matching the Python tables. All 8192 labelled input states across the two graphs were exhaustively processed in each implementation, rather than sampled.

## Relationship to prior work

The qualitative theorem that finite symmetric binary threshold dynamics eventually has period at most two is classical (Goles and Olivos, 1980); the period restriction here is **not** claimed as new. The detailed 2014 Benjamini et al. preprint and the open-access 2020 Fountoulakis–Kang–Makai paper study majority voting on other graph families and do not supply these two finite-graph basin populations. The latter's main theorems concern random graphs under density hypotheses, not deterministic twelve-vertex Archimedean graph censuses.

A published general **line-graph majority** theorem gives an exact half-factor formula for recurrent fixed states and two-cycles on line graphs of regular base graphs. It applies to \(C=L(Q_3)\); its fixed and primitive two-cycle counts for that graph are therefore *covered in principle as finite specializations* and are included here only to make the dynamical comparison readable. The theorem concerns recurrent states, however, not the full preperiodic attraction basins, their entry-time histogram, or absence of transient predecessors of cuboctahedral oscillators. The graph \(T\) is also a line graph, but of the graph obtained by subdividing every edge of \(K_4\): those base edges join degree-three to degree-two vertices. Thus the published line-graph theorem's equal-endpoint-degree-parity hypothesis fails for this representation. Its recurrent-state formula does not directly specialize to \(T\). The present claim's new emphasis is the exact paired **transient/oscillatory basin distinction**, including the isolation law for \(C\), not rediscovery of the prior general recurrent classification.

Published calculations on exactly these graphs concern distinct invariants: three-state Greenberg–Hastings excitation on \(T\) and the homotopy type of their two-independence complexes. Their full results were inspected and do not imply the binary-majority basin table. Standard graph encyclopedia references establish the canonical graph identities and symmetry orders, but do not present this dynamical comparison. Searches of literature and research records using both graph names, line-graph aliases, exact numerical populations and the isolation statement identified no covering transient census. That negative evidence is not proof of global priority.

## Limitations

The result is a **finite exact census** for two particular twelve-vertex graphs, not a universal formula for all cubic or quartic networks. Some recurrent-state numbers shown as context are implied in principle by a broader line-graph theorem; the novel claim is limited to the comparative attraction-basin and sharp-time results. Exact exhaustive computational proofs depend on reviewing the included source code and finite certificate, and are not independent formal or peer validation. An unindexed or inaccessible graph-specific majority census could still affect historical originality.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, *Discrete Mathematics* **30** (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first arXiv submission 2014-05-11, https://arxiv.org/abs/1405.2486.
3. N. Fountoulakis, M. Kang and T. Makai, *Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs*, *Random Structures & Algorithms* (first published 2020-10-13), https://doi.org/10.1002/rsa.20970.
4. *Incidence conservation and half-factor classification of two-cycles in line-graph majority dynamics*, published scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-incidence-conservation-and-half-factor-classification-of-two-cyc--61b3de3ad47a.
5. *Exact excitation clocks and tetrahedral symmetry on the truncated tetrahedral graph*, published scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-excitation-clocks-and-tetrahedral-symmetry-on-the-truncate--6c938bef9545.
6. *Homotopy types of the two twelve-vertex Archimedean 2-independence complexes*, published scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-homotopy-types-of-the-two-twelve-vertex-archimedean-2-independen--e9e32ef4ad60.
7. E. W. Weisstein, *Truncated Tetrahedral Graph* and *Cuboctahedral Graph*, MathWorld, https://mathworld.wolfram.com/TruncatedTetrahedralGraph.html and https://mathworld.wolfram.com/CuboctahedralGraph.html.
