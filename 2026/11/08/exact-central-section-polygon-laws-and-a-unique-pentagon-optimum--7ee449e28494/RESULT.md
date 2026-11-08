# Exact central-section polygon laws and a unique pentagon optimum for an equilateral right prism

## Finding
Let \(P(R,h)\subset\mathbb R^3\) be the closed right prism with an equilateral triangular base of circumradius \(R>0\), height \(h>0\), and centroid at the origin. Put \(H=h/(2R)\). For a Haar-uniform unit vector \(U\in S^2\), let \(N\) be the number of vertices of \(P(R,h)\cap U^\perp\). With probability one, \(N\in\{3,4,5\}\). Define
\[
S_H(b)=\arcsin\!\left(\frac{b}{\sqrt{1+H^2}}\right),\qquad 0\le b\le1.
\]
The *complete* law of the central section type is
\[
\begin{aligned}
 p_3(H)&=1-\frac6\pi S_H(1/2),\\
 p_5(H)&=\frac6\pi\left[2S_H(\sqrt3/2)-S_H(1/2)-S_H(1)\right],\\
 p_4(H)&=1-p_3(H)-p_5(H).
\end{aligned}
\]
Here \(p_j(H)=\Pr\{N=j\}\), and all three probabilities are strictly positive for every \(H>0\).

Moreover, \(p_5\) has a **unique global maximum** on \((0,\infty)\). Its maximizing shape has \(H=H_*\), the unique positive solution of
\[
\frac{\sqrt3 H}{\sqrt{H^2+1/4}}-\frac{H}{2\sqrt{H^2+3/4}}=1.
\]
Numerically, \(H_*=0.5314695510636118\ldots\), with \(p_5(H_*)=0.3851558056741766\ldots\). Finally, \(p_3\) is strictly increasing and by itself recovers the aspect ratio:
\[
H=\sqrt{\frac{1}{4\sin^2\!\bigl(\pi(1-p_3)/6\bigr)}-1}.
\]
Thus one observed triangle frequency determines the aspect ratio of the right equilateral prism, while the full polygon-type law and the best pentagon-producing height are explicit.

## Assumptions and scope
The centroidal plane is selected by choosing its *unoriented normal line* uniformly; using either sign of a Haar-uniform \(U\in S^2\) gives the same section. Only plane orientations are random; the offset is identically zero. The prism is nondegenerate, right, and has an equilateral base, and the measurement is the combinatorial number of section vertices. Degenerate normals causing a section through a prism vertex or along an edge form a spherical set of measure zero and do not affect the probabilities. All statements hold for every real \(R,h>0\), without assumptions of generic ratios.

## Proof
Take the base vertices to be \(R(\cos\theta_j,\sin\theta_j)\), where \(\theta_j=2\pi j/3\), \(j=0,1,2\), and the two horizontal bases to lie at heights \(\pm h/2\). Write a unit normal as \(U=(\rho\cos\phi,\rho\sin\phi,z)\), with \(\rho=\sqrt{1-z^2}\). For a generic orientation with \(\rho>0\), the signs at the six prism vertices are those of
\[
R\rho\cos(\phi-\theta_j)\pm(h/2)z.
\]
Since the plane passes through an interior point, every vertex of the section is an intersection with exactly one prism edge whose endpoint signs are opposite. The nine prism edges comprise three on each horizontal base and three vertical edges.

By reflection in the horizontal plane, replace \(z\) by \(|z|\), and let \(t=H|z|/\rho\). Order the three magnitudes \(|\cos(\phi-\theta_j)|\) as \(b_1\le b_2\le b_3\). The number \(q\) of crossed vertical edges equals the number of these magnitudes strictly less than \(t\). Because the three signed cosines sum to zero, one has a sign opposite to the other two and its absolute value equals the sum of their absolute values. Explicitly, after possibly reversing all three signs, their values can be written \(a,b,-a-b\) with \(0<a\le b\). For \(0<t<a\), both horizontal triangles have mixed signs, contributing four crossed base edges; for \(a<t<b\), both still have mixed signs, again contributing four; for \(b<t<a+b\), exactly one horizontal triangle has mixed signs, contributing two; and for \(t>a+b\), neither has mixed signs. Thus the *total* number of crossed edges (equivalently section vertices) is \(4,5,4,3\) for \(q=0,1,2,3\), respectively. This verifies the complete combinatorial classification, including the case where the two smaller absolute cosines exchange order; equality cases have probability zero.

Conditional on \(\phi\), the variable \(|z|\) is uniform on \([0,1]\), so for every \(b\ge0\),
\[
\Pr\{t<b\}=\Pr\left\{\frac{H|z|}{\sqrt{1-z^2}}<b\right\}
=\frac{b}{\sqrt{H^2+b^2}}.
\]
The symmetry of the three base directions and the absolute values reduces angular averaging to \(0\le\phi\le\pi/6\), multiplied by \(6/\pi\). On this sector,
\[
(b_1,b_2,b_3)=\bigl(\cos(\pi/3+\phi),\cos(\pi/3-\phi),\cos\phi\bigr).
\]
Therefore
\[
\begin{aligned}
p_3(H)&=\frac6\pi\int_0^{\pi/6}\left(1-\frac{\cos\phi}{\sqrt{H^2+\cos^2\phi}}\right)\,d\phi,\\
p_5(H)&=\frac6\pi\int_0^{\pi/6}\left(\frac{\cos(\pi/3-\phi)}{\sqrt{H^2+\cos^2(\pi/3-\phi)}}-\frac{\cos(\pi/3+\phi)}{\sqrt{H^2+\cos^2(\pi/3+\phi)}}\right)\,d\phi.
\end{aligned}
\]
The elementary antiderivative
\[
\int\frac{\cos v}{\sqrt{H^2+\cos^2v}}\,dv=\arcsin\!\left(\frac{\sin v}{\sqrt{1+H^2}}\right)
\]
produces the stated expressions; \(p_4\) is their probability complement. Positivity is immediate from the open intervals \(t>b_3\), \(b_1<t<b_2\), and \(t<b_1\) on positive-measure angular sets.

Set
\[
J(H)=\frac{\sqrt3H}{\sqrt{H^2+1/4}}-\frac{H}{2\sqrt{H^2+3/4}}.
\]
Direct differentiation gives
\[
 p'_5(H)=\frac{6}{\pi(1+H^2)}(1-J(H)),\qquad
 J'(H)=\frac{\sqrt3}{4(H^2+1/4)^{3/2}}-\frac{3}{8(H^2+3/4)^{3/2}}>0.
\]
The last inequality holds because the first numerator exceeds the second while its denominator is smaller. As \(J(0+)=0\) and \(J(\infty)=\sqrt3-1/2>1\), there is exactly one positive critical point of \(p_5\); it is a strict global maximum. Finally,
\[
p'_3(H)=\frac{3H}{\pi(1+H^2)\sqrt{H^2+3/4}}>0.
\]
Solving the explicit formula for \(p_3\) yields the stated aspect-ratio inverse. This completes the proof.

## Verification
The accompanying `verify.py` independently counts intersections of a centroidal plane with the nine geometric edges, for 1,260,000 Gaussian-generated Haar normals at seven aspect ratios. It also compares two independent integrations (closed form and direct angular quadrature) for all three probabilities, checks the critical-point equation, and tests positivity of the derivative of \(J\) numerically at representative points. Observed maximal absolute discrepancy against Monte Carlo section counts was \(0.00219519\); the computed maximizer and its pentagon probability agree with the reported digits. The analytic proof, not the sample count or grid tests, establishes the universal claims.

Reproduce from a Python environment with `numpy` and `scipy` using `python verify.py` (working directory containing the standalone file). No external data is required.

## Relationship to prior work
Wang's 2011 paper establishes that triangular prisms are universal tilers by analyzing which polygonal cross-sections tile the plane; it does not measure the orientation distribution or optimize an aspect ratio. Padrol and Pfeifle's 2014 study classifies geometric realizability and intersection complexity of polygons as polytope sections, rather than frequencies for one fixed prism. Konstantinova and Shchur's later work develops a random-plane sampling algorithm and estimates angle distributions for several polyhedra, including the triangular prism; its accessible abstract does not state a closed-form **centroidal, orientation-only polygon-type law**, and its full text could not be inspected. Via planar polarity, a central polygon section of the prism is dual to the orthogonal planar shadow of its five-vertex polar *triangular bipyramid*; the edge/vertex count agrees, giving a second natural formulation. Related published results for central sections of boxes and for random projections of **quadrangular pyramids** use distinct objects and sampling operations, and do not imply the triangular-bipyramid result merely by substituting geometric parameters.

## Limitations
These probabilities concern central sections only, not arbitrary-offset random planes, which require a separate sampling measure. The base must be equilateral and the prism right; no universal law is asserted for oblique or scalene prisms. All uniqueness statements concern the one-parameter aspect ratio, not absolute scale. Historical-priority assessment remains provisional, particularly against inaccessible stereological literature on triangular-prism sections. There has been no independent validation of the theorem.

## References
1. D. G. L. Wang, *Determining All Universal Tilers*, arXiv:1110.1715, first made public 2011-10-08, https://arxiv.org/abs/1110.1715.
2. A. Padrol and J. Pfeifle, *Polygons as sections of higher-dimensional polytopes*, arXiv:1404.2443, first made public 2014-04-09, https://arxiv.org/abs/1404.2443.
3. L. N. Shchur and E. P. Konstantinova, *Algorithm for Density of Angle Distribution in Random Sections of Polyhedron*, SSRN:4485810, publicly posted 2023-06-20; DOI:10.1016/j.eswa.2023.121195. Accessible abstract only.
