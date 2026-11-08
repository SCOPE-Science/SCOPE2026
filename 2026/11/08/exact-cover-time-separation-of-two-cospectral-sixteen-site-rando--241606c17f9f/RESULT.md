# Exact cover-time separation of two cospectral sixteen-site random-walk networks

## Finding
Let \(R=K_4\square K_4\) be the rook graph, and let \(S\) be the Shrikhande graph. For the discrete-time simple random walk on either graph, let \(T_G\) be the number of jumps required to visit all sixteen vertices, counting the initial vertex as visited at time zero. Write \(C_G=\mathbb E[T_G]\). The walk may start from any vertex.

The two graphs have identical strongly regular parameters \((16,6,2,2)\), and hence the same adjacency spectrum \(\{6^{(1)},2^{(6)},(-2)^{(9)}\}\), but their expected cover times are different:

\[
C_R=55.1202395226859\ldots < C_S=55.1206438175266\ldots.
\]

More precisely, the **strict exact-rational inequality** is accompanied by the certified interval
\[
\frac{40429484}{10^{11}}<C_S-C_R<\frac{40429485}{10^{11}}.
\]
The complete exact numerators and denominators of both cover times and their difference are in `CERTIFICATE.json` and are independently recomputed by `verify.py` using only integer arithmetic and rational sums. In the cardinality-grouped hitting-set inclusion–exclusion sum, both graphs have identical contributions for retained-set sizes \(1,2,3,13,14,15\), while their first discrepancy occurs at size four and equals \(28850/11491337\) (Shrikhande minus rook).

Thus, adjacency cospectrality and even identical strongly regular parameters do not determine the finite-volume mean random-walk covering time on this canonical graph pair.

## Assumptions and scope
Use vertex set \(V=(\mathbb Z/4\mathbb Z)^2\), labeled \(v=4x+y\), \(x,y\in\{0,1,2,3\}\). Distinct vertices are adjacent in \(R\) when their first or second coordinates agree. Distinct vertices are adjacent in \(S\) when their difference belongs to \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\), all coordinates modulo four. The graph is fixed, with no added edges, loops, weights, or absorbing sites. At each jump the walker chooses one of six neighbors uniformly. A starting vertex has already been visited at jump zero.

Both graphs are vertex-transitive, so the mean cover time is independent of the starting vertex; throughout the calculations the starting vertex is \(o=(0,0)\).

The claimed inequality concerns expectations in discrete jump-count units. A rate-one continuous-time walk whose holding times are independent mean-one exponentials has the same expected cover time, but a rate-six-per-vertex walk scales both means by \(1/6\).

## Proof
**1. The graphs have the same spectrum.** In each graph a direct neighborhood check shows degree six and exactly two common neighbors for every pair of distinct vertices. Therefore its adjacency matrix \(A\) satisfies \(A^2=4I+2\mathbf J\). On the all-one direction \(A\) has eigenvalue six. On its orthogonal complement the eigenvalues are \(\pm2\), and the zero diagonal fixes multiplicities six and nine. The two graphs are nonisomorphic: every row of \(R\) forms a four-clique, whereas the neighbors of any vertex of \(S\) induce a six-cycle, precluding a four-clique.

**2. Exact subset-hitting formula.** For each nonempty proper subset \(B\subset V\) containing \(o\), define \(H_B\) as the first time the walk exits \(B\). Put \(M_B=6I-A[B]\), with rows and columns ordered by increasing vertex label. The first-step equations for \(h_v=\mathbb E_v H_B\) give
\[
M_B h=6\mathbf1.
\]
Since the original graph is connected and \(B\) is proper, the killed walk exits with probability one and \(M_B\) is nonsingular (indeed positive definite). Let \(M_B^{[o]}\) be obtained from \(M_B\) by replacing its column indexed by \(o\) by \(6\mathbf1\). Cramer's rule gives
\[
\mathbb E_o H_B=\frac{\det M_B^{[o]}}{\det M_B}.
\]

Let \(T_v\) be the first hitting time of \(v\), for \(v\ne o\). The elementary maximum/minimum inclusion–exclusion identity, valid pointwise for nonnegative times, is
\[
\max_{v\ne o}T_v
=\sum_{\emptyset\ne D\subseteq V\setminus\{o\}}
(-1)^{|D|+1}\min_{v\in D}T_v.
\]
Taking expectations and putting \(B=V\setminus D\), one obtains the **finite exact formula**
\[
C_G=\sum_{\substack{o\in B\subsetneq V}}(-1)^{17-|B|}
\frac{\det M_B^{[o]}}{\det M_B}.
\tag{1}
\]
There are exactly \(2^{15}-1=32767\) terms. This step is an exact identity, not a Monte Carlo approximation.

**3. Integer certification.** The standalone program `exact_cover.cpp` constructs both adjacency matrices exactly, evaluates every determinant in (1) by fraction-free Bareiss elimination using signed 128-bit integer intermediates, and emits each fraction's two integer determinants. The standard-library `fractions.Fraction` calculation in `verify.py` reduces the complete signed sums to the exact rational entries recorded in `CERTIFICATE.json`. In particular, the exact difference has a strictly positive numerator and satisfies the stated two-sided rational bounds. The same calculation groups terms by \(|B|\) and establishes the size-four contribution stated above.

For an independent formulation, `cover_dp.cpp` solves the backward equations on visited-state sets. With current visited set \(B\), present vertex \(v\in B\), and \(F(B,v)\) the remaining expected jumps, it uses \(F(V,v)=0\) and
\[
6F(B,v)-\sum_{w\in B,\,w\sim v}F(B,w)
=6+\sum_{w\notin B,\,w\sim v}F(B\cup\{w\},w).
\tag{2}
\]
Computing these systems in descending subset order gives values agreeing with (1) to better than \(10^{-9}\). Equation (1), rather than floating-point agreement, certifies the strict inequality.

## Verification
From a directory containing the four standalone artifacts run `python3 verify.py` with a C++17 compiler available as `g++`. This recompiles and runs both independent programs; checks symmetry, degrees, and the common-neighbor identity; enumerates all 32767 rooted proper subsets in each exact determinant sum; recomputes all three full rational certificates; checks the strict rational interval and the size-four group term; and verifies agreement with the distinct visited-set recursion. No external data, random seeds, or packages beyond Python's standard library and the C++17 compiler are needed.

The exact arithmetic uses determinants of at most order fifteen. Intermediate integers are bounded well within signed 128-bit range by standard Hadamard bounds on the entries and minors in these matrices. The complete certificate can be recomputed on any conventional 64-bit computer with C++17 support.

## Relationship to prior work
Feige and Rabinovich, *Deterministic Approximation of the Cover Time* (2003), analyze cover-time algorithms and the subset-hitting/inclusion–exclusion method in general. Their examined preliminary full text, including its introduction, Section 2.6, algorithm, and examples, does not evaluate the present two graphs. The general identity (1) is not claimed to be new. Rudinger and collaborators, *Comparing algorithms for graph isomorphism using discrete- and continuous-time quantum random walks* (2012), analyze distinguishing strongly regular graphs using quantum-walk certificates; their examined Sections II, IV, VII and appendix address a different observable and do not imply the cover-time inequality. Existing calculations distinguishing the same two graphs by static independence structures, adsorption kinetics, Ising models, and percolation do not imply a comparison of their classical random-walk cover times.

This is an exact finite-pair transport calculation, not a claim that cover time is previously unknown as an invariant, nor a new general-purpose cover-time algorithm.

## Limitations
The observed difference is small (about seven parts per million of the mean). No claim is made of a universal order relation for all cospectral graphs, a minimal counterexample among all graph pairs, or a broad asymptotic theorem. The first discrepancy at retained-set size four is a statement about the exact inclusion–exclusion decomposition, not a claim that one specific four-vertex motif alone determines the final sign. Although targeted primary-literature and mathematical-result searches did not locate these exact rational values, an unindexed historical exact-cover-time computation may exist. No external independent audit has been performed.

## References
1. U. Feige and Y. Rabinovich, *Deterministic approximation of the cover time*, Random Structures & Algorithms **23** (2003), 1–22, DOI: [10.1002/rsa.10083](https://doi.org/10.1002/rsa.10083). Public preliminary text: [PDF](https://static.aminer.org/pdf/PDF/001/051/963/deterministic_approximation_of_the_cover_time.pdf).
2. K. Rudinger, J. K. Gamble, E. Bach, M. Friesen, R. Joynt, and S. N. Coppersmith, *Comparing algorithms for graph isomorphism using discrete- and continuous-time quantum random walks* (2012), [arXiv:1207.4535](https://arxiv.org/abs/1207.4535).
3. C. Cooper and A. Frieze, *The Cover Time of Random Regular Graphs*, SIAM Journal on Discrete Mathematics **18** (2005), 728–740, DOI: [10.1137/S0895480103428478](https://doi.org/10.1137/S0895480103428478); asymptotic random-regular-graph context, not a source for the exact values above.
