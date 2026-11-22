# Thirty-four three-spheres in the perfect-matching complex of the six-column square cylinder

## Finding
Let \(G=P_3\square C_6\) be the Cartesian product of a three-vertex path and a six-cycle. Let \(\mathcal P(G)\) be the abstract simplicial complex on the edges of \(G\) whose facets are the edge sets of perfect matchings. Then its geometric realization has the **integral homotopy type**
\[
|\mathcal P(G)|\simeq\bigvee^{34}S^3.
\]
Consequently \(\pi_1(|\mathcal P(G)|)=0\), \(\widetilde H_3(\mathcal P(G);\mathbb Z)\cong\mathbb Z^{34}\), and all other reduced integral homology groups vanish. This pure eight-dimensional complex is not shellable.

## Assumptions and scope
Vertices of \(G\) are pairs \((r,c)\), with \(r\in\{0,1,2\}\) and \(c\in\mathbb Z/6\mathbb Z\). Its undirected graph edges are exactly \(\{(r,c),(r,c+1)\}\), with addition modulo six, together with \(\{(r,c),(r+1,c)\}\) for \(r\in\{0,1\}\). Thus there are 18 graph vertices and 30 graph edges. There are no edges joining the first and third rows. Each perfect matching has nine edges, so \(\mathcal P(G)\) is pure of dimension eight. This is the *perfect-matching extendibility* complex, not the ordinary matching complex of all partial matchings.

The proof is finite and exact. Graph vertices are labelled by \(6r+c\); graph edges are sorted as ordered endpoint pairs; a face is represented by a 30-bit integer whose set bits mark its graph edges. The three included certificates and the standalone checker reconstruct the complete finite computation with no external datasets.

## Proof
**1. Exhaustive face enumeration.** Enumerate all perfect matchings by choosing the least uncovered graph vertex and trying each still-available incident edge. This branches over every possible perfect matching uniquely. Exactly 108 perfect matchings result. Taking every nonempty subset of each perfect matching and deduplicating the corresponding 30-bit masks yields 30,353 nonempty faces. The face counts in dimensions zero through eight are
\[
(30,363,2194,6258,9144,7600,3684,972,108).
\]
The checks are performed on the explicit graph, not on a separately supplied table.

**2. Strong deformation retraction to a three-complex.** A codimension-one face \(\sigma\) is free whenever its set of currently present immediate cofaces consists of exactly one face \(\tau\). The certificate `certificates/collapse_pairs.tsv` lists 14,436 successive pairs \((\sigma,\tau)\). The checker reconstructs the original complex and verifies, at the time of each deletion, that both faces exist, that \(\sigma\subset\tau\), and that \(\tau\) is the unique coface; it also checks that \(\tau\) has no cofaces. Each deletion is therefore an elementary simplicial collapse. The remaining simplicial complex \(Y\) has nonempty face counts
\[
(f_0,f_1,f_2,f_3)=(30,270,694,487),
\]
with no higher-dimensional faces. Hence \(|\mathcal P(G)|\simeq|Y|\).

**3. Trivial fundamental group.** Choose the canonical 29-edge spanning tree of the one-skeleton of \(Y\), obtained by scanning edges in mask order and retaining the ones that join distinct components. Collapse the tree when forming the standard edge-path presentation of \(\pi_1(Y)\). The certificate `certificates/pi1_relations.tsv` supplies 241 triangular relations in an order where each relation has two previously trivial edge loops and exactly one still-uneliminated edge loop. Each such triangle kills that last generator. Every one of the remaining 241 non-tree edges is eliminated, proving \(\pi_1(Y)=1\). This is an integral group-presentation argument, not merely a vanishing first-Betti calculation.

**4. Exact integral boundary calculation.** Orient each simplex by increasing graph-edge index. The free cellular chain groups of \(Y\) have ranks \(30,270,694,487\) in dimensions zero through three. The spanning-tree and triangular elimination from Step 3 give \(\operatorname{rank}\partial_1=29\) and \(\operatorname{rank}\partial_2=241\). In fact, those triangle eliminations are also integral unit pivots for the boundary \(\partial_2\) after contracting the tree.

The certificate `certificates/unit_pivots.tsv` supplies 453 sequential integral unit pivots for the 694-by-487 matrix of \(\partial_3\). At each step, the checker confirms a pivot of \(\pm1\), makes the exact Schur-complement update arising from unimodular row and column operations, and removes the pivot row and column. The residual matrix is identically zero, so the Smith invariants are 453 copies of one and 34 zero columns. The checker also independently verifies \(\partial_2\partial_3=0\) on all 487 tetrahedra. It follows that \(\operatorname{im}\partial_3\) is primitive in \(C_2(Y;\mathbb Z)\), and
\[
\operatorname{rank}\ker\partial_2=694-241=453
=\operatorname{rank}\operatorname{im}\partial_3.
\]
Thus \(H_2(Y;\mathbb Z)=0\), including absence of torsion; while \(H_3(Y;\mathbb Z)\cong\mathbb Z^{487-453}=\mathbb Z^{34}\). The fundamental-group proof gives \(H_1=0\), and there is no homology above degree three.

**5. Recover the homotopy type.** Because \(Y\) is simply connected and \(H_2(Y;\mathbb Z)=0\), the degree-two Hurewicz theorem gives \(\pi_2(Y)=0\). Degree-three Hurewicz identifies \(\pi_3(Y)\) with \(H_3(Y;\mathbb Z)\). Choose maps from 34 three-spheres representing an integral homology basis and wedge them to a map into \(Y\). This is an integral homology equivalence between simply connected CW complexes, hence a homotopy equivalence by the homological Whitehead theorem. Finally a pure shellable eight-dimensional simplicial complex has reduced homology only in dimension eight, so the nonzero third homology also proves nonshellability.

## Verification
From the directory containing `check.py` and the three certificate files in `certificates/`, execute `python3 check.py`. It uses only the Python standard library and checks the complete face enumeration, every elementary collapse, the triangular fundamental-group presentation, the integer chain relation, every unit pivot, and all displayed counts. The provided `verification_output.txt` records the successful run. The `--generate` option additionally constructs the same three certificates from the input graph; the ordinary invocation independently validates the packaged certificates rather than trusting recorded output.

## Relationship to prior work
Chandrakar, Chau, Goyal, Karki and Subhash [1] prove an infinite-family homotopy classification for the **open** three-by-even rectangular grids. Their defining edge set excludes longitudinal wrap-around edges, and their proof does not determine this cylinder. In particular the open six-column graph has the homotopy type of one two-sphere, whereas closing the three longitudinal wrap-around edges gives 34 three-spheres here.

Agarwal and Basak [2] classify the perfect-matching complexes of Möbius and circular ladders; the circular ladder is a **two-row** graph \(C_n\square P_2\), not the three-row cylinder studied here. Bayer, Jelić Milutinović and Vega [3] study honeycomb graph perfect-matching complexes. A published exact result for the ordinary matching complex of this **same** graph gives 48 five-spheres [4], but it concerns all partial matchings, whereas the present complex keeps only partial matchings extendible to a perfect matching. Similarly, previously computed transversal-periodic three-row strips [5] have graph \(C_3\square P_n\), not \(P_3\square C_6\). Neither statement implies the present homotopy type.

## Limitations
Only the six-column three-row square cylinder and its ordinary, nonequivariant integral homotopy type are classified. No recurrence for other circumferences, action of the graph automorphism group, or result for the ordinary matching complex is claimed. The proof depends on complete finite certificates and standard CW-homotopy theorems. An independent mathematical audit has not been performed; unindexed or otherwise inaccessible equivalent work remains a publication-priority risk.

## References
1. H. Chandrakar, T. Chau, S. Goyal, R. Karki, B. Subhash, *Perfect Matching Complexes of \(3\times 2n\) Grid Graph*, arXiv:2611.18058v1, first public November 13, 2026, https://arxiv.org/abs/2611.18058.
2. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2, first public August 31, 2026, https://arxiv.org/abs/2608.30601.
3. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, Electronic Journal of Combinatorics 30(2), P2.45 (2023), https://doi.org/10.37236/11525.
4. *Forty-eight five-spheres in the matching complex of \(P_3\square C_6\)*, published exact computation, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-forty-eight-five-spheres-in-the-matching-complex-of-p-3-square-c--0ec52badec4f.
5. *A boundary-sensitive eight-column classification of three-row perfect-matching complexes*, published exact computation, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-boundary-sensitive-eight-column-classification-of-three-row-pe--c400769702b4.
