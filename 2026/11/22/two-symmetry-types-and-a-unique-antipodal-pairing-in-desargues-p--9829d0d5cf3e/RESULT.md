# Two symmetry types and a unique antipodal pairing in Desargues power-domination relocation

## Finding

Let \(G\) be the twenty-vertex Desargues graph, represented as the bipartite double cover of the Petersen graph. Its minimum power-domination number is \(3\). Precisely \(240\) three-vertex sets power-dominate \(G\). These sets form two orbits of size \(120\) under \(S_5\times C_2\), distinguished exactly by the sorted three-pair distance signatures \((2,3,5)\) and \((3,3,4)\).

Form the **optimum token-slide graph** \(\mathcal T\), whose vertices are those \(240\) sets and whose edges exchange one selected vertex with an adjacent unselected vertex of \(G\), requiring the new set to remain power dominating. Then \(\mathcal T\) is connected, four-regular, and has \(480\) edges, radius \(7\) and diameter \(8\). Every signature-\((2,3,5)\) configuration has eccentricity \(7\); every signature-\((3,3,4)\) configuration has eccentricity \(8\) and **exactly one** configuration at distance \(8\). The sixty distance-eight unordered pairs form a perfect matching on the latter symmetry orbit. Both endpoints of each pair are disjoint vertex sets.

The exact unordered-pair distance distribution in \(\mathcal T\), in increasing order of distance \(1,\ldots,8\), is
\[
(480,1440,3540,6780,9000,6000,1380,60).
\]
For comparison, unrestricted one-vertex replacement among the same optima gives a connected graph with \(1800\) edges and diameter \(4\); the exchange degrees of the two symmetry types are \(17\) and \(13\), respectively.

## Assumptions and scope

For the labelled model let \(Q=\binom{\{0,1,2,3,4\}}2\) be the ten two-element subsets and set
\[
V(G)=\{(p,e):p\in Q,\ e\in\{0,1\}\}.
\]
Distinct vertices \((p,e)\) and \((q,f)\) are adjacent if and only if \(e\ne f\) and \(p\cap q=\varnothing\). This is the bipartite double cover of the Petersen graph, also isomorphic to \(GP(10,3)\). For a nonempty sensor set \(S\), first mark its closed neighborhood; thereafter, simultaneously mark the sole unmarked neighbor of any marked vertex with exactly one unmarked neighbor. Call \(S\) power dominating when the process marks every vertex.

A minimum configuration has minimum cardinality among all successful sensor sets. The graph \(\mathcal T\) has one vertex per minimum configuration and an undirected edge between \(S,T\) precisely when \(|S\setminus T|=|T\setminus S|=1\) and the replaced and inserted vertices are adjacent in \(G\). The comparison exchange graph omits only the last adjacency condition. Distances and eccentricities are within these reconfiguration graphs, not the original graph. All configurations and transitions are *unlabelled token* subsets; graph vertices themselves remain labelled.

## Proof

**Minimum size and the distance-signature classification.** There are \(20\) singletons, \(190\) two-vertex sets and \(1140\) three-vertex sets. Enumerate each with the finite propagation rule above, with a marking set that strictly grows during each successful propagation step. None of the first \(210\) candidates succeeds. Exactly \(240\) triples succeed, and their sorted pairwise graph distances have counts
\[
\begin{array}{c|cc}
\text{signature}&(2,3,5)&(3,3,4)\\ \hline
\text{successful triples}&120&120
\end{array}.
\]
Conversely, every three-vertex set of either signature succeeds, and no other three-vertex set does. The two given verification programs carry out all these closed finite enumerations with independent vertex encodings and propagation routines. The search bounds are explicitly \(\binom{20}{1}+\binom{20}{2}+\binom{20}{3}=1350\), so no unenumerated smaller candidate or triple is assumed away.

**Symmetry and metric.** Every permutation of the five labels, together with optionally interchanging the two layers, is an automorphism. Applying all \(120\cdot2=240\) such transformations to a representative of each signature produces its full \(120\)-element class. Thus each signature is a single automorphism orbit. Building all legal exchanges by the stated one-vertex predicate gives the degrees \(17\) and \(13\) and, for slides, degree \(4\) on both orbits. Breadth-first search from a representative of each orbit gives the following complete shell counts (the entry for distance zero is one in each case):

| Slide distance | \((2,3,5)\) type | \((3,3,4)\) type |
|---|---:|---:|
| 1 | 4 | 4 |
| 2 | 12 | 12 |
| 3 | 30 | 29 |
| 4 | 57 | 56 |
| 5 | 75 | 75 |
| 6 | 50 | 50 |
| 7 | 11 | 12 |
| 8 | 0 | 1 |

Each representative reaches all \(240\) configurations. By orbit transitivity, every configuration has the corresponding shell counts. Summing the counts over \(120\) configurations of each type and dividing by two counts each unordered pair once, giving the asserted distance spectrum, radius and diameter. The slide edge total is \(240\cdot4/2=480\). Repeating the same finite metric computation for unrestricted replacements gives the stated comparison graph.

**Explicit antipodal involution.** A type-\((3,3,4)\) triple consists of two same-layer vertices \((a,e),(b,e)\), with \(a,b\) disjoint two-element subsets, and a vertex \((c,1-e)\), where \(c\) meets both \(a\) and \(b\). Put \(U=a\cup b\) (four labels) and \(d=U\setminus c\) (two labels). Among the three perfect matchings of the complete graph on \(U\), one is \(\{a,b\}\), another contains \(c,d\), and the third is \(\{r,s\}\). The unique antipode is exactly
\[
\Phi(\{(a,e),(b,e),(c,1-e)\})
 =\{(r,e),(s,e),(d,1-e)\}.
\]
For the representative \(\{(\{0,1\},0),(\{0,2\},1),(\{1,3\},1)\}\), the formula gives \(\{(\{0,3\},1),(\{1,2\},1),(\{2,3\},0)\}\). Its unique distance-eight status is checked directly by breadth-first search, and all other cases follow from the transitive automorphism action. The prescribed partner rule is also exhaustively checked on all \(120\) type-\((3,3,4)\) triples. It is an involution with no fixed point, giving exactly \(60\) disjoint antipodal pairs.

## Verification

Run `python3 verify_incidence.py` and `python3 verify_petersen_cover.py` from the directory containing this result. Both programs use only the Python standard library. The first constructs the two-subset double cover, checks all labelled candidates, computes the \(S_5\times C_2\) orbit partition, verifies every slide and jump, runs breadth-first searches and checks the explicit antipodal involution. The second independently constructs \(GP(10,3)\) using index arithmetic, performs power-domination propagation with integer bitsets, and computes all reconfiguration distances using Floyd–Warshall. It also verifies the two symmetry-type eccentricities and absence of non-disjoint distance-eight partners. Both programs end with `PASS` if and only if their exact assertions hold.

## Relationship to prior work

Bjorkman, Bozeman, Ferrero, Flagg, Grood, Hogben, Jacob and Reinhart's *Power Domination Reconfiguration* (first public preprint, 5 January 2022) introduces and studies the power-domination transformation framework. Its complete openly accessible journal text establishes general token-jump properties and identifies power-domination token sliding as a research direction; it does not state the Desargues-specific minimum-configuration classification, two eccentricity strata or antipodal involution. Earlier generalized-Petersen power-domination research by Zhao, Shan and Kang gives numerical upper bounds and results for specified parameter families, not this optimum-relocation metric on \(GP(10,3)\). The exact mobility result is also not an implication of results on zero forcing, independent domination or other set predicates on the Desargues graph: the feasibility rules and optimum sets differ.

## Limitations

This is an exact finite theorem for the ordinary twenty-vertex Desargues graph and its ordinary power-domination propagation rule; it asserts nothing for all generalized Petersen graphs or for fault-tolerant sensor placement. The numerical certificate is finite and exhaustive, not a symbolic all-order classification. The comparison to published results supports priority only to the extent of the actually accessed sources and searches; an unindexed equivalent may exist. No independent external mathematical audit has been performed.

## References

- B. Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798, first posted 2022-01-05, https://arxiv.org/abs/2201.01798 ; accessible journal full text https://doi.org/10.1007/s44007-025-00187-5 .
- M. Zhao, E. Shan and L. Kang, *Power domination in the generalized Petersen graphs*, Discussiones Mathematicae Graph Theory 40 (2020), 695–712, https://doi.org/10.7151/DMGT.2137 .
- G. Xu and L. Kang, *On the power domination number of the generalized Petersen graphs*, Journal of Combinatorial Optimization 22 (2011), 282–291, https://doi.org/10.1007/s10878-010-9293-y (abstract and secondary coverage inspected; full text not obtained).
- J. M. Křišťan and J. Svoboda, *Shortest Dominating Set Reconfiguration under Token Sliding*, arXiv:2307.10847, 2023, https://arxiv.org/abs/2307.10847 (different feasibility predicate).
