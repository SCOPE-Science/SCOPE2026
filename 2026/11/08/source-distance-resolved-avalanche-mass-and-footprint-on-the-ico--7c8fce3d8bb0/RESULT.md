# Source-distance-resolved avalanche mass and footprint on the icosahedral sandpile

## Finding
Let \(G\) be the ordinary 12-vertex, 30-edge icosahedral graph, with an arbitrary vertex \(s\) as the sole absorbing sink. Starting with a uniformly chosen recurrent stable state, add one grain at a fixed nonsink vertex \(v\). Let \(T\) denote the **total** number of non-sink topplings, including repetitions, and let \(S\) be the number of **distinct** nonsink vertices toppled. For \(d=\operatorname{dist}_G(s,v)\in\{1,2,3\}\), set
\[
 A_d(u,w)=\sum_{\eta\in\mathrm{Rec}(G,s)}u^{T(\eta,v)}w^{S(\eta,v)}.
\]
The **complete exact coefficient tables** of all three polynomials are `AVALANCHE_COUNTS.csv` (100 nonzero coefficients total). There are exactly \(5,184,000\) recurrent states, and \(A_d(1,1)=5,184,000\) for each \(d\). The polynomial depends only on source-to-sink distance. The following structural distinctions are exact:

- For \(d=1\), \(T=S\) always; its 12 coefficients are
\[
 A_1(u,w)=3,283,200+\sum_{k=1}^{11}c_k(uw)^k,
 \quad (c_1,\ldots,c_{11})=(403202,176000,124836,104978,94626,93516,94626,104978,124836,176000,403202).
\]
In particular \(c_k=c_{12-k}\) for \(1\leq k\leq11\).
- For \(d=2\), \(A_2(0,0)=3,462,398\), and the largest possible total toppling count is \(28\), with exactly \(21,696\) configurations realizing \((T,S)=(28,11)\).
- For \(d=3\), \(A_3(0,0)=3,492,388\), and the largest possible total toppling count is \(29\), with exactly \(30,746\) configurations realizing \((T,S)=(29,11)\).

Here \(A_d(0,0)\) denotes the coefficient of the constant monomial; no topplings occur exactly for \((T,S)=(0,0)\). The stationary joint probability is the appropriate coefficient divided by \(5,184,000\). No asymptotic or infinite-volume claim is made.

## Assumptions and scope
The graph is a simple, undirected, unweighted icosahedral graph. Every vertex has degree five. The sink never topples; a grain transmitted to it is lost. A stable configuration is a function \(\eta:V(G)\setminus\{s\}\to\{0,1,2,3,4\}\). A nonsink site topples when its current height is at least five, losing five grains and sending one along each incident edge. Recurrent means the stationary recurrent class of the usual addition-and-stabilization Markov chain, equivalently Dhar's burning criterion. The source \(v\) and sink \(s\) are fixed for each individual polynomial, and the recurrent configuration is uniformly distributed, as is standard for the Abelian sandpile group.

## Proof
**Finite exhaustive certificate.** There are exactly \(5^{11}=48,828,125\) stable configurations to consider, indexed without omissions by the base-five digits of integers from zero to \(5^{11}-1\). The complete source `icosa_avalanche.cpp` implements a constant-degree adjacency list for the icosahedron and tests recurrence by **Dhar's burning deletion algorithm**: set \(U=V\setminus\{s\}\); delete a vertex \(x\in U\) whenever \(\eta(x)\ge\deg_U(x)\). By the burning theorem, the configuration is recurrent exactly when every vertex can be deleted. The implementation chooses the lowest-index eligible vertex until no such vertex remains. For each recurrent \(\eta\), it adds a grain at the three representative vertices at distances one, two, three, stabilizes by repeatedly toppling the lowest-index unstable vertex, and records both the count of topplings and the bit mask of sites toppled.

The recurrence check rejects every nonrecurrent stable state and accepts exactly \(5,184,000\). The explicit CSV table is the complete accumulation of the 100 nonzero indexed counters. Every accepted configuration contributes exactly one term to every distance class, proving normalization. The code executes a bounded loop over all base-five vectors, so this is **exhaustive finite enumeration**, not sampling or an inference from a finite prefix of an infinite family. All toppling sequences terminate on a finite connected graph with a sink, and the Abelian property makes the resulting counts independent of the legal toppling order.

**Independent replay.** `verify_dhar.cpp` constructs the icosahedron using two staggered five-cycles and their poles rather than the first program's fixed edge list. It applies the **burning-addition criterion** instead: add a grain to each neighbor of the sink and stabilize; recurrence holds exactly when every nonsink vertex topples once and the starting heights are restored. It stabilizes using the **largest-index** unstable vertex. Both independent enumerators yield identical complete \((d,T,S)\)-counters. `verify.py` checks that every counter equals the supplied CSV, checks the three exact normalizations and support endpoints, and compiles and replays both programs.

The icosahedral graph has 120 automorphisms; the stabilizer of the chosen sink acts transitively on each sphere of radius one (five vertices), two (five vertices), and three (one vertex). Thus the three representative-source enumerations suffice for **every** source at each distance. Independently, the exact determinant of the 11-by-11 reduced graph Laplacian is \(5,184,000\), agreeing with the recurrent-state count by the matrix-tree theorem. The claimed maxima, the nearest-source single-toppling property, and the coefficient symmetry are immediate from the **exhaustive** table rather than extrapolation.

## Verification
Run `python3 verify.py` in the directory containing the two C++ files and `AVALANCHE_COUNTS.csv`, with a C++17 compiler available. It independently compiles and executes both complete enumerators, compares every coefficient and confirms each polynomial sums to \(5,184,000\). Auxiliary cross-checks confirmed the reduced-Laplacian determinant and sink-stabilizing automorphism orbits. In the first enumerator, each of the three source classes dissipates exactly \(5,184,000\) grains over all recurrent states, consistent with the exact stationary input-output conservation law. The finite certificate makes **no claim** to certify asymptotic avalanches on growing graphs.

## Relationship to prior work
Austin et al. [1] develop the general avalanche-polynomial formalism and compute explicit graph-family formulas for trees, cycles, complete graphs, and wheels. Reading the full publicly shared text (introduction, definitions, named family results and conclusion) shows no corresponding icosahedral computation. The present statistic retains the source distance and both **total topplings** and **distinct toppled vertices**, yielding an exact three-class joint census. Gauthier [2] studies avalanches on an expanded cactus, not on the icosahedron. The underlying burning test and recurrent-state/spanning-tree equivalence are classical [3] and are not new claims. A preexisting general identity for the coefficient counting full-support avalanches from sink-adjacent sources gives the isolated nearest-source \((11,11)\) coefficient; the other 99 coefficients and three-distance joint profile are not consequences of that isolated identity.

## Limitations
The result is a single finite, highly symmetric graph. The table is exact subject to correct implementation of the two transparently supplied algorithms, not a hand-derived closed-form family theorem. A literature search and comparison cannot exclude an unindexed or inaccessible historical joint distribution; independent priority review has not been performed. The count of distinct sites is not the same as the number of topplings when multiple topplings occur, especially at source distances two and three. Results neither establish infinite-volume exponents nor imply a thermodynamic phase transition.

## References
[1] Demara Austin, Megan Chambers, Rebecca Funke, Luis David García Puente, Lauren Keough, "The Avalanche Polynomial of a Graph", arXiv:1605.02713 (first public 2016-05-09), https://arxiv.org/abs/1605.02713.
[2] Gregory Gauthier, "Avalanche dynamics of the Abelian sandpile model on the expanded cactus graph", arXiv:1110.6263 (first public 2011-10-28), https://arxiv.org/abs/1110.6263.
[3] Deepak Dhar, "Self-organized critical state of sandpile automaton models", Physical Review Letters 64 (1990), 1613–1616; DOI 10.1103/PhysRevLett.64.1613.
