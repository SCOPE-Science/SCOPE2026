# Thirteen nine-spheres and a cyclic homology character for the Desargues dominance complex

## Finding
Let \(G=\operatorname{GP}(10,3)\) be the twenty-vertex Desargues graph, with vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/10\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). Its dominance complex is the simplicial complex
\[
\mathcal D(G)=\{\sigma\subseteq V(G):V(G)\setminus\sigma\text{ dominates }G\}.
\]
There is an *integral homotopy equivalence*
\[
\boxed{\mathcal D(G)\simeq\bigvee^{13}S^9.}
\]
In particular, the reduced integral homology is \(\mathbb Z^{13}\) in degree nine and zero in all other degrees. The complex is eight-connected, and Matsushita's bound is sharp:
\[
\operatorname{conn}_{\mathbb F_2}(\mathcal D(G))+2=8+2=10=\tau(G).
\]
The maximal simplices are not equidimensional: there are respectively \(14,205,180,130\) facets of dimensions \(9,11,12,13\).

The graph rotation \(r:u_i\mapsto u_{i+1},\ v_i\mapsto v_{i+1}\) induces an order-ten action on \(H_9(\mathcal D(G);\mathbb Q)\). For \(t=0,1,\ldots,9\), the character values are, in that order,
\[
\boxed{(13,-1,3,-1,3,-11,3,-1,3,-1).}
\]
Writing \(\varepsilon\) for the one-dimensional sign representation of \(C_{10}\) and \(\mathbb Q(\zeta_{10})\) for its four-dimensional primitive cyclotomic representation, one has
\[
H_9(\mathcal D(G);\mathbb Q)\cong
\mathbf 1\oplus\varepsilon^{\oplus4}\oplus\mathbb Q(\zeta_{10})^{\oplus2}
\]
as rational \(C_{10}\)-modules. In particular, the rotation-fixed subspace has dimension one.

## Assumptions and scope
The graph is finite, simple, and *undirected*. Subscripts on its vertices are taken modulo ten. The term dominating refers to **closed** neighborhoods: a set \(A\subseteq V(G)\) dominates when \(A\cap N_G[x]\ne\varnothing\) for every vertex \(x\). Thus a face \(\sigma\) of \(\mathcal D(G)\) is characterized exactly by
\[
\forall x\in V(G),\qquad N_G[x]\nsubseteq\sigma.
\]
Each closed neighborhood has four vertices. Vertex labels \(0,\ldots,9\) correspond to \(u_0,\ldots,u_9\), and \(10,\ldots,19\) to \(v_0,\ldots,v_9\). A subset is encoded by the sum of its corresponding powers of two. All topological claims are ordinary, nonequivariant homotopy claims except for the explicitly rational \(C_{10}\)-representation above.

## Proof
**Face identification.** The graph has thirty edges and degree three at every vertex. The complement of \(\sigma\) dominates if and only if no closed neighborhood is contained in \(\sigma\). The supplied executable enumerates every one of the \(2^{20}=1,048,576\) subsets by this criterion, then independently verifies each result with a second enumeration method. There are \(434,221\) faces including the empty face. The vector of numbers of \(d\)-simplices for \(d=0,\ldots,13\) is
\[
(20,190,1140,4825,15184,36390,66800,93120,96400,71356,35680,11105,1880,130).
\]

**A complete acyclic matching.** Order the vertices as \(0,1,\ldots,19\). Starting with all faces available, at stage \(j\) pair every still-available face \(\sigma\) missing vertex \(j\) with \(\sigma\cup\{j\}\), provided both are available, and remove both from further stages. This is a matching in the augmented face-poset Hasse diagram because the two faces differ by one vertex and no face is reused. It initially pairs the empty face with the first vertex; discard *that one pair* so that the ordinary nonempty-face poset has a critical vertex. The resulting matching consists of \(217,103\) pairs, one critical vertex, and exactly thirteen critical nine-dimensional faces. There are no other critical faces.

For an independent acyclicity certificate, orient every unmatched Hasse cover from larger to smaller face and every matched cover from smaller to larger face. A complete topological sort visits all \(434,221\) nodes of the augmented Hasse graph, using all \(3,663,100\) cover incidences; in particular the directed graph has no cycle. Repeating this calculation with the reverse vertex order gives a *different* matching with exactly the same critical-cell dimensions and again visits every node of the oriented Hasse graph. These are exhaustive finite graph checks, not a sample or probabilistic assertion. The explicit Python program and complete execution result accompany this document. The reversed orientation of the empty-face edge leaves it a sink and does not invalidate acyclicity of the nonempty-face matching.

By Forman's discrete Morse theorem, the geometric realization is homotopy equivalent to a CW complex with one zero-cell and thirteen nine-cells, and no other cells. Each nine-cell attaches its boundary to the unique zero-cell, because there are no cells in intervening dimensions. Every attaching map is therefore null, giving precisely \(\bigvee^{13}S^9\). This also establishes the claimed *integral* homology and eight-connectivity. The dimension thirteen of the original complex does not obstruct this homotopy collapse.

**Sharp vertex-cover bound.** The ten spoke edges \(u_i v_i\) form a perfect matching, so each vertex cover has at least ten vertices. The bipartition defined by the parity of the outer vertex indices, with opposite parity on inner vertices, has ten vertices per class; either class covers every edge. Hence \(\tau(G)=10\). The homotopy calculation implies \(\operatorname{conn}_{\mathbb F_2}=8\), proving equality in Matsushita's bound.

**Cyclic character.** Every rotation \(r^t\) permutes the faces. A face is fixed setwise exactly when it is a union of vertex-orbits under \(r^t\). For a fixed face, multiply its simplicial chain-sign by \((-1)^{\dim\sigma+1}\) (equivalently \((-1)^{|\sigma|}\)). The contribution is \((-1)^c\), where \(c\) is the number of selected vertex-orbits. Include the empty face with contribution \(1\). Since all reduced homology lies in degree nine, the reduced Lefschetz formula gives
\[
\operatorname{tr}\bigl(r^t\mid H_9(\mathcal D(G);\mathbb Q)\bigr)
=\sum_{\substack{\sigma\in\mathcal D(G)\\r^t\sigma=\sigma}}(-1)^{c(\sigma,r^t)}.
\]
This finite orbit enumeration gives the displayed ten values. A *second* calculation, traversing all simplices and computing the actual signs of their induced permutations, gives the same ten values; the identity check also equals the reduced Euler characteristic with its appropriate sign. Finally the four rational irreducible representations of \(C_{10}\) have degrees \(1,1,4,4\), and their traces at an element of order ten, five, and two uniquely solve to multiplicities \(1,4,0,2\). This proves the displayed rational decomposition.

## Verification
Run `python3 verifier.py` using only the Python standard library. It reconstructs the graph and both complete discrete-Morse certificates from the stated definitions. The certificate tests all \(2^{20}\) subsets, reports the complete face and facet vectors, verifies all \(3,663,100\) Hasse incidences and directed acyclicity in two different matchings, and independently computes both versions of every rotation trace. Its captured results are supplied as `verifier_output.json`. The full face enumeration and Morse certificate provide a finite proof for this *single* twenty-vertex graph; no inference from a finite initial segment of an infinite family is used.

## Relationship to prior work
Taylan established sphere homotopy types for dominance complexes of chordal graphs; the Desargues graph is nonchordal (it has induced cycles of length six). Matsushita established the general homological-connectivity/vertex-cover inequality, not its equality for this particular graph. Matsushita and Wakatsuki identified dominance complexes with Alexander duals of neighborhood complexes of graph complements and computed certain Cartesian-product examples. Their duality alone does not supply this homotopy type or the rotation character.

The known low-degree neighborhood-complex classification of Shukla does not cover the relevant neighborhood complex of the *complement* graph, which has degree sixteen; applying that theorem to the cubic graph itself instead studies another simplicial complex. Previously reported independence-complex and matching-complex calculations on the Desargues graph also involve different face conditions and do not imply this dominance-complex result. No previously inspected result established the thirteen-sphere wedge together with its cyclic character.

## Limitations
The classification concerns only the Desargues graph \(\operatorname{GP}(10,3)\). It does not assert an all-\(n\) theorem for generalized Petersen graphs, determine the integral equivariant module, or establish an equivariant splitting into spheres. Although the rational cyclic character is complete, the full automorphism-group representation is not computed. Literature comparison cannot exclude equivalent results in unindexed, unpublished, or inaccessible work.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754 (first publicly posted 2015-01-27), especially the chordal dominance-complex theorem.
2. T. Matsushita, *Dominance complexes and vertex cover numbers of graphs*, arXiv:2009.04145 (first publicly posted 2020-09-09), Theorem 1.
3. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639 (first publicly posted 2023-12-05), Theorems 1.1 and 5.16.
4. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (first publicly posted 2018-02-13), Theorem 2.1.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
