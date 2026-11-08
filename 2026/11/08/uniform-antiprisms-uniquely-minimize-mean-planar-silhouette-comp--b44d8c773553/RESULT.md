# Uniform antiprisms uniquely minimize mean planar-silhouette complexity in every order

## Finding
Let \(n\ge3\) be an integer. Form a right regular \(n\)-gonal antiprism from two congruent regular polygons of circumradius \(1\), centered at heights \(\pm h\) and rotated by \(\pi/n\) relative to one another, where \(h>0\). For a uniformly oriented planar orthogonal projection, let \(N_{n,h}\) be the number of genuine sides of the projected convex polygon. Put \(c=\cos(\pi/n)\), \(d=1-c\), and \(M=4h^2+d^2\). Then
\[
\mathbb E N_{n,h}=\frac{2n}{\pi}\left[\arccos\left(\frac{d}{\sqrt M}\right)+\arccos\left(\frac{4ch^2-d^2}{M}\right)\right].
\]
For every fixed order \(n\), the expectation is **strictly decreasing** on \(0<h<h_*\) and **strictly increasing** on \(h>h_*\), where
\[
h_*^2=\frac{(1-c)(1+2c)}2.
\]
This minimizing height is exactly the height at which the triangular lateral faces are equilateral: **the uniform antiprism is the unique mean-silhouette minimizer** in the family.

The minimum is exactly
\[
\frac{2n}{\pi}\left[\arccos\sqrt{\frac{1-c}{3(1+c)}}+\arccos\left(\frac{4c-1}{3}\right)\right].
\]
The limits at the flat and tall ends are, respectively, \(2n\) and \(n+2\); both are strictly larger than the finite minimum. As \(n\to\infty\), the minimum is \(n+\sqrt3+O(n^{-2})\). At order \(n=4\), \(h_*=2^{-3/4}\) and the minimal expectation is approximately \(5.716099405109\).

## Assumptions and scope
The projection plane is a Haar-uniform unoriented two-dimensional linear subspace of ordinary Euclidean \(\mathbb R^3\), with the solid fixed. The right antiprism has exactly two parallel regular \(n\)-gon caps and \(2n\) isosceles triangular side faces, all convex for the stipulated parameters. The unit circumradius is a normalization: for a base radius \(R>0\), the unique minimizing half-height equals \(Rh_*\). All counting statements concern generic orientations; the finite union of facet-parallel exceptional directions has zero Haar probability. The case \(n=3\) (a triangular antiprism, or an octahedron) is included.

## Proof
**Step 1: Spherical edge-count identity.** For a generic viewing direction \(u\in S^2\), a convex polyhedron edge between facets with outward unit normals \(v,w\) contributes one edge to the projection boundary precisely when \((u\cdot v)(u\cdot w)<0\). If their angular separation is \(\gamma\in(0,\pi)\), the projection of \(u\) onto their normal span has a uniform azimuth, and opposite signs occupy angular measure \(2\gamma\) out of \(2\pi\). Thus the edge's probability is \(\gamma/\pi\). By linearity of expectation, \(\mathbb E N=\pi^{-1}\sum_e\gamma_e\). This familiar general silhouette identity is not claimed as new.

**Step 2: The two antiprism edge orbits.** Write \(\phi=\pi/n\) and \(c=\cos\phi\), \(d=1-c\). Rotate coordinates so that a particular top base edge has endpoints \((c,\pm\sin\phi,h)\), and its incident lateral triangle has third vertex \((1,0,-h)\). A normal computed from its two spanning edge vectors and oriented outward is proportional to \((2h,0,d)\). The neighboring lateral triangle across a connecting top-to-bottom edge has outward normal proportional to \((2h\cos\phi,2h\sin\phi,-d)\). Both have squared norm \(M=4h^2+d^2\). The cap normal is \((0,0,1)\). Consequently the exterior angles along each of the \(2n\) base edges and each of the \(2n\) connecting edges are, respectively,
\[
\alpha(h)=\arccos\frac d{\sqrt M},\qquad
\beta(h)=\arccos\frac{4ch^2-d^2}{M}.
\]
There are no other edge orbits. The formula in the Finding follows from Step 1.

**Step 3: Exact global optimization.** Since \(\alpha=\arctan(2h/d)\), it increases bijectively from \(0\) to \(\pi/2\). Write \(s=\sin^2\alpha\), and \(k=1+c\). Then
\[
\cos\beta=ks-1,\qquad
\frac{d}{d\alpha}(\alpha+\beta)
=1-2\sqrt{\frac{k(1-s)}{2-ks}}.
\]
Here \(k\in[3/2,2)\) and \(0<s<1\), so every expression is well-defined. The derivative is strictly negative exactly when \(s<(4k-2)/(3k)\), and strictly positive exactly when \(s>(4k-2)/(3k)\). Thus there is exactly one global minimum, characterized by \(s_*=(4k-2)/(3k)\). Substituting \(s=4h^2/(4h^2+d^2)\) gives \(h_*^2=d(1+2c)/2\).

**Step 4: Geometric rigidity and sharp minimum.** Each base edge has squared length \(4(1-c^2)\); each connecting edge has squared length \(4h^2+2(1-c)\). Equating them is equivalent to \(h^2=d(1+2c)/2\). The side faces are isosceles by construction; therefore all edges have equal length exactly when every lateral triangle is equilateral. At the minimizer,
\[
\cos\alpha_* =\sqrt{\frac{1-c}{3(1+c)}},\qquad
\cos\beta_* =\frac{4c-1}{3},
\]
which supplies the exact minimum in the Finding. The endpoints follow directly from the angle limits \((\alpha,\beta)\to(0,\pi)\) as \(h\to0\), and \((\alpha,\beta)\to(\pi/2,\pi/n)\) as \(h\to\infty\). Strict monotonicity shows both limit values exceed the minimum.

**Step 5: Many-sided asymptotics.** For \(\phi=\pi/n\to0\), \(\cos\alpha_*=\tan(\phi/2)/\sqrt3\), so \(\alpha_*=\pi/2-\phi/(2\sqrt3)+O(\phi^3)\). Also \(\cos\beta_*=(4\cos\phi-1)/3\), so \(\beta_*=2\phi/\sqrt3+O(\phi^3)\). Therefore \(\alpha_*+\beta_*=\pi/2+\sqrt3\phi/2+O(\phi^3)\), yielding \(\min_h\mathbb E N_{n,h}=n+\sqrt3+O(n^{-2})\).

## Verification
The accompanying standalone `verify_antiprism.py` reproduces three symbolic identities linking the stationary point, equal-edge condition, and minimizing dihedral angle. It independently reconstructs visible-polygon vertex counts from planar convex hulls for \(2{,}700\) generic sample views, and compares them with the edge-normal indicator formula. An additional \(675{,}000\) isotropic viewing directions across twelve order/height profiles confirm the expected-count formula within a stated sampling tolerance; numerical evaluation also tests the minimizer for seven orders through \(40\). Its successful output ends with `ANTIPRISM_SILHOUETTE_OK`. Exact proof is Steps 1–5, not the samples.

## Relationship to prior work
Kettner and Welzl [1] developed the established general relationship between mean contour size and polyhedral dihedral angles. Glisse, Lazard, Michel, and Pouget [2] explicitly cite this earlier result while studying maximum silhouettes of random spherical polytopes; their objects and conclusions differ. Hartley, Pellicer, and Williams [3] treat regular abstract covers of antiprisms rather than metric height optimization or random planar shadows. The present claim concerns the **specific all-order identity, unique strict minimizing height, equivalence with equilateral side faces, and its sharp large-order asymptotic**; it does not claim novelty for Step 1 or the well-known construction of uniform antiprisms. No equivalent theorem was identified in the inspected records, but absence from searches is not proof of historical priority.

## Limitations
The result is restricted to coaxial right antiprisms with congruent regular bases and their conventional half-step twist. It does not optimize among arbitrary skewed antiprisms, general polyhedra, or non-Haar orientation distributions. The general contour-edge formula is prior work. The complete original text of Kettner–Welzl [1] was not obtained, so the possibility of an earlier unindexed antiprism specialization remains a priority risk. The mathematical argument and computational checks have not received independent validation.

## References
[1] L. Kettner and E. Welzl, “Contour Edge Analysis for Polyhedron Projections,” *Geometric Modeling: Theory and Practice*, pp. 379–394 (1997). https://doi.org/10.1007/978-3-642-60607-6_25.

[2] M. Glisse, S. Lazard, J. Michel, and M. Pouget, “Silhouette of a random polytope,” INRIA Research Report RR-8327, initial version July 2013; *Journal of Computational Geometry* 7 (2016), 86–99. https://hal.science/hal-00841374v2 ; https://doi.org/10.20382/jocg.v7i1a5.

[3] M. I. Hartley, D. Pellicer, and G. Williams, “Minimal covers of the prisms and antiprisms,” arXiv:1206.6119, first posted 2012-06-26. https://arxiv.org/abs/1206.6119.
