# A fixed-point basin inversion under NOR dynamics on the two Petersen double covers

## Finding

Let \(G_k=GP(10,k)\) for \(k\in\{2,3\}\), with \(G_2\) the dodecahedral graph and \(G_3\) the Desargues graph. Under synchronous open-neighborhood NOR, the dodecahedron has **295 fixed configurations**, more than the Desargues graph's **187**, but only **745** of its \(2^{20}\) labelled initial states enter fixed points, versus **1,941** for Desargues. This is a fixed-point-count versus attraction-basin reversal between two cubic twenty-vertex covers of the same Petersen graph.

| Exact invariant | Dodecahedral \(G_2\) | Desargues \(G_3\) |
|---|---:|---:|
| Initial configurations | 1,048,576 | 1,048,576 |
| Fixed configurations | 295 | 187 |
| Primitive two-cycle attractors | 19,830 | 17,391 |
| States initially periodic | 39,955 | 34,969 |
| States first periodic after one update | 1,008,621 | 1,013,607 |
| States attracted to fixed points | 745 | 1,941 |
| States attracted to two-cycles | 1,047,831 | 1,046,635 |
| Largest fixed-point basin | 35 | 388 |
| Basin of the all-zero/all-one two-cycle | 156,533 | 150,545 |

The full **fixed-point** basin-size spectra (size: number of fixed points with that basin size) are

- \(G_2\): \(1:70,\ 2:160,\ 3:60,\ 35:5\).
- \(G_3\): \(1:100,\ 6:60,\ 25:5,\ 29:20,\ 388:2\).

The two size-388 Desargues fixed points are precisely its two bipartition shores. Their 388-element basins each consist of subsets of that shore dominating every vertex of the opposite shore. The associated subset-size distribution for either basin is \(4:10,\ 5:72,\ 6:140,\ 7:110,\ 8:45,\ 9:10,\ 10:1\). The two-cycle basin spectra, including every multiplicity, appear in the embedded census files.

## Assumptions and scope

The graphs are simple and undirected, with vertex set \(\{u_i,v_i:i\in\mathbb Z/10\mathbb Z\}\). Edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+k}\) for each \(i\) (indices modulo 10). Reduction of indices modulo five gives a two-sheeted covering map from each to the standard Petersen graph \(GP(5,2)\): for \(k=3\), the inner stride maps to the same undirected step as \(k=2\). No self-loops, asynchronous updates, tie conventions, external inputs, random initialization, or alternate NOR definitions are included.

A configuration is a vertex subset \(S\), with ones at exactly the vertices in \(S\). Its synchronous update is
\[F_G(S)=\{w\in V(G):N_G(w)\cap S=\varnothing\}.\]
A primitive two-cycle is one unordered pair \(\{A,B\}\) with \(F_G(A)=B\), \(F_G(B)=A\), and \(A\ne B\). The *attraction basin* of a fixed configuration or two-cycle contains every initial state whose eventual periodic orbit equals that attractor, including states on the orbit. First periodic-entry time is zero for already-periodic states.

## Proof

**Structural reduction (all finite undirected graphs).** For any subset \(S\), no neighbor of any vertex in \(S\) belongs to \(F(S)\); hence \(S\subseteq F^2(S)\). The map \(F\) reverses inclusion, so \(F^3(S)\subseteq F(S)\). Applying the same extensivity to \(F(S)\) gives \(F(S)\subseteq F^3(S)\). Thus \(F^3=F\), proving the exact one-update ceiling for reaching a fixed point or two-cycle. A fixed configuration satisfies \(F(S)=S\); equivalently, \(S\) is independent and dominates its complement, i.e. is a maximal independent set. These general reductions are known context, not presented as a new general theorem.

**Finite exact census.** For each of the \(2^{20}\) subsets, the standalone `nor20.cpp` constructs all 20 neighbor bitmasks from the three defining edge families, applies \(F\), and uses indegree peeling on the full functional graph to recover cycles, primitive periods, attraction basins, and first-entry depths. No sampling, truncation, heuristic search, or partial orbit exploration is involved. The output is recorded separately for both \(k=2\) and \(k=3\). Distinct methods in `nor20_verify.py` instead compute \(F(S)\) by vectorized bitmask operations, use \(\min(F(S),F^2(S))\) as the canonical recurrent-orbit key, count its full fiber, and enumerate fixed configurations directly via maximal-independent-set Boolean conditions. These methods agree on every basin multiplicity and the table above.

For the Desargues graph, the fixed-point basins of size 388 are the complementary ten-vertex bipartition shores. A state maps to a shore \(A\) precisely when it is a subset of \(A\) dominating the opposite shore; direct enumeration of its \(2^{10}\) possible subsets gives 388 and the stated weight distribution. For either graph, \(F(\varnothing)=V\), \(F(V)=\varnothing\), and an initial configuration enters that two-cycle exactly if it is empty or is a total dominating set; direct counting gives the two dominant basin sizes.

The two independent whole-state enumerations imply the claimed numerical inversion: \(295>187\), while \(745<1,941\). Their complete basin multiplicities certify the two exceptional 388-basin fixed states and the unique largest two-cycle basin in each graph.

## Verification

With a C++17 compiler, use `g++ -std=c++17 -O3 nor20.cpp -o nor20`, then execute `./nor20 2` and `./nor20 3`. The exact output is recorded in `dodecahedral_census.txt` and `desargues_census.txt`. An independent implementation of the counting identities uses Python 3 with NumPy: `python nor20_verify.py`; compare its printed spectra with `vectorized_check.txt`. The vectorized program separately checks \(F^3(S)=F(S)\) for every state, identifies the maximal-independent-set fixed configurations, verifies the total-dominating-set interpretation of the dominant two-cycle, and sums all attractor basin sizes back to \(2^{20}\). Both edge definitions were also matched to the standard dodecahedral and Desargues graph models by graph isomorphism.

## Relationship to prior work

The equality of NOR fixed states and maximal independent sets is classical and appears explicitly in Aracena–Richard–Salinas, arXiv:1507.06141 (first public version 2015-07-22), Proposition 1. Aledo and collaborators (2020) study general minterm/maxterm parallel graph dynamics and combinatorial periodic-point bounds; their full-text treatment does not tabulate the two Petersen covers or the exact basin reversal here. Related graph-specific majority-rule censuses use a different transition operator, while known NOR results on Kneser graphs and leaf coronas involve different graph families. The genuinely graph-specific statement here is the exact comparison of fixed versus attracted initial states, all basin distributions, and the two distinguished large Desargues fixed-point basins—not the general fact \(F^3=F\).

## Limitations

This is a finite, exact result restricted to two specified twenty-vertex graphs and synchronous open-neighborhood NOR. It does not give a closed formula for arbitrary graph covers or a limit theorem for growing graph families. The computational claim is exhaustive only because each graph has exactly \(2^{20}\) states and each was evaluated. Historical searches cannot exclude unindexed equivalent tables. No independent external scientific audit has been performed.

## References

1. J. Aracena, A. Richard, L. Salinas, *Fixed points in conjunctive networks and maximal independent sets in graph contractions*, arXiv:1507.06141, first public 2015-07-22, https://arxiv.org/abs/1507.06141.
2. J. A. Aledo et al., *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), DOI:10.1155/2020/9708347, https://doi.org/10.1155/2020/9708347.
3. Related indexed mathematical findings on majority dynamics of the dodecahedral and Desargues graphs and NOR dynamics on Kneser graphs and leaf coronas, used only for claim-level comparison; see the originality comparisons in `AUDIT.json`.
