# The clearance distribution of spherical lunes and its hemispherical critical law

## Finding

Let \(d\ge3\) be an integer. In the unit sphere \(S^{d-1}\subset\mathbb R^d\), let \(L_\alpha\) be the closed spherical lune whose two bounding great hemispheres have longitude \(0\) and \(\alpha\), where \(0<\alpha\le\pi\). At \(\alpha=\pi\) the lune is the limiting hemisphere. Sample \(X\) uniformly by spherical surface measure from \(L_\alpha\), and set \(D_\alpha=\operatorname{dist}_{S^{d-1}}(X,\partial L_\alpha)\), the geodesic clearance from its boundary. Define \(a=\alpha/2\) and \(k=(d-2)/2>0\).

**Complete law.** There are independent random variables \(U\sim\operatorname{Unif}[0,a]\) and \(Q\sim\operatorname{Beta}(1,k)\) such that
\[
\sin D_\alpha\ \overset{d}{=}\ \sqrt Q\sin U.
\]
Consequently, for \(0\le t<a\),
\[
\Pr(D_\alpha>t)=\frac2\alpha\int_t^a\left(1-\frac{\sin^2t}{\sin^2u}\right)^k\,du,
\]
and the survival probability is zero for \(t\ge a\). For every real \(s\ge0\),
\[
\mathbb E[(\sin D_\alpha)^s]
=\frac{\Gamma(d/2)\Gamma(1+s/2)}{\Gamma((d+s)/2)}\,
\frac{B_{\sin^2a}((s+1)/2,1/2)}{\alpha},
\]
where \(B_z\) is the unregularized incomplete beta integral. In particular,
\[
\mathbb E[\sin^2 D_\alpha]=\frac1d\left(1-\frac{\sin\alpha}{\alpha}\right).
\]
This single moment uniquely determines \(\alpha\) when \(d\) is known. Moreover, if \(0<\alpha_1<\alpha_2\le\pi\), the two clearances can be coupled so that \(D_{\alpha_1}<D_{\alpha_2}\) almost surely; hence their laws are strictly stochastically ordered.

**Two sharp endpoint phases.** As \(t\downarrow0\),
\[
\Pr(D_\alpha\le t)\sim\frac{2\sqrt\pi\,\Gamma(d/2)}{\alpha\,\Gamma((d-1)/2)}t.
\]
For every fixed \(0<\alpha<\pi\), as \(\varepsilon\downarrow0\),
\[
\Pr(D_\alpha>a-\varepsilon)\sim
\frac4{\alpha d}\left(2\cot a\right)^k\varepsilon^{d/2}.
\]
At the exactly hemispherical endpoint \(\alpha=\pi\), the exponent changes:
\[
\Pr(D_\pi>\pi/2-\varepsilon)\sim
\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)}\varepsilon^{d-1}.
\]
In fact \(\Pr(D_\pi>t)=I_{\cos^2t}((d-1)/2,1/2)\), where \(I\) is the regularized incomplete beta integral.

**Sharp critical aperture crossover.** For every fixed \(\lambda\ge0\), let \(\alpha_\varepsilon=\pi-2\lambda\varepsilon\) and \(a_\varepsilon=\alpha_\varepsilon/2\). Then
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-(d-1)}
\Pr(D_{\alpha_\varepsilon}>a_\varepsilon-\varepsilon)
=\frac2\pi\int_0^1
\big((\lambda+1)^2-(\lambda+v)^2\big)^k\,dv.
\]
The convergence is uniform for \(\lambda\) in compact subsets of \([0,\infty)\). At \(\lambda=0\), it gives the hemispherical constant; for large \(\lambda\), the integral has leading term \((2\lambda)^k/(k+1)\), matching the fixed-opening scaling within its overlap regime.

**Marked rare-clearance law.** For fixed \(\alpha<\pi\), use the above factorization and, on \(D_\alpha>a-\varepsilon\), set \(V=(a-U)/\varepsilon\) and \(W=(1-Q)/(2\varepsilon\cot a)\). Their conditional joint law converges in total variation to the density
\[
 k(k+1)w^{k-1}\,\mathbf1_{\{v\ge0,w\ge0,v+w\le1\}}\,dv\,dw,
\]
i.e. \((V,W,1-V-W)\) approaches \(\operatorname{Dirichlet}(1,k,1)\). In the critical regime \(\alpha_\varepsilon=\pi-2\lambda\varepsilon\), put \(V=(a_\varepsilon-U)/\varepsilon\) and \(W=(1-Q)/\varepsilon^2\). Conditionally on the analogous rare event, \((V,W)\) converges in total variation to the density proportional to \(w^{k-1}\) on
\[
0\le v\le1,\qquad 0\le w\le(\lambda+1)^2-(\lambda+v)^2.
\]

## Assumptions and scope

The ambient metric is the ordinary round-sphere geodesic distance, and probability is normalized \((d-1)\)-dimensional surface measure. The longitude coordinate is measured in the \((x_1,x_2)\)-plane; all remaining coordinates may be nonzero. The lune is the subset with azimuth between \(0\) and \(\alpha\). The value \(\alpha=\pi\) is included only as a limiting hemisphere, not as a pair of distinct non-opposite supporting hemispheres. Equality on boundaries has probability zero. All endpoint asymptotics are for fixed integer \(d\ge3\), unless a compact-uniform parameter range is explicitly stated.

## Proof

**1. Exact geometry.** Write the first two coordinates of \(X\) as \((\rho\cos\phi,\rho\sin\phi)\), where \(0\le\phi\le\alpha\), \(0\le\rho\le1\). The closest face is the great hemisphere at longitude \(0\) for \(\phi\le\alpha/2\), otherwise the one at \(\alpha\). Indeed, the orthogonal projection of \(X\) to the nearest face's ambient hyperplane has nonnegative component along that face's chosen ray, since its azimuthal difference is at most \(\alpha/2\le\pi/2\). Normalizing that projection produces a closest point on the *hemispherical* face. The distance is therefore \(\arcsin(\rho\sin\min\{\phi,\alpha-\phi\})\). This also holds at \(\alpha=\pi\), where both halves form the equator bounding the hemisphere.

**2. Spherical measure.** Realize an unconditioned uniform sphere point as an independent standard Gaussian vector divided by its length. Rotational symmetry makes \(\phi\) uniform on \([0,2\pi)\) and independent of \(\rho\), so conditioning on the lune makes \(\phi\) uniform on \([0,\alpha]\). The ratio of the sum of squares of the first two Gaussian coordinates to the total sum has the \(\operatorname{Beta}(1,(d-2)/2)\) law. Thus \(U=\min\{\phi,\alpha-\phi\}\) is independent of \(Q=\rho^2\), and is uniform on \([0,a]\). The survival integral follows from \(\Pr(Q>z)=(1-z)^k\) and from \(\sin u\ge\sin t\) precisely when \(u\ge t\) inside \([0,a]\).

**3. Moments and ordering.** Independence gives \(\mathbb E[Q^{s/2}]=\Gamma(d/2)\Gamma(1+s/2)/\Gamma((d+s)/2)\). Substitution \(z=\sin^2u\) gives \(\mathbb E[\sin^sU]=B_{\sin^2a}((s+1)/2,1/2)/\alpha\). For \(s=2\), elementary integration yields the displayed second moment. Its derivative in \(\alpha\) is \((\sin\alpha-\alpha\cos\alpha)/(d\alpha^2)>0\), since the numerator has derivative \(\alpha\sin\alpha>0\) and starts at zero. For ordering, use the same independent \(Q\) and \(T\sim\operatorname{Unif}[0,1]\), set \(U_i=\alpha_i T/2\), and use strict monotonicity of sine on \((0,\pi/2)\).

**4. Small-clearance asymptotic.** Conditional on \(\rho\), the probability of clearance at most \(t\) equals \(1\) if \(\rho\le\sin t/\sin a\), and otherwise equals \((1/a)\arcsin(\sin t/\rho)\) unless that expression exceeds one; equivalently it is \(\min\{1,a^{-1}\arcsin(\min(1,\sin t/\rho))\}\). Since \(\Pr(\rho\le z)=O(z^2)\) and \(\mathbb E[1/\rho]=\sqrt\pi\Gamma(d/2)/\Gamma((d-1)/2)<\infty\), dominated convergence gives the stated linear constant. To see domination, split at \(\rho=2\sin t/\sin a\), bound the small-radius contribution by \(O(t^2)\), and on the rest bound \(\arcsin(\sin t/\rho)\le(\pi/2)\sin t/\rho\). The coefficient is also the boundary hypersurface area divided by the lune's surface volume.

**5. Fixed-aperture endpoint.** Put \(t=a-\varepsilon\) and \(u=a-\varepsilon v\) in the exact integral. For \(0\le v\le1\), uniformly,
\[
1-\frac{\sin^2(a-\varepsilon)}{\sin^2(a-\varepsilon v)}
=2\varepsilon\cot a\,(1-v)+O(\varepsilon^2).
\]
Dominated convergence after factoring \(\varepsilon^{k+1}\), and \(\int_0^1(1-v)^k\,dv=1/(k+1)\), gives \(\frac2{\alpha(k+1)}(2\cot a)^k\varepsilon^{k+1}\). Since \(k+1=d/2\), this is the fixed-aperture constant.

**6. Hemisphere and critical crossover.** At \(\alpha=\pi\) the lune is \(x_2\ge0\). The coordinate square \(x_2^2\) has \(\operatorname{Beta}(1/2,(d-1)/2)\) law, giving the regularized incomplete-beta formula. Its small-argument expansion yields the displayed \(\varepsilon^{d-1}\) coefficient. More generally put \(a_\varepsilon=\pi/2-\lambda\varepsilon\), \(t=a_\varepsilon-\varepsilon\), \(u=a_\varepsilon-\varepsilon v\). Uniformly for bounded \(\lambda\) and \(v\in[0,1]\),
\[
1-\frac{\sin^2t}{\sin^2u}
=\varepsilon^2\big((\lambda+1)^2-(\lambda+v)^2\big)+O(\varepsilon^4).
\]
Substitution in the exact integral proves the compact-uniform crossover and its \(\lambda=0\) specialization.

**7. Conditional marks.** The random variable \(1-Q\) has density \(kz^{k-1}\) on \((0,1)\). For fixed \(\alpha<\pi\), the changes \(u=a-\varepsilon v\), \(z=2\varepsilon\cot a\,w\) give, on the rare event, joint density proportional to \(w^{k-1}\) on a domain converging uniformly in its upper boundary to \(\{0\le v\le1,\,0\le w\le1-v\}\). The limiting total unnormalized integral is \(1/[k(k+1)]\), so the displayed normalized Dirichlet density follows by dominated convergence in \(L^1\), which is total-variation convergence. In the critical window, change instead \(z=\varepsilon^2w\); the uniform expansion in Step 6 gives the curved limiting support and the same \(L^1\) argument. The normalizing factor is \(k/\int_0^1((\lambda+1)^2-(\lambda+v)^2)^k\,dv\). The support boundaries have zero limiting mass.

## Verification

The standalone `checker.py` uses an independent closest-point calculation on each bounding great hemisphere for sampled sphere points, numerical quadrature of the survival law, beta-function comparison at the hemisphere, exact moment comparisons, fixed-aperture tail ratios, critical crossover ratios and pathwise ordering. Executed with NumPy and SciPy: 5,230 assertions passed. Finite numerical tests serve only to catch normalization or algebra errors; the all-dimensional claims and limits rely on the analytic proof above.

## Relationship to prior work

Lassak's 2013 public paper on spherical width establishes the relevant lune/thickness language, and Lassak–Musielak's 2016 preprint studies reduced spherical bodies rather than uniformly sampled distance to the bounding great hemispheres. Besau et al. (2023) analyze random spherical convex hulls on an orthogonal wedge, including geometric integral formulas, but not the one-point boundary-clearance law, its two tail exponents, or the conditional rare-clearance marks as statements in the inspected text. The already recorded spherical-lune antipodal-pair distance study concerns the **distance between two independent points**, not the distance of one point to the lune boundary; neither event implies the other. The factorization uses standard Gaussian/Beta spherical-coordinate facts, not claimed as new. The claimed contribution is the combined exact clearance law, strict aperture tomography, sharp critical aperture crossover and marked rare-event laws. Search evidence and remaining priority risks are detailed in the accompanying review.

## Limitations

The law assumes a round sphere, uniformly area-sampled points, a two-hemisphere lune, and intrinsic great-circle distance to the *boundary*. It is not a distribution of pairwise distance, width of random bodies, or Euclidean distance to a face. The fixed-aperture endpoint law requires \(\alpha<\pi\); substituting \(\alpha=\pi\) into its coefficient would be invalid. The critical transition is for \(\alpha\) approaching \(\pi\) at the same scale as the clearance deficit. The moment inverse uses known ambient dimension. General spherical polygons, nonuniform sampling, and statistical finite-sample reconstruction are not addressed. Priority has not been independently established.

## References

1. M. Lassak, *Width of spherical convex bodies*, Aequationes Mathematicae **89** (2015), 555–567; first published online 2013-12-06. DOI: https://doi.org/10.1007/s00010-013-0237-3 (MSC 52A55).
2. M. Lassak and M. Musielak, *Reduced spherical convex bodies*, arXiv:1607.00132, first publicly posted 2016-07-01. https://arxiv.org/abs/1607.00132.
3. F. Besau, A. Gusakova, M. Reitzner, C. Schütt, C. Thäle and E. Werner, *Spherical convex hull of random points on a wedge*, first published online 2023-08-25, Mathematische Annalen **389** (2024), 2289–2316. https://doi.org/10.1007/s00208-023-02704-9.
