# The horizontal-edge defect law for circular-ladder perfect-matching complexes

## Finding
For each integer \(n\ge3\), let \(G_n\) be the prism graph \(C_n\square K_2\) after deletion of **one horizontal edge in exactly one of its two cycles**. Let \(\mathcal P(G_n)\) be the abstract simplicial complex whose facets are the perfect matchings of \(G_n\); its vertices are graph edges appearing in at least one perfect matching. There is an integral homotopy classification
\[
|\mathcal P(G_n)|\simeq
\begin{cases}
*,&n\text{ odd},\\
S^{n/2-1}\vee S^{n/3},&n\equiv0\pmod 6,\\
S^{n/2-1},&n\equiv2\pmod 6,\\
S^{n/2-1}\vee S^{(n-1)/3},&n\equiv4\pmod 6.
\end{cases}
\]
Here the last three cases apply to even \(n\ge4\); in the third case \(n\ge8\). The wedge is a *based* wedge and the equivalence is an ordinary integral homotopy equivalence. In particular \(\mathcal P(G_4)\simeq S^1\vee S^1\), \(\mathcal P(G_6)\simeq S^2\vee S^2\), \(\mathcal P(G_8)\simeq S^3\), and \(\mathcal P(G_{10})\simeq S^4\vee S^3\). Every reduced integral homology group is free.

## Assumptions and scope
Index the two rows by \(0,1\) and the columns by \(\mathbb Z/n\mathbb Z\). Write \(T_i=\{(0,i),(0,i+1)\}\), \(B_i=\{(1,i),(1,i+1)\}\) for horizontal edges, and \(R_i=\{(0,i),(1,i)\}\) for rungs. Indices are cyclic. Delete \(T_0\) only. The entire family of one-horizontal-edge deletions is isomorphic to this choice by cyclic and layer symmetries. In contrast, deleting a *rung* is a different edge orbit and is **not** part of the theorem.

Put \(L_n=\mathcal P(P_n\square K_2)\), the open two-row ladder perfect-matching complex obtained by deleting both \(T_0\) and \(B_0\). As complexes, \(L_n\subseteq\mathcal P(G_n)\). Let \(\operatorname{Ind}(P_m)\) denote the independence complex of a path on \(m\) vertices. The structural statement behind the formula is
\[
\mathcal P(G_{2k})\simeq L_{2k}\vee\Sigma\operatorname{Ind}(P_{2k-1}),\qquad k\ge2,
\]
with \(L_{2k}\simeq S^{k-1}\), while \(\mathcal P(G_n)=L_n\) **as simplicial complexes** for odd \(n\).

## Proof
**1. Perfect-matching dichotomy.** Every perfect matching of the prism with at least one rung is aligned: it contains \(T_i\) exactly when it contains \(B_i\). Indeed, cut the two cyclic rows at a chosen rung. The vertices in each interval between consecutive rungs have matching partners only along their own row, forcing their edges alternately, in the same positions in both rows. A perfect matching with no rungs consists of independent horizontal perfect matchings of the two cycle rows and therefore requires even \(n\).

Since \(T_0\) is absent, an aligned matching cannot contain \(B_0\). Consequently every matching containing a rung is already a perfect matching of the open ladder. If \(n\) is odd there are no rungless matchings, so \(\mathcal P(G_n)=L_n\). If \(n\) is even, the top cycle has a unique allowed horizontal perfect matching: \(T_1,T_3,\ldots,T_{n-1}\). The bottom row permits the two alternating perfect matchings. One is aligned and belongs to \(L_n\); the other gives the unique extra maximal face
\[
F=\{T_1,T_3,\ldots,T_{n-1},\ B_0,B_2,\ldots,B_{n-2}\}.
\]
Thus \(\mathcal P(G_n)=L_n\cup 2^F\), where \(2^F\) denotes the full simplex on this \(n\)-element set.

**2. Exact intersection.** No face of \(L_n\) contains \(B_0\). Order the remaining \(n-1\) vertices of \(F\) as \(T_1,B_2,T_3,B_4,\ldots,T_{n-1}\). A partial matching supported there extends to an open-ladder perfect matching if and only if it contains no consecutive two members in this ordering. For necessity, each horizontal edge of an open-ladder perfect matching forces its parallel partner, so two neighboring choices would demand overlapping two-column domino blocks. For sufficiency, choose the parallel partners for all selected edges; their two-column blocks are disjoint, and cover the remaining columns by vertical rungs. Therefore
\[
L_n\cap 2^F\cong\operatorname{Ind}(P_{n-1}).
\]
The isomorphism is simplicial, not merely homological.

**3. The open-ladder recurrence.** On the straight ladder with \(n\) columns, each perfect matching uses at its first column either the first rung or both parallel first-column horizontal edges. The two facet-generated subcomplexes \(A_n\) and \(B_n\) are cones, respectively with apex that rung and one of the horizontal edges. Their intersection is precisely \(L_{n-2}\), supported on the last \(n-2\) columns: edges touching either of the first two columns cannot belong to both. Hence \(L_n=A_n\cup B_n\simeq\Sigma L_{n-2}\) for \(n\ge3\). The initial complexes are \(L_1\simeq *\) and \(L_2\cong S^0\). Inductively \(L_{2k}\simeq S^{k-1}\) and \(L_{2k+1}\simeq *\).

**4. Null attaching map.** For even \(n=2k\ge4\), let \(I=L_n\cap 2^F\). The standard path independence-complex recurrence \(\operatorname{Ind}(P_m)\simeq\Sigma\operatorname{Ind}(P_{m-3})\) for \(m\ge4\), with \(P_1\) contractible and \(\operatorname{Ind}(P_2)\simeq\operatorname{Ind}(P_3)\simeq S^0\), shows \(I\) is contractible or a sphere whose dimension is **strictly less than** \(k-1\). Since \(L_n\simeq S^{k-1}\) is \((k-2)\)-connected, the inclusion \(I\hookrightarrow L_n\) is nullhomotopic. At \(n=4\), this uses path-connectedness of \(L_4\), since \(I\simeq S^0\). Attaching the simplex \(2^F\), a cone on \(I\), along this null map gives
\[
|\mathcal P(G_n)|\simeq |L_n|\vee\Sigma|I|.
\]
Finally, substituting the three-residue formula for the path independence complex produces the displayed four cases. This is a proof over the integers and establishes the full homotopy types, not merely field Betti numbers.

## Verification
The accompanying Python program `verify_horizontal_defect.py` enumerates all perfect matchings from scratch by recursively covering the first unmatched vertex. For \(3\le n\le10\), it independently constructs complete simplicial face sets, checks exact decomposition \(\mathcal P(G_n)=L_n\cup 2^F\), checks the intersection against the independent subsets of an explicit path, and performs direct reduced simplicial boundary elimination over \(\mathbb F_2\). For \(11\le n\le14\), it additionally verifies the complete perfect-matching partition without building exponentially large boundary matrices. All tests pass; the full eight-boundary-case calculation contains \(67{,}639\) nonempty-or-empty faces summed over those cases. These finite calculations are corroboration, **not** the proof of the all-\(n\) result. Execute `python verify_horizontal_defect.py` from the extracted package directory; its exact recorded output is `verification_output.txt`.

## Relationship to prior work
Agarwal and Basak's September 14, 2026 circular-ladder extension (arXiv:2608.30601v2, Theorem 25) classifies \(\mathcal P(C_n\square K_2)\) for the **intact** prism and establishes contractibility for odd \(n\), with different even-\(n\) sphere bouquets. It does not treat one-sided horizontal-edge deletion. Its first version on August 31, 2026 studied Möbius ladders only; the circular-ladder extension first became public in version 2 on September 14, 2026.

Chandrakar and Singh (arXiv:2407.05809v2, Theorem 3.3) classify the **open** two-row ladder and supply the known type \(L_{2k}\simeq S^{k-1}\), \(L_{2k+1}\simeq *\). Their theorem does not include the extra rungless perfect-matching simplex or its path-independence attaching complex, essential for the even-\(n\) two-tier formula. The independence-complex recurrence for paths is classical (Kozlov). The present classification follows from an exact new one-sided-defect decomposition; it should not be confused with deletion of a rung, with ordinary (rather than extendible) matching complexes, or with edge-deleted rectangular grids.

## Limitations
Only a single horizontal edge is removed, from one row of the circular ladder, with \(n\ge3\). Multiple horizontal defects, vertical-rung deletions, Möbius boundary identifications and symmetry-equivariant homotopy types are not classified here. Exact finite verification through width ten does not independently verify the infinite-range argument. Originality comparisons included the strongest accessible full texts, but equivalent unindexed treatments of one-sided seam defects cannot be ruled out without independent literature audit.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (2026-09-14), especially Section 5.2 and Theorem 25. https://arxiv.org/abs/2608.30601
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v2 (2025-04-07; initial preprint 2024), Theorem 3.3. https://arxiv.org/abs/2407.05809
3. D. N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory Series A 88 (1999), 112–122 (path independence-complex periodicity).
