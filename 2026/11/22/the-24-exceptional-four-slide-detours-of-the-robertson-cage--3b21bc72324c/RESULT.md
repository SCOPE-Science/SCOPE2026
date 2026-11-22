# The 24 exceptional four-slide detours of the Robertson cage

## Finding

Let \(G\) be the Robertson \((4,5)\)-cage on 19 vertices, explicitly represented in `graph_edges.txt`. Under standard power domination, its minimum sensor count is \(\gamma_P(G)=3\), and exactly 753 triples are minimum power-dominating sets. Among these, respectively 109, 320, 204, and 120 finish observation in rounds two, three, four, and five, counting the initial closed-neighborhood observation as round one.

Let \(J\) be the token-jump graph on these 753 optima and \(T\) their token-slide graph. Both are connected. The jump graph has 14,538 edges and radius and diameter three. The slide graph has 3,452 edges, radius six, and diameter seven. Precisely 717 slide states have eccentricity six and 36 have eccentricity seven.

For all unordered pairs of distinct optimum configurations, the exact counts at slide-minus-jump distance excess \(0,1,2,3,4\) are

\[
(29{,}788,\ 131{,}574,\ 109{,}054,\ 12{,}688,\ 24).
\]

Thus the **sharp extra locality cost** is four slides, incurred by exactly 24 unordered pairs. Those are also precisely the 24 slide-diametral pairs. Every one consists of disjoint optimal triples each requiring four observation rounds, has jump distance three and slide distance seven, and all 24 pairs form one orbit under graph automorphisms. For example, \(S=\{1,3,8\}\) and \(U=\{11,14,15\}\) are such a pair. The 36 slide-eccentricity-seven configurations are exactly the endpoints of these 24 pairs.

## Assumptions and scope

The graph is finite, undirected, simple and labelled by \(1,\ldots,19\). Its edge set is the cycle \((1,2),\ldots,(18,19),(19,1)\), the 18 chords

\[
\begin{gathered}
(1,5),(2,14),(3,18),(4,12),(6,17),(7,19),(8,16),(9,13),(10,15),\\
(1,16),(3,8),(4,15),(5,9),(6,14),(7,12),(10,19),(11,17),(13,18),
\end{gathered}
\]

and the edge \((2,11)\). The identical 38 edges are listed once each in `graph_edges.txt`. Each vertex has degree four and the girth is five, as independently checked by the embedded programs and as expected for the Robertson cage. The graph has 19 vertices and 38 edges.

For any sensor set \(S\), the initial observed set is \(P_1(S)=N_G[S]\). Subsequently, all forced vertices are added *simultaneously*:

\[
P_{t+1}(S)=P_t(S)\cup\{v:\exists u\in P_t(S),\ N_G(u)\setminus P_t(S)=\{v\}\}.
\]

The set is power dominating exactly when some \(P_t(S)=V(G)\). An optimum configuration is a successful set with minimum cardinality. Two optima are adjacent in \(J\) precisely when they share two vertices; they are adjacent in \(T\) precisely when, in addition, the removed and inserted vertices are adjacent in \(G\). Distances \(d_J\) and \(d_T\) always refer to shortest paths through optimum configurations, never through non-optimum placements.

## Proof

**Finite exhaustive certificate for the minimum.** Enumerate all labelled singleton sets, all \(\binom{19}{2}=171\) pairs, and all \(\binom{19}{3}=969\) triples. For each, start with its closed neighborhood and repeat the rule above until either every vertex is observed or a stationary proper observed set is reached. No singleton and no pair succeeds; exactly 753 triples succeed. Their completion-round counts are 109, 320, 204 and 120. The finite search is exhaustive because each of the above classes is represented by every increasing tuple in the code.

**Finite exhaustive certificate for the metrics.** Index all 753 successful triples and for each pair differing in one selected vertex insert a jump edge; retain that edge for sliding exactly when the exchanged original vertices are adjacent. The two generated graphs have respectively 14,538 and 3,452 unordered edges. Run breadth-first search from each of the 753 states on each graph. Every search reaches every state. Because breadth-first search explores all vertices in nondecreasing walk length, its first-visit labels are exact shortest-path distances. These 1,506 searches yield the following complete pair-distance counts, each summing to \(\binom{753}{2}=283{,}128\):

| Distance | Jump pairs | Slide pairs |
| --- | ---: | ---: |
| 1 | 14,538 | 3,452 |
| 2 | 104,022 | 20,484 |
| 3 | 164,568 | 67,788 |
| 4 | 0 | 110,994 |
| 5 | 0 | 70,116 |
| 6 | 0 | 10,270 |
| 7 | 0 | 24 |

The same distance arrays give the eccentricities and the five-class excess distribution stated above. In particular the only slide-distance-seven pairs have jump distance three, and the only excess-four pairs have slide distance seven; both classes contain the same 24 pairs. Each exceptional pair consists of disjoint triples and both have four-round completion times.

**Symmetry certificate.** Label vertices internally by \(0,\ldots,18\). The program `verify_bitset.py` contains two explicit permutations `g1` and `g2`. It verifies that each preserves all 38 graph edges and that their permutation-group closure has exactly 24 elements. Applying this group to one excess-four pair generates 24 distinct unordered pairs, exactly the exhaustive excess-four set. This proves the orbit statement without assuming completeness of the automorphism group. The union of their endpoints is exactly the independently identified set of 36 slide-eccentricity-seven states.

All conclusions are for the **fully specified 19-vertex graph**. The proof is an exhaustive finite proof, not an inference from a sample of graphs or from an incomplete search.

## Verification

Run `sh REPRODUCE.sh` with Python 3, a C++17 compiler, and the four machine-readable/reproducible files in the same directory. `verify_bitset.py` implements bit-mask parallel forcing, builds both complete reconfiguration graphs, performs every breadth-first search, checks the symmetry generators, and asserts all displayed counts. The separately written `verify_independent.cpp` uses 19-element Boolean observation arrays, an independent configuration generator and independent breadth-first searches; it asserts the minimum, both complete pair-distance distributions, the eccentricities and all exceptional-pair characteristics. `graph_edges.txt` provides the entire input graph. Both programs terminate with a PASS message only if their exact expectations are satisfied. No external dataset, graph library, randomness, solver or unpublished certificate is required.

## Relationship to prior work

Power-domination reconfiguration was introduced in the public preprint by Bjorkman and collaborators of 5 January 2022, subsequently published in *La Matematica*; its full accessible article treats the general TAR and TJ framework and gives token sliding as a distinct motivating direction, but supplies no Robertson-cage optimum census or relocation metric. The Robertson graph's 19-vertex quartic girth-five identity is classical and not claimed here; the explicit labelled cycle-and-chords representation follows Fiorini's thesis. The publicly indexed result *Exact monomer-adsorption jamming law on the Robertson (4,5)-cage* studies stochastic independent-set adsorption, whose probability calculations do not determine deterministic power domination or its shortest relocation paths. The new claim is the specified exact power-domination optimum and reconfiguration metric, not the graph itself, general reconfiguration definitions, or previous invariants of the cage.

## Limitations

The result does not assert analogous values for any other cage or family of graphs. The computational proof depends on the full embedded edge list and executable finite enumeration, not on symbolic closed formulas for an infinite family. The comparisons of accessible primary literature and indexed mathematical results do not guarantee that no unindexed historical equivalent exists.

## References

1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob and C. Reinhart, *Power Domination Reconfiguration*, arXiv:2201.01798, first public 2022-01-05; later *La Matematica* 5 (2026), article 8, https://doi.org/10.1007/s44007-025-00187-5.
2. S. Fiorini, *The Chromatic Index of Simple Graphs*, Ph.D. thesis, The Open University (1975), Chapter 7, pp. 127–128, https://oro.open.ac.uk/63320/1/27777457.pdf (labelled graph description).
3. E. W. Weisstein, *Robertson Graph*, MathWorld, https://mathworld.wolfram.com/RobertsonGraph.html (structural reference).
4. *Exact monomer-adsorption jamming law on the Robertson (4,5)-cage*, public result record 2026/11/8, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-monomer-adsorption-jamming-law-on-the-robertson-4-5-cage--a93dbce61492 (separate graph process).
