# Sharp grid-phase Hausdorff asymptotics for radially sampled superelliptic disks

## Finding
For each fixed real \(1<p<2\), consider the unit planar \(\ell_p\) disk
\[K_p=\{(x,y)\in\mathbb R^2:|x|^p+|y|^p\le1}\]
and the angle-equispaced inscribed convex polygon
\[P_{p,n}=\operatorname{conv}\{\gamma_p(2\pi j/n):0\le j<n\},\qquad
\gamma_p(\theta)=\frac{(\cos\theta,\sin\theta)}{(|\cos\theta|^p+|\sin\theta|^p)^{1/p}}.\]
Let \(E_{p,n}=d_H(K_p,P_{p,n})\), with Euclidean distance. Then
\[\boxed{\lim_{\substack{n\to\infty\\4\mid n}}\left(\frac{n}{2\pi}\right)^p E_{p,n}=\frac{p-1}{p^{1+p/(p-1)}}},\]
while
\[\boxed{\lim_{\substack{n\to\infty\\4\nmid n}}\left(\frac{n}{2\pi}\right)^p E_{p,n}=\frac{1}{p2^p}}.\]
The second constant is strictly greater than the first for every \(1<p<2\). Thus the scaled Hausdorff error has a genuine two-phase arithmetic resonance determined by whether the angular grid passes through all four coordinate-axis tips. It is an exact statement about the prescribed angular sampling rule, not the optimal polygon approximation of \(K_p\).

## Assumptions and scope
Here \(n\ge3\) is an integer tending to infinity along either of the specified two index sets, and \(p\) is **fixed** in the open interval \((1,2)\). Constants in asymptotic estimates may depend on this fixed \(p\). The set \(P_{p,n}\subset K_p\) is a convex polygon with its distinct vertices listed counterclockwise. The Hausdorff metric is induced by the Euclidean norm, not the \(\ell_p\) gauge. The same points, radial parametrization, and angular sampling occur in Fodor–Minuță (2026, Section 5); only the present error constants are asserted here.

## Proof
**1. Reduction to chord gaps.** Write \(h=2\pi/n\) and \(\theta_j=jh\). The boundary parametrization \(\gamma_p\) is continuously differentiable and regular; \(\inf_\theta\|\gamma'_p(\theta)\|_2>0\). Since its derivative is uniformly continuous, for sufficiently small \(h\) the tangent vector \(\gamma'_p(t)\) has positive dot product with the chord vector \(\gamma_p(\theta_j+h)-\gamma_p(\theta_j)\) whenever \(t\in[\theta_j,\theta_j+h]\). Thus orthogonal projection of every boundary point of this arc onto its chord line falls inside the actual chord segment. Strict convexity makes every chord an exposed polygon edge and places the intervening boundary arc strictly outside its supporting half-plane. Its distance to the convex polygon therefore equals the perpendicular distance to that chord: the half-plane supplies the lower bound and the chord segment supplies the upper bound. Since \(P_{p,n}\subset K_p\) and the distance to \(P_{p,n}\) is convex, its maximum on \(K_p\) is attained on the boundary. Consequently
\[E_{p,n}=\max_j\max_{0\le s\le1}\operatorname{dist}_2\!\left(\gamma_p(\theta_j+sh),\operatorname{line}(\gamma_p(\theta_j),\gamma_p(\theta_j+h))\right)\]
for all sufficiently large \(n\). This equality is about the unsigned line distance, which is nonnegative on each outward convex arc.

**2. The axis-tip scaling law.** Fix any coordinate-axis angle \(\alpha\in\{0,\pi/2,\pi,3\pi/2}\). Up to a Euclidean rotation, uniformly for \(t\to0\),
\[\gamma_p(\alpha+t)=\left(1-\frac{|t|^p}{p}+o(|t|^p),\ t+o(t)\right).\]
For a chord whose initial angle is \(\alpha+uh\), with \(u\) fixed and its other endpoint \(\alpha+(u+1)h\), the rescaled outward normal gap converges **uniformly** in \(s\in[0,1]\) to
\[\frac1p J_p(u,s),\qquad J_p(u,s)=(1-s)|u|^p+s|u+1|^p-|u+s|^p.\tag{1}\]
Indeed the chord is asymptotically tangent to the axis-tip direction, its length is \(h+o(h)\), and the horizontal graph-interpolation discrepancy is precisely \(h^p J_p(u,s)/p+o(h^p)\).

**3. Away from axes does not contribute at leading order.** Direct differentiation of the displayed radial parametrization away from the four axes yields \(\|\gamma_p''(\theta)\|_2\le C_p d(\theta)^{p-2}\), where \(d(\theta)\) is angular distance to the nearest coordinate axis. For any chord interval at least \(Nh\) from every axis, the vector linear-interpolation error, hence the normal gap, is bounded by \(C'_p h^2(Nh)^{p-2}=C'_p N^{p-2}h^p\). Because \(p-2<0\), this coefficient tends to zero as \(N\to\infty\). The remaining at-most-\(O(N)\) intervals per tip have fixed rescaled index \(u\) along each congruence subsequence, and formula (1) applies. Hence the required asymptotic constant is the largest attainable value of \(J_p(u,s)/p\) in these translated unit intervals.

**4. Sharp interpolation lemma.** Put \(f(t)=|t|^p\). Its locally integrable second derivative is \(f''(t)=p(p-1)|t|^{p-2}\) away from zero. The Green-kernel formula for linear interpolation reads
\[J_p(u,s)=p(p-1)\int_0^1 G_s(t)|u+t|^{p-2}\,dt,\]
where \(G_s(t)=(1-s)t\) for \(0\le t\le s\), and \(G_s(t)=s(1-t)\) for \(s\le t\le1\). For fixed \(s\), its symmetric decreasing rearrangement is the triangle \(G_s^*(t)=s(1-s)(1-2|t|)\) on \([-1/2,1/2]\), vanishing outside; the nonnegative kernel \(|u+t|^{p-2}\) is a translate of a symmetric decreasing function. Hardy–Littlewood rearrangement therefore gives
\[J_p(u,s)\le p(p-1)s(1-s)\int_{-1/2}^{1/2}(1-2|t|)|t|^{p-2}\,dt=2^{2-p}s(1-s)\le2^{-p}.\tag{2}\]
The final equality of the integrals follows by elementary integration. Equality in (2) occurs for \(u=-1/2\), \(s=1/2\), where the endpoints of the interval straddle the singularity symmetrically.

For integer \(u\), use reflection to reduce to intervals \([k,k+1]\) with integer \(k\ge0\). Because \(p-2<0\), the integrand \((k+t)^{p-2}\) decreases pointwise with \(k\), so the largest such interpolation gap occurs for \(k=0\). Here \(J_p(0,s)=s-s^p\); differentiating gives the unique maximizing \(s=p^{-1/(p-1)}\), and
\[\max_{k\in\mathbb Z,\ 0\le s\le1}J_p(k,s)=(p-1)p^{-p/(p-1)}.\tag{3}\]

**5. Grid arithmetic and assembly.** If \(4\mid n\), every coordinate-axis tip occurs at an angular sample, so all near-tip interval origins \(u\) are integers. Equations (1), (3), and the tail estimate in Step 3 give the first asserted limit. If \(4\nmid n\), at least one tip is the midpoint of two consecutive sample angles: take the tip at angle \(\pi\) when \(n\) is odd, and the tip at \(\pi/2\) when \(n\equiv2\pmod4\). Its straddling interval has \(u=-1/2\) and realizes \(J_p=2^{-p}\) asymptotically; (2) bounds every other possible interval. This proves the second limit.

Strict inequality of the two constants follows because the universal maximum in (2) is attained only at a centered interval, whereas the integer-grid interval maximum in (3) is smaller for \(1<p<2\). In the endpoint circle case \(p=2\), both constants coincide at \(1/8\), consistent with the classical regular-polygon expansion \(1-\cos(\pi/n)\sim(2\pi/n)^2/8\).

## Verification
A self-contained numerical verifier is supplied as `verify_superellipse.py`. It forms the prescribed polar-grid polygon, computes a second representation of its Hausdorff error by maximizing the difference of support functions \(h_{K_p}(v)-h_{P_{p,n}}(v)\), and compares the resulting errors with both asymptotic constants for several fixed exponents and congruence classes. It also checks the exact algebraic interpolation maxima by one-dimensional optimization. The numerical computations are finite, sampled, and sensitive to tolerance; the universal limits and rearrangement bound are proved above and do not depend on the experiment.

## Relationship to prior work
Fodor and Minuță, *An algorithm for approximating the metric projection onto a superelliptic disk* (arXiv:2605.24599, initial public version 2026-05-23), Section 5, use exactly this radial image of the equally spaced roots of unity; Theorem 5.5 proves convergence but supplies no \(n^{-p}\) sharp asymptotic, no leading constants, and no divisibility-by-four dichotomy. Their introduction explicitly defers detailed error estimates. Glasauer and Schneider, *Asymptotic approximation of smooth convex bodies by polytopes* (1996), give curvature-based asymptotics for \(C^2_+\) bodies; their assumptions fail here because \(\gamma_p''\) has a singularity at the four axis tips for \(1<p<2\). Their optimal/prescribed-density frameworks also do not specify the present fixed angular grid. These comparisons do not establish universal historical novelty; a specialized older sampling theorem could conceivably imply this exact case.

## Limitations
The asymptotic holds for each **fixed** \(p\in(1,2)\), not uniformly as \(p\to1\) or \(p\to2\). No claim is made for non-unit semiaxes, shifted sampling phases, arbitrary sampling densities, higher dimensions, or the sharp error of the metric-projection algorithm itself. Numerical checks are corroborative and cannot certify all indices or exponents. Historical priority against every specialized approximation-theory formulation remains open to expert comparison.

## References
1. V.-A. Fodor and V.-A. Minuță, *An algorithm for approximating the metric projection onto a superelliptic disk*, arXiv:2605.24599v1 (2026-05-23), v2 (2026-10-04). https://arxiv.org/html/2605.24599v2
2. S. Glasauer and R. Schneider, *Asymptotic approximation of smooth convex bodies by polytopes*, Forum Mathematicum 8 (1996), 363–377. https://www.tha.de/~glasauer/publ/glasschn.pdf
3. M. A. López and S. Reisner, *Hausdorff approximation of convex polygons*, Computational Geometry 32 (2005), 139–158. https://doi.org/10.1016/j.comgeo.2005.02.002
