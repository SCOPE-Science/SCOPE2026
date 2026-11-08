# Maximal induced three-colorable rook subgraphs: an exact three-level defect census

## Finding

For integers \(3\le m\le n\), let \(R_{m,n}=K_m\square K_n\), and let \(\mathcal M^{(3)}_{m,n}(z)\) count inclusion-maximal vertex subsets inducing three-colorable subgraphs, by cardinality. All cells of the underlying rectangular board are distinctly labeled. Let \(e_j(x)\) denote the elementary symmetric polynomial in variables \(x_1,\ldots,x_m\), with \(e_0=1\). Define the integer coefficient extractions
\[
Q_{m,n}=[x_1^3\cdots x_m^3](e_0+e_1+e_2+e_3)^n.
\]
For \(r\ge3\), write
\[
A_r=[x_1^3\cdots x_r^3]e_3(x_1,\ldots,x_r)^r,
\qquad H_r=[x_1^2x_2^3\cdots x_r^3]e_2(x_1,\ldots,x_r)e_3(x_1,\ldots,x_r)^{r-1}.
\]
Set \(A_r=H_r=0\) for \(r<3\). Then the **exact maximal-cardinality polynomial** is
\[
\boxed{\mathcal M^{(3)}_{m,n}(z)=Q_{m,n}z^{3m}
+\mathbf{1}_{\{n=m+1\}}m\binom{m+1}{2}A_{m-1}z^{3m-1}\quad(m<n)}
\]
and
\[
\boxed{\mathcal M^{(3)}_{n,n}(z)=
\left(n^2A_{n-1}+\bigl(\binom{n}{2}\bigr)^2 A_{n-2}\right)z^{3n-2}
+n^2(n-1)^2H_{n-1}z^{3n-1}+A_nz^{3n}.}
\]

The exact positive cardinality supports are \(\{9\}\) for \(m=n=3\), \(\{3n-2,3n-1,3n\}\) for \(m=n\ge4\), \(\{3m-1,3m\}\) for \(n=m+1\) and \(m\ge4\), and \(\{3m\}\) for all other \(3\le m\le n\). For example,
\[
\mathcal M^{(3)}_{4,4}(z)=16z^{10}+144z^{11}+24z^{12},\qquad
\mathcal M^{(3)}_{4,5}(z)=40z^{11}+4320z^{12},
\]
while \(\mathcal M^{(3)}_{5,5}(z)=700z^{13}+10800z^{14}+2040z^{15}\).

## Assumptions and scope

The rook graph has one vertex for each cell \((i,j)\) of an \(m\)-by-\(n\) board and joins two cells when they share a row or column. The term *inclusion-maximal* means that no additional board cell can be added while preserving three-colorability. This is not the same as a maximum-cardinality subgraph or a maximal proper coloring. The result holds for all integers \(3\le m\le n\). The coefficients count actual labeled cell sets, not graph isomorphism classes, equivalent colorings, or row-column symmetry orbits.

## Proof

**Step 1: a degree formulation.** Identify the selected board cells with the edges of a selected bipartite graph \(H\subseteq K_{m,n}\). Its line graph is the selected induced rook subgraph. By the bipartite line-coloring theorem, the chromatic number of this line graph is the maximum degree of \(H\). Consequently it is three-colorable precisely when every row and column contains at most three selected cells. It is inclusion-maximal precisely when every unselected cell lies in a saturated row or saturated column, where *saturated* means degree three. Equivalently, the Cartesian block formed by all low rows and all low columns (those with degrees at most two) is completely selected.

**Step 2: deficiency classification.** Let \(I\) be the set of low rows and \(J\) the set of low columns, of cardinalities \(p,q\). If \(p=0\), all rows have degree three, and hence the selected size is \(3m\). For \(n\ge m\), the case \(p>0,q=0\) is impossible: degree three in all \(n\) columns would require more than \(3m\) edges, or, for equal sides, force all rows saturated. When \(p,q>0\), the complete low block gives \(p,q\in\{1,2\}\), since no low row or column can have more than two selected cells.

Put \(\alpha=3m-|E(H)|\) and \(\beta=3n-|E(H)|\). Then \(\beta-\alpha=3(n-m)\). For \((p,q)=(1,1)\), the possible row and column deficits independently lie in \(\{1,2\}\); their difference has magnitude at most one, so this case forces \(n=m\) and equal deficits. For \((p,q)=(1,2)\), the low row necessarily has degree two and the two low columns degree one, giving \((\alpha,\beta)=(1,4)\), hence \(n=m+1\). For \((p,q)=(2,1)\), one gets \((4,1)\), impossible because \(n\ge m\). For \((p,q)=(2,2)\), both deficits equal two, so \(n=m\). No other cases exist.

**Step 3: label each class without overcounting.** When all rows are saturated, each column independently chooses at most three of the \(m\) rows; extracting the exponent three at every row gives exactly \(Q_{m,n}\) sets. For square boards the degree sum forces every column saturated too, so \(Q_{n,n}=A_n\).

In the non-square exceptional case \(n=m+1\), choose the unique low row (\(m\) choices) and the two low columns (\(\binom{m+1}{2}\) choices). Their two intersections are selected and all other cells in those columns are absent. The remaining \((m-1)\)-square block is a three-regular binary matrix: \(A_{m-1}\) choices. The size is \(3m-1\).

For square boards with one low row and one low column, the two deficits must be equal. If both equal two, their shared cell is the only selected edge meeting either low vertex. Choose that row and column (\(n^2\) choices); the remaining \((n-1)\)-square block is three-regular, for \(n^2 A_{n-1}\) sets of size \(3n-2\). If both deficits equal one, each low vertex has degree two: the common cell, plus one cell at a high vertex on the opposite side. Choose the low row and column (\(n^2\) choices), then those two distinct high neighbors (\((n-1)^2\) choices). The remaining \((n-1)\)-square block has one specified row and one specified column of degree two, and all other degrees three; its count is exactly \(H_{n-1}\). This gives \(n^2(n-1)^2H_{n-1}\) sets of size \(3n-1\). Finally, the two-low-rows/two-low-columns case has a completely selected \(2\)-by-\(2\) corner and a disjoint three-regular \((n-2)\)-square block; its count is \(\bigl(\binom{n}{2}\bigr)^2 A_{n-2}\) at size \(3n-2\). The sizes and low-index sets distinguish all counted cases, proving the formulas.

**Step 4: exact support and boundaries.** A three-regular square binary matrix exists at every order at least three (take three disjoint cyclic permutation matrices), and \(A_3=1\), \(A_2=0\). The margin pattern defining \(H_r\) is realized for every \(r\ge3\) by deleting one entry from any three-regular square binary matrix. Every \(Q_{m,n}\) is positive: use a three-regular \(m\)-square matrix in any \(m\) of the \(n\) columns and leave the remainder empty. The asserted support follows immediately, with the special \(3\)-square boundary included. All constructions satisfy the extension obstruction from Step 1, so they are genuinely inclusion-maximal.

## Verification

The accompanying standalone Python program `verify_rook_3colour.py` uses only the standard library. It independently enumerates all candidate cell subsets and tests the row and column degree and extension conditions on six board sizes: \((m,n)=(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)\). This examines \(1{,}413{,}632\) subsets altogether. A separate backtracking vertex-coloring implementation directly checks the equivalence of three-colorability and the degree rule and checks maximality on every subset of the \(3\)-by-\(3\) and \(3\)-by-\(4\) boards. Independently, labeled margin recurrences reproduce \(A_r\) through \(r=7\), \(H_r\) through \(r=6\), and the displayed concrete polynomial examples. The execution printed `VERIFY_OK graph_colorings=3x3,3x4 exhaustive_degree_enumeration_cases=6 total_candidate_subsets=1413632 exact_margin_counts=PASS`. These finite checks support but do not replace the unrestricted proof above.

## Relationship to prior work

Goddard, Kuenzel, and Melville introduced the well-bicovered framework in their 2019 preprint. In their later paper *Well-Hued Graphs* (2022), Section 3.5, Lemma 6 establishes that \(K_m\square K_n\) is well-\(k\)-partite exactly when \(k\ge m\) or \(k\le n-m+1\), for \(n\ge m\). That result already gives the qualitative three-colorability boundary; no claim of novelty is made for it or for the scalar maximum \(3m\). The present result is a **labeled inclusion-maximal cardinality census**, including precise exceptional coefficients, and is not implied by knowing only whether the maximal cardinalities are all equal. In particular, Lemma 6 does not distinguish the two contributing classes at size \(3n-2\) or enumerate their multiplicities.

The labeled three-regular binary-matrix count \(A_r\) is itself classical: it is OEIS A001501 and occurs in earlier enumerative literature. The contribution is the maximality classification, the appropriate mixed-margin count \(H_r\), and their exact assembly into the rook-graph distribution. The result is equivalent, under line graphs, to enumerating inclusion-maximal simple subgraphs of \(K_{m,n}\) with maximum degree at most three. Related general enumeration problems need not imply the present explicit formulas.

## Limitations

The formulas concern only three-colorability and integers \(3\le m\le n\); they are not a formula for arbitrary color bounds, arbitrary bipartite hosts, or numbers of proper three-colorings. The coefficient extractions are finite exact descriptions, not elementary product expressions. Existing work fixes the qualitative support boundary and the regular-matrix sequence, so originality is confined to the complete labeled maximal-subgraph census; possible unindexed equivalent formulas remain a publication-priority risk. No independent mathematical audit has been carried out.

## References

1. W. Goddard, K. Kuenzel, E. Melville, *Graphs in which all maximal bipartite subgraphs have the same order*, arXiv:1909.07503 (first posted 2019-09-16), https://arxiv.org/abs/1909.07503 .
2. W. Goddard, K. Kuenzel, E. Melville, *Well-Hued Graphs*, Discrete Applied Mathematics 320 (2022), 370–380, DOI:10.1016/j.dam.2022.06.010; lawful author full text https://people.computing.clemson.edu/~goddard/papers/wellHued.pdf , especially Section 3.5 and Lemma 6.
3. OEIS A001501, *Number of n by n 0-1 matrices with all row and column sums equal to three*, https://oeis.org/A001501 .
4. B.-Y. Wang and F. Zhang, *On the precise number of (0,1)-matrices in A(R,S)*, Discrete Mathematics 187 (1998), 211–220, DOI:10.1016/S0012-365X(97)00197-0 (margin-enumeration background, as indexed by OEIS A001501).
