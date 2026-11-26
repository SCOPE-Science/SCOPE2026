# Strict Bernstein curvature and sharp angular stability for Minkowski sums of planar ellipses

## Finding
For two ellipses, strict angular area monotonicity was previously recorded in the excluded-area literature. The result here is the stronger **all-orders Bernstein curvature law** in the natural angle coordinate, together with the exact optimal strong-concavity constant and a sharp global quadratic stability refinement.

Let \(a>b>0\) and \(c>d>0\). Define the filled, centered ellipse
\[
E_{a,b}=\{(x,y)\in\mathbb R^2:x^2/a^2+y^2/b^2\le1}\,
\]
and \(R_\theta\) as counterclockwise rotation through angle \(\theta\). For \(u\in[0,1]\), put
\[
F(u)=\operatorname{area}\bigl(E_{a,b}+R_{\arcsin\sqrt u}E_{c,d}\bigr).
\]
Set
\[
T_0=\frac{a^2}{c^2}+\frac{b^2}{d^2},\qquad
H=(a^2-b^2)\left(\frac1{d^2}-\frac1{c^2}\right)>0,\qquad s=\frac{ab}{cd}.
\]
Then the exact formula is
\[
F(u)=\pi(ab+cd)+\sqrt2\,cd\int_0^\infty
\frac{1-\bigl(1+2t(T_0+Hu)+4s^2t^2\bigr)^{-1/2}}{t^{3/2}}\,dt.
\]
For every integer \(k\ge1\) and every \(u\in[0,1]\), with one-sided derivatives at the endpoints,
\[
(-1)^{k-1}F^{(k)}(u)=\sqrt2\,cd\,(2k-1)!!\,H^k
\int_0^\infty\frac{t^{k-3/2}}{\bigl(1+2t(T_0+Hu)+4s^2t^2\bigr)^{k+1/2}}\,dt>0.
\]
In particular the area is strictly increasing and strictly concave as a function of \(u=\sin^2\theta\). The **exact optimal strong-concavity modulus** is
\[
m=3\sqrt2\,cd H^2\int_0^\infty
\frac{t^{1/2}}{\bigl(1+2t(T_0+H)+4s^2t^2\bigr)^{5/2}}\,dt,
\qquad -F''(u)\ge m>0.
\]
Consequently, for all \(0\le u\le1\),
\[
\boxed{F(u)\ge (1-u)F(0)+uF(1)+\frac m2u(1-u)}.
\]
The displayed inequality is strict in the interior, and \(m\) is the largest constant with \(F''\le-m\) on this interval. The already-known alignment extremizers are recovered, but the complete derivative alternation and the positive, sharp quantitative surplus are additional assertions. If \(a=b\) or \(c=d\), \(H=0\), \(F\) is constant and \(m=0\); no strict inequality is asserted.

## Assumptions and scope
The bodies are filled Euclidean ellipses in \(\mathbb R^2\), their centers are at the origin (translations do not change area), and \(a,b,c,d\) are strictly positive. The relative major-axis angle is represented by \(0\le\theta\le\pi/2\); all orientation dependence is through \(u=\sin^2\theta\). Area is ordinary two-dimensional Lebesgue area. The result is not a statement about ellipsoid sums in dimension three or higher.

## Proof
**1. Exact Steiner reduction.** Let \(D\) be the Euclidean unit disk, \(A=\operatorname{diag}(a,b)\), and \(B=R_\theta\operatorname{diag}(c,d)R_\theta^\top\). Since \(E_{a,b}=AD\) and \(R_\theta E_{c,d}=BD\), applying \(B^{-1}\) to their Minkowski sum gives \((B^{-1}A)D+D\). The planar Steiner formula \(\operatorname{area}(K+D)=\operatorname{area}(K)+\operatorname{perimeter}(K)+\pi\), followed by multiplying area by \(\det B=cd\), yields
\[
F(u)=\pi(ab+cd)+cd\,P(L),\qquad L=B^{-1}A,
\]
where \(P(L)\) is the Euclidean perimeter of \(LD\).

**2. Two scalar spectral invariants.** The squared singular values \(\lambda_1^2,\lambda_2^2\) of \(L\) have product \(s^2\) and sum
\[
T=\operatorname{tr}(L^\top L)
=\frac{a^2}{c^2}+\frac{b^2}{d^2}
+(a^2-b^2)(d^{-2}-c^{-2})\sin^2\theta
=T_0+Hu.
\]
Thus \(P(L)\) depends on \(u\) only through \(T\), while the singular-value product \(s\) stays constant.

**3. Gaussian–Laplace perimeter identity.** Let \(Z_1,Z_2\) be independent standard Gaussian variables. Polar decomposition of the Gaussian vector gives
\[
P(L)=2\sqrt{2\pi}\,\mathbb E\sqrt{\lambda_1^2 Z_1^2+\lambda_2^2 Z_2^2}.
\]
The elementary Laplace identity \(\sqrt x=(2\sqrt\pi)^{-1}\int_0^\infty(1-e^{-tx})t^{-3/2}dt\), together with Gaussian factorization,
\[
\mathbb E e^{-t(\lambda_1^2Z_1^2+\lambda_2^2Z_2^2)}
=\bigl((1+2t\lambda_1^2)(1+2t\lambda_2^2)\bigr)^{-1/2}
=\bigl(1+2tT+4s^2t^2\bigr)^{-1/2},
\]
gives the displayed exact integral. All substitutions are legitimate by Tonelli's theorem (the integrand is nonnegative). Its behavior near \(t=0\) is \(O(t^{-1/2})\) and near infinity is \(O(t^{-3/2})\).

**4. Strict derivative signs and sharpness.** For any \(k\ge1\), differentiating under the integral is valid on the compact interval \(T_0\le T\le T_0+H\): the differentiated integrand is bounded by an integrable function, behaving as \(O(t^{k-3/2})\) near zero and \(O(t^{-k-5/2})\) at infinity. Differentiation of the power \(-1/2\) yields the stated \((2k-1)!!\) formula, strictly positive because \(H>0\). In particular \(F'''(u)>0\), so the curvature \(-F''(u)\) is strictly decreasing: its minimum, attained at \(u=1\), is exactly \(m=-F''(1)\). No larger global curvature lower bound is possible. The function \(F(u)+(m/2)u^2\) is concave; its chord inequality is precisely the displayed quadratic surplus. Because \(-F''(u)>m\) for \(u<1\), the surplus is strict for \(0<u<1\). If either ellipse is circular, \(H=0\), and the exact formula shows constant area.

## Verification
A standalone Python 3 checker, `verification.py`, tests the spectral-Steiner expression against an independent support-curvature mixed-area integral and polygonal shoelace integration on the actual boundary. It also compares the Gaussian–Laplace integral with a direct ellipse perimeter integral, checks strict chord gaps and decreasing secant slopes on several scales (including high eccentricity and near disks), and checks circular degeneracies. It reports `ELLIPSE_MIXED_AREA_BERNSTEIN_PASS 214`. These finite numerical tests support, but do not substitute for, the analytic proof for all positive semiaxes and all angles.

## Relationship to prior work
Zheng and Palffy-Muhoray (2007) already report increasing excluded area as two hard ellipses rotate from parallel to perpendicular, illustrated by identical ellipses; **this qualitative monotonicity is not claimed new**. Yan and Chirikjian (2014/2015), and Chirikjian and Shiffman (2020), give closed-form descriptions and exact planar Minkowski-sum areas for arbitrary ellipses using Steiner's formula and elliptic integrals. Ruan and Chirikjian (2020) give smooth-boundary formulas; Yamada and collaborators (2024) pursue superellipsoidal approximations. The new statement concerns the *complete Bernstein derivative hierarchy in the squared-sine orientation parameter* and the *exact best strong-concavity modulus*, neither stated in these inspected treatments. The Laplace representation exposes the derivative signs without relying on numerical monotonicity plots.

## Limitations
The novelty assessment is based on the literature actually inspected and is not a priority guarantee; an equivalent inequality could exist under the labels of excluded area, elliptic-integral inequalities, or matrix means. The sharp curvature coefficient is explicit as a convergent one-dimensional integral, not an elementary constant in general. This result does not assert analogous concavity for other convex shapes or in higher dimensions. Numerical tests are finite and provide no independent mathematical certification.

## References
- X. Zheng and P. Palffy-Muhoray, *Distance of closest approach of two arbitrary hard ellipses in two dimensions*, Phys. Rev. E **75** (2007), 061709, DOI: https://doi.org/10.1103/PhysRevE.75.061709; accessible preprint https://arxiv.org/abs/0911.3420.
- Y. Yan and G. S. Chirikjian, *Closed-form characterization of the Minkowski sum and difference of two ellipsoids*, Geometriae Dedicata **177** (2015), 103–128, DOI: https://doi.org/10.1007/s10711-014-9981-3.
- G. S. Chirikjian and B. Shiffman, *Closed-Form Parametric Equation for the Minkowski Sum of m Ellipsoids in R^N and Associated Volume Bounds*, initial public arXiv version 2020-12-30, https://arxiv.org/abs/2012.15163.
- S. Ruan and G. S. Chirikjian, *Closed-Form Minkowski Sums of Convex Bodies with Smooth Positively Curved Boundaries*, initial public arXiv version 2020-12-31, https://arxiv.org/abs/2012.15461.
- R. Yamada et al., *Fast and precise approximation of Minkowski sum of two rotational ellipsoids with a superellipsoid*, The Visual Computer **40** (2024), https://doi.org/10.1007/s00371-024-03445-9.
