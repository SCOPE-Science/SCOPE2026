# Sharp one-step Steiner inertia contraction of a square and the full rectangle directional law

## Finding
For the centrally positioned rectangle \(R_{a,b}=[-a,a]\times[-b,b]\), where \(a,b>0\), consider Steiner symmetrization about a line through the origin at angle \(\theta\), and polar second moment \(I(K)=\int_K\|x\|^2\,dx\). The inertia drop is \(\Delta_{a,b}(\theta)=I(R_{a,b})-I(S_\theta R_{a,b})\). Its complete directional profile is explicit.

For \(0<\theta<\pi/2\), put \(t=\tan\theta\). In the regime \(t\le a/b\),
\[
\boxed{\Delta_{a,b}(\theta)=\frac{2bt}{3(1+t^2)}\left[2a^3t-2ab^2t^3-4ab^2t+b^3(1+t^2)^2\right].}
\]
For \(t\ge a/b\), use the displayed expression with \((a,b,t)\) replaced by \((b,a,t^{-1})\). Both formulas agree at the separating angle; reflection symmetries and limits extend the law to every unoriented axis.

In particular, for a square \(Q_h=[-h,h]^2\), define \(u=\min\{|\tan\theta|,|\cot\theta|\}\) with continuous value \(0\) at coordinate axes. Then
\[
\boxed{I(Q_h)-I(S_\theta Q_h)=\frac{2h^4}{3}u(1-u)^2\le\frac{8h^4}{81},}
\]
where equality holds if and only if the symmetrization line has slope \(1/3\), \(-1/3\), \(3\), or \(-3\). The corresponding sharp one-step relative drop is \(1/27\): \(I(S_\theta Q_h)\ge(26/27)I(Q_h)\), with equality exactly at those four unoriented axes.

## Assumptions and scope
The bodies have constant area density, Euclidean metric, positive half-side lengths, and center at the origin. The Steiner symmetral \(S_\theta K\) is obtained by replacing each section perpendicular to the line through the origin at angle \(\theta\) with the centered interval of the same length. No renormalization or additional translation occurs. As the rectangle is centrally symmetric, so is every centered symmetral, whose centroid remains the origin. Hence the raw polar moment is also the central polar moment. All displayed formulas hold for every real direction and every positive pair of half-side lengths, including the boundary and equal-projection transition by continuity.

## Proof
Write \(c=\cos\theta>0\), \(s=\sin\theta>0\), \(z=cX+sY\), \(w=-sX+cY\), and \(A=ac\), \(B=bs\). The transformation is orthogonal. For each \(z\), let \(L(z)\) be the length and \(m(z)\) the center of the fiber of the rectangle on the line of constant \(z\). The corresponding fiber in its Steiner symmetral has the same length and center zero. Directly integrating \(w^2\) over an interval of length \(L\) centered at \(m\) gives \(L^3/12+Lm^2\), and the contribution of \(z^2\) is unchanged. Therefore
\[
\Delta_{a,b}(\theta)=\int_{-A-B}^{A+B}L(z)m(z)^2\,dz.
\]
Central symmetry gives \(L(-z)=L(z)\) and \(m(-z)=-m(z)\).

Suppose first that \(A\ge B\), equivalent to \(0<t\le a/b\). Intersecting the two independent coordinate bounds \(|X|\le a\) and \(|Y|\le b\) with a line of fixed \(z\), for nonnegative \(z\) gives exactly
\[
\begin{array}{c|c|c}
\text{range of }z& L(z)&m(z)\\ \hline
0\le z\le A-B&2B/(cs)&-sz/c\\
A-B\le z\le A+B&(A+B-z)/(cs)&((c^2-s^2)z-(A-B))/(2cs).
\end{array}
\]
Indeed, setting \(U=cX\in[-A,A]\), \(V=sY\in[-B,B]\) and \(U+V=z\), the allowed interval for \(U\) is \([\max(-A,z-B),\min(A,z+B)]\); its affine image under \(w=-sU/c+c(z-U)/s\) gives the table. Consequently
\[
\Delta_{a,b}(\theta)=2\left(\int_0^{A-B}\frac{2B}{cs}\frac{s^2z^2}{c^2}\,dz+\int_{A-B}^{A+B}\frac{A+B-z}{cs}\frac{((c^2-s^2)z-(A-B))^2}{4c^2s^2}\,dz\right).
\]
These two polynomial integrals simplify, with \(c^2=1/(1+t^2)\) and \(s=tc\), to the claimed rational formula. The complete symbolic integration and algebraic simplification are replayed in the included checker. If \(A<B\), exchanging the original coordinate axes changes \((a,b,t)\) to \((b,a,1/t)\), proving the complementary branch. The two representations coincide when \(A=B\), since they represent the same geometrically defined integral. At horizontal and vertical axes the rectangle is already symmetric and the decrease is zero; symmetry under reversing either coordinate gives the full angular law.

For \(a=b=h\), the first branch factors as \(2h^4t(1-t)^2/3\) for \(0\le t\le1\), and the second follows from \(t\mapsto1/t\). On \(0\le u\le1\), the derivative of \(2u(1-u)^2/3\) is \(2(1-u)(1-3u)/3\), strictly positive before \(u=1/3\) and strictly negative afterward. The maximum equals \(8/81\), attained only at \(u=1/3\). The polar second moment of the original square is \(I(Q_h)=8h^4/3\), so dividing proves the sharp relative loss \(1/27\) and characterizes all maximizing directions.

## Verification
The standalone file `steiner_rectangle_check.py` uses SymPy to independently integrate the stated fiber pieces symbolically, compare the exact all-rectangle expression, verify the square factorization, calculate the derivative, and establish the rational extremal value. Separately, it constructs the vertices of each rotated rectangle, intersects arbitrary lines with its polygon edges, and numerically integrates \(L(z)m(z)^2\) over fiber breakpoint intervals without using the analytic fiber formulas. It checks five aspect ratios at eight angles each and all four maximizing axes for the unit square. Run `python steiner_rectangle_check.py` with Python, SymPy and SciPy installed. The recorded replay passes 89 assertions. The symbolic computation verifies polynomial integration; the limiting, symmetry and monotonicity arguments above provide the all-real-angle proof.

## Relationship to prior work
Bianchi, Burchard, Gronchi and Volčić established general strict monotonicity of moment of inertia under Steiner symmetrization in their study of convergence in shape. Their monotonicity statement does not specify the amount of decrease or its maximizing direction for rectangles. Basit and Lángi developed Steiner symmetrization methods for discrete isoperimetric problems involving simplices and low-vertex polytopes; their 2022 preprint does not state this rectangle's directional moment formula. Izmestiev's published moment-of-inertia comparison under symmetrization treats width-constrained centroid questions, not this sharp direction optimization. Existing results on random-direction \(\lambda\)-Steiner symmetrization of triangles address different objects and averaged objectives. The contribution here is the complete one-step rectangle profile and the exact square maximizing axes with a sharp dimensionless contraction fraction, not a new general monotonicity theorem.

## Limitations
The square optimum is among single centered Steiner symmetrizations of that fixed square, not among arbitrary area-preserving transformations or among all convex bodies. The formula does not determine the optimal direction for every unequal rectangle in closed form, although it evaluates every direction. It does not prove an accelerated bound for iterative symmetrization. Priorities in unindexed classical symmetrization or mechanical-inertia literature may include equivalent computations; the present review does not establish independence or exhaustive global priority.

## References
- Bushra Basit and Zsolt Lángi, *Discrete isoperimetric problems in spaces of constant curvature*, first posted 2022-06-09, arXiv:2206.04323, https://arxiv.org/abs/2206.04323, journal DOI 10.1112/mtk.12175.
- Gabriele Bianchi, Almut Burchard, Paolo Gronchi and Aljoša Volčić, *Convergence in Shape of Steiner Symmetrizations*, accessible full text https://flore.unifi.it/retrieve/e398c378-d220-179a-e053-3705fe0a4cff/shape-revision-A.pdf.
- Ivan Izmestiev, *Matching centroids by a projective transformation*, *Geometriae Dedicata* 217 (2023), 53; https://doi.org/10.1007/s10711-023-00789-9 (earlier preprint available).
