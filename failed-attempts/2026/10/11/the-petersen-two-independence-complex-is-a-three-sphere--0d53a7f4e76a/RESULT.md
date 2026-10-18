# The Petersen two-independence complex is a three-sphere

## Finding
Let \(P\) be the Petersen graph and let \(\operatorname{Ind}_2(P)\) be the simplicial complex consisting of vertex sets whose induced connected components have at most two vertices. Then
\[
\operatorname{Ind}_2(P)\simeq S^3.
\]
This complex is nonpure: it has exactly five maximal faces of dimension \(3\) and five of dimension \(5\). Thus its actual homotopy dimension is strictly below the largest facet dimension.

## Assumptions and scope
Use ten vertices numbered \(0,1,\ldots,9\). The fifteen undirected edges are the five outer edges \(\{i,(i+1)\bmod5\}\), the five inner edges \(\{5+i,5+((i+2)\bmod5)\}\), and the five spokes \(\{i,5+i\}\), for \(0\le i<5\). Here \(\operatorname{Ind}_2(P)\) means **higher independence** on vertex sets, not the two-matching complex on edge sets, and not the ordinary independence complex. It is equivalently the complex of subsets inducing maximum degree at most one, or the three-vertex-path-free complex.

For encoding, associate to a vertex set \(S\) the integer mask \(\sum_{i\in S}2^i\). The empty face has mask zero and is used only in the augmented intermediate matching. The final simplicial Morse matching is on nonempty faces.

## Proof
A set \(S\) is a face exactly when each vertex \(i\in S\) has at most one neighbor in \(S\). Equivalently, no length-two path of the graph has all three vertices in \(S\). The reproducible verifier `verify.py` constructs all fifteen graph edges, all thirty distinct forbidden triples, and independently enumerates the face set using these two equivalent tests. The tests agree on every one of the \(2^{10}\) possible subsets. There are \(260\) nonempty faces, with dimensional face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(10,45,90,80,30,5).
\]
An exhaustive coface test finds five facets in dimension \(3\) and five in dimension \(5\).

Here is a finite, explicit acyclic discrete-Morse certificate. Start with all faces, including the empty face, available. Process vertices in the order
\[
(0,5,6,8,9,7,1,4,2,3).
\]
At vertex \(v\), visit remaining face masks in increasing order. Whenever a face \(F\) does not contain \(v\) and both \(F\) and \(F\cup\{v\}\) remain available, pair them and remove them from availability. Once every vertex has been processed, exactly one unpaired face remains: mask \(402\), representing the tetrahedron \(\{1,4,7,8\}\). The augmented matching contains the pair of the empty face with the vertex \(\{0\}\) (masks \(0\) and \(1\)). Delete just that pair to obtain a matching of the ordinary nonempty face poset, with exactly two critical faces: the vertex \(\{0\}\) and the tetrahedron \(\{1,4,7,8\}\). Exactly \(129\) disjoint face pairs remain.

To verify acyclicity independently of any heuristic about the toggle order, orient **every** codimension-one Hasse edge between nonempty faces from the lower to the upper face if it is matched, and from the upper to the lower face otherwise. The executable constructs the complete directed graph, counting \(860\) directed Hasse arcs, and performs exhaustive topological sorting. All \(260\) vertices are removed, proving the absence of a directed cycle. Hence the face matching is acyclic. By discrete Morse theory, the complex has a CW model with one cell in dimension \(0\), one in dimension \(3\), and no other cells. The attaching map of the \(3\)-cell is necessarily constant because its target is a point. The model is therefore \(S^3\), as claimed.

The certificate's finite assertions are an exhaustive proof because the complete search space has precisely ten graph vertices and \(2^{10}\) possible vertex subsets; no extrapolation or numerical approximation is involved.

## Verification
Run `python3 verify.py` using only the Python standard library. It reconstructs the entire complex from the specified graph, checks both independent face predicates, verifies the facet counts, creates all matching pairs, and topologically sorts the full reversed-matching Hasse digraph. Its independent binary boundary-matrix computation obtains reduced Betti numbers \((0,0,0,1,0,0)\) in dimensions \(0\) through \(5\). The printed `VERIFY_OK` line includes complete sizes and critical masks. These binary Betti numbers corroborate, but do not replace, the homotopy conclusion supplied by the full acyclic matching.

## Relationship to prior work
Sawant's 2026 investigation of higher independence complexes of trees establishes vertex decomposability for that family and motivates studying the topology of \(r\)-independence complexes beyond trees. The Petersen graph is nonchordal and cubic, so the tree result does not determine its two-independence complex. Deshpande and Singh study higher independence homotopy types for other graph families, and Ghosh and Selvaraja study higher-independence shellability. Barik, Mondal, and Mukherjee's acyclic-matching construction concerns ordinary independence complexes with a simplicial vertex, not the present object. Published computations of Petersen **two-matching** and Petersen **Morse** complexes likewise concern different simplicial complexes. This claim is specifically an exact homotopy computation for the **vertex-based** two-independence complex.

## Limitations
Only the stated Petersen graph and the second higher-independence parameter are classified; the computation does not imply a theorem for arbitrary cubic graphs, generalized Petersen graphs, or other parameters. The homotopy equivalence does not establish shellability or PL-sphere structure; the complex is nonpure and has facets of dimension greater than three. No exhaustive literature index can rule out every unpublished or unindexed equivalent computation. Verification requires executing the supplied finite checker or separately reproducing its finite pair and digraph assertions.

## References
- R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first posted 2026-05-24.
- A. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448.
- A. Ghosh and R. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614.
- S. Barik, A. Mondal and S. Mukherjee, *A Recursive Construction of an Acyclic Matching on the Independence Complex of a Graph with a Simplicial Vertex*, arXiv:2604.12606.
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
