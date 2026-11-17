# Positive second-order endpoint corrections for areas and perimeters of random cyclic polygons

## Finding

Fix an integer \(n\ge3\). Choose \(n\) independent uniform points on the Euclidean unit circle, arrange them in counterclockwise order, and let \(P\) and \(A\) be the perimeter and ordinary nonnegative area of their inscribed convex polygon. Write
\[
 P_*=2n\sin(\pi/n),\qquad A_*=(n/2)\sin(2\pi/n),\qquad d=n-1.
\]
For each \(X\in\{P,A\}\), put \(t_P=\pi/n\), \(t_A=2\pi/n\), \(k_P=1\), \(k_A=4\), and
\[
 C_X=\frac{(n-1)!}{\sqrt n\,\Gamma((n+1)/2)\,[\pi\sin t_X]^{d/2}},\qquad
 B_X=k_X\left[\frac{d(n-2)\cos^2 t_X}{12n(n+1)\sin^3 t_X}+\frac{d^2}{8n(n+1)\sin t_X}\right].
\]
Then for either choice of \(X\), **at fixed \(n\)** and as \(\varepsilon\downarrow0\),
\[
 \Pr(X_*-X<\varepsilon)
 =C_X\varepsilon^{d/2}\left(1+B_X\varepsilon+O_n(\varepsilon^2)\right).
\]
The established leading coefficients \(C_X\) are included for normalization and comparison. **The claim of new mathematical content is the explicit first nonzero relative correction \(B_X\) for both observables, its strict positivity for every \(n\), and its differing geometric growth**:
\[
 B_P\sim\frac{n^3}{12\pi^3},\qquad
 B_A\sim\frac{n^3}{24\pi^3}\qquad(n\to\infty).
\]
In particular, the correction for perimeter and area is different even at the same polygon order. For \(n=3\), \(B_A=4B_P\); for large \(n\) their ratio tends to \(1/2\). The displayed large-\(n\) behavior concerns the **coefficients** of fixed-\(n\) expansions, and does not assert an expansion uniform in \(n\).

## Assumptions and scope

Samples are independent and uniform in angle (equivalently, normalized arclength) on the unit circle. The probability is over one polygon with exactly \(n\) sampled vertices, **not** over the largest or smallest perimeter among polygons selected from a growing cloud. Events using \(<\) and \(\le\) have the same probability because the deficit has no atoms near zero. The \(O_n\) constant may depend on \(n\). For fixed \(n\), positive \(\varepsilon\) is taken sufficiently small.

Let \(\Delta_1,\ldots,\Delta_n>0\) be the consecutive cyclic angular spacings. They sum to \(2\pi\), and their joint density relative to \(d\Delta_1\cdots d\Delta_{n-1}\) is \((n-1)!/(2\pi)^{n-1}\). Put \(x_i=\Delta_i-2\pi/n\). Thus \(x=(x_i)\) lies in the Euclidean hyperplane \(H=\{x:\sum_i x_i=0\}\) of dimension \(d\). The perimeter and area are exactly
\[
 P=2\sum_i\sin(\Delta_i/2),\qquad A=\frac12\sum_i\sin\Delta_i.
\]

## Proof

**1. Unique maximizers and localization.** Strict concavity of \(\sin(\Delta/2)\) on \((0,2\pi)\) implies \(P\le P_*\), with equality only at all-equal spacings. For area, if all spacings are at most \(\pi\), Jensen's inequality for \(\sin\) on \([0,\pi]\) gives \(A\le A_*\), uniquely at equal spacings. If a spacing exceeds \(\pi\), its sine is negative and the other \(n-1\) spacings sum to less than \(\pi\), giving \(2A<(n-1)\sin(\pi/(n-1))<n\sin(2\pi/n)\) (directly for \(n=3\), and using the bound \((n-1)\sin(\pi/(n-1))<\pi< n\sin(2\pi/n)\) for \(n\ge4\)). Thus the area maximum is also uniquely the regular polygon. By compactness of the closed spacing simplex, small deficits are confined to an arbitrarily small neighborhood of \(x=0\).

**2. The local deficit and a common quadratic normalization.** Set \(s=\sin t_X>0\), \(c=\cos t_X\). In either case Taylor expansion, using \(\sum_i x_i=0\), gives
\[
 D_X:=X_*-X=a\sum_i x_i^2+b\sum_i x_i^3+c_4\sum_i x_i^4+O_n(\|x\|^5),
\qquad a=s/4.
\]
For perimeter \((b,c_4)=(c/24,-s/192)\), while for area \((b,c_4)=(c/12,-s/48)\). In particular the Hessian on \(H\) is strictly positive, so the small-deficit set is a smoothly star-shaped neighborhood of zero.

**3. Analytic radial boundary.** Write \(x=\sqrt{\varepsilon/a}\,ru\), where \(u\) ranges over the Euclidean unit sphere \(S_H\) of \(H\). With \(\delta=\sqrt\varepsilon\), the equation \(D_X=\varepsilon\) is
\[
 r^2+\delta B r^3S_3(u)+\delta^2 C r^4S_4(u)+O_n(\delta^3)=1,
 \quad B=b/a^{3/2},\quad C=c_4/a^2,\quad S_j(u)=\sum_i u_i^j.
\]
Its radial solution is analytic in \(\delta\) uniformly over \(S_H\) by the implicit-function theorem, because the radial derivative at \((r,\delta)=(1,0)\) equals \(2\). Expanding yields
\[
 r=1-\frac{B}{2}S_3\delta+\left(\frac58B^2S_3^2-\frac C2S_4\right)\delta^2+O_n(\delta^3).
\]
The radial volume factor \(r^d\), averaged over \(S_H\), therefore equals
\[
 1+\delta^2\left[\frac{d(d+4)}8 B^2\mathbb E S_3(U)^2
 -\frac d2 C\mathbb E S_4(U)\right]+O_n(\delta^4).
\]
The improvement from a potential \(O(\delta^3)\) remainder to \(O(\delta^4)\) is exact: replacing \(\delta\) by \(-\delta\) corresponds to reversing \(u\), so the integrated analytic volume is even in \(\delta\). This also rules out all half-integer relative terms.

**4. Explicit angular moments.** Let \(Q=I-\mathbf1\mathbf1^{\mathsf T}/n\) be the orthogonal projector onto \(H\), and \(U\) uniform on its unit sphere. The spherical fourth- and sixth-moment contraction formulas, with covariance projector \(Q\), give
\[
 \mathbb E\sum_i U_i^4=\frac{3(n-1)}{n(n+1)},\qquad
 \mathbb E\left(\sum_i U_i^3\right)^2=\frac{6(n-2)}{n(n+1)(n+3)}.
\]
For clarity, \(Q_{ii}=(n-1)/n\) and \(Q_{ij}=-1/n\) when \(i\ne j\). The fourth moment equals \(\sum_i3Q_{ii}^2/[d(d+2)]\). The sixth moment equals \(\sum_{ij}(9Q_{ii}Q_{jj}Q_{ij}+6Q_{ij}^3)/[d(d+2)(d+4)]\); direct summation gives the second displayed identity. Thus there is no unverified infinite-dimensional step.

Substitution into the radial expression gives
\[
 \frac{3d(n-2)b^2}{4n(n+1)a^3}
 -\frac{3d^2c_4}{2n(n+1)a^2}.
\]
In the perimeter case \(b^2/a^3=\cos^2t/(9\sin^3t)\), \(c_4/a^2=-1/(12\sin t)\); in the area case both ratios are four times as large. This yields precisely \(B_X\) above.

**5. Probability normalization and further consequences.** The probability density on the coordinate simplex is \(d!/(2\pi)^d\). Because the projection of the Euclidean hyperplane volume onto the first \(d\) coordinates has factor \(1/\sqrt n\), the leading probability of \(\sum_i x_i^2<4\varepsilon/s\) is
\[
 \frac{d!}{(2\pi)^d\sqrt n}\,
 \frac{\pi^{d/2}}{\Gamma(d/2+1)}\left(\frac{4\varepsilon}{s}\right)^{d/2}
 =C_X\varepsilon^{d/2}.
\]
The radial expansion establishes the stated two-term probability law. Both summands in \(B_X\) are nonnegative and the quartic summand is strictly positive. Finally, \(\sin(\pi/n)\sim\pi/n\), \(\sin(2\pi/n)\sim2\pi/n\) prove the displayed distinct cubic growth rates.

As an ancillary leading-order geometric consequence (not independently claimed as new), conditional on \(D_X<\varepsilon\) the scaled spacing vector \(\sqrt{\sin t_X}\,x/(2\sqrt\varepsilon)\in H\) converges in total variation to normalized volume on the unit ball of \(H\). Its squared radius, and therefore \(D_X/\varepsilon\), has limiting distribution \(\operatorname{Beta}(d/2,1)\). This follows directly from convergence in volume of the sublevel domains, not from simulation.

## Verification

An executable self-contained geometric/numerical checker, `checker.py`, recomputes \(C_X\) and \(B_X\) for \(n=3,4\), parameterizes the spherical directions in \(H\), solves the **exact** sine-defined deficit equation along each direction by numerical bisection, integrates the actual radial volume, and compares it to the proved two-term expression. It covers both observables, three threshold values each, and checks that the error falls as the threshold shrinks. For example, for \(n=4\) and perimeter deficit \(0.02\), exact quadrature is approximately \(0.00193231737345\) versus \(0.00193230039205\) from the two-term expression; for area deficit \(0.01\), exact quadrature is approximately \(0.000406199175391\) versus \(0.000406196625222\). These finite tests support but do not establish the asymptotics. The proof above supplies the infinite-parameter statements for each fixed \(n\).

## Relationship to prior work

Koroleva and Nikitin (arXiv:1301.1360, first posted 2013-01-07), in their Lemmas 2.1 and 2.3, **already prove the leading fixed-polygon endpoint constants** for both perimeter and area, and apply them to U-max statistics. In particular the \(C_X\) displayed here agrees with their exact first-order coefficients. Their ellipsoid squeeze and cubic-error estimates give only the leading limit and do not supply the integrated quartic and squared-cubic corrections. The mathematically new assertion assessed here is the explicit, strictly positive \(B_X\) term with the stated \(O_n(\varepsilon^2)\) remainder and its difference between the two observables, not the previously known first-order power or constant.

Bélisle (2011) studied the same random cyclic polygons in the distinct \(n\to\infty\) Gaussian/mean regime; the full text was inaccessible and this comparison is limited to bibliographic abstracts and subsequent accessible works. Xu, Meng and Li (2019) were inspected throughout: their full-text statements concern almost-sure \(n\to\infty\) convergence, expected deficits, and extrapolation. They do not give a fixed-\(n\) second-order endpoint volume law. Wang and Xu (2018) extend the asymptotic-\(n\) analysis to Dirichlet gaps; only the abstract was accessible, so remaining full-text priority risk is acknowledged. These works may provide useful techniques but their inspected theorems do not subsume the correction given above.

## Limitations

This is an asymptotic for **each fixed polygon order**; no uniform-in-\(n\) expansion or second-order approximation to the distribution of a maximum over many polygons is established. The new coefficient is computed from local geometry and does not imply that the original leading endpoint theorem is new. Independent mathematical and historical review has not been performed. The two inaccessible full texts cited above create residual historical-priority uncertainty; searches and the accessible leading-order source do not constitute proof of absolute novelty.

## References

1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1 (2013-01-07), https://arxiv.org/abs/1301.1360. Relevant Lemmas 2.1 and 2.3, proofs in Sections 2.1–2.2.
2. W. Lao and M. Mayer, *U-max-statistics*, Journal of Multivariate Analysis **99** (2008), 2039–2052, https://doi.org/10.1016/j.jmva.2008.02.001. Relevant Section 6 and Lemma 6.2 for triangle perimeters.
3. C. Bélisle, *On the polygon generated by n random points on a circle*, Statistics & Probability Letters **81** (2011), 236–242, https://doi.org/10.1016/j.spl.2010.11.012.
4. W.-Q. Xu, L. Meng, and Y. Li, *Random Polygons and Estimations of π*, Open Mathematics **17** (2019), 575–581, https://doi.org/10.1515/math-2019-0049. Full open text inspected.
5. S. Wang and W.-Q. Xu, *Random cyclic polygons from Dirichlet distributions and approximations of π*, Statistics & Probability Letters **140** (2018), 84–90, https://doi.org/10.1016/j.spl.2018.05.007.
