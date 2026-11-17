# Integral homotopy of the four-by-four square cylinder matching complex

## Finding
For the graph \(G=P_4\square C_4\), the ordinary matching complex has an integral homotopy equivalence
\[
|\mathcal M(G)|\simeq\bigvee^2 S^4\vee\bigvee^{27}S^5.
\]
Both wedge summands are essential: \(\widetilde H_4\cong\mathbb Z^2\), \(\widetilde H_5\cong\mathbb Z^{27}\), and the remaining reduced integral homology groups are zero.

## Assumptions and scope
The graph \(P_4\square C_4\) is simple, with vertex set \(\{(r,c):0\le r,c<4\}\). Its edges connect \((r,c)\) to \((r+1,c)\) for \(r<3\), and to \((r,c+1\pmod4)\) for every column. Thus it has 16 vertices, 28 edges, four cyclic columns, and *open* boundaries in the row direction. The graph is neither the open rectangular grid \(P_4\square P_4\) nor the fully periodic toroidal graph \(C_4\square C_4\).

The ordinary matching complex \(\mathcal M(G)\) has one vertex for each edge of \(G\); a finite subset is a simplex exactly when its graph edges are pairwise disjoint. The empty face is included in the combinatorial description and excluded from the unaugmented face poset used for the discrete-Morse matching. All boundary signs and homotopy statements use integer coefficients.

## Proof
**Enumeration.** Number graph vertices by \(4r+c\), and sort the 28 unoriented graph edges lexicographically by their endpoint pairs; give those graph edges indices \(0,\ldots,27\). Represent each matching as a 28-bit mask. Exhaustively branch over the edges in increasing order, including an edge exactly when neither endpoint has already been used. This produces precisely 21,497 faces including the empty one. The numbers in dimensions zero through seven are respectively 28, 306, 1,672, 4,863, 7,416, 5,470, 1,620 and 121. The supplied executable independently reconstructs this list.

**Acyclic matching.** Begin with the entire nonempty face poset, and for each edge index \(j=0,\ldots,27\), simultaneously pair every still-unmatched face \(a\) not containing \(j\) to \(a\cup\{j\}\) whenever both are still unmatched. Remove both matched faces before advancing to the next index. This specifies exactly 10,723 disjoint cover pairs. Reverse the matched cover incidences of the face-poset Hasse graph and orient every other incidence downwards. The executable constructs all 107,288 nonempty-to-nonempty Hasse cover incidences and topologically sorts the resulting directed graph; it visits every one of its 21,496 vertices, proving the absence of directed cycles. Consequently this is an acyclic face-poset matching, and Forman's discrete-Morse theorem applies. Exactly one critical vertex, 12 critical four-faces, and 37 critical five-faces remain; there are no other critical cells.

**Exact attaching matrix.** The integer cellular boundary between critical dimensions five and four is calculated by signed gradient-path summation. The simplicial boundary of an ordered edge set \(\{e_{i_0}<\cdots<e_{i_d}\}\) removes \(e_{i_k}\) with coefficient \((-1)^k\). If a four-face \(a\) is paired with a five-face \(b\), its projection to critical four-cells is minus the incidence sign of \(a\) in \(b\) times the corresponding projections of all other four-facets of \(b\), each with its signed incidence. For a critical four-face its projection is its own basis vector; four-faces that are lower-dimensional matching targets in no upward pair and are not critical have zero projection. Acyclicity makes the recursion well-founded. Project the boundary of each critical five-face by this recursion. This yields the exact signed matrix \(A\) of size \(12\times37\), stored in `boundary.json`; it has 108 nonzero entries, with absolute values at most two.

The displayed integer matrix has rank exactly ten: the first ten row indices and column indices \(0,1,2,4,6,7,8,14,16,17\) yield a \(10\times10\) determinant \(-1\), so rank is at least ten and the image contains a primitive rank-ten direct summand. To prove rank at most ten, the following two rows annihilate the entire matrix:

`[-1,1,1,-1,-1,-1,1,0,0,-1,1,0]`

`[1,-1,0,1,0,1,-1,1,1,1,0,1]`.

These are independent, hence the matrix rank is at most ten. Together, they establish integral Smith nonzero invariant factors \(1\) repeated ten times. The executable independently calculates the Smith normal form over \(\mathbb Z\).

**Homotopy conclusion.** Since the Morse CW complex has one zero-cell, 12 four-cells and 37 five-cells, its four-skeleton is \(\bigvee^{12}S^4\). Each five-cell attaches by a map from \(S^4\); the natural map \(\pi_4(\bigvee^{12}S^4)\to H_4(\bigvee^{12}S^4;\mathbb Z)\cong\mathbb Z^{12}\) is an isomorphism (the first nontrivial homotopy group of a 3-connected CW complex). Thus the integer columns of \(A\) completely describe the five-cell attaching maps up to homotopy. Integral elementary basis changes correspond to homotopy equivalences of the four-skeleton and cellular handle slides. The ten unit invariant factors cancel ten pairs of four- and five-cells. The remaining two four-cells and 27 five-cells attach trivially, giving exactly \(\bigvee^2S^4\vee\bigvee^{27}S^5\). No assertion about a larger family of cylinders is made.

## Verification
Run `python verify.py` with Python at least 3.10 and SymPy 1.14.0, with `verify.py` and `boundary.json` in the same directory. The verifier regenerates all faces and the acyclic matching, recomputes every signed Morse entry from gradient paths, verifies the unimodular minor and the two annihilating rows, then computes Smith factors. Separately, it reconstructs the *unreduced* simplicial boundary matrices over \(\mathbb F_2\), obtaining ranks \(27,279,1393,3470,3944,1499,121\) in degrees one through seven. Those ranks independently give reduced mod-two Betti numbers two in degree four and 27 in degree five. The mod-two computation is corroboration, not an argument for integral torsion-freeness; the integral proof is the primitive Morse attaching-matrix calculation. The exact expected output appears in `verification_output.txt`. All verification code and necessary data are included.

## Relationship to prior work
The motivating September 23, 2026 study by Chauhan, Sharma and Shukla treats homology of **open rectangular three-row** grids \(P_3\square P_n\), not a four-row cylinder. The earlier papers by Matsushita and by Goyal, Shukla and Singh treat two-row and three-row **open rectangular** grids, respectively; the latter article carries a correction/retraction warning and no theorem from it is used here. Published classifications of \(\mathcal M(P_4\square P_4)\), \(\mathcal M(P_3\square C_5)\), and the perfect-matching complex of \(C_4\square C_4\) concern distinct graph constructions or complex functors. In particular, the first rectangular four-by-four classification is a different mixed sphere wedge, \(\bigvee^6S^4\vee\bigvee^2S^5\). None of the inspected statements logically implies the exact homotopy type here. This comparison does not establish absolute novelty.

## Limitations
This is a finite exact calculation of one naturally distinguished graph, not a recurrence, periodic-width formula, or general classification of cylindrical grid matching complexes. There is no independent external mathematical audit. The full text of the motivating 2026 preprint was not accessible during this comparison; its available abstract and graph scope were examined. A relevant older unpublished grid calculation may remain unindexed or inaccessible. Those are remaining originality risks.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of 3×n grid graphs* (first publicly posted September 23, 2026), arXiv:2609.27366, https://arxiv.org/abs/2609.27366.
2. T. Matsushita, *Matching Complexes of Small Grids*, Electronic Journal of Combinatorics 26 (2019), P3.1, doi:10.37236/8480, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i3p1/pdf/.
3. S. Goyal, S. Shukla, A. Singh, *Matching complexes of 3×n grid graphs*, arXiv:2106.09915 (2021, withdrawn/retracted theorem claims; used only to compare graph definitions), https://arxiv.org/abs/2106.09915.
4. Public research record, *The matching complex of the 4×4 Cartesian square grid is a mixed-dimensional sphere wedge* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-matching-complex-of-the-4-times4-cartesian-square-grid-is-a--f1b5ea641880.
5. Public research record, *Mixed-dimensional matching-complex homotopy on the pentagonal three-row cylinder* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mixed-dimensional-matching-complex-homotopy-on-the-pentagonal-th--da8762498878.
