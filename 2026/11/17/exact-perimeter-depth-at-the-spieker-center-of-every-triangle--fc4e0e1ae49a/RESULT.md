# Exact perimeter depth at the Spieker center of every triangle

## Finding
Let \(T\) be any nondegenerate Euclidean triangle with sorted side lengths \(a\ge b\ge c>0\), perimeter \(P=a+b+c\), and Spieker point \(S\), defined as the center of mass of uniform arclength on \(\partial T\). Define the normalized arclength halfplane depth
\[
\delta_{\partial T}(S)=\frac1P\inf_{\ell\ni S}\min\{\operatorname{length}(\partial T\cap H^+_\ell),\operatorname{length}(\partial T\cap H^-_\ell)\},
\]
where \(H^+_\ell,H^-_\ell\) are the closed halfplanes bounded by \(\ell\), and boundary points on \(\ell\) have zero arclength mass.

Put \(Q=b(a+b)(a+c)-c(P+b)^2\). Then the *complete exact profile* is
\[
\boxed{\delta_{\partial T}(S)=
\begin{cases}
\dfrac{\bigl(\sqrt{c(a+c)}+\sqrt{b(a+b)}\bigr)^2}{2P^2},&Q\le 0,\\[5pt]
\dfrac{b+c}{P+b},&Q>0.
\end{cases}}
\]
A minimizing chord can always be chosen to cut off the vertex opposite a longest side. In the first branch it is the unique minimum-intercept chord across the two adjacent sides (unless vertex choices tie by symmetry); in the second it passes through the endpoint of the shorter adjacent side.

In every nondegenerate triangle,
\[
\boxed{\delta_{\partial T}(S)>\frac13.}
\]
The constant is optimal, not attained: for side lengths \((a,b,c)=(1,1,\varepsilon)\), \(\varepsilon\downarrow0\), the depth tends to \(1/3\). The equilateral value is \(4/9\). The guaranteed \(1/3\) for this explicit canonical center improves on the sharp \(3/10\) worst-case perimeter depth of the **area** centroid established in the motivating literature; no assertion that the Spieker point globally maximizes depth is made.

## Assumptions and scope
The triangle is Euclidean, noncollinear, and its boundary carries normalized arclength rather than area or vertex-count measure. All three side lengths are strictly positive and satisfy the strict triangle inequalities. Ties in ordered side lengths are allowed, and all branch inequalities include the equality case. The Spieker point is interior because it is a positive barycentric combination of the vertices.

## Proof
**1. A vertex-arc reduction.** Fix any interior point \(Z\). If a chord \(MN\) through \(Z\) cuts the sides incident with a vertex \(A\) at distances \(u,v\) from \(A\), and \(Z=x\mathbf e_1+y\mathbf e_2\) in unit edge directions, then \(x/u+y/v=1\) and the boundary arc around \(A\) has length \(u+v\). Solving for \(v\) gives the strictly convex function \(f(u)=u+Yu/(u-X)\), where \(X=x,Y=y>0\). Its unconstrained minimum occurs at \(u=X+\sqrt{XY}\), \(v=Y+\sqrt{XY}\), with value \((\sqrt X+\sqrt Y)^2\). Within the actual side segments, either this point or an endpoint of the allowable interval minimizes the one-vertex arc. Any **two-vertex** arc is the complement of a one-vertex arc along the same pencil; minimizing the former maximizes this strictly convex function on an interval and therefore occurs at an endpoint chord through a triangle vertex. That chord is also a limiting one-vertex arc at another vertex. Hence the smallest boundary arc cut by a line through \(Z\) is the minimum over the three vertex-arc minima. This is the W-line/cevian reduction, also used for the area centroid in Berele--Catoiu (2026), Lemmas 2--3.

**2. Exact side-pair formula.** The arclength center of mass is
\[
S=\frac{a(B+C)+b(C+A)+c(A+B)}{2P},
\]
so its barycentric weights at \(A,B,C\) are \((b+c)/(2P),(a+c)/(2P),(a+b)/(2P)\). At the vertex \(A\), whose two adjacent side lengths are \(b,c\), put
\[
X=\frac{c(a+c)}{2P},\qquad Y=\frac{b(a+b)}{2P}.
\]
Since \(b\ge c\), one has \(0<X<c/2\), \(0<Y<b/2\), and \(\sqrt{XY}<b/2\). Thus the unconstrained intercept on the length-\(b\) edge always fits; only the length-\(c\) intercept can fail. The first branch is feasible precisely when \(X+\sqrt{XY}\le c\), equivalent, by squaring two nonnegative sides, to \(Q\le0\). Otherwise the minimizing chord has intercept \(u=c\), and the second intercept is \(v=Y/(1-X/c)=b(a+b)/(P+b)\). The resulting length is
\[
c+v=\frac{P(b+c)}{P+b}.
\]
Dividing by \(P\) gives both asserted branches.

**3. Why the longest-side vertex controls.** At fixed perimeter \(P\), write \(W_P(u,v)=(\sqrt{v(P-u)}+\sqrt{u(P-v)})^2/(2P)\), and \(E_P(u,v)=P(u+v)/(P+u)\) for \(u\ge v>0\), \(u+v<P\). Each expression is strictly increasing in each argument: for example the derivative of the unsquared sum in \(W_P\) with respect to \(u\) is positive exactly when \((P-u)(P-v)>uv\), which is the condition \(P>u+v\); for the endpoint expression its two partial derivatives are \(P(P-v)/(P+u)^2\) and \(P/(P+u)\). The piecewise minimum-intercept function uses these branches and is continuous at their switching boundary, so it is increasing in both adjacent side lengths. Hence \((b,c)\preceq(a,c)\preceq(a,b)\) implies that the smallest of the three vertex-arc minima is the one opposite \(a\). This confirms that the side-pair expression from Step 2 is the global depth.

**4. Sharp lower bound, endpoint branch.** If \(Q>0\), then
\[
\frac{b+c}{P+b}>\frac13
\quad\Longleftrightarrow\quad b+2c>a.
\]
The last condition follows strictly from \(a<b+c\) and \(c>0\).

**5. Sharp lower bound, internal W-line branch.** Suppose \(Q\le0\), put \(t=b/c\ge1\). For fixed \(b,c\), the W-line ratio
\[
\frac{(\sqrt{c(a+c)}+\sqrt{b(a+b)})^2}{2(a+b+c)^2}
\]
decreases as \(a\) increases through \(a\ge b\): each summand \(\sqrt{c(a+c)}/(a+b+c)\) and \(\sqrt{b(a+b)}/(a+b+c)\) is decreasing since their derivative numerators are respectively \(b-c-a<0\) and \(c-b-a<0\). Since \(a<b+c\), the ratio is strictly larger than its formal flattened-triangle value
\[
G(t)=\frac{(\sqrt{t+2}+\sqrt{t(2t+1)})^2}{8(t+1)^2}.
\]
Feasibility \(X+\sqrt{XY}\le c\) forces \(t\le2+\sqrt5\). To verify this, at fixed \(b,c\), the normalized short-edge intercept \((X+\sqrt{XY})/c\) increases with \(a\): the derivative of \((a+c)/(a+b+c)\) is positive, and the derivative of \(\sqrt{(a+c)(a+b)}/(a+b+c)\) has the positive numerator \(a(b+c)+b^2+c^2\). Evaluate the intercept at the smallest allowed \(a=b\); its feasibility implies \(2t^3-7t^2-6t-1\le0\), which factors as
\[
2(t+\tfrac12)(t-(2+\sqrt5))(t-(2-\sqrt5))\le0.
\]
Thus \(1\le t\le2+\sqrt5<5+2\sqrt6\). Now \(G(t)\ge1/3\) is equivalent (both sides before squaring are nonnegative) to
\[
9t(t+2)(2t+1)-(t^2+5t+1)^2
=-(t+1)^2(t^2-10t+1)\ge0,
\]
which holds for \(5-2\sqrt6\le t\le5+2\sqrt6\); our feasible interval lies strictly inside this range. Hence \(G(t)>1/3\), proving the strict bound also in the W-line branch.

**6. Sharpness.** In the legitimate nondegenerate family \((a,b,c)=(1,1,\varepsilon)\), with \(0<\varepsilon<1\) and \(\varepsilon\to0\), the endpoint branch applies for sufficiently small \(\varepsilon\), giving \(\delta=(1+\varepsilon)/(3+\varepsilon)\to1/3\). At \(a=b=c\) the W-line branch gives \(4/9\).

## Verification
Run `python3 verify.py` using Python 3's standard library. Its independent algorithm constructs the Euclidean triangle from side lengths, computes the arclength center by edge-midpoint weights, enumerates actual line--side intersections for densely spaced line directions, and compares measured minimum cut fractions to the closed formula. It also checks 6,000 deterministic random valid triangles against the strict bound, both formula branches, and the limiting sharp family. The run completed successfully, including nine independent angular tests. These finite checks corroborate the algebra and do not replace the global proof above.

## Relationship to prior work
Berele--Catoiu (2026) determines the perimeter Winternitz profile at the **area centroid**, including its sharp \(3/10\) infimum, and provides the general W-line reduction used here. Amadtohed--Chaidee--Racha-in--Theerakarn (2022) describes envelopes of lines cutting the perimeter of a fixed triangle into prescribed proportions, giving a broader geometric framework from which one may in principle derive point-specific inequalities through additional minimization. Neither inspected article states the exact two-branch Spieker-center formula or its sharp shape-uniform \(1/3\) guarantee. The classical centerpoint theorem guarantees the existence of some point of depth at least \(1/3\); the present statement identifies a fixed, constructible triangle center achieving that guarantee for the boundary measure, with its exact depth for every shape.

## Limitations
The theorem is confined to the arclength-weighted boundary of nondegenerate Euclidean triangles. It does not assert that the Spieker point is the global deepest point, does not extend the same bound to all convex bodies, and does not address area measure. The formula can be derived algorithmically from older general envelope descriptions, so historical priority of its explicit sharp simplification warrants further literature review. No independent audit has been performed.

## References
- A. Berele and S. Catoiu, *The Perimeter Winternitz Theorem in a Triangle*, arXiv:2603.23653, submitted March 24, 2026. https://arxiv.org/abs/2603.23653
- N. Amadtohed, T. Chaidee, P. Racha-in and T. Theerakarn, *Dividing the Perimeter of a Triangle into Unequal Proportions*, International Journal of Mathematics and Mathematical Sciences (2022), article 2751666. https://doi.org/10.1155/2022/2751666
- Classical Spieker center (wire-frame perimeter centroid), https://en.wikipedia.org/wiki/Spieker_center (definition only).
