# Sharp Crofton dust coefficient for convex polygons and its parallelogram extremum

## Finding
Let \(K\) be any nondegenerate compact convex Euclidean polygon of area \(A\), perimeter \(P\), and genuine interior angles \(\alpha_1,\ldots,\alpha_m\in(0,\pi)\). Choose an unoriented line with Euclidean-motion-invariant measure \(d\theta\,dt\), conditioned on meeting \(K\). The line cuts \(K\) into two pieces; define \(S\) to be the smaller piece's area divided by \(A\), so \(0\le S\le1/2\). Define for \(0<\alpha<\pi\)
\[
J(\alpha)=2\sqrt{\frac2{\sin\alpha}}
\int_0^{(\pi-\alpha)/2}
\sqrt{\cos^2t-\sin^2(\alpha/2)}\,dt.
\]
Then, as \(\varepsilon\downarrow0\),
\[
\Pr(S\le\varepsilon)=C(K)\sqrt{\varepsilon}+o(\sqrt\varepsilon),
\qquad C(K)=\frac{\sqrt A}{P}\sum_{i=1}^m J(\alpha_i).
\]
This is a scale- and rotation-invariant *exact leading coefficient*, valid without regularity, equal-side, or symmetry assumptions.

For **every nondegenerate parallelogram**, \(C(K)<\sqrt2\), and this constant is sharp over all parallelograms but unattained. It is approached by rhombi whose acute interior angle tends to zero. For a regular \(n\)-gon, \(n\ge3\), the coefficient obeys the sharp large-order law
\[
C(P_n)=\frac{\pi^2}{4\sqrt n}+O(n^{-5/2}).
\]
Under the *same Crofton protocol* a disk has instead
\[
\Pr(S\le\varepsilon)
\sim\left(\frac{3\pi}{4\sqrt2}\right)^{2/3}\varepsilon^{2/3}.
\]
In particular, the polygon and smooth-disk dust exponents are distinct, and the polygonal leading coefficient tends to zero as the number of sides grows.

## Assumptions and scope
A convex polygon means a compact convex polygonal region with positive area and no redundant collinear vertices. Lines are unoriented, parametrized by a unit normal \(u=(\cos\theta,\sin\theta)\), \(0\le\theta<\pi\), and signed offset \(t\in\mathbb R\), with measure \(d\theta\,dt\). The line law is that measure normalized over lines meeting \(K\). By the planar Cauchy-Crofton formula, the normalizing mass is \(P\). The random variable uses Euclidean area, not chord length and not an independently chosen pair of boundary points. The limit \(\varepsilon\to0\) is taken with the polygon fixed; the large-\(n\) limit of the coefficient is a separate limit. Degenerate parallelograms are excluded from the inequality and appear only as a limiting sharpness sequence.

## Proof
**1. From area fractions to support-cap widths.** For a unit normal \(u\), let \(h(u)=\max_{x\in K}u\cdot x\). For \(s\in(0,A/2)\), define \(\delta(u,s)\) uniquely by
\[
\operatorname{area}\{x\in K:u\cdot x\ge h(u)-\delta(u,s)\}=s.
\]
For each unoriented normal, the set of lines cutting off area at most \(s\) lies in its two disjoint support-side intervals. Combining the two oriented sides gives the exact identity
\[
\Pr(S\le\varepsilon)
=\frac1P\int_0^{2\pi}\delta(u_\theta,\varepsilon A)\,d\theta,
\qquad0<\varepsilon<1/2.
\]

**2. Local corner calculation.** For almost every \(u\), the exposed support face is a single vertex \(v\) whose two incident inward-pointing unit edges \(e_1,e_2\) meet at angle \(\alpha\in(0,\pi)\). Both \(p=-u\cdot e_1\) and \(q=-u\cdot e_2\) are positive. For sufficiently small \(\delta\), the cap is exactly the triangle whose two edge-intersection distances from \(v\) are \(\delta/p\) and \(\delta/q\). Hence its area is \(\delta^2\sin\alpha/(2pq)\), giving
\[
\lim_{s\downarrow0}\frac{\delta(u,s)}{\sqrt s}
=\sqrt{\frac{2pq}{\sin\alpha}}.
\]
The exceptional outward edge-normal directions are finite and therefore have zero angular measure.

**3. Uniform domination and integration.** Fix a disk \(B(z,r)\subset K\) and an upper bound \(D\) on the diameter of \(K\). For every support point \(v\) and sufficiently small cap thickness \(\delta\), convexity places a disk of radius at least \(\delta r/(D+r)\) inside the cap: take a homothetic copy of \(B(z,r)\) with center on the segment from \(v\) to \(z\). Thus cap area is at least \(\pi r^2\delta^2/(D+r)^2\). In particular, \(\delta(u,s)/\sqrt s\) is uniformly bounded in \(u\) for small \(s\), so dominated convergence applies to the exact line integral. Every vertex contributes the integral of the preceding corner limit over its outward normal cone.

Represent the two incident edges by \((\cos(\alpha/2),\pm\sin(\alpha/2))\); represent an outward normal by \((-\cos t,\sin t)\) with \(|t|<(\pi-\alpha)/2\). Their negative dot-product is \(\cos(t\pm\alpha/2)\), whose product is \(\cos^2t-\sin^2(\alpha/2)\). Consequently each vertex's normal-cone integral is precisely \(J(\alpha)\), proving the displayed general coefficient.

**4. Sharp parallelogram bound.** A parallelogram of side lengths \(a,b>0\) and included angle \(0<\alpha<\pi\) has \(A=ab\sin\alpha\), \(P=2(a+b)\), and two occurrences each of \(\alpha\) and \(\pi-\alpha\). Therefore
\[
C(K)=\frac{\sqrt{ab\sin\alpha}}{a+b}
\bigl(J(\alpha)+J(\pi-\alpha)\bigr).
\]
In the preceding integral put \(p(t)=\cos(t+\alpha/2)\), \(q(t)=\cos(t-\alpha/2)\). The arithmetic-geometric mean inequality and direct integration give
\[
\int_{-(\pi-\alpha)/2}^{(\pi-\alpha)/2}\sqrt{p(t)q(t)}\,dt
<\frac12\int(p(t)+q(t))\,dt=1+\cos\alpha.
\]
The inequality is strict because \(p\ne q\) except at isolated points. Replacing \(\alpha\) by \(\pi-\alpha\) gives the strict counterpart with \(1-\cos\alpha\). Adding,
\[
J(\alpha)+J(\pi-\alpha)
<2\sqrt{\frac2{\sin\alpha}},
\]
so \(C(K)<2\sqrt{2ab}/(a+b)\le\sqrt2\). For \(a=b\) and \(\alpha\downarrow0\), dominated convergence in the corner integral gives \(\sqrt{\sin\alpha}\,J(\alpha)\to2\sqrt2\) and \(\sqrt{\sin\alpha}\,J(\pi-\alpha)\to0\). Thus \(C(K)\to\sqrt2\). No nondegenerate equality case exists.

**5. Regular polygon and disk limits.** Write \(\beta=2\pi/n\) for the exterior angle of a regular \(n\)-gon. The identity
\[
J(\pi-\beta)=2\sqrt{\frac2{\sin\beta}}
\int_0^{\beta/2}\sqrt{\sin^2(\beta/2)-\sin^2t}\,dt
=\frac{\pi\sqrt2}{8}\beta^{3/2}(1+O(\beta^2))
\]
follows on substituting \(t=\beta v\) and using the area of a quarter unit disk. With circumradius one, \(A_n=(n/2)\sin\beta\) and \(P_n=2n\sin(\beta/2)\). Substitute into \(C(P_n)=n\sqrt{A_n}J(\pi-\beta)/P_n\) to obtain \(C(P_n)=\pi^2/(4\sqrt n)+O(n^{-5/2})\).

For the unit disk, the area of a cap of height \(\delta\) is \(\arccos(1-\delta)-(1-\delta)\sqrt{2\delta-\delta^2}=(4\sqrt2/3)\delta^{3/2}+O(\delta^{5/2})\). Under invariant-line conditioning the offset is uniform on \([-1,1]\), and the probability of two caps of height at most \(\delta\) is \(\delta\). Set the cap area equal to \(\pi\varepsilon\) to obtain the disk asymptotic.

## Verification
A reproducible standalone script, `verify_crofton.py`, computes the angle integrals, tests the parallelogram bound over nondegenerate shapes, and independently evaluates the **finite-area** cutting probability by geometric half-plane clipping and numerical quadrature over line normals. For square, skew parallelogram, triangle and octagon, the directly integrated ratios \(\Pr(S\le\varepsilon)/\sqrt\varepsilon\) approach the proposed coefficients. It also tests the \(n^{-1/2}\) scaling on regular polygons and sharpness along thin rhombi. These finite computations are corroboration, not the proof of the limit or the global bound.

## Relationship to prior work
Dias and Parisio, *Minimal Fragmentation of Regular Polygonal Plates* (2014, arXiv:1404.6106), derive a square-root dust law and a finite-side regular-polygon coefficient. **Their sampling law differs:** they select a boundary starting point and an angle independently and uniformly (Section I, opening definition), not a line with invariant measure \(d\theta\,dt\) conditioned to hit the polygon. Their regular-polygon coefficient therefore does not supply the present Crofton coefficient, parallelogram extremum, or decreasing large-order law. Bäsel, *Random chords and point distances in regular polygons* (2012, arXiv:1204.2707), explicitly uses invariant line measure and obtains chord-length and point-pair distance distributions; neither is a distribution of the *area of the smaller piece* nor yields the parallelogram bound by a direct implication. The 2011 predecessor of Dias and Parisio was identified bibliographically but could not be examined completely. The coefficient's historical priority is therefore a best-knowledge claim subject to broader specialist literature review.

## Limitations
The coefficient is a one-sided small-area asymptotic for fixed convex polygons, not a complete distribution at positive area thresholds. No uniform-in-\(n\) crossover theorem is asserted. The supremum \(\sqrt2\) is only among nondegenerate parallelograms and is approached by degenerating rhombi; no statement is made about a universal extremum among all convex polygons. The disk exponent concerns the invariant-line protocol only. The comparisons do not constitute independent historical certification.

## References
1. L. Dias and F. Parisio, *Minimal Fragmentation of Regular Polygonal Plates*, arXiv:1404.6106, first posted April 24, 2014; Phys. Rev. E **90** (2014), 032405, DOI: 10.1103/PhysRevE.90.032405.
2. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first posted April 12, 2012; Acta Math. Univ. Comenianae **83** (2014), 1–18.
3. F. Parisio and L. Dias, *Minimal fragmentation problem*, arXiv:1109.2006, first posted September 9, 2011; Phys. Rev. E **84** (2011), 035101(R). Bibliographic comparison only; complete original text not inspected.
