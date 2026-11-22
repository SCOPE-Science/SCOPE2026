# Two sharp contact transitions for unrestricted maximal rectangles in circular segments

## Finding

Let \(K_h=\{(x,y)\in\mathbb R^2:x^2+y^2\le1,\ y\ge h\}\), where \(-1<h<1\). Among **all** nondegenerate Euclidean rectangles contained in \(K_h\), with arbitrary translation and orientation, the greatest area \(M(h)\) is
\[
M(h)=\begin{cases}
2,&-1<h\le-1/\sqrt2,\\
-4h\sqrt{1-h^2},&-1/\sqrt2\le h\le-1/\sqrt3,\\
2(q(h)-h)\sqrt{1-q(h)^2},&-1/\sqrt3\le h<1,
\end{cases}
\qquad q(h)=\frac{h+\sqrt{h^2+8}}4.
\]
There are two distinct contact transitions. At \(h_1=-1/\sqrt2\), a continuum of centered, circularly inscribed optimal squares becomes one unique, cut-parallel rectangle. At \(h_2=-1/\sqrt3\), the lower pair of corners cease touching the circle, though they continue touching the cutting line. The area profile is continuously differentiable but not twice differentiable at either transition:
\[
M''(h_1-)=0,\quad M''(h_1+)=-16;\qquad
M''(h_2-)=-7\sqrt2,\quad M''(h_2+)=\sqrt2/5.
\]
For a vanishing circular cap, \(h=1-\delta\),
\[
M(1-\delta)\sim\frac{4\sqrt6}{9}\delta^{3/2},\qquad
\frac{M(h)}{\operatorname{area}(K_h)}\longrightarrow\frac1{\sqrt3}\quad(h\uparrow1).
\]

## Assumptions and scope

A rectangle means the convex hull of \(c\pm u\pm v\), where \(u,v\in\mathbb R^2\) are nonzero and orthogonal; its Euclidean area is \(4\lVert u\rVert\lVert v\rVert\). No assumption is imposed on its orientation or center. The cutting half-plane is closed, and boundary contacts are allowed. Every assertion concerns \(-1<h<1\); at the endpoints the cap is respectively the full disk in the limiting sense and a point. A disk of radius \(R>0\) reduces to the stated unit-radius normalization by \((x,y)\mapsto(x/R,y/R)\) and multiplies all areas by \(R^2\).

## Proof

**1. Reduction of arbitrary orientations to cut-parallel rectangles.** Write an arbitrary rectangle as the four vertices \(c\pm u\pm v\), with orthogonal \(u,v\), and relabel so \(a=\lVert u\rVert\ge b=\lVert v\rVert>0\). Its vertical half-extent is \(t=|u_y|+|v_y|\ge b\). The cutting constraint gives \(c_y\ge h+t\). Orthogonality gives the exact maximal squared distance of a vertex from the origin:
\[
T=\lVert c\rVert^2+a^2+b^2+2(|c\cdot u|+|c\cdot v|).
\]
If \(e_1=u/a\) and \(e_2=v/b\), then
\[
|c\cdot u|+|c\cdot v|=a|c\cdot e_1|+b|c\cdot e_2|\ge b\lVert c\rVert.
\]
Feasibility inside the disk means \(T\le1\).

If \(h+b\le0\), the axis-aligned rectangle with vertices \((\pm a,\pm b)\) is feasible: its cutting constraint holds, and \(a^2+b^2\le T\le1\). If \(h+b>0\), then \(\lVert c\rVert\ge c_y\ge h+t\ge h+b>0\). Consequently
\[
1\ge T\ge a^2+b^2+(h+b)^2+2b(h+b)=a^2+(h+2b)^2.
\]
The axis-aligned rectangle with vertices \((\pm a,h)\) and \((\pm a,h+2b)\) is therefore also feasible, since \(h+2b>|h|\) in this case. In both cases it has exactly the original area \(4ab\). Thus an unrestricted optimum exists among rectangles whose edges are parallel/perpendicular to the cut. This reduction does not assume the desired orientation.

**2. The exact one-variable area envelope.** For an axis-aligned rectangle with vertical endpoints \(y_-\le y_+\), set \(t=\max\{|y_-|,|y_+|\}\). Its horizontal width is at most \(2\sqrt{1-t^2}\), and its vertical height is at most \(\min\{2t,t-h\}\), with \(\max\{0,h\}\le t\le1\). Conversely, both bounds are simultaneously attained by choosing top \(t\), bottom \(\max\{h,-t\}\), and horizontal endpoints \(\pm\sqrt{1-t^2}\). Hence
\[
M(h)=\max_{\max\{0,h\}\le t\le1}
2\sqrt{1-t^2}\min\{2t,t-h\}.
\]
For \(h<0\), the first factor branch \(4t\sqrt{1-t^2}\) applies to \(t\le-h\), with sole stationary maximum \(t=1/\sqrt2\). The second branch \(2(t-h)\sqrt{1-t^2}\) applies to \(t\ge-h\) (and everywhere if \(h\ge0\)); its derivative has the sign of \(1-2t^2+ht\), whose unique positive zero is \(q(h)\). At their meeting point \(t=-h\), the derivative of the second branch has the sign of \(1-3h^2\). Comparing these unique branch maxima yields, respectively, \(t=1/\sqrt2\), \(t=-h\), and \(t=q(h)\), on the three stated parameter intervals, and exactly the formula for \(M(h)\).

**3. Equality cases and contact geometry.** In the first regime the full-disk optimal rectangles are exactly centered inscribed squares; those whose lowest point is at height at least \(h\) are exactly the cap optimizers. At \(h=h_1\) only a square with horizontal/vertical edges fits. For \(h>h_1\) the one-variable maximizing \(t\) and the horizontal width are unique. Any non-axis-aligned rectangle with the same area would have an axis-aligned comparison rectangle attaining the disk constraint with equality. The inequalities in step 1 must then all be equalities. In the centered case this forces \(c=0\) and \(t=b\); in the shifted case it forces \(c=(0,h+b)\) and \(t=b\). Since \(a>b\) in the strict post-threshold cases, \(t=b\) forces the shorter side vector to be vertical. Thus the optimizer is uniquely aligned up to the rectangle's trivial vertex and edge relabelings. For \(h_1<h\le h_2\), it is centered, with horizontal halfwidth \(\sqrt{1-h^2}\), vertical halfheight \(-h\), and all four corners on the circle. For \(h_2<h<1\), its top is \(q(h)\), bottom is \(h\), and halfwidth is \(\sqrt{1-q(h)^2}\); exactly its upper corners touch the circle and lower corners touch the chord.

**4. Differentiability and vanishing-cap limit.** The three explicit analytic branches agree in value and first derivative at both switches. Direct differentiation yields the four one-sided second derivatives in the Finding. At \(h=h_1+\eta\), the area deficit is \(2-M(h)=8\eta^2+o(\eta^2)\). For \(h=1-\delta\), expanding the defining quadratic \(2q^2-hq-1=0\) gives \(q=1-\delta/3+O(\delta^2)\), and hence \(M(h)=(4\sqrt6/9)\delta^{3/2}+O(\delta^{5/2})\). The cap area is \(S(h)=\arccos h-h\sqrt{1-h^2}=(4\sqrt2/3)\delta^{3/2}+O(\delta^{5/2})\). Division gives \(1/\sqrt3\), as claimed.

## Verification

`checker.py` provides a standalone Python standard-library diagnostic. Run `python3 checker.py` in this directory. It evaluates all three formulas at their interfaces, compares against one-variable grid maximization, checks explicit feasibility and a large reproducibly seeded sample of arbitrarily oriented feasible rectangles, evaluates analytic second-derivative and thin-cap predictions, and checks the area ratio. Its reported assertion count is a finite computational cross-check, not a substitute for the proof above.

## Relationship to prior work

Cabello, Cheong, Knauer and Schlipf give algorithms for maximum-area rectangles in convex *polygons*, without the analytic all-cut-height classification of the curved circular-segment family here. Behroozi develops optimization methods for inscribed rectangles in convex sets, prominently with fixed axes; the present proof adds an unrestricted orientation-rigidity reduction and two exact cap-contact thresholds. The familiar semicircle case is \(h=0\), for which the formula specializes to unit area. These facts and the absence of an equivalent statement among inspected sources support a best-knowledge originality assessment, but do not constitute proof that no older equivalent result exists.

## Limitations

The theorem addresses rectangles (right-angle parallelograms) in planar circular segments and no other quadrilateral classes. It does not assert a sharp stability inequality for near-optimal, rotated rectangles, nor any analogous global classification for intersections of unequal disks. The code is finite validation, not an exhaustive search of continuous shapes. Historical priority has not been independently certified.

## References

- S. Cabello, O. Cheong, C. Knauer and L. Schlipf, *Finding Largest Rectangles in Convex Polygons*, first public May 6, 2014. https://arxiv.org/abs/1405.1223
- M. Behroozi, *Largest Inscribed Rectangles in Geometric Convex Sets*, first public May 30, 2019. https://arxiv.org/abs/1905.13246
- *Maximum area of a rectangle inscribed in a semi-circle with radius R*, Mathematics Stack Exchange, July 20, 2014. https://math.stackexchange.com/questions/872223/maximum-area-of-a-rectangle-inscribed-in-a-semi-circle-with-radius-r/2912879
