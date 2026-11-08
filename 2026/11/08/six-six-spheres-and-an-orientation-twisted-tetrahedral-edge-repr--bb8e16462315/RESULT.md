# Six six-spheres and an orientation-twisted tetrahedral edge representation in a total cut complex

## Finding
Let \(T\) be the truncated-tetrahedral graph and let \(X=\Delta^t_3(T)\) be its total three-cut complex. Then
\[
X\simeq\bigvee^{6} S^6
\]
**integrally and nonequivariantly**. The rational homology action of the full tetrahedral symmetry group \(\mathfrak S_4\) is
\[
\widetilde H_6(X;\mathbb Q)\cong\operatorname{sgn}\otimes\mathbb Q[E(K_4)]
\cong\operatorname{sgn}\oplus S^{(2,1,1)}\oplus S^{(2,2)},
\]
where \(\mathbb Q[E(K_4)]\) is the six-dimensional permutation module on the edges of the untruncated tetrahedron. Hence this rational homology has no nonzero invariant vector. The pure eight-dimensional complex is not shellable. These are aspects of **one** complete homotopy-and-symmetry classification, not separate findings.

## Assumptions and scope
The vertex set is \(V=\{(i,j):0\le i,j\le3,\ i\ne j\}\), with lexicographic indexing. Two different vertices are adjacent if their first coordinates are equal, or if they are reversed ordered pairs. This is the usual graph obtained by truncating the vertices of a tetrahedron, with four disjoint triangular faces and six remaining edges. In particular there are twelve graph vertices and eighteen graph edges.

An independent triple is a three-element subset spanning no graph edge. By definition, a face \(F\subseteq V\) of \(X\) is precisely a subset whose complement \(V\setminus F\) contains an independent triple. A facet has nine graph vertices, hence the complex is pure of dimension eight. Homotopy and integral homology concern the geometric realization of this finite abstract simplicial complex. The symmetry statement is only over \(\mathbb Q\), without an assertion that the homotopy equivalence is equivariant.

## Proof
**Two complete enumerations.** Enumerate the \(\binom{12}{3}=220\) triples of graph vertices. Exactly \(72\) are independent. Complement these triples to construct the \(72\) generating facets, and enumerate all their subsets. Independently, test each of the \(4096\) vertex masks by scanning its complement directly for three pairwise nonadjacent vertices. The procedures agree on all \(3674\) faces, including the empty face. The numbers of faces of dimensions \(-1,0,1,2,3,4,5,6,7,8\) are
\[
(1,12,66,220,495,792,918,744,354,72).
\]
The alternating sum is \(6\), the expected reduced Euler characteristic.

**A complete acyclic matching.** Include the empty simplex in the face poset, and initially mark every face available. Fix the lexicographic vertex order. For each vertex in that order, pair every still-available face \(F\) not containing that vertex with \(F\cup\{v\}\) whenever both are available, removing both before proceeding. This yields \(1834\) pairs and just six unpaired faces, each of dimension six. The reversed vertex order independently gives the same critical dimension distribution.

A checker constructs **every** covering incidence \(F\subset F\cup\{v\}\) among the \(3674\) faces; there are \(20940\) incidences. Orient unmatched incidences from the larger face to the smaller, and matched incidences in the opposite direction. A complete topological sort visits all \(3674\) vertices of this directed Hasse graph under both matchings, proving absence of directed cycles. In the ordinary (non-augmented) face poset, omit the pair containing the empty simplex; this leaves one critical zero-cell and six critical six-cells. Forman's discrete Morse theorem gives a CW model with precisely those cells. Since all six attaching maps meet only the zero-skeleton, it is a wedge of six six-spheres. This establishes the integral homotopy type, not merely a finite-field Betti computation.

**Exact symmetry action.** The four graph triangles, one for each first coordinate, are the graph's only triangles; each pair of them is connected by exactly one remaining graph edge. Thus every automorphism permutes the four triangles and the induced permutation determines its action on every vertex. Conversely all \(24\) permutations of the four labels preserve adjacency. Hence \(\operatorname{Aut}(T)\cong\mathfrak S_4\).

For each of these \(24\) graph automorphisms, enumerate every invariant oriented simplex and weight it by the sign of the induced permutation of its vertices and by \((-1)^{\dim F}\). Include the empty face with weight \(-1\), obtaining the **reduced** Lefschetz number. All reduced homology is concentrated in the even dimension six, so this number equals the trace on \(\widetilde H_6(X;\mathbb Q)\). For permutation cycle types \(1^4,2\,1^2,2^2,3\,1,4\), in that order, the traces are
\[
(6,-2,2,0,0).
\]
On the six edges of the original tetrahedron, the numbers of fixed unordered edges for those types are \((6,2,2,0,0)\). Twisting by the permutation sign gives exactly \((6,-2,2,0,0)\). Equality of rational characters gives \(\widetilde H_6(X;\mathbb Q)\cong\operatorname{sgn}\otimes\mathbb Q[E(K_4)]\). The standard \(\mathfrak S_4\) character table decomposes this as \(\operatorname{sgn}\oplus S^{(2,1,1)}\oplus S^{(2,2)}\), of dimensions \(1+3+2=6\), with no trivial constituent.

Finally, a pure shellable eight-dimensional complex has reduced homology only in its top dimension, whereas \(X\) has nonzero reduced integral homology in dimension six. Therefore \(X\) is not shellable.

## Verification
Run `python3 verify.py` from the unpacked complete file set. It uses only the Python standard library. It independently reconstructs every graph edge, independent triple, face, matching pair and directed Hasse incidence, and performs full acyclicity topological sorts. It computes orientation-signed reduced Lefschetz traces for all \(24\) symmetries and checks all five rational irreducible character multiplicities. Two opposite vertex orders provide separate acyclic matchings. Expected output is stored in `verification_output.txt`; the packaged script was executed and the output matched exactly. The finite computations are exhaustive for this precisely defined graph, not evidence for any infinite family.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue define total cut complexes and calculate paths, cycles, chordal graphs, complete multipartite graphs, clique prisms and grids. Their general simplicial-vertex and chordal formulas do not imply this result: \(T\) has induced six-cycles, is not chordal and has no simplicial vertex. The follow-up results for rectangular grids treat other graph families. A robust-clique-complex classification for bipartite square-sequence graphs cannot cover \(T\), which contains four triangles. Recent cycle-power and Cartesian-product theorems also do not treat the truncated tetrahedral graph at this cut level. The ordinary three-cut complex is **not** the total three-cut complex: its facets also come from disconnected triples that are not independent, and an existing theorem covering the ordinary cut complex therefore does not imply the claim.

An existing hexagonal-prism total-three-cut computation concerns a nonisomorphic twelve-vertex cubic graph and a different symmetry group; neither its sphere rank nor its character determines the present result. Exact-name, alias, graph-operation, Alexander-dual/robust-clique, symmetry-module, and parameter searches were compared. No inspected statement covers both the six-sphere integral homotopy classification and its \(\mathfrak S_4\)-character for this graph.

## Limitations
Only the specified truncated-tetrahedral graph is classified. There is no claimed classification for arbitrary truncated polyhedra, no equivariant homotopy decomposition, and no integral \(\mathbb Z[\mathfrak S_4]\)-lattice decomposition. A logically equivalent result in unindexed literature could affect originality. The verifier checks a finite combinatorial certificate; no independent external mathematical audit has been performed.

## References
- M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, first posted 2022-09-27. https://arxiv.org/abs/2209.13503
- M. Bayer et al., *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first posted 2023-04-26. https://arxiv.org/abs/2304.13675
- H. Chandrakar, N. R. Hazra, D. Rout, A. Singh, *Topology of Total Cut and Cut Complexes of Grid Graphs*, arXiv:2408.07646, first posted 2024-08-14. https://arxiv.org/abs/2408.07646
- M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first posted 2026-02-11. https://arxiv.org/abs/2602.11365
- A. Carnero Bravo, *Total Cut Complexes and Their Duals*, arXiv:2602.21427, first posted 2026-02-24. https://arxiv.org/abs/2602.21427
- E. W. Weisstein, *Truncated Tetrahedral Graph*, MathWorld, accessed 2026-11-01. https://mathworld.wolfram.com/TruncatedTetrahedralGraph.html
