# Strict negative edge correlations for the equal-fugacity arboreal gas on \(K_{3,n}\)

## Finding

**Theorem.** For every integer \(n\ge 5\) and every real \(\beta>0\), sample an acyclic spanning subgraph \(F\) of the complete bipartite graph \(K_{3,n}\) with probability proportional to \(\beta^{|E(F)|}\). For every two *distinct* edges \(e,f\),
\[
\operatorname{Cov}_{\beta}(\mathbf1_{\{e\in F\}},\mathbf1_{\{f\in F\}})<0.
\]
The inequality is strict whether the edges share one of the three left vertices, share one of the \(n\) right vertices, or are vertex-disjoint. The statement holds at every positive common fugacity, not only at the uniform-forest point \(\beta=1\) or in a large-fugacity regime.

## Assumptions and scope

The graph is simple and has one part of size exactly three and a second part of size \(n\ge5\). Every edge has *the same* strictly positive fugacity \(\beta\). A spanning forest includes all graph vertices but need not connect them; its edge set is acyclic. No claim is made for independently varying edge fugacities, for arbitrary bipartite part sizes, or for higher-order negative association.

Write \(b=\beta\), \(h=n-1\), \(A=1+3b\), and \(B=3b^2+b^3\). Define
\[
\begin{aligned}
Z_*&=A^2+nBA+3n(n-1)b^4,\\
E_*&=b\bigl(A^2+(n-1)BA+3(n-1)(n-2)b^4\bigr)\\
&\quad +(2b^2+b^3)A^2+4(n-1)b^4A,\\
Q_0&=b^2\bigl(A^2+(n-2)BA+3(n-2)(n-3)b^4\bigr)\\
&\quad+2b\bigl((2b^2+b^3)A^2+4(n-2)b^4 A\bigr),\\
Q_R&=A^2\bigl(b^2(1+b)A+2(n-1)b^4\bigr),\\
Q_L&=Q_0+2b^4A^2,\qquad Q_D=Q_0+3b^4A^2.
\end{aligned}
\]
Here the subscripts \(R,L,D\) respectively denote an edge pair sharing a right endpoint, sharing a left endpoint, or having disjoint endpoints.

## Proof

**Forest classification.** For each vertex in the right part, record the subset of the three left vertices incident to chosen edges. There is one degree-zero choice and three degree-one choices, with total weight \(A\); there are three degree-two choices and one degree-three choice, with total weight \(B\). A selected edge configuration is a forest if and only if one of the following holds: (i) all right vertices have degree at most one; (ii) exactly one right vertex has degree at least two; or (iii) exactly two right vertices each have degree two, and their two neighbor-pairs are different. Indeed, one degree-three right vertex and another high-degree right vertex create a cycle; two degree-two right vertices with the same neighbor-pair create a four-cycle; and three degree-two right vertices either repeat a pair or use all three pairs and create a six-cycle. Conversely the listed cases contain no cycle because any cycle must use at least two right vertices of degree at least two. Thus the exact partition function is
\[
Z_n=A^n+nBA^{n-1}+3n(n-1)b^4A^{n-2}=A^{n-2}Z_*.
\]

**One- and two-edge incidence counts.** By edge transitivity, the one-edge inclusion probability is the same for each edge. Fix \(e\). If its right endpoint has degree one, its contribution is \(b\) times the forest sum on the other \(n-1\) right vertices. If it has degree at least two, the possibilities have respective weights \(2b^2+b^3\); one additional right vertex may have degree two with a different neighbor-pair, giving four compatible ordered choices of marked right-neighbor patterns. The weighted incidence sum is \(A^{n-3}E_*\); hence
\[
\Pr(e\in F)=\frac{E_*}{AZ_*}.
\]

For two specified edges sharing a right endpoint, that endpoint has degree two or three, yielding weighted two-edge incidence sum \(A^{n-2}[b^2(1+b)A+2(n-1)b^4]\). For two specified edges with different right endpoints, split into cases where both right vertices have degree one, exactly one has degree at least two, or both have degree two. The first two cases have combined weighted count \(A^{n-4}Q_0\); the last has \(2A^{n-2}b^4\) compatible neighbor-pair choices for edges sharing a left endpoint and \(3A^{n-2}b^4\) choices for disjoint edges. Consequently, for each orbit \(s\in\{R,L,D\}\),
\[
\Pr(e,f\in F)=\frac{Q_s}{A^2Z_*}.
\]
Every edge pair belongs to precisely one of these three orbits.

**A positive-polynomial certificate.** Set \(\Delta_s=E_*^2-Q_sZ_*\). Exact expansion in \(b\) and \(h=n-1\) gives
\[
\Delta_R=b^4hP_R(b,h),\quad
\Delta_L=2b^4P_L(b,h),\quad
\Delta_D=b^4P_D(b,h).
\]
The following table lists every coefficient \([b^k]P_s(b,h)\); entries with omitted powers of \(h\) are zero.

| \(k\) | \([b^k]P_R\) | \([b^k]P_L\) | \([b^k]P_D\) |
|---|---|---|---|
| 0 | \(1\) | \(1\) | \(1\) |
| 1 | \(12\) | \(12\) | \(12\) |
| 2 | \(52+6h\) | \(54+5h\) | \(51+7h\) |
| 3 | \(98+46h\) | \(118+36h\) | \(100+44h\) |
| 4 | \(75+106h+12h^2\) | \(135+90h+5h^2\) | \(99+87h+7h^2\) |
| 5 | \(18+66h+48h^2\) | \(78+96h+18h^2\) | \(48+66h+18h^2\) |
| 6 | \(9h+18h^2+9h^3\) | \(18+36h+18h^2\) | \(9+18h+9h^2\) |

All three polynomials are strictly positive for \(b>0\) and \(h=n-1\ge4\), since every displayed coefficient is positive. Therefore
\[
\operatorname{Cov}(\mathbf1_e,\mathbf1_f)
=\frac{Q_sZ_*-E_*^2}{A^2Z_*^2}
=-\frac{\Delta_s}{A^2Z_*^2}<0,
\]
as required. Both the forest classification and the polynomial identities are exact for every allowed parameter; no limiting or numerical approximation is involved in the proof.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The self-contained checker performs polynomial arithmetic with integer coefficient dictionaries in the formal variables \(b,h\), verifies all three identities \(\Delta_s=b^4\cdot(\ldots)\) coefficient by coefficient, and verifies the listed positive polynomial coefficients. It separately enumerates every acyclic edge subset of \(K_{3,n}\) for \(n=2,3,4,5\) at \(b\in\{1/2,1,2\}\), verifying partition functions and the three joint edge probabilities using exact rational arithmetic. The enumeration corroborates but does not replace the general algebraic proof.

## Relationship to prior work

Huang's November 2, 2023 work formulates arboreal-gas negative correlation and proves results for specified graphs or sufficiently large fugacities; it does not give the present complete-bipartite, all-fugacity theorem. Wagner's 2006 Rayleigh analysis includes the finite graphic case \(K_{3,4}\) (with stronger individually varying edge weights), but this does not imply the all-size family \(K_{3,n}\) for \(n\ge5\). Cao and Fu's October 27, 2026 result gives strict negative correlation on *every* \(K_{m,n}\) for the **uniform** forest measure \(b=1\); the present result gives a continuous positive-fugacity theorem along the three-vertex-side family, by an independent constructive polynomial certificate. Çiçeksiz and Ravichandran's September 30, 2026 results cover high-fugacity cases under additional hypotheses and other graph families; they do not state this all-positive-fugacity specialization.

## Limitations

The proof relies on having exactly three vertices on one side, so a forest has at most two right vertices of degree at least two. The coefficient certificate does not cover \(K_{4,n}\) or general irregular edge weights. Strictness concerns distinct edge *pairs* only. A previous derivation hidden in broader Rayleigh or graph-polynomial literature cannot be excluded without an independent historical-priority audit.

## References

1. Xiangyu Huang, *On Negative Correlation of Arboreal Gas on Some Graphs*, arXiv:2311.00965v1, November 2, 2023. https://arxiv.org/abs/2311.00965
2. Ying Cao and Houshan Fu, *Negative edge correlation in complete bipartite graphs*, arXiv:2610.36749v1, October 27, 2026. https://arxiv.org/abs/2610.36749
3. David G. Wagner, *Negatively Correlated Random Variables and Mason's Conjecture for Independent Sets in Matroids*, arXiv:math/0602648, 2006. https://arxiv.org/abs/math/0602648
4. Recep Altar Çiçeksiz and Mohan Ravichandran, *Negative Correlations for Forests and the \(q<1\) Random Cluster Model*, arXiv:2610.00549, September 30, 2026. https://arxiv.org/abs/2610.00549
