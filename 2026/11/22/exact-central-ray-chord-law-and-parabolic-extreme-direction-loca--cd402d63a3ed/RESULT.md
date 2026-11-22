# Exact central-ray chord law and parabolic extreme-direction localization for the Steinmetz bicylinder

## Finding
Let the unit **Steinmetz bicylinder** be the solid intersection of two perpendicular circular cylinders,
\[
K=\{(x,y,z)\in\mathbb R^3:x^2+z^2\le1,\quad y^2+z^2\le1\}.
\]
Select a direction \(U\) uniformly from the unit sphere \(S^2\). Let \(L\) be the Euclidean length of the entire center-passing line segment \(K\cap\{sU:s\in\mathbb R\}\). This is *not* a motion-invariant line conditioned to intersect the solid: every sampled line here passes through the origin.

Put \(T=\min(|U_x|,|U_y|)\). Then
\[
L=\frac{2}{\sqrt{1-T^2}},\qquad 2\le L\le2\sqrt2.
\]
For any \(2<\ell<2\sqrt2\) define
\[
t=\sqrt{1-\frac4{\ell^2}},\qquad s=\sqrt{1-2t^2}=\sqrt{\frac8{\ell^2}-1}.
\]
The **complete central-ray length distribution** is
\[
\boxed{\Pr(L>\ell)=\frac4\pi\left[\arctan s-t\arctan\left(\frac{s}{t}\right)\right].}
\tag{1}
\]
It equals \(1\) for \(\ell\le2\) and \(0\) for \(\ell\ge2\sqrt2\). On the open support, its density is
\[
\boxed{f_L(\ell)=\frac{16}{\pi\ell^3t}\arctan\left(\frac{s}{t}\right).}
\tag{2}
\]
Both endpoints have sharp fractional laws:
\[
\boxed{\Pr(L\le2+\varepsilon)=2\sqrt\varepsilon-\frac2\pi\varepsilon+O(\varepsilon^{3/2}),}
\tag{3}
\]
\[
\boxed{\Pr(L>2\sqrt2-\varepsilon)=\frac4{3\pi2^{3/4}}\varepsilon^{3/2}+O(\varepsilon^{5/2}).}
\tag{4}
\]
Here all limits in \(\varepsilon\) are one-sided as \(\varepsilon\downarrow0\), with the cylinder radius fixed at one.

The long-chord law has a **marked parabolic localization**. For an upper length threshold \(\ell\uparrow2\sqrt2\), let \(h=8/\ell^2-1\downarrow0\). Express \(U\) using its horizontal azimuth \(\phi\in[0,2\pi)\) and vertical coordinate \(z=U_z\):
\[
U=(\sqrt{1-z^2}\cos\phi,\sqrt{1-z^2}\sin\phi,z).
\]
On the rare event \(L>\ell\), take the unique nearby diagonal azimuth \(\phi_J=\pi/4+J\pi/2\), where \(J\in\{0,1,2,3\}\), and put \(q=\phi-\phi_J\), chosen in \((-\pi/4,\pi/4)\). Then, **in total variation**, jointly
\[
\boxed{\left(J,\frac qh,\frac z{\sqrt h}\right)\ \Longrightarrow\ (J_*,A,B),}
\tag{5}
\]
where \(J_*\) is uniform on four labels and independent of \((A,B)\), and the latter has constant density \(3/4\) on the exact parabolic region
\[
\boxed{\mathcal D=\{(a,b)\in\mathbb R^2:2|a|+b^2<1\},}\qquad \operatorname{area}(\mathcal D)=\frac43.
\tag{6}
\]
The four upper-endpoint directions are precisely \((\pm1/\sqrt2,\pm1/\sqrt2,0)\). Statements (1)–(6), taken together, constitute one distribution-and-localization theorem.

## Assumptions and scope
The two cylinders are infinitely extended along their axes, have congruent circular cross sections, and meet orthogonally at their common center. The intersection is compact, convex and centrally symmetric. Probability refers to normalized spherical surface area, equivalently Haar-uniform undirected orientations. The chord is pinned to the center; its distribution is different from the conventional Crofton distribution of noncentral random lines. At exact threshold equality the distinction between \(>\) and \(\ge\) is immaterial because the law has no endpoint atoms. Arc tangent values in (1)–(2) are principal nonnegative angles. For radius \(R>0\), all length thresholds rescale by \(R\).

## Proof
**1. Radial geometry and sharp support.** A point \(rU\) belongs to \(K\) exactly when
\[
r^2(U_x^2+U_z^2)\le1,\qquad r^2(U_y^2+U_z^2)\le1.
\]
Since \(U_x^2+U_y^2+U_z^2=1\), the limiting radial extent in either direction is \(r_{\max}=1/\sqrt{1-\min(U_x^2,U_y^2)}\). The full centrally symmetric chord has length \(L=2r_{\max}\). Also \(0\le T\le1/\sqrt2\), with \(T=0\) exactly on the two coordinate great circles and \(T=1/\sqrt2\) only at the four displayed diagonal directions. This proves the support and identifies the extremizers.

**2. Exact spherical integration.** Haar area in the coordinates \((\phi,z)\) above is exactly \(d\phi\,dz/(4\pi)\). The fourfold symmetry implies, for \(0<t<1/\sqrt2\),
\[
\Pr(T>t)=\frac4\pi\int_{\arcsin t}^{\pi/4}\sqrt{1-\frac{t^2}{\sin^2\phi}}\,d\phi.
\tag{7}
\]
Indeed, in the first octant of azimuth the smaller horizontal coordinate is \(\sqrt{1-z^2}\sin\phi\); at a fixed \(\phi\), the allowed vertical interval is \(|z|<\sqrt{1-t^2/\sin^2\phi}\). There are eight equal azimuth sectors, and the factor follows from the normalized spherical area measure.

Call the integral in (7) \(I(t)\). At the lower endpoint its integrand is zero, so differentiation under the integral, followed by \(v=\cot\phi\), yields
\[
I'(t)=-\int_1^{\sqrt{1-t^2}/t}\frac{t\,dv}{\sqrt{1-t^2-t^2v^2}}=-\arctan\frac{\sqrt{1-2t^2}}{t}.
\tag{8}
\]
The right-hand side of
\[
I(t)=\arctan\sqrt{1-2t^2}-t\arctan\frac{\sqrt{1-2t^2}}t
\tag{9}
\]
has exactly derivative (8) and vanishes at \(t=1/\sqrt2\). Thus (9) holds throughout. Substituting \(t=\sqrt{1-4/\ell^2}\) gives (1). Differentiating (7) yields the positive density of \(T\),
\[
f_T(t)=\frac4\pi\arctan\frac{\sqrt{1-2t^2}}t,
\]
and since \(dt/d\ell=4/(\ell^3t)\), formula (2) follows.

**3. Endpoint asymptotics.** At the lower endpoint, \(t=\sqrt\varepsilon+O(\varepsilon^{3/2})\) for \(\ell=2+\varepsilon\). Expanding (8) at zero gives \(f_T(t)=2-4t/\pi+O(t^3)\). Therefore \(\Pr(T\le t)=2t-2t^2/\pi+O(t^4)\), establishing (3).

For the upper endpoint use \(h=1-2t^2=8/\ell^2-1\). Formula (9) with \(s=\sqrt h\) and \(t=\sqrt{(1-h)/2}\) has cancellation through order \(\sqrt h\), leaving
\[
\Pr(T>t)=\frac4{3\pi}h^{3/2}+O(h^{5/2}).
\tag{10}
\]
As \(\ell=2\sqrt2-\varepsilon\), one has \(h=\varepsilon/\sqrt2+O(\varepsilon^2)\), and (4) follows. The absence of atoms also follows from the continuous spherical coordinate distribution and the fact that each level set of \(T\) has spherical area zero.

**4. Parabolic marked limit.** Center the azimuth at any one of the four maximizing values: \(\phi=\phi_J+q\), \(|q|<\pi/4\). The exact trigonometric identity
\[
1-2T^2=z^2+(1-z^2)|\sin2q|
\tag{11}
\]
turns \(L>\ell\) into
\[
z^2+(1-z^2)|\sin2q|<h.
\tag{12}
\]
It forces \(|z|<\sqrt h\); for small \(h\) it also forces \(|q|\le C h\) with a universal constant \(C\). Apply the invertible change of variables \(q=ha\), \(z=\sqrt h\,b\). The conditioned density is constant on the rescaled region
\[
\mathcal D_h=\bigl\{(a,b):b^2+(1-hb^2)|\sin(2ha)|/h<1,\ |ha|<\pi/4\bigr\}.
\]
The sets are uniformly bounded for small positive \(h\), and their indicator functions converge almost everywhere to that of \(\mathcal D\) in (6). Dominated convergence gives \(\operatorname{area}(\mathcal D_h)\to\operatorname{area}(\mathcal D)=4/3\) and also \(L^1\) convergence of the normalized uniform densities; this is precisely convergence in total variation. Rotation by quarter turns makes the four labels exactly equiprobable and their conditional rescaled laws identical, giving independence. The Jacobian of the transformation is \(h^{3/2}\). Multiplication by four lobes and division by \(4\pi\) recovers the coefficient \(4/(3\pi)\) in (10), independently cross-checking the upper-tail expansion.

## Verification
The included standard-library script `verify_central_bicylinder.py` independently computes direct spherical polar quadratures for eleven thresholds and numerically differentiates the candidate law at seven other thresholds. It tests the two endpoint expansions at three scales, draws 220,000 seeded Haar directions and checks both geometric radial constraints for each, compares eight empirical survival probabilities, and independently integrates four shrinking diagonal neighborhoods. Its successful run reported **440,041 deterministic assertions** and includes the exact executed output in `verification_output.txt`. The universal identities and marked total-variation limit are established by the analysis above, not inferred from finite tests or numerical sampling.

## Relationship to prior work
The bicylinder is a classical solid. A publicly dated 2008 exposition by Ngô Quốc Anh presents its volume, surface area and square cross sections; these elementary facts and the underlying solid are not claimed as new. Finch (2012) studies the *convex hull of two orthogonal disks*, which is linearly related to the bicylinder, but computes intrinsic volumes and mean width rather than the Euclidean law of center-pinned chord lengths. In a nonorthogonal affine transformation, Euclidean lengths and spherical-uniform directions are not preserved, so its reported formulas do not imply (1)–(6). Kellerer (1971) analyzes random tracks through general cylinders under invariant line models, whose offsets are random; that line measure is not the pinned-central Haar law here.

The accessible published result *Complete planar-section area profile of the Steinmetz bicylinder* studies two-dimensional central **plane-section areas** of the same body, not central one-dimensional line lengths. The published *Exact Haar central-chord law of rectangular boxes* addresses a different polyhedral body and consequently different endpoint localization. Other indexed bicylinder studies concern maximal contained tetrahedra or affine planar sections. Search comparisons considered these actual objects and quantifiers, not merely words in their titles. No equivalent or stronger covering theorem was identified in the material inspected; this is **not** a global historical-priority certification. Older works of Moore (1974) and Angell–Moore (1987) on intersecting cylinders were accessible only in extracts/abstracts for this comparison and remain residual risks.

## Limitations
All claims require two equal-radius **orthogonal** cylinders with a common axis-intersection point, and Haar-uniform center-passing directions. This theorem does not address random affine chords, displaced centers, unequal radii, nonorthogonal cylinder axes or tricylinders. The convergence in (5) is for the fixed body at a vanishing length deficit, not a parameter-uniform family of perturbed bodies. Numerical checks do not constitute independent mathematical validation. The originality assessment is provisional given incomplete access to some older specialized sources.

## References
1. Ngô Quốc Anh, *Steinmetz Solid*, dated 2008-01-19, https://anhngq.wordpress.com/2008/01/19/steinmetz-solid/ (classical body, volume and surface area).
2. S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first posted 2012-11-19, https://arxiv.org/abs/1211.4514 (perpendicular disk hull and intrinsic volumes).
3. E. W. Weisstein, *Steinmetz Solid*, MathWorld, https://mathworld.wolfram.com/SteinmetzSolid.html (classical geometric reference).
4. A. M. Kellerer, *Considerations on the Random Traversal of Convex Bodies and Solutions for General Cylinders*, Radiation Research (1971), open full text https://epub.ub.uni-muenchen.de/6318/1/6318.pdf (distinct random-line conventions).
5. M. Moore, *Symmetrical intersections of right circular cylinders*, Mathematical Gazette 58 (1974), 181–185, https://doi.org/10.2307/3615957 (relevant classical geometry; only extract inspected).
6. I. O. Angell and M. Moore, *Symmetrical intersections of cylinders*, Acta Crystallographica A43 (1987), 244–250, https://doi.org/10.1107/S0108767387099501 (relevant cylinder intersections; only abstract inspected here).
7. *Complete planar-section area profile of the Steinmetz bicylinder*, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-complete-planar-section-area-profile-of-the-steinmetz-bicylinder--1bfc7d9fbd11/RESULT.md (different two-dimensional section invariant).
8. *Exact Haar central-chord law of rectangular boxes and its singularity thresholds*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-haar-central-chord-law-of-rectangular-boxes-and-its-singul--04bd972e6d48 (different polyhedral body and endpoint regime).
