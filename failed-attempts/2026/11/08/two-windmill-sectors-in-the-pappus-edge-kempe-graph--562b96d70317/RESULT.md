# Two windmill sectors in the Pappus edge-Kempe graph

## Finding

Let \(P\) be the eighteen-vertex Pappus graph. A *state* is a partition of its edges into three perfect matchings, with **unlabelled** color classes. Two distinct states are adjacent when one is obtained from the other by swapping the two colors along exactly one complete alternating cycle. The entire reconfiguration graph is

\[
\mathcal K(P)\ \cong\ 2\bigl[K_1\vee(K_3\sqcup K_3\sqcup K_3)\bigr],
\]

where \(\vee\) is the graph join and the initial \(2\) denotes disjoint copies. Thus exactly twenty states occur. They form two components of ten states each, each made of three tetrahedra sharing a single vertex and otherwise disjoint. Each component has eighteen edges, radius one, and diameter two; its unique center has nine neighbors, and every other state has three neighbors. There are exactly fifty-four unordered state pairs at distance two (twenty-seven per component), and no legal sequence connects the two components.

The two central states are characterized by having all three two-color complements equal to disjoint unions of three hexagons. Each noncentral state has exactly one such complement; its other two complements are Hamiltonian eighteen-cycles.

## Assumptions and scope

The graph has vertex set \(\mathbb Z/18\mathbb Z\), the cycle edges \(\{i,i+1\}\), and additional edges \(\{i,i+s_i\}\), with subscripts modulo eighteen and the six-periodic sequence of shifts

\[
(s_0,s_1,s_2,s_3,s_4,s_5)=(5,7,-7,7,-7,-5).
\]

Repeated descriptions of an undirected edge count only once. This is the usual Pappus graph in LCF notation \([5,7,-7,7,-7,-5]^3\). Every vertex has degree three, and the graph has twenty-seven edges. Because colors are **unlabelled**, globally permuting colors does not create another state; specifically, this is a reconfiguration graph on one-factorizations, **not** the graph of individually named three-edge-colorings. A Kempe switch means swapping the two participating colors on a single connected component of their bichromatic edge subgraph. Self-transitions are excluded.

## Proof

**Finite structural census.** In a cubic graph, the complement of each perfect matching is a disjoint union of even cycles precisely when that matching belongs to a proper three-edge-coloring. Enumerating the Pappus perfect matchings from the explicit adjacency specification above gives exactly forty-two. For thirty-six, the complement is one cycle of length eighteen; for exactly six, the complement is three disjoint six-cycles. In particular all forty-two are extendible to a three-edge-coloring. We call the latter six *exceptional* matchings and index them \(M_0,\ldots,M_5\) in lexicographic order of their sorted edge-index lists.

Here is a short, fully reproducible certificate of the finite census. List the twenty-seven undirected edges \(e_0,\ldots,e_{26}\) lexicographically, using the graph definition above. The six exceptional perfect matchings are exactly

| Matching | Edge indices |
|---|---|
| \(M_0\) | 0, 5, 9, 12, 16, 19, 21, 24, 26 |
| \(M_1\) | 0, 6, 7, 11, 14, 18, 19, 22, 24 |
| \(M_2\) | 1, 3, 7, 13, 14, 17, 22, 23, 25 |
| \(M_3\) | 1, 4, 5, 10, 12, 17, 20, 23, 26 |
| \(M_4\) | 2, 3, 8, 9, 13, 15, 16, 21, 25 |
| \(M_5\) | 2, 4, 6, 8, 10, 11, 15, 18, 20 |

The two and only two triples of pairwise disjoint exceptional matchings that partition all twenty-seven edges are

\[
\{M_0,M_2,M_5\}\qquad\text{and}\qquad\{M_1,M_3,M_4\}.
\]

Both statements are independently checkable by the complete enumerators included with this note. The Python checker constructs the forty-two matchings via a smallest-remaining-degree recursion, partitions each complement into cycles, and checks the exceptional lists and triples. The C++ checker independently generates all proper edge-colorings by edge-by-edge color assignment, without generating or using the matching list. Neither method assumes the claimed reconfiguration graph.

**Counting states.** Fix a perfect matching \(M\). If its complement consists of \(c\) even cycles, the two remaining colors alternate on each cycle. There are \(2^c\) assignments, and simultaneous exchange of those two colors gives the same unlabelled one-factorization. Thus \(M\) occurs in exactly \(2^{c-1}\) states. Counting incidences of a state with each of its three constituent matchings gives

\[
3\,|V(\mathcal K(P))|=36\cdot1+6\cdot 2^2=60,
\]

hence exactly twenty states.

For each exceptional matching \(M_i\), there are precisely four states containing it. One is the corresponding exceptional triple displayed above; the other three contain exactly one exceptional matching, namely \(M_i\). This last assertion is checked directly by alternating the colors on the three complementary hexagons, with the six displayed matchings as the exhaustive comparison set. Consequently, the two exceptional triples account for two states, and the six exceptional matchings each account for three further, pairwise distinct states. These already exhaust the twenty states. In particular no state contains zero or two exceptional matchings.

**Switch adjacency.** If a two-color complement is one Hamiltonian cycle, swapping its colors acts only as a global relabeling and therefore leaves the unlabelled state unchanged. If the complement is three disjoint hexagons, the three individual swaps act on the four states containing the fixed exceptional matching as translations of \((\mathbb Z/2\mathbb Z)^3/\langle(1,1,1)\rangle\). Any two of those four states differ by a single swap, so they induce a complete graph on four vertices.

There are exactly six such complete four-vertex subgraphs, one for each exceptional matching. Within each of the two exceptional triples, the corresponding three four-vertex subgraphs share only the central triple state. The eighteen noncentral states belong to exactly one of these subgraphs. No remaining Kempe move exists, since every other bichromatic complement is one Hamiltonian cycle. Therefore the graph is exactly the disjoint union of two copies of \(K_1\vee(3K_3)\), as claimed.

**Metric consequences.** Each ten-state component has a universal central vertex and three mutually nonadjacent triangular peripheral blocks. Two noncentral states have distance one precisely when they belong to the same block and distance two otherwise. The number of unordered distance-two pairs per component is \(\binom{9}{2}-3\binom{3}{2}=27\), giving fifty-four in total. The radius, diameter, and degrees follow immediately.

## Verification

All finite assertions can be reproduced with only the included source files. From their directory, run:

```sh
python3 matching_checker.py
g++ -O2 -std=c++17 coloring_checker.cpp -o coloring_checker
./coloring_checker
```

The two methods independently verify the twenty states and the graph decomposition. The matching-based Python computation also verifies the forty-two perfect matchings, the complement-cycle partition \(36+6\), the six explicit exceptional matching edge-index sets, and the two central triples. The C++ method enumerates proper colorings through local color constraints, canonicalizes color names by first occurrence, then reconstructs Kempe adjacency, connected components, triangles, and shortest-path bounds. No stochastic search, solver library, or previously generated data file is needed. Both checks were executed successfully on these exact source files.

## Relationship to prior work

Abreu, Labbate and Sheehan, *Irreducible pseudo 2-factor isomorphic cubic bipartite graphs* (arXiv:1002.1891v1, first posted 2010-02-09), establish the earlier pseudo-2-factor-isomorphic property of Pappus, including the same odd parity of cycle counts for all two-factors. Their result does not determine how individual perfect matchings overlap in one-factorizations, how Kempe switches connect them or the exact switching graph; **pseudo-2-factor isomorphism is not claimed as novel**. Belcastro and Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs* (first public arXiv version dated 2012-09-08), develops equivalence classes under these moves and proves general structural results for cubic graphs, including bipartite and nonplanar cases. Goedgebeur and Östergård, *Switching 3-edge-colorings of cubic graphs* (arXiv 2021), gives exhaustive aggregate class-count tables for all cubic graphs through order thirty and bipartite cubic graphs through order thirty-six, including the order of the Pappus graph. In principle their enumerative machinery could determine this graph's class count, so **the bare number of two components is not asserted as the independent new contribution**. The present claim is the complete *isomorphism type* of the reconfiguration graph, its six overlapping tetrahedral move-cliques, the exceptional-matching mechanism, and its exact metric and extremal configurations. Neither inspected primary text states that Pappus-specific windmill structure or a result that implies it from the reported aggregate tables. The standard Pappus LCF specification is also recorded in the MathWorld graph entry.

## Limitations

The result concerns a particular eighteen-vertex graph and unlabelled one-factorizations only. It does not classify the full named-palette edge-Kempe graph, other cubic graphs, or asymptotic behavior. Its finite census is an exhaustive computer-checkable lemma with a disclosed edge set and standalone enumerators; it does not purport to replace this exact enumeration with a uniform symbolic argument. The literature comparison includes three relevant primary preprints and targeted searches, but cannot exclude unindexed or otherwise inaccessible earlier Pappus-specific calculations. The component count alone is within the scope of earlier large graph censuses and is not separately claimed as novel.

## References

1. M. Abreu, D. Labbate and J. Sheehan, *Irreducible pseudo 2-factor isomorphic cubic bipartite graphs*, arXiv:1002.1891v1, first posted 2010-02-09. https://arxiv.org/abs/1002.1891
2. S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730v1, first posted 2012-09-08. https://arxiv.org/abs/1209.1730
3. J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, arXiv:2105.01363v1, first posted 2021-05-04. https://arxiv.org/abs/2105.01363
4. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html (standard graph identification and LCF notation).
