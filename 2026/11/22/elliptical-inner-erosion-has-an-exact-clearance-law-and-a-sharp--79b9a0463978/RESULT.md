# Elliptical inner erosion has an exact clearance law and a sharp seven-halves cusp

## Finding

Let \(a>b>0\) and let \(E=\{(x,y)\in\mathbb R^2:x^2/a^2+y^2/b^2\le1\}\). For area-uniform \(Z\in E\), put \(D=\operatorname{dist}(Z,\partial E)\). Define
\[
h(\theta)=\sqrt{a^2\cos^2\theta+b^2\sin^2\theta},\qquad
\rho(\theta)=\frac{a^2b^2}{h(\theta)^3},\qquad t_*=\frac{b^2}{a}.
\]
For \(0\le t\le t_*\), put \(\theta_t=0\). For \(t_*<t<b\), put
\[
\theta_t=\arccos\!\left(\frac{b\sqrt{b^2-t^2}}{t\sqrt{a^2-b^2}}\right).
\]
Then the **entire clearance survival law** is
\[
\Pr(D\ge t)=\frac{2}{\pi ab}\int_{\theta_t}^{\pi/2}
\bigl(h(\theta)-t\bigr)\bigl(\rho(\theta)-t\bigr)\,d\theta,
\qquad 0\le t<b,
\]
with \(\Pr(D\ge b)=0\) and \(\Pr(D\ge t)=0\) for \(t>b\).

Write \(A_t=\pi ab\Pr(D\ge t)\) and let \(P=4\int_0^{\pi/2}\rho(\theta)\,d\theta\) be the ellipse perimeter. Below the curvature threshold, the exact inward Steiner polynomial holds:
\[
A_t=\pi ab-Pt+\pi t^2\qquad(0\le t\le t_*).
\]
At the threshold the area has the **positive fractional-power correction**
\[
\boxed{A_t=\pi ab-Pt+\pi t^2+C_{a,b}(t-t_*)^{7/2}
+O_{a,b}((t-t_*)^{9/2})\quad(t\downarrow t_*\text{ from above}),}
\]
where
\[
\boxed{C_{a,b}=\frac{16}{105}\left(\frac{2a^3}{b^2(a^2-b^2)}\right)^{3/2}>0.}
\]
In particular \(t\mapsto A_t\) is three times continuously differentiable but not four times differentiable at \(t_*\). The clearance law determines the unordered semiaxis lengths uniquely: its right endpoint is \(b\), and the first strict departure from its quadratic initial formula is \(t_*=b^2/a\), hence \(a=b^2/t_*\). For a disk \(a=b=R\), the separate formula is \(\Pr(D\ge t)=(1-t/R)^2\) for \(0\le t\le R\), with no interior phase transition.

## Assumptions and scope

Distance is Euclidean and \(Z\) is uniform with respect to two-dimensional Lebesgue area, not boundary arclength. The body \(E_t=E\ominus tB_2\) is the set of centers of radius-\(t\) disks wholly contained in \(E\); equivalently it is \(\{z\in E:\operatorname{dist}(z,\partial E)\ge t\}\). The law concerns every \(t\in[0,b]\), where \(b\) is the inradius. The threshold \(t_*\in(0,b)\) exists only for genuinely unequal semiaxes. Error terms hold for each fixed \(a>b>0\) as \(t-t_*\downarrow0\), not uniformly near circularity.

## Proof

**1. Half-plane geometry.** For the unit normal \(n_\theta=(\cos\theta,\sin\theta)\), the support of the original ellipse is \(h(\theta)\). Disk containment is equivalent to the exact intersection of supporting half-planes
\[
E_t=\bigcap_{\theta\in[0,2\pi)}
\bigl\{z:z\cdot n_\theta\le h(\theta)-t\bigr\}.
\]
The smooth normal-angle curvature radius satisfies \(h+h''=\rho\). Put \(g_t=h-t\). When \(t\le b^2/a\), its curvature distribution is nonnegative everywhere (\(\min\rho=b^2/a\)); thus \(g_t\) itself is the eroded body's support function. Its enclosed area, by the support-parameter area identity, is \(\frac12\int g_t(g_t+g_t'')\,d\theta=\pi ab-Pt+\pi t^2\).

When \(t_*<t<b\), restrict to \(0\le\theta<\pi/2\). The positive horizontal intercept \(X_t\) of \(E_t\) is the minimum of \((h(\theta)-t)/\cos\theta\). Differentiation gives the sign of the derivative as the sign of \(b^2/h(\theta)-t\). Since \(b^2/h\) rises strictly from \(b^2/a\) to \(b\), the unique minimum occurs at \(\theta=\theta_t\), satisfying \(h(\theta_t)=b^2/t\); solving yields the formula above and
\[
X_t=\frac{\sqrt{a^2-b^2}}{b}\sqrt{b^2-t^2}.
\]
The function \(s_t(\theta)\), equal to \(X_t\cos\theta\) on \(|\theta|\le\theta_t\), to \(h(\theta)-t\) on \(\theta_t\le|\theta|\le\pi/2\), and extended with the two axial symmetries, is a genuine convex support function. Indeed the two pieces join with matching value and first derivative because the intercept minimization is stationary; \(s_t+s_t''=0\) on each axial vertex normal cone and \(\rho-t\ge0\) on the remaining smooth arcs. The latter follows from the monotonicity of \(\rho\) from \(0\) to \(\pi/2\) and \(\rho(\theta_t)=a^2t^3/b^4\ge t\).

Moreover \(s_t\le g_t\) for all normals. Thus its convex body lies in the half-plane intersection. On non-axial normals the body meets the constraint \(g_t\). For an axial-cone normal, its expression is a nonnegative linear combination of the normals at \(\pm\theta_t\); adding those two active inequalities bounds any point in \(E_t\) by the vertex support \(X_t\cos\theta\). The support of the half-plane intersection is therefore exactly \(s_t\), not the self-intersecting formal inward normal offset. Hence its boundary consists of the retained inward-offset arcs and exactly two nonsmooth axial vertices.

**2. Exact area and perimeter.** The planar support-area identity remains valid for this piecewise \(C^1\) convex support function (distributionally there is no first-derivative jump). The axial normal-cone portions contribute zero because \(s_t+s_t''=0\). By symmetry,
\[
A_t=2\int_{\theta_t}^{\pi/2}(h-t)(\rho-t)\,d\theta,
\qquad P_t=4\int_{\theta_t}^{\pi/2}(\rho-t)\,d\theta.
\]
These are valid for all \(0\le t<b\), interpreting \(\theta_t=0\) below threshold. As \(t\uparrow b\), \(\theta_t\uparrow\pi/2\) and the body contracts to its single incenter. The uniform-area survival law is \(A_t/(\pi ab)\).

**3. Sharp fractional singularity.** Set
\[
q=1-b^2/a^2,\qquad \alpha=\frac{b^2q}{2a}>0,\qquad
\delta=t-t_*.
\]
The contact condition \(t=b^2/h(\theta_t)\) and curvature radius expansions at \(\theta=0\) give, with \(u=\theta_t\),
\[
\delta=\alpha u^2+\beta u^4+O(u^6),\quad
\rho(\theta)=t_*+3\alpha\theta^2+\gamma\theta^4+O(\theta^6),
\]
where
\[
\beta=\frac{b^2}{a}\left(\frac{3q^2}{8}-\frac q6\right),\qquad
\gamma=\frac{b^2}{a}\left(\frac{15q^2}{8}-\frac q2\right),\qquad
\frac{\gamma}{5}-\beta=\frac{2\alpha}{15}.
\]
Subtraction of the formal full-normal perimeter \(P-2\pi t\) yields
\[
P_t-(P-2\pi t)=-4\int_0^u(\rho(\theta)-t)\,d\theta
=-\frac{8}{15}\alpha^{-3/2}\delta^{5/2}+O(\delta^{7/2}).
\]
Here the quadratic-order contribution cancels exactly because \(\rho=t_*+3\alpha\theta^2+\cdots\) and \(t=t_*+\alpha u^2+\cdots\). The elementary first-variation identity \(A_t'=-P_t\) for disk erosions, or direct differentiation of the displayed area integral with its contact endpoint, integrates this last equation from \(t_*\):
\[
A_t-(\pi ab-Pt+\pi t^2)=\frac{16}{105}\alpha^{-3/2}\delta^{7/2}+O(\delta^{9/2}).
\]
Since the contact equation is analytic in \(u^2\) with nonzero linear coefficient \(lpha\), the local perimeter and area expansions are convergent Puiseux series in \(\delta^{1/2}\). Thus the displayed leading correction also establishes the exact differentiability threshold.

**4. Inverse statement.** The support of the clearance distribution is \([0,b]\). The initial quadratic extrapolation from a neighborhood of zero is unique, and its first point of strict failure is \(b^2/a\) by the positive correction at that point and the exact formula for all smaller erosion radii. These two distributional landmarks recover \(b\) and \(a\). A disk is characterized within ellipses by the absence of an interior failure point.

## Verification

The accompanying standalone `checker.py` uses high-precision quadrature of the analytic area and perimeter formulas and, independently, the planar convex hull of a high-resolution intersection of **all discrete supporting half-planes**. This second computation automatically discards redundant normals after the transition. For a noncircular example with \((a,b)=(2,1)\), the two areas agree to approximately \(2\times10^{-6}\) at five erosion radii on both sides of the threshold. At four decreasing positive increments, the normalized nonpolynomial correction converges to \(1.87684658936564058\ldots\), as predicted. Finite numerical checks are diagnostics and do not replace the all-parameter analytic proof. Reproduce with `python checker.py` using Python, NumPy, SciPy and mpmath.

## Relationship to prior work

Banchoff and Giblin, *On the Geometry of Piecewise Circular Curves* (1994), discuss the development of cusps in formal inward ellipse offset curves and their evolutes; their full text does not state this **true convex erosion** area formula or the noninteger \(7/2\) onset in the clearance distribution. Larson, *A bound for the perimeter of inner parallel bodies* (first public arXiv 2015), studies general sharp perimeter bounds and explains why inner Steiner formulas fail beyond regularity thresholds; his complete accessible revised text does not specify the elliptical distribution or its local coefficient. Standard published ellipse-offset formulas describe formal offsets, which self-intersect and cannot be substituted for the boundary of \(E_t\) after \(t_*\). The novelty claim is limited to the combined exact convex-erosion distribution, explicit coefficient, and inverse identification; the offset-cusp fact and Steiner theory are not claimed as new.

## Limitations

The result is specific to noncircular Euclidean ellipses in the plane and Lebesgue-area-uniform sampling. It does not supply corresponding analytic formulas for general smooth convex ovals or triaxial ellipsoids, finite-sample inference rates, or uniform error bounds in the limit \(a\downarrow b\). The \(7/2\) singularity is distinct from the cusps of the formal inward normal curve. Historical priority remains subject to specialized offset-curve and mathematical-morphology literature; no independent mathematical audit has been performed.

## References

- T. Banchoff and P. Giblin, “On the Geometry of Piecewise Circular Curves,” *American Mathematical Monthly* **101** (1994), 403–416, DOI: `10.1080/00029890.1994.11996965`. Full available copy: https://www-fourier.univ-grenoble-alpes.fr/~marin/une_autre_crypto/articles_et_extraits_livres/Banchoff_T._Giblin_P.-On_the_geometry_of_piecewise_circular_curves.pdf .
- S. Larson, “A bound for the perimeter of inner parallel bodies,” arXiv:1508.06414 (first public August 26, 2015), revised corrected version: https://arxiv.org/html/1508.06414v3 .
- E. W. Weisstein, “Ellipse Parallel Curves,” *MathWorld*: https://mathworld.wolfram.com/EllipseParallelCurves.html .
