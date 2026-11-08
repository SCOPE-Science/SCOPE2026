# Complete inverse classification from boundary-sampled polygon hull vertex counts

## Finding
Let \(Q\) be any strictly convex Euclidean polygon with \(m\ge3\) genuine sides of positive lengths \(\ell_i\), perimeter \(P\), and normalized side lengths \(p_i=\ell_i/P\). For each integer \(n\ge2\), choose \(n\) independent points uniformly by boundary arclength, and let \(V_n(Q)\) denote the number of extreme vertices of their convex hull (a nondegenerate segment has two). With \(N_i\) the number sampled on side \(i\), the **exact pathwise identity** is
\[
 V_n(Q)=\sum_{i=1}^m\min(N_i,2),\qquad (N_1,\ldots,N_m)\sim\operatorname{Multinomial}(n;p_1,\ldots,p_m).
\]
Consequently the complete probability-generating function for every \(n\ge2\) is
\[
 \mathbb E[t^{V_n(Q)}]=n![z^n]\prod_{i=1}^m\left[1+tp_i z+t^2(e^{p_i z}-1-p_i z)\right],
\]
and its exact mean is
\[
 \mu_n(Q)=\sum_{i=1}^m\left[2-2(1-p_i)^n-np_i(1-p_i)^{n-1}\right].
\]
**Complete inverse theorem.** For two such polygons, equality of \(\mu_n\) for every integer \(n\ge2\) holds **if and only if** their unordered multisets of normalized side lengths agree. The same equivalence holds for equality of the entire laws of \(V_n\) for all \(n\). Moreover the multiset and the number of sides have a constructive asymptotic recovery from the means. This implies an exact dimension threshold for congruence up to similarity: the data reconstruct every triangle, while for every \(m\ge4\) a positive-dimensional family of pairwise non-similar strictly convex equilateral \(m\)-gons has exactly the same data.

## Assumptions and scope
Sampling is independent, uniform with respect to Euclidean length on the entire polygon boundary; vertices have sampling probability zero. Each polygon is nondegenerate, with all interior angles strictly between zero and \(\pi\), and a finite number \(m\ge3\) of genuine sides. The data consist of exact population expectations at **all sample sizes**, not a finite set of noisy observations. The recovered lengths are normalized by perimeter; the absolute scale cannot be recovered. The claim includes triangles and all polygons with more sides, not arbitrary curved convex bodies, higher-dimensional polytopes, or nonuniform boundary sampling.

## Proof
**Supporting-edge reduction.** Every chosen point lies in the relative interior of a unique polygon edge almost surely. All chosen points on side \(i\) lie on its supporting line, while chosen points on other sides lie strictly in its interior half-plane. If the side is occupied once, its point is an extreme point; if it is occupied at least twice, exactly the two extremal sampled points along that side are extreme, and the others lie between them. There are no further extreme points. This remains correct when all chosen points occupy just one side, since their hull is a segment. Thus \(V_n=\sum_i\min(N_i,2)\). Boundary uniformity implies the stated multinomial distribution. The exponential generating function for one side is \(1+tp_i z+\sum_{k\ge2}t^2p_i^k z^k/k!\), and multiplying sides yields the law. Since each \(N_i\) is binomial with parameters \(n,p_i\), \(\mathbb E\min(N_i,2)=2-2(1-p_i)^n-np_i(1-p_i)^{n-1}\).

**Constructive inverse.** Since every \(p_i>0\), \(\mu_n\to2m\), hence \(m=\frac12\lim_{n\to\infty}\mu_n\) is recovered. Write \(q_i=1-p_i\in(0,1)\) and set
\[
 a_n=2m-\mu_n=\sum_i\left[2q_i^n+n(1-q_i)q_i^{n-1}\right].
\]
All summands are strictly positive. Let \(q_*\) be the largest \(q_i\), of multiplicity \(r\). Exponential separation of the finitely many distinct \(q_i\) gives
\[
 \lim_{n\to\infty}\frac{a_{n+1}}{a_n}=q_*,\qquad
 \lim_{n\to\infty}\frac{a_n}{nq_*^{n-1}}=r(1-q_*).
\]
Thus the limits determine \(q_*\) and its positive integer multiplicity \(r\). Subtract \(r[2q_*^n+n(1-q_*)q_*^{n-1}]\) from the sequence, and iterate over its finitely many remaining distinct positive roots. This recovers every \(p_i=1-q_i\), including repetitions. If all \(q_i\) coincide, the process terminates after one step. Conversely the generating function depends only on the unordered \(p_i\), so equal multisets imply all laws and means agree. Equality of all laws plainly implies equality of means.

**Sharp shape-identifiability threshold.** For \(m=3\), the unordered normalized side lengths determine a triangle up to Euclidean similarity by side-side-side. For \(m\ge4\), fix all side lengths to \(1/m\). Near the regular equilateral polygon write unit edge directions as angles \(\phi_1,\ldots,\phi_m\), fixing \(\phi_1=0\) to remove rotations. Closing the polygon imposes the two real equations \(\sum_i e^{i\phi_i}=0\). At the regular \(m\)-gon, their Jacobian with respect to \(\phi_2,\ldots,\phi_m\) has real rank two, because the remaining unit directions span the plane. The implicit-function theorem therefore gives a local smooth solution manifold of dimension \(m-3\ge1\). Strict convexity is open in these angle coordinates; restricting to sufficiently small perturbations gives an infinite family of strictly convex equilateral closed polygons. Only finitely many relabelings and reflections correspond to a fixed similarity class near a fixed normalized shape, so this manifold contains infinitely many pairwise non-similar polygons. All have the same \(p_i=1/m\) and hence identical distributions for all \(n\). For \(m=4\), ordinary equal-perimeter rhombi of varying angles give an explicit witness.

## Verification
The standalone `verify.py` independently computes the exact multinomial law at sixteen polygon/sample-size cases, checks each mean, and compares the pathwise occupancy formula with actual planar convex hulls for 10,000 independently generated samples spanning triangles, rectangles, slanted quadrilaterals, and pentagons. It also checks the predicted exponential inverse ratio for a positive five-weight profile. Execution: `python verify.py`; the recorded output is `VERIFY_OK polygons=4 exact_occupancy_mean_cases= 16 geometric_hull_trials= 10000 inverse_rate_cases=3 equal_side_rhombi=1`. These finite diagnostics do not establish the all-sample-size inverse, which follows from the displayed limits and positivity.

## Relationship to prior work
Har-Peled, arXiv:1111.5340, treats expected convex-hull complexity for **interior-uniform** points in convex polygons, not arclength-boundary sampling or inverse recovery of side-length profiles. Reitzner, Schütt and Werner, arXiv:1911.05917, examine boundary samples on general simple polytopes and derive asymptotic expected face numbers, rather than the exact two-dimensional all-sample-size vertex-count law and its inverse equivalence. Earlier work on the four-point hull-vertex law for **triangles** reconstructs normalized triangle sides from one finite probability distribution, and so establishes only the triangular special case of identifiability, not the arbitrary-side-count equivalence or sharp failure for every \(m\ge4\). Existing general occupancy and exponential-sum methods supply standard ingredients; priority is not claimed for either one separately. The contribution assessed here is their complete shape-quotient identification for boundary random hull counts across *all* convex polygons.

## Limitations
Recovery requires exact population means for infinitely many sample sizes, and repeated limit/subtraction is ill-conditioned under noise, particularly for side fractions close together. No finite-sample inverse stability or optimal finite set of observations is established. The observations do not recover perimeter, side order, vertex angles, or shape beyond triangles; indeed large equivalence classes for higher polygons are inevitable. Historical priority remains provisional, since complete coverage of older stochastic-geometry publications is difficult to exclude from negative searches.

## References
[1] S. Har-Peled, *On the Expected Complexity of Random Convex Hulls*, arXiv:1111.5340 (first posted 2011-11-22), https://arxiv.org/abs/1111.5340 .
[2] M. Reitzner, C. Schütt and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first posted 2019-11-14), https://arxiv.org/abs/1911.05917 .
[3] B. Efron, *The convex hull of a random set of points*, Biometrika 52 (1965), 331–343, https://doi.org/10.1093/biomet/52.3-4.331 .
