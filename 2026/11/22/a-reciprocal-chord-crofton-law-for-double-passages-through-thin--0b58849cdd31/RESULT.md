# A reciprocal-chord Crofton law for double passages through thin spatial tubes

Let \(K\subset\mathbb R^2\) be a compact convex region with \(C^3\) boundary \(C\) of strictly positive curvature, and perimeter \(L\). Embed the plane at height zero and set \(T_r=\{x\in\mathbb R^3:\operatorname{dist}(x,C)\le r\}\). Use the invariant measure on unoriented affine lines: probability Haar measure on directions and Lebesgue area on the corresponding orthogonal offset plane. Let \(N_r\) be the number of connected intervals of intersection with \(T_r\), ignoring tangencies of line measure zero.

For \(0\le\phi<\pi\), write \(e_\phi=(\cos\phi,\sin\phi)\), \(n_\phi=(-\sin\phi,\cos\phi)\), and let \(\ell_\phi(t)\) be the length of the chord of \(K\) cut out by \(x\cdot n_\phi=t\), for \(t_-(\phi)<t<t_+(\phi)\). Set
\[
 J(K)=\frac1\pi\int_0^\pi\int_{t_-(\phi)}^{t_+(\phi)}\frac{2}{\ell_\phi(t)}\,dt\,d\phi.
\]
Then \(0<J(K)<\infty\), and
\[
 \Pr(N_r=2\mid N_r\ge1)=\frac{2rJ(K)}{\pi L}+o(r).
\]
Conditional on \(N_r=2\), the azimuth, horizontal projection offset, and rescaled inclination \((\phi,t,v)\), with \(v=|u_z|/r\) for unit line direction \(u\), converge in law to the density
\[
 p(\phi,t,v)=\frac{(2-v\ell_\phi(t))_+}{\pi J(K)}
\quad (t_-<t<t_+,\ v\ge0),
\]
zero outside the indicated chord and inclination domain. In particular the azimuth–offset density is \(2/(\pi J(K)\ell_\phi(t))\). These statements hold for a fixed region as \(r\downarrow0\).

## Proof

**Coordinates.** Represent the unoriented direction by choosing its horizontal component along \(e_\phi\), so its signed vertical component is \(\epsilon\mu\), with \(\mu=|u_z|\), \(\epsilon\in\{-1,1\}\) and \(\alpha=\sqrt{1-\mu^2}\). Apart from a null set this gives uniform independent \(\phi\in[0,\pi)\), \(\mu\in[0,1]\), and sign. Reflection about the plane makes the signs equivalent for the event and marks, so use the positive sign. With horizontal longitudinal coordinate \(q\) and height \(z\), set \(s=\alpha z-\mu q\), the offset in the unit direction \(-\mu e_\phi+\alpha e_z\) perpendicular to \(u\). The other orthogonal offset is \(t\). Line measure is therefore \(\pi^{-1}d\phi\,d\mu\,dt\,ds\). The line has height \(z(q)=h+m q\) with \(h=s/\alpha\), \(m=\mu/\alpha\) for \(\mu<1\). If \(f\) is signed distance to \(C\) in the plane, positive on the exterior, membership in the tube is exactly
\[
 g(q)=f(qe_\phi+tn_\phi)^2+(h+m q)^2\le r^2.
\]
There is a fixed tubular neighborhood of \(C\) on which the signed distance has uniformly bounded second derivatives, by compactness and the normal coordinate map. Fix such a neighborhood. In expressions such as \(f'\) and \(f''\), derivatives are along \(q\).

**A cutoff on inclination.** If \(m\ge A\sqrt r\) for a fixed sufficiently large \(A\), any two hit parameters \(q_1,q_2\) satisfy \(|q_2-q_1|\le 2r/m\) from the height constraint. The whole interval is in the fixed tubular neighborhood for small \(r\) by the distance Lipschitz bound. Interpolation with bounded \(f''\) there yields \(|f|\le r+C_1(r/m)^2\) between the hit points, with a constant \(C_1\) independent of the line. On that interval,
\[
 g''/2=(f')^2+f f''+m^2\ge m^2-C_2[r+C_1(r/m)^2]>0
\]
for sufficiently large \(A\). Thus the sublevel set contains the interval between any two hit points. A vertical line also has a single interval if it hits. In particular any line with at least two components has \(\mu\le A\sqrt r\).

**Uniform planar bounds.** Near each support point in direction \(\pm n_\phi\), the boundary in tangent/normal coordinates is a graph whose vertical drop from support is comparable to the squared tangential displacement, with the absolute graph slope comparable to that displacement. Indeed the graph has zero slope at support and curvature bounded between positive constants, so its second derivative in a sufficiently small neighborhood is bounded above and below by positive constants in absolute value. The neighborhoods and constants can be chosen uniformly by compactness. Away from these neighborhoods, both endpoints of each chord are transverse with a uniform bound on the absolute tangent slope away from zero, expressed equivalently as a uniform lower bound on the absolute \(e_\phi\)-component of the normal. With \(\delta=\min(t-t_-,t_+-t)\) at an interior offset, these facts give \(\ell_\phi(t)\ge c\sqrt\delta\) and an absolute \(e_\phi\)-component of the normal at each endpoint of at least \(c\sqrt\delta\), with a fixed \(c>0\).

Here are the corresponding bounds for the planar band \(|f|\le r\) along each chord line. This band is the difference of the outer parallel convex body and the interior of the eroded convex body. For small \(r\) the two parallel boundaries are the normal offsets of \(C\); their curvatures are \(\kappa/(1\pm r\kappa)\), hence have uniform positive bounds, and their support offsets differ from those of \(C\) by at most \(r\). If \(\delta>D r\), for a sufficiently large fixed \(D\), the band is thus two intervals separated by an eroded chord of length at least \(c'\sqrt\delta\). At any band point, its foot on \(C\) has transverse offset within \(r\) of \(t\), so the normal-component bound just proved implies \(|f'|\ge c''\sqrt\delta\). The foot is on the appropriate chord branch, and \(f'\) has constant sign on each band interval by continuity. Consequently every point of a band interval is at longitudinal distance \(O(r/\sqrt\delta)\) from that interval's chord endpoint where \(f=0\). For \(|t-t_\pm|\le D r\), every planar band point instead has \(|q-q_\pm|\le C_3\sqrt r\), where \(q_\pm\) is the respective support point's longitudinal coordinate. The latter assertion follows by applying the quadratic drop estimate to the foot on \(C\), which is within transverse distance \((D+1)r\) of support, and then adding the distance at most \(r\) from foot to band point. Outside the support enlarged by \(r\) there is no hit.

**Grazing control and tightness.** In the support strips \(|t-t_\pm|\le D r\), a multiple hit has \(\mu\le A\sqrt r\) by the inclination cutoff. From \(|z|\le r\) at any hit and the bound on \(|q-q_\pm|\), its offset satisfies \(|s+\mu q_\pm|\le r+\mu C_3\sqrt r=O(r)\). The line measure of multiple hits in these strips is therefore \(O(r^{5/2})\), including offsets just outside the planar support.

If \(\delta>D r\), then \(g''/2\ge (c'')^2\delta-C_2 r>0\) on each planar band interval, enlarging \(D\) if needed. There is at most one hit interval per band interval. Two components must come from opposite band intervals, so the height constraint and their separation imply \(\mu\le m\le C_4 r/\sqrt\delta\). If \(q_0\) is either chord endpoint, the hit thereabouts then requires
\[
 |s+\mu q_0|\le r+O(\mu r/\sqrt\delta)=O(r),
\]
uniformly in this region. Thus after rescaling by \(r^{-2}\), the measure of multiple hits with \(\delta\le\eta\) is \(O(\sqrt\eta)+O(\sqrt r)\), integrating \(O(r)\) in \(s\) and \(C_4r/\sqrt\delta\) in \(\mu\) outside the support strips. For \(\mu>Mr\), the normalized measure outside the strips is \(O(1/M)\): at each \(\mu\) the allowed \(t\)-range has width \(O((r/\mu)^2)\), and the \(s\)-width is \(O(r)\), so integrate \(O(r^3\mu^{-2})\,d\mu\). All bounds are uniform in azimuth. Any hits with more than two components are confined to the negligible support strips; no exact two-component bound in the strips is needed.

**Interior limit.** For a fixed interior offset, let \(q_1,q_2\) be the chord endpoints and take \(\mu=rv\). The branch containing \(q_i\) gives an interval of hit offsets \(s\) containing \([-\mu q_i-\alpha r,-\mu q_i+\alpha r]\), because \(f=0\) at \(q_i\). Conversely any offset hitting that branch satisfies \(|s+\mu q_i|\le\alpha r+O(\mu r)\) on compact subsets of the interior chord domain since its hit lies within \(O(r)\) of \(q_i\). The separation of the two displayed interval centers is \(rv\ell_\phi(t)\). Thus the measure in \(s\) of their joint hit is \(r(2-v\ell_\phi(t))_++O(r^2)\) on compact interior domains with bounded \(v\). Each band gives only one interval there, so this is the exact two-component event up to the stated estimate in length. Including \(d\mu=r\,dv\), the \(r^{-2}\)-normalized marked measure converges on the interior to \(\pi^{-1}(2-v\ell_\phi(t))_+\,d\phi\,dt\,dv\). The two uniform bounds above and the integrable square-root chord bound extend convergence to bounded continuous tests and to total mass. In particular the mass of this density is \(J(K)\), because \(\int_0^\infty(2-v\ell)_+\,dv=2/\ell\).

**All hits.** At each direction \(u\) the shadow is precisely the planar radius-\(r\) neighborhood of the projected curve \(\pi_u C\). When the direction is nonhorizontal, projection of the plane is invertible; the image is a smooth positively curved oval. For all sufficiently small \(r\) for that fixed direction, the neighborhood has area \(2rL(\pi_u C)\), by the inner and outer normal strip formula. For arbitrary \(r\), its area is at most \(2rL(\pi_u C)+\pi r^2\): the outer parallel area gain is \(rL(\pi_u C)+\pi r^2\), and the inner gain up to erosion distance \(r\) is at most \(rL(\pi_u C)\) by coarea and perimeter monotonicity for nested convex planar bodies. Also \(L(\pi_u C)\le L\). For a fixed unit tangent, its projected length is \(\sqrt{1-z^2}\) for \(z\) uniform on \([0,1]\), so its expected length is \(\pi/4\). Dominated convergence and tangent integration now give total hit measure \(\pi r L/2+o(r)\). Dividing the measure \(r^2J(K)+o(r^2)\) of two-component hits by this expression gives the probability, and normalizing the limiting marked measure gives the stated law.

## Ellipses and the inverse observation

For \(x^2/A^2+y^2/B^2\le 1\), put \(b_\phi=\sqrt{A^2\sin^2\phi+B^2\cos^2\phi}\). Completing the quadratic along the chord gives \(\ell_\phi(t)=2AB\,b_\phi^{-1}\sqrt{1-t^2/b_\phi^2}\) for \(|t|<b_\phi\). Thus \(\int 2\,dt/\ell_\phi(t)=\pi b_\phi^2/(AB)\). Consequently
\[
 J(K)=\frac{\pi(A^2+B^2)}{2AB},\qquad
 \Pr(N_r=2\mid N_r\ge1)=\frac{r(A^2+B^2)}{AB L}+o(r),\qquad
 p(\phi)=\frac{2b_\phi^2}{\pi(A^2+B^2)}.
\]
For a radius-\(R\) circle this is \(r/(\pi R)+o(r)\) with uniform azimuth. For a noncircular ellipse the limiting profile determines principal-axis directions and aspect ratio, since its extrema occur at the principal axes and their ratio is the square of the aspect ratio. An orientation-only profile does not fix scale.

## Verification, context and limits

The proof controls the event of exactly two components and the normalization without numerical assumptions. The accompanying finite diagnostic checks ellipse integrals and uses a seeded quartic line–torus computation at fixed radii; those tests do not prove the asymptotic. The law assumes invariant affine lines conditioned on hitting the tube about the boundary, not lines drawn from a surface sampling rule, nor a tube about the filled planar region. It supplies no claim for nonsmooth or nonconvex cores, or a limit uniform over eccentricities. The denominator uses classical projection averaging. Nonconvex shadow calculations and plane sections can exhibit related geometries, but neither replacing the tube by its shadow nor counting all hitting lines alone yields the marked two-component law. Historical priority is not certified.

Related references: Z. Slepian, *The Average Projected Area Theorem – Generalization to Higher Dimensions*, [arXiv:1109.0595](https://arxiv.org/abs/1109.0595); G. Egan, [*Average Shadows*](https://www.gregegan.net/SCIENCE/AverageShadows/AverageShadows.html), nonconvex solids; S. Finch, *Slicing a Doughnut at Random*, [arXiv:2611.15546](https://arxiv.org/abs/2611.15546).
