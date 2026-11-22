# A five-halves boundary-pinning law for near-maximal Euclidean chord triangles on a hemisphere

## Finding

Let \(H=\{(x,y,z)\in S^2:z\ge0\}\) be the northern closed hemisphere of the unit Euclidean sphere in \(\mathbb R^3\). Sample \(X_1,X_2,X_3\) independently from *normalized spherical surface area* on \(H\), and let
\[
T=\tfrac12\left\|(X_2-X_1)\times(X_3-X_1)\right\|
\]
be the ordinary **Euclidean area of their planar chord triangle**. This differs from the intrinsic area of the geodesic spherical triangle and from the area of the triangle after orthogonally projecting the vertices onto the equatorial disk.

The maximum possible value is \(M=3\sqrt3/4\). As \(\varepsilon\downarrow0\),
\[
\boxed{\Pr\big\{T>M-\varepsilon\big\}
\sim\frac{32\,3^{3/4}}{45\pi}\,\varepsilon^{5/2}.}
\]
The explicit coefficient is \(0.5159748493187007\ldots\).

The asymptotic has a joint geometric refinement. Given the near-maximal event, the labeled sample lies near one of two equilateral orientation families on the *equator*. Write the longitude of the first point as \(\phi\), choose an orientation sign \(\sigma\in\{-1,+1\}\), and use local longitude deviations \(q,r\) such that
\[
\theta_1=\phi,\qquad
\theta_2=\phi+\sigma\,2\pi/3+q,\qquad
\theta_3=\phi+\sigma\,4\pi/3+r.
\]
Let \(z_j\ge0\) denote the third coordinates and put
\[
(a,b,u_1,u_2,u_3)=\varepsilon^{-1/2}(q,r,z_1,z_2,z_3),\qquad
k_a=\sqrt3/4,\quad k_z=\sqrt3/12.
\]
For either sign the joint conditional law of these five rescaled coordinates converges in **total variation** to normalized Lebesgue measure on
\[
\mathcal D=\left\{(a,b,u_1,u_2,u_3):u_j\ge0,\quad
k_a(a^2-ab+b^2)+k_z(u_1+u_2+u_3)^2<1\right\}.
\]
The orientation sign is asymptotically fair and independent; the phase \(\phi\) remains independent and uniform on \([0,2\pi)\). On this limit set, putting \(S=u_1+u_2+u_3\), the share \(J=k_z S^2\) has law \(\operatorname{Beta}(3/2,2)\), while \((u_1,u_2,u_3)/S\) is independently \(\operatorname{Dirichlet}(1,1,1)\). After diagonalizing the angular form and dividing out its available radius, the remaining two-dimensional angular mark is an independent uniform unit-disk point. Also \((M-T)/\varepsilon\), under the stated conditioning, converges to \(\operatorname{Beta}(5/2,1)\).

## Assumptions and scope

The hemisphere and sphere have radius one; the pole is fixed but otherwise irrelevant by rotational invariance. Sampling is independent with normalized **surface measure** \((2\pi)^{-1}d\theta\,dz\), not uniform surface measure on the full sphere and not projected-area measure on the equatorial disk. The number of vertices is exactly three. The area is unsigned and Euclidean, and the threshold \(\varepsilon>0\) tends to zero without any other varying parameter. The statement about total variation applies to the continuous, locally defined marked coordinates once the near-maximal neighborhood is selected; outside that neighborhood the conditioned probability eventually vanishes.

## Proof

**1. Unique maximizing geometry.** Any three vertices on the unit sphere lie in an affine plane whose intersection with the sphere is a circle of radius at most one. Among triangles inscribed in a radius-\(r\) circle, the maximal area is \(3\sqrt3 r^2/4\), attained only by equilateral triangles. Therefore \(T\le M=3\sqrt3/4\), with equality only for a regular triple on a great circle. Such a triple has vector sum zero; since all three third coordinates are nonnegative, that sum forces every third coordinate to vanish. Thus all maximizers belong to precisely two labeled equilateral families on the equator, parameterized by a common longitude \(\phi\). Compactness implies that every sufficiently small area-deficit event lies within arbitrarily small neighborhoods of those families.

**2. Exact sampling density and local deficit.** Use the surface coordinates
\[
X_j=(\sqrt{1-z_j^2}\cos\theta_j,\sqrt{1-z_j^2}\sin\theta_j,z_j),
\qquad 0\le z_j\le1,\quad0\le\theta_j<2\pi.
\]
For uniform surface sampling, all six variables \(z_j,\theta_j\) are independent, with joint density \((2\pi)^{-3}\). On the positive orientation branch set \(q=\theta_2-\phi-2\pi/3\) and \(r=\theta_3-\phi-4\pi/3\); the negative orientation branch is the reflected counterpart. The absolute Jacobian of \((\theta_1,\theta_2,\theta_3)\mapsto(\phi,q,r)\) is one.

Writing \(d_{ij}=X_i\cdot X_j\), the exact identity
\[
4T^2=4(1-d_{12})(1-d_{13})
-(1+d_{23}-d_{12}-d_{13})^2
\]
expresses area through the Gram matrix and therefore permits a direct local expansion without assuming planarity. Its second-order Taylor expansion gives, for either oriented family,
\[
M-T=k_a(q^2-qr+r^2)+k_z(z_1+z_2+z_3)^2
+O\!\left((|q|+|r|+z_1+z_2+z_3)^3\right),
\tag{1}
\]
with \(k_a=\sqrt3/4\) and \(k_z=\sqrt3/12\). Formula (1) is a **boundary-cone** expansion: the three vertical variables have a rank-one quadratic form, but the form is strictly positive on the admissible cone \(z_j\ge0\). In particular
\[
q^2-qr+r^2\ge\tfrac12(q^2+r^2),\qquad
(z_1+z_2+z_3)^2\ge\sum_j z_j^2.
\]
Shrinking the maximizer neighborhood and absorbing the cubic remainder therefore yields a lower bound by a positive multiple of \(q^2+r^2+\sum_jz_j^2\). Every near-maximal configuration obeys \(|q|+|r|+\sum z_j=O(\sqrt\varepsilon)\), and (1) has a uniformly \(o(\varepsilon)\) remainder on that event.

**3. The sharp coefficient.** After the rescaling in the finding, the support of the event converges in measure to \(\mathcal D\). The rescaled support is uniformly bounded by the previous coercivity estimate, and the boundary of \(\mathcal D\) has five-dimensional Lebesgue measure zero. Dominated convergence therefore applies to its volume and to conditional densities.

Set \(S=u_1+u_2+u_3\). At each \(S\ge0\), integrating over the positive simplex of vertical variables gives the measure \((S^2/2)\,dS\). For fixed \(S\) with \(k_z S^2<1\), the angular ellipse \(k_a(a^2-ab+b^2)<1-k_z S^2\) has area \((8\pi/3)(1-k_z S^2)\). Consequently
\[
\begin{aligned}
\operatorname{vol}_5(\mathcal D)
&=\frac{4\pi}{3}\int_0^{k_z^{-1/2}}S^2(1-k_z S^2)\,dS\\
&=\frac{8\pi}{45}k_z^{-3/2}
=\frac{64\pi\,3^{3/4}}{45}.
\end{aligned}
\]
The phase \(\phi\) contributes a factor \(2\pi\); the two orientations contribute a factor two; the joint angular sampling density is \((2\pi)^{-3}\). Thus the total measure coefficient multiplying \(\varepsilon^{5/2}\) is
\[
\frac{2\cdot2\pi}{(2\pi)^3}\operatorname{vol}_5(\mathcal D)
=\frac{\operatorname{vol}_5(\mathcal D)}{2\pi^2}
=\frac{32\,3^{3/4}}{45\pi}.
\]
This proves the sharp asymptotic.

**4. Conditional marks.** Since conditional rescaled densities converge in \(L^1\) to the constant density on the bounded domain \(\mathcal D\), their distributions converge in total variation. Writing \(J=k_zS^2\), the vertical simplex measure contributes a factor proportional to \(J^{1/2}\,dJ\), and the available two-dimensional angular-ellipse area contributes \((1-J)\). Therefore \(J\) has a \(\operatorname{Beta}(3/2,2)\) density. At fixed \(S\), the vertical proportions are uniform on the two-simplex, hence \(\operatorname{Dirichlet}(1,1,1)\), and are independent of \(J\). Whitening the quadratic form \(a^2-ab+b^2\) and scaling by \((1-J)^{-1/2}\) makes the angular coordinate uniform on the unit disk and independent of the other marks. The two orientation neighborhoods have equal density and a common uniformly distributed phase. Finally, the model sublevel volume at threshold \(t\) is exactly proportional to \(t^{5/2}\) by five-dimensional homogeneity. That gives the \(\operatorname{Beta}(5/2,1)\) limit for the normalized area deficit.

## Verification

The standalone `verify.py` requires Python, NumPy, SciPy and SymPy. Run `python verify.py` from the extracted package. It symbolically checks the exact Gram-determinant second-order form and the closed five-dimensional cone volume. It separately evaluates local exact chord-triangle areas against their quadratic expansion and checks the coefficient through deterministic Sobol cubature of the near-maximal event at four positive thresholds. On the supplied environment, the checker returned `ALL_CHECKS_PASSED`; near-cap coefficient ratios at thresholds \(0.02\), \(0.005\), \(0.001\), and \(0.0002\) were approximately \(1.003736\), \(1.001089\), \(0.999981\), and \(0.999933\), respectively. These finite checks corroborate, but do not prove, the infinite-limit theorem; the proof is the geometric localization, Taylor expansion and exact cone integration above.

## Relationship to prior work

Bárány, Hug, Reitzner and Schneider, *Random points in halfspheres* (first public arXiv version 2015-05-18), study hemisphere sampling and large-sample spherical convex-hull expectations. Their primary mathematical classifications include 52A22. Their setting motivates the hemisphere boundary geometry but they do not give this fixed-three-vertex **extrinsic Euclidean triangle-area upper-tail** theorem. The relevant introduction, preliminaries and results concerning expected volume and approximation were examined.

A published disk-triangle upper-tail result, *A Dirichlet rare-shape law for nearly maximal random disk triangles* (2026), gives a general radial-angle sampling law for **planar** triangle area, including projected radial distributions. Indeed projection of a surface-uniform hemisphere point onto the equatorial disk yields a radial density singular at the boundary and a superficially similar \(5/2\) exponent. This does **not** imply the present coefficient or conditional law: the Euclidean area of the original noncoplanar-tilted plane is larger than the area of its horizontal projection, and the leading vertical deficit here is the correlated square \(k_z(z_1+z_2+z_3)^2\), not independent linear radial deficits. For example, at first order in the squared altitude of a *single* lifted equatorial vertex, the intrinsic chord triangle has coefficient \(\sqrt3/12\), whereas its equatorial projection has coefficient \(\sqrt3/4\). The exact upper endpoint is shared, but the sublevel volumes differ.

Akopyan, Edelsbrunner and Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere* (arXiv:2007.07783), study full-sphere sampling, metric expectations, and shape-size factorization. The full text's introduction and sections on metric formulas were examined; they do not present this boundary-pinned hemisphere event. A separate published sphere-sampling finding, *Sharp small-area law for three sphere-uniform Euclidean chord vertices* (2026), treats the **opposite**, zero-area tail under full-sphere sampling. Finch and Jones's *Random Spherical Triangles* concerns intrinsic spherical triangle geometry; the available record provides no direct extrinsic hemisphere endpoint implication. No absolute historical-priority or uniqueness guarantee is asserted.

## Limitations

The theorem treats the unit hemisphere, exactly three independent surface-uniform points, and the leading small-deficit law. It does not assert a complete finite-threshold area CDF, a second-order coefficient, or a dimension-wide generalization. The conditional mark law is relative to the specified maximizing equator and its labeled orientation charts. Historical priority remains provisional because generic multivariate endpoint principles and older isotropic-simplex literature may encode equivalent formulas without using these coordinates; the most relevant accessible texts did not produce the stated claim. No independent mathematical audit has yet been performed.

## References

1. I. Bárány, D. Hug, M. Reitzner and R. Schneider, *Random points in halfspheres*, arXiv:1505.04672, first posted 2015-05-18, https://arxiv.org/abs/1505.04672.
2. A. Akopyan, H. Edelsbrunner and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere*, arXiv:2007.07783, first posted 2020-07-15, https://arxiv.org/abs/2007.07783.
3. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, first posted 2010-09-27, https://arxiv.org/abs/1009.5329.
4. *A Dirichlet rare-shape law for nearly maximal random disk triangles*, published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-dirichlet-rare-shape-law-for-nearly-maximal-random-disk-triang--aea206eaa036.
5. *Sharp small-area law for three sphere-uniform Euclidean chord vertices*, published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-small-area-law-for-three-sphere-uniform-euclidean-chord-ve--cfcd84509873.
