# The cuboctahedral second-independence complex is a wedge of \(32\) three-spheres

## Finding
Let \(Q_3\) be the graph of the three-dimensional cube and let \(C=L(Q_3)\) be its line graph, which is the cuboctahedral graph. Let \(X=\operatorname{Ind}_2(C)\) have as faces the subsets of the twelve vertices of \(C\) whose induced connected components contain at most two vertices. Then the **integral homotopy type**, rather than just the homology, is
\[
X\simeq\bigvee^{32}S^3.
\]
The complex has simplicial dimension four but has a CW model with one zero-cell and thirty-two three-cells only. Its reduced integral homology is \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{32}\), and all other reduced integral homology groups vanish.

## Assumptions and scope
The graph \(Q_3\) has vertices \(\{0,1,\ldots,7\}\) interpreted as three-bit words. Its edge list is ordered lexicographically among pairs \((a,b)\) with \(a<b\) and with exactly one differing binary coordinate. The twelve resulting edges, in that order, label the vertices \(0,\ldots,11\) of \(C\). Two vertices of \(C\) are adjacent precisely when the corresponding cube edges share an endpoint. Thus \(C\) has twelve vertices, twenty-four edges, and degree four everywhere.

A selected set is a face of \(X\) if and only if its induced graph on \(C\) has maximum degree at most one. Indeed a connected graph on at least three vertices has a vertex of degree at least two, whereas graphs with maximum degree at most one are disjoint unions of vertices and edges. Equivalently, \(X\) is the complex of subsets containing no connected three-vertex subgraph of \(C\); this is the \(P_3\)-devoid complex, with non-induced copies of the three-vertex path forbidden. The empty face is present but is not treated as a vertex of the nonempty face poset.

## Proof
Encode each vertex subset by a twelve-bit integer \(m\). Form the nonempty face set \(F\) by testing every integer in the range \(1\le m<4096\), accepting precisely when each selected vertex has at most one selected neighbor. Direct exhaustive enumeration gives \(455\) nonempty faces. By dimensions zero through four the face counts are
\[
(f_0,f_1,f_2,f_3,f_4)=(12,66,164,177,36).
\]
These are exact finite counts, independently reproduced from forbidden connected triples below.

Construct a partial matching of the nonempty face poset as follows. For successive vertex labels in the fixed order
`(9, 8, 10, 2, 5, 0, 4, 7, 6, 11, 3, 1)`, take each still unmatched face \(\sigma\) not containing the current vertex \(v\), in increasing integer-mask order; whenever \(\sigma\cup\{v\}\) also remains unmatched, match the two faces and remove them from the remaining set. The two faces differ by exactly one vertex, so each is a covering relation of the simplicial face poset. No face is used twice.

The resulting matching has **211 pairs**. Its unmatched faces consist of exactly **one vertex and thirty-two three-dimensional simplices**. Crucially, the matching is acyclic: list *every* covering relation among the \(455\) nonempty faces, orient a matched cover from smaller face to larger face, and orient all other covers from larger face to smaller face. There are exactly \(1512\) cover relations. Exhaustive topological elimination of the resulting directed graph removes all \(455\) vertices, so no directed cycle exists. The accompanying `certificate.json` records all matched pairs, all critical faces and a directed topological ordering; `verify.py` reconstructs the entire face poset and checks this certificate from its actual file bytes.

Forman's discrete-Morse CW theorem consequently gives a CW complex homotopy equivalent to \(X\) with one zero-cell and thirty-two three-cells, and no one-, two-, or higher-dimensional cells. Each three-cell has constant attaching map into the zero-cell; the CW complex is therefore a wedge of thirty-two three-spheres. The integral conclusion follows without invoking any assumption about torsion from numerical field homology.

## Verification
Using Python 3 with its standard library, from the same directory run `python3 verify.py` and `python3 independent_homology.py`. The first program reconstructs \(C\) from binary cube edges, checks the face counts, enumerates all \(1512\) covering relations, checks the full matching/certificate, and verifies acyclicity by full directed topological elimination. The second uses a different forbidden-triple enumeration, finding exactly \(56\) connected triples. Independently reducing all simplicial boundary matrices over \(\mathbf F_2\), it obtains boundary ranks \((11,55,109,36)\) and reduced Betti vector \((0,0,0,32,0)\) in dimensions zero through four. Recorded outputs are `verify_output.txt` and `independent_output.txt`; the full integral homotopy proof depends on the verified discrete-Morse certificate, **not** merely on those Betti numbers.

## Relationship to prior work
Taylan's 2015 public preprint introduced matching trees for devoid complexes, including the forbidden-path formulation, and classified such complexes for paths, cycles and forests. Its Theorems 3.10, 3.14 and 5.2 do not give this cuboctahedral calculation. Deshpande and Singh subsequently classified higher-independence homotopy types for complete multipartite, fully whiskered, path, cycle and perfect rooted-tree families, but not for the cuboctahedral graph. This graph has triangles, squares and no degree-one vertices, so none of those family hypotheses applies.

Other indexed computations on the same polyhedral graph concern its ordinary matching complex, its cut complex, or intrinsic metric complexes. These are different face constructions. In particular, the ordinary matching complex has vertices indexed by the twenty-four graph *edges*, whereas this higher-independence complex has vertices indexed by its twelve graph *vertices*. The three-cut complex of \(C\) is also not the Alexander dual formulation relevant here: the latter involves the three-cut complex of the **complement** of \(C\), not of \(C\) itself. No inspected theorem supplies the claimed integral homotopy equivalence. Equivalent unindexed work remains possible.

## Limitations
This is a self-contained finite classification for the particular twelve-vertex graph \(L(Q_3)\), not a theorem for all line graphs, cube dimensions or Archimedean polyhedra. It asserts homotopy equivalence, not homeomorphism or equivariant homotopy type. The result has reproducible finite proof checks, but independent mathematical validation has not been performed. An unsuccessful literature or index search does not itself prove priority.

## References
1. D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754 (first public version 2015-01-27), https://arxiv.org/abs/1501.06754.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first public version 2020-01-15), https://arxiv.org/abs/2001.05448.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
