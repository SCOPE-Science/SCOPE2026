# A cotangent-moment law and marked near-pole facets of random hemispherical polygons

## Finding

Fix an integer \(n\ge3\). Sample independently \(X_1,\ldots,X_n\) in the open northern unit hemisphere of \(\mathbb S^2\), with independent uniform azimuths \(\Phi_i\in[0,2\pi)\) and colatitudes \(R_i\in(0,\pi/2)\) having a common measurable probability density \(g\). Assume
\[
0<m:=\int_0^{\pi/2}g(r)\cot r\,dr<\infty.
\]
Let \(N\) be the north pole, \(K_n\) the shortest-geodesic convex hull, \(I_n=\{N\in\operatorname{int}K_n\}\), and \(D_n=d_{\mathbb S^2}(N,\partial K_n)\) on \(I_n\). Then
\[
\Pr(I_n)=1-\frac n{2^{n-1}},\qquad
\Pr(I_n,D_n<\varepsilon)=\frac{n(n-1)m}{2^{n-2}\pi}\,\varepsilon+o(\varepsilon)
\quad(\varepsilon\downarrow0).
\]

On \(I_n\), the nearest boundary edge is almost surely unique. Write its endpoint-label pair as \(J_1<J_2\). Conditional on \(I_n\cap\{D_n<\varepsilon\}\), the pair is asymptotically uniform among the \(\binom n2\) possibilities. Its ordered colatitudes have a total-variation limit with density
\[
w(r,s)=\frac{g(r)g(s)(\cot r+\cot s)}{2m},\qquad 0<r,s<\pi/2.
\]
Independently, the azimuth \(\Phi_{J_1}\) tends to uniform on \([0,2\pi)\), the sign of the near-antipodal angular deviation tends to a fair sign, and \(D_n/\varepsilon\) tends to uniform on \((0,1)\). The remaining \(n-2\) vertices have their original independent colatitude law and conditional independent uniform azimuths on the semicircle **on the north-pole side of the nearly diametral edge**.

The precise orientation of that semicircle is as follows. Let
\[
\delta=\operatorname{wrap}_{(-\pi,\pi]}(\Phi_{J_2}-\Phi_{J_1}-\pi),\qquad
\theta_k=\operatorname{wrap}_{[0,2\pi)}(\Phi_k-\Phi_{J_1}).
\]
**For \(\delta>0\), each remaining \(\theta_k\) is asymptotically uniform on \((0,\pi)\); for \(\delta<0\), it is asymptotically uniform on \((\pi,2\pi)\).** These orientations follow from the side of the directed near-diametral chord containing the pole. All stated total-variation limits refer to the joint labelled, colatitude, relative-azimuth, sign and rescaled-clearance coordinates; they do not assert total-variation convergence of the unscaled collapsing azimuth difference.

For spherical-area-uniform sampling, \(g(r)=\sin r\), \(m=1\), and \(w(r,s)=\tfrac12\sin(r+s)\). For sampling uniform in the equatorial projected disk, \(g(r)=2\sin r\cos r\), \(m=\pi/2\), so the first-order clearance coefficient increases by exactly the factor \(\pi/2\). Equal cotangent moments give equal first-order coefficients for every fixed \(n\).

## Assumptions and scope

The spherical surface dimension is two; the sample size \(n\ge3\) is fixed as \(\varepsilon\downarrow0\). Azimuths are independent uniform variables and independent of the colatitudes. The density \(g\) may be merely measurable and need not be bounded; the finite positive cotangent moment is essential. The hull has boundary consisting of geodesic minor arcs, which are well defined almost surely. Azimuthal ties, nonunique nearest facets and degenerate supporting lines have probability zero. The pole must be strictly inside the hull in the small-clearance event. The sign convention uses \(J_1<J_2\) and \(\Phi_{J_2}-\Phi_{J_1}-\pi\) in that order; changing the orientation convention interchanges the two semicircles.

## Proof

**1. Gnomonic model and pole inclusion.** The gnomonic projection
\[
(\sin r\cos\phi,\sin r\sin\phi,\cos r)\mapsto(\tan r\cos\phi,\tan r\sin\phi)
\]
sends geodesic minor arcs into Euclidean segments, the geodesic hull into the planar convex hull and the north pole into the origin. The pole belongs to the hull interior exactly when the independent azimuths are not confined to an open semicircle. The complementary event has probability \(n2^{-(n-1)}\): each containing semicircle is uniquely anchored by its initial sample direction almost surely, and each of the other \(n-1\) directions has probability \(1/2\) of falling in that semicircle. A Euclidean supporting line at distance \(\rho\) from the origin corresponds to a great circle at spherical distance \(\arctan\rho\) from the pole. Thus the geodesic pole-clearance event is a planar hull-edge clearance event with threshold \(\tau=\tan\varepsilon\).

**2. A candidate near-antipodal edge.** Set \(a=\tan r\), \(b=\tan s\), \(\tau=\tan\varepsilon\), and suppose \(a,b>\tau\). Elementary tangency to the disk centered at the origin with radius \(\tau\) shows that the segment joining the two projected endpoints meets the disk precisely when its angular separation is at least
\[
\arccos(\tau/a)+\arccos(\tau/b).
\]
Writing its signed deviation from opposition as \(\delta\), the condition is
\[
|\delta|\le H_\varepsilon(r,s)
:=\arcsin(\tau\cot r)+\arcsin(\tau\cot s).
\]
For fixed \(r,s>0\), \(H_\varepsilon(r,s)/\varepsilon\to\cot r+\cot s\). The bound \(\arcsin u\le(\pi/2)u\) gives a dominating constant times \(\cot r+\cot s\) when each argument is at most one. Points with colatitude \(R\le\varepsilon\) have probability
\[
\Pr(R\le\varepsilon)\le\tan\varepsilon\int_0^\varepsilon g(r)\cot r\,dr=o(\varepsilon),
\]
so the exceptional tiny-radius contribution vanishes to first order without additional regularity assumptions on \(g\). Since the azimuth difference has constant density, the candidate probability given \(r,s\) is \(H_\varepsilon(r,s)/\pi\).

**3. Supporting orientation and the edge coefficient.** For fixed positive endpoint radii and \(\delta\to0\), the chord approaches a line through the origin. It is a supporting edge on the side containing the origin exactly when all other vertices lie in the corresponding *pole-side* semicircle. To identify its orientation without ambiguity, rotate so \(\Phi_{J_1}=0\), place the first projected endpoint at \((a,0)\) and the second at \(b(\cos(\pi+\delta),\sin(\pi+\delta))\). For \(\delta>0\) the second endpoint lies below the first azimuth axis. Taking the determinant of the directed chord vector with the vector from its first endpoint to the origin shows that the origin is on the side above the limiting diameter; the pole-side semicircle therefore has relative azimuths \((0,\pi)\). For \(\delta<0\), the determinant reverses and the pole-side semicircle is \((\pi,2\pi)\). This is the sign convention stated in the Finding. Each other azimuth lies in that semicircle with probability \(1/2\), independently, yielding a supporting probability tending to \(2^{-(n-2)}\) for either sign. Away from degenerate configurations, the candidate segment is exposed, its closest point lies inside the segment and the origin lies on its interior-hull side when \(\delta\) is small.

For one unordered label pair the leading probability is therefore
\[
\frac{\varepsilon}{\pi}\,2^{-(n-2)}
\int_0^{\pi/2}\int_0^{\pi/2}
 g(r)g(s)(\cot r+\cot s)\,dr\,ds
=\frac{2m\varepsilon}{2^{n-2}\pi}+o(\varepsilon).
\]
For two distinct label pairs, their independent angular near-antipodality constraints have intersection probability \(O(\varepsilon^2)\) on any fixed positive-radial cutoff, even if they share one label. The omitted small-radial contribution is \(o(\varepsilon)\) by the cotangent moment. It follows by taking \(\varepsilon\downarrow0\) first and then shrinking the radial cutoff that overlaps of two candidate near-pole edges contribute \(o(\varepsilon)\). Summing over \(\binom n2\) pairs proves the scalar coefficient and asymptotic uniqueness of the nearest marked edge.

**4. The conditional marked limit.** For a fixed label pair and compactly restricted positive \(r,s\), the great-circle clearance has the local expansion
\[
D_n=\frac{|\delta|}{\cot r+\cot s}+o(|\delta|),
\]
when the pair is a supporting edge. In the change of variables \(u=D_n/\varepsilon\), the Jacobian from \(|\delta|\) tends to \(\varepsilon(\cot r+\cot s)\), uniformly on compact radial sets. The event that every remaining point lies on the pole side converges almost surely to the appropriate semicircle condition in Step 3. Thus the limiting density factors into a uniform label-pair choice, the endpoint-colatitude density \(w\), independent uniform first azimuth, a fair sign, an independent uniform \(u\in(0,1)\), and independent original colatitude laws with uniform azimuths on the **correctly oriented** semicircle. The density \(w\) integrates to one since \(\int\int g(r)g(s)(\cot r+\cot s)\,dr\,ds=2m\). The cotangent domination, the \(o(\varepsilon)\) small-radius estimate and asymptotically negligible double-edge events give convergence of the normalized marked densities in \(L^1\), first on compact radial sets and then globally. Scheffé's lemma yields joint total-variation convergence.

**5. Specializations.** For \(g(r)=\sin r\), the cotangent moment is \(m=\int_0^{\pi/2}\cos r\,dr=1\), and \(g(r)g(s)(\cot r+\cot s)=\sin(r+s)\). For \(g(r)=2\sin r\cos r\), the moment is \(2\int_0^{\pi/2}\cos^2r\,dr=\pi/2\). Substitution into the preceding formulas proves both examples.

## Verification and limits

The existing standalone `check.py` tests the classical pole-containment probability and finite-small-\(\varepsilon\) scalar clearance coefficients at sample sizes \(n=3,4,5,6\) with seeded numerical experiments. It also checks a selected-edge colatitude observable. Those finite simulations do **not** establish the asymptotic theorem or test the signed semicircle orientation. The orientation is independently determined by the directed-chord determinant in Step 3: for example, endpoint azimuths \(0\) and \(\pi+0.02\), with a third azimuth \(\pi/2\), give a small origin-containing triangle whose nearly diametral edge has positive \(\delta\) and whose third vertex lies in \((0,\pi)\). This is why the sign convention matters. The proof above, not a success marker from a finite checker, supports the infinite and total-variation statements.

The theorem does not cover anisotropic azimuthal laws, radially atomic input, infinite cotangent moment, growing-\(n\) joint limits or higher-dimensional spherical hulls. The marked total-variation convergence uses rescaled local variables; the collapsing raw relative azimuth does not converge in total variation to a nonsingular law.

## Relationship to primary literature

Wendel's 1962 containment formula is used as known background. Bárány, Hug, Reitzner and Schneider (2015/2017) study expectations of global halfsphere-hull face and volume characteristics and growing-sample approximation; Kabluchko (2020) studies halfsphere and Poisson-zero-polytope face expectations. Neither stated setting directly provides the present fixed-\(n\) inside-clearance derivative and full marked configuration law. The published marked Wendel-law result for symmetric planar curves instead studies large-\(n\) center *exclusion* and its outer clearance; the published antipodal cap boundary-layer law studies two-point separation under a moving cap radius. The full 1970 text of H. Carnal, on convex hulls of rotationally symmetric points, was not available through open sources or disconnected authorized institutional access. Its possible historical overlap is an explicit residual originality risk rather than a proof of novelty. No independent historical-priority certification is claimed.

## References

1. J. G. Wendel, “A Problem in Geometric Probability,” *Mathematica Scandinavica* 11 (1962), 109–112, https://doi.org/10.7146/math.scand.a-10655.
2. I. Bárány, D. Hug, M. Reitzner and R. Schneider, “Random points in halfspheres,” arXiv:1505.04672 (2015), https://arxiv.org/abs/1505.04672.
3. Z. Kabluchko, “Expected f-vector of the Poisson zero polytope and random convex hulls in the half-sphere,” *Mathematika* (2020), https://doi.org/10.1112/mtk.12056.
4. P. Bürgisser, F. Cucker and M. Lotz, “Coverage processes on spheres and condition numbers for linear programming,” arXiv:0712.2816, https://arxiv.org/abs/0712.2816.
5. H. Carnal, “Die konvexe Hülle von n rotationssymmetrisch verteilten Punkten,” *Z. Wahrscheinlichkeitstheorie* 15 (1970), 168–176, https://doi.org/10.1007/BF00531885.
