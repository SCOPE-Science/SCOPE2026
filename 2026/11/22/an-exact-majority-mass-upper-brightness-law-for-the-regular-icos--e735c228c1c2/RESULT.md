# An exact majority-mass upper brightness law for the regular icosahedron

## Finding
Let \(I\subset\mathbb R^3\) be the regular icosahedron of edge length \(2\), and let \(U\) be Haar-uniform on the unit sphere. Write \(B(U)\) for the two-dimensional area of the orthogonal projection of \(I\) onto \(U^\perp\). Define
\[
 B_+=\sqrt{42+18\sqrt5},\qquad B_1=\sqrt{42+14\sqrt5}.
\]
For **every** real \(t\) in the closed interval \([B_1,B_+]\),
\[
\boxed{\Pr\bigl(B(U)\ge t\bigr)=10\left(1-\frac{t}{B_+}\right).}
\]
Consequently the brightness distribution has the **exact constant density** \(10/B_+\) throughout the open interval \((B_1,B_+)\). This interval contains exactly \(10(1-B_1/B_+)\approx0.55937488166\) of the full probability mass, i.e., more than half of all viewing directions.

The twenty outward face normals are precisely the twenty maximizers of brightness. For \(B_1<t<B_+\), the high-brightness event is a disjoint union of twenty congruent spherical caps centered at those normals, each of angular radius \(\arccos(t/B_+)\). All these caps, modulo a null set, produce **hexagonal** orthogonal silhouettes. In particular, given \(B(U)\ge t\) in this band, the maximizing face label is exactly uniform among the twenty faces, and conditional orientation is spherical-area uniform within its selected cap. The cap description and law also apply at \(t=B_1\) up to possible isolated boundary directions.

## Assumptions and scope
Put \(\varphi=(1+\sqrt5)/2\). The vertices are precisely the twelve vectors
\[
 (0,\pm1,\pm\varphi),\quad(\pm1,\pm\varphi,0),\quad(\pm\varphi,0,\pm1).
\]
These form a regular icosahedron with thirty edges of length \(2\), twenty congruent triangular faces each of area \(\sqrt3\), and ten antipodal pairs of face normals. The orientation measure is normalized spherical area on \(S^2\), not uniform sampling of projection polygons or incident affine planes. The theorem is invariant under rotations, and a uniform similarity scaling multiplies both threshold values by the square of the similarity factor. The statement fixes edge length \(2\) to make the coefficients explicit.

## Proof
**1. Cauchy brightness as a finite spherical maximum.** For a convex polytope with outward unit face normals \(n_f\) and face areas \(a_f\), Cauchy's projection-area identity is
\[
 B(u)=\frac12\sum_f a_f\,|n_f\cdot u|,\qquad u\in S^2.
\]
For the displayed icosahedron, choose one unnormalized face centroid \(c_j\) from each of the ten antipodal pairs. Each has the same squared length
\[
 L^2=6+9\varphi,
\]
and the corresponding unit face normals are \(\pm c_j/L\). Since every face area is \(\sqrt3\),
\[
 B(u)=\frac{\sqrt3}{L}\sum_{j=1}^{10}|c_j\cdot u|
 =\frac{\sqrt3}{L}\max_{\sigma\in\{-1,1\}^{10}}u\cdot v_\sigma,
 \qquad v_\sigma=\sum_{j=1}^{10}\sigma_jc_j.
\]
The representative centroids are generated directly from triples of vertices supporting the twenty triangular facets; the standalone checker reconstructs them by exact determinant and supporting-plane tests, rather than assuming a floating-point face table.

**2. Exhaustive exact norm classification.** All vertices, centroids and sign sums lie in the ordered quadratic ring \(\mathbb Z[\varphi]\). The checker enumerates the \(\binom{12}{3}=220\) vertex triples, accepts exactly twenty supporting face triples, selects ten antipodal centroid representatives, then exhausts all \(2^{10}=1024\) sign vectors. For clarity the **two largest** squared sign-sum norms and their complete multiplicities are
\[
\begin{array}{c|c|c}
\text{rank}&\|v_\sigma\|^2&\text{number of sign patterns}\\\hline
1&156+252\varphi&20\\
2&140+224\varphi&60.
\end{array}
\]
The remaining 944 patterns occupy sixteen strictly smaller norm levels. The supplied exact certificate specifies and verifies the multiplicity of **each** of all eighteen levels (their counts sum to 1024), so the assertion that no intervening norm exists is exhaustive, not inferred from sampling. Moreover, each of the twenty maximal sign sums is a positive scalar multiple of a distinct outward face normal, verified by exact cross products; conversely every face normal occurs.

Since \(B(u)\) is the maximum of these finite linear forms, Cauchy–Schwarz yields \(B_+=\sqrt{3(156+252\varphi)/(6+9\varphi)}\), and the second-largest sign-sum radius yields \(B_1=\sqrt{3(140+224\varphi)/(6+9\varphi)}\). Elementary simplification using \(\varphi^2=\varphi+1\) gives exactly \(B_+^2=42+18\sqrt5\) and \(B_1^2=42+14\sqrt5\). For \(t>B_1\), no nonmaximal sign vector can satisfy \(u\cdot v_\sigma\ge tL/\sqrt3\). Thus the event \(B(u)\ge t\) is precisely the union of the twenty maximal-vector caps. At \(t=B_1\), other sign vectors can contribute only isolated supporting points of spherical area zero.

**3. The twenty caps do not overlap.** The largest dot product of distinct face-normal unit vectors is \(\sqrt5/3\); equivalently the smallest angular separation is \(\arccos(\sqrt5/3)\). This follows by exact pairwise dot products of the twenty centroids. Cap radii are \(\theta(t)=\arccos(t/B_+)\). The strict inequality
\[
 \frac{B_1^2}{B_+^2}>\frac{1+\sqrt5/3}{2}
\]
shows \(2\theta(B_1)<\arccos(\sqrt5/3)\), proving pairwise cap disjointness throughout the stated band. The checker verifies the inequality without floating-point arithmetic in \(\mathbb Q(\varphi)\).

Each spherical cap of angular radius \(\theta(t)\) has area \(2\pi(1-\cos\theta(t))=2\pi(1-t/B_+)\). Adding twenty disjoint cap areas and dividing by \(4\pi\) gives \(\Pr(B(U)\ge t)=10(1-t/B_+)\), including endpoints by continuity. Differentiation on the open band gives the constant density and the exact majority-mass fraction. Conditional uniformity of the cap labels and the points within each cap follows from spherical-area uniformity and congruence.

**4. Upper-brightness forces six-sided shadows.** The absolute scalar product between any two icosahedral face-normal unit vectors is at least \(1/3\). Hence the spherical distance from a maximizing face normal to every face-normal great circle is at least \(\arcsin(1/3)\). The additional strict comparison
\[
 \frac{B_1^2}{B_+^2}>\frac89
\]
ensures \(\theta(B_1)<\arcsin(1/3)\). Every cap therefore stays inside one cell of the great-circle arrangement where the signs of all twenty face-normal products are constant. For a generic viewing direction, an original edge is silhouetted exactly when its two incident face-normal dot products have opposite signs. Direct exact enumeration of the thirty edge-adjacent face pairs at each maximal direction gives precisely six sign-changing pairs. The silhouette thus remains hexagonal throughout all twenty high-brightness caps, except on null boundaries.

## Verification
Run `python3 verify_icosa_brightness.py` from the directory containing this document. It needs Python 3's standard library only. It constructs the twelve golden vertices; exactly enumerates all supporting faces and thirty adjacent-face pairs; checks all ten antipodal centroid generators; enumerates all 1024 sign patterns across all eighteen norm levels; proves the two leading levels, their multiplicities, and maximizing directions; checks the cap-separation and sign-chamber inequalities exactly; and verifies six silhouetted edges in each maximum chamber. These are finite exhaustive exact-arithmetic computations, used alongside the analytic Cauchy and spherical-area arguments.

A separately labelled diagnostic inside the script samples 65,536 deterministic spherical directions for three thresholds and compares their exceedance proportions with the exact law, with absolute discrepancy below 0.001. Those samples are not an infinite or exhaustive proof. The exact finite certificate and cap geometry supply the proof for every threshold in the interval.

## Relationship to prior work
The brightness function and Cauchy's polytope projection formula are classical; their geometric-tomography motivation and related lightness functions are described by Campi, Gardner, Gronchi and Kiderlen (2012), which carries primary classifications 52A20 and 52A40. Finch (2012) calculates random projections of simpler regular polyhedra, including the cube, tetrahedron and octahedron; those formulas do not state this icosahedral upper-band law.

Published exact icosahedral results on the **unweighted hexagon/octal/decagon shadow probabilities** and the **three first area-weighted silhouette moments** supply adjacent but weaker information: even together with the unconditional first two brightness moments, they do not determine a distribution on an interval. The first area-weighted study explicitly leaves complete silhouette-conditioned brightness laws outside its claim. An exact high-tail law for icosahedral **shadow diameters** studies a different invariant. Related exact high-brightness laws for the regular dodecahedron concern the dual solid's different facet normal configuration; those values do not imply the icosahedral twenty-cap threshold without its separate exact ten-generator spectrum.

The claim here is specifically the explicit twenty-cap band extending over more than half of all viewing directions, its constant brightness density, and its rigorous hexagonal-silhouette marking. A general coarea-density method for random polyhedral brightness (Abas, 2026) may give an alternative derivation; its complete text was not accessible during this comparison, and no historical-priority guarantee is asserted. Such methods and Cauchy's identity are not claimed as new.

## Limitations
This is a sharp **upper-band** distribution for a fixed regular icosahedron, not the complete brightness distribution below \(B_1\), not a new formula for its conditional moments outside that band, and not a uniform law for arbitrary polyhedra or perturbed icosahedra. The statement describes geometric orthogonal projection area, not the projected polygon's diameter or support width. The historical comparison cannot exclude uncatalogued exact prior formulas. Independent mathematical validation has not been performed.

## References
1. S. Campi, R. J. Gardner, P. Gronchi, M. Kiderlen, *Lightness functions*, Advances in Mathematics **231** (2012), 3118–3146, DOI:10.1016/j.aim.2012.08.015; first verifiable public source date 2012-12-20; primary MSC 52A20, 52A40. https://doi.org/10.1016/j.aim.2012.08.015
2. S. R. Finch, *Planar Projections and Second Intrinsic Volume* (2012), arXiv:1203.2464. https://arxiv.org/abs/1203.2464
3. *Exact hexagon–octagon–decagon law for icosahedral shadows and dual dodecahedral sections* (2026), published research record: https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-hexagon-octagon-decagon-law-for-icosahedral-shadows-and-du--3db14789bb66
4. *Exact area-weighted silhouette law and reverse area–complexity ordering for the regular icosahedron* (2026), published research record: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-area-weighted-silhouette-law-and-reverse-area-complexity-o--43964e3c07f3
5. *Exact orientation-variance spectrum of Platonic shadow areas* (2026), published research record: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-orientation-variance-spectrum-of-platonic-shadow-areas--76ed33fc3859
6. *An exact upper-tail law for random icosahedral shadow diameters* (2026), published research record: https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-an-exact-upper-tail-law-for-random-icosahedral-shadow-diameters--4bb075dff7ea
7. S. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability* (2026), arXiv:2609.26202. https://arxiv.org/abs/2609.26202
