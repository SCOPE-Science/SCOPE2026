# The conditional uniform-chord law for nearly coplanar spherical tetrahedra

## Finding

Let \(P_1,P_2,P_3,P_4\) be independent surface-area-uniform points on the Euclidean unit sphere \(S^2\subset\mathbb R^3\). Write \(V\) for the unsigned three-dimensional Euclidean volume of their convex hull and \(E_\varepsilon=\{V\le\varepsilon\}\). The following describes the **joint conditional weak limit** as \(\varepsilon\downarrow0\). The scalar small-volume probability is supplied as its normalization, not separately asserted as a new marginal-volume result:

\[
\Pr(E_\varepsilon)=3\pi\varepsilon+o(\varepsilon).
\]

Define \(D=\|(P_2-P_1)\times(P_3-P_1)\|\), \(n=((P_2-P_1)\times(P_3-P_1))/D\), and \(h=n\cdot P_1\), outside the null set \(D=0\). Let \(\sigma\) denote normalized surface measure on \(S^2\). First draw the ordered triple \((P_1,P_2,P_3)\) with density \(2/(\pi D)\) relative to \(\sigma^{\otimes3}\); then draw \(P_4\) uniformly by arclength on the circle \(S^2\cap\{x:n\cdot x=h\}\). This **is** the joint conditional weak limit given \(E_\varepsilon\).

In particular, for every pair of distinct indices \(i,j\), under conditioning on \(E_\varepsilon\), the Euclidean chord \(\|P_i-P_j\|\) converges in distribution to \(\operatorname{Uniform}(0,2)\). Unconditionally the chord density is \(\ell/2\) on \((0,2)\). This marginal assertion does **not** say the six limiting edges are independent.

## Assumptions and scope

Only four i.i.d. uniform points on the unit two-sphere are considered. Volume is the absolute determinant divided by six, not spherical geodesic volume. The circle sampling above is ordinary arclength normalized to total mass one; almost every selected triple spans a proper plane whose intersection with the sphere is a circle of positive radius. Conditional weak convergence is against every continuous bounded function on \((S^2)^4\). Thresholds approach zero through positive real values. No finite-threshold equality or rate of convergence is asserted beyond the scalar \(o(\varepsilon)\).

## Proof

**1. An inverse-distance identity.** Let \(L\) be any line intersecting the open unit ball and \(Q\sim\sigma\). Then
\[
\mathbb E\bigl[\operatorname{dist}(Q,L)^{-1}\bigr]=\pi/2.
\tag{1}
\]
To see this, rotate coordinates so \(L\) is parallel to the last coordinate axis and has transverse displacement \(y\in\mathbb R^2\), where \(\rho=\|y\|<1\). The two-dimensional projection of \(Q\) has density \(g(x)=(2\pi\sqrt{1-\|x\|^2})^{-1}\) on the unit disk. Its two-dimensional Fourier transform under \(\widehat f(\xi)=\int e^{-i\xi\cdot x}f(x)\,dx\) is \(\widehat g(\xi)=\sin\|\xi\|/\|\xi\|\). The Fourier transform of the locally integrable Coulomb kernel \(1/\|x\|\) is \(2\pi/\|\xi\|\). Radial Fourier inversion, initially with Abel regularization and then by continuity of the finite potential in the disk, gives
\[
\int_{\|x\|<1}\frac{g(x)}{\|x-y\|}\,dx
 =\int_0^\infty\frac{\sin s}{s}J_0(\rho s)\,ds=\frac\pi2.
\]
For the final equality use \(J_0(z)=\pi^{-1}\int_0^\pi\cos(z\cos\theta)\,d\theta\): Abel-damped integration of \(\sin s\cos(\rho s\cos\theta)/s\) yields half the sum of two arctangents of positive arguments \(1\pm\rho\cos\theta\), tending to \(\pi/2\) when \(\rho<1\). This proves (1) including the uniform value at every interior displacement, not merely at the disk center. The singularities at the transverse point and at the disk edge are integrable.

**2. Integrable planar Jacobian.** Put \(\ell=\|P_2-P_1\|\). The exact vector identity
\[
D=\ell\,\operatorname{dist}(P_3,\operatorname{line}(P_1,P_2))
\]
and (1) show
\[
\mathbb E[D^{-1}\mid P_1,P_2]=\frac\pi{2\ell}.
\tag{2}
\]
Since the chord length between two independent uniform sphere points has density \(\ell/2\) on \((0,2)\), \(\mathbb E[\ell^{-1}]=1\), and therefore
\[
\mathbb E[D^{-1}]=\pi/2<\infty.
\tag{3}
\]

**3. Rare-event disintegration and tight normalization.** Given the first triple, use latitude \(z=n\cdot P_4\), uniform on \([-1,1]\), and an independent uniform azimuth. Then \(V=(D/6)|z-h|\) and
\[
p_\varepsilon(P_1,P_2,P_3)
 =\tfrac12\operatorname{length}([-1,1]\cap[h-6\varepsilon/D,h+6\varepsilon/D]).
\]
For almost every triple, \(D>0\), \(|h|<1\), and \(p_\varepsilon/\varepsilon\to6/D\). For all triples and every \(\varepsilon>0\), \(0\le p_\varepsilon/\varepsilon\le6/D\). Equation (3) and dominated convergence give \(\Pr(E_\varepsilon)/\varepsilon\to6\mathbb E[D^{-1}]=3\pi\).

For any bounded continuous test function \(F\) on \((S^2)^4\), the same disintegration integrates \(F\) over the latitude interval, whose normalized conditional azimuthal average tends to the average of \(F\) over the circle at latitude \(h\). Since \(p_\varepsilon/\varepsilon\le6/D\), dominated convergence also applies to the *weighted* joint integral. After division by \(3\pi\), the marginal triple measure has density \((6/D)/(3\pi)=2/(\pi D)\) and the fourth point is arclength-uniform on the conditional circle. This proves joint weak convergence.

**4. Uniform-edge corollary.** By (2), under the limiting triple law the chord \(\ell=\|P_1-P_2\|\) is tilted from its original density \(\ell/2\) by a factor \(\pi/(2\ell)\), and the normalizing factor \(2/\pi\) leaves the constant density \(1/2\) on \((0,2)\). The finite-threshold conditioning is exchangeable in the four labels. Hence every one of the six conditional edge marginals converges to the same uniform law.

## Verification

The standalone checker `check_nearflat_tetra.py` uses independent isotropic Gaussian directions for three vertices and **analytically integrates** the fourth vertex's uniform latitude. With seed 211108 and 1,500,000 triples, the estimates of \(\Pr(E_\varepsilon)/\varepsilon\) at \(\varepsilon=0.01,0.002,0.00025,0.0001\) were approximately \(7.9792,8.7741,9.1992,9.2860\), approaching \(3\pi\approx9.4248\). The corresponding weighted chord means were \(1.1008,1.0514,1.0203,1.0134\), approaching one, the mean of \(\operatorname{Uniform}(0,2)\). Separately, numerical elliptic-integral quadrature of (1) at five transverse displacements returned \(\pi/2\) within floating-point quadrature tolerance. All such tests are finite numerical checks, not proof.

Run `python check_nearflat_tetra.py` after installing the dependency in `requirements.txt`.

## Relationship to prior work

Miles (1971) already gives broad moments of volumes of isotropic random simplices, encompassing the **marginal** spherical-tetrahedron volume problem. Since a bounded random variable is moment-determinate, those moments in principle determine the scalar volume distribution, so the \(3\pi\varepsilon\) factor is not claimed as a standalone original distributional theorem. MathWorld also records the spherical tetrahedron model and selected volume moments. The assessed distinct assertion is the *joint conditional point-configuration limit*, with its inverse-area tilt, and the resulting uniform distribution of every chord length under near-coplanarity. Brauchart et al. (2015 initial preprint) study many spherical random points, covering and hull-facet hole radii, a different large-sample regime; their accessible primary text was compared. Full access to Miles (1971) was unavailable; unexamined statements there remain a priority risk.

## Limitations

This is an exact asymptotic weak-limit result, not a finite-threshold distribution. It does not give independence of edges, an explicit error rate, higher-dimensional extensions, or a statistically stable finite-sample estimation procedure. Older full-text material not accessible for a direct statement-by-statement comparison may contain a related joint distribution; novelty remains provisional and no independent audit has been performed.

## References

1. R. E. Miles, *Isotropic random simplices*, Advances in Applied Probability **3** (1971), 353–382, https://doi.org/10.2307/1426176 (abstract accessible; full text not obtained).
2. J. S. Brauchart, A. B. Reznikov, E. B. Saff, I. H. Sloan, Y. G. Wang, R. S. Womersley, *Random Point Sets on the Sphere — Hole Radii, Covering, and Separation*, first submitted 2015-12-23, https://arxiv.org/abs/1512.07470.
3. E. W. Weisstein, *Sphere Tetrahedron Picking*, MathWorld, https://mathworld.wolfram.com/SphereTetrahedronPicking.html.
