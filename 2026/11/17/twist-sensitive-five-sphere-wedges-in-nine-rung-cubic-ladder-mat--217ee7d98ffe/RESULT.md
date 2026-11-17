# Twist-sensitive five-sphere wedges in nine-rung cubic ladder matching complexes

## Finding
For the Möbius ladder \(M_{18}\) on eighteen vertices and the untwisted nine-rung prism \(P_9=C_9\square K_2\), their **ordinary** matching complexes have the following complete integral homotopy types:
\[
\boxed{\mathcal M(M_{18})\simeq\bigvee^{22} S^5,\qquad \mathcal M(P_9)\simeq\bigvee^{24} S^5.}
\]
Thus closing the same nine-rung ladder strip with or without the Möbius twist changes the number of five-spheres by two, while neither closure has a nontrivial integral homology group outside degree five. These classifications concern exactly the two stated eighteen-vertex graphs, not an infinite ladder family.

## Assumptions and scope
All graphs are finite, simple, undirected. Set \(V(M_{18})=\mathbb Z/18\mathbb Z\). Its edges are the eighteen successive cycle edges \(\{i,i+1\}\) and the nine antipodal edges \(\{i,i+9\}\) for \(0\le i<9\). Define \(P_9\) with vertices \((i,a)\), \(i\in\mathbb Z/9\mathbb Z\), \(a\in\{0,1\}\), and edges \(\{(i,a),(i+1,a)\}\) and \(\{(i,0),(i,1)\}\). Each has 27 edges and 18 vertices. The **ordinary matching complex** \(\mathcal M(G)\) has the graph edges as simplicial vertices and all collections of pairwise disjoint graph edges as faces, whether or not extendible to a perfect matching. All homotopy and homology claims are integral. The empty matching is the formal simplicial empty face and is not a geometric cell. Graph edges are lexicographically ordered as endpoint pairs and encoded by bitmasks in `check_ladder18.py`.

## Proof
**Complete face enumeration.** The verifier constructs the exact conflict bitmask for every graph edge and uses an exhaustive include/exclude recursion. At each branch it excludes the first remaining edge or includes it and excludes all incident edges. These mutually exclusive branches enumerate precisely all matchings. After deduplication the numbers of nonempty simplices are 36,627 for the Möbius closure and 36,625 for the prism. The complete face counts by dimension \(0,1,\ldots,8\) are respectively \((27,297,1719,5652,10656,11097,5823,1278,78)\) and \((27,297,1719,5652,10656,11097,5823,1278,76)\).

**An explicit acyclic matching of faces.** Starting with every nonempty face available, process the 27 lexicographically ordered edge indices in descending order. At each index, pair each remaining face missing the selected edge to its coface obtained by adding that edge, if both faces remain available, and remove both. Every face appears in at most one pair. To check acyclicity, the verifier constructs all cover relations of the nonempty face poset, orients each matched cover upward and every other cover downward, and exhaustively topologically sorts this directed graph. The sorted vertex counts, including the isolated formal empty face, are 36,628 and 36,626, respectively; all 199,908 and 199,890 nonempty-face covering relations were checked. Both directed graphs are acyclic. Forman's theorem therefore produces CW models with the following complete critical-cell census:

| Graph | Critical 0-cells | Critical 5-cells | Critical 6-cells |
| --- | ---: | ---: | ---: |
| Möbius closure | 1 | 23 | 1 |
| Prism closure | 1 | 26 | 2 |

There are no critical cells in any other dimension. The respective numbers of matched geometric face pairs are 18,301 and 18,298.

**Signed integral attaching degrees.** Orient every simplex in increasing graph-edge order, so removing its \(j\)-th listed edge produces incidence \((-1)^j\), starting from \(j=0\). For every matched pair \(L\subset U\), signed boundary cancellation replaces the matched lower face by minus the remaining boundary of its upper partner divided by the incidence \([U:L]\in\{\pm1\}\). The verifier recursively performs all such eliminations along the acyclic matching and constructs the complete integral critical \(6\)-to-\(5\) cellular degree matrices. Its `morse_boundary_6_to_5` arrays are exact integer values, not numerical approximations.

In the Möbius case the boundary has matrix size \(1\times23\), and column 6 (counting from one) has value \(+1\). In the prism case the boundary has matrix size \(2\times26\), and the submatrix in columns 8 and 14 has determinant \(+1\). Therefore both matrices have full row rank and a unimodular full-rank minor. Each permits integral elementary basis changes reducing its full attaching map to unit coordinates and thus cellular cancellation of one, respectively two, adjacent \(5\)- and \(6\)-cell pairs. There are no cells of dimensions one through four; consequently the five-skeleton is a wedge of five-spheres, and maps from a five-sphere into such a wedge are classified by their integer degrees, since \(\pi_5(\bigvee S^5)\cong\mathbb Z^r\). Thus these unit degree reductions are homotopy-preserving rather than merely homology-preserving. After the cancellations there is one 0-cell and exactly 22, respectively 24, 5-cells attached by constant maps. This proves the stated integral sphere-wedge homotopy types.

## Verification
Run `python3 check_ladder18.py` using Python 3 with only the standard library; its complete expected JSON output is `check_ladder18_output.json`. It reconstructs faces, the entire oriented Hasse graph, an acyclic matching, signed integral critical-cell boundaries and the specified unit minors. Independently of the Morse boundary calculation, it computes mod-two homology by Gaussian elimination on the original unreduced simplicial boundary matrices: the only nonzero reduced mod-two Betti ranks are respectively 22 and 24 in degree five. Alternating Euler sums are \(-22\) and \(-24\). The mod-two computations cross-check, but do not replace, the integral unit-minor homotopy proof.

## Relationship to prior work
Agarwal and Basak, arXiv:2608.30601, first publicly released 2026-08-31, establish homotopy types for the **independence** and **perfect-matching** complexes of both ladder families; their Problem 26 explicitly asks for the ordinary matching complexes. Their full manuscript's definitions and main theorems distinguish these objects and do not imply the present two conclusions. The separately available full proofs *Three integral homotopy types of ordinary Möbius-ladder matching complexes* and *Initial integral homotopy types of circular-ladder matching complexes* classify, respectively, only the Möbius orders 12, 14 and 16 and the prism orders three through eight. In particular, both families have mixed-dimensional sphere wedges at the preceding eight-rung boundary, whereas the two nine-rung cases here have homology in a single degree. General outerplanar matching-complex classifications do not apply because both nine-rung cubic graphs have minimum vertex degree three; a nonempty simple outerplanar graph has a vertex of degree at most two. A coincidence of Betti ranks in another graph would not imply these exact homotopy types.

## Limitations
Only the ordinary matching complexes of \(M_{18}\) and \(C_9\square K_2\) are classified. No formula or periodicity for greater widths, no equivariant homology representation, and no comparison of inclusion maps from perfect-matching complexes is asserted. The proof is an exhaustive finite certificate, not a proof about all ladders. Bibliographic searches and inspections cannot eliminate the risk of unindexed equivalent work. The computation has been checked within the same research process; independent mathematical audit has not yet been performed.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public version 2026-08-31; §§1, 3, 5–6 and Problem 26. https://arxiv.org/abs/2608.30601
2. *Three integral homotopy types of ordinary Möbius-ladder matching complexes*, published 2026-10-25. https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-three-integral-homotopy-types-of-ordinary-m-bius-ladder-matching--2836154b88c9/RESULT.md
3. *Initial integral homotopy types of circular-ladder matching complexes*, published 2026-10-25. https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-initial-integral-homotopy-types-of-circular-ladder-matching-comp--94cb26be0034/RESULT.md
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145.
5. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (2024). https://arxiv.org/abs/2411.04601
