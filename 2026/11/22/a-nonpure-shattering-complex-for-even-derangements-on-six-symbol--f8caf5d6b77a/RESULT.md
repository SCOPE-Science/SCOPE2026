# A nonpure shattering complex for even derangements on six symbols

## Finding
Let \(X=\{(i,j):i,j\in\{0,1,2,3,4,5\},\ i\ne j\}\), a set of 30 off-diagonal matrix cells. Let \(\mathcal E_6\) comprise the graphs \(G_\pi=\{(i,\pi(i)):0\le i<6\}\) of the **even fixed-point-free** permutations \(\pi\) on six symbols. Thus \(\mathcal E_6\) has 130 Boolean concepts. A support \(S\subseteq X\) is shattered if every subset of \(S\) is \(G_\pi\cap S\) for some \(G_\pi\in\mathcal E_6\).

**Exact finite classification.** The complex \(\Delta\) of all shattered supports has face enumerator
\[
\Phi_{\mathcal E_6}(z)=1+30z+315z^2+1420z^3+1140z^4.
\]
All size-at-most-three off-diagonal partial matchings are shattered; exactly 1140 of the 2715 size-four partial matchings are shattered; no five-point support is shattered. Consequently \(\operatorname{VCdim}(\mathcal E_6)=4\). The complex is nonpure: it has exactly 360 inclusion-maximal shattered triples and 1140 inclusion-maximal shattered quadruples, and no facets of other sizes. Under simultaneous relabeling of sources and targets by \(S_6\), the triple facets constitute one orbit of size 360, while quadruple facets constitute four orbits of sizes 180, 240, 360, and 360.

The reduced simplicial homology over \(\mathbb F_2\) is concentrated in two consecutive degrees:
\[
\widetilde H_2(\Delta;\mathbb F_2)\cong\mathbb F_2^{384},\qquad
\widetilde H_3(\Delta;\mathbb F_2)\cong\mathbb F_2^{390}.
\]
All other reduced mod-two homology groups vanish. Thus retaining even permutation sign changes not just the top face count but also introduces lower-dimensional maximal supports.

## Assumptions and scope
This is an **exact finite theorem for six symbols only**, not an asymptotic or all-order assertion. The row and column copies are distinguished; the symbol permutations inducing symmetries act *simultaneously* on both. Evenness means the ordinary sign of the permutation is positive. All support cells are distinct, shattering includes the empty and full Boolean traces, and \(\Delta\) includes the empty face. The homology coefficients are \(\mathbb F_2\), not integers or rationals.

## Proof
**1. Necessary support restriction and concept enumeration.** A shattered support is a partial bipartite matching: otherwise its all-positive trace demands that one permutation take a single row to two columns or two rows to a single column. Every fixed-point-free permutation on six symbols has cycle type one of \((6)\), \((4,2)\), \((3,3)\), or \((2,2,2)\). Its sign is \((-1)^{6-c}\), where \(c\) is its number of cycles, so even derangements have only the two-cycle-count types \((4,2)\) and \((3,3)\). Their multiplicities are 90 and 40, respectively, giving 130. Two independent finite enumerators verify this and use different sign tests (inversion parity and cycle count).

**2. Exhaustion of potential shattered supports.** Fix the lexicographic ordering of all 30 cells. For each \(k=0,1,\ldots,5\), enumerate every matching \(S\) of \(k\) off-diagonal cells exactly once: choose \(k\) source rows, choose \(k\) image columns, enumerate all bijections, and discard diagonal assignments (equivalently, recursively choose nonattacking rook cells). For each of the 130 concepts, encode the trace on the ordered \(k\) cells by the binary integer \(\sum_{j=0}^{k-1}2^j\mathbf1_{\{\pi(a_j)=b_j\}}\). The support is shattered precisely when the set of codes has cardinality \(2^k\). This is a finite exhaustive decision procedure, with integer-only operations and no random sampling or unproved search pruning. Both `verify_python.py` and `verify_cpp.cpp` execute it from first principles; their enumerations yield face counts \((1,30,315,1420,1140,0)\) for sizes zero through five. Every larger shattered support would contain a shattered five-cell subset by heredity, contradicting the exhaustive five-cell computation. Nonmatching supports are already excluded by the all-positive-trace argument. This proves the complete face enumerator and the stated VC dimension.

**3. Facets and symmetry.** Within the computed face sets, a face is maximal precisely when no one-cell extension belongs to the next face set; heredity makes this sufficient against extensions by any number of cells. The direct one-cell-extension test identifies 360 maximal triples and all 1140 quadruples as maximal, with no smaller facets. Every simultaneous relabeling \(\sigma\in S_6\) sends cell \((i,j)\) to \((\sigma(i),\sigma(j))\) and permutes \(\mathcal E_6\), since fixed-point-freeness and permutation sign are conjugacy-invariant. Explicitly generate all 720 such relabelings and the orbit of each previously unclassified facet. The facet orbit sizes are \(360\) for triples and \((360,360,240,180)\) for quadruples. Their union equals the complete facet sets, proving the orbit classification. Representatives using the numbers zero through five are:

- Triple: \(\{(0,3),(1,2),(2,0)\}\).
- Quadruple orbit of size 360: \(\{(0,4),(1,2),(2,1),(3,0)\}\).
- Quadruple orbit of size 360: \(\{(0,5),(1,4),(2,1),(3,0)\}\).
- Quadruple orbit of size 240: \(\{(0,2),(1,4),(2,3),(3,0)\}\).
- Quadruple orbit of size 180: \(\{(0,3),(1,5),(2,4),(3,0)\}\).

**4. Exact binary homology.** Form the augmented simplicial chain complex in which each face corresponds to a basis element and the boundary of a size-\(k\) face is the sum modulo two of its \(k\) size-\((k-1)\) deletions. The ranks of the augmented boundary matrices from sizes one through four are, respectively, \((1,29,286,750)\). The two independent verifiers construct the boundary columns directly from their respective face enumerations and perform exact GF(2) elimination. The resulting reduced Betti numbers by dimension are \((0,0,384,390)\) in dimensions zero through three. In particular, the alternating-sum cross-check gives \(-1+30-315+1420-1140=-6=384-390\). There are no higher chain groups, proving all vanishing statements.

## Verification
Run `python3 verify_python.py` from the extracted files. Separately compile `verify_cpp.cpp` with `g++ -O2 -std=c++17 -o verify_cpp verify_cpp.cpp` and execute `./verify_cpp`. Both use the standard libraries only. The Python script enumerates matches by independent row/column choices and inversion-sign parity, and classifies the complete facet orbits. The C++ script enumerates nonattacking cells recursively and uses permutation cycle parity; it independently calculates exact binary boundary ranks. Each has explicit assertions or failure exits for the stated counts. Successful final markers are `EVEN_DERANGEMENT_PYTHON_PASS` and `EVEN_DERANGEMENT_CPP_PASS`.

## Relationship to prior work
Bucić, Devlin, Hendon, Horne, and Lund's 2019 preprint on perfect matchings and derangements investigates intersection proportions and derangements of directed graphs. Its main statements concern ratios and matching intersections, not Boolean shattering of a sign-restricted family. A separate published published-finding corpus finding establishes the exact all-order shattering polynomial for **all** derangements: for six symbols it is \(1+30z+315z^2+1420z^3+2715z^4\), whereas the present family restricts to **even** derangements, has only 1140 shattered quadruples, has 360 maximal triples, and has nonzero homology in two degrees. Hence the unrestricted result does not imply the parity-sensitive incidence classification: shattering need not survive taking a subfamily. Classical rook-counting, cycle-type counts, group orbits and binary boundary reduction are ingredients, not individually claimed as new.

## Limitations
The claim concerns exactly 130 even derangements at six symbols, with no extrapolation to larger sizes. Mod-two homology does not establish the integral homology or a wedge-of-spheres type. Finite exhaustive computation supplies the decisive certificate; the scripts are inspectable and were independently executed, but a separate external mathematical audit has not occurred. The relevant derangement literature does not exclude older, unindexed incidence computations or equivalent descriptions under parity-constrained matching terminology.

## References
1. M. Bucić, P. Devlin, M. Hendon, D. Horne, B. Lund, *Perfect matchings and derangements on graphs*, arXiv:1906.05908, first posted June 13, 2019; Journal of Graph Theory 97 (2021), 340–354. https://arxiv.org/abs/1906.05908
2. *Perfect-matching trace universality and the shattering polynomial of derangements*, published-finding corpus research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-perfect-matching-trace-universality-and-the-shattering-polynomia--d84d57a040aa
