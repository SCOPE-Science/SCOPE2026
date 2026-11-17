# Complete orientation law for equilateral triangle containment in rectangles

## Finding

Let \(T\) be an equilateral triangle of circumradius one, with vertices \(v_j=(\cos(2\pi j/3),\sin(2\pi j/3))\), \(j=0,1,2\). For any rectangle of positive horizontal width \(w\) and vertical height \(h\), let \(L_{w,h}(\theta)\) be the greatest \(\lambda\geq0\) for which some translation of \(\lambda R_\theta T\) lies in that rectangle. The orientation \(\Theta\) is uniform on \([0,2\pi)\). Define \(m=\min(w,h)\), \(M=\max(w,h)\), \(S=wh\), and
\[
\mathcal A(w,h)=\begin{cases}
8wh-2\sqrt3(w^2+h^2),& M/m<2/\sqrt3,\\
(2/\sqrt3)m^2,& M/m\ge2/\sqrt3.
\end{cases}
\]
Set
\[
R(w,h)=\begin{cases}
\dfrac2{\sqrt3}\sqrt{w^2+h^2-\sqrt3wh},&M/m<2/\sqrt3,\\
\dfrac23m,&M/m\ge2/\sqrt3.
\end{cases}
\]
Then \(R(w,h)=\max_\theta L_{w,h}(\theta)\), and the *entire exact survival function* is, for \(0<u<R(w,h)\),
\[
\Pr\{L_{w,h}(\Theta)\ge u\}=1-\frac6\pi\left[\arccos\!\left(\min\!\left\{1,\frac{w}{\sqrt3u}\right\}\right)+\arccos\!\left(\min\!\left\{1,\frac{h}{\sqrt3u}\right\}\right)\right].
\]
For \(u\le0\) the survival probability is one; for \(u\ge R(w,h)\) it is zero (the endpoint has angular measure zero). In particular,
\[
\mathbb E[L_{w,h}(\Theta)^2]=\frac{\mathcal A(w,h)}\pi.
\]
At fixed rectangle area \(S\), the square uniquely maximizes this angular mean square, with sharp value \((8-4\sqrt3)S/\pi\). By contrast, \(\max_\theta L_{w,h}(\theta)^2\), when further maximized over all rectangles of fixed area, has sharp value \(2\sqrt3S/9\), attained exactly at the two aspect ratios \(h/w=2/\sqrt3\) and \(h/w=\sqrt3/2\), *not* at the square. The feasible similarity-factor polygon is a cyclic dodecagon for \(\sqrt3/2<h/w<2/\sqrt3\), degenerating to a regular hexagon at or outside those thresholds. The square case gives a regular dodecagon.

## Assumptions and scope

Every \(w,h\) is a positive real number. All copies may be translated arbitrarily, rotated in the plane, and uniformly scaled; reflection is unnecessary because the source is equilateral. The original triangle is normalized by circumradius, so any change of source circumradius multiplies all allowable scales by its reciprocal. The angular law uses Lebesgue-uniform orientation, not a distribution on physical translations. Rectangles include their boundaries. Coincident threshold cases are covered by the non-strict branch formulas, and the endpoint survival values refer to probabilities of positive-measure orientation sets.

## Proof

**1. Eliminate translation.** For any finite point set \(V\), a translate of \(\lambda R_\theta V\) fits in an axis-parallel \(w\)-by-\(h\) rectangle if and only if its horizontal coordinate range is at most \(w\) and its vertical coordinate range is at most \(h\). Necessity is immediate; sufficiency follows by translating the minimum of each projected coordinate to the lower rectangle side. Applying this to the three vertices of \(T\) gives
\[
L_{w,h}(\theta)=\min\left\{\frac{w}{W_T(\theta)},\frac{h}{H_T(\theta)}\right\},
\]
where \(W_T,H_T\) are their two projected spans. Both spans are positive for every angle.

**2. The six-strip representation.** Let \(z=s+it=\lambda e^{i\theta}\). Differences of the three vertices have Euclidean length \(\sqrt3\) and directions separated by \(\pi/3\) modulo sign. The three horizontal range constraints are precisely three strips with normal magnitudes \(\sqrt3\) and angular normal directions \(\pi/6,\pi/2,5\pi/6\) modulo \(\pi\), each of half-width \(w/\sqrt3\). Vertical range constraints are three more strips, rotated by \(\pi/2\), of half-width \(h/\sqrt3\). Consequently the feasible set
\[
F_{w,h}=\{z\in\mathbb C:\ zT\text{ can be translated into the rectangle}\}
\]
is the intersection of two regular hexagons, one of inradius \(w/\sqrt3\), the other of inradius \(h/\sqrt3\), rotated by \(\pi/6\) relative to one another. Its radial function is exactly \(L_{w,h}(\theta)\).

**3. Polygon and extreme radial length.** Assume \(w\le h\); the other case follows by a quarter-turn and swapping \(w,h\). The first hexagon has circumradius \(2w/3\). The second contains the first exactly when its inradius \(h/\sqrt3\) is at least \(2w/3\), equivalently \(h/w\ge2/\sqrt3\). In that case \(F_{w,h}\) is a regular hexagon and its circumradius is \(2w/3\). Otherwise each of the six vertices of the first hexagon is cut by one side of the second; no other incidence changes, and there are twelve vertices. Around the original vertex at \((2w/3,0)\), the cutting line is \(s=h/\sqrt3\), while the two adjacent sides of the first hexagon have equations \(t=\pm\sqrt3(2w/3-s)\). Thus the two new vertices are
\[
\left(\frac h{\sqrt3},\ \pm\left(\frac{2w}{\sqrt3}-h\right)\right).
\]
The other ten are obtained by rotation through integer multiples of \(\pi/3\). All twelve therefore lie on the circle of radius \(\frac2{\sqrt3}\sqrt{w^2+h^2-\sqrt3wh}\). These statements also cover the equal-width case, in which the twelve-gon is regular. At \(h/w=2/\sqrt3\), each truncated edge shrinks to a vertex and the hexagon results. This proves the combinatorial claims and the formula for \(R(w,h)\).

**4. Area and the second moment.** The original \(w\)-hexagon has area \(2w^2/\sqrt3\). In the twelve-vertex regime, each of its six removed triangular corners has altitude \(d=2w/3-h/\sqrt3\) and base length \(2\sqrt3d\); its area is \(\sqrt3d^2\). Hence
\[
\operatorname{area}(F_{w,h})=\frac{2w^2}{\sqrt3}-6\sqrt3\left(\frac{2w}{3}-\frac h{\sqrt3}\right)^2=8wh-2\sqrt3(w^2+h^2).
\]
The same formula is symmetric in \(w,h\). In the hexagonal regime the area is \(2m^2/\sqrt3\). Polar integration gives
\[
\operatorname{area}(F_{w,h})=\frac12\int_0^{2\pi}L_{w,h}(\theta)^2\,d\theta,
\]
proving the asserted exact mean-square formula.

**5. The complete probability law.** Fix \(0<u<R(w,h)\). The orientation is admissible at scale \(u\) precisely if all six strip inequalities hold on the circle \(|z|=u\). For a strip of half-width \(a\) with normal angle \(\phi\), failure occurs in two open angular intervals centered at \(\phi\) and \(\phi+\pi\); their combined length is \(4\arccos(\min\{1,a/u\})\). The six normal directions modulo \(\pi\) alternate every \(\pi/6\) between the two strip groups. Put \(\alpha(u)=\arccos(\min\{1,w/(\sqrt3u)\})\) and \(\beta(u)=\arccos(\min\{1,h/(\sqrt3u)\})\). In the twelve-vertex regime, the explicit intersection vertex in Step 3 shows \(\alpha(R)+\beta(R)=\pi/6\), with each angle strictly between zero and \(\pi/6\). Both functions are nondecreasing in \(u\), so for \(u<R\) the forbidden angular intervals around alternate normals have half-widths with sum strictly below \(\pi/6\), and intervals from the same group remain farther apart. Therefore they are pairwise disjoint. In the hexagon regime the larger-half-width group has inradius at least \(R\), hence contributes no forbidden intervals, while the active group has \(\alpha(R)=\pi/6\), so its intervals are likewise disjoint for \(u<R\). At \(u=R\), adjacent intervals just meet, a finite set of angles. Summing three strips from each of the two groups gives excluded length
\(12[\arccos(\min\{1,w/(\sqrt3u)\})+\arccos(\min\{1,h/(\sqrt3u)\})]\). Division by \(2\pi\) establishes the survival formula and its endpoint limits.

**6. Distinct sharp rectangle optimizers.** Put \(S=wh\) and \(q=\max(w,h)/\min(w,h)\ge1\). In the twelve-gon regime,
\[
\frac{\mathcal A(w,h)}S=8-2\sqrt3(q+1/q),\qquad
\frac{R(w,h)^2}S=\frac43(q+1/q-\sqrt3).
\]
The first expression is strictly decreasing for \(q>1\), so its unique maximum is at \(q=1\). For \(q\ge2/\sqrt3\), the normalized area is \(2/(\sqrt3q)\le1<8-4\sqrt3\); hence the square is the unique mean-square maximizer over all rectangles. The second expression is strictly increasing for \(1<q<2/\sqrt3\), whereas for \(q\ge2/\sqrt3\) it equals \(4/(9q)\), strictly decreasing. Thus the global maximum occurs exactly when \(q=2/\sqrt3\), where \(R^2/S=2\sqrt3/9\); reciprocation of the aspect gives precisely two oriented ratios.

## Verification

The accompanying standalone file `CHECK.py` independently reconstructs the feasible polygon by intersecting the twelve linear halfplanes arising from all three vertex pairs. It compares polygon area and farthest-vertex distance with the analytic expressions on twelve shape choices across both critical thresholds. It also computes orientation-by-orientation fit directly from projected vertex coordinates, checking the radial-area identity by midpoint quadrature and checking 48 survival probabilities against their exact formulas. It uses only the Python standard library. Execute `python3 CHECK.py`; this finite regression is not used as a proof for the all-positive-real-parameter theorem.

## Relationship to prior work

Choi and Choi (arXiv:2611.08556, first posted 2026-11-05) introduce the similarity containment polytope and study efficient organization of its silhouette for general triangles and convex polygons, under general-position assumptions that exclude rectangles with parallel sides. Their identification of the feasible projected similarity polygon is the conceptual starting point; the present theorem supplies an explicit orientation-distribution and aspect-ratio optimization for the degenerate-symmetry rectangle case that is not asserted there. The classical largest-equilateral-triangle-in-a-square result gives the maximally fitting orientation in the square and is not new here. The known minimum-area axis-aligned bounding rectangle of an equilateral triangle, equivalently the minimum endpoint of the published rotated-regular-polygon bounding-box-area law, already implies the fixed-container-area *best single orientation* extremum at aspect ratio \(2/\sqrt3\); we include it only for the comparison with the new mean-square extremum. The bounding-box-area law itself measures only a product of widths; the new survival law depends jointly on horizontal and vertical widths and is not a one-dimensional transform of that product distribution. The separate published exact triangle-self-containment result concerns a triangle as both source and target; it does not imply the rectangle law. The explicit prior-work comparisons and remaining priority risks appear in the review record.

## Limitations

The theorem concerns a fixed equilateral source triangle, axis-aligned rectangular targets, unrestricted translations, and uniformly distributed orientation. It does not classify all source triangles or all convex polygon targets, nor does it specify a unique optimal translation when multiple translations fit. The classical optimal fitting in a square, the minimum-area enclosing-rectangle aspect ratio for an equilateral triangle, and the generic containment-polytope representation are credited prior knowledge. The scientific priority assessment is necessarily provisional; independent audit has not been performed.

## References

1. Y. Choi and S. Choi, *The Containment Polytope of a Triangle and a Convex Polygon*, arXiv:2611.08556v1 (2026-11-05), https://arxiv.org/html/2611.08556v1 .
2. B. Chazelle, and the works of Agarwal--Amenta--Sharir and Chan--Hair, on geometric containment algorithms, as cited in Choi--Choi (2026), Introduction; the main present proof uses only the explicit containment definition.
3. *Fold Square into Equilateral Triangle*, cut-the-knot, https://www.cut-the-knot.org/pythagoras/PaperFolding/EquilateralTriangleInSquare.shtml (classical square optimum).
4. *The largest triangle in a square*, Origami & Folding, https://www.origami-folding.com/essays/the-largest-triangle-in-a-square/ (independent treatment of the classical square benchmark).
