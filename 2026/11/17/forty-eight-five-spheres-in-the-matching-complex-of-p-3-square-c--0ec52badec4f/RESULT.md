# Forty-eight five-spheres in the matching complex of \(P_3\square C_6\)

## Finding
Let \(G=P_3\square C_6\) be the simple Cartesian product of the three-vertex path and six-cycle, and \(\mathcal M(G)\) its ordinary matching complex. Then
\[
|\mathcal M(G)|\simeq\bigvee^{48}S^5.
\]
In particular, \(\widetilde H_5(\mathcal M(G);\mathbb Z)\cong\mathbb Z^{48}\) and every other reduced integral homology group is zero. The result is a complete integral homotopy classification for this particular periodic three-row grid, not a general formula for all circumferences.

## Assumptions and scope
The graph vertices are \((r,c)\) with \(r\in\{0,1,2\}\) and \(c\in\mathbb Z/6\mathbb Z\). Its 30 undirected edges are the 18 horizontal edges \(\{(r,c),(r,c+1)\}\) (columns modulo six) and the 12 vertical edges \(\{(r,c),(r+1,c)\}\) for \(r\in\{0,1\}\). There are no diagonals, no wrap-around edges in the row direction, and no repeated edges. A simplex of \(\mathcal M(G)\) is a set of graph edges having pairwise disjoint endpoints. The empty face is included only in the augmented bookkeeping and is not a CW cell of the geometric realization.

## Proof
**Exact face census.** Sort graph vertices lexicographically. Sort each edge's two endpoints, then sort all 30 edges lexicographically to get indices \(0,\ldots,29\). Enumerate faces recursively by deciding, for each graph edge, whether to exclude or include it, with inclusion allowed precisely when its endpoints are unused. This enumerates every face once by induction on the 30 edge decisions. The numbers of nonempty faces by dimensions \(0,\ldots,8\) are
\[
(30,363,2290,8139,16446,18141,9870,2148,108),
\]
for a total of 57,535.

**Acyclic matching.** Process graph-edge indices in the order

`[25,12,24,20,6,0,28,26,27,9,5,17,19,7,4,8,2,10,3,11,15,22,21,16,23,1,29,13,18,14]`.

At each stage pair every still-available face \(\sigma\) not containing that edge with the still-available face \(\sigma\cup\{e\}\), and remove both from later stages. First carry this out on the augmented face set. Delete the augmented pair containing the empty face, making its former vertex a critical ordinary cell. The resulting nonempty face-poset matching has 28,733 disjoint pairs and exactly one critical 0-face, 58 critical 5-faces, and ten critical 6-faces. To establish acyclicity, reverse the orientation of every matched Hasse edge, while orienting every other cover from upper to lower face. A complete topological sort visits all 57,535 vertices and processes all 318,474 nonempty Hasse covers. Thus there is no directed closed gradient path. Forman's theorem provides a homotopy-equivalent CW complex with precisely these critical cells.

**Integral attaching degrees.** Orient each face by increasing graph-edge index. For a five-face \(s\) paired upward with a six-face \(t\), write \(\epsilon=[\partial t:s]\in\{-1,+1\}\). Its projection into critical degree-five chains satisfies
\[
R(s)=-\epsilon^{-1}\sum_{u\prec t,\,u\ne s}[\partial t:u]R(u).
\]
For a critical five-face \(u\), set \(R(u)=u\); for a five-face paired downward, set \(R(u)=0\). The acyclic matching makes this recursion well founded. Applying \(R\) to the signed simplicial boundaries of the ten critical six-faces produces the exact integral \(58\times10\) Morse boundary matrix in `proof/morse_boundary_58x10.csv`. The independent source file `proof/verify_cylinder.py` reconstructs this matrix and checks its 580 entries against the embedded CSV. Its Smith normal form has ten nonzero invariant factors, all equal to one. In particular, the integer boundary is a split injection with primitive image of rank ten.

The CW complex has one 0-cell, no cells in dimensions 1 through 4, 58 cells in dimension five and ten in dimension six. Its 5-skeleton is \(\bigvee^{58}S^5\). By Hurewicz, its fifth homotopy group is \(\mathbb Z^{58}\), with the fifth homology generators as a basis. Hence the signed integer Morse boundary records the full attaching classes of all ten six-cells, not just their induced homology maps. An integer Smith basis change cancels ten 5/6-cell pairs, leaving a wedge of exactly 48 five-spheres. This proves the asserted integral homotopy equivalence.

## Verification
Run from the extracted package root:

```text
python3 proof/verify_cylinder.py proof/morse_boundary_58x10.csv
```

The self-contained graph/face enumeration, complete directed Hasse acyclicity test, all signed Morse boundary entries, and exact integer Smith computation are performed at execution. The script reports `CYLINDER_3X6_MATCHING_EXACT_PASS`. It independently computes the ranks of the **original simplicial boundary matrices over the field of two elements**, obtaining reduced fifth Betti number 48 and all other positive-degree Betti numbers zero. These modular calculations corroborate, but do not substitute for, the integral Smith proof. The original simplicial Euler characteristic is \(-47\), consistent with 48 five-spheres. Machine-readable output appears in `proof/verification_output.json` and the exact 58-by-10 integer matrix is included.

## Relationship to prior work
Chauhan, Sharma and Shukla (2026, first public September 23, 2026) study \(\mathcal M(P_3\square P_n)\), with an **open rectangular** horizontal boundary, and establish connectivity and homological vanishing; they do not treat the periodic \(C_6\) factor in their 23-page preprint. The earlier rectangular-width classifications through eight columns likewise differ in their underlying graphs and are not homotopy classifications of this cylinder. A directly relevant calculation for the pentagonal three-row cylinder \(P_3\square C_5\) gives \(\bigvee^{24}S^4\vee\bigvee^3S^5\), so it does not imply the six-column result. The hexagonal prism \(P_2\square C_6\) is only two rows and has different topology. The 18-vertex three-dimensional grid \(P_2\square P_3\square P_3\) happens to have the same sphere count and dimension, but its graph has 33 rather than 30 edges and is not isomorphic to \(G\); equality of its homotopy answer is not prior coverage of this graph. The proof does not invoke an unproved cylindrical recursion. Relevant published-record searches and inspection of the closest primary full text uncovered no equivalent six-column statement; this is not a guarantee against unindexed prior work.

## Limitations
Only the graph with three path rows and six cyclic columns is classified. No homotopy statement is made for other circumferences, the full dihedral representation, or any geometric quotient. The result requires reproducible exact finite computation and standard discrete Morse/CW-attachment arguments. Independent mathematical validation has not been performed, and unindexed or unavailable literature could contain an equivalent calculation.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366v1 (first public September 23, 2026), https://arxiv.org/pdf/2609.27366v1.
2. *Mixed-dimensional matching-complex homotopy on the pentagonal three-row cylinder \(P_3\square C_5\)* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mixed-dimensional-matching-complex-homotopy-on-the-pentagonal-th--da8762498878.
3. *Finite integral wedge classifications for matching complexes of \(3\times n\) grids through width eight* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-finite-integral-wedge-classifications-for-matching-complexes-of--2352ab105c17.
4. *Hexagonal-prism matching complex: twelve three-spheres and a full-symmetry rational class* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-hexagonal-prism-matching-complex-twelve-three-spheres-and-a-full--440f9df687e8.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
