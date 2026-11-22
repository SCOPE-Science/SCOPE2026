# Sharp asymmetry-conditioned Wigner-caustic spectrum of parallel-opposite hexagons

## Finding

Let \(P\subset\mathbb R^2\) be a strictly convex hexagon with three pairs of parallel opposite edges. Let its Minkowski asymmetry, difference-body area ratio, and normalized absolute oriented Wigner-caustic area be
\[
s=s(P)=\min_{o\in\mathbb R^2}\min\{\lambda\ge1:-(P-o)\subseteq\lambda(P-o)\},\qquad
\mathcal R(P)=\frac{A(P-P)}{A(P)},\qquad
\mathcal W(P)=\frac{|A^*(E_{1/2}(P))|}{A(P)}.
\]
Here \(E_{1/2}(P)\) is the closed triangle of midpoints of corresponding opposite vertices, and \(A^*\) is oriented shoelace area. For every \(1<s<2\), the **complete fixed-asymmetry spectra** are
\[
\boxed{\frac{2(s+1)^2}{4s-s^2-1}\le\mathcal R(P)<\frac{2(5-s)}{3-s}},
\qquad
\boxed{\frac{3(s-1)^2}{4(4s-s^2-1)}\le\mathcal W(P)<\frac{s-1}{4(3-s)}}.
\]
Every value in both respective half-open intervals is realized by a genuine strictly convex parallel-opposite hexagon with that same asymmetry; the two invariants obey \(\mathcal R(P)=4+8\mathcal W(P)\). The lower endpoints are attained exactly by the affine threefold-rotationally symmetric members of this class; the upper endpoints are strict, approached only when the normalized hexagon degenerates toward a trapezoid, up to cyclic relabeling. When \(s=1\), central symmetry forces \(\mathcal R=4\) and \(\mathcal W=0\).

There is also an exact stability identity. With the positive-asymmetry normalization \(t>0\) given below, set \(x=a/t\), \(y=(b-t)/t\), \(z=c/t\), and \(U=x+y+z=(2-s)/(s-1)\). Then
\[
\boxed{\frac1{\mathcal R_{\min}(s)-4}-\frac1{\mathcal R(P)-4}
=\frac12\left[(x-U/3)^2+(y-U/3)^2+(z-U/3)^2\right] .}
\]
This is an exact affine-normalized variance formula, not merely a qualitative equality statement.

## Assumptions and scope

Every strictly convex hexagon with parallel opposite edges has, up to invertible affine transformation, translation and cyclic labeling, successive edge vectors
\[
(a,0),\ (0,b),\ (-c,c),\ (-(a+t),0),\ (0,-(b-t)),\ (c+t,-(c+t)),
\]
where \(a,b,c>0\) and \(a+t,b-t,c+t>0\). This is obtained by positively scaling the first three edge rays so the middle ray is the sum of the first and third, and using closure. Its successive vertices, based at the origin, are
\[
(0,0),\ (a,0),\ (a,b),\ (a-c,b+c),\ (-c-t,b+c),\ (-c-t,c+t).
\]
The invariant \(s\) is the genuine Minkowski homothetic-containment asymmetry, not the affine-reflection energy introduced in related work. The known exact identity for this normalized class is
\[
s(P)=\max\left\{\frac{a+b+c+t}{a+b+c},\frac{a+b+c}{a+b+c+t}\right\};
\]
this preceding asymmetry formula is explicitly credited, not claimed as new. If \(t<0\), start the cyclic labeling at the fourth edge and apply a central inversion to replace \(t\) by \(-t>0\). Thus \(t>0\) suffices for noncentrally symmetric shapes. The equality classification is up to affine equivalence and cyclic labeling, not Euclidean congruence.

## Proof

**1. A direct primal–difference-body identity.** Shoelace computation on the displayed vertices gives
\[
A(P)=ab+ac+bc+bt-\frac{t^2}{2}.
\]
Alternatively, for \(t>0\) let \(x=a/t\), \(y=(b-t)/t\), \(z=c/t\); then
\[
\frac{A(P)}{t^2}=\frac12+x+y+z+xy+xz+yz=:B(x,y,z).
\]
The successive edge vectors of \(P-P\) are twice the half-differences of paired edges, namely
\[
(2a+t,0),\ (0,2b-t),\ (-2c-t,2c+t),
\]
followed by their negatives. They occur in cyclic order and exhaust the boundary of the central symmetral scaled by two, because each difference-body supporting edge has the sum of the corresponding opposite-edge lengths. Direct shoelace summation, or expansion of these three generators, yields the **exact identity**
\[
\boxed{A(P-P)=4A(P)+t^2.}
\]
For an independent geometric check, the midpoint triangle with vertices \(M_j=(P_j+P_{j+3})/2\), \(j=0,1,2\), has successive edges \((-t/2,0)\), \((0,t/2)\), \((t/2,-t/2)\), hence oriented area \(-t^2/8\). Therefore
\[
\mathcal W(P)=\frac{t^2}{8A(P)},\qquad \mathcal R(P)=4+\frac{t^2}{A(P)}=4+8\mathcal W(P).
\]
This also recovers the established general Wigner-caustic/central-symmetral area identity in this six-sided case.

**2. Fixing asymmetry.** The quoted exact containment formula gives, for \(t>0\),
\[
s=\frac{a+b+c+t}{a+b+c}=\frac{U+2}{U+1},\qquad U=x+y+z=\frac{2-s}{s-1}>0.
\]
Since the three variables are all strictly positive with fixed sum \(U\), the elementary variance identity is
\[
xy+xz+yz=\frac{U^2}{3}-\frac12\sum_{q\in\{x,y,z\}}(q-U/3)^2.
\]
Consequently
\[
\frac12+U<B(x,y,z)\le\frac12+U+\frac{U^2}{3}.
\]
The upper bound is attained precisely when \(x=y=z=U/3\). The lower bound is strict because \(xy+xz+yz>0\), but is approached by triples such as \((U-2\varepsilon,\varepsilon,\varepsilon)\) for \(\varepsilon\downarrow0\). Since \(\mathcal R=4+1/B\), reversing the inequalities and substituting \(U=(2-s)/(s-1)\) gives exactly
\[
\frac{2(s+1)^2}{4s-s^2-1}\le\mathcal R(P)<\frac{2(5-s)}{3-s}.
\]
Subtracting \(4\) and dividing by \(8\) gives the paired caustic interval. Every intermediate value is realized: the strictly positive simplex \(x+y+z=U\) is connected, \(B\) is continuous, and along the segment joining \((U/3,U/3,U/3)\) to \((U-2\varepsilon,\varepsilon,\varepsilon)\), its values cover the intermediate range. Sending \(\varepsilon\) to zero reaches all values strictly below the excluded endpoint.

**3. Rigidity and exact stability.** Equality at the attained endpoint forces \(x=y=z\). The alternating edge lengths in the normalized three directional classes then repeat under an affine transformation of order three, so this is the unique balanced threefold-symmetric class at fixed \(s\). The strict opposite endpoint requires two positive coordinates to vanish; it corresponds to a limiting trapezoid, not a strictly convex hexagon. Finally
\[
\frac1{\mathcal R_{\min}(s)-4}=\frac12+U+\frac{U^2}{3},\quad
\frac1{\mathcal R(P)-4}=B(x,y,z),
\]
and their difference equals the displayed half-variance exactly. If \(t=0\), the opposite edges have equal lengths and the hexagon is centrally symmetric, giving \(s=1\), \(\mathcal W=0\), \(\mathcal R=4\). The known full range \(1\le s<2\) supplies the claimed fixed-parameter domain. \(\square\)

## Verification

Run `python verify.py` with Python 3.9 or newer; no nonstandard packages are required. The test constructs both the input polygon and the hull of all 36 pairwise vertex differences independently with exact fractions; it independently computes the three-vertex Wigner-caustic area, checks the difference-area identity, both sharp bounds, and the exact variance stability identity in 964 valid rational normal-form configurations of both signs of \(t\). It also verifies balanced extremizers and sequences tending to the strict endpoint. Expected output: `VERIFY_OK 964 exact-rational polygon hull/profile cases`. These computations test algebra and conventions but are not an exhaustive search over real parameters; the analytic proof establishes the universal theorem.

## Relationship to prior work

Giblin, Janeczko and Zwierzyński (first public preprint 27 August 2026), *Affine reflection transforms of convex polygons with parallel opposite sides*, Theorem 7.1, invoke the difference-body area to bound their affine-reflection energy but do not impose fixed Minkowski asymmetry or determine its sharp difference-body spectrum. Konicer and coauthors (arXiv:2606.22612v1), Theorem 4.7 and Equation (4.8), derive the general Wigner-caustic/central-symmetral area relation and a sharp \(1/4\) universal upper ratio for CPPOS polygons, without a fixed-asymmetry classification. A prior published mathematical finding, *Exact Minkowski asymmetry and unique critical point of parallel-opposite hexagons*, proves the **asymmetry formula used as an input**. The present contribution is conditional optimization of the separate area invariants at every prescribed asymmetry, including the complete interval, distinct equality mechanisms, and exact variance stability. The older Craizer–Teixeira–da Silva paper develops the area-evolute class but does not provide this fixed-s profile. Published results for equiangular constant-width octagons, decagons and dodecagons optimize different constrained families and do not cover six-sided fixed-asymmetry polygons. General Rogers–Shephard bounds alone give only \(4\le\mathcal R<6\) with no conditional refinement.

## Limitations

The classification concerns genuine strictly convex **six-sided** polygons with parallel corresponding opposite sides. It is not a general planar fixed-asymmetry inequality, nor a result for arbitrary CPPOS with eight or more vertices. The upper extremum is a nonattained limit and the variance normalization depends on choosing affine edge directions; the numerical variance is not a Euclidean metric invariant. Existing exact asymmetry and Wigner/symmetral identities are not newly proved contributions. No independent mathematical audit has been performed, and equivalent results in unindexed or inaccessible literature cannot be excluded with certainty.

## References

1. P. Giblin, S. Janeczko, M. Zwierzyński, *Affine reflection transforms of convex polygons with parallel opposite sides*, arXiv:2609.27931v1 (first public 27 August 2026), revised v2 29 October 2026, especially Theorem 7.1. https://arxiv.org/abs/2609.27931
2. I. Konicer, B. Murawski, B. Rogala, T. Wieczorek, M. Zwierzyński, *Convex Polygons with Parallel Opposite Sides: Convergence, Reconstruction, and Isoperimetric Inequalities*, arXiv:2606.22612v1, 21 June 2026, Theorem 4.7 and Equation (4.8). https://arxiv.org/abs/2606.22612
3. M. Craizer, R. C. Teixeira, M. A. H. B. da Silva, *Polygons with Parallel Opposite Sides*, Discrete Comput. Geom. 50 (2013), 474–490; arXiv:1210.2442. https://arxiv.org/abs/1210.2442
4. *Exact Minkowski asymmetry and unique critical point of parallel-opposite hexagons*, published mathematical finding, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-minkowski-asymmetry-and-unique-critical-point-of-parallel--4f2410956682
5. C. A. Rogers, G. C. Shephard, *The difference body of a convex body*, Arch. Math. 8 (1957), 220–233, DOI:10.1007/BF01899997.
