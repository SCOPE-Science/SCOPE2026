# Sharp conformal central derivative and quantitative rigidity for harmonic maps into ellipses

## Finding

Let \(a\ge b>0\), let \(\mathbb D\) be the open unit disk, and put
\[
 E_{a,b}=\{(x,y)\in\mathbb R^2:x^2/a^2+y^2/b^2<1\}.
\]
For \(0\le u\le1\), define the explicit one-dimensional elliptic integral
\[
 J_{a,b}(u)=\frac4\pi\int_0^{\pi/2}
 \sqrt{a^2u^2\cos^2t+b^2(1-u)^2\sin^2t}\,dt.
\]
It has a **unique minimizer** \(u_{a,b}\in(0,1)\). Put
\(L(a,b)=J_{a,b}(u_{a,b})\). Every harmonic map
\(F:\mathbb D\to E_{a,b}\) with \(F(0)=0\) and conformal differential
\(DF(0)=\lambda R\), \(\lambda\ge0\), \(R\in O(2)\), satisfies the sharp bound
\[
 \boxed{\lambda\le L(a,b)=\min_{0\le u\le1}J_{a,b}(u).}
\]
For the positive-orientation normalization \(DF(0)=\lambda I\), **equality determines
one map**: the Poisson extension \(F_*\) of the continuous boundary parametrization
\[
 g_*(t)=\frac{(a^2u_{a,b}\cos t,\ b^2(1-u_{a,b})\sin t)}
 {\sqrt{a^2u_{a,b}^2\cos^2t+b^2(1-u_{a,b})^2\sin^2t}},
 \qquad 0\le t<2\pi.
\]
The map \(F_*\) is a harmonic diffeomorphism from \(\mathbb D\) **onto**
\(E_{a,b}\). Without orientation normalization, precisely its precompositions
by orthogonal transformations of the source disk are extremal.

There is also a quantitative equality statement. If \(F\) has normalized
\(DF(0)=\lambda I\), and \(g(t)\) is its almost-everywhere radial boundary trace,
then, with normalized angular expectation
\(\mathbb E_t h=(2\pi)^{-1}\int_0^{2\pi}h(t)\,dt\),
\[
 \boxed{L(a,b)-\lambda\ \ge\ d_{a,b}\,
 \mathbb E_t\!\left[
 \frac{(g_1(t)-g_{*,1}(t))^2}{a^2}
 +\frac{(g_2(t)-g_{*,2}(t))^2}{b^2}\right],}
 \quad d_{a,b}=\min\{a u_{a,b},\ b(1-u_{a,b})\}>0.
\]
Thus the same sharp theorem quantitatively forces the entire boundary profile,
not merely the two first-order Fourier coefficients.

For noncircular ellipses, the constant obeys
\(b<L(a,b)<4b/\pi\). It has the two sharp geometric limiting laws
\[
 L(1+\varepsilon,1-\varepsilon)=1-2\varepsilon^2+O(\varepsilon^4)
 \quad(\varepsilon\to0),\qquad
 \lim_{a/b\to\infty}\frac{L(a,b)}b=\frac4\pi.
\]
At the circular case \(L(b,b)=b\), with the usual rigid disk extremizers.

## Assumptions and scope

The harmonicity of \(F=(F_1,F_2)\) means that both coordinates solve the
ordinary planar Laplace equation. No global injectivity or analyticity is
assumed. The conformal differential condition means that its two column
vectors are orthogonal and have the same norm \(\lambda\). The ellipse is
nondegenerate, centered, axis-aligned, and open. The bound includes maps
with vanishing differential, though equality never occurs in that case.
After a source-disk orthogonal precomposition, a nonzero conformal
matrix can always be changed into \(\lambda I\).

## Proof

**1. Boundary formula and dual upper bound.** Since \(E_{a,b}\) is bounded,
every coordinate of \(F\) has an almost-everywhere radial boundary trace
\(g(t)\in\overline E_{a,b}\) and is its Poisson extension. In the
normalization \(DF(0)=\lambda I\), the Poisson first-moment identities give
\[
 \lambda=2\mathbb E_t[g_1(t)\cos t]
 =2\mathbb E_t[g_2(t)\sin t].
\]
For any \(0\le u\le1\), their convex combination and the support function
of the closed ellipse give
\[
 \lambda=2\mathbb E_t\big[u g_1(t)\cos t
 +(1-u)g_2(t)\sin t\big]
 \le2\mathbb E_t\sqrt{a^2u^2\cos^2t+b^2(1-u)^2\sin^2t}
 =J_{a,b}(u).
\]
This proves the upper bound without any assumption on the higher Fourier
coefficients of \(g\).

**2. Strictly convex finite dual problem.** For each \(t\in(0,\pi/2)\),
\(u\mapsto\|(a u\cos t,b(1-u)\sin t)\|_2\) is strictly convex: the
vectors at two distinct parameters have determinant
\(ab(u-v)\cos t\sin t\ne0\). Integrating preserves strictness.
Differentiation under the integral, including one-sided differentiation at
the endpoints, gives
\[
 J'_{a,b}(0)=-\frac{4b}{\pi}<0,
 \qquad J'_{a,b}(1)=\frac{4a}{\pi}>0.
\]
Consequently the minimizer \(u_{a,b}\) exists, is unique, is interior,
and is the unique solution of
\[
 \int_0^{\pi/2}
 \frac{a^2u\cos^2t-b^2(1-u)\sin^2t}
 {\sqrt{a^2u^2\cos^2t+b^2(1-u)^2\sin^2t}}\,dt=0.
\]
Its denominator is strictly positive for all \(t\) because both
\(u\) and \(1-u\) are positive.

**3. Primal attainment and exact first jet.** For this unique minimizer,
\(g_*(t)\) lies on the ellipse boundary since
\(g_{*,1}(t)^2/a^2+g_{*,2}(t)^2/b^2=1\). Its two components have the
appropriate odd/even symmetries, so \(\mathbb E_tg_*=0\) and the
cross first Fourier moments vanish. Write
\(X=2\mathbb E_t[g_{*,1}\cos t]\) and
\(Y=2\mathbb E_t[g_{*,2}\sin t]\).
Direct differentiation of the integrand gives
\(J'_{a,b}(u_{a,b})=X-Y\), so \(X=Y\). The support-function identity
also gives \(J_{a,b}(u_{a,b})=u_{a,b}X+(1-u_{a,b})Y=X=Y\).
The Poisson extension \(F_*\) therefore has \(F_*(0)=0\) and
\(DF_*(0)=L(a,b)I\); it reaches the bound.

The numerator of \(g_*\) traces an axis-aligned ellipse with positive
semiaxes \(a^2u_{a,b}\) and \(b^2(1-u_{a,b})\). Radial normalization gives
a positively oriented homeomorphism of the source circle onto the
boundary of \(E_{a,b}\). Since this target is convex, the
Radó–Kneser–Choquet theorem makes its harmonic Poisson extension an
orientation-preserving diffeomorphism of the open disk onto the ellipse.

**4. Rigidity and stability.** Put
\(q(t)=(a u_{a,b}\cos t,b(1-u_{a,b})\sin t)\) and
\(y(t)=(g_1(t)/a,g_2(t)/b)\in\overline{\mathbb B^2}\).
Then \(y_*(t)=q(t)/\|q(t)\|\) equals the correspondingly scaled extremal
trace and, pointwise almost everywhere,
\[
 \|q\|-q\cdot y
 =\|q\|(1-y_*\cdot y)
 \ge\tfrac12\|q\|\,\|y-y_*\|^2,
\]
using \(\|y\|\le1\). On the full circle,
\(\|q(t)\|\ge d_{a,b}\). Integrating and using the Poisson expression in
Step 1 gives the asserted deficit inequality, with no unstated numerical
constant. In particular, equality forces \(g=g_*\) almost everywhere,
hence \(F=F_*\). An arbitrary conformal orientation is recovered by
precomposing with an orthogonal transformation of \(\mathbb D\).

**5. Shape limits.** At \(a=b\), symmetry and strict convexity give
\(u_{b,b}=1/2\) and \(L(b,b)=b\). If \(a>b\), increasing the first
semiaxis strictly increases \(J_{a,b}(u)\) for every \(u\in(0,1)\), hence
\(L(a,b)>b\); strict interior minimality gives
\(L(a,b)<J_{a,b}(0)=4b/\pi\).
For large \(a/b\), the inequalities
\(L(a,b)\ge4a u_{a,b}/\pi\) and
\(L(a,b)\ge4b(1-u_{a,b})/\pi\), together with
\(L(a,b)\le4b/\pi\), imply \(u_{a,b}\le b/a\to0\) and
\(L(a,b)/b\to4/\pi\).

For the near-round law, put \(a=1+\varepsilon\),
\(b=1-\varepsilon\) and \(u=1/2+\alpha\varepsilon\).
The integrand is analytic near the circular minimizer and its strict
second derivative there is positive. Taylor expansion under the integral
uniformly for bounded \(\alpha\) yields
\[
 J_{1+\varepsilon,1-\varepsilon}
 (1/2+\alpha\varepsilon)
 =1+\bigl[2\alpha+(\alpha+1/2)^2\bigr]\varepsilon^2
 +O(\varepsilon^3).
\]
The unique quadratic minimizer is \(\alpha=-3/2\), yielding coefficient
\(-2\). The implicit-function theorem supplies an analytic minimizing
branch. Interchanging the semiaxes replaces \(\varepsilon\) by
\(-\varepsilon\) and \(u\) by \(1-u\), so the optimal value is an
even analytic function. The remainder is therefore \(O(\varepsilon^4)\).

## Verification

The included `checker.py` is a standard-library numerical diagnostic. It
checks the unique convex minimizer for representative axis ratios, first
Fourier moments of the explicit boundary trace, membership on the ellipse,
pointwise support-function stability, the circular specialization, and
near-round and elongated-ellipse limits. The universal inequalities and
diffeomorphism assertion are established by the analytic proof above;
finite quadrature is not used as an infinite proof or as independent
validation.

## Relationship to prior work

Forstnerič and Kalaj (arXiv:2102.12403; published in *Analysis & PDE* 17
(2024), 981–1003) prove the sharp round-ball theorem (Theorem 1.1),
exhibit a square-target example (Example 4.2), and use a nonround ellipse
to obtain a strict qualitative bound in Example 6.3. Their inspected
statements do not give the exact semiaxis-dependent ellipse constant,
unique Poisson-boundary parametrization, or quantitative ellipse stability
shown here. Their use of Radó–Kneser–Choquet is acknowledged.

Knežević and Mateljević (arXiv:2609.19609, first submitted 17 September
2026) establish a general target-geometry/boundary-pairing framework and
sharp ball inequalities. The abstract supplies motivation and could
underlie part of the dual viewpoint; the full manuscript was not
available for inspection. Therefore the comparison with possible
unstated ellipse specializations remains a historical-priority risk,
not a claim of independent certification.

## Limitations

This is a fixed-center, axis-aligned ellipse result with a conformal
**first** differential, not a Schwarz–Pick bound for all interior
points or a theorem about harmonic maps that are conformal everywhere.
Quantitative boundary stability applies after source-orientation
normalization and measures the trace in ellipse coordinates.
No complete historical-priority or independent external audit has been
performed. The relevant 2026 primary manuscript was accessible only at
abstract level; that access gap is material to originality assessment.

## References

1. F. Forstnerič and D. Kalaj, *Schwarz–Pick lemma for harmonic maps which are conformal at a point*, arXiv:2102.12403 (first posted 24 February 2021), *Analysis & PDE* **17** (2024), 981–1003. In particular Theorem 1.1, Example 4.2, Example 6.3 and the cited Radó–Kneser–Choquet theorem.
2. M. Knežević and M. Mateljević, *Target Geometry in Prescribed-Value Schwarz Lemmas for Harmonic Maps*, arXiv:2609.19609 (first posted 17 September 2026). Abstract checked; full text unavailable during this assessment.
3. T. Radó, H. Kneser and G. Choquet, classical Radó–Kneser–Choquet theorem for harmonic extensions of boundary homeomorphisms onto convex Jordan curves (used as an established theorem).
