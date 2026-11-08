# An exact barycentric coverage profile and strict majorization law for side-sampled triangles

## Finding

For every nondegenerate Euclidean triangle \(T=\operatorname{conv}\{A,B,C\}\), choose independently one point from each of its three sides, uniformly with respect to normalized arclength on that side. Denote their convex hull by \(K\). If a fixed target \(P\in T\) has barycentric coordinates \(a,b,c\ge0\), \(a+b+c=1\), then the exact containment probability is
\[
\boxed{\Pr\{P\in K\}=\Phi(a,b,c):=\sum_{t\in\{a,b,c\}}t(1-t)\log\!\frac{1-t}{t}.}
\]
Here \(t(1-t)\log((1-t)/t)\) is defined to be zero at \(t=0,1\). The profile is independent of the shape and scale of \(T\), not just of its area. It vanishes everywhere on \(\partial T\), is positive in \(\operatorname{int}T\), and is **strictly Schur-concave on the open barycentric simplex**: if two positive barycentric triples \(u,v\) sum to one, \(u\) majorizes \(v\), and \(u\) is not a permutation of \(v\), then \(\Phi(u)<\Phi(v)\). Consequently the centroid is the unique maximizer and the exact attained range on the closed triangle is
\[
\boxed{0\le \Pr\{P\in K\}\le\frac{2}{3}\log2.}
\]
At a vertex, along barycentric rays \((1-\varepsilon,\varepsilon t,\varepsilon(1-t))\), the profile has the directional boundary law
\[
\Phi(1-\varepsilon,\varepsilon t,\varepsilon(1-t))
=\varepsilon[-t\log t-(1-t)\log(1-t)]
+O(\varepsilon^2|\log\varepsilon|),
\quad0\le t\le1,\quad\varepsilon\downarrow0,
\]
with the usual zero conventions and an error uniform in \(t\). If the target itself is independently area-uniform on \(T\), the probability of containment is exactly \(1/4\).

## Assumptions and scope

Every triangle is nondegenerate. Each of the three side selections is independent, with a continuous uniform *conditional* arclength distribution on its specified side; the side is selected once, deterministically, not randomly according to its length. The target is fixed independently of the side selections, and the event includes its boundary (irrelevant away from the fixed exterior boundary because degeneracies have probability zero). For the strict majorization statement all three barycentric entries are positive; on the closed simplex the profile is only Schur-concave, and the full geometric boundary has probability zero. No other distributional or noise model is assumed.

## Proof

**Affine reduction.** The unique affine map sending \(A,B,C\) to \((0,0),(1,0),(0,1)\) sends each uniform side point to a uniform side point because the restriction to a straight segment rescales arclength by a constant. It also preserves convex hulls, containment, and barycentric coordinates. Thus work on the reference triangle.

**Partition into corner triangles.** Write the three random points as \(U=(u,0)\) on \(AB\), \(V=(1-v,v)\) on \(BC\), and \(W=(0,w)\) on \(CA\), where \(u,v,w\) are independent uniform variables on \((0,1)\). Except at boundary coincidences of probability zero, \(T\) is partitioned (up to borders) into \(K\) and the three corner triangles \(\operatorname{conv}\{A,U,W\}\), \(\operatorname{conv}\{B,U,V\}\), \(\operatorname{conv}\{C,V,W\}\). For target \(P=(b,c)\), membership in the corner near \(A\) is exactly \(b/u+c/w\le1\) and depends only on \(u,w\). Writing \(a=1-b-c\), its probability equals
\[
\int_{b/(1-c)}^1\left(1-\frac{cu}{u-b}\right)\,du
=a-bc\log\frac{(a+b)(a+c)}{bc}.
\]
This holds for positive \(a,b,c\); the lower limit and integrand arise by solving \(w\ge cu/(u-b)\). Cyclically adding the three disjoint corner probabilities and subtracting from one yields
\[
\Phi(a,b,c)=\sum_{\mathrm{cyc}}bc\log\frac{(a+b)(a+c)}{bc}
=\sum_{t\in\{a,b,c\}}g(t),\quad
 g(t)=t(1-t)\log\frac{1-t}{t}.
\]
The second equality follows by grouping the logarithms involving each variable, since \(\sum_{s\ne t}s=1-t\). Continuity extends the formula to boundary triples. There, \(g(0)=g(1)=0\) and \(g(t)+g(1-t)=0\), so \(\Phi=0\).

**Strict balancing order.** Direct differentiation gives
\[
g'(t)=(1-2t)\log\frac{1-t}{t}-1,
\qquad g'(1-t)=g'(t),
\]
\[
g''(t)=-2\log\frac{1-t}{t}-\frac{1-2t}{t(1-t)}.
\]
Thus \(g'\) is strictly decreasing on \((0,1/2)\) and strictly increasing on \((1/2,1)\), by inspection of the two terms; its symmetry transfers both halves to the same decreasing function of \(\min\{t,1-t\}\). If \(0<a<b\) and \(a+b<1\), then \(a<\min\{b,1-b\}\), hence \(g'(a)>g'(b)\). Replacing \((a,b)\) by \((a+s,b-s)\) while \(0<s<(b-a)/2\) strictly increases \(\Phi\). By the finite-dimensional Hardy–Littlewood–Pólya pairwise-balancing characterization of majorization (or by successive pair balancing), any nontrivial majorization comparison between positive triples strictly increases the profile when balancing, proving strict Schur-concavity. Every interior triple is majorized by its permutations and majorizes \((1/3,1/3,1/3)\), so the centroid is uniquely optimal, at
\[
3g(1/3)=3\cdot\frac29\log2=\frac23\log2.
\]
Interior positivity follows also from the positive probability that all random side points lie sufficiently near their associated vertices, making \(K\) contain any prescribed interior point. The continuous image of the connected closed triangle contains every number between the boundary value zero and the centroid maximum.

**Further exact consequences.** The near-vertex expansion follows on inserting \((1-\varepsilon,\varepsilon t,\varepsilon(1-t))\) into the exact formula: the \(\varepsilon\log\varepsilon\) terms cancel, leaving binary entropy. Taylor remainders of \(x(1-x)\log((1-x)/x)\) show the stated bound uniformly for \(t\in[0,1]\). Finally, each corner triangle has expected area \(\operatorname{Area}(T)/4\): at \(A\) its area fraction is \(uw\), with \(u,w\) independent uniforms. The three corner triangles are disjoint, so \(\mathbb E\operatorname{Area}(K)=\operatorname{Area}(T)/4\). Fubini gives \(\mathbb E_{P\sim\mathrm{Unif}(T)}\Phi(P)=1/4\), independently confirming the integrated formula.

## Verification

`verify.py` runs exact symbolic derivative/integral checks, 40-digit independent one-corner numerical quadrature in four nonidentical triples, 18,000 positive barycentric balancing tests, 201 boundary checks, and a direct independent affine-coordinate Monte Carlo experiment with 480,000 random triangles at seven target positions in a scalene image of the reference triangle. It also tests the near-vertex binary-entropy coefficient. The successful run reports `VERIFY_OK`; these finite checks support, but do not replace, the proof for all triangles and all targets.

## Relationship to prior work

The 2014 public problem and solution by Dmitri Kovalenko and achille hui compute the equilateral-centroid containment probability \(\log4/3\) for exactly one independent uniform point on each side, using a corner-triangle integration. This value is **not** new and is recovered as \(\Phi(1/3,1/3,1/3)\). What is established here is the **whole affine-invariant target-location profile** for arbitrary triangles, the **strict majorization comparison** for any two interior targets, and the directional vertex-entropy law. A separate earlier analysis of triples sampled independently from an entire triangle perimeter studies how centroid coverage varies with side-selection probabilities; that problem holds the target fixed and varies the sampling measure, whereas the present theorem fixes one point per side and varies the target. Earlier studies of three points drawn from a polygon perimeter without side conditioning, and of three points drawn from a planar region by area, are different sampling experiments. Searches did not identify a statement giving this complete strict target-location ordering, but absence of a search hit is not a mathematical priority proof.

## Limitations

No claim is made about selecting sides randomly by perimeter weights, about general convex bodies or polygons, or about targets drawn from nonuniform distributions. The strict order does not extend to distinct boundary points, whose probabilities are all zero; likewise, a coordinatewise majorization comparison must use **barycentric** coordinates and cannot be replaced by a claim about Euclidean radial distance. The exact population probability need not be estimable stably from finitely many triangles near a vertex, and no statistical confidence guarantees are supplied. The classical centroid value and the corner-partition method are explicitly prior work. Independent validation and exhaustive historical-priority verification have not been performed.

## References

- D. Kovalenko, question (26 November 2014), and achille hui, solution (29 November 2014), *Find probability that random triangle covers centre of circumscribed circle*, Mathematics Stack Exchange. https://math.stackexchange.com/questions/1040314/find-probability-that-random-triangle-covers-centre-of-circumscribed-circle
- A. Pretorius and responses, *Probability of random points on perimeter containing center* (question 18 July 2012), Mathematics Stack Exchange. Different perimeter-uniform sampling without one-point-per-side conditioning. https://math.stackexchange.com/questions/172296/probabilty-of-random-points-on-perimeter-containing-center
- E. J. Ionaşcu, *Random triangles in planar regions containing a fixed point*, arXiv:1612.08619, first submitted 15 December 2016. Different area-uniform point sampling; cited for methodological context, not as the archive focal source. https://arxiv.org/abs/1612.08619
