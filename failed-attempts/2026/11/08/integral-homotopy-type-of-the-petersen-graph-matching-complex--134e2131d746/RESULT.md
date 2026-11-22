# Integral homotopy type of the Petersen graph matching complex

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph: its vertices are the ten unordered two-element subsets of \(\{0,1,2,3,4\}\), and two are adjacent precisely when disjoint. Its ordinary matching complex \(\mathcal M(P)\) has one simplicial vertex per *edge of* \(P\), with a face for each collection of pairwise vertex-disjoint graph edges. There is an integral homotopy equivalence
\[
\mathcal M(P)\simeq \bigvee^5 S^2\vee\bigvee^5 S^3.
\]
Consequently \(\widetilde H_2(\mathcal M(P);\mathbb Z)\cong\mathbb Z^5\), \(\widetilde H_3(\mathcal M(P);\mathbb Z)\cong\mathbb Z^5\), and every other reduced integral homology group vanishes. This asserts the homotopy type, not just its Betti numbers.

## Assumptions and scope
The graph is simple and is exactly the ten-vertex Kneser graph specified above. Order its vertices lexicographically as two-subsets, then order its fifteen edges lexicographically by endpoint indices. Encode a collection of graph edges as a fifteen-bit nonnegative integer, whose set bits are the selected simplicial vertices. A mask is a face if and only if no two selected edges share an endpoint. All assertions concern this finite simplicial complex and ordinary integral homotopy, without equivariant structure.

## Proof
**Enumerate faces.** There are exactly 331 nonempty simplices. Their numbers in dimensions \(0,1,2,3,4\) are \((15,75,145,90,6)\), respectively. These counts follow from an exhaustive loop over all \(2^{15}\) edge masks, with independent endpoint-collision tests; the included verifier tests their agreement. The complex is nonpure: its facets occur in dimensions \(2,3,4\), with counts \(5,60,6\), respectively.

**Construct an acyclic matching.** Include the empty simplex in the augmented face poset. Start with all 332 faces unmatched. For each edge-bit index \(j=0,\ldots,14\), in increasing order, pair each as-yet-unpaired face \(F\) without bit \(j\) with \(F\cup\{j\}\), whenever both are still unpaired. This constructs exactly 159 disjoint matched covering relations. Orient every other face-poset covering relation downward and every matched relation upward. A complete topological-sort check on all 990 covering relations processes all 332 faces, proving no directed cycle exists. The unpaired simplices are precisely seven two-simplices and seven three-simplices. The empty face is paired with a vertex; under the standard augmented Morse convention this supplies a single base zero-cell. Thus the associated Morse CW complex has one zero-cell, seven two-cells and seven three-cells and no other cells.

**Compute attaching degrees over the integers.** Use increasing edge-bit orientation for each simplex, so the augmented signed boundary is \(\partial[e_0,\ldots,e_k]=\sum_i(-1)^i[e_0,\ldots,\widehat e_i,\ldots,e_k]\). For each matched low/high pair with current boundary coefficient \(a=\pm1\), cancel algebraically: replace any same-dimensional other column \(c\) by \(c-(\operatorname{coeff}_{low}(c)/a)\partial(high)\), then remove the paired generators. Choose the available unit pair with minimal high-cell size and then smallest high mask. This exact integer chain contraction terminates after 159 steps. The critical two-cells, ordered by bit mask, are \((162,276,530,1156,2336,4114,28672)\); the critical three-cells are \((5250,6416,10400,14464,17696,21760,25120)\). In these bases the complete signed degree boundary is
\[
\partial_3=\begin{pmatrix}
1&0&-1&0&1&0&1\\
0&-1&1&1&-1&-1&-1\\
0&0&0&0&0&0&0\\
0&0&0&0&0&0&0\\
0&0&0&0&0&0&0\\
-1&1&0&-1&0&1&0\\
0&0&0&0&0&0&0
\end{pmatrix}.
\]
Its sixth row is minus the sum of its first two rows, and all other rows are zero. The minor in its first two rows and first two columns has determinant \(-1\). Hence the Smith normal form has exactly two unit factors and five zero factors.

**Upgrade homology to homotopy.** The CW two-skeleton is \(\bigvee^{7}S^2\). By the (dimension-two) Hurewicz theorem, \(\pi_2(\bigvee^{7}S^2)\cong\mathbb Z^7\), so the attaching map of each three-cell is determined by its column of integer degrees. Integral elementary row changes are realizable by self-homotopy equivalences of the two-skeleton; elementary column changes correspond to changes of attaching-map generators. Bringing the degree matrix to \(\operatorname{diag}(1,1,0,0,0,0,0)\) gives two contractible two-/three-cell pairs, leaving five freely attached two-spheres and five three-cells with nullhomotopic attaching maps. This proves the displayed wedge equivalence. The argument asserts no stronger equivariant equivalence.

## Verification
The standalone script `verification/petersen_matching_verify.py` requires only Python 3 standard libraries and runs with `python3 verification/petersen_matching_verify.py`. It checks every graph edge and simplex, two independent face predicates, the complete 990-incidence acyclicity test, all 159 integral chain cancellations, the exact displayed boundary, and original simplicial chain ranks independently modulo primes \(2,3,5,7\). Expected output is embedded as `verification/verification_output.txt`. The integral homotopy argument requires the exact matrix and topological attaching-map reasoning; finite-field checks alone do not establish the integral claim.

## Relationship to prior work
Björner, Lovász, Vrećica and Živaljević (1994) initiated connectivity methods for matching and chessboard complexes, primarily for complete graphs. Shareshian and Wachs (2004 preprint; 2007 journal article), Jonsson (2008 journal article; 2012 uploaded manuscript), and Mondal, Mukherjee and Saha (2023 preprint; 2024 journal article) study the ordinary matching complexes of *complete* graphs. In particular, the observation that the one-dimensional complex \(\mathcal M(K_5)\) **is the Petersen graph** does not determine the higher-dimensional complex \(\mathcal M(P)\) *of the Petersen graph*, as treated here. Nikseresht's classifications address Gorenstein and Cohen–Macaulay properties and do not give this integral homotopy type. Published findings concerning the two-matching complex of \(P\) and the discrete Morse complex *of* \(P\) treat mathematically different constructions; neither published result statement implies this equivalence.

## Limitations
This is a self-contained finite case, not an infinite-family theorem. No automorphism-representation computation or equivariant splitting is claimed. Although several highly relevant full primary manuscripts were inspected, an unindexed or inaccessible overlapping result may exist; novelty is assessed relative to the explicitly inspected sources. No independent validation is claimed.

## References
1. A. Björner, L. Lovász, S. T. Vrećica, R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, J. London Math. Soc. 49 (1994), 25–39. https://doi.org/10.1112/jlms/49.1.25 (published 1994-02-01).
2. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054 (first public 2004-09-03); Adv. Math. 212 (2007), 525–570. https://arxiv.org/abs/math/0409054
3. J. Jonsson, *Exact Sequences for the Homology of the Matching Complex*, J. Combin. Theory Ser. A 115 (2008), 1504–1526; manuscript arXiv:1203.5641. https://arxiv.org/abs/1203.5641
4. A. Mondal, S. Mukherjee, K. Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, Discrete Math. Theor. Comput. Sci. 26:3 (2024), article 13. https://arxiv.org/abs/2305.02973
5. A. Nikseresht, *Gorenstein and Cohen-Macaulay Matching Complexes*, arXiv:2106.13993. https://arxiv.org/abs/2106.13993
