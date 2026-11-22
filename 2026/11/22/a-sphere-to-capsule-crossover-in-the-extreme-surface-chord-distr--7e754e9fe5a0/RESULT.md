# A sphere-to-capsule crossover in the extreme surface-chord distribution

## Finding
Let \(r>0\) and \(a\ge0\), and define the compact Euclidean capsule
\[
K_{a,r}=([-a,a]e_3)+rB_2^3\subset\mathbb R^3.
\]
Its boundary has surface area \(S_{a,r}=4\pi r(r+a)\) and Euclidean diameter \(d_{a,r}=2(r+a)\). Independently sample \(X,Y\) according to **normalized two-dimensional Hausdorff (surface-area) measure** on \(\partial K_{a,r}\), and let \(D=\|X-Y\|_2\).

**Fixed positive segment.** For each fixed \(a,r>0\), as \(\varepsilon\downarrow0\),
\[
\boxed{\Pr\{D>d_{a,r}-\varepsilon\}=\frac{\varepsilon^2}{4a(a+r)}+O_{a,r}(\varepsilon^3).}\tag{1}
\]
For the ball endpoint \(a=0\), by contrast the complete exact formula for \(0\le\varepsilon\le2r\) is
\[
\Pr\{D>2r-\varepsilon\}=\frac{\varepsilon}{r}-\frac{\varepsilon^2}{4r^2}.\tag{2}
\]
Thus every positive axial segment, however short, changes the diameter-tail exponent from one to two.

**Sharp singular crossover.** Fix \(r>0\) and \(\lambda\ge0\), and set \(a=\lambda\varepsilon\) *as the distance deficit tends to zero*. Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac r\varepsilon\Pr\{D>2(r+a)-\varepsilon\}=\Psi(\lambda)}\tag{3}
\]
with the universal, continuous, strictly positive profile
\[
\boxed{\Psi(\lambda)=\int_0^1[1-2\lambda(1-z)]_+\,dz
=\begin{cases}1-\lambda,&0\le\lambda\le\tfrac12,\\[2pt]
1/(4\lambda),&\lambda\ge\tfrac12.
\end{cases}}\tag{4}
\]
Here \([x]_+=\max\{x,0\}\). The profile is \(C^1\) but not \(C^2\) at the exact transition \(\lambda=1/2\); the right-minus-left second derivative is \(4\). For \(\lambda\to\infty\), \(\Psi(\lambda)\sim(4\lambda)^{-1}\), matching the small-segment limit of (1) in the *overlap of their coefficient asymptotics*; no unproved simultaneous large-\(\lambda\) error estimate is asserted.

**Shape recovery.** If \(a>0\) and the diameter \(d=d_{a,r}\) and fixed-shape tail coefficient \(C=\lim_{\varepsilon\downarrow0}\varepsilon^{-2}\Pr\{D>d-\varepsilon\}\) are known, then
\[
a=\frac{1}{2Cd},\qquad r=\frac d2-\frac{1}{2Cd}.\tag{5}
\]
The exact feasible dimensionless range is \(Cd^2>1\); values tend to the excluded thin-segment endpoint \(1\) and diverge as \(a\downarrow0\) at fixed diameter. The sphere is separately distinguished by its first-order rather than quadratic tail.

## Assumptions and scope
The sampling distribution is normalized **surface area on the complete boundary**: both hemispherical caps and the cylindrical band participate. It is not volume-uniform sampling and not the Euclidean-motion-invariant random-line/chord convention. In (1), \(a,r\) remain fixed with \(a>0\); in (3), \(r>0\) and \(\lambda\ge0\) remain fixed while \(a=\lambda\varepsilon\). The cylinder-to-cap seams have zero surface area. The condition \(D>d-\varepsilon\) is strict, but equality endpoints have probability zero.

## Proof
**1. Diameter and surface normalization.** Every capsule point can be represented as \(se_3+ru\), with \(s\in[-a,a]\) and \(\|u\|\le1\). Hence for two points
\(\|X-Y\|\le |s_X-s_Y|+r\|u_X-u_Y\|\le2(a+r)\). If \(a>0\), equality forces the unique unordered diametral pair \(\{(a+r)e_3,-(a+r)e_3\}\), which lies strictly inside the two spherical caps. The hemisphere pair contributes area \(4\pi r^2\) and the cylindrical band area \(4\pi ar\), giving the stated \(S_{a,r}\).

**2. Quadratic deficit at a unique pair.** Near the upper and lower poles parameterize the cap surfaces by transverse vectors \(x,y\in\mathbb R^2\), both small:
\[
P(x)=(rx,a+r\sqrt{1-|x|^2}),\qquad
Q(y)=(ry,-a-r\sqrt{1-|y|^2}).
\]
Put \(s=x+y\), \(h=x-y\), and \(\kappa=a/(a+r)>0\). Taylor expansion of the *exact Cartesian distance* gives
\[
2(a+r)-\|P(x)-Q(y)\|
=\frac r4\bigl(|s|^2+\kappa|h|^2\bigr)
+O_{a,r}\bigl((|x|+|y|)^4\bigr).\tag{6}
\]
There is no cubic term, because simultaneous sign reversal \((x,y)\mapsto(-x,-y)\) preserves the distance. The positive-definite form in (6), together with compactness and uniqueness of the diameter pair, shows that every sufficiently small deficit comes from these two charts, and \(|x|+|y|=O_{a,r}(\sqrt\varepsilon)\).

Each cap surface element is \(r^2(1-|x|^2)^{-1/2}dx\), so the product surface measure is \(r^4(1+O(|x|^2+|y|^2))dx\,dy\). The linear map \((s,h)\mapsto(x,y)\) has four-dimensional absolute Jacobian \(1/4\). The set defined by the leading term in (6) being less than \(\varepsilon\) has \((s,h)\)-volume
\[
\frac{\pi^2}{2}\left(\frac{4\varepsilon}{r}\right)^2\frac1\kappa
=\frac{8\pi^2\varepsilon^2}{r^2\kappa}.\tag{7}
\]
Multiply (7) by \(r^4/4\), then by two for the two ordered choices of caps, and divide by \(S_{a,r}^2=16\pi^2r^2(a+r)^2\). This yields precisely \(\varepsilon^2/[4a(a+r)]\). The analytic, even-degree fourth-order distance error and smooth even surface-density correction change the four-dimensional sublevel volume by \(O_{a,r}(\varepsilon^3)\), proving (1). This remainder claim uses smoothness only in neighborhoods strictly away from both cap seams; global surface smoothness at the seams is unnecessary.

**3. Exact spherical endpoint.** For independent uniform points on the radius-\(r\) sphere, their directional dot product is uniform on \([-1,1]\). Hence \(\Pr(D\le d)=d^2/(4r^2)\) for \(0\le d\le2r\). Taking its complement at \(d=2r-\varepsilon\) proves (2).

**4. Moving-cap crossover.** Set \(a=\lambda\varepsilon\). Except on a set with asymptotically negligible mass, a sample point on one of the two hemispherical caps has the form \(rn+a\operatorname{sgn}(n_3)e_3\), with \(n\in S^2\), while the other lies near the opposite spherical direction \(-n\). Let \(\delta\) denote the small angle between the second direction and \(-n\), and put \(z=|n_3|\). Away from the equator \(n_3=0\), the exact distance has the uniform expansion, for \(\delta=O(\sqrt\varepsilon)\),
\[
2(r+a)-D=2a(1-z)+\frac r4\delta^2+O_{r,\lambda}(\varepsilon^{3/2}).\tag{8}
\]
The \(\varepsilon^{3/2}\) bound follows from the mixed translation/angular error \(O(a\delta)\), the quartic spherical-angle term and \(O(a^2)\). For a uniform second spherical direction, an angular ball of radius \(\delta_0\) about an antipode has probability \(\delta_0^2/4+O(\delta_0^4)\). Equation (8) therefore gives, conditional on the first direction,
\[
\Pr\{D>2(r+a)-\varepsilon\mid n\}
=\frac\varepsilon r[1-2\lambda(1-z)]_++o_{r,\lambda}(\varepsilon)
\]
away from the equatorial strip. Bounded convergence permits discarding an arbitrarily thin equatorial strip after first taking the limit. The normalized cap measure tends to uniform spherical measure, under which \(z=|n_3|\) is uniform on \([0,1]\).

For completeness, the cylinder area fraction is \(a/(a+r)=O(\varepsilon)\). For any given cylindrical point, the set of other boundary points with a nearly maximal separation lies in an angular \(O(\sqrt\varepsilon)\) neighborhood of its opposite equatorial direction, of cap area \(O(\varepsilon)\); hence all cylinder-involved pairs are \(O(\varepsilon^2)\). Cap pairs on the same hemisphere contribute only \(o(\varepsilon)\), since almost antipodal directions from the same hemisphere force both into a vanishing-width equatorial strip. The remaining cross-cap pairs yield (3) after averaging over \(z\). Elementary integration gives (4). Direct differentiation gives the \(C^1\)-not-\(C^2\) statement.

**5. Recovery.** With \(d=2(a+r)\), (1) gives \(C=1/(2ad)\), so solving for \(a,r\) proves (5). Positivity of both parameters is equivalent to \(Cd^2>1\).

## Verification
The accompanying `verify_capsule.py` evaluates an *independent exact cap-to-cap angular integral*, without replacing the Cartesian point-pair distance by its quadratic approximation. It checks fixed-shape \(\varepsilon^2\) coefficients, the near-sphere crossover at several \(\lambda\) and \(\varepsilon\) values, scale invariance, shape reconstruction, and the \(C^1\)-not-\(C^2\) algebra. Numerical quadrature supports the coefficients and scaling; the proofs are the expansions, localization and dominated-limit argument above, not finite testing. Run `python verify_capsule.py` with Python 3 and NumPy installed.

## Relationship to prior work
Mayer and Molchanov (2006, arXiv:math/0605289v1, §§4–5) give general near-diameter methodology and the explicit spherical-boundary law. Their complete public text was inspected. They study spherical symmetry and sampling on or inside balls; their statements do not include capsule surface-area sampling or the moving-axial-length crossover. Schrempp (2017, arXiv:1709.03706v1, §§3–6) studies extreme interpoint distances with densities absolutely continuous relative to ambient volume on smooth bodies; this does not imply the surface-supported law here. A published study of random *central section areas* of capsules has a different random observable. Published extremal chord results for cylinders use motion-invariant random lines rather than independent surface points. The exact sphere formula (2), the elementary capsule surface area and local quadratic expansions are acknowledged as known ingredients; the new composite claim is the fixed-capsule coefficient together with the uniform near-ball crossover (3)–(4).

## Limitations
No complete finite-deficit chord-length density is claimed. The small-deficit remainder in (1) is not uniform as \(a\to0\); the separate crossover result (3) treats fixed \(\lambda\) and does not claim uniformity for \(\lambda\to\infty\). The analysis is confined to three-dimensional capsules with a circular cylindrical band, spherical endcaps, independent surface-area samples and ambient Euclidean distances. Related unindexed stereological calculations may contain equivalent special cases; historical priority is not independently established.

## References
1. M. Mayer and I. Molchanov, *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, first arXiv posting 2006-05-11, arXiv:math/0605289v1. https://arxiv.org/abs/math/0605289 (full public HTML inspected, especially §5.2).
2. M. Schrempp, *Limit laws for the diameter of a set of random points from a distribution supported by a smoothly bounded set*, first arXiv posting 2017-09-12, arXiv:1709.03706v1. https://arxiv.org/html/1709.03706v1 (full public HTML inspected, especially §§3,5–6).
3. L. Portal et al., *Jamming of hard rods I: From Onsager to Edwards*, first arXiv posting 2011-02-03, arXiv:1102.0608v1. https://arxiv.org/abs/1102.0608 (capsule/spherocylinder context).
4. *A sharp cap-contact singularity in random central sections of capsules*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-cap-contact-singularity-in-random-central-sections-of-ca--c05ab623ea0b (full theorem and proof inspected; a distinct central-section observable).
5. *Uniform near-diameter crossover and sharp anisotropy ordering for ellipsoids*, publicly available result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-uniform-near-diameter-crossover-and-sharp-anisotropy-ordering-fo--157978e267c9 (full theorem and proof inspected; volume-uniform ellipsoids).
