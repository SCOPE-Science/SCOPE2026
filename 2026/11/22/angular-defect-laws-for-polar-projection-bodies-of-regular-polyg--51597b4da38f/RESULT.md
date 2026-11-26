# Two optimal polar-projection fits for regular polygons

## Finding

Let \(K_N\) be the centered regular \(N\)-gon of circumradius one, with \(4\mid N\). Let \(\Pi K_N\) be its projection body and \(K_N^\circ\) its polar. Two standard ways to fit the polar to the projection body by scaling are to minimize the angular squared support-function error or the Hausdorff distance. They give **different** optimal scales, even for these highly symmetric bodies.

Put \(\alpha=\pi/N\), \(s=\sin\alpha\), and \(c=\cos\alpha\); abbreviate the two supports on the unit circle by \(p=h_{\Pi K_N}\) and \(q=h_{K_N^\circ}\). The unique minimizers over \(\lambda>0\) and the associated errors are
\[
\begin{aligned}
\lambda_2&=\frac{2c(s+\alpha c)}{\alpha+sc},
&E_N&=\min_{\lambda>0}\int_0^{2\pi}(p-\lambda q)^2\,d\theta
=\frac{4Ns^2(\alpha^2-s^2)}{\alpha+sc},\\
\lambda_\infty&=2c>\lambda_2,
&H_N&=\min_{\lambda>0}d_H(\Pi K_N,\lambda K_N^\circ)=2(1-c).
\end{aligned}
\]
The relative squared error is \(E_N/\int_0^{2\pi}p^2\,d\theta=s^2(\alpha^2-s^2)/(\alpha+sc)^2\). Along multiples of four,
\[
E_N=\frac{2\pi^5}{3N^4}+O(N^{-6}),\qquad
\sqrt{E_N/\textstyle\int_0^{2\pi}p^2\,d\theta}=\frac{\pi^2}{2\sqrt3 N^2}+O(N^{-4}),\qquad
H_N=\frac{\pi^2}{N^2}+O(N^{-4}).
\]
For comparison, when \(N\equiv2\pmod4\) the known exact parity branch gives \(\Pi K_N=2c K_N^\circ\); both fits then have zero error and the same scale.

## Assumptions and scope

Here \(N\ge4\), the metric is Euclidean, angular measure is unnormalized \(d\theta\), and \(h_{\Pi K}(u)=\operatorname{length}(\operatorname{proj}_{u^\perp} K)\) for \(\|u\|=1\). The polar is \(\{y:x\cdot y\le1\text{ for all }x\in K\}\). Only positive homotheties about the origin are fitted; there is no optimization over rotations, translations or general linear maps.

## Proof

Central symmetry makes a projection length twice the perpendicular support, so \(\Pi K_N\) is twice a quarter-turn of \(K_N\). The polar has circumradius \(1/c\) and its vertices are offset by \(\alpha\) from those of \(K_N\). For \(N\equiv2\pmod4\) the quarter-turn is a half vertex step modulo a symmetry, giving the known exact fit. For \(4\mid N\) it is a symmetry. Write \(u\in[0,\alpha]\) for the unsigned distance to a nearest vertex in the angular variable; then
\[
p=2\cos u,\qquad q=c^{-1}\cos(\alpha-u).
\]
There are \(2N\) such half-sectors. Integration uses
\(\int_0^\alpha\cos^2u\,du=(\alpha+sc)/2\) and
\(\int_0^\alpha\cos u\cos(\alpha-u)\,du=(s+\alpha c)/2\). Thus
\[
A=\int p^2=4N(\alpha+sc),\quad B=\int q^2=N(\alpha+sc)/c^2,\quad C=\int pq=2N(s+\alpha c)/c.
\]
The strictly convex quadratic \(A-2\lambda C+\lambda^2B\) is minimized at the positive scale \(C/B\); the error is \(A-C^2/B\). Use
\((\alpha+sc)^2-(s+\alpha c)^2=s^2(\alpha^2-s^2)\) for both stated error formulas. The scale inequality is strict because \((\alpha+sc)-(s+\alpha c)=(1-c)(\alpha-s)>0\).

For compact convex bodies, the Hausdorff distance equals the uniform norm of the support-function difference on the unit circle. At \(\lambda=2c\) the difference is \(2\cos u-2\cos(\alpha-u)\), decreasing from \(2(1-c)\) to \(-2(1-c)\). For smaller scales the vertex-direction error \(2-\lambda\) is larger than \(2(1-c)\); for larger scales the edge-normal error has magnitude \(\lambda/c-2c>2(1-c)\). This proves uniqueness in the uniform norm. Finally use \(\alpha^2-s^2=\alpha^4/3+O(\alpha^6)\), \(\alpha+sc=2\alpha+O(\alpha^3)\), and \(1-c=\alpha^2/2+O(\alpha^4)\) for the asymptotics.

## Verification

The accompanying standalone `verify_polar_defect.py` checks the fit formulas by support evaluation on a finite angular grid, using vertex extrema and shadow lengths. It does not prove the all-order or all-direction assertions.

## Relationship to prior work and limitations

The exact parity branch is established background in planar Radon geometry. Also, the prior *Exact translative convex-hull profile of every regular polygon* gives the pointwise product \(4\rho_K(u)h_K(u^\perp)\) in its equations (6)–(9). For these centered symmetric polygons this is twice \(p(u)/q(u)\), by polarity and the width formula. In particular the ratio range and angular probability laws obtained by transforming that profile are not claimed here. The contribution is the explicit comparison of two fit criteria: the prior directional profile does not evaluate the weighted squared fit or establish that it chooses a different scale from the Hausdorff fit. This is a bounded literature comparison, not a priority guarantee. Neither the norms nor the constants assert affine invariance, a stability theorem for general bodies, or a result for rotated fits.

## References

1. *Exact translative convex-hull profile of every regular polygon*, 11 October 2026, [published mathematical record](https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-translative-convex-hull-profile-of-every-regular-polygon--79b005afe9c0/RESULT.md), equations (6)–(9).
2. K. Mandal, D. Sain, K. Paul, *A Geometric Characterization of Polygonal Radon Planes*, Journal of Convex Analysis 26 (2019), 1113–1123; [arXiv:1809.04760](https://arxiv.org/abs/1809.04760), Theorem 2.8 and Remark 2.1.
3. H. Martini, *Convex polytopes whose projection bodies and difference sets are polars*, Discrete & Computational Geometry 6 (1991), 83–91, [doi:10.1007/BF02574676](https://doi.org/10.1007/BF02574676), abstract and §4.
4. Y. Zhang, *A solution to Petty's polar projection problem*, [arXiv:2611.17926v1](https://arxiv.org/html/2611.17926v1), Remark 3.1 (hexagon).
