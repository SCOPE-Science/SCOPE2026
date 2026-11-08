# Perfect-matching complex of the four-cube: \(54\) three-spheres and \(21\) four-spheres

## Finding
Let \(Q_4\) be the graph on the sixteen binary words of length four, with an edge between words differing in exactly one coordinate. Let \(\mathcal M_p(Q_4)\) be the simplicial complex on its 32 edges whose faces are the edge subsets extendable to a perfect matching. Then
\[
\mathcal M_p(Q_4)\simeq\left(\bigvee^{54}S^3\right)\vee\left(\bigvee^{21}S^4\right).
\]
Its only nonzero reduced integral homology is \(\widetilde H_3\cong\mathbb Z^{54}\) and \(\widetilde H_4\cong\mathbb Z^{21}\). The complex is pure of dimension seven but not shellable. Via \(Q_4\cong C_4\square C_4\), this also determines the perfect-matching complex of the sixteen-vertex four-by-four *toroidal* square grid (not the rectangular grid \(P_4\square P_4\)).

## Assumptions and scope
All graphs are finite and simple. A perfect matching is a set of mutually disjoint graph edges covering all graph vertices. A face of \(\mathcal M_p(G)\) is precisely a subset of some perfect matching; thus facets are all perfect matchings. The claim concerns ordinary nonequivariant, integral homotopy type. Spheres in the displayed wedge carry their usual based CW topology. The graph is exactly \(Q_4\), not a statement for arbitrary dimensions, toroidal grids, or graph families.

## Proof
**Exhaustive underlying complex.** Number the binary vertices by integers \(0,\ldots,15\) and list the undirected graph edges \((u,v)\) lexicographically, with \(u<v\) and \(u\oplus v\in\{1,2,4,8\}\). A recursive enumeration that chooses the least uncovered vertex and tries each available neighbor produces all 272 perfect matchings, each of cardinality eight. Independently, bipartition the vertices by Hamming-weight parity and assign the eight even vertices injectively to their adjacent odd neighbors. This yields exactly the same 272 edge sets. Exhausting the subsets of the resulting perfect matchings yields 30,561 distinct simplicial faces, including the empty face. A separate enumeration of all 41,025 graph matchings, checking whether the unmatched induced graph admits a perfect matching by vertex-subset recursion, agrees exactly with membership in those 30,561 faces. The number of faces in dimensions \(-1,0,1,2,3,4,5,6,7\) is
\[
(1,32,400,2496,7776,10560,6848,2176,272).
\]

**Acyclic matching.** Run successive element toggles through the 32 lexicographically ordered edge-vertices of the simplicial complex. At each toggle, pair every remaining face not containing the toggled edge with its remaining coface obtained by adding that edge. No simplex appears in more than one pair. The successive-element matching is acyclic by the standard patchwork argument; independently, orient every unmatched Hasse cover from a face to its codimension-one subface and every matched cover in the opposite direction. Topological sorting visits all 30,561 nodes in this directed graph, comprising 150,720 cover incidences, so there is no gradient cycle. The result has 15,173 matched pairs (including the pair containing the empty face), with exactly 124 critical three-simplices and 91 critical four-simplices, and no other critical simplices. Forman's theorem gives a CW complex with one basepoint, 124 three-cells and 91 four-cells.

**Exact integral Morse boundary.** Orient each simplex by increasing edge indices. For each matched lower face \(L\) and upper face \(U\), write \(\partial U=\epsilon L+\sum_{F\ne L}\epsilon_F F\) with \(\epsilon\in\{\pm1\}\), and recursively eliminate \(L\) using \(L=-\epsilon\sum_{F\ne L}\epsilon_F F\). Matched upper cells project to zero and critical cells to their basis elements. The acyclic orientation ensures recursion terminates. Applying the projection to the boundaries of the 91 critical four-simplices gives the exact integer Morse boundary matrix of shape \(124\times91\). A deterministic integer elimination uses 70 pivots, each equal to \(+1\) after sign normalization; elementary row and column operations leave the remaining submatrix identically zero. Therefore the Smith factors of the nonzero boundary are exactly 70 units, with rank 70 and no torsion.

**Promotion to homotopy.** There are no critical cells in dimensions one or two. The three-skeleton is therefore a wedge of 124 three-spheres. The attaching maps of the four-cells lie in \(\pi_3(\bigvee^{124}S^3)\cong\mathbb Z^{124}\), identified by their cellular degrees (the relevant Hurewicz map is an isomorphism). Unimodular row and column operations are realized by homotopy changes of bases and cellular handle slides. The 70 unit attachments cancel 70 pairs of three- and four-cells; the remaining 54 three-cells and 21 four-cells are attached trivially. This proves the displayed integral homotopy equivalence.

**Non-shellability.** The 272 eight-edge perfect matchings are all facets, so the complex is pure of dimension seven. A pure shellable complex has reduced homology only in its top dimension, whereas here dimensions three and four have nonzero reduced homology. Thus the complex cannot be shellable.

## Verification
The standalone standard-library script `verify.py`, supplied with this result, reconstructs the graph, enumerates perfect matchings in two independent ways, checks all graph matchings against a second extendability predicate, constructs both ascending- and descending-edge discrete-Morse matchings, checks all 150,720 Hasse incidences for directed acyclicity, forms exact signed integer Morse boundary matrices, and performs unit-only integer matrix elimination. Its output is supplied in `verify_output.txt`.

The reverse-order matching independently has 15,154 matched pairs and critical cells in dimensions three, four, five numbering 134, 110, 9. Its boundary ranks are 80 (degree four to degree three) and 9 (degree five to degree four), with unit pivots, and the composition of consecutive Morse boundaries vanishes. In addition, direct mod-two reduction of the *unreduced* simplicial boundary matrices has ranks \((1,31,369,2127,5595,4944,1904,272)\) in degrees zero through seven, giving reduced Betti numbers \(54\) and \(21\) in degrees three and four and zero otherwise. These are independent numerical cross-checks; the forward exact integral Morse construction is the proof of the homotopy type.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega [1] introduced the perfect-matching-complex homotopy problem for honeycomb families, proving sphere-wedge or contractible results in the explicitly treated instances. Their main theorems concern honeycomb tilings, not the four-cube or a square toroidal grid. Chandrakar and Singh [2] treat rectangular two-row grids and polygonal *line* tilings, and formulate a broader question for rectangular grids; neither their theorems nor the definition of a rectangular grid includes the periodic four-by-four toroidal graph. The later Möbius-ladder classification [3] concerns cubic graphs and does not include the four-regular four-cube. Kiwi and Loebl [4] study parity types and bijections of perfect matchings on toroidal square grids, not the topology of the simplicial complex generated by those perfect matchings. Perfect matching counts and parity identities do not determine its attaching maps or homotopy type. Existing results on ordinary matching, independence, cut, and nerve complexes of a cube or square grid address different face conditions. The result establishes a new exact instance of the perfect-matching-complex homotopy question, subject to the possibility of an independently obtained but unindexed equivalent result.

## Limitations
The theorem is for the explicitly defined sixteen-vertex graph only. It does not classify \(\mathcal M_p(Q_d)\) for other \(d\), prove a family formula, determine the action of the automorphism group on homology, or determine the inclusion into the ordinary matching complex. The finite certificates are exhaustive for this graph because every perfect matching and every face is enumerated, not because sampling is presumed sufficient. No external independent audit of these calculations is asserted.

## References
[1] M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (first posted 2022-09-06), later Electronic Journal of Combinatorics 30 (2023), P2.45. https://arxiv.org/abs/2209.02803

[2] H. Chandrakar, A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v1 (first posted 2024-07-08); see Theorem 1.1 and Section 6. https://arxiv.org/abs/2407.05809

[3] A. Agarwal, B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601v1 (first posted 2026-08-31), main theorem. https://arxiv.org/abs/2608.30601

[4] M. Kiwi, M. Loebl, *Types of Perfect Matchings in Toroidal Square Grids*, arXiv:1406.3317v1 (first posted 2014-06-12), introductory Theorems 1–2. https://arxiv.org/abs/1406.3317
