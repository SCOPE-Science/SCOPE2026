# Exact polygon laws for random affine sections of a right triangular bipyramid

## Finding
For every \(h>0\), let \(B_h\subset\mathbb R^3\) have the five vertices
\[
 v_j=(\cos(2\pi j/3),\sin(2\pi j/3),0)\quad (j=0,1,2),\qquad
 v_+=(0,0,h),\quad v_-=(0,0,-h).
\]
Choose an isotropic uniformly random (IUR) affine plane conditioned to intersect \(B_h\): its unoriented unit normal has rotation-invariant measure and its offset has Lebesgue measure, both restricted to intersecting planes and jointly normalized. Almost surely the section is a polygon with \(N\in\{3,4,5,6\}\) sides.

Put \(c=3\sqrt3/4\) and, for \(h>0\),
\[
\begin{aligned}
 F(h)&=\frac3\pi\left[\frac{\sqrt3}{2}\arctan(2h)
 -\sqrt{1+h^2}\arctan\frac{\sqrt3h}{\sqrt{1+h^2}}
 +\frac{\pi h}{3}\right],\\
 G(h)&=\frac3\pi\left[-\frac{\sqrt3}{2}\arctan\frac1{2h}
 +\sqrt{1+h^2}\arctan\frac{\sqrt{1+h^2}}{\sqrt3h}
 -\frac{\pi h}{6}\right],\\
 W(h)&=h+c-F(h).
\end{aligned}
\]
Then the **entire polygon-type distribution** is
\[
\boxed{\quad
\begin{aligned}
 \mathbb P_h(N=3)&=\frac{h-F(h)}{W(h)},&
 \mathbb P_h(N=4)&=\frac{c-F(h)-G(h)}{W(h)},\\
 \mathbb P_h(N=5)&=\frac{F(h)}{W(h)},&
 \mathbb P_h(N=6)&=\frac{G(h)}{W(h)}.
\end{aligned}\quad}
\]
Here \(W(h)>0\) is the averaged full offset width. All four probabilities are positive for every finite \(h>0\).

The pentagonal-section probability has **one and only one global maximizer** \(h_*\in(0,\infty)\), characterized by
\[
 \boxed{\quad F'(h_*)(h_*+c)=F(h_*).\quad}
\]
Numerically, \(h_*\simeq1.211448413583\) and \(\mathbb P_{h_*}(N=5)\simeq0.462970871315\). The hexagonal-section probability is strictly decreasing as \(h\) increases. The uniqueness statements are exact; decimals are numerical approximations only.

## Assumptions and scope
The base triangle has circumradius one, is centered at the origin, and the two apices are directly above and below its center at height \(\pm h\). The angular law is Haar-uniform over unoriented normals. **Offsets are not sampled independently after first conditioning on intersection**: the correct conditional law of planes is the restriction of the invariant product measure \(d\sigma(u)\,ds\) to all intersecting planes, which biases normals proportionally to the body's width. Planes through a vertex, coplanar with an edge, or producing a degenerate section have measure zero.

## Proof
**1. Intersections and edge crossings.** Fix a normal direction and write it as
\[
 u=(\sqrt{1-t^2}\cos\phi,\sqrt{1-t^2}\sin\phi,\pm t),\qquad 0\le t\le1.
\]
For Haar-uniform normals, \(t\) is uniform on \([0,1]\) and \(\phi\) uniform on \([0,2\pi)\), independently. Let \(a=ht\), and let \(b_1\le b_2\le b_3\) be the increasing rearrangement of the projected base-vertex coordinates
\[
 \sqrt{1-t^2}\cos(\phi+2\pi j/3),\quad j=0,1,2.
\]
Their sum is zero, so \(b_1\le0\le b_3\). The nine edges of \(B_h\) are the three base edges and the six apex-to-base edges. Offsets \(s\) between successive projected vertex levels have a fixed set of crossed edges, and the number of crossed edges equals the number of vertices of the nondegenerate planar section.

The interval of offsets producing **five** crossed edges is exactly \((-a,a)\cap(b_1,b_3)\): three apex-to-base edges and two base edges cross there. Its length is
\[
 \ell_5=\min(a,b_3)+\min(a,-b_1).
\]
For offsets strictly above \(a\) or below \(-a\), both apices lie on the same side of the plane. There are **six** crossings precisely when two base vertices are on the other side; the total length of these offsets is
\[
 \ell_6=(|b_2|-a)_+.
\]
For offsets \(|s|<a\) outside \((b_1,b_3)\), exactly three apex-to-base edges cross, hence
\[
 \ell_3=2a-\ell_5.
\]
All other intersecting offsets have four crossings. The full admissible offset interval has length
\[
 \ell=\max(a,b_3)+\max(a,-b_1)
 =2a+(b_3-b_1)-\ell_5,
\]
which gives \(\ell_4=(b_3-b_1)-\ell_5-\ell_6\). These are identities for all directions outside a measure-zero set, not numerical classifications.

**2. Integrating offset lengths.** Write \(\langle\cdot\rangle\) for expectation over uniformly distributed normals. The probability of a type is \(\langle\ell_k\rangle/\langle\ell\rangle\), not \(\langle\ell_k/\ell\rangle\). Since \(t\) is uniform on \([0,1]\), \(\langle2a\rangle=h\). The three edges of the equilateral base triangle each have length \(\sqrt3\); the mean three-dimensional directional width of the triangle is one quarter of its perimeter, hence
\[
 \langle b_3-b_1\rangle=c=3\sqrt3/4.
\]
For \(m\ge0\), direct integration gives
\[
 \int_0^1\min(ht,m\sqrt{1-t^2})\,dt
 =\frac m2\arctan(h/m),
\qquad
 \int_0^1(m\sqrt{1-t^2}-ht)_+\,dt
 =\frac m2\arctan(m/h).
\]
The first identity is interpreted continuously at \(m=0\). The two \(\min\) terms in \(\ell_5\) have equal spherical averages by antipodal symmetry. On each of the three congruent maximum-coordinate sectors, \(\max_j\cos(\phi+2\pi j/3)=\cos\theta\) for \(-\pi/3\le\theta\le\pi/3\). Therefore
\[
 \langle\ell_5\rangle
 =\frac3\pi\int_0^{\pi/3}
 \cos\theta\,\arctan\frac h{\cos\theta}\,d\theta=F(h).
\]
Similarly the absolute median of the three cosines has twelve congruent angular sectors, each parameterized by \(\sin\theta\) for \(0\le\theta\le\pi/6\), so
\[
 \langle\ell_6\rangle
 =\frac3\pi\int_0^{\pi/6}
 \sin\theta\,\arctan\frac{\sin\theta}{h}\,d\theta=G(h).
\]
Integration by parts followed by the substitutions \(\tan\theta\) in the resulting rational integrals yields precisely the two displayed arctangent expressions. Thus
\[
 \langle\ell_3\rangle=h-F(h),\quad
 \langle\ell_4\rangle=c-F(h)-G(h),\quad
 \langle\ell\rangle=h+c-F(h),
\]
and normalization proves the four probabilities. Every type has an open, positive-measure set of orientations and offsets (the six-gon case occurs in sufficiently near-horizontal normals), which proves strict positivity.

**3. Unique pentagon maximum.** From its integral representation, \(F(0+)=0\), \(F(\infty)=c\), and
\[
 F'(h)=\frac3\pi\int_0^{\pi/3}
 \frac{\cos^2\theta}{h^2+\cos^2\theta}\,d\theta>0,
 \qquad
 F''(h)=-\frac{6h}{\pi}\int_0^{\pi/3}
 \frac{\cos^2\theta}{(h^2+\cos^2\theta)^2}\,d\theta<0.
\]
Moreover \(F'(0+)=1\) and \(F'(\infty)=0\). Differentiating \(F/W\) shows that its derivative has the sign of
\[
 Q(h)=F'(h)(h+c)-F(h).
\]
Now \(Q'(h)=(h+c)F''(h)<0\), \(Q(0+)=c>0\), and \(Q(\infty)=-c<0\). Hence \(Q\) has precisely one zero, and the pentagon probability increases strictly before it and decreases strictly after it. Likewise the integral for \(G\) is strictly positive and strictly decreasing, while \(W'(h)=1-F'(h)>0\) for \(h>0\). Thus \(G/W\) strictly decreases, proving the hexagon assertion.

## Verification
A standalone Python 3 checker (`VERIFY.py`, using only the standard library) independently evaluates the one-dimensional integrals by midpoint quadrature, compares them with the closed forms, solves the uniquely defined optimizing equation, and directly counts crossed edges in sampled three-dimensional planes. The Monte Carlo uses the correct directional width weights. Tested heights \(0.2,0.9,2\) and the deterministic checker reported `BIPYRAMID_AFFINE_SECTION_POLYGON_LAW_CHECKS_PASSED`. Exact geometry, normalization, positivity, uniqueness and infinite-dimensional quantifiers rely on the foregoing proof, not on finite simulations or quadrature.

## Relationship to prior work
Brandenburg, De Loera and Meroni (2023) establish the general chamber decomposition of affine polytope sections and fixed edge-crossing combinatorial types; it does **not** evaluate the invariant-measure mass of each chamber for this bipyramid. Van der Jagt, Jongbloed and Vittorietti (2023) study isotropically sampled hyperplane **section areas**, including the correct invariant measure, not this discrete polygon-type law. Sukiasyan (1982) gives numerical IUR polygon-section probabilities for triangular pyramids, triangular prisms, rectangular parallelepipeds and hexagonal prisms, but not this five-vertex bipyramid, and does not give the stated formulas or optimizer. A known exact equilateral-triangular-prism affine-section distribution concerns a different solid; duality of prism and bipyramid does not identify these noncentral Crofton-conditioned section probabilities. Existing extremal **shadow-area** results for this bipyramid are for projections, not affine sections; the operation and sampling measure differ. Thus the contribution is the **entire explicit four-atom law for this family** and the exact uniqueness of its pentagon-frequency maximizer, not general chamber theory or the IUR sampling definition.

## Limitations
The result concerns congruent equilateral base configurations and symmetric heights \(\pm h\), not arbitrary skew or asymmetric bipyramids. It treats section *polygon types* rather than section areas or perimeters. The decimals for the optimizer are not claimed as algebraic constants. An older equivalent formula under alternative stereological nomenclature cannot be ruled out without exhaustive historical review; no independent mathematical audit has been performed.

## References
1. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1, first posted 2023-04-27, https://arxiv.org/html/2304.14239v1.
2. T. van der Jagt, G. Jongbloed and M. Vittorietti, *Existence and Approximation of Densities of Chord Length- and Cross Section Area Distributions*, arXiv:2305.02864v1, first posted 2023-05-04, https://arxiv.org/abs/2305.02864.
3. G. S. Sukiasyan, *On random sections of polyhedra*, Dokl. Akad. Nauk SSSR **263** (1982), 809–812, https://www.mathnet.ru/eng/dan45193.
4. A. E. Black and F. Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936v1, first posted 2024-06-11, https://arxiv.org/abs/2406.06936.
