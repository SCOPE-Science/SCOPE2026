# A mixed-dimensional sphere wedge for the Hesse nonincidence neighborhood complex

## Finding
Let \(\mathcal A=\operatorname{AG}(2,3)\) be the nine-point affine plane over \(\mathbb F_3\), with twelve affine lines, and let \(B\) be its point–line **nonincidence** graph: a point and a line are adjacent precisely when the point is not on the line. For the ordinary Lovász open-neighborhood complex, the two components, on the point and line vertex classes respectively, have the same integral homotopy type:
\[
\boxed{\mathcal N(B)\simeq
\left(\bigvee^{11} S^3\vee S^4\right)
\sqcup
\left(\bigvee^{11} S^3\vee S^4\right).}
\]
The point component is a pure five-dimensional complex on nine vertices, while the line component is a pure seven-dimensional complex on twelve vertices. Both are non-shellable: their nonzero third homology lies below their facet dimensions. The statement is about this single affine plane, not about all affine planes. The associated **integral Betti numbers were already determined** through the line-free complex of the same affine plane; the new assertion is the full integral homotopy equivalence, supported by an explicit acyclic matching and integer attaching-degree calculation.

## Assumptions and scope
The affine points are \(P=\mathbb F_3^2\), indexed lexicographically. The lines are the twelve sets satisfying \(a x+b y=c\) over \(\mathbb F_3\), with \((a,b)\in\{(1,0),(0,1),(1,1),(1,2)\}\) and \(c\in\mathbb F_3\). Each line contains three points; each point lies on four lines. Hence \(B\) is bipartite, with nine point vertices, twelve line vertices, and seventy-two nonincidence edges.

For any simple graph \(G\), a nonempty vertex set is a face of \(\mathcal N(G)\) when its vertices have a common *open* neighbor. Since \(B\) is bipartite, every face is on one side. Write \(X_P\) and \(X_L\) for the point and line components. The facets of \(X_P\) are exactly the twelve six-point complements of the affine lines. The facets of \(X_L\) are exactly the nine eight-line complements of the four lines through a point. Both complexes have complete one-skeleta; in particular, these are exactly the two connected components.

In the language of noncover complexes, \(X_P\) is the complex of point sets avoiding at least one affine line. This is the noncover complex of the three-uniform line hypergraph of \(\mathcal A\). The opposite-side component is its Dowker dual for the finite nonincidence relation. The two components are not simplicially isomorphic: their vertex and facet dimensions differ.

## Proof
A complete finite proof is furnished by the source `verify_hesse_nonincidence.py` accompanying this result. The script defines the affine plane directly from the four normalized directions and three offsets each. It generates all faces from the facet complements and independently tests each of the \(2^9\) point subsets and \(2^{12}\) line subsets for a common nonincident line or point, respectively. The tests agree exactly.

The face enumeration, omitting the empty face, gives the dimension-indexed vectors
\[
 f(X_P)=(9,36,84,126,72,12),\qquad
 f(X_L)=(12,66,216,450,468,252,72,9).
\]
Thus \(X_P\) has 339 nonempty faces, and \(X_L\) has 1545.

For each component, the verifier builds a concrete acyclic discrete-Morse matching by processing vertex indices in order and, at each index, pairing each still-unmatched face not containing that vertex with its one-vertex extension, whenever both remain unmatched. The empty face is never matched. The point component has 163 pairs; the line component has 766 pairs. In each case, the remaining critical simplices consist of **one vertex, eleven three-simplices, and one four-simplex**. As a genuinely separate matching check, the script repeats the complete process in reverse vertex order, obtaining the same critical dimension counts.

For both matchings on both components, the verifier constructs the entire nonempty-face Hasse diagram and directs each cover relation from coface to facet, except that matched edges point upward. Complete topological sorting of these directed graphs certifies acyclicity: the point component has 1260 oriented incidences, and the line component has 7008. No unverified extrapolation beyond finite enumeration enters this assertion. Forman's discrete Morse theorem gives each component a CW model with one zero-cell, eleven three-cells, and one four-cell.

The critical four-cell's attaching class is computed **over the integers** rather than inferred from field homology. Orient each simplex by increasing vertex index. To reduce the signed boundary of the critical four-cell, whenever a three-face is the lower member of a matched three/four-dimensional pair, subtract the appropriate signed boundary of its matched four-face. The acyclic matching makes the reduction terminating. The full signed Morse boundary from the unique four-cell to the eleven three-cells is the **zero vector**, for each component and for both matching orders. The script performs this integer elimination explicitly.

Because the three-skeleton of the Morse model is a wedge of eleven three-spheres, the Hurewicz map \(\pi_3(\bigvee^{11}S^3)\to H_3(\bigvee^{11}S^3;\mathbb Z)\) is an isomorphism. The vanishing integral attaching-degree vector therefore means the four-cell attaching map is null-homotopic. Each component is consequently \(\bigvee^{11}S^3\vee S^4\), proving the assertion.

## Verification
Run `python3 verify_hesse_nonincidence.py` with Python 3 and the standard library alone. The complete recorded output is included as `morse_output.txt`. The two full incidence tests, complete Hasse-diagram topological sorts, exact integral critical boundary, and opposite-order matching are all recomputed.

The independent program `verify_binary_homology.py` constructs the same incidence relation using a separate coordinate enumeration, selects faces directly by subset containment, builds the simplicial mod-two boundary matrices, and computes their ranks by binary elimination. Its full output is `binary_output.txt`. The boundary ranks \(d_1,\ldots,d_5\) on the point component are \((8,28,56,59,12)\); the ranks \(d_1,\ldots,d_7\) on the line component are \((11,55,161,278,189,63,9)\). Both independently yield reduced mod-two Betti numbers eleven in degree three and one in degree four, vanishing otherwise. This field calculation is supporting evidence; the signed Morse reduction supplies the integral homotopy proof.

## Relationship to prior work
Alan Lew's 2021 doctoral thesis *Studies in topological combinatorics*, Introduction §1.5 and Chapter 7, studies the simplicial complex \(I_3\) of **line-free subsets** of \(\mathbb F_3^2\). Its Figure 1.1 already reports the full integral homology \(\widetilde H_2(I_3;\mathbb Z)=\mathbb Z\) and \(\widetilde H_3(I_3;\mathbb Z)=\mathbb Z^{11}\), with other degrees zero, and Theorem 1.5.2 establishes the top rank in a general affine-plane formula. Here \(I_3\) is **not** the present point neighborhood complex; it is the independence complex of the twelve-line hypergraph. The present point component is its combinatorial Alexander dual. Therefore combinatorial Alexander duality and universal coefficients already imply precisely the **integral homology groups** \(\widetilde H_3(X_P;\mathbb Z)=\mathbb Z^{11}\) and \(\widetilde H_4(X_P;\mathbb Z)=\mathbb Z\). By Dowker duality the line component has the same homotopy type as the point component. **None of these homology ranks or this abstract duality is claimed as new.**

The thesis does not state a homotopy sphere-wedge decomposition for the Alexander-dual noncover complex, give an explicit perfect discrete-Morse matching on that complex, or determine its integral attaching map. The new contribution here is the explicit **homotopy**, not homology, classification: exhibiting a three/four-dimensional CW model and proving its four-cell attaches trivially. Nontrivial attaching maps can share cellular ranks or homology in general; these properties cannot be inferred solely from Lew's Betti table without establishing sufficient connectivity and an appropriate CW model.

Kim and Kim define noncover complexes for arbitrary hypergraphs and derive homological bounds and homotopy classifications for tight paths and tight cycles. Their theorems do not provide the present acyclic matching or integral sphere-wedge homotopy classification.

A separately published homotopy calculation for the **nonincidence** graph of the thirteen-point **projective** plane \(\operatorname{PG}(2,3)\) finds \(igvee^{39}S^4ee S^5\) on each side; it does not classify the nine-point affine case. A classification of graph-metric **Vietoris–Rips** complexes of affine-plane **incidence** graphs produces \(igvee^{16}S^2eeigvee^{16}S^3\) at scale two for \(\operatorname{AG}(2,3)\), but uses different adjacency and simplices. A general result for the ordinary neighborhood complexes of Steiner-design **incidence** graphs applies to this affine design but produces circle wedges, not the present nonincidence complex. These statements do not subsume the new homotopy claim.

## Limitations
This is a complete finite homotopy classification for the order-three affine plane and its specified graph/complex conventions. It does not classify nonincidence neighborhood complexes at all affine-plane orders, establish an equivariant homotopy decomposition, or prove a general non-shellability theorem. The simultaneous point/line computations are finite exact checks, not evidence about uncomputed orders. The full integral homology ranks were previously available by Alexander duality from Lew's results, and are not claimed as new. Although closely related primary literature and research records were compared at the level of homotopy statements and implications, an equivalent homotopy classification in unindexed literature remains possible. Independent external scientific audit has not been performed.

## References
1. A. Lew, *Studies in topological combinatorics*, PhD thesis, Technion (August 2021), Introduction §1.5, Figure 1.1, Theorem 1.5.2, Chapter 7. https://www.math.cmu.edu/users/alanlew/files/theses/phd%20thesis.pdf
2. J. Kim and M. Kim, *Domination numbers and noncover complexes of hypergraphs*, arXiv:2101.01850v1, first publicly submitted 2021-01-06; *Journal of Combinatorial Theory, Series A* 180 (2021), article 105408. https://arxiv.org/abs/2101.01850
3. J. Kim and M. Kim, *Noncover Complexes, Independence Complexes, and Domination Numbers of Hypergraphs*, Séminaire Lotharingien de Combinatoire 84B.46 (2020), final manuscript 2020-04-30. https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2020/46.html
4. *Mixed-dimensional neighborhood-complex homotopy of the ternary projective nonincidence graph*, public mathematical result, https://github.com/published-finding corpus/2026 (identified public result; full `RESULT.md` compared).
5. *Affine-plane incidence Rips complexes have two sphere dimensions*, public mathematical result, https://github.com/published-finding corpus/2026 (identified public result; full `RESULT.md` compared).
6. S. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1 (2012), general contextual reference. https://arxiv.org/abs/1210.2803
