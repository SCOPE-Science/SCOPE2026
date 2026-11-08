# Silhouette-conditioned circumradius laws for random regular-octahedron shadows

## Finding
Let \(O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\subset\mathbb R^3\). Choose an unoriented plane \(E=U^\perp\) from rotationally invariant probability measure, and let \(R\) be the Euclidean circumradius of its orthogonal shadow \(P_EO\). Let \(N\) be the number of vertices of that planar shadow. Almost surely \(N\in\{4,6\}\).

**Exact joint law.** Define, for \(0\le t\le1/\sqrt3\),
\[
\alpha(t)=\arcsin\frac{t}{\sqrt{1-t^2}},\qquad
\beta(t)=\arccos\frac{t}{\sqrt{2(1-t^2)}}-\frac\pi4,
\]
\[
L(t)=\frac\pi4-\alpha(t),\quad
L_4(t)=\begin{cases}\beta(t)-\alpha(t),&0\le t<1/\sqrt6,\\0,&1/\sqrt6\le t\le1/\sqrt3,\end{cases}
\quad L_6(t)=L(t)-L_4(t).
\]
For each \(j\in\{4,6\}\), the full **joint, non-conditional** cumulative probability is
\[
\boxed{\Pr\{N=j,\ R\le r\}=\frac{12}{\pi}
\int_{\sqrt{1-r^2}}^{1/\sqrt3}L_j(t)\,dt},
\qquad \sqrt{2/3}\le r\le1.
\]
It equals zero for \(r<\sqrt{2/3}\) and equals \(\Pr(N=j)\) for \(r>1\). The integral is an ordinary proper, nonnegative one-dimensional integral. In particular
\[
\Pr(N=6)=\frac4\pi\arctan\frac{\sqrt2}{5},\qquad
\Pr(N=4)=1-\Pr(N=6).
\]
The two conditional supports differ sharply:
\[
\operatorname{supp}(R\mid N=6)=[\sqrt{2/3},1],\qquad
\operatorname{supp}(R\mid N=4)=[\sqrt{5/6},1].
\]
Moreover **four-vertex shadows have strictly stochastically larger circumradius** than six-vertex shadows:
\[
\boxed{\Pr(R\le r\mid N=4)<\Pr(R\le r\mid N=6)}
\quad\text{for all }\sqrt{2/3}<r<1.
\]

**Sharp endpoint laws.** As \(\varepsilon\downarrow0\),
\[
\boxed{\Pr\{N=4,R\le\sqrt{5/6}+\varepsilon\}
\sim\frac{30\sqrt6}{\pi}\varepsilon^2},\qquad
\boxed{\Pr\{N=6,R\le\sqrt{2/3}+\varepsilon\}
\sim\frac{18\sqrt3}{\pi}\varepsilon^2},
\]
\[
\boxed{\Pr\{N=4,R>1-\varepsilon\}\sim3\sqrt{2\varepsilon}},\qquad
\boxed{\Pr\{N=6,R>1-\varepsilon\}\sim\frac{6\sqrt2}{\pi}\varepsilon}.
\]
Thus the extreme upper tail is of square-root order for quadrilateral shadows, but only linear order for hexagonal shadows. The two joint CDFs are \(C^1\) across the interior phase radius \(\sqrt{5/6}\), with jumps in their second derivatives of opposite signs: respectively \(+60\sqrt6/\pi\) and \(-60\sqrt6/\pi\). Their sum has no such interior jump.

For completeness the *unconditioned* CDF is elementary. With \(t=\sqrt{1-r^2}\),
\[
\Pr(R\le r)=1-3t+\frac{12}{\pi}\left[t\alpha(t)+\arctan\sqrt{1-2t^2}-\frac\pi4\right],
\quad\sqrt{2/3}\le r\le1.
\]
Its squared-radius expectation is
\[
\mathbb E R^2=\frac23+\frac2\pi\left(1-\frac1{\sqrt3}\right).
\]
The unconditioned formulas are included as consistency checks and are not asserted to be novel independently of existing spherical-coordinate statistics.

## Assumptions and scope
All distances use the Euclidean metric within the orthogonal projection plane. The octahedron has vertices at unit coordinate vectors, so its original circumradius is one and its edge length is \(\sqrt2\). Haar-random planes are represented by \(U\) uniform on \(S^2\), with \(U\) and \(-U\) giving the same plane. The circumradius means the **minimum radius of an enclosing planar disk**, not the projected body's inradius, a random directional width, or the circumradius of a central section. An exceptional set of normals produces degenerate vertex coincidences; it has spherical measure zero and does not change any probability statement. All claimed limit laws are for real \(\varepsilon\downarrow0\) with the octahedron fixed.

## Proof
**1. Circumradius and silhouette criterion.** Let \(p_i=P_{U^\perp}e_i=e_i-U_iU\). Because the projected octahedron \(\operatorname{conv}\{\pm p_1,\pm p_2,\pm p_3\}\) is centrally symmetric, its least enclosing disk can be centered at zero: if any disk \(B(z,r)\) encloses the set, so does \(B(-z,r)\), and the triangle inequality gives \(\|x\|\le(\|x-z\|+\|x+z\|)/2\le r\) for every point of the set. Consequently
\[
R^2=\max_i\|p_i\|^2=1-\min_i U_i^2.
\]
For nonzero normal coordinates, \(\sum_iU_ip_i=0\). The pair \(\pm p_i\) is not an extreme-vertex pair precisely if \(p_i\) lies in the diamond \(\operatorname{conv}\{\pm p_j,\pm p_k\}\), equivalently \(|U_i|\ge|U_j|+|U_k|\). Two such conditions cannot both hold for strictly positive coordinates. Thus \(N=4\) if the largest absolute normal coordinate exceeds the sum of the other two, and \(N=6\) otherwise. Equalities and zero coordinates have probability zero.

**2. Exact spherical disintegration.** In each of the \(48\) signed and ordered coordinate chambers, write
\[
a=\sqrt{1-t^2}\cos\varphi,\qquad
b=\sqrt{1-t^2}\sin\varphi,\qquad
c=t,\quad a\ge b\ge c\ge0.
\]
Here \(0\le t\le1/\sqrt3\) and \(\alpha(t)\le\varphi\le\pi/4\). The surface area element on the unit sphere is exactly \(dt\,d\varphi\). Dividing the \(48\) chambers by total area \(4\pi\) gives probability density factor \(12/\pi\). Since \(R=\sqrt{1-t^2}\), the event \(R\le r\) is \(t\ge\sqrt{1-r^2}\).

The quadrilateral inequality \(a\ge b+c\) becomes
\[
\cos(\varphi+\pi/4)\ge \frac{t}{\sqrt{2(1-t^2)}},
\quad\text{hence}\quad\varphi\le\beta(t).
\]
The angular interval \([\alpha(t),\beta(t)]\) is nonempty precisely when \(t\le1/\sqrt6\). To see the threshold directly, at the last admissible normal \(a=b+c\) and \(b=c\), hence \((a,b,c)=(2,1,1)/\sqrt6\). Integrating the available angular widths yields the two joint formulas. Their positivity and the exact supports follow from the positive widths on the respective interiors. Integrating \(L_6\) over its entire range recovers the already-known solid-angle value \(4\arctan(\sqrt2/5)/\pi\); alternatively this is the spherical area of the cone generated by \((1,1,0),(1,0,1),(0,1,1)\).

**3. Strict stochastic order.** Conditioning on \(t=\min_i|U_i|\), the probability of a four-vertex shadow is \(q(t)=L_4(t)/L(t)\). For \(0<t<1/\sqrt6\), the complementary numerator \(\pi/4-\beta(t)\) is strictly increasing, whereas \(L(t)=\pi/4-\alpha(t)\) is strictly decreasing. Therefore \(q(t)=1-(\pi/4-\beta(t))/L(t)\) is strictly decreasing. On the remaining interval \(q(t)=0\). Thus the likelihood ratio of the conditional densities of \(t\) given \(N=4\) and \(N=6\), proportional to \(q(t)/(1-q(t))\), decreases. Integrating this single-crossing density comparison shows that \(t\mid N=4\) is strictly stochastically smaller than \(t\mid N=6\). Because \(R=\sqrt{1-t^2}\) is strictly decreasing, the claimed strict reverse stochastic ordering of radii follows at every interior threshold.

**4. Endpoint expansions and interior regularity.** Direct differentiation gives
\[
\alpha'(t)=\frac1{(1-t^2)\sqrt{1-2t^2}},\qquad
\beta'(t)=-\frac1{(1-t^2)\sqrt{2-3t^2}}.
\]
At \(t_0=1/\sqrt6\), \(\beta(t_0)=\alpha(t_0)\) and \(\beta'(t_0)-\alpha'(t_0)=-\sqrt6\). Hence \(L_4(t)=\sqrt6(t_0-t)+O((t_0-t)^2)\) from below. The transformation \(r=\sqrt{1-t^2}\) gives \(t_0-t=\sqrt5(r-\sqrt{5/6})+O((r-\sqrt{5/6})^2)\). Integrating the triangular angular region yields \(30\sqrt6\varepsilon^2/\pi\) and the two opposite second-derivative jumps.

At \(t_1=1/\sqrt3\), only hexagons are possible and \(L_6(t)=\frac{3\sqrt3}{2}(t_1-t)+O((t_1-t)^2)\). Because \(t_1-t=\sqrt2(r-\sqrt{2/3})+O((r-\sqrt{2/3})^2)\), the hexagonal lower coefficient is \(18\sqrt3/\pi\).

Finally at \(t\downarrow0\), \(\alpha(t)=t+O(t^3)\), \(\beta(t)=\pi/4-t/\sqrt2+O(t^3)\). Thus \(L_4(t)=\pi/4+O(t)\), \(L_6(t)=t/\sqrt2+O(t^3)\). At \(r=1-\varepsilon\), \(t=\sqrt{1-r^2}=\sqrt{2\varepsilon}+O(\varepsilon^{3/2})\). Integrating from zero gives the two upper-tail coefficients exactly.

**5. Unconditioned consistency identities.** On \(0\le t\le1/\sqrt3\), inclusion-exclusion applied to \(|U_i|<t\) gives \(\Pr(\min|U_i|\ge t)=1-3t+3J(t)\), because simultaneous smallness of all three coordinates is impossible. The joint density of \((U_1,U_2)\) is \((2\pi\sqrt{1-x^2-y^2})^{-1}\) in the unit disk; differentiating its symmetric square integral gives \(J'(t)=\frac4\pi\alpha(t)\). Integration by parts yields \(J(t)=\frac4\pi[t\alpha(t)+\arctan\sqrt{1-2t^2}-\pi/4]\), proving the unconditioned formula. Similarly, \(\mathbb E(\min U_i^2)=\frac13-\frac2\pi+\frac2{\pi\sqrt3}\) by integrating the density \(3-(12/\pi)\alpha(t)\) against \(t^2\), proving the moment formula. These are independent checks on the two joint pieces.

## Verification
The standalone `verify.py` uses Python 3, NumPy and SciPy. It independently enumerates projected two-dimensional convex hulls and their circumradii for 2,400 random normals, compares the exact joint formulas with 600,000 independently drawn Gaussian-normalized sphere points at nine thresholds, integrates the quadrilateral angular region against the known vertex probability, checks strict conditional ordering on 48 interior thresholds, and checks the four endpoint constants at three decreasing scales. It returned `OCTAHEDRON_SHADOW_RADIUS_SILHOUETTE_LAW_OK 600000 2400 48`. These are diagnostic finite computations, not an infinite proof or independent expert validation.

## Relationship to prior work
Finch [1] computes planar projection area and perimeter moments and states the regular octahedron's four- versus six-vertex probabilities. Böröczky and Henk [2] study expected face numbers of regular-polytope random projections, not their joint distribution with a circumradius. Rivin [3] studies the minimum absolute coordinate of a uniform spherical vector, making the unconditional radius reduction a classical order-statistic object; the unconditioned radius law and moment are not counted as standalone novelty. Two accessible prior mathematical records [4,5] respectively establish the full inradius law of regular-octahedron planar shadows and the sharp six-vertex probability for triaxial octahedra. Inradius, vertex probability, and circumradius marginal data do not determine the **joint** radius–silhouette law. The specific new contribution assessed here is the full joint formula, its strict stochastic comparison, its split endpoint exponents and coefficients, and the interior second-derivative cancellation. Both the projection criterion and the total regular hexagon probability are explicitly prior facts.

## Limitations
This result is for the unit regular octahedron, not general triaxial or nonorthogonal octahedra, higher-dimensional projections, or biased directions. It does not claim a new theorem about the general minimum-coordinate statistic. The cited primary literature may not exhaust all equivalent terminology, especially the polar or support-function viewpoint; independent historical-priority confirmation is still warranted. No conclusions about moments or densities conditional on additional shadow attributes are asserted. Numerical checks supplement, but do not replace, the analytic proof.

## References
[1] S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464, first posted 2012-03-12, full text https://arxiv.org/abs/1203.2464, especially Sections 2.3 and 5.

[2] K. Böröczky Jr. and M. Henk, *Random Projections of Regular Polytopes*, author preprint SC-97-21 (May 1997); subsequently *Archiv der Mathematik* **73** (1999), 465–473. https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf.

[3] I. Rivin, *Spheres and Minima*, arXiv:math/0305252, first posted 2003-05-18; full text mirrored at https://www.researchgate.net/publication/2107079_Spheres_and_Minima.

[4] *Exact inradius law for random planar projections of the regular octahedron*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-inradius-law-for-random-planar-projections-of-the-regular--5fbcddcea5e5.

[5] *Sharp triaxial octahedron shadow bound and quadratic shape stability*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-triaxial-octahedron-shadow-bound-and-quadratic-shape-stabi--c544249c351b.
