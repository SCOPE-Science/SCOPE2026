# The complete reflected mixed-volume profile of barycentrically capped tetrahedra

## Finding

Let \(T\subset\mathbb R^3\) be any nondegenerate tetrahedron, with barycentric affine coordinates \(\lambda_1,\ldots,\lambda_4\), normalized by \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\) on \(T\). For \(t>1/4\), define the equal-cap body
\[
K_t=\{x\in T:\lambda_i(x)\le t\text{ for all }i\}.
\]
Write \(V_T=\operatorname{vol}_3(T)\), \(V_t=\operatorname{vol}_3(K_t)\), and \(M_t=V_3(K_t,K_t,-K_t)\), with the conventional Minkowski mixed-volume normalization. Define the two facet-area multipliers for \(1/3\le t\le1\):
\[
(L(t),U(t))=\begin{cases}
\bigl((3t-1)^2,(1-t)^2-3(1-2t)^2\bigr),&1/3\le t\le1/2,\\
\bigl(1-3(1-t)^2,(1-t)^2\bigr),&1/2\le t\le1.
\end{cases}
\]
Then the **complete volume and reflected mixed-volume profiles**, independent of the shape of \(T\), are
\[
\frac{V_t}{V_T}=\begin{cases}
(4t-1)^3,&1/4<t\le1/3,\\
L(t)+(4t-1)U(t),&1/3\le t\le1,\\
1,&t\ge1,
\end{cases}
\qquad
\frac{M_t}{V_T}=\begin{cases}
3(4t-1)^3,&1/4<t\le1/3,\\
(4t-1)L(t)+U(t),&1/3\le t\le1,\\
3,&t\ge1.
\end{cases}
\]
The branches agree at their shared endpoints. With \(\rho(t)=M_t/V_t\), one has \(\rho=3\) on \((1/4,1/3]\) and \([1,\infty)\), strict decrease on \((1/3,1/2)\), strict increase on \((1/2,1)\), and a **unique global minimum** \(\rho(1/2)=1\). Moreover
\[
\frac{\operatorname{vol}_3(K_t-K_t)}{\operatorname{vol}_3(K_t)}=2+6\rho(t)
\]
travels exactly from the simplex extremal value \(20\) to the centrally symmetric value \(8\) and back. At the octahedral transition,
\[
\rho(t)=\begin{cases}
1+32(t-1/2)^2-32(t-1/2)^3+O((t-1/2)^4),&t\uparrow1/2,\\
1+32(t-1/2)^2-224(t-1/2)^3+O((t-1/2)^4),&t\downarrow1/2.
\end{cases}
\]
Thus \(\rho\) is twice continuously differentiable, but not three times differentiable, at \(t=1/2\); the jump in its one-sided third derivatives (right minus left) is \(-1152\). For \(t<1/4\), the caps have empty intersection; at \(t=1/4\) they intersect in one point, where the normalized mixed-volume ratio is undefined.

## Assumptions and scope

The tetrahedron is arbitrary, not necessarily regular: the construction and volume ratios are affine invariant. All bodies for \(t>1/4\) are three-dimensional. Throughout, \(V_3(A,B,C)\) denotes the symmetric mixed volume determined by the coefficient identity
\[
\operatorname{vol}_3(sA+uB)=s^3\operatorname{vol}_3(A)+3s^2u V_3(A,A,B)+3su^2V_3(A,B,B)+u^3\operatorname{vol}_3(B)
\]
for nonnegative \(s,u\). Reflections use any fixed origin; mixed volumes are translation invariant.

## Proof

**1. First simplex chamber.** If \(1/4<t\le1/3\), the vertices of \(K_t\) in barycentric coordinates are the four permutations of \((1-3t,t,t,t)\). Writing \(c\) for the centroid of \(T\), one obtains \(K_t=c-(4t-1)(T-c)\). Consequently \(V_t/V_T=(4t-1)^3\), and the standard simplex mixed-volume identity gives \(M_t=3V_t\). If \(t\ge1\), all upper caps are redundant and \(K_t=T\), with \(M_t=3V_T\).

**2. Facet areas in the intermediate chambers.** Fix an index \(i\); let \(F_i=\{\lambda_i=0\}\cap T\), with area \(A_i\). When \(1/3\le t\le1\), the lower face \(\lambda_i=0\) of \(K_t\) has area \(A_iL(t)\), and the upper face \(\lambda_i=t\) has area \(A_iU(t)\). For \(1/3\le t\le1/2\), on \(\lambda_i=0\), the other three coordinates form a triangle with vertices the permutations of \((t,t,1-2t)\), homothetic to \(F_i\) with absolute scale \(3t-1\). On \(\lambda_i=t\), the remaining barycentric triangle has total coordinate mass \(1-t\) and three disjoint removed corner triangles, each of scale \(1-2t\). Hence its area multiplier is \((1-t)^2-3(1-2t)^2\). For \(1/2\le t\le1\), the lower face is the original triangle minus three disjoint corner triangles of scale \(1-t\), giving \(L=1-3(1-t)^2\), while the upper face is a full triangle of scale \(1-t\), giving \(U=(1-t)^2\). These are all possible facets, including the degenerate endpoints by continuity.

**3. Support-area formula.** Let \(h_i=1/\|\nabla\lambda_i\|\) be the altitude of \(T\) above \(F_i\). The simplex volume relation is \(A_ih_i=3V_T\) for every \(i\). Translate the centroid \(c\) to the origin and set \(n_i=\nabla\lambda_i/\|\nabla\lambda_i\|\). In the intermediate chambers the lower and upper outer normals are respectively \(-n_i\) and \(n_i\), with support heights
\[
h_{K_t}(-n_i)=\tfrac14h_i,\qquad h_{K_t}(n_i)=(t-\tfrac14)h_i.
\]
Reflection interchanges these heights. The standard surface-area identity \(V_3(K,K,L)=\frac13\sum_{F\subset\partial K}\operatorname{area}(F)h_L(n_F)\), applied first with \(L=K_t\) and then with \(L=-K_t\), gives
\[
V_t=V_T\bigl(L+(4t-1)U\bigr),\qquad
M_t=V_T\bigl((4t-1)L+U\bigr).
\]
No regularity or symmetry of the original tetrahedron is used.

**4. Difference body and strict phase diagram.** Symmetry and reflection invariance of mixed volume give \(V_3(K_t,K_t,-K_t)=V_3(K_t,-K_t,-K_t)=M_t\). Expanding \(K_t+(-K_t)\) therefore yields \(\operatorname{vol}_3(K_t-K_t)=2V_t+6M_t\). For \(1/3<t<1/2\), direct simplification of the displayed rational expression yields
\[
\rho(t)-1=\frac{2(2t-1)^2(10t-3)}{1-4(1-t)^3+6(1-2t)^3};
\]
for \(1/2<t<1\), it yields
\[
\rho(t)-1=\frac{2(2t-1)^2(3-2t)}{1-4(1-t)^3}.
\]
All denominators are positive volumes divided by \(V_T\). The derivatives in these two ranges are respectively
\[
\rho'(t)=\frac{4(2t-1)(28t^3+18t^2-18t+3)}{\bigl(44t^3-60t^2+24t-3\bigr)^2},
\quad
\rho'(t)=\frac{4(2t-1)(4t^3-18t^2+18t-3)}{\bigl(4t^3-12t^2+12t-3\bigr)^2}.
\]
For the first numerator polynomial, substituting \(t=1/3+u\) gives \(28u^3+46u^2+(10/3)u+1/27>0\). For the second, substituting \(s=1-t\in[0,1/2]\) gives \(1+6s-6s^2-4s^3\ge1+6s-8s^2\ge1\). The derivative signs are therefore negative then positive. The barycentric involution \(\lambda_i\mapsto1/2-\lambda_i\) shows that \(K_{1/2}\) is an affine octahedron, centrally symmetric about \(c\). Taylor expansion of the two exact rational expressions gives the stated one-sided cubic coefficients, proving the differentiability assertion.

## Verification

The independent exact-rational checker `check_tetra.py` reconstructs all vertices as intersections of three barycentric bounding planes and reconstructs all polygonal facets by rational 2D convex hulls. It computes both the volume and the reflected mixed volume directly from the oriented facet-area vector formula, **without using the closed formulas it checks**. It compares these against the displayed identities at twelve rational parameters on both sides of every combinatorial transition, including the tetrahedral and octahedral endpoints. All twelve vertex/facet reconstructions and all twenty-four exact volume/mixed-volume equalities passed with Python 3 standard-library arithmetic. Separately, symbolic differentiation and Taylor expansion establish the rational derivative and smoothness identities; those algebraic calculations are reproduced explicitly in the proof above. Finite checks do not replace the proof for all real \(t\).

## Relationship to prior work

The classical Rogers--Shephard inequality bounds the difference-body volume ratio above by \(20\) in dimension three; the Brunn--Minkowski inequality bounds it below by \(8\). Kotrbatý and Mouamine (2026) proved the termwise Godbersen bound, and Fryš, Kotrbatý, Mouamine, and Wang (2026) identified all general equality cases. Those universal inequalities and extremizer classifications are prior results. The present result is the **all-parameter exact value and strict phase diagram** on the affine-invariant equal-cap tetrahedral family, which the bounds alone do not determine. A published explicit mixed-volume profile for **one** truncated simplex vertex concerns a different deformation and does not by itself provide the simultaneous four-vertex formula. Standard geometric descriptions of regular truncated tetrahedra supply ordinary face and volume data but not the reflected mixed-volume profile established here.

## Limitations

The theorem concerns three-dimensional tetrahedra with **equal barycentric upper caps**; it does not classify arbitrary unequal truncations or higher-dimensional clipped simplices. The normalized ratios require positive three-dimensional volume. Although relevant recent full text and targeted searches found no equivalent complete formula, historical priority is not established by search alone; older material on tetrahedral difference bodies or multi-vertex truncation could conceivably contain an equivalent profile. This work has not undergone independent mathematical audit.

## References

1. F. Fryš, J. Kotrbatý, M. A. Mouamine and S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v2 (first posted 2026-10-05), https://arxiv.org/html/2610.06806v2 .
2. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers--Shephard inequality*, arXiv:2607.20387v2 (first posted 2026-07-22), https://arxiv.org/html/2607.20387v2 .
3. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Arch. Math. 8 (1957), 220--233.
4. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, published published-finding corpus mathematical record, 2026-10-11 (comparison concerns its one-vertex domain, not a four-vertex formula).
