# Logarithmic mean-distance deficit for degenerating Euclidean stadiums

## Finding
Let \(B_2\) be the closed Euclidean unit disk, \(L,r>0\), and \(S_{L,r}=([0,L]\times\{0\})+rB_2\). If \(X,Y\) are independent points sampled uniformly by arclength from \(\partial S_{L,r}\), write \(P=\operatorname{per}(S_{L,r})=2L+2\pi r\) and \(Q(L,r)=\mathbb E|X-Y|/P\). Then, as \(\eta=r/L\downarrow0\),
\[
Q(L,r)=\frac16+\eta^2\log(1/\eta)+O(\eta^2),\qquad
\lim_{\eta\downarrow0}\frac{Q(L,r)-1/6}{\eta^2\log(1/\eta)}=1.
\]
The error constant is absolute, uniformly for all \(L>0\) and \(0<\eta\le 1/10\). In particular the sharp lower perimeter inequality is approached with a logarithmically amplified quadratic deficit along a natural \(C^{1,1}\) family with rounded caps.

## Assumptions and scope
All distances are Euclidean and the arclength probability has total mass one. The stadium is the Minkowski sum of a horizontal segment of length \(L\) and the radius-\(r\) disk. The assertion is an asymptotic theorem at fixed positive segment length or, equivalently by scaling, as \(r/L\to0\); it does not assert a global closed formula or extremality among all planar convex curves. The curved boundary consists of two semicircles of radius \(r\), and the remaining boundary consists of the horizontal segments \([0,L]\times\{\pm r\}\).

## Proof
Define \(N(L,r)=\int_{\partial S_{L,r}}\!\int_{\partial S_{L,r}}|p-q|\,ds(p)ds(q)\). Since both points are arclength-uniform, \(Q=N/P^3\). We may take \(L=1\) by scaling, but retain \(L\) to show the coefficient.

Let \(N_0=\int\!\int|p_x-q_x|\,ds(p)ds(q)\), the same double integral with horizontal-coordinate difference instead of Euclidean distance. The two straight boundary segments together project to the horizontal interval \([0,L]\) with multiplicity two. Each cap has total arclength \(\pi r\) and projects within horizontal distance \(r\) of its respective endpoint. Replace the horizontal projection of each cap by a mass \(\pi r\) at the corresponding endpoint. Since the function \((x,y)\mapsto|x-y|\) is 1-Lipschitz in each argument, this replacement changes \(N_0\) by at most \(2(2L+2\pi r)(2\pi r)r=O(Lr^2+r^3)\). The resulting projected measure is \(2\mathbf1_{[0,L]}(x)\,dx+\pi r(\delta_0+\delta_L)\). Its exact double absolute-distance integral is
\[
\frac{4L^3}{3}+4\pi r L^2+2\pi^2r^2L.
\]
On the other hand,
\[
\frac{P^3}{6}=\frac43(L+\pi r)^3
=\frac{4L^3}{3}+4\pi rL^2+4\pi^2r^2L+\frac43\pi^3r^3.
\]
Consequently \(N_0-P^3/6=O(Lr^2+r^3)\), with no linear deficit.

For points on the same straight side, \(|p-q|-|p_x-q_x|=0\). For the two opposite sides, define
\[
J_L(a)=\int_0^L\!\int_0^L\sqrt{(x-y)^2+a^2}\,dxdy
=2\int_0^L(L-s)\sqrt{s^2+a^2}\,ds.
\]
A direct antiderivative gives, for \(a>0\),
\[
J_L(a)=L^2\sqrt{L^2+a^2}+La^2\operatorname{arsinh}(L/a)
-\frac23\big((L^2+a^2)^{3/2}-a^3\big),
\]
while \(J_L(0)=L^3/3\). Expansion at \(a/L\to0\) yields
\[
J_L(a)-J_L(0)=La^2\log(L/a)+O(La^2)
\]
(the harmless \(\log2\) is absorbed in the remainder). There are two ordered opposite-straight-side pairings; hence their contribution to \(N-N_0\) equals
\[
2\big(J_L(2r)-J_L(0)\big)
=8Lr^2\log(L/r)+O(Lr^2).
\]

It remains to bound all pairs involving caps. Their horizontal separation has the form \(|x-u|\), where \(x\in[0,L]\) and \(u\) lies within \(r\) of an endpoint, and their vertical separation is at most \(2r\). For \(a\ge0\), \(0\le b\le2r\), the elementary estimate
\[
0\le\sqrt{a^2+b^2}-a\le\min\{b,b^2/(2a)\}\quad (a>0)
\]
shows, by splitting the horizontal integral at distance \(O(r)\) from \(u\), that \(\int_0^L[\sqrt{(x-u)^2+b^2}-|x-u|]dx=O(r^2[1+\log(L/r)])\) uniformly in cap points for \(0<r\le L/10\). Integrating over the two cap lengths \(2\pi r\) and both straight sides gives \(O(r^3[1+\log(L/r)])\). Cap-cap pairs contribute \(O(r^3)\), because their total arclength-product mass is \(O(r^2)\) and the pointwise vertical correction is at most \(2r\). Both are \(O(Lr^2)\) in the stated range.

Combining these estimates,
\[
N(L,r)=\frac{P^3}{6}+8Lr^2\log(L/r)+O(Lr^2).
\]
Since \(P^3=8L^3(1+O(r/L))\), division gives the displayed expansion, with an absolute error bound after scaling. This concludes the proof.

## Verification
The proof is analytic for every \(L>0\) and all sufficiently small positive \(r/L\), not a finite sampling argument. The accompanying Python quadrature script uses closed-form straight-to-straight and straight-to-arc integrations and Gaussian quadrature for cap-cap pairs. Representative values for \(r/L=0.04,0.02,0.01,0.005\) give normalized logarithmic coefficients approximately \(0.5731,0.6741,0.7450,0.7930\), respectively, consistent with convergence to one. The script provides a numerical sanity check only; its truncation and rounding errors are not certified.

## Relationship to prior work
Shen (arXiv:2611.21661v1, publicly posted 2026-11-07) proves the sharp universal inequality \(Q(K)>1/6\), sharp in the limit of degenerating rectangles, but does not supply this logarithmic expansion for disk-rounded segments. Results on thin parallelograms describe boundary-minus-interior mean distances, a different observable and shape. Other stadium results on area, minimum width, and the Mahler product do not imply the present boundary pair-distance asymptotic. This is a shape-specific quantitative refinement, not a new universal lower bound.

## Limitations
The result covers only Euclidean stadiums and the thin regime; it does not identify a sharp universal stability modulus, the exact all-aspect-ratio stadium mean distance, or optimality of stadiums at fixed area or perimeter. The mathematical derivation is self-contained; historical priority could be affected by unindexed stochastic-geometry computations or unpublished work. Independent audit has not been performed.

## References
- E. Shen, *A Sharp Perimeter Inequality for Mean Distances on Convex Curves*, arXiv:2611.21661v1 (first public version, 2026-11-07), https://arxiv.org/html/2611.21661v1.
- Published published-finding corpus records: *Universal linear and angular logarithmic saturation for thin parallelograms*, identifier `2026/11/1/SCOPE-universal-linear-and-angular-logarithmic-saturation-for-thin-par--fb1616479c47`; *Sharp canonical stadium stability at fixed perimeter and minimum width*, identifier `2026/10/25/SCOPE-sharp-canonical-stadium-stability-at-fixed-perimeter-and-minimum--1bf3824f73bc`; *Mahler profiles of Euclidean capsules: a planar logarithmic tail and a Gaussian dimension crossover*, identifier `2026/11/2/SCOPE-mahler-profiles-of-euclidean-capsules-a-planar-logarithmic-tail--8ddecde838a0` (indexed summaries used solely for statement comparison).
