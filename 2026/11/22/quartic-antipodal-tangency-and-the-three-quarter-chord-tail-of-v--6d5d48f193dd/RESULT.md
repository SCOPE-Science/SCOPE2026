# Quartic antipodal tangency and the three-quarter chord tail of Viviani's curve

## Finding

**General spherical-curve theorem.** Let \(\Gamma\) be a compact, closed, \(C^3\) regular immersed curve, counted with its arclength multiplicity, contained in the Euclidean sphere of radius \(R>0\) centered at the origin. Suppose there is exactly one unordered pair of distinct curve parameters whose position vectors are antipodal. Suppose the tangent lines at those parameters are parallel. Choose local *signed arclength* parametrizations \(X(s)\) and \(Y(t)\) at the two points with
\[
X(0)=P,\quad Y(0)=-P,\quad X'(0)=T,\quad Y'(0)=-T,\quad \|T\|=1.
\]
Let \(a=\|X''(0)+Y''(0)\|/2>0\), and let \(L>0\) be the entire arclength of \(\Gamma\), counted with multiplicity. Independently choose \(X_1,X_2\) from normalized arclength measure on \(\Gamma\), and set \(D=\|X_1-X_2\|\). Then, as \(\varepsilon\downarrow0\),
\[
\Pr(2R-D\leq\varepsilon)
\sim \frac{2\,\mathrm B(1/4,3/2)}{L^2\sqrt a}
(4R\varepsilon)^{3/4}.
\tag{1}
\]
Here \(\mathrm B\) denotes the Euler beta function. The two possible ordered endpoint arrangements each have asymptotic conditional probability \(1/2\). Conditional on the arrangement with first point near \(P\) and second near \(-P\), write their signed arclength offsets as \(s,t\) and put \(w=s-t\). Then
\[
\left(\frac{\sqrt a\,s}{(4R\varepsilon)^{1/4}},
\frac{w}{(4R\varepsilon)^{1/2}}\right)
\ \Big|\ \{2R-D\leq\varepsilon\}
\quad\Longrightarrow\quad
\operatorname{Unif}\{(x,y)\in\mathbb R^2:x^4+y^2\leq1\}.
\tag{2}
\]
In particular the fourth power of the first limiting coordinate has the \(\operatorname{Beta}(1/4,3/2)\) law, and, given that coordinate, the second is uniform over the indicated vertical section.

**Viviani specialization.** For any \(r>0\), the classical figure-eight curve of intersection of the sphere \(x^2+y^2+z^2=4r^2\) and the cylinder \((x-r)^2+y^2=r^2\) is parametrized, once with arclength multiplicity, by
\[
V_r(\theta)=r(1+\cos\theta,\sin\theta,2\sin(\theta/2)),
\qquad 0\leq\theta<4\pi.
\]
Its Euclidean diameter is \(4r\), attained only by the pair \(V_r(\pi),V_r(3\pi)\). For two independent normalized-arclength points on this curve,
\[
\boxed{\displaystyle
\Pr(4r-D\leq\varepsilon)
\sim C_{\mathrm V}(\varepsilon/r)^{3/4},\qquad
C_{\mathrm V}=\frac{8^{3/4}\,\mathrm B(1/4,3/2)}{32\,E(-1)^2}
=0.14244157343155045\ldots,}
\tag{3}
\]
where \(E(-1)=\int_0^{\pi/2}\sqrt{1+\sin^2 t}\,dt\) is a complete elliptic integral of the second kind in the parameter convention. If the first angular parameter is \(\pi+u\) and the second is \(3\pi+v\), then conditional on this ordered arrangement the pair
\[
\left(\frac{u}{(8\varepsilon/r)^{1/4}},
\frac{u+v}{(8\varepsilon/r)^{1/2}}\right)
\]
converges in distribution to the same uniform quartic-ellipse law.

## Assumptions and scope

The curve may be immersed and self-intersecting, but both endpoint samples are by **one-dimensional Euclidean arclength**, with multiplicities of regular parametrized branches. Antipodality means opposite points relative to the sphere center. A unique unordered antipodal *parameter* pair is required, not merely a unique geometric pair when multiple branches coincide. The curvature-vector sum is computed after choosing opposite unit tangents. Equation (1) applies for each fixed curve and radius under the nonzero \(a\) assumption; it does not claim uniformity when a curve deforms toward \(a=0\).

## Proof

1. **Global maximum and localization.** The sphere identity
\[
\|X-Y\|^2+\|X+Y\|^2=4R^2
\]
shows \(D\leq2R\), with equality precisely at antipodal pairs. By compactness and the assumed unique pair, every pair with \(2R-D\) sufficiently small belongs to one of two disjoint ordered neighborhoods of that pair. There are no omitted maximizing configurations.

2. **Quartic normal form.** In a neighborhood with points written as \(X(s)\) and \(Y(t)\), put \(w=s-t\). Taylor expansion in signed arclength yields
\[
X(s)+Y(s-w)=Tw+As^2+O(|s|^3+|sw|+w^2),
\qquad A=\frac{X''(0)+Y''(0)}2.
\]
Since signed arclength gives \(T\perp X''(0),Y''(0)\), one has \(T\perp A\) and \(\|A\|=a\). Thus
\[
\|X(s)+Y(s-w)\|^2
=w^2+a^2s^4+o(w^2+s^4)
\tag{4}
\]
uniformly as \((s,w)\to(0,0)\). To justify the relative remainder, note that the tangential and normal components of the leading terms are orthogonal, so their combined norm is bounded below by a positive multiple of \(|w|+s^2\); the displayed Taylor remainder is \(o(|w|+s^2)\).

3. **Probability measure and constant.** The event \(2R-D\leq\varepsilon\) is exactly
\[
\|X+Y\|^2\leq4R\varepsilon-\varepsilon^2.
\]
Equation (4) localizes the set to \(s=O(\varepsilon^{1/4})\), \(w=O(\varepsilon^{1/2})\). Its normalized indicator converges almost everywhere, and after localization is dominated on a fixed compact set. The Jacobian from \((s,t)\) to \((s,w)\) is one. Rescaling \(x=\sqrt a\,s/(4R\varepsilon)^{1/4}\) and \(y=w/(4R\varepsilon)^{1/2}\) gives area scaling \((4R\varepsilon)^{3/4}/\sqrt a\). The exact limiting area is
\[
\int_{-1}^{1}2\sqrt{1-x^4}\,dx
=\mathrm B(1/4,3/2).
\]
Dividing by \(L^2\) and accounting for the two ordered neighborhoods proves (1). The same dominated-convergence argument with bounded continuous test functions proves (2) and the equal orientation weights.

4. **Viviani geometry and normalization.** Direct substitution gives \(\|V_r(\theta)\|=2r\) and \((x-r)^2+y^2=r^2\). Because \(x=r(1+\cos\theta)\geq0\), an antipodal pair must have both \(x=0\); the only parameters are \(\pi,3\pi\), giving \((0,0,2r)\) and \((0,0,-2r)\). The speed is \(r\sqrt{1+\cos^2(\theta/2)}\), hence
\[
L_r=\int_0^{4\pi}\|V_r'(\theta)\|\,d\theta=8rE(-1).
\]
Both tangents are parallel and nonzero. With the second signed arclength orientation reversed, their curvature vectors are
\[
X''(0)=\frac1r(1,0,-1/2),\qquad
Y''(0)=\frac1r(1,0,1/2),
\]
so \(a=1/r\). Substituting \(R=2r\), \(a=1/r\), and \(L=8rE(-1)\) into (1) proves (3) and the displayed angular marking.

## Verification

`CHECK.py` is a standalone Python-standard-library diagnostic. It independently evaluates the exact sum-of-antipodal-points identity
\[
\|V_1(\pi+u)+V_1(3\pi+v)\|^2
=4(1-\cos d)^2+4(1+\cos d)(1-\cos m),
\quad d=(u-v)/2,\ m=(u+v)/2,
\]
checks the sphere and speed normalization, and quadratures the exact small-deficit region with its arclength Jacobian. Its reported ratios of finite-deficit probability to the leading term at \(\varepsilon=10^{-2},10^{-3},10^{-4},10^{-5}\) are respectively approximately \(1.04140033444,1.01252434095,1.00390365284,1.00122875006\). All 120 deterministic assertions passed. Numerical checks support, but do not prove, the asymptotic theorem.

## Relationship to prior work

Classical descriptions supply Viviani's sphere–cylinder intersection, its parametrization and elliptic arclength; these are not claimed as new. Graefe–Korsch–Strzys (arXiv:1308.3569, first public August 16, 2013) analyze generalized Viviani intersections and their spherical areas for Bose–Hubbard dynamics, not the distribution of independently sampled Euclidean chord lengths. Deng and collaborators (2025) analyze Frenet invariants and related Smarandache curves, not diametral pair laws. The novel mathematical target here is the sharp quartic-antipodal probability constant and its marked limit, with an explicit general spherical-curve mechanism. Related published work on invariant chords of convex bodies uses a different sampling measure and a nondegenerate diameter geometry.

## Limitations

The exponent \(3/4\) requires a unique antipodal pair, parallel tangents and nonzero quadratic curvature-vector sum. Multiple pairs, transverse tangents, vanishing curvature sum, nonuniform endpoint distributions and nonspherical ambient curves are not included. No convergence rate or complete chord-distance CDF is claimed. Historical priority beyond the inspected sources remains provisional. The numerical checker supplies finite diagnostics only, not a proof of the infinite asymptotic.

## References

- E.-M. Graefe, H. J. Korsch and M. P. Strzys, *Bose-Hubbard dimers, Viviani's windows and pendulum dynamics*, arXiv:1308.3569 (first submitted August 16, 2013), especially Section 2.1 (curve and pole geometry) and Section 2.2 (enclosed spherical areas). https://arxiv.org/abs/1308.3569
- E. W. Weisstein, *Viviani's Curve*, MathWorld, including the historical parametrization and complete elliptic arclength; references A. Gray, *Modern Differential Geometry of Curves and Surfaces with Mathematica*, 2nd ed. (1997), pp. 201–202. https://mathworld.wolfram.com/VivianisCurve.html
- Y. Deng, Y. Li, S. Şenyurt, D. Canlı and İ. Gürler, *On the Special Viviani's Curve and Its Corresponding Smarandache Curves*, Mathematics 13 (2025), 1526, https://doi.org/10.3390/math13091526 (curve Frenet geometry rather than chord statistics).
