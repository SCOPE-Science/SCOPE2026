# Adjacent sphere dimensions in two extremal triangle-free four-chromatic dissociation complexes

## Finding
Let \(G\) be the eleven-vertex Grötzsch graph, realized as the Mycielskian of the five-cycle, and let \(H\) be the twelve-vertex Chvátal graph with edges specified in the accompanying verifier. For a finite graph \(X\), define \(\operatorname{Ind}_2(X)\) to contain those vertex subsets whose induced connected components each have at most two vertices. Then the **complete integral homotopy types** are
\[
\operatorname{Ind}_2(G)\simeq S^2,\qquad
\operatorname{Ind}_2(H)\simeq S^3.
\]
In particular, the first higher-independence complexes of these two natural triangle-free, four-chromatic graphs have different sphere dimensions, despite sharing those two graph properties. Each complex has reduced integral homology \(\mathbb Z\) in its indicated sphere dimension and zero in all other dimensions.

## Assumptions and scope
Graphs are finite, simple and undirected. The Grötzsch graph uses vertices \(0,\ldots,4\) on a five-cycle, shadows \(5,\ldots,9\), and hub \(10\): an original vertex is adjacent to its two cycle neighbors and the shadows of those neighbors, while each shadow is adjacent to the hub. The Chvátal graph uses vertices \(0,\ldots,11\), with the complete 24-edge list in `verify.py`; it is independently checked isomorphic to the standard Chvátal graph. Both are triangle-free and have chromatic number four, verified exactly for these labeled graphs.

A nonempty vertex subset is a face precisely when every included vertex has at most one included neighbor. Equivalently, it avoids every vertex triple spanning at least two graph edges. In the triangle-free setting, this is also the \(P_3\)-devoid (dissociation) complex. The empty face is included mathematically but excluded from the finite face-poset representation; all homotopy statements concern the ordinary geometric realization.

## Proof
A complete acyclic partial matching of the nonempty face poset suffices. Fix an ordered list of graph vertices. Starting with all faces unmatched, for each pivot \(v\) pair every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) if that latter face is also still unmatched; remove both. These pairs are Hasse covering relations. The appended verifier reconstructs all faces by *two independent membership criteria*, performs the entire matching, reverses precisely the matched Hasse incidences, and topologically sorts the directed Hasse diagram. A complete sort establishes that no directed cycle exists, hence that the matching is acyclic.

For the Grötzsch graph, take pivot sequence \((0,5,4,3,1,7,10,9,8,6,2)\). Exactly 312 nonempty faces occur, with face vector \((11,55,110,95,36,5)\); there are 155 matched pairs and exactly two critical faces: singleton bitmask \(1\), and three-vertex bitmask \(88\). All 1,030 Hasse coverings are checked. Thus the Morse CW complex consists of one zero-cell and one two-cell.

For the Chvátal graph, take pivot sequence \((11,10,9,8,7,6,5,4,3,2,1,0)\). Exactly 424 nonempty faces occur, with face vector \((12,66,148,142,52,4)\); there are 211 matched pairs and exactly two critical faces: singleton bitmask \(2048\), and four-vertex bitmask \(232\). All 1,428 Hasse coverings are checked. Thus its Morse CW complex consists of one zero-cell and one three-cell.

By Forman's discrete Morse theorem, the original complexes are homotopy equivalent to these respective CW complexes. Attaching one cell of dimension at least two to a point produces the corresponding sphere. In particular, no additional integer boundary or attaching-map computation is needed: the sphere conclusions follow integrally, not merely over a field.

## Verification
Run `python3 verify.py` using Python's standard library only, alongside the included `verification_output.txt` as a reproducible reference output. The script builds the edge lists, checks graph properties by exact coloring backtracking, constructs the full face sets in two independent ways, checks the exact matching pairs, and verifies the absence of cycles in **every covering incidence** by complete topological sorting. It separately computes mod-two simplicial homology as a sanity check, obtaining exactly one generator in degree two for the Grötzsch complex and exactly one in degree three for the Chvátal complex. The integral homotopy conclusion comes from the complete acyclic matching, not from mod-two homology.

## Relationship to prior work
Taylan's original 2015 paper establishes the general \(P_k\)-devoid-complex framework and explicitly calculates paths, cycles and forests. The two graphs here are neither forests nor paths nor cycles, and its inspected classification statements do not yield either exact homotopy type. Deshpande and Singh later study higher independence complexes for complete multipartite, fully whiskered, path, cycle and perfect-tree families, none of which contains these two specific graphs. Previously available results on the **ordinary** independence or neighborhood complexes of the Chvátal graph, and on the matching or graph-Čech complexes of the Grötzsch graph, involve different simplex definitions. None of the inspected scientific statements implies these two \(\operatorname{Ind}_2\) sphere classifications. An equivalent result in unindexed or inaccessible literature cannot be excluded.

## Limitations
This is a complete result only for the two explicitly defined graphs and the parameter two. It does not prove an analogous dimension formula for all four-chromatic triangle-free graphs, nor a relationship between chromatic number and sphere dimension. The findings have not undergone independent mathematical review. Exact source-priority claims beyond the inspected literature are not made.

## References
- Demet Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, first public version 27 January 2015, arXiv:1501.06754v1, https://arxiv.org/html/1501.06754v1.
- Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of graphs and their homotopy types*, first public version 15 January 2020, arXiv:2001.05448, https://arxiv.org/html/2001.05448v2.
- Sergey Kitaev and Artem Pyatkin, *On semi-transitive orientability of triangle-free graphs*, arXiv:2003.06204 (2020), https://arxiv.org/abs/2003.06204; contextual identification of the two extremal graphs, not a source for the homotopy claim.
