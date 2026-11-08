# Exact excitation clocks and tetrahedral symmetry on the truncated tetrahedral graph

## Finding

For the synchronous threshold-one three-state Greenberg–Hastings map \(F\) on the twelve-vertex truncated tetrahedral graph, every labelled configuration has eventual primitive period in \(\{1,3,4,6,8\}\). The exact number of distinct temporal cycles and the number of initial configurations in their respective eventual basins are:

| Primitive period | Temporal cycles | Basin size |
|:---:|---:|---:|
| \(1\) | 1 | 52,677 |
| \(3\) | 3,108 | 340,848 |
| \(4\) | 6 | 4,656 |
| \(6\) | 12 | 127,116 |
| \(8\) | 6 | 6,144 |

There are exactly \(9,469\) periodic labelled configurations among \(3^{12}=531,441\) states. The sharp largest time to reach a periodic state is \(10\), attained by exactly \(384\) initial configurations; each of these eventually enters a three-cycle.

Under the full graph automorphism group \(S_4\), all six four-cycles form one orbit with spatial stabilizer of order \(4\), all twelve six-cycles form one orbit with stabilizer of order \(2\), and all six eight-cycles form one orbit with stabilizer of order \(4\). In a representative cycle, the numbers of excited vertices at successive times, minimized over temporal rotation, are respectively \((2,4,2,4)\), \((1,1,2,2,4,2)\), and \((3,3,3,3,3,3,3,3)\). Every vertex is excited exactly once per four- or six-cycle and exactly twice per eight-cycle. In particular, a four-cycle and an eight-cycle can have the same per-vertex asymptotic excitation rate \(1/4\) while having distinct primitive periods.

## Assumptions and scope

Index the twelve vertices by ordered pairs \((a,b)\) of *distinct* elements of \(\{0,1,2,3\}\), in lexicographic order. The vertex \((a,b)\) is adjacent precisely to \((b,a)\) and to the two vertices \((a,c)\) with \(c\notin\{a,b\}\). Each vertex therefore has degree three. The four triples of pairs sharing a first coordinate are the four triangular faces; the six reverse-pair edges connect them, giving the standard truncated-tetrahedral skeleton (twelve vertices, eighteen edges). This labelled construction is part of the theorem, so there is no dependence on a drawing or implicit graph conventions.

A configuration \(x\) assigns to each vertex one state \(0\) (rest), \(1\) (excited), or \(2\) (refractory). The map \(F\) acts simultaneously: \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) exactly when at least one neighbor currently has state \(1\), otherwise \(0\mapsto0\). For any configuration, \(\tau(x)\) is the smallest nonnegative integer \(t\) for which \(F^t(x)\) belongs to a temporal cycle, and \(\ell(x)\) is that cycle's least period. A temporal cycle comprises the orbit of one periodic configuration under iteration of \(F\), with its temporal shifts identified but its spatial labels retained. A spatial symmetry acts on such cycles by applying the same graph automorphism at every time.

The classification concerns this *finite, deterministic, synchronous* map, only at three states and threshold one. All counts are exact integers.

## Proof

**Graph and symmetries.** Each edge joining \((a,b)\) to \((a,c)\) lies in exactly one triangle; no reverse-pair edge lies in a triangle. Thus the four triangles are intrinsic and every graph automorphism permutes them. An automorphism inducing the identity on those triangles fixes every vertex: \((a,b)\) is characterized as the member of triangle \(a\) whose reverse-pair edge meets triangle \(b\). Therefore the graph automorphism group injects into \(S_4\). Conversely any permutation of \(\{0,1,2,3\}\) acts by \((a,b)\mapsto(\pi(a),\pi(b))\) and preserves all adjacencies. Hence the full spatial symmetry group is exactly \(S_4\) of order \(24\).

**Complete finite-state certificate.** Let the ordered vertices be \(v_0,\ldots,v_{11}\). Encode \(x\) by the integer \(s(x)=\sum_{i=0}^{11}x(v_i)3^i\), which is a bijection between labelled configurations and the integers \(0\) through \(531440\). The independently supplied programs `census_cpp.cpp` and `census_python.py` both construct each successor using the explicitly defined three-neighbor rule and visit all \(3^{12}\) encoded states. The exhaustive C++ implementation forms the entire directed functional graph. It removes indegree-zero vertices repeatedly, which eliminates exactly the nonperiodic vertices of a finite functional graph. What remains is a disjoint union of directed cycles; traversing each once determines its exact length, and reverse traversal of the removed vertices determines \(\tau\) and \(\ell\). Its output counts sum to \(531441\) across the basin classes and to \(9469\) on the periodic vertices. There are no unvisited states or presumptive maximum-period cutoffs.

The independently written Python implementation instead follows each previously unassigned forward orbit, detects its first repeated state or a previously classified state, and propagates its exact period and entry time backwards. Its exhaustive temporal-class table is identical, cell by cell, to that of the indegree algorithm. The two programs therefore establish the displayed exact temporal-census and sharp transient values by separately checkable finite exhaustive arguments; neither uses experimental sampling to conclude a universal infinite-domain statement.

**Spatial orbits and excitation profiles.** Apply all \(24\) permutations of the tetrahedron labels to each temporal cycle's integer-minimal representative, and take the integer-minimal representative of each transformed temporal cycle. The explicit output of *both* programs partitions all six length-four cycles into one group of six, all twelve length-six cycles into one group of twelve, and all six length-eight cycles into one group of six. Orbit–stabilizer gives stabilizer orders \(24/6=4\), \(24/12=2\), and \(24/6=4\). The two programs independently count state-one occurrences at every time and, for the second, at every vertex through the complete orbit. Since each class is transitive under spatial symmetries, the representative profiles and site counts hold for every cycle in that class. This proves the asserted excitation-frequency distinction.

For explicit witnesses of least periods \(4\), \(6\), and \(8\), initial encoded states \(454\), \(14\), and \(1169\) respectively have the following complete distinct forward iterates (each twelve-digit word lists vertex colors in the defined lexicographic order):

- Period \(4\): `112121000000`, `220202100010`, `000000211121`, `001010022202`.
- Period \(6\): `211000000000`, `022000100100`, `000000211211`, `000011022022`, `000122000000`, `100200000000`.
- Period \(8\): `220121100000`, `000202211010`, `000010022121`, `001121000202`, `112202000010`, `220000100121`, `001000211202`, `112010022000`.

The input representation and the algorithms' termination arguments above are sufficient to reproduce all counts; the witness words are ancillary checks rather than a substitute for exhaustiveness.

## Verification

Run `python3 verify.py` from a directory containing the bundled `census_cpp.cpp`, `census_python.py`, and both recorded JSON output files, using a C++17 compiler. The checker recompiles the C++ implementation, executes both programs, checks their equality with recorded outputs, compares every exact temporal-class cell and all six-/eight-/four-cycle spatial classes, verifies the \(3^{12}\) coverage identity, and checks every long-cycle vertex-excitation frequency. Captured output is in `verification_output.txt`, with final line `VERIFY_OK`. The executable is rebuilt locally, not trusted from an external binary.

For full time-to-cycle data, `census_cpp.json` and `census_python.json` contain the entire array of triples \((\ell,\tau,\#\{x:\ell(x)=\ell,\tau(x)=\tau\})\). The nonzero counts, indexed in ascending order of entry time starting from zero, are:

- Period \(1\): \((1,4095,15969,15262,8464,8886)\).
- Period \(3\): \((9324,6152,23920,57160,78392,73788,51060,24876,11904,3888,384)\).
- Period \(4\): \((24,360,1836,2436)\).
- Period \(6\): \((72,9528,37416,36180,17712,15840,10368)\).
- Period \(8\): \((48,528,1728,2592,1248)\).

## Relationship to prior work

The Greenberg–Hastings excitable-media model and its three-state version are classical; see Durrett and Griffeath (1993), publicly deposited March 22, 1993. Gravner, Lyu and Sivakoff (arXiv:1610.07320, October 24, 2016; published in 2018) characterize the synchronization/oscillation dichotomy and common asymptotic excitation activity on arbitrary finite graphs using circulation of a graph one-form. Their Theorem 3 applies here and provides the general qualitative framework, but neither its statement nor the investigated finite-graph sections supply the exact temporal populations, four-/six-/eight-cycle census, graph-specific maximal entry time, or spatial-symmetry orbit structure proved above. The two simultaneous period-four and period-eight orbit classes, with equal site activity \(1/4\), show why the common activity alone does not determine the present finer invariant.

The truncated tetrahedral graph and its order-\(24\) symmetry group are standard graph-theoretic objects (Weisstein, MathWorld, *Truncated Tetrahedral Graph*). These structural facts are cited background, not asserted as discoveries. The new claim is the exact dynamical classification and the long-cycle symmetry/frequency distinction for this graph. Searches found no directly covering classification, but absence of indexed matches is not a proof of global historical priority.

## Limitations

The result is graph-specific, assumes three states and threshold one, and does not extrapolate to other Archimedean graphs or more colors. The long-period spatial orbits (lengths \(4,6,8\)) are classified, but the \(3108\) length-three cycles are **not** classified into spatial symmetry classes. The exhaustive programs prove a finite classification conditional on their explicitly reviewable logic and input conventions; their successful replay is not independent formal or peer certification. Prior literature not available through the consulted searches could contain equivalent results.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002 (first submitted March 22, 1993), https://arxiv.org/abs/patt-sol/9303002.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (October 24, 2016), *Annals of Applied Probability* **28** (2018), 3324–3357, https://doi.org/10.1214/17-AAP1350; authors' complete text: https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf.
3. E. W. Weisstein, *Truncated Tetrahedral Graph*, MathWorld, https://mathworld.wolfram.com/TruncatedTetrahedralGraph.html.
