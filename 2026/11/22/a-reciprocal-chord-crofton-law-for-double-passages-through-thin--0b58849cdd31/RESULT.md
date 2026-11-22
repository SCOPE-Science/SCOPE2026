# A reciprocal-chord Crofton law for double passages through thin spatial tubes

## Finding
A Euclidean-invariant random line hitting a very thin solid tube about any positively curved planar oval usually produces one connected material segment, but has a probability of *two* disjoint segments that is linear in the tube radius. The sharp coefficient is the reciprocal-chord functional of the enclosed convex region, rather than the usual mean chord length. Moreover the rare line's azimuth, transverse chord offset and rescaled inclination have an explicit joint limiting distribution.

Let \(K\subset\mathbb R^2\) have \(C^3\) strictly convex boundary \(C\), curvature bounded strictly between positive constants, and perimeter \(L=L(C)\). Let \(T_r=\{x\in\mathbb R^3: \operatorname{dist}(x,C)\le r\}\). An unoriented affine line is sampled with the Euclidean invariant measure \(d\sigma(u)\,dA_{u^\perp}\), conditioned on intersecting \(T_r\). Write \(N_r\) for the number of connected intervals comprising the line's intersection with \(T_r\), ignoring null-probability tangencies. For azimuth \(\phi\in[0,\pi)\), let \(e_\phi=(\cos\phi,\sin\phi)\), \(n_\phi=(-\sin\phi,\cos\phi)\), and let \(\ell_\phi(t)>0\) be the Euclidean length of the segment \(K\cap\{x:x\cdot n_\phi=t\}\). Its support offset is \(t\in(t_-(\phi),t_+(\phi))\). Define
\[
J(K)=\frac1\pi\int_0^\pi\int_{t_-(\phi)}^{t_+(\phi)}\frac{2\,dt\,d\phi}{\ell_\phi(t)}.
\]
The integral is finite and positive. Then
\[
\boxed{\Pr(N_r=2\mid N_r\ge1)=\frac{2rJ(K)}{\pi L}+o(r).}
\]
More strongly, given \(N_r=2\), let \(\phi\) be horizontal azimuth, let \(t\) be the perpendicular offset of the *horizontal projection* of the line onto \(\mathbb R^2\), and put \(v=|u_z|/r\) for its unit direction \(u\). The joint conditional law converges weakly to
\[
\boxed{p(\phi,t,v)=\frac{(2-v\ell_\phi(t))_+}{\pi J(K)}\qquad(0\le\phi<\pi,\quad t_-<t<t_+,\quad v\ge0).}
\]
In particular, \(p(\phi,t)=2/(\pi J(K)\ell_\phi(t))\): rare double passages give the **reciprocal** of the chord length as their location weight. This measure integrates to one.

**Ellipse case and inverse consequence.** For the ellipse \(x^2/A^2+y^2/B^2\le1\), with \(A,B>0\) and \(L\) its perimeter, set \(b_\phi=\sqrt{A^2\sin^2\phi+B^2\cos^2\phi}\). One obtains
\[
J(K)=\frac{\pi(A^2+B^2)}{2AB},\qquad
\Pr(N_r=2\mid N_r\ge1)=\frac{r(A^2+B^2)}{AB L}+o(r),
\]
and the limiting azimuth density is
\[
\boxed{p(\phi)=\frac{2(A^2\sin^2\phi+B^2\cos^2\phi)}{\pi(A^2+B^2)}.}
\]
For a circle of radius \(R\) the leading probability is \(r/(\pi R)\), with uniform azimuth. For a noncircular ellipse the ratio of the largest and smallest angular density values is \(\max(A,B)^2/\min(A,B)^2\), so the aspect ratio and principal-axis directions are determined by the rare-event orientation profile (up to the obvious axis symmetries).

## Assumptions and scope
The body \(T_r\) is the closed Euclidean radius-\(r\) neighborhood of the *curve* \(C\times\{0\}\), not the tube about the filled planar region. The orientation law is Haar measure on **unoriented** three-dimensional directions, with Lebesgue measure on each perpendicular offset plane, conditioned on hitting \(T_r\); this is not a uniform distribution on its surface or on a bounding box of lines. The curve has everywhere positive curvature and \(C^3\) smoothness; in particular its chord functions behave like square roots at both tangent endpoints. The limit takes \(r\to0\) for one fixed curve, not a simultaneous high-eccentricity limit. For sufficiently small \(r\), generic intersecting lines have one or two connected components; only the number two enters the theorem.

## Proof
**1. Invariant-line coordinates.** An unoriented spatial direction has uniform horizontal azimuth \(\phi\in[0,\pi)\) and absolute vertical component \(\mu=|u_z|\in[0,1]\), independently uniform in these coordinates. Fix \(\phi,\mu\). The horizontal projection of the oriented line is parallel to \(e_\phi\). Let \(t\) denote its offset across \(n_\phi\), and let \(s\) denote its other coordinate in the plane perpendicular to \(u\), chosen so that increasing vertical height changes \(s\) by \(\sqrt{1-\mu^2}\) times that height. The pair \((t,s)\) has Euclidean area Jacobian one; thus, up to a common constant, invariant line measure is \(\pi^{-1}d\phi\,d\mu\,dt\,ds\). Projecting \(T_r=C+B_r^3\) onto \(u^\perp\) gives exactly the radius-\(r\) planar tube about the orthogonal projection of \(C\).

**2. Local two-branch lens.** For each interior \(t\), the chord \(K\cap(tn_\phi+\mathbb Re_\phi)\) has two distinct endpoints, separated along \(e_\phi\) by \(\ell_\phi(t)\). For \(\mu=rv\) with fixed \(v\), the images of these two endpoints in \(u^\perp\), at fixed \(t\), have their \(s\)-coordinates separated by \(rv\ell_\phi(t)\) **exactly** (the sign is immaterial). Each nearby projected branch contributes an interval in the \(s\) offset coordinate of width \(2r+o(r)\), locally uniformly for \(\phi,t,v\) in compact subsets of the interior domain. Indeed the projected curve branches are smoothly transverse to the \(t\) coordinate, and the normal radius-\(r\) tube changes the \(s\)-halfwidth by \(o(r)\) as \(r,\mu\to0\). Their common offset interval therefore has length \(r(2-v\ell_\phi(t))_++o(r)\). Each line represented by an offset in this overlap meets two distant tubular neighborhoods along its longitudinal parameter, and, for small \(r\) and fixed interior chord, these are distinct segments. Multiplying by \(d\mu=r\,dv\) gives the local limiting double-hit line measure \(r^2(2-v\ell_\phi(t))_+\,d\phi\,dt\,dv/\pi\).

**3. Control of grazing lines and of large inclinations.** Positive upper and lower curvature bounds imply, uniformly in \(\phi\), that \(\ell_\phi(t)\) is comparable to \(\sqrt{\delta_\phi(t)}\) at either support endpoint, where \(\delta_\phi(t)\) is the closer support-distance. Consequently \(1/\ell_\phi(t)\) is integrable uniformly in \(\phi\). For \(v\) bounded, the projected normal-tube intervals have width at most \(2r\) each and their overlap tends pointwise to the displayed lens; dominated convergence applies after removing support strips of width \(\eta\), with the removed normalized contribution bounded by a constant times \(\sqrt\eta\), uniformly for sufficiently small \(r\). For \(\mu\ge Mr\), a double hit requires the two projected sides to approach within \(2r\). The supporting-line curvature comparison confines such offsets to two tangent strips of width \(O((r/\mu)^2)\) for \(\mu\) not too close to one; the remaining projected \(s\)-range is at most \(O(r)\). Integrating gives \(O(r^3\int_{Mr}^1\mu^{-2}d\mu)=O(r^2/M)\). The nearly vertical directions cannot produce two separated line components for sufficiently small \(r\); they contribute no larger order. Letting \(M\to\infty\) yields the full weak limit and total mass
\[
\nu_2(r)=r^2J(K)+o(r^2),\quad\text{since}\quad
\int_0^\infty (2-v\ell)_+\,dv=\frac2\ell.
\]
The same estimates show configurations of extra components have vanishing measure at this scale; the counted event is \(N_r=2\).

**4. All hitting lines.** By projection, the invariant line measure of all hits at direction \(u\) is the area of the radius-\(r\) planar neighborhood of the projected curve. For every fixed nonhorizontal \(u\) this is an embedded convex curve and the area is \(2rL(\pi_u C)\) for sufficiently small \(r\). It is bounded uniformly by \(2rL(\pi_u C)+\pi r^2\), and the projected lengths are bounded by \(L\). Hence dominated convergence, together with the elementary Cauchy average \(\mathbb E_u|\pi_u T|=\pi/4\) for a fixed tangent unit vector \(T\), gives
\[
\nu_{\mathrm{hit}}(r)=2r\mathbb E_u L(\pi_u C)+o(r)=\frac{\pi rL}{2}+o(r).
\]
Dividing the double-hit measure by this expression proves the probability coefficient; dividing its marked measure by \(J(K)\) yields the claimed conditional density.

**5. Ellipse integration.** In orthonormal coordinates parallel/perpendicular to \(e_\phi\), a line at offset \(t\) intersects the ellipse in a chord of length \(\ell_\phi(t)=2AB\,b_\phi^{-1}\sqrt{1-t^2/b_\phi^2}\) for \(|t|<b_\phi\). Therefore
\[
\int_{-b_\phi}^{b_\phi}\frac{2\,dt}{\ell_\phi(t)}
=\frac{b_\phi^2}{AB}\int_{-1}^1\frac{dz}{\sqrt{1-z^2}}
=\frac{\pi b_\phi^2}{AB}.
\]
Integration over \(\phi\) gives \(J(K)=\pi(A^2+B^2)/(2AB)\); normalization gives the azimuth density. Its extrema are proportional to \(A^2\) and \(B^2\), establishing inverse identification.

## Verification
The accompanying standalone `verify_line_tubes.py` recomputes the elliptical reciprocal-chord integral numerically for multiple axis ratios, checks the normalization of the marked density and the exact circle limit, and independently estimates finite-radius double-hit probability by solving the quartic line/torus intersection equation for seeded random line offsets. The finite-radius circle experiment corroborates, but is not used as a substitute for, the limit proof. For example, at circle radius one and tube radius \(0.2\), the computed exact conditional double-hit probability is about \(0.0414384\); at radius \(0.05\) it is about \(0.0131687\), consistent with the derived first-order coefficient \(1/\pi\).

## Relationship to prior work
Classical Cauchy and Crofton formulas, including Slepian's 2011 projected-area treatment, supply the invariant measure and average projected length, but do not count multiple connected line passages through nonconvex spatial tubes. Egan's 2021–2022 *Average Shadows* observes that a torus ray can cross its surface four times, but does not state the thin-tube reciprocal-chord asymptotic or the marked conditional law. The published published-finding corpus torus-shadow phase theorem studies topology and area of **planar orthographic shadows**, not the multiplicity of 3D Crofton line intersections; even its pointwise shadow formulas do not contain the arbitrary-oval reciprocal-chord angular bias. Finch's 2026 random-torus-slice study concerns intersecting **planes**, and a planar racetrack analogue, not the claimed spatial affine-line limit. Specialized historical stereology might contain an equivalent unindexed identity: historical priority is not certified.

## Limitations
The result is first-order asymptotic for thin tubes about planar smooth strictly positively curved closed curves; it does not provide a nonasymptotic probability for general radius, nonsmooth or nonconvex cores, multiple nested cores, noisy orientation inference, or a quantitative convergence rate uniform over varying eccentricity. Independent mathematical validation and exhaustive historical-priority review have not been performed.

## References
- Z. Slepian, *The Average Projected Area Theorem – Generalization to Higher Dimensions*, arXiv:1109.0595 (first public 2011-09-03), https://arxiv.org/abs/1109.0595.
- G. Egan, *Average Shadows*, section on nonconvex solids, 2021–2022, https://www.gregegan.net/SCIENCE/AverageShadows/AverageShadows.html.
- S. Finch, *Slicing a Doughnut at Random*, arXiv:2611.15546 (first public 2026-11-11), https://arxiv.org/abs/2611.15546.
- *Two visibility transitions and a critical hole-area tail for torus shadows*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-two-visibility-transitions-and-a-critical-hole-area-tail-for-tor--128776cbdf5e.
