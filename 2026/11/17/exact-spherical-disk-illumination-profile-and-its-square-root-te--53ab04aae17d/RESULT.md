# Exact spherical-disk illumination profile and its square-root terminal cusp

## Finding
Fix a point \(O\) on the unit two-sphere \(\mathbb S^2\) and \(0<r<\pi/2\). Let \(B_r(O)\) be the closed spherical geodesic disk. If \(P\) is a point at distance \(t\) from \(O\), \(r<t<\pi-r\), set
\[
H_r(P)=\operatorname{gconv}(B_r(O)\cup\{P\}),\qquad
\Delta_r(t)=\operatorname{area}(H_r(P)\setminus B_r(O)).
\]
Here \(\operatorname{gconv}\) is the geodesically convex hull inside a common open hemisphere; the interval restriction makes this unambiguous. Then the exact added area is
\[
\boxed{\Delta_r(t)=2\cos r\,\arccos\!\left(\frac{\tan r}{\tan t}\right)
 +2\arcsin\!\left(\frac{\sin r}{\sin t}\right)-\pi.}
\]
At \(t=\pi/2\), the first inverse-cosine argument is understood continuously as zero; equivalently use \(\tan r\cos t/\sin t\) throughout. The principal inverse trigonometric branches have \(\arccos\in(0,\pi)\) and \(\arcsin\in(0,\pi/2)\).

The function \(\Delta_r\) is strictly increasing from zero to the finite limit \(\Delta_*(r)=2\pi\cos r\); in particular every \(0<\delta<2\pi\cos r\) gives exactly one distance \(t_r(\delta)\in(r,\pi-r)\) with added area \(\delta\). Its two endpoint asymptotics are
\[
\begin{aligned}
\Delta_r(r+h)&=\frac23\sqrt{2\tan r}\,h^{3/2}+O_r(h^{5/2}),\\
2\pi\cos r-\Delta_r(\pi-r-h)&=4\sqrt{2\cot r}\,h^{1/2}+O_r(h^{3/2}).
\end{aligned}
\]
Consequently the inverse radius has two distinct sharp laws:
\[
\begin{aligned}
t_r(\delta)-r&\sim \left(\frac{3\delta}{2\sqrt{2\tan r}}\right)^{2/3}\quad (\delta\downarrow0),\\
\pi-r-t_r(\delta)&\sim\frac{\tan r}{32}\,(2\pi\cos r-\delta)^2
\quad (\delta\uparrow2\pi\cos r).
\end{aligned}
\]
The claim is for strictly subcritical points and illumination levels; no convention-dependent statement about geodesics with antipodal endpoints is required.

## Assumptions and scope
The curvature is exactly \(+1\); all distances are intrinsic angular distances in radians and all areas are intrinsic spherical areas. For fixed \(0<r<\pi/2\) and \(r<t<\pi-r\), there is an open hemisphere containing the disk and the point: take its center on the geodesic \(OP\) at distance \((t-r)/2\) from \(O\), so every included point has distance at most \((t+r)/2<\pi/2\) from that center. Gnomonic projection therefore makes the hull well-defined and maps its boundary geodesics to Euclidean line segments. The illumination body at level \(0\le\delta<2\pi\cos r\) is the centered disk with radius \(t_r(\delta)\), with \(t_r(0)=r\).

## Proof
**Tangency and exact area.** There are two geodesic tangents from \(P\) to the disk, meeting the small circle at \(T_+\) and \(T_-\). The spherical right triangle \(O T_+ P\) has angle \(\pi/2\) at \(T_+\). Let \(u=\angle T_+OP\in(0,\pi)\) and \(v=\angle OPT_+\in(0,\pi/2)\). The spherical right-triangle cosine law and sine law give
\[
\cos u=\frac{\tan r\cos t}{\sin t},\qquad
\sin v=\frac{\sin r}{\sin t}.
\]
The right spherical triangle has area \(u+v-\pi/2\) by Girard's theorem. The hull boundary consists of the two tangent geodesics and the far circular arc. In the resulting added-area decomposition, twice this right-triangle area is reduced by the spherical disk sector of angular width \(2u\), whose area is \(2u(1-\cos r)\). Thus
\[
\Delta_r(t)=2(u+v-\pi/2)-2u(1-\cos r)
=2u\cos r+2v-\pi.
\]
Substitution yields the displayed exact profile. The same decomposition is valid even when \(u>\pi/2\): it is intrinsic to the common hemisphere, and the sector is the angular portion facing \(P\).

**Monotonicity and endpoint limits.** Differentiating the inverse-trigonometric expressions yields, for \(r<t<\pi-r\),
\[
\boxed{\Delta_r'(t)=
\frac{2\sin r\,(\cos r-\cos t)}{\sin t\sqrt{\sin^2t-\sin^2r}}>0.}
\]
Both denominator factors are positive on the stated open interval; \(\cos r-\cos t>0\). As \(t\downarrow r\), \(u\to0\), \(v\to\pi/2\), so \(\Delta_r(t)\to0\). As \(t\uparrow\pi-r\), \(u\to\pi\), \(v\to\pi/2\), so \(\Delta_r(t)\to2\pi\cos r\).

**Sharp endpoint exponents.** Writing \(t=r+h\), use \(\sin^2(r+h)-\sin^2r=2\sin r\cos r\,h+O_r(h^2)\) and \(\cos r-\cos(r+h)=\sin r\,h+O_r(h^2)\). In the derivative formula this gives
\[
\Delta_r'(r+h)=\sqrt{2\tan r}\,h^{1/2}+O_r(h^{3/2}).
\]
Integrating from zero to \(h\) proves the first expansion. At the other endpoint, write \(t=\pi-r-h\); now \(\sin^2t-\sin^2r=2\sin r\cos r\,h+O_r(h^2)\) and \(\cos r-\cos t=2\cos r+O_r(h)\), giving
\[
\Delta_r'(\pi-r-h)=2\sqrt{2\cot r}\,h^{-1/2}+O_r(h^{1/2}).
\]
Integration backward from the limiting endpoint proves the second expansion. Since the profile is continuous and strictly monotone, inversion gives the two radius laws, including the exact coefficient \(\tan r/32\) at the terminal level.

## Verification
The standalone `checker.py` uses only the Python standard library. It checks the analytic expression against two independent calculations: Simpson quadrature of the derivative with the endpoint square-root singularity removed, and direct geodesic spherical polygon areas for sampled circular boundaries. The latter uses a common-hemisphere gnomonic projection, computes an ordinary planar convex hull, then sums intrinsic spherical-triangle solid angles. It includes configurations with \(t>\pi/2\), checks several disk radii and both endpoint coefficients, and gives 27 passing comparisons. Sampling a circle by finitely many vertices is an approximation, not an exact certificate and not part of the infinite proof.

## Relationship to prior work
Assouline, Besau and Werner (2026, arXiv:2605.25122, Section 5.2, Example 2) already prove by symmetry that the illumination body of a spherical geodesic ball is concentric, identify the finite critical area and the later all-sphere transition, and characterize the radius *implicitly* through a geodesic-hull volume. These results are credited, not claimed as new. What is evaluated here is the explicit two-angle formula at every subcritical level and the sharp first-order behavior of the inverse radius at **both** ends, particularly the quadratic terminal law with coefficient \(\tan r/32\). Assouline, Schütt and Werner (arXiv:2606.21112) give a general asymptotic Riemannian illumination theorem; its accessible abstract does not provide this full finite-level computation. Existing Euclidean ball-convex illumination profiles and hyperbolic second-order small-level expansions use different geometric settings and do not imply the spherical terminal cusp as stated.

## Limitations
The result assumes a unit sphere, two dimensions, a disk of radius strictly less than a hemisphere, and \(t<\pi-r\). It does not assert a formula at or beyond the antipodal-contact distance; this avoids ambiguity in conventions for all minimizing geodesics at antipodal endpoints. It does not classify general nonspherical convex bodies or higher dimensions. The full text of arXiv:2606.21112 was not accessible in the consulted sources; historical priority is therefore provisional, and an unindexed equivalent calculation is possible. The numerical checks cannot replace the analytic derivation or independently certify novelty.

## References
1. R. Assouline, F. Besau, E. M. Werner, *Illumination Bodies in Projective Geometries*, arXiv:2605.25122v1 (first public 2026-05-24), https://arxiv.org/abs/2605.25122 . Full text consulted through https://www.academ.us/article/2605.25122/ , especially Section 5.2.
2. R. Assouline, C. Schütt, E. M. Werner, *Illumination bodies on Riemannian manifolds*, arXiv:2606.21112 (first public 2026-06-19), https://arxiv.org/abs/2606.21112 . Abstract consulted; full text not available in consulted retrieval.
3. Standard spherical right-triangle cosine and sine laws, spherical excess (Girard), and gnomonic projection; their uses are proved/explained above.
