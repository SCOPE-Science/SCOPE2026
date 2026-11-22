# Exact power-domination and five-step relocation obstructions in the Doyle–Holt graph

## Finding

Let \(H\) be the 27-vertex Doyle–Holt graph, described explicitly in the next section. For standard power domination, \(\gamma_P(H)=3\), and there are exactly \(567\) minimum power-dominating triples. These triples fall into eleven orbits under \(\operatorname{Aut}(H)\), one of size \(27\) and ten of size \(54\). Precisely \(351\) triples finish observation in round five and \(216\) in round six. Every optimum triple has pairwise graph distances either \((2,3,3)\) (\(513\) triples) or \((3,3,3)\) (\(54\) triples).

Let \(R_J\) and \(R_S\) be the token-jump and edge-constrained token-slide reconfiguration graphs on these same \(567\) triples, with all intermediate configurations required to remain minimum power dominating. Then both graphs are connected. The jump graph has \(5400\) edges and radius and diameter four. The slide graph has \(1242\) edges, radius seven, diameter eight, and eccentricity distribution \(432\) vertices at seven and \(135\) at eight.

For every two optimum triples \(S,T\), their respective shortest-path lengths satisfy
\[
0\le d_{R_S}(S,T)-d_{R_J}(S,T)\le5.
\]
The upper bound is attained by exactly \(351\) unordered pairs, forming eight orbits under \(\operatorname{Aut}(H)\): five of size \(54\) and three of size \(27\). In particular, exactly \(54\) pairs have a one-step jump but need six slides. The complete slide-minus-jump difference distribution among \(\binom{567}{2}=160461\) unordered pairs is

| Extra slides | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Number of pairs | 12501 | 34830 | 54189 | 47250 | 11340 | 351 |

## Assumptions and scope

The graph's vertices are \(V=\{(x,y): x\in\mathbb Z_9,\ y\in\mathbb Z_3\}\). Each vertex \((x,y)\) is joined to the four distinct vertices
\[
(4x+1,y-1),\quad(4x-1,y-1),\quad(7x+7,y+1),\quad(7x-7,y+1),
\]
with coordinates reduced modulo \(9\) and \(3\). This is the Doyle–Holt presentation recorded by Weisstein, following Holt. For calculations, label \((x,y)\) by \(9y+x\), from \(0\) through \(26\). The resulting undirected graph is degree four, connected, has girth five, and is the smallest half-arc-transitive graph.

For a seed set \(S\), the synchronous power-domination process begins with observation of \(N_H[S]\) at round one. At each subsequent round, every currently observed vertex with exactly one unobserved neighbor forces that neighbor, using the observations available **at the start** of that round. A seed succeeds if all vertices are eventually observed. The minimum cardinality is \(\gamma_P(H)\). A token jump replaces one selected vertex by any unselected vertex; a slide does so only when the removed and inserted vertices are adjacent in \(H\). All reconfiguration vertices are optimum three-element sets, not arbitrary successful sets.

## Proof

This is a finite exhaustive theorem, with complete enumerations and independently coded representations; the proof does not infer an infinite assertion from sample runs. The finite domain contains exactly \(\binom{27}{1}=27\), \(\binom{27}{2}=351\), and \(\binom{27}{3}=2925\) possible seed sets of sizes one, two and three. Each is enumerated lexicographically by the self-contained `verify_bitset.py` program. Its inner observation recurrence is exactly the definition above: the initial bit set is \(N_H[S]\), and each synchronous iteration adds all unique unobserved neighbors, or returns failure when there are none. Since the observed set strictly increases on a nonterminal iteration and is contained in \(V\), this procedure terminates after at most \(27\) such increases and yields the exact answer for each candidate.

The complete enumeration finds no successful seed of cardinality one or two, and exactly \(567\) successful triples. The finish-round census and pair-distance-type count follow by tabulating those \(567\) triples. All \(\binom{567}{2}=160461\) unordered pairs are then assessed by explicitly inserting exactly those one-coordinate replacements whose destination triple occurs in the successful-triple table. For slides the exchanged two original vertices must additionally be adjacent in the graph. This construction tests all \(3\cdot24\) proposed replacements for every optimum triple, so there are no omitted transitions. Dividing the directed counts by two gives \(5400\) jump edges and \(1242\) slide edges.

Breadth-first search from each of the \(567\) vertices in each finite reconfiguration graph exhausts all shortest-path distances. Its reachability checks prove both graphs connected, its eccentricity maxima prove the claimed radii and diameters, and its complete pairwise difference table establishes the sharp five-slide penalty and the \(54\) one-jump/six-slide pairs. These counts are asserted explicitly in both `verify_bitset.py` and `verify_group.cpp`; the second program reconstructs the graph using a different, nonabelian-group Cayley presentation and uses a separate C++ enumeration.

Finally, `verify_orbits.py` enumerates all graph automorphisms (\(54\) in total) by exhaustive isomorphism backtracking, confirms that the two graph presentations are isomorphic, partitions the optimum triples into the stated eleven orbits, and partitions the \(351\) maximum-penalty unordered pairs into eight orbits of the stated sizes. Each asserted orbit is the complete image of a representative under all \(54\) automorphisms, and the program checks that the resulting orbits exhaust the relevant enumerated sets.

As an explicit witness of the extreme one-jump detour, the optimum triples with integer labels \(S=\{0,1,4\}\) and \(T=\{0,3,4\}\) differ by one vertex, but a shortest slide sequence has length six:
\[
\{0,1,4\}\to\{1,4,16\}\to\{4,16,21\}\to\{4,5,16\}
\to\{4,10,16\}\to\{0,4,10\}\to\{0,3,4\}.
\]
Each triple in the displayed sequence appears in the complete successful-triple table, and each arrow removes and inserts adjacent vertices in \(H\). No shorter slide path exists by the exhaustive BFS distances.

## Verification

From the unpacked directory containing the supplied files, run `sh REPRODUCE.sh` with Python 3, a C++17 compiler, and NetworkX. It executes three checks, which together rebuild the graph in coordinate and group presentations, enumerate every small seed set, construct all exact legal moves, perform full shortest-path searches, and check the automorphism orbits. Outputs include the optimum count, latency census, reconfiguration counts, diameters, complete distance-penalty census, and orbit sizes. The plain standard-library checker and C++ checker require no external mathematical databases; only `verify_orbits.py` requires NetworkX. Both main programs assert exact numerical outcomes rather than relying on human examination of logs.

## Relationship to prior work

Bjorkman, Bozeman, Ferrero, Flagg, Grood, Hogben, Jacob and Reinhart initiated power-domination reconfiguration and established definitions and results for token addition/removal and jumping, with general graph constructions. Their Sections 3–5 discuss generic properties and families such as paths, cycles, wheels and bicliques, not the exact three-sensor geometry of the Doyle–Holt graph. Doyle's original construction establishes the 27-vertex half-arc-transitive graph, not any power-domination or relocation counts. Weisstein records a convenient coordinate construction. Those existing graph-theoretic definitions and graph construction are credited, not claimed as novel. The full source-specific claims above are the new exact computations.

## Limitations

The claim concerns precisely this named 27-vertex graph under synchronous standard power domination and a fixed minimum number of three sensors. It does not supply a theorem for all half-arc-transitive graphs or all power-domination reconfiguration problems. Computational exhaustiveness is finite and reproducible; correctness depends on the implementation matching the stated graph and rules, which is checked by the separate formulations. Searches of indexed records and accessible primary literature have not identified an equivalent result; this is not a proof of global uniqueness. The reviewed 2022 preprint was accessible in full; the JavaScript-based House of Graphs entry was not materially accessible, so possible unindexed table overlap remains a limited risk. No external independent mathematical audit has been performed.

## References

1. B. Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798v1 (first posted 2022-01-05), https://arxiv.org/abs/2201.01798 .
2. P. G. Doyle, *A 27-vertex graph that is vertex-transitive and edge-transitive but not 1-transitive*, arXiv:math/0703861v1 (2007), https://arxiv.org/abs/math/0703861 .
3. E. W. Weisstein, *Doyle Graph*, MathWorld, https://mathworld.wolfram.com/DoyleGraph.html .
4. B. Brimkov et al., *Power domination polynomials of graphs*, arXiv:1805.10984 (2018), https://arxiv.org/abs/1805.10984 (abstract consulted for related counting context).
