# Seven residual wave geometries and an eight-step extinction clock on the icosahedral graph

## Finding
Let \(I\) be the ordinary twelve-vertex icosahedral graph, and let \(F\) be synchronous three-state Greenberg–Hastings excitation with *two* excited neighbors required to activate a resting vertex. There are exactly \(200\) primitive three-cycles, one fixed point, and no other periodic orbits among its \(3^{12}=531441\) labelled states. Under the full \(120\)-element spatial automorphism group and temporal phase shifts, the \(200\) cycles form exactly **seven** geometric classes of sizes \(5,5,20,30,40,40,60\). Exactly \(1260\) initial states reach a nonconstant cycle, while \(530181\) reach the all-rest state. The attraction basins of the \(200\) nonconstant cycles have precisely three possible sizes: \(100\) basins of size \(3\), \(40\) of size \(6\), and \(60\) of size \(12\).

The global map identity is sharp:
\[
F^{11}=F^8,\qquad F^{10}\neq F^7.
\]
All oscillating states enter a three-cycle by update \(3\), and all extinguishing states reach the all-rest configuration by update \(8\). Exactly \(420\) initial states first reach rest at update \(8\). The complete joint first-entry time and eventual primitive-period counts are:

| First periodic entry \(t\) | Period \(1\) | Period \(3\) |
|---:|---:|---:|
| 0 | 1 | 600 |
| 1 | 4,095 | 540 |
| 2 | 66,091 | 60 |
| 3 | 206,142 | 60 |
| 4 | 176,472 | 0 |
| 5 | 64,900 | 0 |
| 6 | 10,440 | 0 |
| 7 | 1,620 | 0 |
| 8 | 420 | 0 |
| **Total** | **530,181** | **1,260** |

## Assumptions and scope
The labelled vertices are \(0,\ldots,11\), with the five distinct neighbors of each vertex given in `adjacency.txt`. The input is the standard simple, undirected, connected, five-regular icosahedral graph with \(30\) edges. A configuration \(x\) assigns \(x_v\in\{0,1,2\}\) to each vertex; the meanings are resting, excited, and refractory, respectively. For every vertex the simultaneous update is
\[
(Fx)_v=\begin{cases}
2,&x_v=1,\\
0,&x_v=2,\\
1,&x_v=0\text{ and }|\{u\sim v:x_u=1\}|\ge2,\\
0,&x_v=0\text{ and }|\{u\sim v:x_u=1\}|<2.
\end{cases}
\]
A temporal orbit is a cycle of the labelled functional graph of \(F\), counted once without regard to its starting phase. A spatial geometric class identifies temporal orbits under automorphisms of \(I\), with phase rotation also allowed. The first periodic entry time \(\tau(x)\) is the smallest nonnegative integer \(t\) for which \(F^t(x)\) is periodic. Each basin is the set of all initial labelled states that ultimately enter a specified temporal orbit, including its periodic states.

## Proof
**Exhaustive state encoding.** Each configuration has the unique integer code
\[
c(x)=\sum_{v=0}^{11}3^v x_v\in\{0,\ldots,531440\}.
\]
`verify_direct.cpp` reads the explicitly listed graph, calculates the successor of each of these \(531441\) codes from the displayed rule, and decomposes the entire resulting functional digraph into cycles and rooted in-trees. The depth of a vertex in an in-tree is exactly its first periodic-entry time; the cycle length is its eventual primitive period. Every code is classified exactly once. The output `direct_output.txt` is the full depth-by-period histogram above and also lists the individual orbit-basin histogram, giving \(200\) primitive three-cycles, one fixed point, and the stated basin counts. *Only* cycle lengths \(1\) and \(3\) occur: the code checks and rejects any other length before producing the census.

**Independent direct-iterate certificate.** Rather than reconstructing functional trees, `verify_vector.py` constructs the Boolean excited-neighbor contact arrays over the full base-three state cube and forms the exact iterates \(F^t\) for \(0\le t\le11\), using a vectorized implementation independent of the C++ traversal. It checks the equality \(F^{11}(x)=F^8(x)\) **for every** state code and checks that equality fails for some code when the exponent pair is \((10,7)\). The least \(0\le t\le8\) for which \(F^{t+3}(x)=F^t(x)\) is then the first periodic-entry time because all recurrent periods divide three; period \(1\) versus \(3\) is distinguished by testing \(F^{t+1}(x)=F^t(x)\). The second implementation reproduces every table cell and all \(200\) individual cycle basin sizes independently, comparing its complete canonical-root table to `orbit_roots.csv`. This direct finite identity and complete range of codes prove the global claim without assuming any unobserved extrapolation.

**Rotating-phase check.** A phase-rotating three-cycle necessarily has \((Fx)_v=x_v+1\pmod3\) at every vertex. Such a cycle exists if and only if every vertex has at least two neighbors with color \(x_v+1\pmod3\); the condition is applied when that vertex is resting. The independent checker enumerates all \(531441\) colorings and finds exactly \(600\) satisfying this local condition, and verifies that these are *precisely* all \(600\) nonconstant recurrent states obtained through the dynamical certificate. This does not assume that on arbitrary graphs every three-cycle must rotate every vertex: that equivalence is verified here for this specific graph. Dividing by the primitive temporal period \(3\) gives \(200\) cycles.

**Sharpness and basins.** In base-three encoding the state of code \(2824\), with vertex-order digits `121212010000`, follows the integer-code trajectory
\[
2824\to267725\to526611\to637\to184619\to371307\to4867\to2\to0.
\]
It first becomes resting after exactly eight updates, proving the asserted bound is sharp and that \(F^{10}\ne F^7\). The direct and vector checkers separately find exactly \(420\) states of depth eight. Canonicalizing each primitive three-cycle by its least integer code, then counting all preimages of its cycle, gives \(100\) basins of size \(3\), \(40\) of size \(6\), and \(60\) of size \(12\). Their total is \(100(3)+40(6)+60(12)=1260\), leaving \(530181\) states in the fixed-point basin.

**Full spatial symmetry check.** The graph automorphism group has order at most \(12\cdot10=120\): a chosen vertex has twelve possible images; its five neighbors induce a cycle, with at most ten possible oriented-cycle images; and the remaining vertices are uniquely determined by their contact pairs in that neighbor cycle, plus the opposite vertex. `automorphisms.json` lists \(120\) pairwise distinct permutations, all verified to preserve adjacency and form a group by `verify_symmetry.py`; hence the upper bound is attained and the list is the full group. Acting on the \(200\) temporal orbit canonical roots and recanonicalizing phases gives the seven disjoint orbits tabulated in `orbit_classes.csv`:

| Spatial orbit size | Representative code | Vertex-order phase digits | Basin per temporal cycle |
|---:|---:|---|---:|
| 5 | 39070 | `100121222100` | 3 |
| 5 | 49466 | `200212111200` | 3 |
| 20 | 32456 | `200211221100` | 3 |
| 30 | 24514 | `122121020100` | 3 |
| 40 | 16490 | `202121112000` | 6 |
| 40 | 24694 | `121212020100` | 3 |
| 60 | 25408 | `100212120100` | 12 |

The seven sizes total \(200\), and their basin-weighted total is exactly \(1260\). These calculations are complete finite certificates using labelled graph data, not samples.

## Verification
All input, source, table and output files are supplied in this package. In the directory containing them, run `c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct` and compare stdout with `direct_output.txt` (the first program generates `orbit_roots.csv`). Then run `python3 verify_vector.py` with NumPy available, compare stdout to `vector_output.txt`, and verify it agrees on every root and basin. Finally run `python3 verify_symmetry.py` (Python standard library) and compare stdout and `orbit_classes.csv` to the included references. The `VERIFICATION.md` contains exact commands. The complete finite check has \(3^{12}\) inputs, so it is exhaustive, but it proves nothing about larger graphs or other contact rules.

## Relationship to prior work
Durrett and Griffeath (1993) and Adamatzky (2011) motivate excitation-threshold changes in excitable cellular automata. Gravner, Lyu and Sivakoff (2016), Theorem 3, and Doba (2018), Theorems 1–2, characterize key aspects of single-contact three-state excitation on finite graphs; their local rule is different here. A published single-contact icosahedral census gives \(48400\) primitive three-cycles, \(513210\) initial states reaching a nonconstant cycle and a sharp six-update periodic-entry bound. It also supplies \(473\) geometric classes and their representatives. Some *static* two-contact phase-coloring data could be recovered by filtering those representatives, but its single-contact transition map does **not** supply the two-contact attraction basins or the sharp eight-update identity. A published four-state single-contact icosahedral census concerns a different local state space and contact requirement. The strict induced-density extinction bound does not apply here, as the full icosahedral graph has induced edge-density \(30/12=5/2\), larger than the contact threshold two. This work isolates the two-contact finite dynamical census rather than claiming discovery of the three-state rule or general three-color excitation theory.

The comparison reveals a counterintuitive relationship: raising the threshold from one to two reduces the number of primitive waves from \(48400\) to \(200\), but the maximum entry time increases from six to eight updates. The precise near-majority attraction-basin distribution is not implied by earlier single-contact orbit counts.

## Limitations
The accepted theorem concerns exactly the ordinary twelve-vertex icosahedral graph under three-state, absolute contact threshold two. It is not a general theorem for regular triangulations or a probabilistic large-system limit. Every numerical claim is finite and exact, with two independently structured exhaustive checkers; the analytic arguments by themselves do not establish the eight-step identity or all basin counts. Independent external audit has not been performed. Indexed and accessible published sources were compared, but an unpublished, differently named, or unindexed equivalent enumeration remains possible. No claim of novelty is made for single-contact theory, the strict density bound, or general phase-rotation observations.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, preprint first posted 1993-03-22, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002.
2. A. Adamatzky, *Excitable Delaunay triangulations*, preprint first posted 2011-02-05, arXiv:1102.1069, https://arxiv.org/abs/1102.1069.
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, preprint first posted 2016-10-24, arXiv:1610.07320, https://arxiv.org/abs/1610.07320.
4. N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–126, https://doi.org/10.25088/ComplexSystems.27.2.101.
5. *Icosahedral excitation: exact three-cycle, geometric-orbit, and six-step entrance census* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-icosahedral-excitation-exact-three-cycle-geometric-orbit-and-six--6295ce972482.
6. *Four-state icosahedral excitation: a ten-step relaxation clock and two extremal symmetry classes* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-four-state-icosahedral-excitation-a-ten-step-relaxation-clock-an--721372059306.
7. *A densest-subgraph threshold and finite excitation budget for three-state graph dynamics* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-densest-subgraph-threshold-and-finite-excitation-budget-for-th--352367f51e91.
