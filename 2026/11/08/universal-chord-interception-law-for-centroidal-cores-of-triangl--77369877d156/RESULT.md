# Universal chord-interception law for centroidal cores of triangles

## Finding
Let \(T\) be any nondegenerate Euclidean triangle with perimeter \(P\), sides \(a_1,a_2,a_3\), and centroid \(G\). Put \(p_i=a_i/P\). Choose independent points \(X,Y\) uniformly with respect to arclength on \(\partial T\). For \(0\le r\le1\), let \(T_r=G+r(T-G)\), and define the least intercepted scale
\[
R_*:=\inf\{r\in[0,1]:[X,Y]\cap T_r\ne\varnothing\}.
\]
For \(0<r<1\), let \(t=(1-r)/3\). Then
\[
\Pr(R_*\le r)=\left(1-\sum_{i=1}^3p_i^2\right)F(r),
\]
where the universal function \(F\) is
\[
F(r)=1-2t-3t^2+2t^2\log t
+2t(2t-1)\log(1-2t)
+2t(1-3t)\log(1-t).
\]
The endpoint values are \(\Pr(R_*\le0)=0\) and \(\Pr(R_*\le1)=1\). In particular, \(R_*\) has an atom of mass \(\sum_i p_i^2\) at \(1\), and no atom in \([0,1)\). Conditional on endpoints lying on distinct sides, \(R_*\) has distribution function \(F\), independent of the triangle's angles and proportions.

For every \(0<r<1\), this probability is uniquely maximized, among all nondegenerate triangles of a fixed perimeter, by the equilateral triangle. Sharp bounds are
\[
\frac12F(r)<\Pr(R_*\le r)\le\frac23F(r),
\]
with the lower infimum approached by flattening triangles whose normalized side lengths approach \((1/2,1/2,0)\). The small-core law is
\[
\Pr(R_*\le r)=\left(1-\sum_i p_i^2\right)
\left(\frac{2(1+\log2)}{3}\,r+O(r^2)\right)
\qquad(r\downarrow0).
\]
Also \(F(r)=1-\frac23(1-r)+O((1-r)^2|\log(1-r)|)\) as \(r\uparrow1\).

More generally, if each endpoint first independently selects side \(i\) with any probabilities \(w_1,w_2,w_3\ge0\) summing to one and then samples uniformly along that side, the same law holds with \(p_i\) replaced by \(w_i\). This includes arclength sampling as \(w_i=p_i\).

## Assumptions and scope
The triangle is closed and nondegenerate, points are sampled independently, and side endpoints have probability zero. The target \(T_r\) is obtained by positive homothety about the **area centroid**, not by an arbitrary incenter scaling or Euclidean offset. A chord is the closed segment \([X,Y]\), not the full supporting line. Its intersection with \(T_r\) may be tangential, with probability-zero endpoint exceptions. The formula for \(r<1\) must not be substituted at \(r=1\): same-side chords meet the outer triangle but no strictly smaller core. All logarithms are natural.

## Proof
**Conditional side reduction.** If the two endpoints fall on one side, their segment remains on that side of \(T\) and misses every \(T_r\) with \(r<1\). If they fall on two distinct sides, the affine map carrying \(T\) to the standard barycentric triangle preserves uniform parameters along each side. Every ordered distinct-side choice therefore has the same conditional hit probability. The probability of distinct sides is \(1-\sum_i w_i^2\), which proves the factorization once the universal conditional probability \(F\) is computed.

**Exact conditional integration.** Label the sides through a common vertex \(A\) by \(AB\) and \(AC\). Independently choose \(u,v\) uniformly on \([0,1]\), giving barycentric endpoint triples \((1-u,u,0)\) and \((1-v,0,v)\). The core \(T_r\) consists of barycentric triples whose three entries are at least \(t=(1-r)/3\). Along the chord, with interpolation parameter \(\lambda\in[0,1]\), the three coordinates are
\[
(1-u+\lambda(u-v),\ (1-\lambda)u,\ \lambda v).
\]
By symmetry it suffices to treat \(u\ge v\). Requiring the last two coordinates to be at least \(t\) gives \(t/v\le\lambda\le1-t/u\), possible precisely when \(v\ge tu/(u-t)\). On this interval the first coordinate is nondecreasing in \(\lambda\), so its maximum occurs at \(\lambda=1-t/u\). The additional requirement that this maximum is at least \(t\) is \(v\le(1-2t)u/(u-t)\). Combining with \(v\le u\), the permitted region is
\[
\begin{array}{ll}
2t\le u\le1-t:&\quad \dfrac{tu}{u-t}\le v\le u,\\[2mm]
1-t\le u\le1:&\quad \dfrac{tu}{u-t}\le v\le\dfrac{(1-2t)u}{u-t}.
\end{array}
\]
Consequently its doubled area in the unit square is
\[
F(r)=2\int_{2t}^{1-t}\left(u-\frac{tu}{u-t}\right)du
+2\int_{1-t}^{1}\frac{(1-3t)u}{u-t}\,du.
\]
Elementary integration gives exactly the logarithmic expression in the Finding. Since the regions are nested as \(r\) increases and have strictly increasing area for \(0<r<1\), \(F\) is continuous and strictly increasing from zero to one on that interval. The limit \(F(1^-)=1\) follows from the integral or from the formula. Thus the only atom in the unconditional law is the same-side atom at \(1\).

**Sharp shape bounds.** For nondegenerate side lengths, \(p_i\in(0,1/2)\) and \(\sum_i p_i=1\). Cauchy's inequality gives \(\sum_i p_i^2\ge1/3\), with equality precisely for an equilateral triangle. Conversely, \(p_i^2<p_i/2\) implies \(\sum_i p_i^2<1/2\). Triples approaching \((1/2,1/2,0)\) are realized by nondegenerate flattening triangles and approach the upper bound \(1/2\) on this sum. Multiplication by the strictly positive \(F(r)\) yields the stated unique maximizer and sharp unattained lower bound.

**Asymptotics.** Differentiating the displayed elementary formula at \(t=1/3\) gives \(dF/dt=-2(1+\log2)\). Since \(dt/dr=-1/3\), the small-core coefficient is \(2(1+\log2)/3\). As \(t\downarrow0\), the elementary expansion is \(F=1-2t+O(t^2|\log t|)\). These expansions apply to the continuous component; at \(r=1\) the unconditional distribution jumps by \(\sum_i p_i^2\).

## Verification
The dependency-free Python script `checker.py` separately clips Euclidean segments against three oriented half-planes of the actual inner triangle and samples endpoint side choices in proportion to their Euclidean side lengths. On three scalene/right-shaped test triangles and five scales it checked \(975000\) chords in total against the full formula, with every discrepancy within six binomial standard errors plus \(0.0005\); it reported `TRIANGLE_CENTROID_CORE_CHORD_CDF_OK 975000`. Separately, symbolic integration of the two explicit integrals yielded the stated expression, and a direct unit-square simulation of the barycentric inequalities matched it at six scales. These finite checks are not substitutes for the preceding exact proof. To reproduce: `python3 checker.py`.

## Relationship to prior work
Classical geometric-probability literature distinguishes invariant random lines, random line-section lengths, and random chords generated by two points. Álvarez Lobo's 2016 preprint on random triangle-cut segment lengths is especially relevant to the distinct-side sampling model; its accessible abstract concerns a length threshold, not interception of every centroidal homothetic core. Bäsel's 2013 work addresses intersection of random convex bodies with a triangular lattice, which is a different hitting experiment. Egan's treatment of two interior-uniform points in a square determines which *sides a supporting line* crosses; here the samples are on the boundary and one tests whether the finite segment meets a nested target. MathWorld's triangle line-picking material concerns Euclidean distances between area-uniform interior points. Existing boundary-chord moments and rectangular target-hit profiles likewise do not imply this triangle-core distribution: chord length, midpoint statistics, or one fixed target probability do not determine the entire core-interception law. The essential claimed contribution is the all-scale logarithmic law, its side-weight factorization, its endpoint atom, and its sharp triangle-shape bounds, not the elementary affine invariance of a simplex or the general ability to integrate two-dimensional probabilities.

## Limitations
The theorem is specific to triangle **boundary endpoints** and **centroidal homothetic targets**. It does not treat area-uniform endpoints, invariant random affine lines, off-center homotheties, polygons with more sides, or three-dimensional simplices. The law only depends on \(\sum_i p_i^2\), so it cannot reconstruct a triangle's entire shape. Full-text historical priority checks of the 2016 triangle-cut segment-length preprint remain incomplete; a related paper not available in full text could alter the novelty assessment. Independent mathematical verification has not been performed.

## References
- J. Álvarez Lobo, *A Geometric-Probabilistic problem about the lengths of the segments intersected in straights that randomly cut a triangle*, preprint, arXiv:1602.03005 (2016), https://arxiv.org/abs/1602.03005 .
- U. Bäsel, *Hitting probabilities for random convex bodies and lattices of triangles*, arXiv:1312.5131 (public December 18, 2013), https://arxiv.org/abs/1312.5131 .
- J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, J. Appl. Probab. **19** (1982), 873–879, DOI:10.2307/3213843 .
- G. Egan, *Pick Two Points*, https://www.gregegan.net/SCIENCE/PickTwoPoints/PickTwoPoints.html (section on two interior-uniform points in a square).
- E. W. Weisstein, *Triangle Line Picking*, MathWorld, https://mathworld.wolfram.com/TriangleLinePicking.html .
