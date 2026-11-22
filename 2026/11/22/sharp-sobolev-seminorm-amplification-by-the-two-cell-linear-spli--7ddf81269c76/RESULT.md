# Sharp Sobolev seminorm amplification by the two-cell linear-spline orthoprojector

## Finding
For every interior knot \(h\in(0,1)\), with \(b=1-h\) and \(\mu=\min\{h,b\}\), the ordinary real \(L^2(0,1)\) orthogonal projector \(P_h\) onto continuous linear splines with knots \(0,h,1\) satisfies the exact, attained bounds
\[
\|P_h\|_{\dot W^{1,\infty}\to\dot W^{1,\infty}}=1+\frac{4(1-\mu)^2}{9\mu},
\]
\[
\|P_h\|_{\dot W^{1,2}\to\dot W^{1,2}}^2
=\frac{3}{20hb}\big(1+4hb+|1-2h|\sqrt{1-3hb}\big).
\]
Both functions of \(h\) have their unique minima at \(h=1/2\): respectively \(11/9\) and \(\sqrt{6/5}\). In the singular grading limit \(\mu\downarrow0\), their leading behaviours are \(4/(9\mu)\) and \(\sqrt{3/(10\mu)}\). A two-element mesh is the smallest mesh capable of this grading-dependent divergence.

## Assumptions and scope
All functions and inner products are real, with Lebesgue measure on \((0,1)\). No boundary conditions or point-mass weights are imposed. \(S_h\) is the three-dimensional space of continuous functions linear on each element, and \(P_h\) is the \(L^2\)-orthogonal projector onto \(S_h\). For \(p=2,\infty\), the derivative-seminorm operator norm is
\[
\sup_{f\in W^{1,p}(0,1),\ \|f'\|_{L^p}>0}
\frac{\|(P_h f)'\|_{L^p}}{\|f'\|_{L^p}}.
\]
Constants are quotiented out: the result is *not* about the full inhomogeneous Sobolev norm. Endpoints \(h=0,1\) are excluded because the spline space changes dimension there.

## Proof
Let \(\phi_0,\phi_1,\phi_2\) be the nodal hat basis at \(0,h,1\). Its mass matrix and inverse are
\[
M_h=\frac16\begin{pmatrix}2h&h&0\\h&2&b\\0&b&2b\end{pmatrix},\qquad
M_h^{-1}=\begin{pmatrix}1+3/h&-2&1\\-2&4&-2\\1&-2&1+3/b\end{pmatrix}.
\]
For any \(f\in W^{1,1}\), the projected slopes \(D_L(f)=(P_h f)'\vert_{(0,h)}\) and \(D_R(f)=(P_h f)'\vert_{(h,1)}\) are represented as
\[
D_L(f)=\int_0^1 Q_L(t)f'(t)\,dt,\qquad D_R(f)=\int_0^1Q_R(t)f'(t)\,dt,
\]
with four explicit quadratic pieces
\[
Q_L(t)=\begin{cases}
\frac{3t(2h(h+1)-(3h+1)t)}{2h^3},&0\le t\le h,\\
\frac{3(1-t)(1+2h-3t)}{2hb},&h\le t\le1,
\end{cases}
\]
\[
Q_R(t)=\begin{cases}
\frac{3t(3t-2h)}{2hb},&0\le t\le h,\\
\frac{3(1-t)(2b(1+b)-(3b+1)(1-t))}{2b^3},&h\le t\le1.
\end{cases}
\]
Indeed, if \(k_L(t)=(\phi_1-\phi_0)^{\mathsf T}M_h^{-1}\phi(t)/h\) and \(k_R(t)=(\phi_2-\phi_1)^{\mathsf T}M_h^{-1}\phi(t)/b\) are the scalar slope kernels against \(f(t)\), then the displayed quadratics have \(-Q'_L=k_L\), \(-Q'_R=k_R\), vanish at the exterior endpoints, and are continuous at \(h\). Integration by parts gives the formulas. Direct integration yields \(\int Q_L=\int Q_R=1\).

The first influence kernel is positive up to \(r=(1+2h)/3\) and negative after; the other is negative up to \(s=2h/3\) and positive after. Notice \(h<r<1\), and \(0<s<h\). Therefore
\[
\int_0^1|Q_L(t)|\,dt=1+\frac{4b^2}{9h},\qquad
\int_0^1|Q_R(t)|\,dt=1+\frac{4h^2}{9b}.
\]
For the \(L^\infty\) derivative norm we take the maximum of these two row integrals, proving the first formula. There is no nonattainment issue: a Lipschitz function with \(f'(t)=\operatorname{sgn}Q_L(t)\) attains the left-row integral; for example \(f(t)=t\) up to \(r\) and \(f(t)=2r-t\) after \(r\). Reflection attains the right-row norm.

For the \(L^2\) derivative norm, identify \(g=f'\in L^2(0,1)\) and the weighted output slope vector \((\sqrt h\langle Q_L,g\rangle,\sqrt b\langle Q_R,g\rangle)\). Every \(g\in L^2\) arises as a derivative of an \(H^1\) function. The squared norm is the maximal eigenvalue of the \(2\times2\) matrix
\[
H=\begin{pmatrix}
h\langle Q_L,Q_L\rangle&\sqrt{hb}\langle Q_L,Q_R\rangle\\
\sqrt{hb}\langle Q_L,Q_R\rangle&b\langle Q_R,Q_R\rangle
\end{pmatrix}.
\]
Exact integration gives
\[
\langle Q_L,Q_L\rangle=\frac{3(2h^2+h+1)}{10h^2},\quad
\langle Q_R,Q_R\rangle=\frac{3(2b^2+b+1)}{10b^2},\quad
\langle Q_L,Q_R\rangle=-\frac{3(1-2h)^2}{20hb}.
\]
Hence
\[
\operatorname{tr}H=\frac{3(1+4hb)}{10hb},\quad
\det H=\frac{9(15+4hb)}{400hb},\quad
(\operatorname{tr}H)^2-4\det H=\frac{9(1-2h)^2(1-3hb)}{100h^2b^2}.
\]
The quadratic eigenvalue formula proves the stated squared \(H^1\) coefficient. Equality is attained by choosing \(g\) as the corresponding normalized linear combination of \(Q_L\) and \(Q_R\); integrating \(g\) produces a genuine input \(f\in H^1(0,1)\).

The first norm is strictly decreasing in \(\mu\in(0,1/2]\), as is immediate by differentiation. For the second, set \(u=hb\in(0,1/4]\); its square is \(3(1+4u+\sqrt{(1-4u)(1-3u)})/(20u)\). The terms \(1/u\) and \(\sqrt{(1-4u)(1-3u)}/u\) are strictly decreasing with \(u\), and \(u\) has its unique maximum at \(h=1/2\). The displayed minima and asymptotics follow by substitution and expansion. On a one-element mesh the projection is onto global affine functions, so its Lipschitz seminorm gain is exactly one, precluding any element-ratio divergence.

## Verification
Run `python checker.py` with SymPy. It recomputes the exact Gram inverse and both integrated influence kernels, tests the two absolute integrals, verifies an explicit tent-function extremizer, integrates the quadratic Gram matrix and its trace/determinant/discriminant, and compares the formulas on five distinct rational knots. These algebraic checks supplement, rather than replace, the sign analysis, operator-duality argument, and eigenvector attainment above.

## Relationship to prior work
Diening, Storn and Tscherpel (arXiv:2008.01801, first posted 4 August 2020) derive broad mesh-grading-dependent sufficient Sobolev and \(L^p\) stability conditions for finite-element \(L^2\)-orthogonal projection. Their Theorem 4.13 bounds \(W^{1,p}\) seminorms on qualified meshes but does not provide these exact two-element constants. Bank and Yserentant treat finite-element \(H^1\)-stability and in their Section 7 exhibit a counterexample using an *infinite geometrically graded partition*, not an exact three-node finite-mesh formula. Ali, Funken and Schmidt address \(H^1\) stability on adaptive two-dimensional quadrilateral meshes. Related sharp uniform-norm results for periodic/bi-infinite spline projection concern \(L^\infty\)-input size, not sharp derivatives of arbitrary \(W^{1,p}\) inputs. The claimed additional information is the exact finite-mesh answer at two Sobolev endpoints, sharp extremizers, unique balanced optimum and distinct grading exponents; general qualitative instability alone would not establish the numerical identities.

## Limitations
Only a single interior knot, continuous degree-one splines, no boundary constraints, and \(p=2,\infty\) derivative seminorms are covered. The formulas do not supply operator norms for higher dimensions, other \(p\), or full inhomogeneous Sobolev norms. In the one-dimensional variable-mesh literature there may be earlier equivalent formulas not identified by accessible bibliographic searches. The claim is mathematically derived and symbolically checked but has no independent external validation.

## References
- L. Diening, J. Storn, T. Tscherpel, *On the Sobolev and \(L^p\)-Stability of the \(L^2\)-projection*, first submitted 2020-08-04, https://arxiv.org/abs/2008.01801 (Theorem 4.13).
- R. E. Bank, H. Yserentant, *On the \(H^1\)-stability of the \(L^2\)-projection onto finite element spaces*, Numerische Mathematik, DOI https://doi.org/10.1007/s00211-013-0562-4 (Section 7).
- M. Ali, S. A. Funken, A. Schmidt, *\(H^1\)-Stability of the \(L^2\)-Projection onto Finite Element Spaces on Adaptively Refined Quadrilateral Meshes*, first submitted 2020-08-28, https://arxiv.org/abs/2008.12759.
