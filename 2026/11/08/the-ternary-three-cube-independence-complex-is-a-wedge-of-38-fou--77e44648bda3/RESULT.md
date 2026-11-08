# The ternary three-cube independence complex is a wedge of 38 four-spheres

## Finding
Let \(G\) be the Hamming graph on \(\{0,1,2\}^3\), with two different triples adjacent precisely when they differ in **one** coordinate; equivalently, \(G=K_3\square K_3\square K_3\), the three-dimensional three-by-three-by-three rook graph. Write \(\operatorname{Ind}(G)\) for the simplicial complex of independent vertex subsets. Then
\[
\operatorname{Ind}(K_3\square K_3\square K_3)\simeq\bigvee^{38}S^4.
\]
This is an integral homotopy equivalence. In particular, its only nonzero reduced integral homology is \(\widetilde H_4\cong\mathbb Z^{38}\).

## Assumptions and scope
The graph is finite and simple, has precisely 27 vertices and 81 edges, and uses the **Cartesian**, not categorical, product convention. For distinct vertices \(u=(a,b,c)\) and \(v=(a',b',c')\), adjacency means exactly one of the three respective equalities fails. The simplices are the nonattacking three-dimensional rook placements on a cube of side length three: no two positions lie in the same axis-parallel line. All assertions refer to this fixed graph; no claim is made for other Hamming parameters or for the usual hypergraph-matching complex on three coordinate classes.

## Proof
Encode \((a,b,c)\) as bit \(9a+3b+c\) for \(a,b,c\in\{0,1,2\}\). A mask represents an independent face exactly when no two of its set bits have Hamming distance one. The complete independent-face set \(\mathcal F\), including the empty mask, has cardinality 11,776. Its counts at cardinalities zero through nine are
\[
(1,27,270,1278,3078,3834,2412,756,108,12).
\]
These are checked by two distinct exhaustive constructions. The first recursively chooses or excludes each eligible bit while removing its neighbors when it is chosen. The second expresses each face as a triple of independent placements in the three coordinate layers. Each layer is a partial permutation matrix on a three-by-three board, admitting exactly \(1+9+18+6=34\) placements; the three layer masks must be pairwise disjoint in their two-dimensional coordinates. The two generated sets agree exactly.

We now describe a finite acyclic discrete-Morse matching on the face poset. Consider the vertex indices in the fixed order

`[3,14,10,17,5,0,7,21,19,18,23,25,4,2,22,6,11,20,9,26,15,16,8,1,13,24,12]`.

Start with all 11,776 faces, including the empty face. For each pivot vertex in this order, inspect the remaining masks in increasing integer order. Whenever a remaining mask \(s\) does not contain the pivot and both \(s\) and the mask obtained by adjoining the pivot remain, pair these two faces and remove both from further consideration. This is an explicit, deterministic enumeration of 5,869 disjoint incident pairs. Precisely 38 faces remain, all with five vertices (dimension four). The empty mask occurs in one pair; discard that single pair to obtain an ordinary matching on the nonempty-face poset with 5,868 pairs, one unmatched vertex, and 38 unmatched four-simplices.

The acyclicity check orients every covering relation from the higher-dimensional face to the lower-dimensional face, except that the direction is reversed for matched covering relations. There are exactly 56,592 such relations between nonempty faces; the resulting directed graph has 11,775 vertices. The standalone verifier explicitly builds every directed covering relation and exhausts all 11,775 vertices by a topological sort, proving that there is **no directed cycle**. Thus this is an acyclic matching, not merely a count of unmatched simplices.

By the discrete-Morse CW-reduction theorem, the realization of the simplicial complex has the homotopy type of a CW complex with one zero-cell, 38 four-cells, and no other cells. Every attaching map of a four-cell has target the zero-skeleton point and is therefore nullhomotopic. This CW complex is exactly a wedge of 38 copies of \(S^4\), proving the finding. All finite computations in this proof are regenerated from the specified graph and pivot order by the standalone verifier; none depends on a precomputed matching file.

## Verification
Run `python3 verification/verify.py` with ordinary Python 3 (standard library only). The script generates all faces twice, checks the exact face-set equality, checks the matching pair counts and critical dimensions, builds and topologically sorts the entire oriented Hasse graph, and independently reduces the unreduced simplicial boundary matrices modulo two. It reports boundary ranks in dimensions zero through eight as
\[
(0,26,244,1034,2044,1752,660,96,12)
\]
and ordinary mod-two Betti ranks \((1,0,0,0,38,0,0,0,0)\), consistent with the integral homotopy theorem. Reproduction output is in `verification/observed_output.txt`. The combinatorial directed-graph check, not the mod-two calculation, verifies the stronger homotopy conclusion.

## Relationship to prior work
The higher-dimensional rook graph is explicitly studied by Burchett (2016), but the questions there concern independence numbers and pawn-blocker independence-separation parameters, not the homotopy type of its independence complex. Classical chessboard complexes are independence complexes of **two-dimensional** rook graphs. The multiple chessboard complexes studied by Jojić, Vrećica, and Živaljević (2014 preprint) use row/column capacity rules on two-dimensional boards; their connectivity and shellability theorems do not directly identify the present three-dimensional line-avoidance complex. Likewise, Antolín Camarena and Carnero Bravo (2023 preprint) treat **categorical** products, in which edges require adjacency in every coordinate, rather than the Cartesian product used here. The multidimensional complete-partite-hypergraph matching complex forbids pairs sharing any coordinate, while the present complex permits pairs differing in exactly two coordinates. Related known results for the neighborhood and Vietoris–Rips complexes of the same 27-point graph concern different simplicial complexes.

## Limitations
This is a finite, reproducible integral homotopy calculation, not a classification of the family of Hamming graphs. The chosen Morse matching need not respect graph symmetries, and no equivariant decomposition is asserted. A systematic publication-priority search found no covering result, but unindexed equivalent work or results buried in adjacent graph-product literature remain possible. Independent mathematical verification has not been performed.

## References
1. P. A. Burchett, *The Independence-Separation Problem on the 3-D Rook's Graph*, Open Journal of Discrete Mathematics **6** (2016), 167–173, doi:10.4236/ojdm.2016.63014; publicly published 2016-07-14. Full text: https://www.scirp.org/html/3-1200287_68335.htm.
2. D. Jojić, S. T. Vrećica, R. T. Živaljević, *Multiple chessboard complexes and the colored Tverberg problem*, arXiv:1412.0386 (first public 2014-12-01), https://arxiv.org/abs/1412.0386.
3. O. Antolín Camarena, A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first public 2023-07-23), https://arxiv.org/abs/2307.12401.
4. D. B. Karaguezian, V. Reiner, M. L. Wachs, *Matching Complexes, Bounded Degree Graph Complexes, and Weight Spaces of GL-Complexes*, Journal of Algebra **239** (2001), 77–92, doi:10.1006/jabr.2000.8654 (related background; the entire paper was not inspected).
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145. The finite acyclic matching used above satisfies the standard hypotheses of discrete-Morse reduction.
