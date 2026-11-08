# Universal geodesic containment laws for meridian-cut spherical domains

## Finding

Let \(d\ge 2\). Choose an oriented two-dimensional coordinate plane in \(\mathbb R^{d+1}\) and write \(\phi(x)=\arg(x_1+i x_2)\) off the axis \(x_1=x_2=0\). Let \(E\) be a union of \(k\ge1\) pairwise disjoint, nonempty, proper open circular arcs with lengths \(\ell_1,\ldots,\ell_k\in(0,2\pi]\); equality \(\ell_j=2\pi\) is allowed only for a single component consisting of the circle with one angle omitted. The complement may include zero-width meridian cuts. Set \(\theta=\sum_j\ell_j\le2\pi\) and \(\Omega_E=\{x\in S^d:\phi(x)\in E\}\).

For independent normalized-surface-area-uniform \(X,Y\in\Omega_E\), let \(\gamma_{X,Y}\) be their unique minimizing spherical geodesic (well defined almost surely). The **exact containment probability** is

\[
\boxed{\Pr\{\gamma_{X,Y}\subset\Omega_E\}
=\frac1{\theta^2}\sum_{j=1}^k
 \left(\ell_j^2-(\ell_j-\pi)_+^2\right),\qquad (u)_+=\max(u,0).}
\]

This formula holds unchanged on every \(S^d\), \(d\ge2\), and also for independent samples from *any* sphere probability measure whose azimuthal marginal before conditioning on \(\Omega_E\) is uniform, provided it assigns zero mass to the axis and antipodal endpoint pairs.

For fixed \(k\ge2\) and total angular measure \(0<\theta\le2\pi\), the sharp inequalities are

\[
\boxed{\frac1k\ \le\Pr\{\gamma_{X,Y}\subset\Omega_E\}
\ <\ \frac{\theta^2-(\theta-\pi)_+^2}{\theta^2}.}
\]

Equality at the lower bound holds **exactly** when all component lengths equal \(\theta/k\); the upper bound is an unattained supremum approached as all but one component shrink to zero angular length. For \(k=1\), the right-hand expression is the attained exact probability.

A single deleted open meridian (angular set \(E=S^1\setminus\{\phi_0\}\)) has zero surface area but changes the containment probability from \(1\) for the complete sphere to exactly \(3/4\). With \(k\ge2\) equally spaced deleted meridians, it is exactly \(1/k\).

## Assumptions and scope

The sphere has its standard round intrinsic metric. A proper open circular arc is a connected open subset of \(S^1\) not equal to \(S^1\); an arc of length \(2\pi\) denotes the circle with one point removed. Distinct components must be separated by at least one omitted angle, which may be a singleton. Thus \(\theta=2\pi\) is allowed even when the excluded set is nonempty and has angular measure zero. For an actually uncut sphere, the geodesic stays inside with probability \(1\), and the component formula is not applied because \(E=S^1\) is not a proper arc.

All probability claims disregard the measure-zero sets where the azimuth is undefined, endpoints are antipodal, or angular separations are exactly \(\pi\). The uniform-azimuth generalization assumes that those exceptional endpoint pairs have zero probability. The surface-uniform law automatically has these properties.

## Proof

**1. Longitude of a shortest spherical arc.** For \(x,y\in S^d\) distinct and nonantipodal, the normalized affine interpolation
\[
g(t)=\frac{(1-t)x+ty}{\|(1-t)x+ty\|},\qquad 0\le t\le1,
\]
traces exactly the unique minimizing great-circle arc, although not at constant speed. Its projection to the designated complex coordinate plane is proportional to
\[
(1-t)\rho_x e^{i\phi(x)}+t\rho_y e^{i\phi(y)},
\]
where \(\rho_x,\rho_y>0\). If the endpoint azimuths are not diametrically opposite, this planar segment avoids zero and its argument traces the *shorter* circular arc between the two azimuths. This follows because positive combinations of two nonopposite planar rays fill their pointed cone of angular opening less than \(\pi\). Hence a shortest spherical geodesic remains in \(\Omega_E\) if and only if the shorter azimuthal arc between its endpoint azimuths remains in \(E\).

**2. Exact component probability.** Rotational invariance of surface measure makes both endpoint azimuths independent and uniform on \(E\); the same is true under the stated uniform-azimuth sampling extension. If the two angles belong to different components of \(E\), no connecting circular arc lies wholly in \(E\), so the spherical geodesic exits. Given both angles in one component of length \(\ell\), identify that arc with \((0,\ell)\) and let \(U,V\) be iid uniform there. The shorter angular path lies in this component precisely when \(|U-V|\le\pi\), outside a probability-zero boundary. Since the two corners of the square \((0,\ell)^2\) satisfying \(|U-V|>\pi\) have total area \((\ell-\pi)_+^2\), the conditional survival probability is \(1-(\ell-\pi)_+^2/\ell^2\). The probability that both sampled angles belong to that component is \((\ell/\theta)^2\). Summing these disjoint cases proves the boxed formula.

**3. Sharp extremal law.** Put \(f(s)=s^2-(s-\pi)_+^2\) for \(0\le s\le2\pi\). This function is strictly convex on \([0,\pi]\), affine on \([\pi,2\pi]\), convex throughout, and \(f(0)=0\). Jensen's inequality gives
\[
\sum_{j=1}^k f(\ell_j)\ge k f(\theta/k)
=\frac{\theta^2}{k},
\]
because \(k\ge2\) and \(\theta/k\le\pi\). Equality forces all \(\ell_j=\theta/k\), including the endpoint case \(k=2,\theta=2\pi\).

Also \(f(s)/s=s\) for \(s\le\pi\) and \(f(s)/s=2\pi-\pi^2/s\) for \(s>\pi\), which is strictly increasing for \(s\in(0,2\pi]\). Thus \(f(a)+f(b)<f(a+b)\) whenever \(a,b>0\) and \(a+b\le2\pi\); iterating gives \(\sum_j f(\ell_j)<f(\theta)\) for \(k\ge2\). Shrinking \(k-1\) components while keeping total \(\theta\) makes the left side approach \(f(\theta)\), proving sharpness and nonattainment of the upper bound.

**4. Zero-area cuts.** For a single missing meridian, \(k=1,\ell_1=\theta=2\pi\), hence \(f(2\pi)/(2\pi)^2=(3\pi^2)/(4\pi^2)=3/4\). For \(k\) equally spaced missing meridians, the components all have length \(2\pi/k\), giving probability \(1/k\). With no deleted meridian every minimizing arc lies in the entire sphere, so the probability is \(1\).

## Verification

The proof is exact and dimension-independent. The independent numerical checker `check_spherical_azimuth_visibility.py` samples unit-sphere points in dimensions \(2,3,5,6\), directly interpolates spherical minimizing arcs in ambient coordinates, and measures whether the interpolated points remain within the azimuthal domain. In five test configurations covering convex sectors, reflex sectors, two- and three-component domains, its empirical frequencies agree with the exact formula within the stated numerical tolerance; the checker also tests the algebraic equal-length bound for a range of component counts. Run with `python check_spherical_azimuth_visibility.py` (requires NumPy).

## Relationship to prior work

Lassak's *Width of spherical convex bodies* (first published online 6 December 2013) develops spherical convexity and lune width, including the positive-cone criterion for spherical convexity. Lassak and Musielak's *Reduced Spherical Convex Bodies* (arXiv first submitted 1 July 2016) studies reduced convex bodies and their containing lunes. These works supply natural geometric context, not the probability that random short geodesics remain in nonconvex/disconnected meridian-cut regions. The result here treats all angular component arrangements, arbitrary sphere dimensions, sharp extremizers, and zero-area meridian cuts.

The elementary pointed-cone fact in Step 1 is classical and is not claimed as new. The claimed contribution is its exact probabilistic and extremal classification for meridian-cut domains, including the positive defect under zero-area cuts.

## Limitations

The result does not concern arbitrary curved boundaries or general spherical subsets: it requires azimuthal preimages of finite unions of intervals. The probability concerns geodesics of the *ambient round sphere*, not intrinsic shortest paths constrained to lie in \(\Omega_E\). The formula is for independent endpoints with a uniform azimuthal marginal; different angular densities can change it. Boundary events and antipodal degeneracies are excluded almost surely, and independent historical validation remains unperformed.

## References

1. M. Lassak, “Width of spherical convex bodies,” *Aequationes Mathematicae* 89 (2015), 555–567; first online 2013-12-06. DOI: 10.1007/s00010-013-0237-3. Open full text: https://link.springer.com/content/pdf/10.1007/s00010-013-0237-3.pdf
2. M. Lassak and M. Musielak, “Reduced Spherical Convex Bodies,” arXiv:1607.00132, first public 2016-07-01. Full text: https://arxiv.org/abs/1607.00132
