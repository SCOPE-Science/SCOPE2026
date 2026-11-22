# Sharp five-halves shadow contact and a two-fifths rare-orientation law for spherical caps

## Finding
For \(-1<h<1\), let \(K_h=\{x\in\mathbb R^3:\|x\|_2\le1,\ x_3\ge h\}\) be the **solid** unit spherical cap. Let \(U\) be uniform on the unit sphere, and \(B_h\) be the ordinary Euclidean area of the orthogonal projection of \(K_h\) onto \(U^\perp\). Put \(r=\sqrt{1-h^2}\), \(c=|U_3|\), \(s=\sqrt{1-c^2}\), and, for \(s>|h|\),
\[
\beta=\arccos\!\left(-\frac{hc}{rs}\right).
\]
The complete directional brightness profile is
\[
B_h(c)=\begin{cases}
\pi r^2c,& h>0,\ s\le h,\\
\pi,& h<0,\ s\le-h,\\
\arccos(h/s)+r^2c\beta-hrs\sin\beta,&s>|h|.
\end{cases}
\]
At \(h=0\), this is the continuous, exact formula \(B_0(c)=\pi(1+c)/2\). Boundary values use continuous extension. Since \(c\) is uniform on \([0,1]\), the profile gives a full, uniquely invertible distribution on its nonconstant range.

Let \(b_-(h)=\arccos(h)-hr\). The minimum brightness is \(b_-(h)\), at equatorial viewing. The maximum is \(\pi r^2\) for \(h\ge0\) (interpreting \(r=1\) when \(h=0\)), and \(\pi\) for \(h<0\). The brightness is strictly increasing in \(c\), except for a plateau \(c\in[r,1]\) when \(h<0\). Thus
\[
\Pr(B_h=\pi)=1-r\quad(h<0),
\]
while there is no atom for \(h\ge0\).

The lower-tail probability, for every fixed \(-1<h<1\), satisfies
\[
\Pr(B_h\le b_-(h)+\varepsilon)
=\frac{2\varepsilon}{\pi r^2}+O_h(\varepsilon^2).
\]
For \(h>0\) there is an **exact** positive-length terminal interval,
\[
\Pr(B_h\ge\pi r^2-\varepsilon)=\frac{\varepsilon}{\pi r^2}
\quad\left(0\le\varepsilon\le\pi r^2(1-r)\right).
\]
For \(h=0\) the brightness is uniform on \([\pi/2,\pi]\), hence the upper-tail slope is instead exactly \(2/\pi\). For \(h<0\), writing \(a=-h\), the continuous probability immediately below the upper atom has the sharp noninteger law
\[
\Pr(B_h\ge\pi-\varepsilon)
=1-r+\left(\frac{15a^3}{8\sqrt2\sqrt r}\right)^{2/5}\varepsilon^{2/5}
+o_h(\varepsilon^{2/5}).
\]

The geometric contact transition takes place at \(s=|h|\). For fixed \(h\ne0\) and \(\delta=s-|h|\downarrow0\),
\[
B_h(s)-B_h^{\mathrm{base}}(s)=
\operatorname{sgn}(h)\frac{8\sqrt2}{15r^2\sqrt{|h|}}\delta^{5/2}
+O_h(\delta^{7/2}),
\]
where \(B_h^{\mathrm{base}}(s)=\pi r^2\sqrt{1-s^2}\) if \(h>0\), and \(B_h^{\mathrm{base}}(s)=\pi\) if \(h<0\). Therefore the profile is \(C^2\) but not \(C^3\) at the contact threshold. The exponent \(2/5\) in the negative-height probability law is the inverse of this five-halves contact exponent.

## Assumptions and scope
The ball has Euclidean radius one and is clipped by the oriented plane \(x_3=h\), with \(-1<h<1\). Uniform directions refer to normalized spherical surface area on \(S^2\); projection is ordinary orthographic projection of the **solid convex cap**, not spherical surface area, solid angle, or a randomly selected point. Reflection of the viewing direction does not change the brightness. The constants in \(O_h\) may depend on the fixed clipping height. The transition asymptotic is for fixed nonzero \(h\), not uniform in \(h\to0\).

## Proof
**1. Brightness integral.** For any convex body with outward surface normal \(n\), its planar projected area in direction \(u\) is \(\int_{\partial K}(n\cdot u)_+\,dS\). By replacing \(u\) with \(-u\) if necessary and rotating horizontally, write \(u=(s,0,c)\) with \(c\ge0\). The flat base of \(K_h\) has outward normal \(-e_3\), so contributes zero. The spherical patch has outward normal equal to its position \(n\). Hence
\[
B_h=\int_{n\in S^2,\ n_3\ge h,\ n\cdot u\ge0}(n\cdot u)\,d\sigma(n).
\]
For \(h>0\), if \(s\le h\), the spherical patch lies in the forward hemisphere, and direct integration of \(c n_3\) gives \(\pi(1-h^2)c\). For \(h<0\), if \(s\le-h\), the forward hemisphere is contained in the cap, yielding the full-disk brightness \(\pi\).

**2. Mixed silhouette.** If \(s>|h|\), the boundary of the spherical region in the preceding integral consists of a great-circle arc \(n\cdot u=0\) and an arc on the latitude circle \(n_3=h\). The great-circle arc subtends angle \(2\arccos(h/s)\). Parameterize the latitude arc by \(n=(r\cos\phi,r\sin\phi,h)\) with \(-\beta\le\phi\le\beta\), where \(\cos\beta=-hc/(rs)\). Applying the spherical vector-area formula \(\int_R n\,d\sigma=\frac12\int_{\partial R}n\times dn\), then dotting with \(u\), gives the stated mixed formula. For the latitude arc, \(u\cdot(n\times dn)=(r^2c-hrs\cos\phi)\,d\phi\). The great-circle arc contributes \(2\arccos(h/s)\). The formula is continuous at the two tangencies and at \(c=0\).

**3. Monotonicity and the exact law.** Set \(s=\sin\alpha\), \(c=\cos\alpha\) for \(0\le\alpha\le\pi/2\). Differentiating the mixed formula, and using cancellation of the endpoint terms, yields
\[
\frac{dB_h}{d\alpha}=-r^2s\beta-hrc\sin\beta.
\]
For \(h\ge0\) this is negative away from the endpoint. For \(h=-a<0\), \(\cos\beta=ac/(rs)\) and \(\beta>\sin\beta\cos\beta\) for \(0<\beta<\pi/2\), proving strict negativity after the plateau. The other pieces are immediate. Since \(|U_3|\) is uniform on \([0,1]\), the exact distribution is obtained by inverting the monotone profile: on the open brightness range, \(\Pr(B_h\le b)=c_b\), where \(B_h(c_b)=b\), with the jump \(1-r\) at \(b=\pi\) for \(h<0\).

**4. Five-halves contact normal form.** Write spherical latitude \(t=n_3\), so \(d\sigma=dt\,d\phi\) and the integrand is the positive part of \(F(t,\phi)=ct+s\sqrt{1-t^2}\cos\phi\). For \(h>0\), just above \(s=h\), the correction to the all-visible latitude integral comes from the negative part in \(h\le t<s\), near \(\phi=\pi\). With \(v=s-t\) and \(\psi=\phi-\pi\),
\[
-F=\frac{v}{c}-\frac{sc}{2}\psi^2+O(v^2+v\psi^2+\psi^4).
\]
The positive parabola is supported in a \(\psi\)-interval of length \(O(\sqrt v)\), and its integral is \(4\sqrt2\,v^{3/2}/(3c^2\sqrt s)\). Integrating \(v\) from zero to \(\delta\) gives \(8\sqrt2\,\delta^{5/2}/(15c^2\sqrt s)+O_h(\delta^{7/2})\). At the threshold \(s=h\), \(c=r\), giving the positive coefficient. For \(h<0\), use the complementary excluded visible patch \(-s<t<h\) near \(\phi=0\); the same local parabola gives the negative of that coefficient, evaluated at \(s=-h\). Since neither coefficient vanishes, the profile has precisely \(C^2\) contact regularity.

**5. Probability tails.** At \(c=0\), the mixed expression has \(B_h(c)=b_-(h)+\frac{\pi r^2}{2}c+O_h(c^2)\), establishing the lower tail. When \(h>0\), the all-visible exact branch gives the stated upper tail. For \(h=0\) the mixed formula reduces exactly to \(\pi(1+c)/2\). Finally let \(h=-a<0\); near \(c=r\) from below, \(s-a=(r/a)(r-c)+O((r-c)^2)\). The five-halves formula therefore becomes
\[
\pi-B_h(c)=\frac{8\sqrt2\sqrt r}{15a^3}(r-c)^{5/2}+o((r-c)^{5/2}).
\]
Uniformity of \(c\) and inversion yield the asserted \(2/5\)-power excess above the atom.

## Verification
The standalone `check.py` compares the closed profile with independent one-dimensional quadrature of the brightness integral, checks its monotonic pieces, verifies the extrema, and numerically examines the contact and atomic-tail coefficients. Running it requires only Python's standard library; all assertions passed when this result was packaged. These finite numerical checks do not replace the analytic proof, certify the infinite theorem, or establish historical priority.

## Relationship to prior work
S. Li's 2010 published treatment derives ordinary hyperspherical cap areas and volumes, not the distribution of orthographic shadow brightness under isotropic viewing. The 2018 paper by Ureña and Georgiev studies **projections of spherical caps** in computer graphics and explicitly analyzes ellipse/lune silhouettes and projected area computations. Those geometric constructions are credited; the present claim is not that spherical-cap projection shapes or their basic area integrals were previously unknown. The distinction is the full **random-direction area law**, its atom transition at the hemisphere, and the sharp five-halves contact / inverse two-fifths probability scaling. Direct searches for equivalent brightness and orientation-distribution theorems did not identify an explicit prior statement. This negative search is not proof of global novelty.

## Limitations
The claim is confined to solid Euclidean ball caps in three dimensions and isotropic viewing directions. It does not address perspective projection, arbitrary cap deformations, or a parameter-uniform crossover as \(h\to0\). The mathematical novelty claim remains provisional, particularly because existing illumination literature develops comparable projected-cap geometry. No independent scientific audit has been performed.

## References
1. S. Li, “Concise Formulas for the Area and Volume of a Hyperspherical Cap,” *Asian Journal of Mathematics & Statistics* 4 (2011), 66–70; first published November 8, 2010, DOI: 10.3923/ajms.2011.66.70. https://scialert.net/fulltext/?doi=ajms.2011.66.70
2. C. Ureña and I. Georgiev, “Stratified Sampling of Projected Spherical Caps,” *Computer Graphics Forum* 37 (2018), 13–20, DOI: 10.1111/cgf.13471. https://iliyan.com/publications/ProjectedSphericalCaps/ProjectedSphericalCaps_EGSR2018.pdf
3. Classical Cauchy projection/brightness formula for convex surfaces, used in the proof; see any standard integral-geometry treatment.
