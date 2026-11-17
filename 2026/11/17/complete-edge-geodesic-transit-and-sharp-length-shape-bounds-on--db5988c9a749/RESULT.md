# Complete-edge geodesic transit and sharp length-shape bounds on parallel metric graphs

## Finding

Let \(m\ge3\), and let \(G\) be the compact metric graph consisting of two vertices \(A,B\) joined by \(m\) distinct interval edges of positive lengths \(a,\ell_1,\ldots,\ell_{m-1}\), where \(0<a<\ell_i\) for every \(i\). Equip \(G\) with its intrinsic shortest-path metric and normalized arclength measure. Pick \(X,Y\) independently from this measure. With probability one their shortest geodesic is unique. Let \(T\) be the event that this geodesic traverses **the entire** shortest edge of length \(a\), including passage from one junction to the other. Write
\[
L=a+\sum_{i=1}^{m-1}\ell_i,\qquad d_i=\ell_i-a,\qquad S=\sum_{i=1}^{m-1}d_i=L-ma.
\]
Then the complete-edge transit law is
\[
\boxed{\mathbb P(T)=\frac{1}{L^2}\left(\frac14\sum_i d_i^2+\sum_{i<j}d_i d_j\right)
=\frac{2S^2-\sum_i d_i^2}{4L^2}.}
\]
No other edge has a positive probability of being traversed **in its entirety** by a minimizing geodesic. This concerns complete junction-to-junction transit, **not** use of a proper subsegment or standard vertex-pair edge betweenness.

The formula gives sharp two-sided length-shape bounds for fixed \(m\), fixed total length \(L\), and fixed shortest-edge length \(a\), where \(0<a<L/m\):
\[
\boxed{\frac14\left(1-\frac{ma}{L}\right)^2
<\mathbb P(T)\le\frac{2m-3}{4(m-1)}\left(1-\frac{ma}{L}\right)^2.}
\]
Equality in the upper bound holds if and only if \(\ell_1=\cdots=\ell_{m-1}\). The lower bound is the unattained infimum and is approached when all but one of the \(d_i\) tend to zero, maintaining their positivity and the fixed value of \(S\). Across all admissible edge lengths for fixed \(m\), the exact unattained supremum is \((2m-3)/(4(m-1))\), approached as \(a/L\to0\) with equal remaining edges. In the three-edge theta graph this supremum equals \(3/8\).

An exact conditional shape law refines the probability formula. Suppose both endpoints lie on one longer edge \(i\), and orient them so their coordinates from \(A\) satisfy \(x<y\). On the transit event, with \(\delta_i=d_i/2\), the three normalized nonnegative quantities
\[
\left(\frac{x}{\delta_i},\frac{\ell_i-y}{\delta_i},
1-\frac{x+\ell_i-y}{\delta_i}\right)
\]
are exactly \(\operatorname{Dirichlet}(1,1,1)\). If the endpoints lie on distinct longer edges \(i,j\) and the minimizing route goes from \(A\) to \(B\) along the shortest edge, then the coordinates
\[
\frac{2x}{d_i},\qquad \frac{2(\ell_j-y)}{d_j}
\]
are independent \(\operatorname{Uniform}(0,1)\) variables, conditional on this edge-pair and route orientation. The reverse orientation is symmetric. The unconditional law conditioned on \(T\) is the explicit finite mixture with unnormalized weights \(d_i^2/4\) for same-edge cases and \(d_i d_j\) for unordered distinct-edge cases.

## Assumptions and scope

Edges are intervals identified **only at their two endpoints**. Distances and geodesics are intrinsic to the abstract compact length space; no Euclidean embedding, traffic dynamics, or edge capacity is assumed. Every \(d_i\) is strictly positive, so the shortest \(A\)-to-\(B\) edge is unique. Equality among the longer lengths is allowed. Endpoints are independent and uniform in total arclength; they are not chosen from the two graph vertices. Events of tied minimizing routes lie on finitely many line segments in products of edge coordinates and have probability zero. The result holds for every integer \(m\ge3\), with no asymptotic hypothesis.

## Proof

**1. Reduction to finitely many simple paths.** A positive-length minimizing path cannot revisit a vertex. If an endpoint lies in the interior of the shortest edge, a shortest path cannot traverse that edge completely: doing so would require first reaching an endpoint and then returning past an interior endpoint. For two points on any fixed longer edge, the only potentially shortest routes are their direct connecting subinterval and the two routes running out to opposite junctions and crossing the shortest edge. A route using any other full longer edge is strictly improved by substituting the unique shortest \(A\)-to-\(B\) edge. For points on distinct longer edges, the only candidates are the two same-junction routes via \(A\) or \(B\) and the two opposite-junction routes through the shortest edge. These observations also establish that complete traversal of a longer edge cannot occur on any minimizing path. The finitely many candidate lengths are distinct except on sets of planar measure zero.

**2. Same longer edge.** Choose an edge of length \(\ell_i\) and write endpoint coordinates \(x,y\in(0,\ell_i)\), measured from \(A\). For \(x<y\), the direct length is \(y-x\), while the shorter of the routes via opposite junctions has length \(x+a+\ell_i-y\). The latter is strictly shorter precisely when
\[
y-x>\frac{\ell_i+a}{2}.
\]
The set of such ordered coordinates is a right triangle of area \(d_i^2/8\); its reflected counterpart \(x>y\) has the same area. Thus this same-edge pair contributes exactly \(d_i^2/4\) to the unnormalized area of \(T\) in \(G\times G\). In the triangle \(x<y\), the change of variables \(u=x\), \(v=\ell_i-y\) identifies the event with \(u,v>0\) and \(u+v<d_i/2\), preserving Lebesgue measure. Uniformity on this triangle gives the stated Dirichlet law.

**3. Distinct longer edges.** For a point \(x\in(0,\ell_i)\) and a point \(y\in(0,\ell_j)\), \(i\ne j\), the four candidate lengths are
\[
x+y,\quad (\ell_i-x)+(\ell_j-y),\quad x+a+(\ell_j-y),\quad (\ell_i-x)+a+y.
\]
The third is strictly minimal if and only if
\[
0<x<\frac{d_i}{2},\qquad \frac{\ell_j+a}{2}<y<\ell_j.
\]
Indeed, these two inequalities are necessary and sufficient for the third candidate to beat the first two; they also force it to beat the fourth because \(2(x-y)<\ell_i-\ell_j-2a<\ell_i-\ell_j\). This rectangle has area \(d_i d_j/4\). The opposite route corresponds to a disjoint rectangle of the same area. Therefore each **ordered** pair of distinct longer edges contributes \(d_i d_j/2\), and the two orders together contribute \(d_i d_j\). The product-rectangle geometry gives the two independent uniform coordinates in the conditional statement.

**4. Integration.** Normalized product arclength on \(G\times G\) is the sum of Euclidean product areas divided by \(L^2\). Adding the disjoint same-edge triangles and distinct-edge rectangles gives
\[
L^2\mathbb P(T)=\sum_i\frac{d_i^2}{4}+\sum_{i<j}d_i d_j
=\frac{2S^2-\sum_i d_i^2}{4}.
\]
The mixture weights follow from these same areas. No contribution arises from pairs with an endpoint inside the shortest edge.

**5. Sharp extremal bounds.** For the \(m-1\) positive numbers \(d_i\) of fixed sum \(S>0\), Cauchy–Schwarz gives \(\sum_i d_i^2\ge S^2/(m-1)\), with equality exactly for equal \(d_i\). Also \(\sum_i d_i^2<S^2\) because there are at least two positive summands, while the supremum \(S^2\) is approached by concentrating their fixed sum in one coordinate. Substitution gives the stated strict lower bound, sharp upper bound, and equality characterization. Finally, at fixed \(m\), \(0<S/L=1-ma/L<1\), so the global supremum over lengths is the upper coefficient, approached as \(a/L\downarrow0\) and the other edges become equal.

## Verification

The accompanying standalone `verify.py` computes the claimed formula and independently enumerates the competing path lengths, rather than using the geometry of the proof. A midpoint-grid area quadrature and independently sampled arclength-uniform endpoint pairs test eight configurations of three through seven parallel edges, including strongly unequal lengths and nearly collapsed shortest edges. It also checks the sharp inequality and its equality cases. The script uses only Python's standard library and can be rerun with `python verify.py` from this package. The successful completion marker is `PARALLEL_GEODESIC_COMPLETE_EDGE_TRANSIT_CHECKS_OK 8`. Finite tests corroborate but do not prove the theorem; the proof above handles all positive admissible lengths and all integers \(m\ge3\).

## Relationship to prior work

Kennedy, Kurasov, Malenová and Mugnolo (2015) study metric graphs including *pumpkin* or dipole graphs, but their invariant is the Laplacian spectral gap, not the probability that two arclength-uniform points have a geodesic traversing an entire edge. Garijo, Márquez and Silveira (first circulated in 2021) give a general computational theory for the **mean distance** between points on metric graph edges, including shortest-path-cell decompositions. Their stated assumption that each edge itself realizes its endpoints’ intrinsic distance does not hold for the longer parallel edges considered here: their endpoints are only distance \(a\) apart, strictly less than the corresponding \(\ell_i\). Subdividing such edges can still make their general methodology relevant. Baptista, Kennedy and Mugnolo (first circulated in 2023) investigate average intrinsic distance and sharp geometric comparisons. Neither mean-distance invariant is a complete-edge transit indicator; their general cell methods are a relevant possible route to related formulas but the cited statements do not give the exact traffic formula, the sharp length-shape bounds, or the conditional Dirichlet/uniform laws. Durón, Kravitz and Brio (2025) define a distinct spectral-energy centrality for metric graphs, not the geodesic event studied here. Conventional finite-vertex edge betweenness likewise samples **vertices**, not arclength-uniform points. No implication from the examined statements supplies the full package of conclusions, but this comparison is not a certificate of historical uniqueness.

## Limitations

This is a complete result for a family with exactly two junction vertices and a **unique** shortest connecting edge. It does not address equal multiple shortest edges, general networks with intermediate junctions, or the probability that a geodesic uses merely a **part** of an edge. Prior computational partition methods may make some individual area formulas accessible by a different derivation; historical originality, especially of the scalar transit probability, remains provisional. No external independent proof audit has been performed.

## References

1. J. B. Kennedy, P. Kurasov, G. Malenová and D. Mugnolo, *On the spectral gap of a quantum graph*, arXiv:1504.01962, first posted 2015-04-08. https://arxiv.org/abs/1504.01962
2. D. Garijo, A. Márquez and R. I. Silveira, *Continuous mean distance of a weighted graph*, arXiv:2103.11676, first posted 2021-03-22; *Results in Mathematics* **78**, article 139 (2023). https://arxiv.org/abs/2103.11676
3. L. N. Baptista, J. B. Kennedy and D. Mugnolo, *Mean distance on metric graphs*, arXiv:2312.04952, first posted 2023-12-08; *Journal of Geometric Analysis* **34**, article 137 (2024). https://arxiv.org/abs/2312.04952
4. C. Durón, H. Kravitz and M. Brio, *Kolmogorov–Smirnov-Based Edge Centrality Measure for Metric Graphs*, *Dynamics* **5**, article 16 (2025). https://doi.org/10.3390/dynamics5020016
