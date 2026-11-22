# Exact slimness and a contact transition for compact regular hyperbolic polygons

## Finding
Let \(n\ge 3\) be an integer and \(R>0\). Let \(P_{n,R}\) be the geodesically convex regular \(n\)-gon in the hyperbolic plane of sectional curvature \(-1\), with all vertices at hyperbolic distance \(R\) from its center. Define its *side slimness* by
\[
\delta(P_{n,R})=\max_{0\le j<n}\max_{x\in S_j}d_{\mathbb H^2}\!\left(x,\bigcup_{i\ne j}S_i\right),
\]
where \(S_0,\ldots,S_{n-1}\) are the closed geodesic side segments.

Put \(a=\pi/n\), \(s=\sin a\), \(c=\cos a\), and
\[
B=s\sinh R,\qquad
T=\frac{2cs^2\sinh R\cosh R}{1+s^2\sinh^2 R}.
\]
Then the exact formula, for every indicated \(n,R\), is
\[
\boxed{\delta(P_{n,R})=\begin{cases}
\operatorname{arsinh} B,&n\ge5\ \text{and}\ 0<R\le R_n,\\
\operatorname{arsinh} T,&n\in\{3,4\}\ \text{or}\ R\ge R_n,
\end{cases}\qquad R_n=\operatorname{arcosh}(\cot(\pi/n))\quad(n\ge5).}
\]
At \(R=R_n\) the two branches agree. On each side the unique farthest point from the other sides is the side midpoint. For \(n\ge5\), at \(R<R_n\) its nearest points on the other sides are the two adjacent vertices; at \(R=R_n\) the perpendicular feet first reach these vertices; at \(R>R_n\) the nearest points are two interior perpendicular feet on the adjacent sides. For \(n=3,4\), the perpendicular feet are interior for every \(R>0\).

For each fixed \(n\), the slimness is strictly increasing in \(R\), tends to its ideal-polygon value \(\operatorname{arsinh}(2\cos(\pi/n))\), and has the explicit endpoint approach
\[
\operatorname{arsinh}(2c)-\delta(P_{n,R})
=\frac{4c(2/s^2-1)}{\sqrt{1+4c^2}}e^{-2R}+O_n(e^{-4R}).
\]
For every \(n\ge5\), the function of \(R\) is \(C^1\) but not \(C^2\) at \(R_n\). In the convention \(\delta''(R_n+)-\delta''(R_n-)\), its exact second-derivative jump is
\[
\boxed{-\frac{\cos^{3/2}(2\pi/n)}{\sqrt2\cos^3(\pi/n)}<0.}
\]

## Assumptions and scope
All distances are intrinsic hyperbolic geodesic distances in the ambient curvature-\(-1\) plane. The sides are **finite geodesic segments**, not their complete supporting lines. The radius \(R\) is the vertex circumradius (not the inradius or Euclidean coordinate radius). No condition that the regular polygon tile the plane is imposed. The claim is restricted to the regular convex family; it does not assert a universal sharp slimness bound among all geodesic polygons.

## Proof
**1. Hyperbolic regular-polygon data.** Let \(O\) be the center, \(M\) the midpoint of a fixed side \(AB\), \(r=d(O,M)\), \(L=d(A,B)\), and \(\theta\) the common polygon interior angle. The right hyperbolic triangle \(OMA\) has central angle \(a\), vertex angle \(\theta/2\), and hypotenuse \(R\). Its sine and angle identities give
\[
\sinh(L/2)=\sinh R\sin a=B,
\qquad \tan(\theta/2)=\frac{\cot a}{\cosh R},
\qquad \tanh r=\cos a\tanh R.
\]
In particular, \(\theta\) strictly decreases from \(\pi-2a\) to zero as \(R\) increases. The inequality \(\theta\ge\pi/2\) is possible only when \(n\ge5\), and is then equivalent to \(R\le R_n=\operatorname{arcosh}(\cot a)\).

**2. Every side midpoint is closest to adjacent sides, not nonadjacent ones.** Use hyperbolic polar coordinates \((q,\beta)\) centered at \(O\), with \(M\) at angle zero. The support line of the side with normal direction \(\phi=2ja\) meets radial rays according to
\[
\tanh q\,\cos(\beta-2ja)=\tanh r.
\]
Within each finite side, \(u=\beta-2ja\) runs through \([-a,a]\); hence its radial distance \(q=q(u)\) is the same across all rotated sides. Any point of a nonadjacent side can, after reflection to the angular half-plane \(0\le\beta\le\pi\), be matched with a point on one of the two adjacent sides having exactly the same radial distance \(q\) and no larger (generically smaller) absolute angular separation from \(M\). This follows from the disjoint cyclic angle intervals \([(2j-1)a,(2j+1)a]\): the adjacent intervals start at \(a\), while nonadjacent intervals start at \(3a\). For the matched pair, the hyperbolic cosine law
\[
\cosh d(M,Q)=\cosh r\cosh q-\sinh r\sinh q\cos\beta
\]
shows the adjacent point is no farther from \(M\). Therefore the distance from \(M\) to the union of all other side segments is already the distance to the union of its two adjacent side segments. For a triangle all remaining sides are adjacent, so the conclusion is immediate.

**3. The midpoint uniquely maximizes the distance.** Parametrize the fixed side by arclength \(u\in[0,L]\) measured from vertex \(A\). Let \(f(u)\) be the distance to the adjacent side issuing from \(A\). If \(\theta\ge\pi/2\), the nearest adjacent-side point is \(A\), so \(f(u)=u\). If \(\theta<\pi/2\), the perpendicular foot lies in that adjacent finite side, because its distance \(v\) along that side from \(A\) satisfies \(\tanh v=\tanh u\cos\theta\), whence \(0<v<u\le L\). The right-triangle sine formula yields
\[
f(u)=\operatorname{arsinh}(\sinh u\sin\theta).
\]
In either case \(f\) is strictly increasing. Reflection interchanges the two neighboring sides, so the distance from the point at arclength \(u\) to the union of the neighboring sides is \(\min\{f(u),f(L-u)\}\), uniquely maximized at \(u=L/2\). Its distance to all other sides is bounded above by this quantity and equals it at the midpoint by Step 2. Hence precisely the side midpoint realizes the slimness on every side.

**4. Piecewise formula and transition.** At the midpoint, \(f(L/2)=\operatorname{arsinh}B\) in the obtuse/right-angle regime and \(\operatorname{arsinh}(B\sin\theta)\) in the acute regime. From \(\tan(\theta/2)=c/(s\cosh R)\),
\[
\sin\theta=\frac{2cs\cosh R}{1+s^2\sinh^2R},
\qquad B\sin\theta=T.
\]
This proves both branches and the threshold. The two adjacent vertices or the two interior feet are the only nearest-side contacts: on each adjacent segment, the perpendicular-distance minimizer is unique, and Step 2 excludes any strictly nonadjacent contact except a vertex shared with an adjacent side.

**5. Monotonicity, curvature kink, and ideal limit.** The first branch increases strictly. On the second branch put \(y=\sinh^2 R\); then \(T=2cs^2\sqrt{y(1+y)}/(1+s^2y)\), and
\[
\frac{d}{dy}\log T=\frac{1+(2-s^2)y}{2y(1+y)(1+s^2y)}>0.
\]
At \(R_n\), \(\sin\theta=1\), \(B=\sqrt{\cos(2a)}\), \(\cosh(L/2)=\sqrt2c\), and differentiation of the angle formula gives \(\theta'(R_n)=-\tanh R_n=-\sqrt{\cos(2a)}/c\). Thus the first derivatives of the two branches match, while their second-derivative difference is
\[
-\frac{B\,\theta'(R_n)^2}{\sqrt{1+B^2}}
=-\frac{\cos^{3/2}(2a)}{\sqrt2c^3}.
\]
Finally, \(T\to 2c\) as \(R\to\infty\); expansion in \(y^{-1}=4e^{-2R}+O(e^{-4R})\) gives the displayed sharp approach coefficient. These arguments hold for every fixed integer \(n\ge3\) and all positive radii.

## Verification
The accompanying Python 3 program `verify.py` (standard library only) computes distances in the hyperboloid model, minimizing along **each target geodesic side exactly in one variable** rather than using the proposed side-distance formula. It samples arclength points on every tested polygon edge, checks the predicted maximum and midpoint, tests branch continuity at the critical radii, and checks the ideal limiting coefficient. `python3 verify.py` returned `PASS: 169 hyperboloid endpoint, interior projection, threshold, and limit checks`. The finite sample checks are corroboration, not a substitute for the preceding proof or an exhaustive proof for all \(n,R\).

## Relationship to prior work
Tselekidis (2026) supplies the definition of geodesic polygon slimness and proves qualitative large-scale theorems for all polygons in certain unbounded metric spaces/graphs. It does not calculate the exact slimness of compact regular polygons in the hyperbolic plane. Lassak (2024) and Sagmeister (2025) study the distinct invariants of width, thickness, perimeter, diameter, and circumradius of hyperbolic polygons; their statements do not determine the distance from an edge point to the other edge segments. The ideal regular-polygon endpoint \(\operatorname{arsinh}(2\cos(\pi/n))\) is treated as background; the new mathematical content is the finite-radius formula, global midpoint and nearest-contact classification, transition, and sharp approach.

## Limitations
The theorem concerns convex regular polygons in curvature \(-1\); it does not cover arbitrary irregular polygons, variable curvature, or graphs. It characterizes geodesic *side slimness*, which is different from Lassak thickness or a four-point Gromov hyperbolicity constant. The literature comparison gives a best-knowledge originality assessment, not proof of historical priority. Independent external mathematical audit has not been performed.

## References
1. P. Tselekidis, *Logarithmically Slim Polygons*, arXiv:2611.05429v1, publicly submitted 2026-11-03, https://arxiv.org/html/2611.05429v1 .
2. M. Lassak, *Reduced polygons in the hyperbolic plane*, Archiv der Mathematik 123 (2024), 329–337, https://doi.org/10.1007/s00013-024-02009-6 .
3. Á. Sagmeister, *On the perimeter, diameter and circumradius of ordinary hyperbolic reduced polygons*, Canadian Mathematical Bulletin 68 (2025), 950–965, https://doi.org/10.4153/S0008439525000189 .
