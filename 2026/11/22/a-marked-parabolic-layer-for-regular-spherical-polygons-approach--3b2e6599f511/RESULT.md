# A marked parabolic layer for regular spherical polygons approaching a hemisphere

## Finding
Fix an integer \(n\ge3\) and a regular geodesic \(n\)-gon on the unit sphere, with vertices at colatitude \(R_\varepsilon=\pi/2-\varepsilon\) from its north-polar center, where \(0<\varepsilon<\pi/2\). Let \(\alpha=\pi/n\), and let its centered incircle radius be
\[
\rho_\varepsilon=\arctan(\cot\varepsilon\cos\alpha).
\]
Choose a point \(Z_\varepsilon\) uniformly in spherical area, and consider the rare event \(E_\varepsilon\) that it lies in the polygon **outside** the incircle. Let \(\Phi_\varepsilon\in[-\alpha,\alpha]\) be the point's longitude relative to the midpoint meridian of the nearest polygon side (ties have zero area); let \(D_\varepsilon=d(Z_\varepsilon,N)\) denote center distance and
\[
 X_\varepsilon=\frac{\pi/2-D_\varepsilon}{\varepsilon},\qquad
 C_\alpha=\frac{\alpha-\sin\alpha}{\cos\alpha}>0.
\]
Then the **sharp rarity** is
\[
\boxed{\Pr(E_\varepsilon)=\frac{nC_\alpha}{\pi}\,\varepsilon+O_n(\varepsilon^2).}
\]
Moreover the conditional joint distribution converges in total variation at rate \(O_n(\varepsilon^2)\) to two-dimensional Lebesgue measure normalized on the curved band
\[
\boxed{B_\alpha=\{(\phi,x):|\phi|\le\alpha,\quad
       \cos\phi/\cos\alpha\le x\le\sec\alpha\}.}
\]
The limiting density is the constant \(1/(2C_\alpha)\) on the band, and zero elsewhere. In particular its two marginal densities are, on their stated supports,
\[
 \boxed{f_\Phi(\phi)=\frac{1-\cos\phi}{2(\alpha-\sin\alpha)},\qquad -\alpha<\phi<\alpha,}
\]
\[
 \boxed{f_X(x)=\frac{\alpha-\arccos(x\cos\alpha)}{C_\alpha},\qquad 1<x<\sec\alpha.}
\]
The side-sector index itself is independent and uniform on the \(n\) sides. The limit is therefore vertex-biased within each side sector: its density vanishes at the side midpoint rather than being longitude-uniform.

There is a **second, many-sided limit**. First take the displayed fixed-\(n\), near-hemisphere limit; then let \(n\to\infty\). Normalize its coordinates by
\[
 U=\Phi/\alpha,\qquad Y=(X-1)/(\sec\alpha-1).
\]
These new marked laws converge in total variation, with error \(O(n^{-2})\), to the constant-density law
\[
\boxed{\frac32\,\mathbf1\{ |u|\le1,\ 1-u^2\le y\le1\}\,du\,dy.}
\]
Thus
\[
 f_U(u)=\frac32u^2\quad(-1<u<1),\qquad
 f_Y(y)=3(1-\sqrt{1-y})\quad(0<y<1),
\]
and its radial cumulative law is \(F_Y(y)=3y-2+2(1-y)^{3/2}\), with \(\mathbb E Y=7/10\). The consecutive limits are essential: no joint regime with \(n\to\infty\) and \(\varepsilon\to0\) simultaneously is asserted.

## Assumptions and scope
The ambient space is the unit round two-sphere with great-circle geodesic distance and normalized uniform spherical area on the polygon (not uniform longitude/latitude or chord measure). Its vertices are
\[
 v_j=(\sin R_\varepsilon\cos(2\pi j/n),\ \sin R_\varepsilon\sin(2\pi j/n),\ \cos R_\varepsilon),\quad 0\le j<n,
\]
and all polygon sides are shorter great-circle arcs. For \(R_\varepsilon<\pi/2\), this polygon lies in the open northern hemisphere, is geodesically convex and has a unique natural polar center. The incircle is the centered geodesic disk of radius \(\rho_\varepsilon\). A sector is the longitude interval between the two vertex meridians bounding a polygon side, measured relative to their midpoint longitude. In particular, sector endpoints are vertex meridians, not side midpoint meridians. The conditional law is well-defined for every positive \(\varepsilon\). Total variation is the supremum over Borel measurable events of the difference of their probabilities; for densities it equals one-half of the \(L^1\) distance.

For clarity, the conditional distribution is an ordinary distribution in the stated coordinates \((\Phi_\varepsilon,X_\varepsilon)\), not a vague point-process limit. Here and below the constants in \(O_n\) may depend on the fixed integer \(n\). The many-side rate concerns only the family of the **first limiting laws**, not a uniform estimate in \(\varepsilon\) and \(n\).

## Proof
**1. Exact wedge geometry.** Write the north-polar spherical coordinates as \((r,\phi)\), where \(r\in[0,\pi/2)\). Under the gnomonic projection \((r,\phi)\mapsto\tan r(\cos\phi,\sin\phi)\), great-circle edges become Euclidean segments. The two adjacent vertices bounding a folded sector have planar coordinates \((\tan R_\varepsilon\cos\alpha,\pm\tan R_\varepsilon\sin\alpha)\). Therefore their edge line is \(x=\tan R_\varepsilon\cos\alpha\), giving the exact boundary
\[
 \tan r_{\max}(\phi)=\frac{\tan R_\varepsilon\cos\alpha}{\cos\phi},
 \qquad |\phi|\le\alpha.
\]
The minimum of this radius occurs at \(\phi=0\); it equals \(\rho_\varepsilon\), proving the incircle formula. In each folded sector, the rare event is exactly the radial interval \(\rho_\varepsilon<r<r_{\max}(\phi)\).

**2. Uniform rescaled boundary.** Set \(h_\varepsilon(\phi)=(\pi/2-r_{\max}(\phi))/\varepsilon\) and \(H_\varepsilon=(\pi/2-\rho_\varepsilon)/\varepsilon\). Using \(\tan R_\varepsilon=\cot\varepsilon\),
\[
 h_\varepsilon(\phi)=\frac1\varepsilon\arctan\left(\tan\varepsilon\frac{\cos\phi}{\cos\alpha}\right),\qquad
 H_\varepsilon=\frac1\varepsilon\arctan(\tan\varepsilon\sec\alpha).
\]
For fixed \(n\), the Taylor expansions of \(\tan\) and \(\arctan\) are uniform for \(|\phi|\le\alpha\), so
\[
 h_\varepsilon(\phi)=\frac{\cos\phi}{\cos\alpha}+O_n(\varepsilon^2),\quad
 H_\varepsilon=\sec\alpha+O_n(\varepsilon^2).
\]
Because larger \(r\) means smaller \(x=(\pi/2-r)/\varepsilon\), the rescaled rare-event sector is exactly
\(B_{\alpha,\varepsilon}=\{(\phi,x):|\phi|\le\alpha,\ h_\varepsilon(\phi)\le x\le H_\varepsilon\}\). Its symmetric difference from \(B_\alpha\) has Euclidean area \(O_n(\varepsilon^2)\).

**3. Area and sharp probability.** The spherical area element is \(\sin r\,dr\,d\phi\). Substitution \(r=\pi/2-\varepsilon x\) gives \(\varepsilon\cos(\varepsilon x)\,dx\,d\phi\). The rescaled layer's limiting area in one sector is
\[
 |B_\alpha|=\int_{-\alpha}^\alpha\left(\sec\alpha-\frac{\cos\phi}{\cos\alpha}\right)d\phi
 =2\frac{\alpha-\sin\alpha}{\cos\alpha}=2C_\alpha.
\]
Taylor expansion and the uniform boundary control show that the unnormalized physical layer area is
\[
 L_{n,\varepsilon}=2nC_\alpha\varepsilon+O_n(\varepsilon^3).
\]
The full polygon's area tends to the northern hemisphere's area \(2\pi\) and differs from it by \(O_n(\varepsilon)\), since its boundary colatitudes all approach \(\pi/2\) at rate \(O_n(\varepsilon)\). Dividing \(L_{n,\varepsilon}\) by this area proves the rare-event probability, including the stated \(O_n(\varepsilon^2)\) rather than a stronger unjustified remainder.

**4. Total variation and the two marginals.** Conditioned on the layer, the folded pair has the exact density
\[
 p_\varepsilon(\phi,x)=\frac{n\varepsilon}{L_{n,\varepsilon}}\cos(\varepsilon x)
       \mathbf1_{B_{\alpha,\varepsilon}}(\phi,x).
\]
The prefactor is \(1/(2C_\alpha)+O_n(\varepsilon^2)\), and \(\cos(\varepsilon x)=1+O_n(\varepsilon^2)\) uniformly on these bounded bands. Combining these bounds with their \(O_n(\varepsilon^2)\) symmetric difference proves the conditional \(L^1\), hence total variation, error bound. Rotational symmetry makes the sector index independent and uniformly distributed.

For fixed \(\phi\), the limiting band has vertical length \((1-\cos\phi)/\cos\alpha\), giving the angular density after normalization. For fixed \(x\in[1,\sec\alpha]\), admissible longitudes satisfy \(|\phi|\ge\arccos(x\cos\alpha)\); their total length is \(2[\alpha-\arccos(x\cos\alpha)]\), giving the radial density. Both integrate to one by Fubini's theorem.

**5. Parabolic many-side limit.** Apply the affine coordinate transform \(u=\phi/\alpha\), \(y=(x-1)/(\sec\alpha-1)\) to the **fixed-\(n\) limiting band**. Its lower boundary is
\[
 y\ge q_\alpha(u):=\frac{\cos(\alpha u)-\cos\alpha}{1-\cos\alpha},\qquad |u|\le1,
\]
and its constant density is \(k_\alpha=\alpha(\sec\alpha-1)/(2C_\alpha)\). Uniform Taylor expansions in \(u\in[-1,1]\) yield
\[
 q_\alpha(u)=1-u^2+O(\alpha^2),\qquad k_\alpha=\frac32+O(\alpha^2).
\]
The symmetric-difference area of the supports and the \(L^1\) density error are thus both \(O(\alpha^2)=O(n^{-2})\). The limiting support has area \(\int_{-1}^1u^2du=2/3\), so density \(3/2\) is normalized. Its vertical lengths give \(f_U(u)=3u^2/2\); its horizontal lengths give \(f_Y(y)=3[1-\sqrt{1-y}]\). Integration yields the stated CDF and \(\mathbb EY=7/10\). This proves each assertion without interchanging the two limits. \(\square\)

## Verification
The standalone `verify_spherical_layer.py` provides three partly independent sanity-check paths: direct polar quadrature of the finite rare-layer area against an exact spherical polygon-area identity; finite-\(\varepsilon\) radial CDF values against the integrated first-limit density; and direct sampling from the exact finite-\(\varepsilon\) area measure on the layer (random longitude accepted with area weight, followed by a uniform area-coordinate), compared with analytic angular and radial histograms. It additionally tests the second-limit band and normalized density at three large side counts. Executing `python3 verify_spherical_layer.py` with NumPy and SciPy yielded:

`PASS: 40 area/coefficient checks; 80 finite conditional CDF tests; 376 marked-law Monte Carlo and second-limit checks`

The proof is the uniform-support and density expansion in Steps 1–5; these finite numerical checks are not used to infer convergence for all parameters or to claim independent proof.

## Relationship to prior work
Khalid and Durrani (2012) explicitly derive center-distance CDFs in **Euclidean** regular polygons from overlap of disks and polygons. Kouřimská, Skuppin and Springborn (2015), Section 3, establish foundational geometry for cyclic **spherical** polygons. Wang (2009), dissertation Chapter 8, provides more general algorithms for areas of intersections of spherical caps and spherical polygonal regions. Those methods subsume ordinary finite-radius cap-overlap and area calculations; **neither their geometry nor the finite-radius radial CDF alone is asserted as new here**. The distinct object is the *conditional joint longitude–latitude mark* of a rare near-hemispherical layer, its sharp probability, total-variation limit, and the successive universal parabolic law.

Existing statements on farthest points from a fixed **vertex** of a regular spherical polygon address a deterministic extremal-distance question, not a center-conditioned area-random point. Known inverse radial laws for planar tangential polygons use Euclidean measure and geometry. Published spherical-cap coverage-multiplicity laws for equatorial regular site arrays measure counts of covered sites, not a point restricted to a **geodesic polygon outside its incircle**. General geometric area algorithms allow one to calculate many component measures but do not supply the displayed sharp marked conditional limits or the second parabolic scaling without further singular asymptotic analysis. A stronger equivalent result in specialized spherical stochastic geometry is a residual historical risk.

## Limitations
Only geodesically convex regular spherical polygons in the northern hemisphere and an area-uniform point are treated. The first theorem holds for each fixed number of sides, and the second is a successive limit of the first limiting laws; uniform estimates in a joint \(n\)-and-\(\varepsilon\) regime are unproved. It is a conditional rare-event theorem, not a general method for reconstructing an unknown spherical polygon from noisy samples. The finite area formula is classical in scope; no priority for the general spherical-cap intersection method is claimed. Historical priority is provisional, and independent mathematical validation has not been performed.

## References
1. Z. Khalid and S. Durrani, *Distance Distributions in Regular Polygons*, arXiv:1207.5857v1, first public 2012-07-25, https://arxiv.org/abs/1207.5857.
2. H. Kouřimská, L. Skuppin and B. Springborn, *A variational principle for cyclic polygons with prescribed edge lengths*, arXiv:1506.08069v1, first public 2015-06-26, https://arxiv.org/abs/1506.08069.
3. L. Wang, *RFID in Supply Chains*, University of Pittsburgh doctoral dissertation, 2009, Chapter 8, spherical-cap intersection area methods, https://d-scholarship.pitt.edu/6276/1/WangLin_Feb6_2009.pdf. Defense year is not used to assert an exact first-public online date.
4. *A sharp farthest-point transition on regular spherical polygons*, published 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-farthest-point-transition-on-regular-spherical-polygons--6f9e3488fec9.
5. *Radial-distance laws classify tangential polygons up to cyclic ordering*, published 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-radial-distance-laws-classify-tangential-polygons-up-to-cyclic-o--682fa94d6003.
6. *Exact all-depth spherical-cap laws for regular equatorial point sets*, published 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-all-depth-spherical-cap-laws-for-regular-equatorial-point--1f86ecf5421c.
