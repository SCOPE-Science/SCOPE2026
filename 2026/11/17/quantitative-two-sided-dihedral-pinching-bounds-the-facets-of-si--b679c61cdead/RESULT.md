# Quantitative two-sided dihedral pinching bounds the facets of simple spatial polytopes

## Finding
Fix \(0<\delta<\pi/4\) and \(2\delta<\alpha\le\pi/2+\delta\), with angles in radians. Define
\[
\ell=\frac\pi2-\delta,\qquad
E_*(\alpha,\delta)=4\arctan\!\left[\tan\!\left(\frac\ell4\right)\sqrt{\tan\!\left(\frac{3\ell}{4}\right)\tan\!\left(\frac{\alpha-2\delta}{4}\right)}\right].
\]
Every bounded, full-dimensional, **simple** convex three-polytope \(P\) with interior dihedral angles in \([\alpha,\pi/2+\delta]\) satisfies
\[
\boxed{f_2(P)\le 2+\frac{2\pi}{E_*(\alpha,\delta)}.}
\]
In particular, for a fixed \(\delta\), any sequence of such simple polytopes with \(f_2(P)\to\infty\) must have
\[
\liminf_{f_2(P)\to\infty}\min_{e\in E(P)}\theta_e\le 2\delta.
\]
For fixed positive \(\delta\), the displayed upper bound grows at most as \(O_\delta((\alpha-2\delta)^{-1/2})\) as \(\alpha\downarrow2\delta\). The square-root order is necessary for this **pointwise spherical-triangle lower-bound method**, not asserted optimal for polyhedral facet counts.

## Assumptions and scope
An interior dihedral angle \(\theta_e\in(0,\pi)\) is measured inside the convex polytope along an edge \(e\). A three-polytope is *simple* when exactly three facets meet at every vertex. Every facet and vertex is nondegenerate. The parameter conditions imply \(0<\ell<\pi/2\) and \(\alpha-2\delta>0\). All logarithmic or asymptotic limits keep \(\delta\in(0,\pi/4)\) fixed. No claim is made for nonsimple polytopes, for \(\alpha\le2\delta\), or for sharp global facet bounds.

## Proof
Let \(F=f_2(P)\), \(V=f_0(P)\). At any vertex \(v\), let \(n_1,n_2,n_3\) be the exterior unit normals to the three incident facets. The spherical normal cone \(T_v\subset S^2\) is their geodesic triangle. Its side lengths are the pairwise angles between the normals, hence the complements of the corresponding interior dihedral angles:
\[
\pi/2-\delta=\ell\ \le a,b,c\le\pi-\alpha=u.
\]
The normal cone is contained in an open hemisphere, since an interior point of \(P\), viewed from \(v\), gives a vector pairing strictly negatively with each incident exterior normal. Thus its spherical triangle has half-perimeter \(s=(a+b+c)/2<\pi\), and its spherical area \(E_v\) lies in \((0,2\pi)\).

Relabel so \(a\ge b\ge c\). The elementary estimates are
\[
\begin{aligned}
s&\ge3\ell/2,\\
s-a&=\tfrac12(b+c-a)\ge \tfrac12(2\ell-u)=\tfrac12(\alpha-2\delta),\\
s-b&=\tfrac12(a+c-b)\ge c/2\ge\ell/2,\\
s-c&=\tfrac12(a+b-c)\ge b/2\ge\ell/2.
\end{aligned}
\]
They imply all four arguments below are positive and less than \(\pi/2\). L'Huilier's spherical-area identity gives
\[
\tan^2(E_v/4)=\tan(s/2)\tan((s-a)/2)\tan((s-b)/2)\tan((s-c)/2).
\]
On the indicated interval the tangent is increasing. Substitution of the four lower bounds yields
\[
\tan(E_v/4)\ge\tan(\ell/4)\sqrt{\tan(3\ell/4)\tan((\alpha-2\delta)/4)},
\]
so \(E_v\ge E_*(\alpha,\delta)>0\).

The spherical normal cones of all vertices form a spherical tessellation, disjoint in interior and with total area \(4\pi\). Consequently \(VE_*\le\sum_vE_v=4\pi\). Since \(P\) is simple, its edge count satisfies \(2f_1=3V\); Euler's identity \(V-f_1+F=2\) therefore gives \(V=2F-4\). Solving \((2F-4)E_*\le4\pi\) proves the bound.

If \(F\to\infty\) while all maximal dihedral angles remain at most \(\pi/2+\delta\), but \(\liminf\min_e\theta_e>2\delta\), choose a common \(\alpha\) strictly between these values. The just-proved finite upper bound contradicts \(F\to\infty\).

Finally put \(\varepsilon=\alpha-2\delta\). The displayed definition gives
\[
E_*(\alpha,\delta)=2\tan(\ell/4)\sqrt{\tan(3\ell/4)}\,\sqrt\varepsilon+O_\delta(\varepsilon^{3/2}).
\]
The exponent \(1/2\) cannot be improved in a lower bound based *only* on the permitted sides of one normal triangle: consider a spherical triangle with side lengths \((2\ell-\varepsilon,\ell,\ell)\). For small positive \(\varepsilon\) it is nondegenerate and contained in a hemisphere. L'Huilier's identity gives its area
\[
2\tan(\ell/2)\sqrt{\tan\ell}\,\sqrt\varepsilon+O_\delta(\varepsilon^{3/2}).
\]
This is a local spherical construction; it does **not** show a matching sequence of full three-polytopes.

## Verification
A standalone deterministic verifier (`verify.py`) independently compares L'Huilier spherical areas with angles recovered via the spherical cosine law, tests the lower inequality on thousands of admissible spherical triangles, checks the right-octant case, and checks the square-root local limit. It gives 16,598 successful numerical comparisons. The universal facet theorem follows analytically from the proof, not from finite sampling. In particular, the counting identity and the spherical normal-fan area identity have no computational assumptions.

## Relationship to prior work
Li, Wang and Yu (2026, first posted November 6) show that a fixed upper dihedral bound \(\pi/2+\delta\) alone allows arbitrarily many facets. Their explicit simple-polytope construction has no uniform positive lower-angle restriction of the type imposed here. The present inequality gives a necessary *small-angle compensation* in every such unbounded sequence of simple polytopes, independent of that construction. Coxeter's classical nonobtuse classification applies at zero upper excess; it does not itself provide this explicit two-sided bound at positive upper excess. Gromov (2022/2024) provides geometric context on dihedral-angle restrictions but no matching finite-facet statement was identified from available material. L'Huilier's identity and the normal-fan area theorem are standard inputs, not claimed as discoveries.

## Limitations
This bound is not asserted to be the optimal possible facet count, and \(2\delta\) is a threshold for the present local-triangle mechanism, not a proven sharp universal lower-angle threshold for unbounded families. The result needs simplicity, three-dimensional Euclidean convexity, and strict \(\alpha>2\delta\). No claim is made about uniqueness, number of realizations, or general nonsimple polytopes. Historical priority remains provisional against unindexed angular-packing arguments.

## References
1. Z. Li, J. Wang, J. Yu, *Infinitely many convex polytopes with dihedral angles bounded above by* \(\pi/2+\delta\), arXiv:2611.09021v1 (2026-11-06), https://arxiv.org/html/2611.09021v1 .
2. H. S. M. Coxeter, *Discrete groups generated by reflections*, Ann. of Math. **35** (1934), 588–621; cited and applied by Li–Wang–Yu.
3. M. Gromov, *Convex Polytopes, Dihedral Angles, Mean Curvature and Scalar Curvature*, arXiv:2207.13346 (2022), https://arxiv.org/abs/2207.13346 .
4. E. W. Weisstein, *L'Huilier's Theorem*, MathWorld, https://mathworld.wolfram.com/LHuiliersTheorem.html .
