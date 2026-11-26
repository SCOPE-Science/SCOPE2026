# The first rounding-dependent term in the mean boundary chord of a thin stadium

## Finding

Let \(S_{L,r}=([0,L]\times\{0\})+rB_2\), where \(B_2\) is the Euclidean unit disk and \(L,r>0\). For independent points \(X,Y\) uniform with respect to arclength on its boundary, put \(Q_S=\mathbb E|X-Y|/\operatorname{per}(S_{L,r})\) and \(\eta=r/L\). Then
\[
Q_S=\frac16+\eta^2\log(1/\eta)
    +\left(\frac32-\frac{\pi^2}{4}\right)\eta^2
    +O\!\left(\eta^3[1+\log(1/\eta)]\right).
\]
The remainder has an absolute constant for all \(L>0\) and \(0<\eta\le 1/10\). In particular, if \(Q_{\rm rect}\) is the same quotient for the rectangle \([0,L]\times[-r,r]\), then
\[
\lim_{\eta\downarrow0}\frac{Q_S-Q_{\rm rect}}{\eta^2}
=3-\frac{\pi^2}{4}>0.
\]
The comparison holds at equal straight-side length and width, with each mean normalized by that shape's own perimeter. The leading logarithmic term is shared by the two shapes; the nonlogarithmic quadratic term detects rounding.

## Proof

Let \(N=\int\!\int |p-q|\,ds(p)ds(q)\), with ordered pairs on the boundary, so \(Q=N/P^3\) for perimeter \(P\). Let \(N_x\) be the integral with \(|p_x-q_x|\) in place of the Euclidean distance. In both shapes the straight horizontal sides project with density two onto \([0,L]\). Let \(m\) be the length of each of the two remaining boundary pieces: \(m=\pi r\) for the stadium, \(m=2r\) for the rectangle. If each such piece is projected to a point mass at its straight-side endpoint, the resulting integral is
\[
A(m)=\frac{4L^3}{3}+4mL^2+2m^2L,
\qquad A(m)-\frac{(2L+2m)^3}{6}=-2m^2L-\frac43m^3.
\]
The three terms in \(A(m)\) come from side-side, side-end (both orders), and opposite end-end pairings, respectively.

On the semicircle at the left endpoint, the outward horizontal displacement is \(r\cos\theta\) with \(-\pi/2\le\theta\le\pi/2\), so its arclength integral is \(2r^2\); the right endpoint gives the same integral. Since the caps project outside the interval, each outward displacement increases the horizontal distance to every point on a straight side by exactly that displacement. The horizontal sides have total length \(2L\), and both orders count, giving a net correction \(2(2L)(4r^2)=16Lr^2\) from straight-to-cap pairs. Cap-cap pairs change by \(O(r^3)\) under collapse, since each displacement is at most \(r\) and the total arclength product is \(O(r^2)\). In the rectangle the projection collapse is exact. Thus
\[
N_x-P^3/6=\begin{cases}
(16-2\pi^2)Lr^2+O(r^3),&\text{stadium},\\
-8Lr^2+O(r^3),&\text{rectangle}.
\end{cases}
\]

The same horizontal side has no vertical correction. For opposite straight sides let
\[
J_L(a)=2\int_0^L(L-s)\sqrt{s^2+a^2}\,ds
= L^2\sqrt{L^2+a^2}+La^2\operatorname{arsinh}(L/a)
 -\frac23\big((L^2+a^2)^{3/2}-a^3\big).
\]
Using \(J_L(0)=L^3/3\), and expanding the square root, the \(3/2\) power and \(\operatorname{arsinh}(L/a)=\log(2L/a)+O((a/L)^2)\), gives, uniformly for \(0<a\le L/5\),
\[
J_L(a)-J_L(0)=La^2\left(\log(2L/a)-\frac12\right)+O(a^3+a^4/L).
\]
The two ordered opposite-side terms at \(a=2r\) consequently contribute \(8Lr^2\log(L/r)-4Lr^2+O(r^3)\) to \(N-N_x\) for either shape.

For an end-to-side pair with horizontal distance \(s\) and vertical distance at most \(2r\), the correction is at most \(\min(2r,2r^2/s)\) for \(s>0\), and at most \(2r\) even when \(s=0\). The projected end point lies at or outward from a straight-side endpoint. Integrating over a side, the portion within horizontal distance \(r\) contributes at most \(2r^2\), and the rest is bounded by \(2r^2\log((L+r)/r)\). Multiplying by the lengths of the end pieces bounds all end-to-side corrections by \(O(r^3[1+\log(L/r)])\). End-to-end corrections are \(O(r^3)\) by the uniform bound \(2r\) and their arclength product.

The preceding estimates give
\[
N-P^3/6=8Lr^2\log(L/r)+\begin{cases}
(12-2\pi^2)Lr^2,&\text{stadium},\\
-12Lr^2,&\text{rectangle},
\end{cases}
+O(r^3[1+\log(L/r)]).
\]
Finally \(P^{-3}=(8L^3)^{-1}(1+O(r/L))\) in both shapes. After division the denominator approximation costs only \(O(\eta^3[1+\log(1/\eta)])\). This yields the stated stadium expansion and the rectangle coefficient \(-3/2\) at order \(\eta^2\), proving the comparison.

## Scope and relation to prior work

The universal lower bound \(Q>1/6\) and its sharpness are not new here; see E. Shen, *A Sharp Perimeter Inequality for Mean Distances on Convex Curves*, [arXiv:2611.21661v1](https://arxiv.org/html/2611.21661v1), Theorem 1.1. The exact Euclidean rectangle profile (record `2026/11/22/SCOPE-sharp-boundary-chord-mean-distance-profile-of-euclidean-rectangl--28c76116152b`) already gives the rectangle expansion. At logarithmic accuracy, an \(O(\eta^2)\) cap comparison transfers that leading correction to the stadium; the separate conclusion here is the explicit first coefficient sensitive to the semicircular caps. The fixed-profile collapsing-lens law (record `2026/11/22/SCOPE-universal-logarithmic-mean-distance-law-for-collapsing-convex-le--5e66fde6292b`) captures a related leading logarithm, not the quadratic term for the stadium's scale-dependent caps. No general rounding law or optimality across convex families is claimed.

The proof is analytic; the unchanged leading-order numerical diagnostic does not verify the quadratic coefficient or the uniform bound. No historical priority beyond the comparisons described here is asserted.
