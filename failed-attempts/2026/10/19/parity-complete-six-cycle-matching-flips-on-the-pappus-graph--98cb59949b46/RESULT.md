# Parity-complete six-cycle matching flips on the Pappus graph

## Finding
Let \(P\) be the Levi (point–line incidence) graph of the Pappus configuration and let \(\mathcal F_6(P)\) have one vertex for each perfect matching, with an undirected edge for each transition whose symmetric difference is precisely one simple six-cycle. Define \(H\) from three independent hubs \(h_0,h_1,h_2\) as follows: for each unordered pair of hubs, add a private cycle of six new vertices, attaching successive cycle vertices alternately to the first and second hub. The three six-cycles have disjoint vertex sets and there are no further edges. Then
\[
\mathcal F_6(P)\cong H\sqcup H.
\]
Each copy of \(H\) has 21 vertices, 36 edges and diameter four. Thus \(P\) has exactly 42 perfect matchings, 18 distinct simple six-cycles, 72 distinct legal flips, and two connected components. In each component, precisely three vertices have degree six and eighteen have degree three.

For either ordering of its two 9-vertex bipartition classes, every matching determines a permutation of nine letters. A six-cycle flip composes this permutation with a three-cycle and hence preserves its sign. Both signs occur 21 times, and **matching reachability by six-cycle flips is equivalent to equality of sign**. The exact worst-case number of flips between reachable matchings is four.

## Assumptions and scope
The graph is simple, with vertices 0 through 8 representing points and vertices 9 through 17 representing lines. The nine lines, written as triples of point indices, are

```
(0,1,2), (3,4,5), (6,7,8), (0,4,6), (3,1,6),
(0,5,7), (3,2,7), (1,5,8), (4,2,8)
```

This is the Pappus \(9_3\) incidence configuration, not a geometric embedding of a different graph. Every simple six-cycle of the **abstract graph** is permitted; no face or drawing is distinguished. Perfect matchings are unordered sets of nine edges and each undirected flip is counted once. The statement concerns this graph alone; it is not an assertion about all cubic bipartite graphs or all alternating-cycle lengths.

## Proof
**Parity.** Every matching bijects the two parts of the incidence graph. Replacing the three matching edges around a simple alternating six-cycle with the other three acts on three matched point–line pairs by a cyclic permutation; all remaining images stay fixed. Hence it multiplies the matching permutation by an even three-cycle, so sign is constant on each flip component.

**Exhaustive determination.** The attached `verification/verify_pappus_lcf.py` constructs the Pappus graph independently by the LCF specification \([5,7,-7,7,-7,-5]^3\), that is, the cycle of length 18 with chords from vertex \(i\) to \(i+s_i\bmod18\), with the displayed six shifts repeated three times. Its least-unmatched-vertex recursion exhaustively lists perfect matchings: if \(v\) is the least unused vertex, every completion contains exactly one edge \(vw\) for some unused neighbor \(w\); recursing on the remaining vertex set covers every matching exactly once. It produces 42 matchings.

The program enumerates all simple six-cycles by extending every simple path from every starting vertex up to six vertices, checking a closing edge, and deduplicating the resulting unordered edge sets. This covers every six-cycle and gives 18. For every enumerated matching \(M\) and cycle \(C\), the program adds an edge to \(M\triangle C\) if and only if three edges of \(C\) belong to \(M\). It checks reciprocal adjacencies and obtains 72 undirected transitions.

**Exact component isomorphism.** Exhaustive connected-component search gives two sets of 21 vertices. Within each, there are exactly three vertices of degree six, which are pairwise nonadjacent. Each of the other eighteen vertices has degree three, is adjacent to exactly one high-degree hub, and has two neighbors of degree three. The subgraph on the eighteen low-degree vertices consists of three disjoint six-cycles. Each such cycle has vertex labels alternating between two distinct hubs, and the three cycles exhaust the three distinct unordered hub pairs, one of each. These necessary and sufficient adjacency conditions identify the component with the explicitly defined graph \(H\), not merely with its degree sequence. Exhaustive breadth-first search from all vertices in each component gives maximum distance four, attained in both components.

**Matching signs and completeness.** Bipartition search produces two parts of size nine. The code calculates the permutation sign of every enumerated matching, obtaining exactly 21 of each sign. Since each component has 21 vertices and flips preserve sign, every sign class is exactly one component. Thus the stated sign criterion is both necessary and sufficient.

**Independent reconstruction.** `verification/verify_pappus_incidence.py` starts from the nine line triples above, enumerates all permutations of nine lines, and filters to the 42 point–line bijections satisfying incidence. It joins any pair differing in a cyclic permutation of precisely three assignments, a direct six-cycle flip test. Independently it enumerates the graph's simple six-cycles. An explicitly supplied, edge-by-edge checked isomorphism converts this model to the LCF model; under the induced matching bijection, all 42 adjacency sets coincide exactly. The second program independently repeats the connected-component and diameter checks. Because all vertex pairs are checked and both generation procedures are exhaustive, these are finite proofs of the stated exact numerical and structural claims rather than statistical experiments.

## Verification
Using Python 3 standard library only, run:

```sh
python3 verification/verify_pappus_lcf.py
python3 verification/verify_pappus_incidence.py
```

Both files have been executed successfully from the reviewed package. The first checks the structural six-cycle/hub description and parity classes; the second checks the complete 42-by-42 flip relation under the explicit graph isomorphism, including the diameter. Their source constructions and adjacency tests are different.

## Relationship to prior work
Abreu, Labbate and Sheehan study pseudo-two-factor isomorphism of cubic bipartite Levi graphs and identify the Pappus graph as a distinguished case. They do not classify its reconfiguration graph under six-cycle flips. Ito and collaborators study perfect-matching reconfiguration under **alternating cycles of arbitrary length**, for which every two perfect matchings are reachable; that universal result does not imply reachability using only six-cycles or determine the restricted transition graph. The present classification gives the exact restricted reachability and graph structure. A related geometric example can behave differently when only facial cycles are allowed; this theorem permits all abstract six-cycles and does not transfer from facial-flip classifications.

## Limitations
The classification is specific to the 18-vertex Pappus graph and to length-six flips. The finite proof rests on two transparent exhaustive algorithms whose source is supplied; it makes no claim about general graph families, unrestricted alternating-cycle flips, or independent external certification. Hidden earlier enumerations are a residual originality risk.

## References
1. M. Abreu, D. Labbate and J. Sheehan, *Irreducible pseudo 2-factor isomorphic cubic bipartite graphs*, arXiv:1002.1891v1 (first posted 2010-02-09); https://arxiv.org/abs/1002.1891.
2. T. Ito, N. Kakimura, N. Kamiyama, Y. Kobayashi and Y. Okamoto, *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, arXiv:1907.01700 (2019); https://arxiv.org/pdf/1907.01700.
3. M. Bonamy et al., *The Perfect Matching Reconfiguration Problem*, arXiv:1904.06184 (2019); https://arxiv.org/abs/1904.06184.
