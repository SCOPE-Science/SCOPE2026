# The complete Euclidean pair-distance law on the regular tetrahedral wireframe

## Finding
Let \(G\) be the union of the six edges of a regular tetrahedron in \(\mathbb R^3\) of side length one. Let \(X,Y\) be independent, uniform with respect to arclength on \(G\), and let \(R=\|X-Y\|_2\) be their **ambient Euclidean** separation. Put
\[
h=\frac1{\sqrt2},\qquad k=\frac{\sqrt3}{2}.
\]
For \(0\le r\le1\), define
\[
S(r)=2r-r^2,
\]
\[
A(r)=\begin{cases}
\dfrac{2\pi r^2}{3\sqrt3},&0\le r\le k,\\[3pt]
\dfrac{4r^2}{\sqrt3}\arcsin\!\left(\dfrac{\sqrt3}{2r}\right)
-\dfrac{4\pi r^2}{3\sqrt3}+2\sqrt{r^2-\tfrac34},&k<r\le1,
\end{cases}
\]
and
\[
O(r)=\begin{cases}
0,&0\le r\le h,\\[2pt]
\pi(r^2-\tfrac12),&h<r\le k,\\[2pt]
2\sqrt{r^2-\tfrac34}+4(r^2-\tfrac12)
\arcsin\!\left(\dfrac1{2\sqrt{r^2-\tfrac12}}\right)
-\pi(r^2-\tfrac12),&k<r\le1.
\end{cases}
\]
Then the **complete distribution** is
\[
\boxed{\Pr(R\le r)=\frac16S(r)+\frac23A(r)+\frac16O(r)}
\qquad(0\le r\le1),
\]
with values zero for \(r<0\) and one for \(r>1\). In particular, its first branch is the exact polynomial
\[
\Pr(R\le r)=\frac r3+\left(\frac{4\pi}{9\sqrt3}-\frac16\right)r^2
\qquad(0\le r\le h).
\]
The law has two distinct interior thresholds. The density jumps *up* by \(\pi/(3\sqrt2)\) at \(r=h\). At \(r=k\), put \(\delta=r^2-3/4\) and let
\[
P(r)=\frac16(2r-r^2)+\frac{4\pi r^2}{9\sqrt3}+\frac\pi6(r^2-\tfrac12).
\]
Then, as \(r\downarrow k\) from above,
\[
\Pr(R\le r)=P(r)-\frac{56}{27}\delta^{3/2}+O(\delta^{5/2}).
\]
The upper-distance endpoint and second moment satisfy
\[
\boxed{\Pr(R>1-\varepsilon)\sim\frac{25}{6}\varepsilon^2}
\quad(\varepsilon\downarrow0),\qquad
\boxed{\mathbb E R^2=\frac5{12}}.
\]

## Assumptions and scope
Arclength-uniform means one chooses each of the six edges with probability \(1/6\), then chooses a point uniformly in its unit-length arclength coordinate. Points on shared vertices have probability zero. All probabilities above refer to two *independent* points, and \(\|\cdot\|_2\) denotes the three-dimensional Euclidean metric, **not** shortest-path distance along the edge network. The formulas are scale-normalized; for edge length \(a>0\), replace \(r\) by \(r/a\).

## Proof
**Edge-pair reduction.** There are 36 equiprobable ordered edge pairs: six coincide, 24 share a vertex but are distinct, and six are disjoint. Thus their weights are \(1/6,2/3,1/6\). With independent \(U,V\sim\operatorname{Unif}[0,1]\), the squared distances for these classes are respectively
\[
(U-V)^2,\qquad U^2+V^2-UV,\qquad
\frac12+(U-\tfrac12)^2+(V-\tfrac12)^2.
\]
The second identity is the cosine law at the \(60^\circ\) tetrahedral vertex angle. In the third identity the opposite edges are mutually perpendicular, and their midpoints have separation \(1/\sqrt2\), perpendicular to both edge directions. Consequently the CDF is the stated weighted mixture of the three unit-square sublevel areas.

**Coincident edges.** The complement of \(\{|U-V|\le r\}\) consists of two triangles each of area \((1-r)^2/2\). Hence \(S(r)=2r-r^2\) for \(0\le r\le1\).

**Adjacent edges.** On the first quadrant the quadratic form \(u^2+v^2-uv\) has the linear Euclidean coordinates \((x,y)=(u-v/2,\sqrt3 v/2)\), Jacobian \(\sqrt3/2\). The positive quadrant becomes a wedge of opening \(2\pi/3\); its disk sublevel area in original \((u,v)\) coordinates is \(2\pi r^2/(3\sqrt3)\). For \(r\le\sqrt3/2\) the disk wedge meets neither upper side \(u=1\) nor \(v=1\) of the unit square. For \(\sqrt3/2<r\le1\), two disjoint symmetric caps lie beyond those sides, each of area
\[
C_A(r)=\int_1^{2r/\sqrt3}\sqrt{4r^2-3u^2}\,du.
\]
They are disjoint in the first-quadrant wedge for \(r<1\), since the only common corner \((1,1)\) has quadratic form one. Evaluating this elementary circular-segment integral gives precisely the asserted second branch \(A(r)=2\pi r^2/(3\sqrt3)-2C_A(r)\).

**Opposite edges.** Translating the unit square by \((-1/2,-1/2)\) reduces its sublevel set to the intersection of the centered square \([-1/2,1/2]^2\) with the disk of radius \(\rho=\sqrt{r^2-1/2}\). For \(r\le h\) this disk has zero area, and for \(h<r\le k\) it lies wholly in the square, giving \(\pi\rho^2\). Above \(k\), four disjoint caps are clipped from the disk, each of area
\[
C_O(r)=2\int_{1/2}^{\rho}\sqrt{\rho^2-t^2}\,dt.
\]
The cap regions are disjoint for \(r<1\), because the square corners lie on the circle only when \(r=1\). Integrating gives the stated third branch \(O(r)=\pi\rho^2-4C_O(r)\). Both formulas are continuous at the thresholds and give one at \(r=1\).

**Interior thresholds.** The opposite-edge contribution is identically zero below \(h\) and \(\pi(r^2-1/2)\) just above it. Its weighted derivative jump is \(\frac16(2\pi h)=\pi/(3\sqrt2)\). For \(r>k\), write \(\delta=r^2-3/4>0\). A Taylor expansion of the two cap integrals at tangency yields, with explicit positive leading coefficients,
\[
C_A(r)=\frac89\delta^{3/2}+O(\delta^{5/2}),\qquad
C_O(r)=\frac43\delta^{3/2}+O(\delta^{5/2}).
\]
For the first, set \(u=1+t\), expand \(4r^2-3u^2=4\delta-6t-3t^2\), and rescale \(t=\delta s\); the integration endpoint is \(t=2\delta/3+O(\delta^2)\), giving \(\int_0^{2/3}2\sqrt{1-3s/2}\,ds=8/9\). For the second, set \(t=1/2+s\) in its defining integral, use \(\rho^2-t^2=\delta-s-s^2\), and obtain \(2\int_0^1\sqrt{1-s}\,ds=4/3\) after rescaling. Below \(k\), the relevant analytic continuation is exactly \(P(r)\). The clipped area changes the mixture by
\[
-\frac23(2C_A(r))-\frac16(4C_O(r))
=-\left(\frac{32}{27}+\frac89\right)\delta^{3/2}
+O(\delta^{5/2})
=-\frac{56}{27}\delta^{3/2}+O(\delta^{5/2}),
\]
as required.

**Upper endpoint.** In the unit parameter square, the distance can equal one only at boundary corners: two ordered corners for coincident edges, three for adjacent edges, and four for opposite edges. At a coincident-edge maximizing corner the deficit condition \(R>1-\varepsilon\) cuts a triangular area \(\varepsilon^2/2+o(\varepsilon^2)\), giving conditional coefficient one. At adjacent corners \((1,0)\), \((0,1)\), and \((1,1)\), the deficit of squared distance is respectively \(2(1-u)+v\), \(u+2(1-v)\), and \((1-u)+(1-v)\), to first order. Since \(R^2>(1-\varepsilon)^2\), their corner areas sum to \((1+1+2)\varepsilon^2+o(\varepsilon^2)=4\varepsilon^2+o(\varepsilon^2)\). At each of the four opposite corners, the leading squared-distance deficit is the sum of the inward coordinate displacements, giving \(2\varepsilon^2+o(\varepsilon^2)\) per corner, or conditional coefficient eight. The weighted total is \(\frac16+\frac23\cdot4+\frac16\cdot8=25/6\).

**Second moment.** Direct expectations of the three squared-distance forms yield \(1/6,5/12,2/3\), respectively. Weighting by \(1/6,2/3,1/6\) gives \(5/12\). This completes the proof for all claimed cases.

## Verification
The accompanying standalone `check.py` requires the Python standard library only. It independently enumerates ordered edge pairs and numerically integrates the actual coordinate-section lengths, rather than reusing the closed-form integration. It checks 18 section integrals (maximum observed numerical error below \(4\times10^{-6}\)), the exact second moment, the \(-56/27\) cusp constant and the \(25/6\) upper-tail constant. All deterministic checks passed. These experiments corroborate, but do not replace, the full analytic proof above.

## Relationship to prior work
Finch [1] studies widths obtained by uniformly sampling a *direction* for the entire regular tetrahedron, not a pair of points uniformly sampled along its edges. Bäsel [2] studies random Euclidean chords and distances for points sampled in a *planar polygon's interior*, not a tetrahedral wireframe. Fodor, Hug and Ziebarth [3] study volume errors for randomly circumscribed convex polytopes, a different sample space and observable. The edge-conditioned decomposition above is directly checkable against those differences. Searches of related mathematical records, including works on tetrahedral *surface* geodesics, *volume*-uniform simplices and intrinsic graph distances, found no theorem implying this complete three-regime skeleton-distance distribution. This is not a proof of historical priority.

## Limitations
The formula is for the complete arclength-uniform 1-skeleton of a **regular** Euclidean tetrahedron. It does not address arbitrary tetrahedra, unequal edge-sampling weights, graph shortest-path distance, surface-area or volume sampling, nor higher-order joint distance distributions. The published-literature search was nonexhaustive; priority and mathematical verification require independent evaluation.

## References
[1] Steven R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first public 2011-10-04. https://arxiv.org/abs/1110.0671

[2] Uwe Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first public 2012-04-12. https://arxiv.org/abs/1204.2707

[3] Ferenc Fodor, Daniel Hug, and Ines Ziebarth, *The volume of random polytopes circumscribed around a convex body*, arXiv:1409.8105, first public 2014-09-29, primary MSC 52A22. https://arxiv.org/abs/1409.8105
