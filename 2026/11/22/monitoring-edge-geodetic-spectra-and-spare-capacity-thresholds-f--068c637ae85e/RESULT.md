# Monitoring edge-geodetic spectra and spare-capacity thresholds for three Petersen covering graphs

## Finding
Consider the Petersen graph \(P=GP(5,2)\) and the two distinguished connected cubic double covers \(D=GP(10,2)\) and \(H=GP(10,3)\), respectively the dodecahedral and Desargues graphs. For a graph \(G\), let \(M_G(z)=\sum_{S\subseteq V(G),\ S\text{ monitoring}}z^{|S|}\), and let \(I_G(z)\) count *inclusion-minimal* monitoring edge-geodetic sets in the same way. Then
\[
\begin{aligned}
M_P(z)&=5z^6+30z^7+30z^8+10z^9+z^{10},\\
I_P(z)&=5z^6+10z^7;\\
M_D(z)&=25z^8+1840z^9+13686z^{10}+37020z^{11}+54000z^{12}\\
&\quad+49880z^{13}+31650z^{14}+14392z^{15}+4765z^{16}\\
&\quad+1140z^{17}+190z^{18}+20z^{19}+z^{20},\\
I_D(z)&=25z^8+1540z^9+2006z^{10};\\
M_H(z)&=2z^{10}+20z^{11}+115z^{12}+480z^{13}+1320z^{14}\\
&\quad+1924z^{15}+1510z^{16}+660z^{17}+160z^{18}+20z^{19}+z^{20},\\
I_H(z)&=2z^{10}+25z^{12}+60z^{13}+100z^{14}.
\end{aligned}
\]
In particular, the monitoring edge-geodetic numbers are \(\operatorname{meg}(P)=6\), \(\operatorname{meg}(D)=8\), and \(\operatorname{meg}(H)=10\); the numbers of minimum configurations are respectively \(5,25,2\). The five Petersen optima are exactly the complements of its five maximum independent four-sets. Of the twenty-five dodecahedral optima, five are its five maximum independent eight-sets (the five inscribed cubes); each of the other twenty induces precisely three vertex-disjoint edges and two isolated vertices. The only two Desargues optima are its two bipartition classes.

Define the *bounded monitoring reconfiguration graph* \(\mathcal R_b(G)\) to have all monitoring vertex subsets of size at most \(b\) as vertices and edges between subsets that differ by exactly one vertex, so every intermediate configuration also monitors every graph edge. The least budget \(b\) for which \(\mathcal R_b(G)\) is connected is respectively \(8,11,15\) for \(P,D,H\). Thus the exact extra-position budgets beyond the optimum are \(2,3,5\). At the preceding budgets \(7,10,14\), respectively, there are \(15,2007,101\) connected components; at \(8,11,15\), respectively, all \(65,52571,3861\) available states lie in one component.

The usual minimum vertex-cover sizes are \(\tau(P)=6\), \(\tau(D)=12\), and \(\tau(H)=10\). Hence the dodecahedron has a *strict four-position saving* relative to monitoring by a vertex cover, while the other two graphs attain the vertex-cover bound. This illustrates that a monitoring set need not be a vertex cover; in particular five dodecahedral optima are themselves independent sets.

## Assumptions and scope
All graphs are finite, simple, undirected and unweighted. The generalized Petersen graph \(GP(n,k)\) here has precisely the \(2n\) vertices \(u_i,v_i\), indexed modulo \(n\), and exactly the \(3n\) edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+k}\), with undirected edge duplicates removed (none occur for the three stated parameter pairs). In the primary finite checker the labels are \(u_i=i\) and \(v_i=n+i\). The Desargues graph is also isomorphic to the inclusion-incidence graph of the two- and three-element subsets of a five-element set. The Petersen graph is isomorphic to \(KG(5,2)\).

A distinct pair \(s,t\) *monitors* an edge \(e\) if every shortest \(s\)-\(t\) path contains \(e\), equivalently if \(d_{G-e}(s,t)>d_G(s,t)\). A vertex subset is monitoring if every edge is monitored by at least one selected pair. A monitoring set is inclusion-minimal if deleting any one selected vertex destroys this property. The reconfiguration graph uses additions and deletions, **not** simultaneous replacements or token sliding. Empty budgets below the minimum are excluded from connectivity assertions. All counts are for distinct *labelled subsets*, without quotienting by graph automorphisms.

## Proof
**1. Finite witness characterization.** For any fixed graph and unordered vertices \(s,t\), compute the edge set
\[
B_{st}=\{e\in E(G):d_{G-e}(s,t)>d_G(s,t)\}.
\]
The equivalence in the definition shows rigorously that a set \(S\) is monitoring if and only if \(\bigcup_{\{s,t\}\subseteq S}B_{st}=E(G)\). This is an exact characterization for all selected subsets, not a sample of shortest paths.

**2. Exact exhaustive recurrence.** Order the \(3n\) graph edges and encode every \(B_{st}\) as its exact edge bitmask. For the empty selected mask set \(C(\varnothing)=0\); for a nonempty selected mask \(S\), let \(v\) be its lowest-index selected vertex and put \(T=S\setminus\{v\}\). Then
\[
C(S)=C(T)\mathbin{\vert}\bigvee_{u\in T} B_{vu},
\]
where the operations are bitwise union. Induction on \(|S|\) proves that \(C(S)\) encodes exactly the set of monitored edges. The standalone `verify_meg.cpp` computes each \(B_{st}\) with breadth-first distances in \(G\) and in all the single-edge-deleted graphs, evaluates this recurrence for **all** \(2^{10}\) subsets of \(P\) and all \(2^{20}\) subsets of each cover, and records every successful cardinality. By monotonicity, a successful \(S\) is inclusion-minimal if and only if every one-vertex deletion fails, which gives exactly the displayed \(I_G\) coefficients. Enumerating the graph-induced edges of all optimizers gives the stated optimum structures.

**3. A distinct shortest-path multiplicity check.** The second standalone checker, `verify_meg_independent.py`, computes shortest-path distances \(d\) and numbers \(\sigma(s,t)\) by increasing-distance breadth-first propagation, without deleting edges. For an edge \(e=ab\), the number of shortest \(s\)-\(t\) paths traversing \(a\) to \(b\) is \(\sigma(s,a)\sigma(b,t)\) exactly when \(d(s,a)+1+d(b,t)=d(s,t)\); otherwise it is zero. Add the reverse orientation (the two possibilities are disjoint for shortest paths). The edge is monitored precisely if this total equals \(\sigma(s,t)\). The checker builds the resulting witness masks and enumerates every selected subset by a different highest-bit recurrence. It separately constructs \(P\) as \(KG(5,2)\) and \(H\) as a two-/three-subset incidence graph. Both checkers reproduce all six polynomials and the optimum structures in the assertion itself. The computation is finite but **exhaustive**, not an extrapolation to larger generalized Petersen graphs.

**4. Sharp relocation thresholds.** For each cardinality cap, the checkers construct the full induced subgraph on successful masks of permitted size and run exhaustive breadth-first connected-component searches under one-bit toggles. For \(P\) at cap \(7\), the components have sizes \(1\) (ten times) and \(5\) (five times); at cap \(8\) all \(65\) states are connected. For \(D\) at cap \(10\), there are \(2006\) singleton components and one component of size \(13545\); at cap \(11\) all \(52571\) states are connected. For \(H\) at cap \(14\), there are \(100\) singleton components and one component of size \(1837\); at cap \(15\) all \(3861\) states are connected. The uppermost inclusion-minimal sizes are \(7,10,14\). At those caps, any inclusion-minimal set of maximal size is isolated: deletion destroys monitoring while addition exceeds the budget. Since other valid states exist, this proves **necessity** of at least one further position; exhaustive connectedness at the next caps proves sufficiency.

**5. Comparison to vertex covers.** The second checker also exhaustively enumerates all independent subsets and obtains the independence numbers \(4,8,10\), with respectively \(5,5,2\) maximum independent sets. Their complementary vertex-cover numbers are consequently \(6,12,10\). The optimum monitoring census from Steps 2 and 3, not the vertex-cover bounds, establishes the strict dodecahedral gap.

## Verification
With a C++17 compiler and Python 3 standard library, execute `g++ -O2 -std=c++17 verify_meg.cpp -o verify_meg && ./verify_meg` and then `python3 verify_meg_independent.py`. The two source files are embedded beside this document; `verification_output.txt` contains actual program outputs. All arithmetic is integral and every selected subset is tested. The C++ program asserts all six polynomials, the optimum geometry and exact component multisets at each relevant budget. The Python program implements a different shortest-path criterion, independently constructs two graphs, checks the same polynomials and component sizes, and separately checks the independent-set extrema. Both finish with success markers. No randomization, nonstandard package, remote service, or external dataset is required.

## Relationship to prior work
Dev, Dey, Foucaud, Narayanan and Ramasubramony Sulochana introduced monitoring edge-geodetic sets (first arXiv posting 2022-10-07), determining the minimum for trees, cycles, unicyclic graphs, complete/multipartite graphs, grids and hypercubes. Haslegrave (arXiv 2022-10-17) gave hardness and product bounds, not the three graphs here. Foucaud, Marcille, Myint, Sandeep, Sen and Taruni (arXiv 2024-03-14, Theorem 6.3 in the 2025 preprint) prove that any vertex cover of a connected minimum-degree-at-least-two girth-at-least-five graph is monitoring. That theorem only proves a sufficient condition and hence an **upper bound** \(\operatorname{meg}(G)\le\tau(G)\); it does not imply the enumerators or reconfiguration thresholds. The dodecahedral strict inequality and its independent optimum configurations demonstrate concretely why its converse fails here.

Published results on the two covers' induced-matching complexes establish their common Petersen quotient and describe different *simplicial homotopy* invariants, which do not control shortest-path edge-failure witnesses. A separate published dodecahedral independence-complex result explicitly establishes the five maximum independent eight-sets; their existence is credited, not claimed as novel. Targeted searches of published research records, primary arXiv text and bibliographic queries found no statement implying the complete finite classification and the three sharp capacity thresholds. Negative search results alone do not prove worldwide priority.

## Limitations
These are exact finite theorems for three specified graphs, **not** a formula for all cubic double covers or the whole family \(GP(n,k)\). The comparison of cover graphs does not assert monotonicity under graph covers, nor a general relation between minimum monitoring size and maximum inclusion-minimal size. The proof relies on fully reproducible finite enumeration and exact BFS certificates. Possible unindexed tables or equivalent earlier computations remain a residual priority risk.

## References
1. S. R. Dev, S. Dey, F. Foucaud, K. Narayanan, L. Ramasubramony Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774, first posted 2022-10-07, https://arxiv.org/abs/2210.03774 .
2. J. Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, arXiv:2210.08955, first posted 2022-10-17, https://arxiv.org/abs/2210.08955 .
3. F. Foucaud, C. Marcille, Z. M. Myint, R. B. Sandeep, S. Sen, S. Taruni, *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs*, arXiv:2403.09122, first posted 2024-03-14, https://arxiv.org/abs/2403.09122 .
4. *Equal sphere multiplicities in different degrees for two Petersen double covers*, prior published combinatorics result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-equal-sphere-multiplicities-in-different-degrees-for-two-peterse--6a8674c7694e .
5. *Integral five-cube quotient lattice in dodecahedral independence homology*, prior published combinatorics result (maximum independent octets established there), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-integral-five-cube-quotient-lattice-in-dodecahedral-independence--6135c3416108 .
