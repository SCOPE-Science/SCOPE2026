# Two sharp brightness transitions and an exact anisotropy plateau in cube–octahedron intersections

## Finding
For every real \(0<t<1\), let
\[
K_t=[-1,1]^3\cap\{z\in\mathbb R^3:\|z\|_1\le1+t\},
\qquad b_t(u)=\operatorname{area}_2(\operatorname{proj}_{u^\perp}K_t),\quad \|u\|_2=1.
\]
Set
\[
p=2t^2,\quad q=\frac{1+2t-2t^2}{2},\quad
\alpha=\frac{1+\sqrt7}{6},\quad
\beta=\frac{1+\sqrt{3+\sqrt2}}{2+\sqrt2}.
\]
There are **two distinct sharp orientation transitions** at \(\alpha\approx0.607625218511\) and \(\beta\approx0.908262747179\). The complete minimum and maximum projected areas are
\[
\boxed{\min_{\|u\|_2=1}b_t(u)
=\min\{p+4q,\ \sqrt2(p+2q)\}},
\qquad
\boxed{\max_{\|u\|_2=1}b_t(u)
=\max\{\sqrt{(p+4q)^2+2p^2},\ \sqrt3(p+2q)\}}.
\]
Every minimizing direction is a signed coordinate permutation of \((1,1,0)/\sqrt2\) when \(0<t<\beta\), and a signed coordinate axis when \(\beta<t<1\); at \(t=\beta\) both orbits, and no others, minimize. Every maximizing direction is a signed permutation of
\[
\frac{(p+4q,p,p)}{\sqrt{(p+4q)^2+2p^2}}
\]
when \(0<t<\alpha\), and a body diagonal \((\pm1,\pm1,\pm1)/\sqrt3\) when \(\alpha<t<1\); at \(t=\alpha\) both orbits, and no others, maximize.

The resulting *brightness anisotropy* is exactly constant on the nondegenerate closed interval \([\alpha,\beta]\):
\[
\boxed{\frac{\max b_t}{\min b_t}=\sqrt{\frac32}}.
\]
The unique member whose fourteen facets all have equal area is at
\[
t_\mathrm{eq}=\frac{\sqrt3+\sqrt{9+4\sqrt3}}{4+2\sqrt3}
=0.766745472646\ldots\in(\alpha,\beta).
\]
Its fourteen outward unit facet normals (six axes and eight cube diagonals) constitute a spherical \(3\)-design. After normalizing total surface area to \(4\pi\), it is precisely the centered equal-facet-area Minkowski polytope of this design. Its minimum and maximum brightness are attained at the face-diagonal and body-diagonal normal orbits, respectively, with the same exact anisotropy ratio \(\sqrt{3/2}\).

## Assumptions and scope
All quantities are ordinary Euclidean ones in \(\mathbb R^3\). A viewing direction \(u\) is a unit vector, and opposite vectors represent the same projection plane; the equality classifications above list oriented unit vectors. The open parameter interval \(0<t<1\) ensures all fourteen facets are nondegenerate (six square faces, eight hexagonal faces), and all \(24\) vertices are the signed permutations of \((1,t,0)\). No claim is made for the other combinatorial regime \(2<1+t<3\) or the degenerate endpoint polytopes. The parameter thresholds are unrelated to changes in the number of facets: all three regimes have the same face lattice.

## Proof
**1. Facet areas and exact directional brightness.** Each axial facet, say \(z_1=1\), has the planar diamond \(|z_2|+|z_3|\le t\), with area \(p=2t^2\). A facet with normal \((1,1,1)/\sqrt3\) lies in the positive octant and is obtained from the triangle \(z_1+z_2+z_3=1+t\), \(z_i\ge0\), by excluding three disjoint triangles cut off by \(z_i>1\). Its area is
\[
H=\frac{\sqrt3}{2}[(1+t)^2-3t^2]=\sqrt3 q.
\]
Cauchy's projection formula applied to the six axial and eight diagonal facets yields, for every unit \(u=(u_1,u_2,u_3)\),
\[
b_t(u)=p\sum_{i=1}^3|u_i|+\frac{q}{2}\sum_{\varepsilon\in\{-1,1\}^3}|\varepsilon\cdot u|.
\]
Let \(x\ge y\ge z\ge0\) be the absolute coordinates of \(u\). The eight-sign sum is \(8x\) when \(x\ge y+z\), and \(4(x+y+z)\) otherwise. Thus
\[
\boxed{b_t(u)=\begin{cases}
(p+4q)x+p(y+z),&x\ge y+z,\\
(p+2q)(x+y+z),&x\le y+z.
\end{cases}}
\]
The two expressions coincide on their common boundary. Notice the simplification \(p+2q=1+2t\).

**2. Sharp maximum and all equality directions.** In the chamber \(x\le y+z\), Cauchy–Schwarz gives \(b_t(u)\le\sqrt3(p+2q)\), with equality exactly at \(x=y=z=1/\sqrt3\). In the chamber \(x\ge y+z\), Cauchy–Schwarz gives
\[
b_t(u)\le\sqrt{(p+4q)^2+2p^2},
\]
with equality only when \((x,y,z)\) is proportional to \((p+4q,p,p)\). This vector lies in the first chamber whenever \(q\ge p/4\); in particular this holds for \(q\ge p\). The squared difference between the two displayed candidate maxima equals \(4q(q-p)\). Hence the first-chamber maximizer is global exactly when \(q>p\), the body diagonal is global when \(q<p\), and both are global at equality; there are no other maximizers because both Cauchy–Schwarz equality conditions are strict outside their stated rays. Solving \(q=p\) gives \(t=\alpha\).

**3. Sharp minimum and all equality directions.** In the second chamber, write \(S=x+y+z\). The chamber hypothesis implies each coordinate is at most \(S/2\), so \(1=x^2+y^2+z^2\le S^2/2\). Thus \(b_t(u)\ge\sqrt2(p+2q)\), with equality exactly at signed permutations of \((1,1,0)/\sqrt2\). In the first chamber put \(w=y+z\le x\). Since \(x^2+y^2+z^2\le x^2+w^2\),
\[
\frac{b_t(u)}{\|u\|_2}\ge
\frac{(p+4q)x+pw}{\sqrt{x^2+w^2}}.
\]
For \(s=w/x\in[0,1]\), the derivative of \(((p+4q)+ps)/\sqrt{1+s^2}\) has the sign of \(p-(p+4q)s\), so the minimum on the interval occurs at an endpoint. The two endpoint values are \(p+4q\) and \(\sqrt2(p+2q)\). Equality at \(s=0\) occurs only on a coordinate axis, while equality at \(s=1\) also requires \(yz=0\), giving precisely the face-diagonal directions. The equality analysis rules out mixed families at the tie. The relation \(p+4q=\sqrt2(p+2q)\) is equivalent to \(q/p=\sqrt2/4\) and has unique solution \(t=\beta\).

**4. Plateau and the equal-area design.** The ratio \(q/p=1/(4t^2)+1/(2t)-1/2\) decreases strictly. For \(\alpha\le t\le\beta\), Step 2 gives maximal brightness \(\sqrt3(p+2q)\) and Step 3 minimal brightness \(\sqrt2(p+2q)\), yielding \(\sqrt{3/2}\) with no approximation. Equality of the six axial facet areas and eight diagonal facet areas means \(p=\sqrt3q\), equivalent to the unique root \(t=t_\mathrm{eq}\) displayed in the finding. Since \(\sqrt2/4<1/\sqrt3<1\), strict monotonicity gives \(\alpha<t_\mathrm{eq}<\beta\). The six unit coordinate axes form a spherical \(3\)-design, as do the eight normalized cube corners: both have zero odd moments and covariance \(I/3\). Their equally weighted union is therefore a spherical \(3\)-design. The equal-area property and Minkowski existence/uniqueness establish the asserted identification up to scale and translation; symmetry fixes the centered representative.

## Verification
The independent `verify_brightness.py` constructs all \(24\) polytope vertices and directly projects them to \(3344\) orthogonal planes using two-dimensional convex-hull area, comparing each numerical result against the directional formula and both proposed sharp bounds. It checks points below, at, between and above both transition parameters, includes all candidate equality directions, and independently recovers the regular truncated-octahedron endpoint values after rescaling by a factor two. All checks pass. The analytic argument above, rather than the finite computer tests, proves the continuum statements.

To reproduce in an environment with Python 3, NumPy and SciPy, run `python verify_brightness.py`.

## Relationship to prior work
Cauchy's projection formula is classical and not claimed as new. Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability* (arXiv:2609.26202v1, first public 2026-08-10), establishes a broad random-brightness framework and explicitly addresses the **regular truncated octahedron**, corresponding here to \(t=1/2\). The published record *Sharp shadow-area extrema and projection-body volume of the regular truncated octahedron* determines exactly the 12 minimizing and 24 maximizing directions for that single regular member. At \(t=1/2\), the present formula specializes to those same endpoints; neither the single-member statement nor its known support-function formula gives the global thresholds or constant-ratio interval without additional analysis.

Congpei An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity* (arXiv:2608.11570v1, 2026-08-12), proves general equal-facet-area realizations and general projection-body estimates. Its full text gives Cauchy's formula and design correspondence, not an exact all-parameter brightness extremum classification for this 14-normal family. The published *Exact random-silhouette law along the cube–octahedron interpolation* classifies **numbers of projected vertices**, a different functional from their projected areas; that paper does not determine the present extrema. Earlier truncated-cube models in the packing literature concern phase behavior and supply the known geometric family, not these brightness claims.

## Limitations
The theorem covers exactly the open interval \(0<t<1\) in the specified Euclidean normalization and determines the extremes, not the full random-brightness distribution. An inaccessible full text for the wide-ranging Abas manuscript remains a source-priority risk; its accessible abstract and the full published regular-member result do not establish broader coverage. No claim of absolute historical novelty or independent mathematical auditing is made. No conclusion about facet-number changes is intended, because none occur in the stated interval.

## References
1. Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202v1 (first public 2026-08-10). https://arxiv.org/abs/2609.26202
2. Congpei An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, arXiv:2608.11570v1 (first public 2026-08-12), especially Theorems 3.1 and 6.1 and Cauchy's formula (15). https://arxiv.org/abs/2608.11570
3. *Sharp shadow-area extrema and projection-body volume of the regular truncated octahedron*, published mathematical record (2026-11-08; identifier `ef8f8ba8bf3f`), especially its Finding and Proof §§1–3.
4. *Exact random-silhouette law along the cube–octahedron interpolation*, published mathematical record (2026-10-18; identifier `23b7c8205147`), especially its Finding and Proof §§1–2.
5. Gantapara, de Graaf, van Roij, and Dijkstra, *Phase Behavior of a Family of Truncated Hard Cubes*, arXiv:1412.2597v1 (2014), for an equivalent geometric interpolation in a distinct applied context.
