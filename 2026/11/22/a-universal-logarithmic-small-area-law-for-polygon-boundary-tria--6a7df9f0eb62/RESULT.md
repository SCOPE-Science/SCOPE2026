# A universal logarithmic small-area law for polygon-boundary triangles

## Finding

Let \(K\) be a convex Euclidean polygon with \(m\ge4\) genuine sides (no collinear consecutive sides), side lengths \(\ell_1,\ldots,\ell_m>0\), total perimeter \(P=\sum_i\ell_i\), and interior angles \(\alpha_i\in(0,\pi)\), indexed so that side \(i-1\) and side \(i\) meet at vertex \(i\). Sample \(X_1,X_2,X_3\) independently from normalized boundary arclength on \(\partial K\), and write \(A=\operatorname{Area}[X_1,X_2,X_3]\). Then

\[
\Pr(A=0)=\sum_{i=1}^m(\ell_i/P)^3
\]

and, as \(s\downarrow0\),

\[
\boxed{\Pr(0<A/P^2\le s)=C(K)s\log(1/s)+O_K(s),\qquad
C(K)=\frac{12}{P}\sum_{i=1}^m\frac{\ell_{i-1}+\ell_i}{\sin\alpha_i}.}
\]

The sharp shape inequality is \(C(K)\ge24\), and equality holds **if and only if \(K\) is a rectangle**, with no restriction on its aspect ratio. In particular, any rectangle has the same leading nonzero small-area probability after scaling area by squared perimeter. For a square of side one, \(\Pr(A=0)=1/16\) and \(\Pr(0<A\le t)=\frac32 t\log(1/t)+O(t)\). The triangle-host case is excluded because its complete three-point boundary-area distribution was previously determined; it supplies a known consistency check, not a new case.

There is also a limiting geometric description. Condition on \(0<A\le t\), and put \(s=t/P^2\). With conditional probability tending to one, precisely two sampled points lie on a common side \(i\), and the third lies on an adjacent side \(j\). The ordered side pattern \((i,i;j)\) has limiting probability

\[
\frac{\ell_i/\sin\alpha_v}{\sum_w(\ell_{w-1}+\ell_w)/\sin\alpha_w},
\]

where \(v\) is the shared vertex. Given this pattern, let \(u\) be the distance along side \(i\) between its two sampled points; let \(b\) be the smaller of their two arclength coordinates measured from any fixed endpoint; and define

\[
Q_t=\frac{\log(u/\ell_i)}{\log(t/P^2)},\qquad Z_t=A/t,\qquad B_t=b/\ell_i.
\]

Jointly, the pattern, \(Q_t\), \(Z_t\), and \(B_t\) converge in law to the stated discrete pattern distribution times three independent uniform distributions on \([0,1]\). Thus the near-degeneracy has a uniform logarithmic split between the two same-side points and the third point's approach to the common vertex.

## Assumptions and scope

The polygon has at least four genuine sides and is fixed while \(t\to0^+\). All sides have strictly positive lengths and no interior angle is \(\pi\). Boundary sampling uses Euclidean arclength, not uniform sampling of the polygon interior or uniform selection of a side. Sample coincidences at vertices have probability zero. The \(O_K\) constant may depend on the particular polygon; no uniform error bound over degenerating polygon families is asserted.

## Proof

**1. Zero-area atom.** A line intersects the boundary of a convex polygon in at most two points unless it contains a side. Three independent boundary samples can be collinear with positive probability only when all three are on the same side. The mutually exclusive events have probabilities \((\ell_i/P)^3\), proving the atom.

**2. Exact integral for the only logarithmic configurations.** Distinguish the side containing each of the three labelled samples. Suppose two samples lie on side \(i\), the third on its neighboring side \(j\), and their common vertex has interior angle \(\alpha\). Parametrize the repeated-side points by coordinates \(x,y\in[0,\ell_i]\), and the remaining point by its distance \(r\in[0,\ell_j]\) from that vertex. Regardless of whether \(x\) and \(y\) are measured from the common vertex or the opposite endpoint,

\[
A=\tfrac12|x-y|r\sin\alpha.
\]

Writing \(\delta=2t/(\ell_j\sin\alpha)\), integration first in \(r\) gives the exact, *unnormalized* arclength-coordinate volume, for \(0<t<\ell_i\ell_j\sin\alpha/2\):

\[
\begin{aligned}
I_{i,j}(t)&=2\int_0^{\ell_i}(\ell_i-u)\min\left\{\ell_j,\frac{2t}{u\sin\alpha}\right\}\,du\\
&=\frac{4\ell_i t}{\sin\alpha}\log\frac{\ell_i\ell_j\sin\alpha}{2t}
+\frac{4t^2}{\ell_j\sin^2\alpha}.
\end{aligned}
\]

The apparent singularity at \(u=0\) is resolved by the first branch of the minimum. Each side pattern has three placements of its singleton among the labelled samples, giving a factor of three. The two orientations at each vertex (which side contains the repeated samples) give the coefficient \(12(\ell_{i-1}+\ell_i)/(P^3\sin\alpha_i)\) before rescaling.

**3. All other patterns have \(O_K(t)\) probability.** If the samples lie on one side, their area is exactly zero, already excluded. If two lie on side \(i\) and the third lies on a nonneighboring side \(j\), the distance from side \(j\) to the supporting line of side \(i\) has a strictly positive minimum. The area is half that distance times \(|x-y|\); integrating the set \(|x-y|\le c_Kt\) gives \(O_K(t)\).

If all three samples lie on distinct sides, parameterize each side by an arclength interval. Their signed double-area is a smooth multiaffine function \(F\) of the three arclength coordinates, with fixed sign because the three sides occur in cyclic polygon order. A zero of \(F\) forces two sampled points to coincide at a common vertex \(V\), while the third point \(W\) lies on a third, distinct side. At the zero, the two partial derivatives of \(F\) in the coordinates of the coincident points are (up to signs) \(\det(e_1,W-V)\) and \(\det(e_2,W-V)\), where \(e_1,e_2\) are unit directions of the two incident sides. These cannot both vanish: the incident directions are linearly independent and \(W\ne V\). Thus at least one coordinate partial derivative has absolute value bounded away from zero in a neighborhood of every zero. Compactness gives a finite cover of the zero set by such neighborhoods. For fixed other coordinates, monotonicity in the nonvanishing-derivative coordinate bounds the set \(|F|\le2t\) by an interval of length \(O_K(t)\); the complement of these neighborhoods is bounded away from zero. Fubini yields \(O_K(t)\) for every three-distinct-sides pattern. There are only finitely many side patterns.

Combining step 2 with this bound and dividing by \(P^3\), then setting \(t=P^2s\), proves the asserted expansion.

**4. Universal optimum.** Since every \(\sin\alpha_i\le1\),

\[
C(K)=\frac{12}{P}\sum_i\frac{\ell_{i-1}+\ell_i}{\sin\alpha_i}
\ge\frac{12}{P}\sum_i(\ell_{i-1}+\ell_i)=24.
\]

Every length is positive, so equality forces \(\sin\alpha_i=1\) for every vertex, hence every interior angle is a right angle. The polygon angle-sum formula then forces exactly four sides; the polygon is a rectangle. Conversely every rectangle realizes equality.

**5. Marked limiting law.** In the positive-area rare event, step 3 is smaller by a factor \(1/\log(1/t)\), so only oriented adjacent-side patterns survive. Their normalized leading coefficients give the discrete weights in the statement. Within one such pattern, change variables from \((x,y,r)\) to the lower repeated-side coordinate \(b\), its gap \(u=|x-y|\), and the normalized triangle area \(z=u r\sin\alpha/(2t)\). On \(0<z<1\), the arclength volume element becomes \(4t(\ell_i-u)\,du\,dz/(u\sin\alpha)\) after integrating or retaining the lower coordinate as appropriate. The dominant logarithmic mass comes from gaps in \(t^{1-\eta}\ll u\ll t^\eta\) for any fixed \(0<\eta<1/2\); the discarded endpoints have relative mass at most \(2\eta+o(1)\). In this region \(u\to0\), the lower point ranges asymptotically uniformly along the full side, the variable \(z\) ranges uniformly in \([0,1]\), and the measure in \(\log u/\log t\) is flat. First let \(t\downarrow0\) and then \(\eta\downarrow0\). The joint convergence, including independence from the discrete side pattern, follows by bounded-continuous test functions. Fixed length normalizations change logarithms by \(O(1)\), negligible compared with \(|\log t|\).

## Verification

The standalone file `check_small_area.py` re-evaluates the exact side-pair integral by independent logarithmic quadrature; checks the square, a non-square rectangle, an equilateral triangle, and several regular polygons; checks the geometric determinant formula; and performs a finite direct simulation for the square. Run with `python3 check_small_area.py`. Its success marker is `POLYGON_BOUNDARY_SMALL_AREA_CHECKS_OK`. The analytical proof covers all fixed convex polygons with at least four genuine sides; the previously known triangle case appears only as a code consistency check. The finite simulation is not an infinite proof or a full numerical error certificate.

## Relationship to prior work

A prior exact result, *Sharp area-law ordering and shape reconstruction for triangles sampled by boundary arclength*, gives the complete unconditional three-perimeter-point area distribution for a triangular host. In that setting the atom and a logarithmic small-area term are already implied by its mixture formula; **none of the triangle-host specializations is claimed new here**. That prior result treats hosts with exactly three sides and explicitly makes no assertion for quadrilateral or higher-sided polygons. The present contribution is the multi-edge (at least four sides) logarithmic coefficient, its sharp rectangle-only minimizer, and the universal marked conditional geometric law. Its full published RESULT.md was read and the exact distribution compared.

Bárány and Steiger's article on the variance of random polygons studies hulls from *interior-uniform* points, not this three-point boundary model. Bäsel's polygon work gives invariant random-line chord-length and interior point-distance distributions, not the area of a triangle formed by three independent perimeter samples. Reitzner, Schütt, and Werner study convex hulls of many boundary-random points and their expected facet counts and missed volumes, not a fixed three-point triangle's lower-area distribution. A published square-boundary probability calculation treats a fixed positive area threshold, not the zero endpoint. The separate smooth-boundary small-triangle law has a \(t^{2/3}\) behavior; polygonal edges instead produce a positive atom and the \(t\log(1/t)\) term. None of these comparisons alone proves priority, and an unindexed earlier small-area computation remains possible.

## Limitations

The asserted new results hold for each fixed convex polygon with at least four genuine sides, not uniformly over vanishing edges or angles. The marked limit concerns the positive-area tail after removing the zero-area atom. The bound \(24\) optimizes the leading *continuous* small-area coefficient, not the atom nor the entire triangle-area distribution. Independent specialist verification and an exhaustive historical-priority determination have not been performed.

## References

1. I. Bárány and W. Steiger, *On the variance of random polygons*, Computational Geometry (2013), DOI: https://doi.org/10.1016/j.comgeo.2012.01.003. Public bibliographic record dated 2012-12-04: https://portal.mardi4nfdi.de/wiki/On_the_variance_of_random_polygons. The record classifies it under 52A22.
2. U. Bäsel, *Random chords and point distances in regular polygons*, Acta Math. Univ. Comenianae 83 (2014), 1–18, https://www.kurims.kyoto-u.ac.jp/EMIS/journals/AMUC/_vol-83/_no_1/_baesel/baesel.pdf. Primary MSC 60D05 and 52A22, as printed in the article.
3. M. Reitzner, C. Schütt, E. M. Werner, *The Convex Hull of Random Points on the Boundary of a Simple Polytope*, Discrete Comput. Geom. 69 (2023), 453–504, https://doi.org/10.1007/s00454-022-00460-2 (open preprint: https://arxiv.org/abs/1911.05917).
4. *Probability that a triangle inscribed in a square comprises at least one quarter of the square*, Mathematics Stack Exchange, https://math.stackexchange.com/questions/4877892/probability-that-a-triangle-inscribed-in-a-square-comprises-at-least-frac14 (2024; a different fixed-threshold problem).

5. *Sharp area-law ordering and shape reconstruction for triangles sampled by boundary arclength*, published mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-sharp-area-law-ordering-and-shape-reconstruction-for-triangles-s--b972c9513f97/RESULT.md. Exact three-edge boundary area distribution, an explicitly credited prior special case.
