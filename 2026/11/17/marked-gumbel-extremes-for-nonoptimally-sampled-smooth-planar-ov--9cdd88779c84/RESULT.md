# Marked Gumbel extremes for nonoptimally sampled smooth planar ovals

## Finding

Let \(K\subset\mathbb R^2\) be a strictly convex body with a positively curved \(C^5\) boundary, parametrized counterclockwise by arclength \(s\in\mathbb R/L\mathbb Z\), and curvature \(\kappa(s)>0\). Let \(f(s)>0\) be a \(C^3\) probability density with respect to arclength. Define the *sampling-to-curvature ratio*
\[
b(s)=\frac{f(s)}{\sqrt{\kappa(s)}},\qquad \beta=\min_s b(s)>0.
\]
Assume that the set of global minima consists of distinct points \(s_1,\ldots,s_k\), all nondegenerate: \(b''(s_i)>0\). Put
\[
C=\sum_{i=1}^k f(s_i)\sqrt{\frac{2\pi\beta}{b''(s_i)}}>0,
\qquad
w_i=\frac{f(s_i)}{C}\sqrt{\frac{2\pi\beta}{b''(s_i)}}.
\]
Draw \(n\) independent boundary points with density \(f\), let \(K_n\) be their convex hull, and write \(H_n=d_H(K,K_n)\) for Euclidean Hausdorff distance. Then
\[
\boxed{n\beta\sqrt{8H_n}-\log n+\tfrac12\log\log n-\log C\ \Longrightarrow\ G,}
\]
where \(\Pr(G\le x)=\exp(-e^{-x})\) is the standard Gumbel distribution.

There is a stronger *marked* convergence. The exposed boundary arcs between consecutive sampled points each bound a cap between that arc and the inscribed chord. For each such cap, let \(h_{nj}\) be its maximal chord-normal height and \(m_{nj}\) the arclength midpoint of its boundary arc. Define the cap score
\[
z_{nj}=n\beta\sqrt{8h_{nj}}-\log n+\tfrac12\log\log n-\log C.
\]
Fix small disjoint neighborhoods of the \(s_i\). On any region where scores are bounded below, the point process of marks
\[
\Bigl(i,\sqrt{\log n}(m_{nj}-s_i),z_{nj}\Bigr)
\]
for arcs whose midpoints lie near \(s_i\) converges vaguely to a Poisson point process on \(\{1,\ldots,k\}\times\mathbb R^2\) with intensity
\[
\boxed{\lambda_i(v,z)\,dv\,dz
=\frac{f(s_i)}{C}\exp\!\left(-\frac{b''(s_i)}{2\beta}v^2\right)e^{-z}\,dv\,dz.}
\]
With probability tending to one, the uniquely worst cap lies in one of these neighborhoods. If \(I_n\) denotes its neighborhood and \(S_n\) its midpoint, then jointly with the Gumbel score,
\[
\Pr(I=i)=w_i,\qquad
\sqrt{\log n}(S_n-s_i)\mid I=i\ \Longrightarrow\ N\!\left(0,\frac{\beta}{b''(s_i)}\right),
\]
and the limiting Gumbel score is independent of the limiting marked location \((I,\sqrt{\log n}(S_n-s_I))\). All distances in the mark coordinate are signed arclength distances within a fixed local chart about a minimum.

Thus, unlike optimal curvature-weighted sampling (where \(b\) is constant), nonoptimal smooth sampling with isolated quadratic worst locations has a **negative one-half log-log centering correction** and a Gaussian spatial localization of the worst approximation error. The principal new statement is the joint *geometrically marked* Poisson limit and independent Gaussian location; the scalar centering is compatible with earlier general maximal-spacing distribution results.

## Assumptions and scope

The boundary has positive curvature everywhere and is \(C^5\). The arclength probability density is positive and \(C^3\), normalized by \(\int_0^L f(s)\,ds=1\). The function \(b=f/\sqrt\kappa\) has finitely many, and only finitely many, global minima, each with strictly positive second derivative in arclength. These hypotheses exclude the constant-ratio case and flat or degenerate minima. The number \(n\) tends to infinity while \(K\) and \(f\) remain fixed.

The primary theorem concerns planar strictly convex geometry and the Hausdorff approximation by random inscribed polygons. The marked limit is a point-process weak limit on sets bounded below in the score coordinate, not a total-variation limit of arbitrary infinite point configurations. The formula does not assert finite-sample efficiency or a rate of weak convergence.

A concrete example is the unit circle with angular density \(f(\theta)=(1+a\cos\theta)/(2\pi)\), \(0<a<1\). Here \(\beta=(1-a)/(2\pi)\), the sole minimum is \(\theta=\pi\), and
\[
C=\frac{1-a}{2\pi}\sqrt{\frac{2\pi(1-a)}a},\qquad
\sqrt{\log n}(S_n-\pi)\Longrightarrow N\!\left(0,\frac{1-a}{a}\right).
\]
On this circle, for every polygon with maximum angular gap \(g<\pi\), the exact error is \(H_n=1-\cos(g/2)\). This example provides a direct geometric test independent of numerical convex-hull algorithms.

## Proof

**Step 1: uniform cap-height expansion.** Write the arclength parametrization as \(\gamma(s)\). For an arc of length \(\ell\) from \(s\) to \(s+\ell\), the uniform Frenet expansion, valid for all \(s\), gives the normal displacement from the chord at position \(u\in[0,\ell]\):
\[
\frac12\kappa(s)u(\ell-u)+O(\ell^3).
\]
The maximal chord-normal cap height is consequently
\[
h(s,\ell)=\frac18\kappa(s)\ell^2+O(\ell^3),
\qquad
\sqrt{8h(s,\ell)}=\sqrt{\kappa(s)}\ell+O(\ell^2),
\]
uniformly around the whole curve. For sufficiently short arcs, the projection of every point of the arc onto the chord's supporting line falls inside the segment. The convex hull lies on the inward side of each chord's line, while the chord belongs to the hull. Hence the distance from a point of an exposed boundary arc to the hull equals its perpendicular distance to that chord. Distance to a convex set is convex, so its maximum over \(K\) is attained on the boundary. Therefore, whenever the maximal boundary spacing is sufficiently small,
\[
H_n=\max_j h(s_{nj},\ell_{nj}),
\]
where \(s_{nj}\) and \(\ell_{nj}\) are the starting arclength and length of the \(j\)th cyclic sampled arc.

**Step 2: exact uniformization and exponential spacings.** Define the periodic probability coordinate \(F(s)=\int_0^s f(u)\,du\pmod1\). Its sampled values are independent uniform points on the unit circle. Choose one of the sampled points as cyclic origin, with location \(U_0\) independent of the circular spacing vector. The circular spacings have the exact representation
\[
\left(\frac{E_1}{T_n},\ldots,\frac{E_n}{T_n}\right),\qquad T_n=\sum_{j=1}^n E_j,
\]
for independent mean-one exponentials \(E_j\), and this vector is independent of \(U_0\). Thus \(T_n/n=1+O_{\mathbb P}(n^{-1/2})\) and \(\max_j E_j=O_{\mathbb P}(\log n)\). Let \(s_{nj}\) be the sampled starting positions and \(s^0_{nj}=F^{-1}(U_0+(j-1)/n\pmod1)\) the shifted deterministic quantile grid. The centered partial-sum maximal inequality gives
\[
\max_j d_{\mathrm{arc}}(s_{nj},s^0_{nj})=O_{\mathbb P}(n^{-1/2}),
\]
with circular arclength distance. Taylor expansion of \(F^{-1}\) and Step 1 now show *uniformly over all gaps*
\[
\max_{1\le j\le n}\left|
\,n\beta\sqrt{8h_{nj}}-\frac{\beta}{b(s^0_{nj})}E_j\right|\xrightarrow{\mathbb P}0.
\]
Indeed, the error from the normalization \(n/T_n\) and the shifted-grid replacement is \(O_{\mathbb P}((\log n)/\sqrt n)\), and the geometric and inverse-quantile Taylor errors are \(O_{\mathbb P}((\log n)^2/n)\). The gap midpoints differ from their quantile-grid starting positions by \(O_{\mathbb P}((\log n)/n)\), which is negligible on the \((\log n)^{-1/2}\) localization scale.

**Step 3: Laplace principle for the independent weighted exponentials.** Conditionally on \(U_0\), set \(Y_{nj}=\beta E_j/b(s^0_{nj})\). They are independent, and
\[
\Pr(Y_{nj}>y)=\exp\left[-y\frac{b(s^0_{nj})}{\beta}\right].
\]
Let \(y_n(x)=\log n-\tfrac12\log\log n+\log C+x\). Uniform shifted-grid Riemann sums and the quadratic expansion
\[
\frac{b(s)}\beta=1+\frac{b''(s_i)}{2\beta}(s-s_i)^2+o((s-s_i)^2)
\]
near each isolated minimum yield, by Laplace's method,
\[
\begin{aligned}
\sum_{j=1}^n\Pr(Y_{nj}>y_n(x))
&=n\int_0^L f(s)e^{-y_n(x)b(s)/\beta}\,ds+o(1)\\
&=e^{-x}\frac{1}{C}\sum_{i=1}^k f(s_i)\sqrt{\frac{2\pi\beta}{b''(s_i)}}+o(1)\\
&\longrightarrow e^{-x}.
\end{aligned}
\]
Moreover, \(\max_j\Pr(Y_{nj}>y_n(x))=O(\sqrt{\log n}/n)\to0\). Independence and the logarithm of the product \(\prod_j(1-\Pr(Y_{nj}>y_n(x)))\) give
\[
\Pr(\max_jY_{nj}\le y_n(x))\longrightarrow\exp(-e^{-x}).
\]
Uniform score approximation in Step 2 proves the asserted Gumbel law for \(H_n\).

**Step 4: local marks.** For any fixed \(z\) and bounded interval \(B\subset\mathbb R\), restrict the exceedance sum to grid points satisfying \(\sqrt{\log n}(s^0_{nj}-s_i)\in B\). The same calculation with the substitution \(s=s_i+v/\sqrt{\log n}\) proves
\[
\sum_{j:\,\sqrt{\log n}(s^0_{nj}-s_i)\in B}\Pr(Y_{nj}>y_n(z))
\longrightarrow\frac{e^{-z}f(s_i)}{C}\int_B e^{-b''(s_i)v^2/(2\beta)}\,dv.
\]
For disjoint spatial-score test rectangles the counts are sums of independent rare indicators whose largest success probability tends to zero. The multivariate law-of-small-numbers argument (equivalently, Laplace-functional convergence) therefore yields the displayed marked Poisson process; score density is \(e^{-z}\,dz\). No competing exceedances away from the minima survive, since \(b>\beta\) on their compact complement. The maximizer of this point process is almost surely unique. Its largest score is standard Gumbel, and the factorization of the intensity into a function of position times \(e^{-z}\) proves independence of score and location and gives the stated Gaussian mixture.

## Verification

The proof is analytic. The standalone script `check_nonoptimal_hausdorff.py` checks the constant and the Laplace tail-intensity integral by independent midpoint quadrature for several large sample sizes. It also draws genuinely independent nonuniform circular points, solves the inverse angular cumulative distribution numerically, uses the *exact* circular gap-to-Hausdorff identity, and compares finite-sample score and worst-location statistics with the limits. It uses a fixed random seed and reports finite-size discrepancies instead of treating Monte Carlo as proof.

Run from the artifact directory with `python check_nonoptimal_hausdorff.py` (requires Python 3 and NumPy). Successful replay ends in `NONOPTIMAL_INSCRIBED_GUMBEL_CHECKS_OK`. The analytic proof, not the simulation, establishes the asymptotic theorem.

## Relationship to prior work

Schneider's 1988 boundary-sampling theorem and Glasauer–Schneider's 1996 Theorem 4 obtain the first-order normalized Hausdorff approximation constant for general positive boundary density. The latter's formula in dimension two is \(H_n\sim(\max_s\kappa(s)/f(s)^2)(\log n/n)^2/8\), without a centered fluctuation law or a spatial mark distribution. Brunel's 2015 preprint gives general Hausdorff deviation bounds, not a joint limit for the worst-cap location.

**A strong prior scalar result is explicitly acknowledged:** Barbe's 1992 *Limiting distribution of the maximal spacing when the density function admits a positive minimum*, as reproduced and extended in Antonik–Berred–Malov (2013), Corollary 3.1, covers the scalar maximal-spacing distribution for positive nonuniform densities. Reparametrizing the oval by \(t=\int^s\sqrt{\kappa(u)}\,du\) turns the leading cap score into a nonuniform spacing with transformed density \(b=f/\sqrt\kappa\). Applying their scalar integral and Laplace asymptotics yields the same **unmarked Gumbel correction**. Neither prior statement supplies the *joint* spatially marked cap-height point process, its explicit Gaussian mixtures, or independence between normalized cap-height excesses and their curvature-dependent locations. Consequently the marginal Gumbel law and its log-log correction are presented as essential components, **not claimed as independent discoveries**.

Sonnleitner's 2025 Theorem 1 establishes a Gumbel result in general dimensions under the *optimal* density \(f\propto\sqrt\kappa\), while leaving nonoptimal densities outside its theorem. Hüsler's 1988 paper studies the different case of a density vanishing at its minimum. The exact proof here uses classical exponential-gap couplings, but combines them with the convex cap geometry and spatially marked Laplace principle to identify the limiting *position and height together*. The claimed new contribution is **only** this marked geometric limit and its Gaussian localization for the isolated nondegenerate minimum regime, not the already established scalar nonuniform-spacing limit. No result for higher dimensions or flat minima is asserted.

## Limitations

The theorem does not cover higher-dimensional hypersurfaces, optimal density, vanishing densities, degenerate minima, nonsmooth or zero-curvature boundaries, or a density that changes with \(n\). It is a weak limit, not a quantitative finite-sample confidence guarantee. The unmarked nonuniform-spacing law is already covered by earlier general maximal-spacing results; the asserted new contribution is the curvature-sensitive Gaussian spatial marking, which still has possible priority risk from incompletely accessible older literature. Empirical checks cannot certify the general theorem.

## References

1. R. Schneider, *Random approximation of convex sets*, Journal of Microscopy 151 (1988), 211–227. DOI: https://doi.org/10.1111/j.1365-2818.1988.tb04682.x.
2. S. Glasauer and R. Schneider, *Asymptotic approximation of smooth convex bodies by polytopes*, Forum Mathematicum 8 (1996), 363–378; original full text https://www.tha.de/~glasauer/publ/glasschn.pdf ; publisher https://doi.org/10.1515/form.1996.8.363 (electronic posting dated 2009-12-11).
3. V.-E. Brunel, *Uniform Behaviors of Random Polytopes under the Hausdorff Metric*, arXiv:1503.01504, first submitted 2015-03-05; https://arxiv.org/abs/1503.01504.
4. M. Sonnleitner, *A limit theorem for Hausdorff approximation by random inscribed polytopes*, arXiv:2508.16442, first submitted 2025-08-22; https://arxiv.org/abs/2508.16442.
5. J. Hüsler, *Maximal, non-uniform spacings and the coverage problem*, Journal of Applied Probability 25 (1988), 519–528; https://doi.org/10.2307/3213981.
6. P. Barbe, *Limiting distribution of the maximal spacing when the density function admits a positive minimum*, Statistics & Probability Letters 14 (1992), 53–60; https://doi.org/10.1016/0167-7152(92)90210-V.
7. A. Antonik, A. Berred, S. Malov, *Coverage Problem Revisited*, arXiv:1306.5069, first submitted 2013-06-21; full text https://arxiv.org/pdf/1306.5069, especially Theorem 3.2 and Corollary 3.1.
8. P. Deheuvels, *Strong limit theorems for maximal spacings from a general univariate distribution*, Annals of Probability 12 (1984), 1181–1193; https://doi.org/10.1214/aop/1176993147.
