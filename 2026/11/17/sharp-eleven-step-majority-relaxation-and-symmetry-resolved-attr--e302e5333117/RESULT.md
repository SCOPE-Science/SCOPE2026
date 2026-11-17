# Sharp eleven-step majority relaxation and symmetry-resolved attractors on the McGee cage

## Finding
Let \(G\) be the 24-vertex McGee graph, the unique cubic graph of girth seven. Let \(F\) be **synchronous, open-neighborhood binary majority** on \(G\). Then
\[
F^{13}=F^{11}\quad\text{as maps on }\{0,1\}^{24},\qquad F^{12}\ne F^{10}.
\]
Consequently, each configuration first enters a fixed point or primitive two-cycle at some time \(t\le 11\); the bound is sharp. There are exactly **550** fixed configurations and **63,715** primitive temporal two-cycle orbits (127,430 configurations). Modulo the full 32-element spatial automorphism group, the fixed configurations occupy **39** classes and the primitive two-cycle orbits **2,415** classes (allowing temporal phase exchange within each orbit).

Every one of the \(2^{24}=16,777,216\) labelled configurations has the following first-periodic-entry classification:

| First entry \(t\) | Eventually fixed | Eventually primitive two-cycle |
| ---: | ---: | ---: |
| 0 | 550 | 127,430 |
| 1 | 19,806 | 4,000,542 |
| 2 | 83,472 | 5,901,208 |
| 3 | 277,872 | 2,350,112 |
| 4 | 490,464 | 1,213,504 |
| 5 | 470,528 | 530,016 |
| 6 | 445,216 | 313,920 |
| 7 | 267,392 | 145,856 |
| 8 | 34,816 | 80,512 |
| 9 | 1,152 | 18,048 |
| 10 | 0 | 4,480 |
| 11 | 0 | 320 |
| **Total** | **2,091,268** | **14,685,948** |

The two unanimous fixed points each attract exactly **1,033,256** initial configurations. Every initial state attaining the sharp eleven-update first-entry time eventually reaches a two-cycle.

## Assumptions and scope
The vertex set is \(V=\{0,1,\ldots,23\}\), with indices read modulo 24. Form the undirected graph from edges between consecutive vertices on the Hamiltonian 24-cycle and chords \(\{i,i+s_i\}\), where \((s_0,s_1,s_2)=(-12,7,-7)\) is repeated eight times. Thus the LCF specification is \([-12,7,-7]^8\). The graph has degree three, 36 edges, girth seven, and precisely 32 automorphisms. The update rule is, for every \(x\in\{0,1\}^{24}\) and every vertex \(i\),
\[
(F(x))_i=\begin{cases}1,&\sum_{j\in N_G(i)}x_j\ge 2,\\0,&\sum_{j\in N_G(i)}x_j\le 1.\end{cases}
\]
There are no self-neighbor contributions, external fields, asynchronous updates, or tie cases. The first-periodic-entry time is \(d(x)=\min\{t\ge0:F^{t+2}(x)=F^t(x)\}\). A primitive two-cycle orbit is an unordered pair \(\{x,F(x)\}\) satisfying \(F^2(x)=x\) and \(F(x)\ne x\).

## Proof
All assertions concern a **finite, completely specified** map and are established by exhaustive enumeration with transparent algorithms; no finite check is extrapolated to an infinite family.

1. The source `verify_exhaustive.cpp` constructs the graph using the specified LCF rule and checks each chord and rim adjacency is reciprocal and unique. It computes the 24 output bits from the three neighbor bits. The state space is identified bijectively with the integers \(0\) through \(2^{24}-1\), so one loop constructs exactly one successor for each possible state, with no sampling.
2. For each previously unclassified vertex of this finite functional digraph, follow its successor chain to a known state or a state already on the current chain. The latter case identifies precisely one directed cycle; its least period is its length. Mark that cycle with entry time zero, then process the chain backwards, assigning entry time one more than its successor. A previously classified successor contributes its already established period and entry time. These are exhaustive and disjoint cases for a finite function; the implementation explicitly rejects any detected period greater than two.
3. Aggregating entry times and least periods over all \(2^{24}\) states gives the displayed table. The program finds 550 distinct length-one cycles, 63,715 distinct length-two cycles, maximal first-entry time eleven, and exactly 320 states attaining eleven. Identifying the two integer masks representing unanimity produces equal attraction basins of 1,033,256.
4. Independently, `verify_independent.py` reconstructs the graph using an undirected graph library and computes the map in vectorized blocks, directly enumerating the fixed-point and two-cycle equations and checking \(F^{13}(x)=F^{11}(x)\) for **every** state. It also finds a witness \(x=152253\) (hexadecimal `0252bd`) with \(F^{12}(x)\ne F^{10}(x)\), which proves the sharp delay. It independently counts first-entry classes and unanimous basins.
5. The independent script enumerates all graph automorphisms as adjacency-preserving permutations, finding exactly 32. For every periodic configuration it computes its least integer representative under all spatial automorphisms; for each primitive two-cycle it additionally identifies its two temporal phases. Counting distinct representatives gives 39 fixed and 2,415 primitive-two spatial classes.

For completeness, the sharp identity implies that the eventual period divides two after eleven updates; the witnessed strict failure of the corresponding identity at ten updates proves that eleven cannot be reduced. The graph-characterization facts are checked in the independent script and agree with the published LCF description.

## Verification
Compile and execute `verify_exhaustive.cpp` with a C++17 compiler, for example `g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive && ./verify_exhaustive`. Its deterministic standard output is `verify_exhaustive.out`. Run `python verify_independent.py` with NumPy and NetworkX installed; its deterministic standard output is `verify_independent.out`. Each implementation scans all 16,777,216 states and performs different checks: functional-digraph classification versus vectorized power identities and direct periodicity tests. The group calculation uses all 32 adjacency-preserving permutations.

The totals satisfy \(2,091,268+14,685,948=16,777,216\) and \(550+2(63,715)=127,980\) immediately recurrent states. The group-orbit size histograms, first-entry histogram, sample maximum-delay witness, and 32-element automorphism group are printed by the independent checker. Both programs have reproducible deterministic outputs included as files, and both were replayed from the packaged source paths with exact output agreement.

## Relationship to prior work
Goles and Olivos proved eventual period at most two for symmetric threshold networks. This supplies the qualitative periodicity framework, not the graph-specific census or sharp eleven-update cutoff. Benjamini–Chan–O'Donnell–Tamuz–Tan analyze general and random graphs and confirm the classical finite-period fact. Turau treats exact threshold fixed states and two-cycles on **trees**, whereas the McGee cage has cycles of girth seven. Baez and MathWorld describe the McGee graph and its automorphisms, but not its majority-dynamics basins. Indexed studies of majority on the Heawood and dodecahedral graphs concern other, non-isomorphic graphs and do not imply this 24-vertex cage's counts. The nearest available prior same-size cubic majority classification concerns the distinct Nauru graph; no graph isomorphism or domination transfers its census to McGee.

The search located no published source providing the exact McGee majority census, sharp cutoff, or 39/2,415 orbit counts. This is a bounded novelty assessment, not a proof of worldwide priority.

## Limitations
The result concerns exactly one canonical finite graph and this synchronous binary update rule; it makes no claim for arbitrary cubic cages, other girths, or stochastic/asynchronous variants. The exact numerical conclusions rely on exhaustive executable enumeration with two distinct algorithms, rather than short closed-form symbolic identities. The 1980 foundational paper was available in accessible abstract form but not inspected as full text; historical priority cannot be asserted conclusively. Independent third-party mathematical validation has not been performed.

## References
- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, doi:10.1016/0012-365X(80)90121-1.
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first public version 2014-05-11, https://arxiv.org/abs/1405.2486.
- V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580, https://arxiv.org/abs/2202.01580.
- J. C. Baez, *McGee Graph*, September 15, 2015, https://math.ucr.edu/home/baez/visual_insight/20150915%20-%20McGee%20Graph.html.
- E. W. Weisstein, *McGee Graph*, MathWorld, https://mathworld.wolfram.com/McGeeGraph.html (LCF graph specification).
