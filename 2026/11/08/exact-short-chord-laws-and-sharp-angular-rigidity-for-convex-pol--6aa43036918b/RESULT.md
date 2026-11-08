# Exact short-chord laws and sharp angular rigidity for convex polygon boundaries

## Finding
Let \(Q\subset\mathbb R^2\) be a nondegenerate convex polygon with \(m\ge3\) genuine sides, perimeter \(P\), and exterior turning angles \(\theta_1,\ldots,\theta_m\in(0,\pi)\), in cyclic order. Thus \(\sum_i\theta_i=2\pi\). For independent points \(X,Y\) sampled uniformly by arclength on \(\partial Q\), write \(D=\|X-Y\|_2\) and
\[
B(Q)=\sum_{i=1}^m\left(\frac{\theta_i}{\sin\theta_i}-1\right).
\]
There exists \(r_0(Q)>0\) such that, **exactly** for \(0\le r<r_0(Q)\),
\[
\boxed{\Pr(D\le r)=\frac{2r}{P}+\frac{B(Q)r^2}{P^2}.}\tag{1}
\]
The coefficient is independent of individual edge lengths once the angles are fixed. Furthermore, with \(\overline\theta=2\pi/m\),
\[
\boxed{B(Q)\ge m\left(\frac{\overline\theta}{\sin\overline\theta}-1\right)+\frac16\sum_{i=1}^m(\theta_i-\overline\theta)^2.}\tag{2}
\]
Equality in (2) holds **exactly for equiangular polygons** (which need not be regular). The coefficient \(1/6\) is the best constant valid uniformly over all \(m\ge3\) and all convex polygons, but is not asserted optimal for any fixed \(m\).

## Assumptions and scope
A genuine side has positive length and two consecutive sides are noncollinear. The polygon is compact and full-dimensional; all interior angles \(\alpha_i=\pi-\theta_i\) lie strictly between \(0\) and \(\pi\). Points \(X,Y\) are independent draws from the probability measure \(\mathcal H^1|_{\partial Q}/P\), not independent interior-area points, invariant-line chords, or sampled vertices. The equality/inequality choice in \(D\le r\) is immaterial because the distribution has no atoms at positive distances. The small-radius threshold is polygon-dependent; no bound uniform over degenerating polygons is claimed.

## Proof
**1. Decomposition by sides.** Label the edges \(E_1,\ldots,E_m\), with lengths \(\ell_i\). For \(0\le r\le\ell_i\), ordered pairs of endpoints on the same edge satisfying \(\|X-Y\|\le r\) occupy the arclength-parameter square of area \(2\ell_i r-r^2\). Adding these contributions and dividing by \(P^2\) gives
\[
\frac1{P^2}\sum_i(2\ell_i r-r^2)=\frac{2r}{P}-\frac{mr^2}{P^2}.\tag{3}
\]
Distinct nonadjacent compact edges have a strictly positive distance, so there is a positive threshold below which they make no contribution. For a triangle, there are no pairs of nonadjacent edges.

**2. Exactly one corner contribution.** Consider consecutive edges meeting at an interior angle \(\alpha\). Put their arclength coordinates \(s,t\ge0\) outward from their shared vertex, and let their outward unit directions be \(u,v\), with angle \(\alpha\). Their endpoint difference is \(s u-t v\). The linear map \((s,t)\mapsto s u-t v\) has absolute Jacobian \(\sin\alpha\), and maps the positive quadrant onto the infinite cone between \(u\) and \(-v\), of aperture \(\pi-\alpha=\theta\). The preimage of the disk of radius \(r\) therefore has parameter area
\[
\frac1{\sin\alpha}\frac{\theta r^2}{2}=\frac{\theta r^2}{2\sin\theta}.\tag{4}
\]
For each edge pair, if \(r<\min(\ell_{i-1},\ell_i)\sin\alpha_i\), the inequality \(\|su-tv\|\le r\) forces both \(s,t\) below the corresponding edge lengths, so the finite edge domains do not truncate (4). Summing the *two* possible orders of each adjacent edge pair gives \(\sum_i\theta_i r^2/(P^2\sin\theta_i)\). Combining this with (3) proves (1). One may take any positive \(r_0(Q)\) smaller than all edge lengths, all adjacent-edge truncation thresholds, and the distances between nonadjacent edge pairs. The formula includes all possible edge allocations, and its polynomial terminates exactly at degree two locally.

**3. Quantitative angular rigidity.** Put \(f(t)=t/\sin t\) for \(0<t<\pi\). Euler's sine product gives the locally absolutely convergent expansion
\[
f(t)=\prod_{k\ge1}\left(1-\frac{t^2}{k^2\pi^2}\right)^{-1}=1+\frac{t^2}{6}+\sum_{j\ge2}c_jt^{2j},\qquad c_j>0.\tag{5}
\]
Consequently \(f''(t)>1/3\) throughout \((0,\pi)\), so \(g(t)=f(t)-t^2/6\) is strictly convex. Since \(\sum_i\theta_i=m\overline\theta\), Jensen's inequality gives
\[
\sum_i f(\theta_i)-m f(\overline\theta)\ge\frac16\left(\sum_i\theta_i^2-m\overline\theta^2\right)=\frac16\sum_i(\theta_i-\overline\theta)^2.\tag{6}
\]
This is (2). Strict convexity implies equality exactly for equal angles; such polygons exist (including regular ones), and not all equiangular polygons are regular.

**4. Optimality of the universal coefficient.** Let \(m=4k\to\infty\), \(b=2\pi/m\), and \(\varepsilon=b/7\). Prescribe cyclic turns \(\theta_i=b+(-1)^i\varepsilon\), and take successive unit-length edge vectors whose direction increments are these angles. All turns lie strictly in \((0,\pi)\), and every half-period of \(m/2\) turns sums to \(\pi\), so the second half of the edge-vector sequence is precisely the negative of the first. The edge path therefore closes and bounds a strictly convex, centrally symmetric equilateral polygon. For this family, the ratio of the difference on the left of (2) before the variance term to the angular variance equals
\[
\frac{\tfrac12[f(b+\varepsilon)+f(b-\varepsilon)]-f(b)}{\varepsilon^2}\longrightarrow\frac12 f''(0)=\frac16.\tag{7}
\]
Here \(b,\varepsilon\to0\), and the Taylor expansion is uniform near zero by (5). Therefore no universal positive improvement beyond \(1/6\) is possible. This construction demonstrates sharpness in the convex-polygon class, rather than merely among unconstrained angle lists.

## Verification
The accompanying standard-library program `verify.py` calculates exterior angles from actual convex polygon coordinates, checks (1) against seeded independent arclength-pair simulations on four distinct shapes, checks the exact equilateral-triangle and square coefficients, tests (2), and exhibits convergence of the sharpness quotient for \(m=16,64,256,1024\). Run `python3 verify.py`; the output ends in `VERIFY_OK convex_polygons=4 random_pairs=1080000 analytic_special_cases=2 sharpness_sizes=4`. The sampling experiments are finite checks and do not prove (1)–(2); the complete proof is analytic above. In particular, for a square \(B=2\pi-4\), whereas an equilateral triangle has \(B=4\pi/\sqrt3-3\).

## Relationship to prior work
Bäsel [1] obtains invariant-line chord-length distributions for regular polygons and, as a consequence, distances for independent **interior-area-uniform** points. Pure and Durrani [2] give an exact polygon distance-to-reference-point algorithm for an **interior-area-uniform** point. Tong and Pan [3] describe an algorithmic distribution for two random points of arbitrary polygons, also under interior sampling. Baltzis [4] discusses distances of points in convex polygons, but only its abstract was available for inspection. Those contexts must not be conflated with independent **perimeter-arclength endpoints**. A separate published polygon-angle result [5] establishes an exactly quartic small-distance probability for two **interior-area-uniform** points and an optimal \(1/(24\pi^2)\) angle-stability coefficient, based on a different covariogram; it neither yields (1) nor (2) by specializing its hypotheses. The present short-boundary-pair coefficient and its sharp angular rigidity were not identified in the inspected materials. The general problem of recovering full distance laws from polygonal integration is well established; only the particular exact local law and globally optimal angular variance bound are proposed here.

## Limitations
The equal-angle class is not required to have equal sides. Formula (1) is not a full-distance CDF and applies only for polygon-dependent sufficiently small radii. The optimal \(1/6\) is uniform over all side counts and not claimed to be the optimal fixed-\(m\) stability coefficient. It is not claimed that a single short-distance coefficient uniquely determines a polygon. No analogous theorem for nonconvex boundaries, smooth curves, higher dimensions, or correlated sampling is established. An unindexed equivalent historical statement remains possible, and [4] could not be inspected beyond its abstract. These are population-probability, not finite-sample estimation, statements.

## References
1. Uwe Bäsel, *Random Chords and Point Distances in Regular Polygons*, arXiv:1204.2707v1, first posted 12 April 2012, https://arxiv.org/abs/1204.2707; author-uploaded accessible full text, https://www.researchgate.net/publication/223967035_Random_chords_and_point_distances_in_regular_polygons.
2. Ross Pure and Salman Durrani, *Computing Exact Closed-Form Distance Distributions in Arbitrarily Shaped Polygons with Arbitrary Reference Point*, The Mathematica Journal 17 (2015), https://www.mathematica-journal.com/2015/06/28/computing-exact-closed-form-distance-distributions-in-arbitrarily-shaped-polygons-with-arbitrary-reference-point/.
3. Fei Tong and Jianping Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407 (2016), https://arxiv.org/abs/1602.03407.
4. K. B. Baltzis, *Distance Distribution in Convex n-Gons: Mathematical Framework and Wireless Networking Applications*, Wireless Personal Communications 71 (2013), 1487–1503, https://doi.org/10.1007/s11277-012-0887-9 (abstract inspected, full text unavailable).
5. *Sharp uniform angular stability for the short-pair distance coefficient of convex polygons*, published-finding corpus record, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b/RESULT.md (complete mathematical statement and proof inspected).
