# Independent speed factors, a complete circumradius law and two caustics for ellipse-inscribed triangles

## Finding

Fix a noncircular Euclidean ellipse with semiaxes \(a>b>0\). Choose three independent eccentric anomalies \(\Theta_j\) uniformly on \([0,2\pi)\), and let \(\mathcal R\) be the ordinary Euclidean circumradius of the triangle with vertices \(P_j=(a\cos\Theta_j,b\sin\Theta_j)\). This is **uniform eccentric-anomaly (equiaffine) sampling**, not Euclidean-arclength sampling. Put \(d=a^2-b^2\) and
\[
q(t)=\sqrt{b^2+d\sin^2t}.
\]

**Exact independent-product law.** For three *independent* \(T_j\sim\operatorname{Unif}[0,\pi)\),
\[
\boxed{\mathcal R\ \stackrel{\mathrm d}=\ \frac{q(T_1)q(T_2)q(T_3)}{ab}.}
\]
The distribution is absolutely continuous with positive density on exactly \((b^2/a,a^2/b)\), has no atoms, and has no mass outside the closed interval. More precisely, if
\[
g(x)=\frac{2e^{2x}}{\pi\sqrt{(e^{2x}-b^2)(a^2-e^{2x})}}\,\mathbf1_{\{\log b<x<\log a\}},
\]
then its complete density, at all regular values, is the threefold logarithmic convolution
\[
\boxed{p_{\mathcal R}(r)=\frac{1}{r}\,(g*g*g)(\log(ab r)).}
\]
This determines the full cumulative distribution by integration; convolution is on the real line. For every real \(s\), with \(k^2=1-b^2/a^2\),
\[
\boxed{\mathbb E[\mathcal R^s]=\left(\frac{a^2}{b}\right)^s
\left[{}_2F_1\!\left(-\frac s2,\frac12;1;k^2\right)\right]^3.}
\]
For the complete elliptic integral \(E(k)=\int_0^{\pi/2}\sqrt{1-k^2\sin^2u}\,du\), examples are
\[
\mathbb E[\mathcal R]=\frac{8a^2}{\pi^3b}E(k)^3,
\qquad \mathbb E[\mathcal R^2]=\frac{(a^2+b^2)^3}{8a^2b^2}.
\]

**Exactly two interior square-root caustics.** The smooth extension of the circumradius to the full angular torus has exactly two interior critical values, \(b\) and \(a\). Its critical configurations have coincident vertices; the circumradius restricted to triangles with distinct vertices has no critical points. The radius density extends continuously to \(b\) and \(a\), and, as \(h\downarrow0\),
\[
\boxed{\begin{aligned}
p_{\mathcal R}(b-h)&=p_{\mathcal R}(b)-\frac{12\sqrt2\,a\sqrt b}{\pi^2d^{3/2}}\sqrt h+O_{a,b}(h),\\
p_{\mathcal R}(b+h)&=p_{\mathcal R}(b)+O_{a,b}(h),\\
p_{\mathcal R}(a+h)&=p_{\mathcal R}(a)-\frac{12\sqrt2\,b\sqrt a}{\pi^2d^{3/2}}\sqrt h+O_{a,b}(h),\\
p_{\mathcal R}(a-h)&=p_{\mathcal R}(a)+O_{a,b}(h).
\end{aligned}}
\]
Thus these are one-sided square-root cusps of the full density, not atoms. The endpoint probabilities have the corresponding sharp three-halves-power behavior:
\[
\boxed{\begin{aligned}
\Pr(\mathcal R<b^2/a+h)&\sim\frac4{3\pi^2}\left(\frac{2a}{d}\right)^{3/2}h^{3/2},\\
\Pr(\mathcal R>a^2/b-h)&\sim\frac4{3\pi^2}\left(\frac{2b}{d}\right)^{3/2}h^{3/2}.
\end{aligned}}
\]
The extrema themselves and their ordinary local quadratic character are not asserted to be new separately.

**Exact log-radius tomography.** Write \(\rho=(a-b)/(a+b)\) and \(\operatorname{Li}_2(z)=\sum_{n\ge1}z^n/n^2\). Then
\[
\boxed{L:=\mathbb E[\log\mathcal R]=3\log\frac{a+b}{2}-\log(ab),\qquad
V:=\operatorname{Var}(\log\mathcal R)=\frac32\operatorname{Li}_2(\rho^2).}
\]
The statistic \(V\) increases strictly from \(0\) to the unattained limit \(\pi^2/4\) as the axis ratio grows from one to infinity. Consequently **the two population statistics \((L,V)\) reconstruct both semiaxes**, up to their ordering: determine the unique \(\rho\in[0,1)\) from \(\operatorname{Li}_2(\rho^2)=2V/3\), let \(m=e^L(1-\rho^2)\), and recover \(a=m(1+\rho)\), \(b=m(1-\rho)\). This includes a circle by continuity, where the radius law is a point mass.

## Assumptions and scope

The ellipse is nondegenerate and noncircular unless the explicitly mentioned circle limit is used. The ambient metric is Euclidean. Repeated vertices have probability zero, and the circumradius is well-defined almost surely; no assertion concerns the ambiguous circumcircle of a degenerate triangle. Directions \(\Theta_j\) are independent and uniformly sampled in eccentric anomaly, equivalently equiaffine arclength on this fixed ellipse. In the caustic expansions \(a,b\) are held fixed and positive while \(h\) tends to zero; no uniform estimate as \(a\) approaches \(b\) is asserted. All probability densities use ordinary one-dimensional Lebesgue measure in the radius variable.

## Proof

**1. Exact circumradius identity.** For distinct parameters \(\theta_i,\theta_j\), the chord formula is
\[
|P_i-P_j|=2\left|\sin\frac{\theta_i-\theta_j}{2}\right|q\left(\frac{\theta_i+\theta_j}{2}\right).
\]
The affine area scaling from the unit circle to the ellipse gives the unsigned triangle area
\[
\Delta=2ab\prod_{i<j}\left|\sin\frac{\theta_i-\theta_j}{2}\right|.
\]
Applying the standard circumradius identity \(\mathcal R=|P_1-P_2|\,|P_2-P_3|\,|P_3-P_1|/(4\Delta)\) cancels the three sine factors and proves, pointwise outside null degeneracies,
\[
\mathcal R=\frac1{ab}\prod_{i<j}q\left(\frac{\theta_i+\theta_j}{2}\right).
\]

The right-hand side is smooth on the full angular torus, giving the unique continuous extension of the radius as a function of the parameters. This does not assign a circumcircle to a degenerate triangle.

**2. The nontrivial independence.** On the three-dimensional angular torus, the integer-linear map
\[
(\theta_1,\theta_2,\theta_3)\longmapsto
(\theta_1+\theta_2,\theta_2+\theta_3,\theta_3+\theta_1)\pmod{2\pi}
\]
has determinant \(2\). It is therefore a surjective finite covering of compact groups and pushes normalized Haar measure to normalized Haar measure. Haar measure on the target three-torus is the product of three uniform angle measures. Hence the three pairwise half-sums modulo \(\pi\) are **jointly independent uniforms**, even though each uses two of the same three original angles. This proves the displayed independent-product law.

**3. Full density and Mellin moments.** Because \(\sin^2T\) has the arcsine density \(1/(\pi\sqrt{v(1-v)})\) on \((0,1)\), the positive speed \(U=q(T)\) has density
\[
f_U(u)=\frac{2u}{\pi\sqrt{(u^2-b^2)(a^2-u^2)}}\,\mathbf1_{\{b<u<a\}}.
\]
Changing to \(\log U\) yields \(g\); the sum of three independent log speeds minus \(\log(ab)\) yields the stated multiplicative-convolution density. Its support is the closure of the open product range, positivity holds at every regular interior radius, and every individual speed distribution is atomless. The integral
\[
\frac1\pi\int_0^\pi q(t)^s\,dt
=a^s\,{}_2F_1\!\left(-\frac s2,\frac12;1;1-\frac{b^2}{a^2}\right)
\]
is the Euler beta-integral representation of the Gauss hypergeometric function. Independence gives the exact radius moments. The first moment uses \(\int_0^\pi q(t)\,dt=2aE(k)\); the second uses \(\mathbb E[q(T)^2]=(a^2+b^2)/2\).

**4. Critical-value census and both caustics.** Regard the product \(F(t_1,t_2,t_3)=q(t_1)q(t_2)q(t_3)/(ab)\) as a smooth function on \((\mathbb R/\pi\mathbb Z)^3\). Since \(q'\) vanishes exactly at \(t=0,\pi/2\) modulo \(\pi\), its eight isolated critical points have exactly four critical values: \(b^2/a\) (one minimum), \(b\) (three saddles of Morse index one), \(a\) (three saddles of Morse index two), and \(a^2/b\) (one maximum). Every Hessian is nondegenerate because \(a>b\). The half-sum map is a local diffeomorphism. At each critical point at least two half-sums agree modulo \(\pi\), which forces the two original angles not common to those half-sums to agree modulo \(2\pi\). Thus all critical points of the extended angular map are excluded from the distinct-vertex domain. Omitting that null set does not change the pushforward distribution.

At a saddle of value \(b\), translate the local torus coordinates to that saddle, with the coordinate corresponding to \(q=a\) first. Taylor expansion gives
\[
F=b-Ax^2+B(y^2+z^2)+O(\|(x,y,z)\|^4),\quad
A=\frac{bd}{2a^2},\quad B=\frac d{2b}.
\]
Choose Morse coordinates with identity derivative at the saddle, so the quadratic form is exact, and use a smooth cutoff supported in the chart, equal to one near the saddle. In polar coordinates in \((y,z)\), put \(w=B(y^2+z^2)\). After integration in \(w\), the local pushforward at \(s=r-b\) is \(\pi/B\) times the integral over \(x\) with \(s+Ax^2\ge0\) of the angularly averaged cutoff times Jacobian, evaluated at \((x,w)=(x,s+Ax^2)\). The angular average is smooth in \(w\ge0\) up to zero (Taylor expansion cancels each odd radial power), equals one at \((0,0)\), and can be extended smoothly across \(w=0\). Integrating the extension over all \(x\) gives a smooth function of \(s\) near zero. For \(s<0\) the removed interval \(|x|<\sqrt{-s/A}\) has integrand \(1+O(|x|+|s|)\), so the leading nonsmooth term, up to \(O(|s|)\), is
\[
-\frac{2\pi}{B\sqrt A}\sqrt{(-s)_+}.
\]
The angular density in the product torus is \(\pi^{-3}\), and there are three disjoint congruent saddles at \(b\). The complementary cutoff gives a regular-value pushforward with smooth density near \(b\). Thus the total coefficient at \(b\) is \(6/(\pi^2B\sqrt A)=12\sqrt2a\sqrt b/(\pi^2d^{3/2})\), with the loss occurring for \(r<b\). At a saddle of value \(a\), the signs reverse and
\[
F=a+Ax^2-B(y^2+z^2)+O(\|(x,y,z)\|^4),\quad
A=\frac{ad}{2b^2},\quad B=\frac d{2a}.
\]
The missing central interval now occurs for \(r>a\), giving the coefficient \(12\sqrt2b\sqrt a/(\pi^2d^{3/2})\). This proves all four one-sided density expansions, including finiteness and continuity at the critical values. There are no other critical values at which a caustic could occur.

At the unique minimum in pair-sum torus coordinates,
\[
F=\frac{b^2}{a}+\frac d{2a}(t_1^2+t_2^2+t_3^2)+O(\|t\|^4).
\]
The uniform torus density \(\pi^{-3}\) times the volume \(4\pi(2ah/d)^{3/2}/3\) of the corresponding small Euclidean ball gives the lower endpoint constant. At the unique maximum \(F=a^2/b\), the quadratic deficit is \(\frac d{2b}\sum(t_j-\pi/2)^2\), giving the upper endpoint constant. Standard bounded-coordinate localization and dominated convergence make these genuine three-dimensional probability asymptotics, not numerical extrapolations.

**5. Log moments and inversion.** Set \(m=(a+b)/2\) and \(\rho=(a-b)/(a+b)\). The elementary identity
\[
q(t)=m|1-\rho e^{2it}|
\]
provides the absolutely convergent Fourier series, for \(0\le\rho<1\),
\[
\log q(t)=\log m-\sum_{n=1}^{\infty}\frac{\rho^n}{n}\cos(2nt).
\]
Uniform-angle orthogonality gives \(\mathbb E\log q(T)=\log m\) and \(\operatorname{Var}(\log q(T))=\frac12\operatorname{Li}_2(\rho^2)\). Summing three independent copies and subtracting \(\log(ab)\) gives \(L,V\). Positive series coefficients make \(\operatorname{Li}_2(\rho^2)\) strictly increasing for \(\rho>0\). Its limit is \(\pi^2/6\), and \(ab=m^2(1-\rho^2)\), so the stated unique inverse reconstruction follows.

## Verification

Run `python3 verify_circumradius.py` with Python 3.10 or later, standard library only. The checker reconstructs circumradii directly from the three vertices using chord lengths and Euclidean triangle area and compares them with the independent-product identity. It tests all four critical values and local Hessian coefficients, two exact population radius moments, independent numerical quadrature of the log moments against the dilogarithm series, exact inversion of semiaxes from those log moments, and seeded Monte Carlo cross-checks over four ellipse shapes. The packaged checker printed `ALL_CHECKS_PASSED 1845` in the recorded execution. This finite reproducibility check is supplementary; the proof above establishes the infinite identities, cusp expansions, and inverse uniqueness.

## Relationship to prior work

Classical ellipse and triangle-center geometry supplies chord formulas and circumradius identities. Garcia's 2016 paper and Romaskevich's 2013 preprint examine **one-parameter triangular billiard orbits**, rather than three independent equiaffine-uniform ellipse points. A published full circumcenter distribution for the *same* independent-sampling model identifies an astroid-supported **two-dimensional marginal** of the circumcenter and its cusp neighborhoods. That marginal is not the circumradius law: for instance, for a centered noncircular ellipse, different centered circles of radii throughout \((b,a)\) each intersect the ellipse in four points, and each supplies inscribed triangles with the *same* circumcenter but different circumradii. Thus that circumcenter marginal does not determine the product-factorization distribution or its two interior density caustics; its existing sharp cusp localization is credited as closely related background rather than repackaged as an original contribution. Published results on the same sampling model concerning **acute-triangle probabilities** and **Delaunay diagonal choices** also do not determine circumradius moments or its density. Known circle, chord, and general beta-integral formulas are not claimed as new.

The compared contribution is the exact *three-independent-speed factorization* of an ellipse triangle's circumradius, the full Mellin/convolution law with exactly two interior caustics and their coefficients, and the invertible log-radius moment pair. Historical priority remains provisional; older conic-probability and special-function literature may contain a differently expressed version of the factorization or some corollaries.

## Limitations

There is no assertion of a new classical extremal curvature radius, a new uniform circle law, or novelty in the standalone Fourier/dilogarithm identity. These results do not apply to Euclidean-arclength-uniform boundary sampling, dependent billiard triples, interior-uniform samples, or general convex curves. The one-dimensional density is supplied by an exact convolution, not a claimed elementary closed form at every radius. The caustic expansions are for fixed noncircular semiaxes; they are not uniform in the near-circular degeneration. Population log moments determine axes without sampling-error bounds; historical uniqueness and independent validation remain open.

## References

1. Ronaldo A. Garcia, *Centers of inscribed circles in triangular orbits of an elliptic billiard*, arXiv:1607.00179v1, initially public July 1, 2016, primary MSC 51M04. https://arxiv.org/abs/1607.00179 .
2. Olga Romaskevich, *On the incenters of triangular orbits in elliptic billiard*, arXiv:1304.7588, initially public April 29, 2013. https://arxiv.org/abs/1304.7588 .
3. *The universal astroid law and sharp cusp scaling of random ellipse circumcenters*, Resultary (2026), https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-the-universal-astroid-law-and-sharp-cusp-scaling-of-random-ellip--d371bd320795/RESULT.md .
4. *An aspect-ratio-invariant Delaunay fan for points sampled on ellipses*, Resultary record b6c235a8e49b (2026).
5. *Sharp dilogarithmic acuteness law for affine-uniform ellipse triangles*, Resultary record a5911e351b92 (2026).
6. Eric W. Weisstein, *Ellipse*, Wolfram MathWorld, reference for classical ellipse geometry: https://mathworld.wolfram.com/Ellipse.html .
