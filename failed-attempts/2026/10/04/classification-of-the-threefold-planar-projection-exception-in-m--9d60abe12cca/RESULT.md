# Classification of the threefold planar-projection exception in \(\mathbb R^3\)
## Finding
Let \(K\subset\mathbb R^3\) be a convex body, with support function \(h_K:S^2\to\mathbb R\). Then every planar orthogonal projection \(K|P\) is, after a translation within \(P\), invariant under rotation through \(2\pi/3\) if and only if
\[
h_K(u)=c+\langle a,u\rangle+H(u),\qquad u\in S^2,
\]
where \(c>0\), \(a\in\mathbb R^3\), \(H\in\mathcal H_3(S^2)\), and
\[
cI+\nabla^2_{S^2}H(u)+H(u)I\succeq0\qquad\text{for every }u\in S^2.
\]
Here \(\mathcal H_3(S^2)\) is the seven-dimensional space of real spherical harmonics of degree three. Since every \(H\in\mathcal H_3(S^2)\) is odd, the convexity condition is equivalently
\[
\sup_{u\in S^2}\left\|\nabla^2_{S^2}H(u)+H(u)I\right\|_{\mathrm{op}}\le c.
\]
Thus, after the single global translation by \(-a\), every exceptional body has constant width \(2c\). For fixed \(c\), the translation classes form a seven-dimensional compact convex body in \(\mathcal H_3(S^2)\), and its interior consists exactly of the functions for which the curvature-radius matrix is positive definite at every direction.

## Assumptions and scope
A convex body means a compact convex subset of \(\mathbb R^3\) with nonempty interior. For a two-dimensional linear subspace \(P\), the support function of the orthogonal projection agrees with the ambient support function on the great circle: \(h_{K|P}(u)=h_K(u)\) for \(u\in P\cap S^2\). Translating \(K|P\) by \(t_P\in P\) adds the first Fourier mode \(u\mapsto\langle t_P,u\rangle\) on that circle.

The statement is specific to the exceptional order-three case isolated by Myroshnychenko, Ryabogin, and Saroglou. It does not assert an analogous non-spherical family for rotational orders \(q\ge4\), where their theorem proves rigidity to the Euclidean ball.

## Proof
Fix a great circle \(C=P\cap S^2\). A planar support function becomes invariant under rotation by \(2\pi/3\) after translation exactly when its Fourier series on \(C\) has no frequencies except
\[
0,\ \pm1,\ \pm3,\ \pm6,\ \pm9,\ldots .
\]
Indeed, translation contributes exactly the frequencies \(\pm1\), while threefold invariance leaves precisely the frequencies divisible by three. The 2026 source formulates this allowed-frequency space in its reduction of the projection problem.

Let \(V\subset C(S^2)\) be the functions whose restriction to every great circle has only those allowed frequencies. The source proves that the relevant space is closed and rotation invariant and, crucially, that every spherical-harmonic projection of a member of \(V\) remains in \(V\). Write
\[
h_K=\sum_{\ell\ge0} H_\ell,
\qquad H_\ell\in\mathcal H_\ell(S^2).
\]
It is therefore enough to decide which degrees can occur separately.

The same source proves that for every nonzero \(Y\in\mathcal H_\ell(S^2)\) and every integer \(r\) with \(0\le r\le\ell\) and \(r\equiv\ell\pmod2\), some rotated great-circle restriction of \(Y\) has a nonzero Fourier coefficient of frequency \(r\). If \(\ell\ge2\) is even, frequency \(2\) is therefore present on some great circle, but frequency \(2\) is forbidden. Hence every even component with \(\ell\ge2\) vanishes. If \(\ell\ge5\) is odd, frequency \(5\) is present on some great circle and is forbidden, so every odd component with \(\ell\ge5\) vanishes. The only possible degrees are consequently
\[
\ell=0,1,3.
\]
Conversely, every degree-three spherical harmonic is the restriction of a homogeneous harmonic cubic. Restricting any homogeneous cubic to a two-dimensional plane and then to its unit circle yields only frequencies \(1\) and \(3\); degree zero contributes frequency \(0\), and degree one is precisely the translation mode. Hence every function in \(\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_3\) satisfies the required circle-frequency condition.

Write \(H_0=c\) and \(H_1(u)=\langle a,u\rangle\). The degree-one term is the support-function effect of a single global translation. A smooth function \(h\) on \(S^2\) is the support function of a convex body exactly when its spherical curvature-radius form
\[
Q_h(u)=\nabla^2_{S^2}h(u)+h(u)I
\]
is positive semidefinite at every \(u\). The linear term has \(Q_{\langle a,\cdot\rangle}=0\), so the condition becomes
\[
Q_h(u)=cI+Q_H(u)\succeq0,
\qquad
Q_H(u)=\nabla^2_{S^2}H(u)+H(u)I.
\]
Because \(H\) has odd degree, \(H(-u)=-H(u)\), and under the antipodal identification of tangent planes one has \(Q_H(-u)=-Q_H(u)\). Positivity at both \(u\) and \(-u\) is therefore equivalent to all eigenvalues of \(Q_H(u)\) lying in \([-c,c]\), which is exactly
\[
\|Q_H(u)\|_{\mathrm{op}}\le c
\]
for every \(u\). Oddness also gives
\[
h_K(u)+h_K(-u)=2c,
\]
after deleting the linear translation term, so the translated body has constant width \(2c\). Nonempty interior forces \(c>0\).

Finally, define
\[
\mathcal B_c=\left\{H\in\mathcal H_3(S^2):\sup_{u\in S^2}\|Q_H(u)\|_{\mathrm{op}}\le c}\right\}.
\]
This set is convex and closed. The map \(H\mapsto Q_H\) is injective on \(\mathcal H_3(S^2)\): a function with \(Q_H=0\) is the restriction of a linear functional, while a degree-three harmonic is orthogonal to degree one. Thus \(H\mapsto\sup_u\|Q_H(u)\|_{\mathrm{op}}\) is a norm on the finite-dimensional seven-dimensional space \(\mathcal H_3(S^2)\). Hence \(\mathcal B_c\) is compact, has nonempty interior, and is seven-dimensional. Strict inequality is equivalent, using the antipodal relation, to positive definiteness of \(cI+Q_H(u)\) for every direction.

## Verification
The proof was checked at the level of the exact frequency sets and quantifiers. In particular, higher harmonic degrees cannot survive through cancellation between degrees because the 2026 paper's harmonic-projection lemma keeps each degree inside the allowed-frequency space. Every even degree \(\ell\ge2\) is killed by a forced frequency \(2\), and every odd degree \(\ell\ge5\) is killed by a forced frequency \(5\). Degree three is genuinely allowed because a cubic restricted to a circle has only frequencies \(1\) and \(3\).

The convexity step is analytic rather than experimental. The standard support-function criterion reduces convexity to positive semidefiniteness of \(Q_h\); antipodal oddness then gives the exact operator-norm ball. No finite sampling of directions is used to infer the universal statement.

## Relationship to prior work
Myroshnychenko, Ryabogin, and Saroglou prove that rotational order \(q\ge4\) forces a ball and explicitly identify \(q=3\) as exceptional. In their exceptional section they exhibit the cubic \(u_1u_2u_3\), show its great-circle restrictions use only frequencies \(1\) and \(3\), and obtain non-spherical smooth constant-width examples for sufficiently small perturbations of the ball. Their paper does not state the complete order-three classification above: the classification uses their harmonic-projection and great-circle frequency lemmas to eliminate every degree except \(0\), \(1\), and \(3\), then imposes the exact support-function convexity condition.

The 2016 paper by the same authors proves rigidity under a stronger centered complete-symmetry hypothesis for projections. That result does not dominate the present statement because the order-three problem allows an independently chosen translation in each projection plane before symmetry is imposed. The classification here shows that these apparently plane-dependent centers nevertheless force a single global translation plus a degree-three support component.

## Limitations
The result classifies the three-dimensional order-three projection condition only. It does not classify the higher-dimensional extension mentioned in the source, nor does it quotient the seven-dimensional parameter body by rotations or other congruences. The boundary of \(\mathcal B_c\) can contain bodies with vanishing curvature radius in some directions; only its interior is asserted to have positive-definite curvature-radius form everywhere. A residual bibliographic risk remains that an older equivalent classification exists under different harmonic-analysis terminology, although targeted searches for the order-three projection condition, the \(\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_3\) formulation, and constant-width cubic support functions did not locate such a statement.

## References
1. S. Myroshnychenko, D. Ryabogin, and C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1, first public 2026-09-23.
2. S. Myroshnychenko, D. Ryabogin, and C. Saroglou, *Star bodies with completely symmetric sections*, arXiv:1611.09443v1, first public 2016-11-29.
3. R. Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, second edition, for the standard spherical support-function convexity criterion.
