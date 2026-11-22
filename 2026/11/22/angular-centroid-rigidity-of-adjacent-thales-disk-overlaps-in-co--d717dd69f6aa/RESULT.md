# Angular-centroid rigidity of adjacent Thales-disk overlaps in convex polygons

## Finding
Let \(P\subset\mathbb R^2\) be a strictly convex polygon with cyclic vertices \(v_1,\ldots,v_m\), \(m\ge3\), interior angles \(\theta_i\in(0,\pi)\), and area \(A(P)\). For every \(B\in\operatorname{int}P\), write \(D_i(B)\) for the closed Euclidean disk with diameter \([B,v_i]\). Define the *adjacent overlap energy* using the **full-plane** lens areas
\[
S_P(B):=\sum_{i=1}^{m}\operatorname{area}\bigl(D_i(B)\cap D_{i+1}(B)\bigr),\qquad v_{m+1}:=v_1.
\]
Then the following exact identity holds for every such \(P\) and \(B\):
\[
\boxed{S_P(B)=\frac14\sum_{i=1}^{m}\theta_i\lVert B-v_i\rVert^2-\frac12 A(P).}
\]
The unique minimum over interior points is attained at the angle-weighted vertex center
\[
\boxed{B_*=\frac{\sum_i\theta_i v_i}{(m-2)\pi}\in\operatorname{int}P,\quad
S_P(B)-S_P(B_*)=\frac{(m-2)\pi}{4}\lVert B-B_*\rVert^2.}
\]
Thus the exact curvature of the overlap energy is independent of all geometry except the number of vertices. In particular, for a triangle, this energy is also the Euclidean area of the set covered by at least two of its three disks (up to a null set), so the formula exactly optimizes genuine double-coverage area, not merely a pair-counting surrogate.

## Assumptions and scope
The ambient measure is ordinary two-dimensional Lebesgue area on the whole plane. The reference point \(B\) lies strictly inside \(P\); the polygons have no repeated or collinear adjacent vertices. The discs are closed and their pairwise boundary sets have zero area. For \(m>3\), adjacent overlaps are counted with multiplicity: the energy is **not** the total area of all doubly covered points, nor is it truncated to \(P\). No extension to nonconvex polygons is asserted.

## Proof
First prove a two-disk lemma. For distinct points \(u,v,B\) with \(B\) off the supporting line \(uv\), let \(\alpha=\angle Buv\), \(\beta=\angle Bvu\), and \(T=\operatorname{area}(\triangle Buv)\). The circles with diameters \([B,u]\) and \([B,v]\) intersect at \(B\) and the perpendicular projection of \(B\) onto the line \(uv\). Their radii are \(\lVert B-u\rVert/2\) and \(\lVert B-v\rVert/2\), and their center separation is \(\lVert u-v\rVert/2\). The two circular sectors of their lens have central angles \(2\alpha\) and \(2\beta\). Subtracting the two center-to-common-chord triangles (the resulting kite has area \(T/2\)) gives
\[
\operatorname{area}(D_u\cap D_v)
=\frac14\left(\alpha\lVert B-u\rVert^2+\beta\lVert B-v\rVert^2\right)-\frac12T.
\]
This formula also holds when a vertex angle of \(\triangle Buv\) is obtuse: the central-sector formula uses angles in \((0,\pi)\), without assuming the perpendicular foot lies inside \([u,v]\).

Apply the lemma to every directed boundary edge \([v_i,v_{i+1}]\). Because \(B\in\operatorname{int}P\), the fan triangles \(\triangle Bv_iv_{i+1}\) partition \(P\) in area, so \(\sum_i T_i=A(P)\). At the vertex \(v_i\), the two fan-triangle angles are exactly the pieces of its polygon angle, so \(\angle Bv_iv_{i-1}+\angle Bv_iv_{i+1}=\theta_i\). After summation each squared distance gets coefficient \(\theta_i/4\), proving the identity.

The polygon's angle sum is \(T_\theta:=\sum_i\theta_i=(m-2)\pi>0\). Completing the square in the weighted sum gives
\[
\sum_i\theta_i\lVert B-v_i\rVert^2
=\sum_i\theta_i\lVert B_*-v_i\rVert^2+T_\theta\lVert B-B_*\rVert^2.
\]
Every \(\theta_i\) is strictly positive, so \(B_*\) is a strictly positive convex combination of all vertices and lies in \(\operatorname{int}P\). This proves existence, uniqueness, and the sharp global quadratic stability identity.

For triangles only, every \(X\) in all three diameter disks satisfies \(\lVert X-B\rVert^2\le (X-B)\cdot(v_i-B)\) for all three vertices. Take positive barycentric weights \(\lambda_i\) representing \(B=\sum_i\lambda_i v_i\). Summing the three inequalities yields \(\lVert X-B\rVert^2\le0\), hence \(X=B\). Thus triple intersection has zero area, and the three pairwise intersections are disjoint almost everywhere. Every point belonging to two or three disks is therefore counted exactly once by \(S_P(B)\). For an equilateral triangle of circumradius one and center \(B=0\), the exact minimum is \(\pi/4-3\sqrt3/8\); the sharp quadratic rise is \(\pi\lVert B\rVert^2/4\).

## Verification
The accompanying \`verify_lens.py\` independently evaluates two-circle intersection areas via the arccosine lens formula and compares them to the angular weighted polygon expression on 900 deterministic convex polygon instances with three through twelve vertices. It includes points close to vertices and a separate analytic-limit comparison for a triangle. All tests pass at a maximum absolute tolerance of \(10^{-7}\) for the full sum. These finite comparisons are sanity checks only; the proof above is exact and covers all admitted polygons and interior reference points.

## Relationship to prior work
Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1, establishes polytope coverage by vertex-to-point diameter balls and a power-diagram tiling, not the full-plane area of neighboring-disk intersections as the point moves. Existing published calculations describe the coverage multiplicity and average coverage depth of regular polygons with the point at their center; they do not imply the variable-interior-point identity for arbitrary convex polygons or its angle-weighted minimizer. The two-circle segment-area formula itself is classical and is not claimed to be new. The assertion here is its polygon-wide cancellation, sharp independent-of-shape quadratic stability, and double-coverage interpretation for arbitrary triangles.

## Limitations
The result concerns adjacent pair areas, even when some portions lie outside \(P\). For polygons with at least four vertices this is not the full overlap-multiplicity distribution, and an optimal position for this energy need not minimize the clipped or total multiply-covered area. Independently indexed older geometric literature may contain equivalent identities; the originality assessment is provisional and not independent validation.

## References
1. J. Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277v1 (first posted 10 November 2026), https://arxiv.org/html/2611.14277v1 .
2. *Exact multiplicity spectrum of vertex-to-center diameter disks of regular polygons*, public mathematical record (17 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-multiplicity-spectrum-of-vertex-to-center-diameter-disks-o--1b3f060ecc28 .
3. *Exact diameter-disk depth of a regular polygon: mean redundancy and a quantitative limit law*, public mathematical record (17 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-diameter-disk-depth-of-a-regular-polygon-mean-redundancy-a--a85d54c61c1a .
