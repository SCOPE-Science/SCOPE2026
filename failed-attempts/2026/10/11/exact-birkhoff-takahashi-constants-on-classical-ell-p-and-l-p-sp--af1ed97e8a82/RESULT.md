# Exact Birkhoff–Takahashi constants on classical \(\ell_p\) and \(L_p\) spaces up to quadratic order
## Finding
For every \(1\le p\le\infty\), every index set \(I\) with \(|I|\ge2\), and every \(-\infty\le t\le2\),
\[
C_t^B(\ell_p(I))=2^{|2/p-1|},
\]
with \(1/\infty=0\). The same identity holds for real \(L_p[0,1]\).

Here \(C_t^B\) is the Birkhoff-orthogonal Takahashi–von Neumann–Jordan constant introduced by Qi, Yin and Liu. The result shows that, on these two canonical classes, the Birkhoff restriction is nonbinding for every power-mean order up to the quadratic one.

## Assumptions and scope
All spaces are real. For \(\ell_p(I)\), the index set has at least two elements. The parameter satisfies \(-\infty\le t\le2\). For \(p=\infty\), the exponent is interpreted using \(1/\infty=0\).

No assertion is made here for \(t>2\) when \(1<p<\infty\) and \(p\ne2\). The focal paper leaves only lower/asymptotic information for its \(\ell_p^2\) example, and the later isosceles-orthogonal analogue treats a different orthogonality relation.

## Proof
Qi–Yin–Liu prove monotonicity in the power-mean order and the comparison with Takahashi’s unrestricted constant. Hence, for every real Banach space \(X\) and every \(t\le2\),
\[
C_t^B(X)\le C_2^B(X)\le C_2(X)=C_{\mathrm{NJ}}(X).
\]
Clarkson’s classical formula gives
\[
C_{\mathrm{NJ}}(\ell_p(I))=C_{\mathrm{NJ}}(L_p[0,1])=2^{|2/p-1|}.
\]
It remains to produce Birkhoff-orthogonal unit pairs attaining this value at the endpoint \(\tau=1\).

First suppose \(1\le p\le2\). In \(\ell_p(I)\), choose distinct coordinates \(i,j\) and set \(x=e_i\), \(y=e_j\). Then \(x\perp_B y\), since
\[
\|x+\lambda y\|_p\ge1\qquad(\lambda\in\mathbb R),
\]
and
\[
\|x+y\|_p=\|x-y\|_p=2^{1/p}.
\]
Because every power mean of two equal numbers equals that common number,
\[
C_t^B(\ell_p(I))\ge \frac{(2^{1/p})^2}{2}=2^{2/p-1}.
\]
Together with the upper bound, this proves equality for \(1\le p\le2\).

For \(2\le p<\infty\), take
\[
x=2^{-1/p}(e_i+e_j),\qquad y=2^{-1/p}(-e_i+e_j).
\]
Both are unit vectors. For \(p>1\), the standard smoothness criterion for Birkhoff–James orthogonality in \(\ell_p\) gives
\[
\sum_k |x_k|^{p-2}x_k y_k=0,
\]
so \(x\perp_B y\). At \(\tau=1\),
\[
\|x+y\|_p=\|x-y\|_p=2^{1-1/p},
\]
and therefore
\[
C_t^B(\ell_p(I))\ge\frac{(2^{1-1/p})^2}{2}=2^{1-2/p}.
\]
This matches the Clarkson upper bound. For \(p=\infty\), use \(x=e_i+e_j\) and \(y=-e_i+e_j\). Then
\[
\|x+\lambda y\|_\infty=\max\{|1-\lambda|,|1+\lambda|\}\ge1,
\]
while both endpoint chord lengths equal \(2\), giving \(C_t^B(\ell_\infty(I))=2\).

The argument for \(L_p[0,1]\) is parallel. For \(1\le p\le2\), let \(A=[0,1/2]\), \(B=(1/2,1]\), and use the disjoint unit functions
\[
x=2^{1/p}\mathbf 1_A,\qquad y=2^{1/p}\mathbf 1_B.
\]
They are Birkhoff orthogonal and both endpoint chord lengths are \(2^{1/p}\). For \(2\le p<\infty\), take
\[
x=1,\qquad y=\mathbf 1_A-\mathbf 1_B.
\]
The integral form of the smoothness criterion gives \(x\perp_B y\), and both endpoint chord lengths are \(2^{1-1/p}\). The same pair works directly for \(p=\infty\), because the essential supremum of \(1+\lambda y\) is at least \(1\) for every real \(\lambda\). Thus the same lower bounds meet the same classical upper bound in every case.

## Verification
The proof is exact and symbolic. The upper bound uses only two inequalities from the focal paper—monotonicity in \(t\) and \(C_2^B(X)\le C_2(X)\)—plus Clarkson’s exact von Neumann–Jordan constant. The lower bounds are witnessed by explicit two-coordinate or two-half-interval unit pairs whose Birkhoff orthogonality and endpoint chord lengths are computed exactly.

The endpoint \(p=1\) is checked directly rather than through differentiability. The endpoint \(p=\infty\) is also checked directly. No finite numerical experiment is used as evidence for any quantified statement.

## Relationship to prior work
Qi, Yin and Liu introduce \(C_t^B\), prove the general comparison \(C_t^B(X)\le C_t(X)\), and for \(\ell_p^2\) give a balanced Birkhoff-orthogonal family yielding a lower bound and the limit \(C_t^B(\ell_p^2)\to2\) as \(p\to\infty\). Their paper does not state the exact finite-\(p\) formula above, does not cover the complementary \(1\le p<2\) extremal branch, and does not give the \(L_p[0,1]\) evaluation.

A later isosceles-orthogonal Takahashi paper proves the analogous formula for its distinct direct isosceles restriction. That result does not imply the present statement because Birkhoff–James and isosceles orthogonality are different constraints. The present proof identifies explicit extremal pairs that happen to satisfy the Birkhoff condition and thereby closes the exact comparison for the Birkhoff-restricted invariant.

Clarkson’s 1937 formula for \(C_{\mathrm{NJ}}(L_p)\) supplies the sharp unrestricted upper bound. It is an input, not the new conclusion.

## Limitations
The result is confined to real \(\ell_p(I)\) with at least two coordinates and real \(L_p[0,1]\). It does not determine \(C_t^B\) for \(t>2\) when \(1<p<\infty\), \(p\ne2\), nor does it classify all Banach spaces for which the Birkhoff restriction leaves the unrestricted Takahashi constant unchanged.

The originality conclusion is based on targeted searches of the new invariant, its aliases, the exact formula, the focal full text, the closest isosceles analogue, classical von Neumann–Jordan literature, and the available prior research record. A short equivalent argument could still exist under unindexed terminology.

## References
1. J. Qi, Z. Yin, Q. Liu, “Birkhoff-Orthogonal Takahashi–von Neumann–Jordan Type Constants in Banach Spaces,” arXiv:2608.07146v1, 2026.
2. J. A. Clarkson, “The von Neumann–Jordan constant for the Lebesgue spaces,” Annals of Mathematics 38 (1937), 114–115, DOI 10.2307/1968512.
3. Y. Li, W. Zhou, J. Qi, Q. Liu, “Isosceles-Orthogonal Takahashi–von Neumann–Jordan-Type Constants in Banach Spaces,” Axioms 15 (2026), 684, DOI 10.3390/axioms15090684.
