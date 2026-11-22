# Sharp two-endpoint brightness laws and silhouette selection for the regular dodecahedron

## Finding
Let \(\varphi=(1+\sqrt5)/2\) and \(R=\sqrt{\varphi+2}\). Let \(D\) be a regular Euclidean dodecahedron and let \(F\) denote the area of one of its twelve congruent pentagonal faces. For a sphere-uniform unit viewing normal \(U\), define normalized orthographic shadow area
\[
B(U)=\frac{\operatorname{area}(D\mid U^\perp)}{F}.
\]
Put
\[
 b_-=2\sqrt{1+\frac2{\sqrt5}},\qquad b_+=1+\sqrt5,
 \qquad \Delta=b_+-\sqrt{6+\frac6{\sqrt5}}.
\]
The exact range is \([b_-,b_+]\). There are precisely 30 oriented minimizers, on axes through midpoints of opposite dodecahedral edges, and precisely 12 oriented maximizers, on axes normal to the pentagonal faces. The **new probability statements** are:
\[
 \boxed{\Pr\{B\le b_-+\varepsilon\}
 =\frac{15\sqrt5}{2\pi}\varepsilon^2
 +\frac{5b_-(\varphi+2)^2}{4\pi}
       (\varphi^{-1}+\varphi^{-3})\varepsilon^3
 +O(\varepsilon^4)\quad(\varepsilon\downarrow0).}
\]
For the other endpoint there is an **exact**, not merely asymptotic, law:
\[
 \boxed{\Pr\{B\ge b_+-\varepsilon\}
 =\frac6{b_+}\varepsilon\quad(0\le\varepsilon<\Delta).}
\]
Numerically, \(b_-=2.752763840942347\ldots\), \(b_+=3.236067977499790\ldots\), \(\Delta=0.289327138369252\ldots\); the lower quadratic and cubic coefficients are \(5.338219075628829\ldots\) and \(12.245713705349765\ldots\).

There are two angular conditional limits. Around any minimizer, identify the tangent plane using two orthonormal directions as in the proof. Conditioned on \(B\le b_-+\varepsilon\), the tangent offsets divided by \(\varepsilon\) converge to uniform Lebesgue probability on
\[
 \mathcal R=\left[-\frac R2,\frac R2\right]
 \times\left[-\frac R{2\varphi},\frac R{2\varphi}\right].
\]
The thirty minimizing directions have equal limiting weights \(1/30\). The near-minimum shadow is asymptotically 10-sided or 12-sided with probability \(1/2\) each. Conditioned on \(B\ge b_+-\varepsilon\), all sufficiently small-deficit shadows are 10-sided, the twelve maximizing directions have equal weights \(1/12\), and after normalizing transverse angular offsets by \(\sqrt\varepsilon\), each conditional limit is uniform on the Euclidean disk of radius \(\sqrt{2/b_+}\).

The new contribution consists of the two probability laws, the cubic lower-tail correction, the conditional orientation limits and the silhouette-type selection. The facet-normal formula, its previously calculated mean and type-conditioned moments, and the underlying spherical chamber tessellation are credited prior ingredients; the endpoint values are stated here to identify the thresholds rather than claimed as historically new extrema.

## Assumptions and scope
Normalize the dodecahedron as
\[
 D=\{x\in\mathbb R^3:|x\cdot s_i|\le1,\ i=1,\ldots,6\},
\]
where
\[
\begin{split}
 s_1&=(0,1,\varphi),&s_2&=(0,1,-\varphi),\\
 s_3&=(1,\varphi,0),&s_4&=(1,-\varphi,0),\\
 s_5&=(\varphi,0,1),&s_6&=(\varphi,0,-1).
\end{split}
\]
All \(s_i\) have Euclidean norm \(R\), and the twelve planes \(x\cdot s_i=\pm1\) cut out the regular dodecahedron. Every direction is an *oriented* point of \(S^2\); projection and silhouette count are unchanged on reversing orientation, but the count of minimizers or maximizers on the sphere includes both antipodes. Uniform means normalized spherical area. The shadow is a generic convex polygon away from a finite union of great circles; its 10-versus-12 vertex count is understood almost surely. Statements are invariant under similarity of \(D\) owing to normalization by \(F\).

## Proof
**1. Exact brightness function.** For a convex polyhedron Cauchy's facet projection identity is half the sum of projected facet areas. Pairing each opposite pair of equal-area pentagonal facets gives
\[
 B(u)=\sum_{i=1}^6\frac{|s_i\cdot u|}{R},\qquad |u|=1.
\tag{1}
\]
In particular, for a sign vector \(\sigma\in\{\pm1\}^6\), put \(v_\sigma=R^{-1}\sum_i\sigma_i s_i\). Then \(B(u)=\max_\sigma v_\sigma\cdot u\). Exactly enumerating the 64 sign vectors in the quadratic field \(\mathbb Q(\sqrt5)\) gives the complete squared-length table
\[
\begin{array}{c|c}
 |v_\sigma|^2&\text{multiplicity}\\\hline
 6-2\sqrt5&12\\
 6-6/\sqrt5&20\\
 6+6/\sqrt5&20\\
 6+2\sqrt5&12
\end{array}.
\tag{2}
\]
The 12 largest vectors are \(b_+s_i/R\) and their antipodes, one for each face normal. Consequently \(\max_{S^2}B=b_+\), attained at exactly those 12 directions. A reproducible exact rational-quadratic-field enumeration of (2) is in `verify_dodeca_brightness.py`; (2) can also be checked by expanding the six displayed coordinate vectors using \(\varphi^2=\varphi+1\).

**2. Global minimum and its thirty directions.** The six great circles \(s_i\cdot u=0\) divide the sphere into geodesically convex sign cells. In the interior of each cell, \(B(u)=v_\sigma\cdot u>0\). Along a great-circle arc contained in a cell, \(B\) has second derivative \(-B<0\); the same is true along each cell edge. It follows by descending along an arc to an edge, then along the edge, that no global minimum lies away from a cell vertex. The vertices of the arrangement are the antipodes of \(s_i\times s_j\), \(i<j\). Their 15 axes are distinct (there is no triple crossing). Direct exact calculation yields
\[
 B\!\left(\frac{s_i\times s_j}{|s_i\times s_j|}\right)^2
 =4+\frac8{\sqrt5}=b_-^2
 \quad\text{for all }1\le i<j\le6.
\tag{3}
\]
The symmetric icosahedral group also acts transitively on these 15 axes: after fixing one opposite-vertex axis its fivefold rotations permute the other five axes. Equation (3), which follows already from \(i=1,j=2\) and this transitivity, is independently checked for all 15 pairs in exact arithmetic. Every minimum is therefore one of the 30 oriented crossings. In this realization these are the opposite-edge-center viewing axes.

**3. Exact upper-tail interval.** The second-largest distinct norm in (2) is \(q_+=\sqrt{6+6/\sqrt5}\). For \(0\le\varepsilon<b_+-q_+=\Delta\), the inequality \(B(u)\ge b_+-\varepsilon\) can be attained only by one of the 12 largest sign vectors; it is exactly the union of the 12 spherical caps
\[
 u\cdot n\ge1-\varepsilon/b_+,
 \qquad n\in\{\pm s_i/R\}_{i=1}^6.
\]
These caps are disjoint throughout this interval: their angular radii are at most \(\arccos(q_+/b_+)\), less than half the minimal separation \(\arccos(1/\sqrt5)\) of the 12 face normals. Each has area \(2\pi\varepsilon/b_+\), giving \(12(2\pi\varepsilon/b_+)/(4\pi)=6\varepsilon/b_+\). Inside these caps each normal is strictly within its 10-sided sign chamber (the angular distance from the normal to its nearest great circle is \(\arcsin(1/\sqrt5)\), larger than the cap radius). Each cap is rotationally uniform, and its small-angle scaled tangent-plane disk has radius \(\sqrt{2/b_+}\). This proves the exact upper law, the conditional disk limit and the bright-silhouette statement.

**4. Two lower-tail coefficients.** It suffices by symmetry to work at the minimum \(u_0=(1,0,0)\). Write nearby points as \(u=(\sqrt{1-y^2-z^2},y,z)\). Four dot products in (1) have positive fixed signs, while the other two are \(y+\varphi z\) and \(y-\varphi z\). For small \(y,z\) the following identity is exact:
\[
 B(u)=b_-\sqrt{1-y^2-z^2}
       +c\max\{|y|,\varphi|z|\},\qquad c=\frac2R.
\tag{4}
\]
Thus, uniformly near zero,
\[
 B(u)-b_-=c\max\{|y|,\varphi|z|\}
       -\frac{b_-}{2}(y^2+z^2)+O((y^2+z^2)^2).
\tag{5}
\]
The first-order sublevel set, rescaled by \(1/\varepsilon\), is the rectangle \(\mathcal R\). Its area is \(R^2/\varphi=\sqrt5\), since \((\varphi+2)/\varphi=\sqrt5\). There are 30 disjoint minimizing neighborhoods, and the sphere area is \(4\pi\). The quadratic probability coefficient is therefore \(30\sqrt5/(4\pi)=15\sqrt5/(2\pi)\).

For the cubic correction put \(Y=\varepsilon/c\), \(Z=\varepsilon/(c\varphi)\) in the positive \((y,z)\)-quadrant. Its bounding positive coordinate branches from (4) have uniform expansions
\[
 y_{\max}(z)=Y+\frac{b_-}{2c}(Y^2+z^2)+O(\varepsilon^3),\qquad
 z_{\max}(y)=Z+\frac{b_-}{2c\varphi}(y^2+Z^2)+O(\varepsilon^3).
\]
Integrating the two outward boundary strips (their mutual overlap is \(O(\varepsilon^4)\)), the area of this quadrant is
\[
 YZ+\frac{2b_-}{3c^4}(\varphi^{-1}+\varphi^{-3})\varepsilon^3
 +O(\varepsilon^4).
\tag{6}
\]
The spherical area element is \((1-y^2-z^2)^{-1/2}dy\,dz=(1+O(\varepsilon^2))dy\,dz\), so it affects only the fourth order and beyond. Multiplying (6) by 4 quadrants and 30 minima and dividing by \(4\pi\) gives the stated cubic coefficient \(20b_- (\varphi^{-1}+\varphi^{-3})/(\pi c^4)\), equivalently \(5b_-(\varphi+2)^2(\varphi^{-1}+\varphi^{-3})/(4\pi)\).

**5. Lower conditional angles and silhouette type.** Formula (5) gives uniform convergence of rescaled sublevel indicators away from the rectangle boundary; the area element also converges uniformly. Consequently the conditional rescaled offsets converge weakly to the uniform rectangle law, and the 30 minimizing neighborhoods carry equal limiting probability \(1/30\). The two lines \(y=\pm\varphi z\) pass through the rectangle's opposite corner pairs, dividing it into four equal-area triangles. By the exact facet-normal silhouette-edge count, the horizontal sectors \(|y|>\varphi|z|\) produce 12 vertices and the vertical sectors \(|y|<\varphi|z|\) produce 10, up to null boundaries. Hence each type has conditional limiting probability \(1/2\). No assertion is made of independence of the count and the full tangent-plane offsets.

## Verification
From the package directory run `python3 verify_dodeca_brightness.py` with Python 3 and no nonstandard libraries. The script uses exact rational arithmetic in \(\mathbb Q(\varphi)\) to enumerate all 64 sign vectors and all 15 cross axes, verify every squared-norm multiplicity in (2), all equalities in (3), the 15 distinct axes, and the axial nature of each maximizer. It checks the angular cap separation and tests 2,900 independent deterministic orientations/local representations, four silhouette sectors, and deterministic one-dimensional spherical integrations at three small deficit values against the quadratic-plus-cubic expansion. These numerical diagnostics are supplemental: the continuum statements follow from (1)--(6), exact finite exhaustive tables and rigorous local expansion.

## Relationship to prior work
Finch's 12 March 2012 random-planar-projection study establishes the stochastic shadow viewpoint and evaluates moments for the cube, tetrahedron and octahedron, not this dodecahedral endpoint distribution. Cauchy's projection formula and the six-icosahedral-normal representation (1) are classical and are not claimed to be novel. The published exact regular-dodecahedron type-weighted area moments and its full icosahedral chamber calculation supply stronger prior input: they already identify the six-normal brightness expression, 20 triangular and 12 pentagonal sign chambers, and the common brightness value at their 30 vertices. In particular, the candidate extrema can be extracted from those data; no historical novelty is claimed for their values alone. Those papers do not establish the two sharp endpoint probability laws (including the exact finite upper interval and cubic lower correction) or the conditional rectangle/disk limits and rare-silhouette selection. The published Platonic variance spectrum concerns global second moments, which cannot alone determine endpoint CDFs or conditional direction laws. The new endpoint analysis requires the finite sign-norm spectrum, localization and area expansion. This comparison does not prove historical uniqueness.

## Limitations
Only one regular three-dimensional dodecahedron (up to scaling and rotation) and Haar-uniform orthographic normals are covered. The distribution away from the two endpoints is not evaluated. The lower probability expansion is local and asymptotic; the upper probability is exact only on the stated interval. The orientation limits are weak convergence statements, not finite-deficit total-variation bounds. Earlier stereological or projection-body literature may contain equivalent endpoint results not located in accessible full text. These conclusions have not received an independent mathematical audit.

## References
1. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464, first public 12 March 2012, https://arxiv.org/abs/1203.2464.
2. *Conditional projected-area moments of ten- and twelve-vertex regular-dodecahedron silhouettes*, published published-finding corpus record, 18 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-conditional-projected-area-moments-of-ten-and-twelve-vertex-regu--dd8366e1b75c.
3. *Exact orientation-variance spectrum of Platonic shadow areas*, published published-finding corpus record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-orientation-variance-spectrum-of-platonic-shadow-areas--76ed33fc3859.
4. *Exact Haar polygon-type law for central icosahedron sections*, published published-finding corpus record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f.
