# A five-landmark obstruction and an eight-step relocation geometry on the Möbius–Kantor graph

## Finding
Let \(M=GP(8,3)\), the sixteen-vertex cubic Möbius–Kantor graph, with ordinary vertex-to-edge distances. A **vertex–edge dominant edge-resolving set** is a vertex subset that (i) distinguishes every two edges by their vectors of distances to the selected vertices and (ii) lies at distance at most one from every edge. Its minimum cardinality is \(\gamma_{emd}\). The exact values for this graph are
\[
\beta_e(M)=4,\qquad \gamma_{ve}(M)=4,\qquad \gamma_{emd}(M)=5.
\]
There are precisely \(368\) minimum ordinary edge-resolving four-sets and \(128\) vertex–edge dominating four-sets, but **none** satisfies both conditions. There are exactly \(512\) minimum joint configurations. In fact the complete labelled cardinality polynomial, which includes all feasible sets rather than only minima, is
\[
\begin{aligned}
J_M(z)={}&512z^5+3432z^6+8560z^7+11790z^8+11200z^9\\
&+7984z^{10}+4368z^{11}+1820z^{12}+560z^{13}\\
&+120z^{14}+16z^{15}+z^{16}.
\end{aligned}
\]
Thus \(J_M(1)=50363\). The full graph automorphism group has \(96\) elements and the \(512\) minimum sets occupy precisely eight orbits, of sizes \(32,48,48,48,48,96,96,96\).

Consider two graphs on these \(512\) minimum subsets. A **jump** removes one selected vertex and inserts any unselected vertex; a **slide** requires the removed and inserted vertices to be adjacent in \(M\). Every intermediate configuration must still satisfy both landmark requirements. Both reconfiguration graphs are connected. The slide graph has \(1320\) edges and **every state has eccentricity eight**, giving radius and diameter \(8\) despite unequal degrees. The jump graph has \(3616\) edges, radius \(5\) and diameter \(6\). Its eccentricities are \(5\) for \(368\) configurations and \(6\) for \(144\) configurations.

## Assumptions and scope
The graph is finite, simple and undirected. Its vertices are \(u_i,v_i\), \(0\le i\le7\), with indices modulo eight. Its edges are precisely \(u_iu_{i+1}\), \(u_iv_i\) and \(v_iv_{i+3}\), for every \(i\in\{0,\ldots,7\}\). Encode \(u_i\) as integer \(i\) and \(v_i\) as \(8+i\). There are \(16\) vertices and \(24\) edges. For a vertex \(x\) and edge \(ab\), define \(d(x,ab)=\min\{d_M(x,a),d_M(x,b)\}\). We say \(x\) dominates the edge \(ab\) when \(d(x,ab)\le1\). For distinct edges \(e,f\), a vertex \(x\) distinguishes them when \(d(x,e)\ne d(x,f)\). All subsets, polynomials and reconfiguration states are **labelled**; no symmetry quotient is used except in the explicit orbit statement. All paths in the reconfiguration graphs preserve the minimum cardinality five.

## Proof
The result is a finite exact theorem with two standalone, differently constructed exhaustive certificates.

**Witness characterization.** For each edge \(e=ab\), let \(C_e=N_M[a]\cup N_M[b]\), where brackets denote the closed neighborhood. For each unordered pair of distinct edges \(e,f\), let \(W_{ef}=\{x\in V(M):d(x,e)\ne d(x,f)\}\). A vertex set \(S\) is vertex–edge dominant exactly when \(S\cap C_e\ne\varnothing\) for all \(24\) edges. It is edge-resolving exactly when \(S\cap W_{ef}\ne\varnothing\) for all \(\binom{24}{2}=276\) pairs. These are *if and only if* statements directly from the definitions, so together they give a complete finite test with \(300\) explicit nonempty-intersection constraints, not a necessary-only bound.

**Exhaustive independent computation of the polynomial and threshold.** `verify_mk.py` constructs all \(24\) edges, performs breadth-first shortest-path calculations from every vertex, and computes for every subset \(S\subseteq V(M)\) the actual \(24\) edge-distance tuples and the edges covered by \(S\). It examines **all** \(2^{16}=65536\) binary masks. `verify_mk_independent.cpp`, independently, computes vertex distances by Floyd–Warshall and constructs the \(276\) pair-separation witness masks and \(24\) edge-cover witness masks; it checks each of the same \(65536\) subsets by bitwise hitting tests rather than by building metric signatures. Both obtain the displayed polynomial, no joint subset of size at most four, and \(512\) joint sets of size five. The first program separately finds no dominating or resolving set of size at most three, exactly \(128\) dominating four-sets and exactly \(368\) resolving four-sets. The second independently checks both four-set counts. This exhausts all possible witnesses and configurations, proving all stated cardinality claims.

**Complete reconfiguration metrics.** Each program builds the exact set of all \(512\) feasible size-five masks. A pair of distinct masks represents a single replacement if and only if its symmetric difference consists of one removed and one inserted vertex; a slide additionally requires that ordered removal/insertion pair to be an edge of \(M\). `verify_mk.py` generates every allowable move from every state, while `verify_mk_independent.cpp` independently searches all ordered selected/unselected position pairs. They agree on \(1320\) undirected slide edges and \(3616\) undirected jump edges. Both conduct a complete breadth-first shortest-path search rooted at **each** of the \(512\) states. Their searches reach all states in both graphs and establish the exact eccentricities, radii and diameters displayed above. In particular, the entire slide graph, not a sampled subgraph, has eccentricity eight at every state.

**Symmetry certificate.** `verify_mk.py` further enumerates all graph automorphisms by assigning every vertex to a possible image subject to adjacency and nonadjacency with each vertex already assigned, backtracking through all choices. It finds precisely \(96\) permutations. Applying all of them to each as-yet-unclassified feasible size-five subset produces disjoint orbits with respective sizes and bitmask representatives
\[
(96,\mathrm{0x18e}),\ (96,\mathrm{0x1a6}),\ (48,\mathrm{0x1aa}),\ (96,\mathrm{0x34c}),\\
(48,\mathrm{0x354}),\ (48,\mathrm{0x394}),\ (48,\mathrm{0x52a}),\ (32,\mathrm{0x54a}).
\]
Their sizes add to \(512\) and they cover the complete optimum list. The first coordinate denotes the orbit size and the hexadecimal number is the encoded representative mask. This is exhaustive, not a probabilistic automorphism search: a graph automorphism is exactly a permutation preserving the adjacency relation, and every allowed candidate image is explored.

The proof uses exhaustive coverage of one fixed sixteen-vertex graph. Neither bounded experiments on growing graphs nor an infinite-order extrapolation is invoked.

## Verification
Execute the two supplied self-contained sources from a directory containing them:

```sh
python3 verify_mk.py
g++ -std=c++17 -O2 -Wall -Wextra verify_mk_independent.cpp -o verify_mk_independent
./verify_mk_independent
```

Successful terminal markers are `MK_EDGE_LANDMARK_VERIFY_OK` and `INDEPENDENT_PAIR_HITTING_CHECK_OK`. The Python checker also verifies the eight symmetry orbits and all eccentricity distributions; the C++17 checker verifies the polynomial, the separate size-four counts, all-optimum connectivity, edge counts, radii and diameters. They reconstruct the host graph from its edge rule and rely only on standard libraries. The exact source texts are embedded as standalone artifacts. The mathematical claims are those encoded by these full exhaustive computations, not mere conjectures inferred from a log.

## Relationship to prior work
Ikhlaq, Hayat and Siddiqui [1] introduced the combined vertex–edge domination/edge-resolving parameter and studied several classical graph families and Cartesian products; their result does not enumerate its realizations on \(GP(8,3)\). Filipović, Kartelj and Kratica [2] treated edge metric dimension for generalized Petersen graphs, giving exact formulas for inner steps one and two and lower bounds more generally; neither joint edge coverage nor the present complete Möbius–Kantor census and relocation geometry follows from those results. Independent indexed research on complete prisms [3] determines the same combined parameter on \(K_n\square K_2\), but those are different host graphs and its structural characterization does not apply to the Möbius–Kantor graph.

Other known Möbius–Kantor configuration censuses [4,5] concern closed-neighborhood identifying codes and ordinary zero forcing respectively, not the simultaneous constraints \(C_e\) and \(W_{ef}\). Their reconfiguration graphs consequently have different vertices and feasibility criteria; matching words such as 'self-centered' or 'token slides' does not make them covering results. A targeted literature and indexed-record comparison found no statement implying this exact combined census or metric; that negative search is not proof of historical uniqueness.

## Limitations
The calculation is a complete finite theorem for this one canonical sixteen-vertex graph, not an all-order result for the generalized Petersen family. Vertex–edge domination uses distance at most one from an edge; the edge metric uses distances from vertices to edges, not the line-graph metric. The symmetry classes describe unweighted labelled optimum sets. The all-pairs reconfiguration metrics are exact finite certificates, not symbolic formulas for arbitrary graphs. Publication priority can be affected by unindexed or inaccessible studies. No independent external scholarly audit has been performed.

## References
[1] H. M. Ikhlaq, S. Hayat and H. M. A. Siddiqui, *Unique identification and domination of edges in a graph: The vertex-edge dominant edge metric dimension*, arXiv:2211.09327, first publicly posted 2022-11-17, https://arxiv.org/abs/2211.09327

[2] V. Filipović, A. Kartelj and J. Kratica, *Edge metric dimension of some generalized Petersen graphs*, arXiv:1807.00580, first publicly posted 2018-07-02, https://arxiv.org/abs/1807.00580

[3] *Exact vertex-edge dominant edge-metric bases of complete prisms*, research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-vertex-edge-dominant-edge-metric-bases-of-complete-prisms--458dd571fbf7

[4] *Frozen and mobile minimum identifying codes of the Möbius–Kantor graph*, research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-frozen-and-mobile-minimum-identifying-codes-of-the-m-bius-kantor--de0bfc0e8a82

[5] *A self-centered, nonregular zero-forcing exchange graph on 1,704 configurations*, research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-self-centered-nonregular-zero-forcing-exchange-graph-on-1-704--81c4ae0ea3cb
