# Two-torsion Moore summands in multipath complexes of bidirected complete bipartite graphs

## Finding
Let \(\overleftrightarrow{K}_{2,n}\) be the digraph obtained by replacing each edge of the ordinary complete bipartite graph \(K_{2,n}\) by its two opposite directed arcs. For a digraph \(D\), let \(X(D)\) be the multipath simplicial complex: its vertices are the arcs of \(D\), and an arc subset is a face exactly when its selected digraph is a disjoint union of directed simple paths and isolated vertices.

Define the mod-two Moore space \(M(\mathbb Z/2,2)=S^2\cup_{2}e^3\), formed by attaching a three-cell to a two-sphere by a map of degree two. Then the two exact, integral homotopy classifications are

\[
\begin{aligned}
|X(\overleftrightarrow{K}_{2,4})|&\simeq M(\mathbb Z/2,2)\vee\bigvee^{7}S^2,\\
|X(\overleftrightarrow{K}_{2,5})|&\simeq M(\mathbb Z/2,2)\vee\bigvee^{31}S^3.
\end{aligned}
\]

In particular, the first complex has \(\widetilde H_2\cong\mathbb Z^7\oplus\mathbb Z/2\) and zero other reduced integral homology. The second has \(\widetilde H_2\cong\mathbb Z/2\), \(\widetilde H_3\cong\mathbb Z^{31}\), and zero other reduced integral homology. Both have nonzero two-torsion and are not wedges of ordinary spheres.

## Assumptions and scope
The underlying ordinary graphs are unfilled, one-dimensional, simple complete bipartite graphs. Fix the short vertex class \(\{0,1\}\), the long vertex class \(\{2,\ldots,n+1\}\), and take both arcs \((u,v)\) and \((v,u)\) for every edge joining the classes. The complex contains **all** subgraphs that are disjoint unions of directed paths, rather than only maximal multipaths. The result concerns exactly \(n=4\) and \(n=5\), with integral (not merely rational or mod-two) homotopy equivalences.

A face is equivalently an arc subset in which every vertex has indegree and outdegree at most one and no directed cycle occurs. Every selected arc meets one of the two short-class vertices. Because each of them contributes at most one incoming and one outgoing selected arc, a face has at most four arcs. Thus there are no simplices above dimension three. This proves that enumeration of subsets of zero through four arcs is exhaustive.

## Proof
Construct all faces as follows. List the \(4n\) directed arcs in lexicographic order. For each subset of at most four arcs, check the indegree and outdegree bounds and directed acyclicity. The standalone verifier constructs the same complex a second way, by starting from the empty face and successively adding admissible arcs, with an independent transitive-closure cycle test. The two entire face sets agree exactly. The nonempty face vectors in dimensions zero through three are, respectively,

\[
\begin{array}{c|rrrr|r}
n&f_0&f_1&f_2&f_3&\text{nonempty faces}\\\hline
4&16&80&144&72&312\\
5&20&130&320&240&710
\end{array}
\]

On the complete nonempty face poset, use the explicit prioritized-toggle matching. Its ordered arc indices are the arrays `ORDERS` in `verify.py`. For each index in sequence, pair every still-unpaired nonempty face that omits the indexed arc with its one-arc enlargement, whenever both remain unpaired. This is a deterministic complete certificate of all pairs; no search outcome is needed to reconstruct it. Every pair is checked to be a genuine codimension-one incidence and to be used only once. Reverse the matching arrows in the entire Hasse diagram and topologically sort the resulting directed graph, checking all its incidences. For \(n=4\), the algorithm verifies 151 pairs and all 880 Hasse incidences; for \(n=5\), 338 pairs and all 2,180 incidences. Both oriented Hasse diagrams are acyclic. The matching is therefore a valid discrete-Morse matching.

The critical-cell vectors by dimension \((0,1,2,3)\) are \((1,0,8,1)\) for \(n=4\) and \((1,0,1,32)\) for \(n=5\). In particular, the Morse two-skeleton is a wedge of two-spheres, with eight or one sphere respectively.

The remaining essential calculation is the **integer**, signed Morse differential between critical three-cells and two-cells. Give every simplex the orientation obtained by increasing lexicographic arc index. The verifier computes cellular incidence signs from this orientation and projects all two-faces to critical two-cells by eliminating every matched two-three pair. Explicitly, if a two-face \(\sigma\) is matched upward to a three-face \(\tau\), the relation \(\partial\tau=0\) solves for \(\sigma\) with unit coefficient \(\pm1\) and recursively substitutes its other two-faces. Two-faces paired downward with one-faces project to zero; critical two-faces project to themselves. Acyclicity makes the recursion terminate. The boundary of each critical three-cell is then projected by these signed substitutions. The resulting integer matrices have sizes \(8\times1\) and \(1\times32\), and in each case the greatest common divisor of every entry is exactly two. In the first case, the single column has entries in \(\{0,\pm2\}\) with at least one nonzero entry; in the second, the single row contains entries in \(\{0,\pm2,\pm4\}\) with greatest common divisor two. In both cases the Smith normal form has one nonzero invariant factor, equal to two.

Since the Morse one-skeleton has one vertex and no edges, its two-skeleton is simply connected. By the Hurewicz theorem, \(\pi_2\) of that two-skeleton is the free abelian group generated by its two-cells, so the integer attaching-degree matrices determine all the three-cell attaching maps. Unimodular changes of bases of the two-cells or three-cells are realized by homotopy self-equivalences of the corresponding wedges of two-spheres. Smith reduction therefore changes the attaching map into a degree-two map on one two-sphere and zero maps on all remaining summands. Its cofiber is precisely the displayed Moore space wedge with the remaining spheres. This establishes the integral homotopy equivalences, rather than merely the integral homology groups.

## Verification
Run `python3 verify.py` with Python 3.10 or later; it uses only the standard library. The embedded file `verify_output.txt` records the actual replay. The verifier checks all faces by two distinct constructions; every matching incidence and global Hasse acyclicity; the critical cell census; exact integral signed Morse substitutions and their Smith content; and independent full simplicial boundary-rank calculations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\).

The independent field computations give the reduced Betti ranks \((\beta_2,\beta_3)=(8,1)\) in characteristic two and \((7,0)\) in characteristics three and five for \(n=4\). For \(n=5\) they are \((1,32)\) in characteristic two and \((0,31)\) in characteristics three and five. These tests corroborate, but do not replace, the exact integral attaching-degree computation. The final output marker is `ALL_VERIFY_OK`.

## Relationship to prior work
Caputi, Collari and Smith's 2026 study of *multipath complexes of bidirectional polygonal digraphs* (arXiv:2601.05670, first posted 2026-01-09) motivates the investigation of directed-cycle-bearing, symmetric graph families. Its main objects are bidirected paths and cycles, including their homology and connectivity. It does not determine the integral homotopy types of the present bidirected complete bipartite graphs. This distinction matters: a bidirected \(K_{2,4}\) or \(K_{2,5}\) has many overlapping directed four-cycles and is not a bidirected polygon.

Caputi, Collari, Di Trani and Smith's earlier *On the homotopy type of multipath complexes* (arXiv:2208.04656, first posted 2022-08-09) computes Euler characteristics for complete bipartite **one-way-oriented** digraphs; its Section 3.2 explicitly defines all arcs from one vertex class to the other. That complex is a chessboard/matching complex and differs from the current bidirected construction, where directed cycles occur. The general observation there that some multipath complexes have torsion does not imply these exact spaces or attaching degrees.

Published results and indexed mathematical records for closely related bidirected double stars, ordinary matching complexes, and Morse matching complexes concern different face conditions or different graphs and do not imply this classification. The new contribution is the two **particular integral Moore-space splittings**, not a claim that torsion in all multipath complexes was unknown.

## Limitations
This is an exhaustive finite classification at the two specified widths; it is not an all-\(n\) theorem. The discrete-Morse certificate and integral reductions are fully reproducible, but they have not received an independent mathematical audit. The result neither asserts a complete torsion census across symmetric digraphs nor determines equivariant homotopy types. Searches cannot exclude equivalent work that is not indexed or was not accessible.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, 2026-01-09, https://arxiv.org/abs/2601.05670 .
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, 2022-08-09, https://arxiv.org/abs/2208.04656 .
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145, doi:10.1006/aima.1997.1650.
