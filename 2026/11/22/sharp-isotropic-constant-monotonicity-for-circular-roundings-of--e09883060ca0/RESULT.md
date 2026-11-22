# Sharp isotropic-constant monotonicity for circular roundings of all regular polygons

## Finding
Let \(P_n\) be the regular, origin-centered \(n\)-gon of circumradius one in \(\mathbb R^2\), where \(n\ge3\) is an integer, and let \(B\) be the closed Euclidean unit disk. For every \(t\ge0\), set \(K_{n,t}=P_n+tB\). If \(X\) is uniform in a planar convex body \(K\), write
\[
L(K)^4=\frac{\det\operatorname{Cov}(X)}{\operatorname{area}(K)^2}.
\]
Then **\(t\mapsto L(K_{n,t})^4\) is strictly decreasing on \([0,\infty)\) for every \(n\ge3\)**. In particular, it lies strictly between the regular-polygon value and the disk value for every \(t>0\):
\[
\frac{1}{16\pi^2}<L(K_{n,t})^4<L(P_n)^4
=\frac{\left(\cos^2(\pi/n)+\tfrac13\sin^2(\pi/n)\right)^2}
{16n^2\sin^2(\pi/n)\cos^2(\pi/n)}.
\]
The right bound is attained only when \(t=0\); the left bound is approached, not attained, as \(t\to\infty\). The convergence has an exact positive leading term: with \(\alpha=\pi/n\), \(c=\cos\alpha\), \(s=\sin\alpha\), and
\[
g_n=\alpha^2+\alpha cs-2s^2>0,
\]
one has
\[
L(K_{n,t})^4=\frac{1}{16\pi^2}+\frac{n^2g_n}{4\pi^4t^2}+O_n(t^{-3})
\qquad(t\to\infty).
\]
For arbitrary initial circumradius \(R>0\), replace \(t\) by \(t/R\); the displayed isotropic constant is unchanged by the common dilation.

## Assumptions and scope
The polygon is regular, full-dimensional, and has \(n\ge3\) vertices. Rounding means the **outer Minkowski sum with a Euclidean disk** for every real \(t\ge0\), with no restriction to small radii. Area and covariance are computed from two-dimensional Lebesgue measure on the solid region, not arclength measure on its boundary. The center is the origin by rotational symmetry, and the covariance is scalar because the rotation angle \(2\pi/n\) is not a multiple of \(\pi\). No statement is made for irregular polygons, noncircular gauges or arbitrary convex bodies.

## Proof
**1. An exact polygon–strip–sector decomposition.** Put \(\alpha=\pi/n\), \(c=\cos\alpha\), and \(s=\sin\alpha\). The original polygon has inradius \(c\), side half-length \(s\), area \(ncs\), and polar second moment
\[
J(P_n)=\int_{P_n}\|x\|^2dx
=\frac{ncs}{2}\left(c^2+\frac{s^2}{3}\right).
\]
The moment identity follows by dividing the polygon into \(n\) congruent triangles and integrating in coordinates normal and tangent to each side, or directly by Green's theorem. Apart from zero-area interfaces, \(K_{n,t}\) partitions into the polygon, one \(2s\times t\) rectangle on each side, and one circular sector of radius \(t\) and angular span \(2\alpha\) outside each vertex. Integrating \(\|x\|^2\) in the normal strip coordinates and polar vertex-sector coordinates gives, without approximation,
\[
\begin{aligned}
A(t)&=\operatorname{area}(K_{n,t})=ncs+2nst+\pi t^2,\\
J(t)&=\int_{K_{n,t}}\|x\|^2dx\\
&=\frac{ncs}{2}\left(c^2+\frac{s^2}{3}\right)
+2ns\left(c^2+\frac{s^2}{3}\right)t
+(2ncs+\pi)t^2+2nst^3+\frac{\pi}{2}t^4.
\end{aligned}
\]
For clarity, each strip contributes moment \(2s(c^2+s^2/3)t+2cst^2+(2s/3)t^3\). Each vertex sector, centered at a unit-length vertex, contributes \(\alpha t^2+(4s/3)t^3+(\alpha/2)t^4\). These add to the stated coefficients.

**2. Scalar covariance and a positive derivative certificate.** Rotational symmetry gives
\(\operatorname{Cov}(X)=\frac{J(t)}{2A(t)}I_2\), hence
\[
L(K_{n,t})^4=\frac{J(t)^2}{4A(t)^4}.
\]
Write \(k=\alpha/s\) and set \(A(t)=ns\,a(t)\), \(J(t)=ns\,j(t)\), where
\[
\begin{aligned}
a(t)&=c+2t+kt^2,\\
j(t)&=\tfrac c2(c^2+s^2/3)+2(c^2+s^2/3)t
+(2c+k)t^2+2t^3+\tfrac k2t^4.
\end{aligned}
\]
A polynomial expansion, using \(c^2+s^2=1\), yields the exact identity
\[
\begin{aligned}
j'(t)a(t)-2j(t)a'(t)
={}&-\frac{4s}{3}(s-\alpha c)t
-\frac{2}{s}f(\alpha)t^2
-\frac{2}{s^2}g(\alpha)t^3,\\
f(\alpha)&=\alpha(1+2\cos^2\alpha)-3\sin\alpha\cos\alpha,\\
g(\alpha)&=\alpha^2+\alpha\sin\alpha\cos\alpha-2\sin^2\alpha.
\end{aligned}
\]
For \(0<\alpha\le\pi/3\), the function \(u(\alpha)=\sin\alpha-\alpha\cos\alpha\) is strictly positive, because \(u(0)=0\) and \(u'(\alpha)=\alpha\sin\alpha>0\). Moreover \(f(0)=g(0)=0\) and
\[
f'(\alpha)=4\sin\alpha\,u(\alpha)>0,\qquad
 g'(\alpha)=f(\alpha)>0.
\]
Thus all three coefficients on the right are strictly negative. Since \(a(t)>0\) and \(j(t)>0\),
\[
\frac{d}{dt}\frac{j(t)}{a(t)^2}
=\frac{j'(t)a(t)-2j(t)a'(t)}{a(t)^3}<0
\qquad(t>0).
\]
This proves strict decrease of \(J(t)/A(t)^2\) and hence \(L(K_{n,t})^4\). At \(t=0\) the derivative is zero, but strict decrease on \((0,\infty)\) and continuity establish strict ordering for all distinct \(t\ge0\).

**3. Sharp disk comparison and asymptotic rate.** Let
\[
h(\alpha)=\alpha\left(\cos^2\alpha+\frac{\sin^2\alpha}{3}\right)-\sin\alpha\cos\alpha.
\]
Here \(h(0)=0\) and \(h'(\alpha)=\frac43\sin\alpha\,u(\alpha)>0\), so \(h(\alpha)>0\). Direct expansion of the exact polynomials gives a *second* positive identity,
\[
2\pi J(t)-A(t)^2=n^2\bigl(cs\,h(\alpha)+4s\,h(\alpha)t+2g(\alpha)t^2\bigr)>0.
\]
Therefore \(J(t)>A(t)^2/(2\pi)\), giving \(L(K_{n,t})^4>1/(16\pi^2)\) for every finite \(t\ge0\). Finally, \(A(t)\sim\pi t^2\) and \(2\pi J(t)-A(t)^2=2n^2g(\alpha)t^2+O_n(t)\); substituting in \(J^2/(4A^4)\) yields the exact inverse-square leading term in the finding. The value at \(t=0\) follows immediately from Step 1.

## Verification
The companion standalone program `check_parallel_polygon.py` verifies both displayed polynomial identities symbolically with the trigonometric relation \(c^2+s^2=1\), and independently reconstructs area and second moment through Green boundary integrals along straight segments and circular arcs, for nine polygon orders and seven radii. Run `python3 check_parallel_polygon.py` with SymPy installed. The mathematical proof is the sign argument in Step 2; numerical checks verify finite instances only. The analytic sign certificate applies to all parameters, while the finite checker applies only to its tested cases.

## Relationship to prior work
Richter and Saorín Gómez, in their 2020 preprint and subsequent journal article, prove monotonic decrease of the **isoperimetric quotient** (perimeter squared divided by area in the planar case) of parallel bodies, and further quermassintegral quotients. This result does not govern the **solid-body covariance determinant** or imply the moment identities here. The published *Sharp isotropic response to Euclidean rounding of cubes* establishes a universal second-order loss under cube rounding and global monotonicity in dimension three; its dimension-two result determines the small-radius quadratic term for a rounded square, but does not give all-radius strict ordering for arbitrary regular polygons. The published *Strict Mahler-product growth along circular roundings of regular polygons* studies exactly the same rounded polygons and proves monotonicity for a **polar-area volume product**, which is a different invariant and does not imply the uniform-interior second-moment ordering. This result supplies the independent exact covariance profile and a sharp all-radius sign certificate.

## Limitations
The result does not assert that all convex bodies have decreasing isotropic constants under Euclidean rounding; the proof uses regularity to make covariance scalar and to obtain a three-term positive certificate. The large-radius expansion is for a fixed polygon order and is not a uniform joint \(n,t\) asymptotic. Known local square behavior is credited explicitly. Priority against every unindexed classical engineering-inertia calculation is not guaranteed by the cited comparisons.

## References
- C. Richter and E. Saorín Gómez, *On the monotonicity of the isoperimetric quotient for parallel bodies*, arXiv:2003.14182, first public version 2020-03-31; *Journal of Geometric Analysis* 32 (2022), article 15. https://arxiv.org/abs/2003.14182
- *Sharp isotropic response to Euclidean rounding of cubes*, publicly available research finding, 2026, source identifier `c7d29f80bf57` (comparison of the dimension-two local result and dimension-three global result).
- *Strict Mahler-product growth along circular roundings of regular polygons*, publicly available research finding, 2026, source identifier `cd13878768d7` (comparison for an alternate affine invariant).
