# Sharp three-cell stability and endpoint localization for linear-spline orthoprojection

## Finding

Let \(0=t_0<t_1<t_2<t_3=1\) and let \(P\) be the \(L^2[0,1]\)-orthogonal projection onto the four-dimensional space of continuous functions that are affine on each \([t_{j-1},t_j]\). Regard \(P\) as an integral operator on bounded measurable inputs. For every such strictly positive three-cell partition,
\[
\boxed{\frac53<\|P\|_{L^\infty\to L^\infty}<\frac83.}
\]
Both constants are sharp **over all partitions**, but neither is attained by any nondegenerate three-cell partition:
\[
\inf_{0<t_1<t_2<1}\|P\|_{\infty\to\infty}=\frac53,\qquad
\sup_{0<t_1<t_2<1}\|P\|_{\infty\to\infty}=\frac83.
\]
There is also an exact localization law. Writing \(a=t_1\), \(b=t_2-t_1\), \(c=1-t_2\), the maximum Lebesgue function is always attained at an *endpoint*, never only at an interior knot: at \(t_0\) if \(a<c\), at \(t_3\) if \(c<a\), and at both endpoints if \(a=c\). For every fixed partition, a measurable sign-valued input attains the norm.

An explicit exact profile is available. Put
\[
E=4ab+3ac+2b^2+2bc,\qquad D=4ab+3ac+4b^2+4bc,
\]
and define
\[
\mathcal R(a,b,c)=\frac53+
\frac{8b(a+b)(b+c)^2(4b+3c)}{3(2b+c)ED}.
\]
Then
\[
\boxed{\|P\|_{\infty\to\infty}=
\begin{cases}
\mathcal R(a,b,c),&a\le c,\\
\mathcal R(c,b,a),&c<a.
\end{cases}}
\]
In particular, for the positive unnormalized cell triples \((a,b,c)=(1,\varepsilon,1)\), the norm tends to \(5/3\) as \(\varepsilon\downarrow0\). For \((a,b,c)=(\varepsilon^2,\varepsilon,1)\), it tends to \(8/3\). Overall length rescaling does not affect the operator norm.

## Assumptions and scope

All cell lengths \(a,b,c\) are strictly positive and finite. The measure is ordinary Lebesgue measure; the spline space has **continuity at both interior knots** and no prescribed endpoint conditions. The projection is orthogonal in \(L^2\), while its stability is measured as an induced \(L^\infty\) operator norm, not as a pointwise interpolation constant. Absolute input boundedness is an essential assumption. The result is specific to exactly three cells; no theorem for arbitrary cell counts or higher spline degrees is asserted.

## Proof

Let \(\phi_0,\ldots,\phi_3\) be the usual continuous nodal hat basis, satisfying \(\phi_j(t_i)=\delta_{ij}\). The Gram matrix \(G_{ij}=\int_0^1\phi_i(y)\phi_j(y)\,dy\) is
\[
6G=\begin{pmatrix}
2a&a&0&0\\
a&2(a+b)&b&0\\
0&b&2(b+c)&c\\
0&0&c&2c
\end{pmatrix}.
\]
It is positive definite. If \(S\) is the diagonal matrix with alternating \(+1\) and \(-1\), then \(S(6G)S\) is an irreducible strictly diagonally dominant symmetric matrix with positive diagonal and negative neighboring off-diagonals. Its inverse is strictly entrywise positive. Consequently, for \(C=G^{-1}\), every \((-1)^{i+j}C_{ij}\) is positive.

The reproducing kernel is \(K(x,y)=\sum_{i,j}\phi_i(x)C_{ij}\phi_j(y)\). For each fixed \(y\), the map \(x\mapsto|K(x,y)|\) is convex on each cell; therefore its integral is maximized at a knot. Thus
\[
\|P\|_{\infty\to\infty}=\max_{0\le i\le3}R_i,\qquad
R_i=\int_0^1|K(t_i,y)|\,dy.
\]
On cell \(j\), the kernel interpolates linearly between \(C_{i,j-1}\) and \(C_{ij}\), which have opposite signs. The elementary identity
\[
\int_0^h\left|u\left(1-\frac yh\right)-v\frac yh\right|dy
=\frac{h(u^2+v^2)}{2(u+v)}\qquad(u,v>0)
\]
gives the exact finite expression
\[
R_i=\sum_{j=1}^{3}\frac{h_j\left(C_{i,j-1}^{\,2}+C_{ij}^{\,2}\right)}{2\left(|C_{i,j-1}|+|C_{ij}|\right)},\qquad (h_1,h_2,h_3)=(a,b,c).
\]

Direct inversion and rational cancellation yield \(R_0=\mathcal R(a,b,c)\) and \(R_3=\mathcal R(c,b,a)\). Moreover,
\[
R_0-R_1=\frac{8b^2(b+c)(4ab+3ac+4b^2+5bc+c^2)}{3(2b+c)ED}>0,
\]
and reflection gives \(R_3>R_2\). Hence the norm is always the larger endpoint row.

To determine which endpoint dominates, put \(E'=2ab+3ac+2b^2+4bc\) and
\[
\begin{aligned}
H={}&24a^2b^2+30a^2bc+9a^2c^2+60ab^3+86ab^2c\\
&+30abc^2+36b^4+60b^3c+24b^2c^2.
\end{aligned}
\]
The exact difference factorization is
\[
R_0-R_3=\frac{8b(a+b)(c-a)(b+c)H}{3(a+2b)(2b+c)EE'D}.
\]
Every factor except \(c-a\) is strictly positive. This proves the endpoint localization law and the equality criterion.

The lower bound follows immediately from \(R_0=5/3+\text{a strictly positive rational term}\). For the upper bound, exact cancellation gives
\[
\frac83-R_0=\frac{F}{3(2b+c)ED},
\]
where
\[
\begin{aligned}
F={}&a^2(96b^3+192b^2c+126bc^2+27c^3)\\
&+a(112b^4+236b^3c+154b^2c^2+30bc^3)\\
&+16b^3(b+c)^2.
\end{aligned}
\]
Thus \(8/3-R_0>0\); the reflected identity gives \(8/3-R_3>0\). Combined with endpoint dominance, this proves both strict inequalities.

Finally, replacing \((a,b,c)\) by a common positive multiple leaves all the computed \(R_i\) unchanged. Substituting \((1,\varepsilon,1)\) into the four exact row formulas shows \(R_i\to5/3\) for each \(i\). Substituting \((\varepsilon^2,\varepsilon,1)\) gives \(R_0\to8/3\). The strict inequalities already proved exclude equality at positive cell lengths. Choosing \(f(y)=\operatorname{sgn}K(t_i,y)\) for any maximizing knot \(t_i\) attains the corresponding norm; the kernel zeros have measure zero and their values are immaterial.

## Verification

The standalone `checker.py` reconstructs the Gram matrix, inverts it symbolically, derives the four row integrals, checks the displayed rational identities and polynomial positivity, and verifies both degeneration limits exactly. It also independently samples the kernel integral by midpoint quadrature over positive integer cell triples, testing symbolic expressions against numerical integration. The checker uses Python 3, SymPy and NumPy; run `python checker.py` from the directory containing the file. Exact identities, not the finite tests, establish the theorem for every positive real triple.

## Relationship to prior work

Classical spline projection estimates establish a global \(L^\infty\) bound of \(3\) for linear splines over arbitrary one-dimensional partitions (Ciesielski, as discussed by Oswald and Kayumov). Passenbrunner–Shadrin prove general convergence and inverse-Gram localization results for orthogonal spline projectors. These are important background inputs but their inspected statements do not identify the exact finite three-cell constant, the strict lower envelope, or the endpoint localization law. Oswald's counterexample concerns higher-dimensional triangulations rather than this one-dimensional classification. A closely related 2013 chapter by Oswald on linear-spline projection bounds was identifiable bibliographically but its full text was not accessible; an equivalent finite-three-cell calculation in that or older literature remains a priority risk.

The two-cell exact norm profile has separately been investigated; the present three-cell supremum \(8/3\), strict lower envelope \(5/3\), and shorter-end localization are not consequences of the two-cell statement. No general formula for arbitrarily many cells is claimed.

## Limitations

The lower and upper constants are **uniform extremal values across meshes**, not values achieved at any positive three-cell mesh. The proof addresses maximum-norm stability of the ordinary orthogonal projector only; it does not establish best projection constants among all possible projectors, higher-degree spline estimates, or analogous bounds in higher dimensions. The uniqueness of the limiting degenerating geometry is not asserted. Bibliographic priority remains provisional because not every plausibly relevant older paper could be inspected in full. No independent mathematical or bibliographic validation has been performed.

## References

1. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418 (first posted 30 August 2004). General linear-spline bound and an \(L\)-spline analogue; abstract/source record inspected.
2. P. Oswald, *A counterexample concerning the \(L^2\)-projector onto linear spline spaces*, arXiv:math/0611573 (19 November 2006). Selected full-PDF pages inspected, including Section 1 and the start of the higher-dimensional construction.
3. M. Passenbrunner and A. Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, arXiv:1308.4824 (first posted 22 August 2013). Selected full-PDF pages inspected, including the introduction, kernel estimates, and inverse-Gram analysis.
4. P. Oswald, *\(L^\infty\)-Bounds for the \(L^2\)-Projection onto Linear Spline Spaces*, Springer Proceedings in Mathematics & Statistics 25 (2013), pp. 303–316, DOI:10.1007/978-1-4614-4565-4_24. Bibliographic metadata inspected; full text unavailable at review time.
