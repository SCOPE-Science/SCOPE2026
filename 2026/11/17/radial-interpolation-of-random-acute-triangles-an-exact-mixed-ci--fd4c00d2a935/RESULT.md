# Radial interpolation of random acute triangles: an exact mixed-circle law and a cusp at the center

## Finding
Let \(A\) and \(B\) be independent points uniformly distributed by arclength on the unit circle, and fix \(C=(r,0)\) with \(0\le r\le1\). Let \(p(r)\) be the probability that the Euclidean triangle \(ABC\) has three strictly acute angles. Define, for \(0\le r\le1\),
\[
J(r)=\int_0^{\pi/2}\frac{r\cos t\,\arcsin(r\cos t)}{\sqrt{1-r^2\sin^2t}}\,dt,
\]
where the value at \(r=1\) is the continuous improper-integral value. Then the **exact radial law** is
\[
\boxed{\displaystyle p(r)=\frac12-\frac2{\pi^2}\bigl(\operatorname{Li}_2(r)-\operatorname{Li}_2(-r)\bigr)+\frac2{\pi^2}J(r).}
\]
In particular, \(p(0)=1/2\), \(p(1)=1/4\), and the centered response has the expansion
\[
\boxed{\displaystyle p(r)=\frac12-\frac4{\pi^2}r+\frac{r^2}{2\pi}-\frac4{9\pi^2}r^3+\frac{r^4}{8\pi}+O(r^5)\quad(r\downarrow0).}
\]
Equivalently, as a function of the interior point \(C\in\mathbb R^2\), this acute-triangle probability has a radial **linear cusp** at the center and is not differentiable there.

The decomposition by the location of the unique obtuse angle is also exact. For \(0\le r\le1\),
\[
\begin{aligned}
\Pr(\angle A>\pi/2)=\Pr(\angle B>\pi/2)&=\frac{\operatorname{Li}_2(r)-\operatorname{Li}_2(-r)}{\pi^2},\\
\Pr(\angle C>\pi/2)&=\frac12-\frac{2J(r)}{\pi^2}.
\end{aligned}
\]
The first probability is strictly increasing on \((0,1)\); the second is strictly decreasing. Thus movement of the pinned vertex redistributes the location of obtuseness, with the first-order effect at the center entirely due to angles at the randomly sampled boundary vertices.

## Assumptions and scope
The two random vertices are independent and **arclength-uniform on the same unit circle**; the third is fixed, not sampled uniformly in the disk. By rotation invariance only its radius \(r\) matters. Coincident or collinear configurations and right angles have probability zero; defining all three angles strictly acute therefore entails no endpoint ambiguity. \(\operatorname{Li}_2\) denotes the standard real dilogarithm \(\sum_{k\ge1}z^k/k^2\) for \(|z|\le1\). The expansion is for a fixed outer-circle radius and \(r\downarrow0\), not a large-sample limit.

## Proof
**1. Disjoint obtuseness events.** A nondegenerate Euclidean triangle has at most one angle greater than \(\pi/2\). Since the three right-angle events have probability zero, \(p(r)=1-2q_A(r)-q_C(r)\), where \(q_A\) and \(q_C\) are the respective obtuse-angle probabilities.

**2. Obtuseness at a boundary vertex.** Write \(A=(\cos\alpha,\sin\alpha)\), with \(\alpha\) uniform on \([0,2\pi)\). The condition \((B-A)\cdot(C-A)<0\) cuts from the unit circle an arc of angular length
\[
2\arctan\!\left(\frac{r|\sin\alpha|}{1-r\cos\alpha}\right)
\]
for \(0\le r<1\). Conditional on \(\alpha\), the probability is this length divided by \(2\pi\). Reflecting about the horizontal axis gives
\[
q_A(r)=\frac1{\pi^2}\int_0^\pi\arg(1-r e^{-i\alpha})\,d\alpha,
\]
where the argument is taken positive on \((0,\pi)\). More explicitly it is \(\arctan(r\sin\alpha/(1-r\cos\alpha))\). The uniformly convergent Fourier series for \(r<1\),
\[
\arg(1-r e^{-i\alpha})=\sum_{k\ge1}\frac{r^k\sin(k\alpha)}k,
\]
gives, after termwise integration,
\[
q_A(r)=\frac2{\pi^2}\sum_{j\ge0}\frac{r^{2j+1}}{(2j+1)^2}
=\frac{\operatorname{Li}_2(r)-\operatorname{Li}_2(-r)}{\pi^2}.
\]
Continuity gives \(q_A(1)=1/4\). Every term of the power series is positive, proving strict increase.

**3. Visual-angle density at the pinned point.** Parameterize the ray from \(C\) at angle \(\phi\) as \(C+\rho e^{i\phi}\). Its outward circle intersection has
\[
\rho=\sqrt{1-r^2\sin^2\phi}-r\cos\phi.
\]
If the intersection point has usual polar angle \(\theta\), direct differentiation gives
\[
\frac{d\theta}{d\phi}=
1-\frac{r\cos\phi}{\sqrt{1-r^2\sin^2\phi}}.
\]
Thus the directions from \(C\) toward \(A\) and \(B\) are independent with density
\[
f_r(\phi)=\frac{1-h_r'(\phi)}{2\pi},\qquad h_r(\phi)=\arcsin(r\sin\phi).
\]
This holds for \(r<1\); its almost-everywhere limit supplies the endpoint \(r=1\).

**4. Obtuseness at the pinned vertex.** Two rays enclose an obtuse angle precisely when their angular difference modulo \(2\pi\) lies in \((\pi/2,3\pi/2)\). Put \(K(u)=\mathbf1_{(\pi/2,3\pi/2)}(u\bmod 2\pi)\). Then
\[
q_C(r)=\int_0^{2\pi}\!\int_0^{2\pi}f_r(\phi)f_r(\psi)K(\phi-\psi)\,d\phi\,d\psi.
\]
The linear terms in \(h_r'\) vanish because \(\int_0^{2\pi}h_r'=0\), and the constant term is \(1/2\). Integrating the remaining product twice by parts (or first smoothing the step function \(K\) and passing to the limit) yields the exact identity
\[
\int\!\int h_r'(\phi)h_r'(\psi)K(\phi-\psi)\,d\phi\,d\psi
=-2\int_0^{2\pi}h_r'(t)h_r(t+\pi/2)\,dt=-8J(r).
\]
Indeed \(h_r(t+\pi/2)=\arcsin(r\cos t)\), and its product with \(h_r'(t)\) has four equal positive quadrant integrals. Hence \(q_C(r)=1/2-2J(r)/\pi^2\). The integrand in \(J\) increases strictly in \(r\in(0,1)\) for almost every \(t\in(0,\pi/2)\); thus \(q_C\) strictly decreases.

**5. Endpoint values and the small-radius expansion.** At \(r=0\), both \(q_A\) and \(J\) vanish. As \(r\uparrow1\), dominated convergence follows from
\[
0\le\frac{r\cos t}{\sqrt{1-r^2\sin^2t}}\le1,
\]
so \(J(1)=\int_0^{\pi/2}(\pi/2-t)dt=\pi^2/8\). Also \(\operatorname{Li}_2(1)-\operatorname{Li}_2(-1)=\pi^2/4\). These give \(p(1)=1/4\). For \(r\) near zero, uniform Taylor expansion on the compact integration interval gives
\[
J(r)=\frac\pi4r^2+\frac\pi{16}r^4+O(r^6).
\]
The odd-dilogarithm identity expands as \(\operatorname{Li}_2(r)-\operatorname{Li}_2(-r)=2r+2r^3/9+O(r^5)\). Substitution proves the stated expansion. Since \(p(C)=p(|C|)\) and \(p'(0+)=-4/\pi^2\ne0\), the map from planar target position \(C\) to probability has no derivative at the origin.

## Verification
The included `check.py` independently integrates the angle-at-\(C\) event using the quadratic inequality in the sum and difference of boundary angles, and independently integrates the boundary-vertex obtuseness event using a chord-arc formula. It also evaluates the original acute-angle inequalities on a Cartesian product grid and checks the fifth-order residual of the small-radius series. Running `python check.py` with Python 3, NumPy and SciPy prints `RADIAL_PINNED_TRIANGLE_FORMULA_AND_EXPANSION_OK`. Numerical quadrature and grid tests support, but do not replace, the analytic proof.

## Relationship to prior work
The classical \(1/4\) all-circle acuteness probability and the general random-triangle models discussed by Edelman and Strang are not claimed as new. Their Gaussian-coordinate/shape-space model does not imply a mixed distribution with two circle-boundary vertices and one pinned interior vertex. Hall's 1982 calculation uses three volume-uniform points in a ball and likewise does not directly evaluate this mixed conditional law. A publicly available 2015 full-text discussion of the three-boundary-point model establishes only the \(r=1\) endpoint. The present claim concerns the entire radial interpolation, the split among the three possible obtuse-angle locations, and its non-smooth centered response.

## Limitations
No formula is claimed for three independently area-uniform points, arbitrary noncircular supports, or other distributions of the pinned point. Strict monotonicity of the *total* function \(p(r)\) is not asserted. Historical novelty remains provisional, particularly relative to non-indexed geometric-probability literature. No independent mathematical audit was conducted.

## References
- A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053 (public submission January 9, 2015), especially Sections 1 and 3.3. https://arxiv.org/abs/1501.03053
- G. R. Hall, *Acute Triangles in the \(n\)-Ball*, Journal of Applied Probability 19 (1982), 712–715. https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/acute-triangles-in-the-nball/4EAAF3C4F8653033C210E089E11E6800
- Mathematics Stack Exchange, *Probability of triangle to be acute?*, April 24–25, 2015, https://math.stackexchange.com/questions/1250394/probability-of-triangle-to-be-acute
