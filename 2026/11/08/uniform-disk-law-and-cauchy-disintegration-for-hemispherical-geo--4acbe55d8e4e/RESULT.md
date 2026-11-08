# Uniform-disk law and Cauchy disintegration for hemispherical geodesic midpoints

## Finding

Let \(H=\{(x_1,x_2,x_3)\in S^2:x_3\ge0\}\) be the closed unit northern hemisphere, and let \(X,Y\) be independent, normalized spherical-area-uniform points of \(H\). Almost surely \(X\ne-Y\). Put
\[
M=\frac{X+Y}{\|X+Y\|},\qquad \Delta=\arccos(X\cdot Y)\in(0,\pi),\qquad Z=M_3.
\]
Thus \(M\) is the midpoint of the unique minimizing spherical geodesic. Let \(\Pi(M)=(M_1,M_2)\) be its *orthogonal* projection onto the equatorial plane, not its stereographic or gnomonic projection.

**Exact planar midpoint law.** The random point \(\Pi(M)\) is *uniform by Euclidean area* on the unit disk. Equivalently, the spherical-area density of \(M\) is \(Z/\pi\) on \(H\), \(Z\) has density \(2z\) for \(0<z<1\), and \(1-Z^2\) is uniform on \([0,1]\).

**Complete joint disintegration.** At an interior midpoint \(m\), write \(z=m_3\in(0,1)\), \(s=\sqrt{1-z^2}\), and take the unit tangent vectors \(e_1=(e_3-zm)/s\), \(e_2=m\times e_1\). The ordered endpoint pair has the unique representation
\[
X=\cos t\,m+\sin t\,v,\quad Y=\cos t\,m-\sin t\,v,\quad
v=\cos\phi\,e_1+\sin\phi\,e_2,
\]
where \(0<t<\pi/2\), \(0\le\phi<2\pi\). Set \(w=\sin^2t\), and
\[
q(z,\phi)=\frac{z^2}{z^2+(1-z^2)\cos^2\phi}.
\]
The joint probability measure of \((M,\phi,w)\), with reference measure spherical area \(d\sigma(m)\,d\phi\,dw\), has the constant density
\[
\boxed{\frac{1}{2\pi^2}\,\mathbf1_{\{m\in H^\circ,\ 0<w<q(z,\phi)\}}.}
\]
In particular,
\[
\boxed{f(\phi\mid Z=z)=\frac{z}{2\pi\{z^2+(1-z^2)\cos^2\phi\}},\qquad
w\mid(z,\phi)\sim\operatorname{Unif}[0,q(z,\phi)].}
\]
After reduction modulo \(\pi\), the variable \(\tan\phi\) is Cauchy with scale \(1/z\). Moreover
\[
\boxed{\mathbb E[\cos^2\phi\mid Z=z]=\frac{z}{1+z},\qquad
\mathbb E[\cos^2\phi]=2\log2-1.}
\]
Thus the theorem gives an exact disk/Cauchy/uniform-factorized method of sampling an *ordered independent* uniform hemispherical endpoint pair.

**Geodesic-length law.** Independently of the preceding marginal calculations, the complete length distribution is
\[
\boxed{f_\Delta(\delta)=\left(1-\frac\delta\pi\right)\sin\delta\quad(0<\delta<\pi),}
\]
with \(\mathbb E[\Delta]=4/\pi\) and \(\mathbb E[\Delta^2]=2\).

**Dimension rigidity.** For an upper hemisphere of \(S^{d-1}\subset\mathbb R^d\), two independent surface-uniform endpoints and the same geodesic midpoint operation yield a midpoint whose orthogonal projection onto the equatorial \((d-1)\)-ball is uniform **if and only if \(d=3\)**, for every integer \(d\ge2\).

## Assumptions and scope

All spheres have radius one; endpoints are sampled by normalized *surface* measure, not by volume in a solid hemisphere or by uniform chord/line measure. The midpoint uses the shorter intrinsic geodesic. Coincident and antipodal endpoint pairs, midpoint at the pole or equator, and nonunique tangent frames have probability zero; all density assertions are on interiors or are understood almost everywhere. The ordered pair convention matters when reconstructing endpoints; exchanging endpoints sends \(\phi\) to \(\phi+\pi\). The dimension assertion concerns orthogonal projection and the same independent-uniform-endpoint model in every dimension.

## Proof

**1. Full-sphere midpoint coordinates.** For two independent points on the full \(S^2\), rotational invariance makes the midpoint \(m\) uniform on \(S^2\) and the ordered tangent direction \(\phi\) uniform on its tangent circle, conditional on the half-separation \(t=\Delta/2\). Also \(X\cdot Y\) is uniform on \([-1,1]\), so the density of \(t\) is \(\sin(2t)\,dt\), \(0<t<\pi/2\). Hence the full-sphere joint law equals
\[
\frac{d\sigma(m)}{4\pi}\frac{d\phi}{2\pi}\sin(2t)\,dt.
\]
The endpoint event \(X,Y\in H\) has probability \(1/4\), by independence and hemisphere symmetry. Conditioning multiplies the preceding density by four on the admissible region.

**2. Endpoint positivity and the constant-density transformation.** With \(z=m_3\) and \(s=\sqrt{1-z^2}\), the two third coordinates are \(z\cos t\pm s\cos\phi\sin t\). They are both nonnegative precisely when
\[
\tan t\le\frac{z}{s|\cos\phi|},
\]
with the evident infinite-bound convention when \(\cos\phi=0\). Since \(w=\sin^2t\) satisfies \(dw=\sin(2t)\,dt\), this condition is exactly \(0<w<q(z,\phi)\), and the stated constant joint density \(1/(2\pi^2)\) follows. This is a genuine joint disintegration, not a marginal ansatz.

**3. Midpoint and tangent-angle laws.** Integrating over \(w\) gives the joint midpoint/direction density \(q(z,\phi)/(2\pi^2)\). The elementary integral, valid for every \(0<z\le1\), is
\[
\int_0^{2\pi}\frac{d\phi}{z^2+(1-z^2)\cos^2\phi}=\frac{2\pi}{z}.
\]
It follows by dividing the circle into four quadrants and substituting \(u=\tan\phi\). Thus \(f_M(m)=z/\pi\). In equatorial Cartesian coordinates \(u=(m_1,m_2)\), spherical area satisfies \(d\sigma(m)=d^2u/z\); therefore \(f_M(m)d\sigma=d^2u/\pi\), proving uniformity on the unit disk and \(f_Z(z)=2z\). Dividing the midpoint/direction joint density by \(z/\pi\) proves the conditional angular law. On either half-turn interval \(\phi\in(-\pi/2,\pi/2)\) modulo \(\pi\), substitution \(a=\tan\phi\) yields normalized density \(z/\{\pi(1+z^2a^2)\}\), the claimed Cauchy distribution. Conditional \(w\) is uniform by constancy of the joint density.

For the conditional angular moment, use
\[
\frac{\cos^2\phi}{z^2+(1-z^2)\cos^2\phi}=
\frac{1}{1-z^2}\left(1-\frac{z^2}{z^2+(1-z^2)\cos^2\phi}\right).
\]
Integration gives \(\mathbb E[\cos^2\phi\mid Z=z]=z/(1+z)\). Integrating this against \(2z\,dz\) gives \(2\log2-1\).

**4. Geodesic length.** Before hemisphere conditioning, \(\Delta\) has density \(\tfrac12\sin\delta\). For two fixed unit vectors of mutual angle \(\delta\), a uniformly rotated north pole sees both third coordinates positive with probability \((\pi-\delta)/(2\pi)\): the admissible poles form a spherical lune of area \(2(\pi-\delta)\). Conditioning on the pair lying in the hemisphere multiplies by four. Therefore \(f_\Delta(\delta)=(1-\delta/\pi)\sin\delta\). Direct integration gives the first and second moments as stated.

**5. Dimension rigidity.** On \(S^{d-1}\), rotational invariance makes the *unconditioned* pair midpoint uniform. At the north pole \(m=e_d\), the endpoints are always in the northern hemisphere whenever their midpoint is \(m\), because each has height \(\cos t>0\). Continuity of the conditioned midpoint density near the pole follows from dominated convergence in the rotationally invariant midpoint/tangent/half-distance disintegration. Hence its pole density is \(4/\sigma_{d-1}\), where \(\sigma_{d-1}=2\pi^{d/2}/\Gamma(d/2)\). If orthogonal projection were uniform in the equatorial unit ball of volume \(\kappa_{d-1}=\pi^{(d-1)/2}/\Gamma((d+1)/2)\), its corresponding spherical density at the pole would be \(1/\kappa_{d-1}\). Necessarily
\[
\frac{\sigma_{d-1}}{\kappa_{d-1}}=
2\sqrt\pi\frac{\Gamma((d+1)/2)}{\Gamma(d/2)}=4.
\]
This ratio is strictly increasing with \(d>0\) since its logarithmic derivative is half the positive difference of digamma values at \((d+1)/2\) and \(d/2\). It equals four exactly at \(d=3\). The preceding direct density computation proves sufficiency in that dimension, completing the if-and-only-if statement.

## Verification

The proof is exact; the accompanying executable `check_midpoint.py` supplies independent Monte Carlo checks, not a substitute for any analytic argument. It directly samples 660,000 ordered endpoint pairs and tests projected squared-radius quantiles, midpoint-height and length moments, the exact length CDF, and the conditional tangent-angle identity. A separate factorized disk/Cauchy/uniform sampler generates 340,000 ordered pairs and tests hemisphere support, endpoint height means, endpoint cross moment and length mean. Elementary gamma-function tests compare the pole-density criterion for ambient dimensions 2 through 25. The checker prints `HEMISPHERE_GEODESIC_MIDPOINT_UNIFORM_DISK_AND_CAUCHY_OK` if all specified assertions hold. Execute from the package directory using `python check_midpoint.py` with NumPy installed.

## Relationship to prior work

Bárány, Hug, Reitzner and Schneider (arXiv:1505.04672, first public version 18 May 2015) study spherical convex hulls of independent points in halfspheres, including facet counts, surface area, mean width, volume and approximation. That important same-domain study does not state a two-point geodesic-midpoint pushforward or the disk/Cauchy joint law. Gille (2005, DOI 10.3844/jmssp.2005.24.28) obtains *Euclidean straight-line* chord-length densities of a solid hemisphere under isotropic-line sampling; it uses a different sample space and does not imply the area-uniform *spherical surface endpoint* midpoint distribution. Both source texts were checked for the relevant objects and results. The use of spherical midpoint parametrization, the sine separation density, and the disk Jacobian is classical; the asserted contribution is their evaluated conditional joint law, its Cauchy factorization and its dimension-specific uniform-projection consequence, not these classical ingredients.

## Limitations

The result does not extend the uniform-disk conclusion to arbitrary spherical caps or other sampling weights. The uniqueness statement is restricted to orthogonal projections of midpoint distributions for independent area-uniform endpoint pairs; alternative projection maps may have other equal-area properties. Searches cannot establish absolute historical uniqueness; older integral-geometric or directional-statistical sources may encode equivalent transformations. No independent mathematical audit has been performed. The numerical checks are finite and do not certify the infinite statements.

## References

1. I. Bárány, D. Hug, M. Reitzner, R. Schneider, *Random points in halfspheres*, arXiv:1505.04672v1 (18 May 2015), https://arxiv.org/abs/1505.04672 ; open manuscript https://arxiv.org/pdf/1505.04672 .
2. W. Gille, *Chord Length Distributions of the Hemisphere*, *Journal of Mathematics and Statistics* **1** (2005), 24–28, published 31 March 2005, DOI 10.3844/jmssp.2005.24.28, https://thescipub.com/jmss/jmssp.2005.24.28.pdf .
