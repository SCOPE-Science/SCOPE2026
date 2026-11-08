# Curvature–width Pareto law for bounded random tangent polygons

## Finding
Let \(K\subset\mathbb R^2\) be a compact strictly convex body with a \(C^2\) boundary of everywhere positive curvature. Fix an integer \(n\ge3\). At \(n\) independent boundary points sampled uniformly by arclength, take the supporting tangent half-planes that contain \(K\); let \(P_n\) be their intersection. Write \(B_n=\{P_n\text{ is bounded}\}\) and let \(A_n\) be the Euclidean area of \(P_n\) on \(B_n\).

Choose any origin inside \(K\). Let \(h(\theta)\) be its support function and define
\[
\rho(\theta)=h(\theta)+h''(\theta)>0,\quad
L=\int_0^{2\pi}\rho(\theta)\,d\theta,\quad
w(\theta)=h(\theta)+h(\theta+\pi),\quad
H(\theta)=\frac1L\int_{\theta+\pi}^{\theta+2\pi}\rho(\phi)\,d\phi.
\]
All angular functions are \(2\pi\)-periodic. The boundedness probability is exactly
\[
 p_n=\Pr(B_n)=1-\frac nL\int_0^{2\pi}\rho(\theta)H(\theta)^{n-1}\,d\theta>0.
\]
**The fixed-sample Pareto coefficient** is
\[
\boxed{\lim_{t\to\infty}t\Pr(A_n>t\mid B_n)
=\frac{n(n-1)}{2p_n L^2}\int_0^{2\pi}
\rho(\theta)\rho(\theta+\pi)H(\theta)^{n-2}w(\theta)^2\,d\theta=:C_n(K)>0.}
\]
Here \(t\) has units of area. For every real \(q>0\), \(\mathbb E[A_n^q\mid B_n]<\infty\) exactly when \(q<1\). Thus boundedness conditioning does not make the mean area finite.

The proof actually allows any strictly positive continuous density \(f\) for the independent outward-normal angles: replace \(\rho/L\) by \(f\) in the two formulas, with \(H(\theta)=\int_{\theta+\pi}^{\theta+2\pi}f(\phi)\,d\phi\); the width \(w\) is unchanged.

**An exact constant-width distinction.** For \(h_\varepsilon(\theta)=1+\varepsilon\cos(3\theta)\), with \(0<|\varepsilon|<1/8\), the corresponding smooth strictly convex body has constant width \(2\). Writing \(\eta=8\varepsilon\), arclength sampling with \(n=3\) gives
\[
 p_3=\frac14-\frac{\eta^2}{6\pi^2},\qquad
 C_3=\frac{3(1-\eta^2/2)}{\pi\left(\frac14-\frac{\eta^2}{6\pi^2}\right)}<\frac{12}{\pi}.
\]
The unit disk, despite the identical width function, has \(C_3=12/\pi\). Hence the tail coefficient detects sampling-curvature structure beyond width alone.

## Assumptions and scope
The body is \(C^2\), strictly convex and has curvature bounded above and below by positive constants. The \(n\) tangent half-planes are independent; there is no independent random offset. The supporting points are selected using normalized boundary arclength, equivalently the normal-angle density \(f=\rho/L\). All probabilities are population quantities. Degenerate coincident sample points and exact antipodal normal pairs occur with probability zero. The asymptotics are for fixed \(K,n\) and area threshold \(t\to\infty\), not for \(n\to\infty\).

## Proof
**1. Angular reduction and boundedness.** In the outward-normal parametrization, a boundary point is \(h(\theta)u_\theta+h'(\theta)v_\theta\), where \(u_\theta=(\cos\theta,\sin\theta)\) and \(v_\theta=(-\sin\theta,\cos\theta)\). Its arclength derivative has magnitude \(\rho(\theta)=h+h''\). Thus iid arclength points have iid normal angles of density \(f(\theta)=\rho(\theta)/L\).

Order these angles cyclically, with successive counterclockwise gaps \(g_1,\ldots,g_n>0\) summing to \(2\pi\). The intersection of the inward supporting half-planes is bounded if and only if the outward normals are not contained in any closed semicircle, equivalently \(g_i<\pi\) for every \(i\). At most one gap can be \(\ge\pi\), outside a null set. Choosing its starting sample point and requiring all other sample normals to lie in the complementary semicircle gives
\[
 \Pr(B_n^c)=n\int_0^{2\pi}f(\theta)
 \left(\int_{\theta+\pi}^{\theta+2\pi}f(\phi)\,d\phi\right)^{n-1}d\theta.
\]
The event \(B_n\) has positive probability because \(f>0\) and neighborhoods of the \(n\) equally spaced normal directions yield bounded intersections.

**2. Vertex growth near one semicircular gap.** Take \(g_i=\pi-\delta\) with \(\delta\downarrow0\), starting at angle \(\theta\). Let \(q_i\) be the intersection of the two consecutive supporting lines. In the frame \((u_\theta,v_\theta)\), their equations give
\[
q_i=h(\theta)u_\theta+
\frac{h(\theta+\pi-\delta)-h(\theta)\cos(\pi-\delta)}{\sin(\pi-\delta)}v_\theta
=\frac{w(\theta)}\delta v_\theta+O(1).
\]
If all other gaps are at most \(\pi-\epsilon\), the other vertices remain uniformly bounded, even if some of their gaps approach zero. The predecessor \(q_{i-1}\) lies on the tangent at \(\theta\); the successor \(q_{i+1}\) lies on the tangent at \(\theta+\pi-\delta\). Consequently their projections along \(u_\theta\) differ by \(-w(\theta)+o(1)\). The two shoelace terms involving \(q_i\) contribute \(w(\theta)^2/(2\delta)+o(1/\delta)\), and all other terms are bounded. Uniformly on this restricted parameter region,
\[
\delta A_n\longrightarrow\frac{w(\theta)^2}{2}.
\]

**3. Dominating singularities and exclusion of double extremes.** Because \(K\) contains a positive-radius disk and lies inside a finite-radius disk centered at the origin, all support heights are positive and uniformly bounded. A pair of consecutive support lines with gap \(g\in(0,\pi)\) intersects at a point whose distance is at most \(M/(\pi-g)\): this follows from the preceding explicit intersection formula, the bounded derivative of \(h\), and \(|\sin g|\ge c\min(g,\pi-g)\). Every sampled tangent actually forms a side of \(P_n\), since it supports \(K\) at a distinct contact point. The area formula \(A_n=\frac12\sum h(\theta_i)\ell_i\), where \(\ell_i\) is the length of that polygon side, therefore implies
\[
0<A_n\le M'\sum_{i=1}^n\frac1{\pi-g_i}.
\]
Thus \(A_n>t\) forces at least one gap to satisfy \(\pi-g_i<nM'/t\). With the angular density bounded, the joint probability of one such gap and a different gap with \(\pi-g_j<\epsilon\) is \(O(t^{-1}\epsilon^{n-2})+o(t^{-1})\). Indeed, the remaining \(n-2\) nonnegative gaps must then sum to less than \(\epsilon+nM'/t\); their simplex cross-section has volume of order \((\epsilon+nM'/t)^{n-3}\) (for \(n=3\), this factor is \(1\)). Hence their contribution to \(t\Pr(A_n>t,B_n)\) vanishes as \(\epsilon\downarrow0\). This excludes double-extreme errors rather than assuming independence of the gaps.

**4. Probability flux into a single near-semicircular gap.** For a specified ordered pair of distinct sampled normals at angles \(\theta\) and \(\theta+g\), the probability density that they are successive counterclockwise samples is
\[
n(n-1)f(\theta)f(\theta+g)
\left(1-\int_\theta^{\theta+g}f(\phi)\,d\phi\right)^{n-2}d\theta\,dg.
\]
When \(g=\pi-\delta\) and \(\delta\downarrow0\), this density tends uniformly to \(n(n-1)f(\theta)f(\theta+\pi)H(\theta)^{n-2}\). On the boundedness event, all other gaps are below \(\pi\) except a boundary set whose conditional measure tends to zero. By Step 2, on configurations with no second near-semicircular gap the event \(A_n>t\) has, to leading order, \(0<\delta<w(\theta)^2/(2t)\). Integrating this flux and then using Step 3 to remove the gap exclusion gives
\[
\lim_{t\to\infty}t\Pr(A_n>t,B_n)
=\frac{n(n-1)}2\int_0^{2\pi}f(\theta)f(\theta+\pi)H(\theta)^{n-2}w(\theta)^2d\theta.
\]
Dividing by \(p_n\) yields the theorem. Every factor is positive and bounded, so the constant is strictly positive and finite.

**5. Moments and constant width.** The tail integral \(\mathbb E[A_n^q\mid B_n]=q\int_0^\infty t^{q-1}\Pr(A_n>t\mid B_n)dt\) converges at infinity exactly when \(q<1\), proving the threshold. For \(h_\varepsilon=1+\varepsilon\cos3\theta\), we have \(\rho=1-8\varepsilon\cos3\theta\), \(L=2\pi\), \(w=2\), and \(H=1/2-\eta\sin3\theta/(3\pi)\). Orthogonality of the trigonometric terms gives \(p_3=1/4-\eta^2/(6\pi^2)\) and the displayed coefficient. Its ratio to the disk coefficient is \((1-\eta^2/2)/(1-2\eta^2/(3\pi^2))<1\) for \(0<|\eta|<1\).

## Verification
Run `python verify_tangent_tail.py` in an environment with Python, NumPy and SciPy available. The verifier recomputes the general integrals for circles, ellipses and noncircular constant-width curves, checks the closed constant-width formulas, tests \(\delta A_n\to w^2/2\) for three shapes, and compares the predicted Pareto coefficient against independent Monte Carlo samples of randomly selected supporting tangents. The analytical proof covers all smooth strictly convex bodies and every fixed \(n\ge3\); finite numerical tests do not certify the infinite-domain statement. Running the supplied code produced `VERIFY_OK`.

## Relationship to prior work
Fodor, Hug and Ziebarth (arXiv:1409.8105, first public 2014-09-29) study asymptotic expectations of *outer-truncated* random circumscribed polytopes as the number of half-spaces grows. Their support-hyperplane model also permits random offsets. The present theorem instead concerns zero-offset tangent lines, a fixed sample size and a *conditional large-area tail* with its exact coefficient. Xu (2015) studies circle-tangent random polygons and observes possible unbounded magnitudes; the circle specialization is not asserted to be new. The general curvature–width flux coefficient, fixed-sample moment dichotomy, and exact constant-width discrimination are the assessed contributions. The complete Xu article was not accessible for a whole-document priority comparison.

## Limitations
The theorem does not handle flat boundary segments, nonsmooth curves, vanishing curvature, tangent offsets, or dimension greater than two. It gives a first-order tail, not second-order error bounds, and makes no claims about estimation from finite samples. The separate issue of historical originality needs independent assessment, particularly for any inaccessible full-text treatments of random circumscribing polygons.

## References
1. F. Fodor, D. Hug, I. Ziebarth, *The volume of random polytopes circumscribed around a convex body*, arXiv:1409.8105 (publicly posted 2014-09-29), https://arxiv.org/abs/1409.8105.
2. W.-Q. Xu, *Random circumscribing polygons and approximations of π*, Statistics & Probability Letters **106** (2015), 52–57, DOI:10.1016/j.spl.2015.06.026.
