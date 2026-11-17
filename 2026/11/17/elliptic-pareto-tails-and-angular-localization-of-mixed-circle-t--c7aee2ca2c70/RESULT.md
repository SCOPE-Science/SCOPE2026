# Elliptic Pareto tails and angular localization of mixed-circle triangle circumcenters

## Finding
Fix \(0\le r<1\) and a point \(C=(r,0)\) of the unit disk. Independently sample \(A,B\) with uniform arclength measure on its unit-circle boundary. Let \(O\) and \(R\) be the Euclidean circumcenter and circumradius of triangle \(ABC\); put \(S=\|O\|\). Define the complete elliptic integral
\[
K(r)=\int_0^{\pi/2}\frac{dt}{\sqrt{1-r^2\sin^2t}},\qquad 0\le r<1.
\]
The radial circumcenter and circumradius have the same exact first-order heavy-tail coefficient:
\[
\boxed{\lim_{T\to\infty}T\Pr(S>T)=\lim_{T\to\infty}T\Pr(R>T)
=c(r):=\frac{2(1-r^2)}{\pi^2}K(r).}
\]
For every \(T>0\), not only in the tail, an exact quadrature is available. With \(\delta=(1-r^2)/2\) and \(\operatorname{clip}(z)=\max\{-1,\min\{1,z\}\}\),
\[
\boxed{\Pr(S>T)=\frac1{2\pi^2}\int_0^{2\pi}
\left[\arccos\bigl(\operatorname{clip}(r\cos u-\delta/T)\bigr)
-\arccos\bigl(\operatorname{clip}(r\cos u+\delta/T)\bigr)\right]du.}
\]

The location of a remote circumcenter is not isotropic unless \(r=0\). Let \(\Theta=\arg(O)\) modulo \(2\pi\) and \(Y_T=T/S\). Then, **conditionally on \(S>T\)**,
\[
(\Theta,Y_T)\xrightarrow[\,T\to\infty\,]{\mathrm{TV}}g_r(\theta)\,d\theta\otimes\operatorname{Unif}(0,1),
\qquad
\boxed{g_r(\theta)=\frac1{4K(r)\sqrt{1-r^2\cos^2\theta}}.}
\]
The rare-event magnitude and direction become asymptotically independent. The direction concentrates as the fixed vertex approaches the original circle:
\[
g_r(\theta)d\theta\Longrightarrow\tfrac12\delta_0+\tfrac12\delta_\pi\qquad(r\uparrow1).
\]

The coefficient \(c(r)\) is strictly decreasing from \(c(0)=1/\pi\) to zero and obeys
\[
\boxed{c(r)\sim\frac{1-r^2}{\pi^2}\log\frac1{1-r^2}\qquad(r\uparrow1).}
\]
Thus the centered fixed point uniquely maximizes the far-circumcenter tail constant, while all interior fixed points produce infinite expected circumradius and circumcenter distance. At the boundary value \(r=1\), all three vertices lie on the unit circle, hence \(O=0\), \(R=1\) almost surely: every moment becomes finite.

## Assumptions and scope
All circles are Euclidean and of radius one. The two random boundary vertices are independent and uniform in *angle*, equivalently in arclength. The third point is deterministic, at radial distance \(r\). For \(r<1\) collinearity occurs on a set of probability zero, and the circumcircle is uniquely defined almost surely. An angle of the circumcenter on the null event \(O=0\) may be assigned arbitrarily. The symbols \(S\) and \(R\) denote nonnegative Euclidean distances, not graph metrics. All statements about \(T\to\infty\) hold with \(r<1\) fixed. The weak directional limit as \(r\uparrow1\) concerns the limiting *rare-event angle law*, not the actual angle when \(r=1\), at which the circumcenter is the origin.

## Proof
**1. Independent chord coordinates and an exact circumcenter identity.** Write the random vertices as
\[
A=(\cos(U+V),\sin(U+V)),\qquad
B=(\cos(U-V),\sin(U-V)),
\]
with \(U\) uniform on \([0,2\pi)\), \(V\) uniform on \([0,\pi)\), and independent. To justify this parameterization, start from the independent uniform angles of \(A,B\), take their difference modulo \(2\pi\), and use the second angle as the other Haar coordinate. Their difference divided by two modulo \(\pi\) is uniform and independent of the second angle; adding it to the latter yields \(U\), still uniform and independent of \(V\). The circle's center lies on the perpendicular bisector of \(AB\), whose line is spanned by \(n(U)=(\cos U,\sin U)\). Thus the circumcenter is \(O=\lambda n(U)\) for some real \(\lambda\). Equality of its squared distances from \(A\) and \(C\) gives
\[
1-2\lambda\cos V=r^2-2\lambda r\cos U,
\qquad \boxed{\lambda=\frac{\delta}{D},\quad D=\cos V-r\cos U,\quad\delta=\frac{1-r^2}{2}.}
\]
Hence \(S=\delta/|D|\). The random variable \(D\) has a continuous, strictly positive density at zero for each fixed \(r<1\).

**2. Full survival distribution.** For fixed \(U=u\), the variable \(\cos V\) has arcsine density \(h(z)=(\pi\sqrt{1-z^2})^{-1}\) on \((-1,1)\). Consequently \(S>T\) is the event \(|\cos V-r\cos u|<\delta/T\). Its conditional probability is the difference of two clipped arccosines divided by \(\pi\). Averaging over \(U\) gives the stated one-dimensional quadrature, including both clipped endpoints. In particular for \(r=0\) and \(T\ge1/2\), it reduces to the exact identity \(\Pr(S>T)=\frac2\pi\arcsin(1/(2T))\).

**3. Elliptic tail coefficient.** The joint density of \((U,D)\) at \((u,d)\) is
\[
p_r(u,d)=\frac{\mathbf1_{\{|d+r\cos u|<1\}}}{2\pi^2\sqrt{1-(d+r\cos u)^2}}.
\]
For fixed \(r<1\), this function is continuous and bounded uniformly in \(u\) for \(d\) in a sufficiently small interval around zero. Thus, using \(S>T\iff|D|<\delta/T\) and dominated convergence,
\[
\lim_{T\to\infty}T\Pr(S>T)
=2\delta\int_0^{2\pi}p_r(u,0)\,du
=\frac{\delta}{\pi^2}\int_0^{2\pi}\frac{du}{\sqrt{1-r^2\cos^2u}}.
\]
The last integral equals \(4K(r)\), proving the claimed coefficient. Since the circumradius is \(R=\|O-A\|\), the reverse triangle inequality gives \(|R-S|\le1\). Sandwiching their survival functions between the thresholds \(T-1\) and \(T+1\) yields the identical circumradius coefficient.

**4. Marked total-variation limit.** On \(S>T\), set \(y=T|D|/\delta\in(0,1)\) and \(\sigma=\operatorname{sgn}D\in\{-1,1\}\). The joint unnormalized density of \((U,y,\sigma)\), relative to angular Lebesgue measure and \(dy\), is \((\delta/T)p_r(u,\sigma\delta y/T)\). Uniform continuity in the compact \((u,y)\)-domain implies uniform convergence, after conditioning, to a probability law in which \(\sigma\) is fair, \(y\) is uniform, and \(U\) has density \(p_r(u,0)/\int p_r(v,0)dv\). This convergence is in \(L^1\), hence in total variation. The direction of \(O\) is \(U\) for positive \(D\) and \(U+\pi\) for negative \(D\); its limiting angle density is unchanged by this shift because \(p_r(u,0)\) is \(\pi\)-periodic. The normalized density is exactly \(g_r\) displayed above, independent of \(y=Y_T\). Measurable pushforward cannot increase total-variation distance, proving the joint claim.

**5. Strict radial monotonicity and the boundary layer.** Set \(q=r^2\). Apart from a positive constant,
\[
c(r)=\frac2{\pi^2}\int_0^{\pi/2}\frac{1-q}{\sqrt{1-q\sin^2t}}\,dt.
\]
The derivative of the integrand with respect to \(q\) equals
\[
\frac{-1+\frac12(1+q)\sin^2t}{(1-q\sin^2t)^{3/2}},
\]
which is strictly negative for every \(0\le q<1\). This proves strict decrease, including comparison with \(r=0\). The standard endpoint expansion \(K(r)=\log(4/\sqrt{1-r^2})+O((1-r^2)\log(1/(1-r^2)))\) gives the stated asymptotic for \(c(r)\). Moreover \(g_r\) assigns vanishing mass to any closed angular set avoiding \(0\) and \(\pi\), since its numerator remains bounded there while \(K(r)\to\infty\). Symmetry forces the two limiting masses to be \(1/2\) each.

**6. Moment transition.** Since \(c(r)>0\) for \(r<1\), the tail integral identity \(\mathbb E[Z]=\int_0^\infty\Pr(Z>t)dt\) for nonnegative \(Z\) gives \(\mathbb E[S]=\mathbb E[R]=\infty\). In fact all positive moments of order at least one diverge and those below one are finite. For \(r=1\) the three points lie on the unit circle almost surely and their unique circumcenter is its center with circumradius one.

## Verification
The separate file `circumcenter_verify.py` solves the two perpendicular-bisector equations directly for \(1{,}200{,}000\) independent pairs of Cartesian circle points at each of four fixed vertices. It compares Monte Carlo tail probabilities against a numerically integrated exact *clipped-arccos* formula, checks the special centered case, verifies the elliptic normalization of the limiting angular density, checks an anisotropic angular Fourier moment, and tests the sharp logarithmic coefficient trend. Running `python circumcenter_verify.py` with NumPy and SciPy yields `MIXED_CIRCLE_CIRCUMCENTER_NUMERIC_CHECKS_OK`. These simulations are only consistency diagnostics. The analytic proof above, not finite sampling or a numerical limit, establishes the statements.

## Relationship to prior work
Edelman and Strang [1] develop random triangle shape theory and compare several random-triangle sampling schemes, including angle-uniform and Gaussian configurations. Their inspected Section 3.3 treats acute-triangle probabilities for Gaussian-derived shape distributions; it does not provide a tail law or directional mark for the model of one fixed interior vertex and two independent circle-boundary vertices. The elementary circle-chord arcsine law is classical and is not claimed as new.

A published joint circumradius–circumcenter density for three *area-uniform disk points* [2] gives an exact law for an absolutely continuous, three-vertex sampling model. A published universal marked large-circumradius theorem for three area-uniform vertices in convex bodies [3] identifies a sixth-power chord bias and a Dirichlet gap law. Neither theorem implies the present elliptic intensity, radial extremality, or angular localization, because the present sampling measure is singular with two boundary vertices and one deterministic vertex. Classical work on random triangle shape and collinearity, especially Kendall [4], is a priority risk; its accessible abstract concerns identically distributed area-uniform vertices, while the full text was not obtained. The novelty claim is confined to this mixed fixed/boundary law and its displayed consequences, not generic near-collinearity theory, the arcsine density, or elliptic-integral asymptotics.

## Limitations
No uniform large-\(T\) remainder is asserted as \(r\uparrow1\). The model is limited to exactly two independent, arclength-uniform circle vertices and one fixed interior vertex. The sharp radial comparison concerns the **tail coefficient**, not stochastic ordering of the full circumcenter-distance distributions at all thresholds. The actual angle at \(r=1\) is undefined because \(O=0\); only the limiting rare-event angle densities are compared. Historical novelty remains provisional against older, unindexed literature and the inaccessible full text of Kendall [4]. The numerical diagnostics do not constitute an independent mathematical certification.

## References
[1] A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053v1, first public January 9, 2015, https://arxiv.org/pdf/1501.03053.

[2] *The joint circumradius–circumcenter law for three uniform points in a disk*, published mathematical research record, November 1, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-joint-circumradius-circumcenter-law-for-three-uniform-points--06c38ac25e1d.

[3] *A universal marked large-circumradius law for three random points in a convex body*, published mathematical research record, October 25, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-universal-marked-large-circumradius-law-for-three-random-point--ddc53a9069e0.

[4] D. G. Kendall, *Exact distributions for shapes of random triangles in convex sets*, Advances in Applied Probability 17 (1985), 308–329, DOI:10.2307/1427143; full text not accessed.
