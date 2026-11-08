# The sharp three-regime circumradius law of random planar cube shadows

## Finding
Let \(Q=[-1,1]^3\), let \(U\) be uniformly distributed on the unit sphere \(S^2\), and let \(K_U\) be the orthogonal image of \(Q\) on \(U^\perp\). Denote its **Euclidean circumradius** by \(R\), measured within the projection plane. Then \(\sqrt2\le R\le\sqrt3\), with no atoms. The following provides its complete law as a single elementary one-dimensional quadrature, a sharp interior change of differentiability, and both endpoint powers.

For \(0\le t\le1\), \(0\le\varphi\le\pi/4\), put
\[
q=\cos\varphi+\sin\varphi,\quad
B=\frac{\cos\varphi}{\sqrt{1+\cos^2\varphi}},\quad
\tau=\frac{\sin\varphi}{\sqrt{1+\cos^2\varphi}},
\]
\[
A_\pm(t,\varphi)=\frac{\pm t+q\sqrt{1+q^2-t^2}}{1+q^2}.
\]
Define
\[
G(t)=\frac{12}{\pi}\int_0^{\pi/4}\!\left[
1-A_+(t,\varphi)+\mathbf1_{\{t<\tau(\varphi)\}}
\bigl(A_-(t,\varphi)-B(\varphi)\bigr)
\right]d\varphi.
\]
The complete cumulative distribution is
\[
\boxed{\Pr(R\le r)=G(\sqrt{3-r^2}),\qquad \sqrt2\le r\le\sqrt3.}
\]
It is zero below \(\sqrt2\) and one above \(\sqrt3\). The positive-part integral \(G_+(t)=12\pi^{-1}\int_0^{\pi/4}(1-A_+(t,\varphi))d\varphi\) is real analytic near \(t_*=1/\sqrt3\), and
\[
G(t)=G_+(t)+\frac{9\sqrt3}{4\pi}(t_*-t)_+^2+O((t_*-t)_+^3)
\]
near \(t_*\), where \(x_+=\max\{x,0\}\). Consequently the distribution function is continuously differentiable but not twice continuously differentiable at the single interior point
\[
\boxed{r_*=\sqrt{8/3},\qquad
F_R''(r_*+)-F_R''(r_*-)=\frac{36\sqrt3}{\pi}.}
\]
Finally, as \(\varepsilon\downarrow0\),
\[
\boxed{\Pr(R\le\sqrt2+\varepsilon)\sim\frac6\pi\varepsilon^2,\quad
\Pr(R>\sqrt3-\varepsilon)\sim4\sqrt{\frac2{\sqrt3}}\sqrt\varepsilon.}
\]
These results are specific to the circumradius of a *projected cube*; the inradius of a projected cube and the circumradius of a central cube section are different observables.

## Assumptions and scope
All lengths use the Euclidean metric. The cube has vertices \((\pm1,\pm1,\pm1)\). Orthogonal projection planes pass through the origin and follow Haar probability on the Grassmannian of two-planes in \(\mathbb R^3\), equivalently their unoriented normal is represented by a uniformly distributed \(U\in S^2\). For a compact convex set \(K\) in its affine hull, the circumradius is the radius of its smallest enclosing Euclidean disk. Because \(K_U\) is centrally symmetric, an enclosing disk of optimal radius can be centered at its origin, and the circumradius equals the largest norm of a projected vertex. Exceptional normals with coordinate ties have probability zero; deterministic formulas extend to them by continuity.

## Proof
**1. Deterministic reduction.** Every projected vertex is \(P_{U^\perp}v=v-(U\cdot v)U\), whence \(\|P_{U^\perp}v\|_2^2=3-(U\cdot v)^2\). For centrally symmetric \(K_U\), the origin-centered smallest enclosing disk is optimal: if a disk centered at \(z\) with radius \(r\) contains \(K_U\), the disk at \(-z\) also does, and the intersection/convex average argument gives the disk at zero with radius \(r\). Thus \(R^2=3-\min_{v\in\{\pm1\}^3}(U\cdot v)^2\). Let \(a\ge b\ge c\ge0\) be the ordered absolute values of the coordinates of \(U\). Up to simultaneous sign reversal, the four candidate absolute values are \(a+b+c\), \(a+b-c\), \(a-b+c\), and \(|a-b-c|\). Since \(a-b\ge0\), \(b\ge c\), both \(|a-b-c|\le a-b+c\) and \(|a-b-c|\le a+b-c\). Hence
\[
\boxed{R^2=3-(a-b-c)^2.}
\]
For unit \(U\), \(|a-b-c|\le1\): when \(a\ge b+c\), it is at most \(a\); otherwise it is at most \(c\) because \(a\ge b\). Equality is attained at coordinate axes, while zero occurs along directions with \(a=b+c\). This proves the exact support.

**2. Spherical chamber and exact quadrature.** The unit sphere has 48 congruent sign-and-order chambers, each represented (off null boundaries) by \(a\ge b\ge c\ge0\). Parametrize one by
\[
(a,b,c)=(\cos\theta,\sin\theta\cos\varphi,\sin\theta\sin\varphi),\quad
0\le\varphi\le\pi/4,\quad0\le\theta\le\Theta(\varphi)=\arctan(1/\cos\varphi).
\]
Spherical area measure is \(\sin\theta\,d\theta\,d\varphi\). The signed coordinate gap is \(f(\theta,\varphi)=a-b-c=\cos\theta-q\sin\theta\), strictly decreasing in \(\theta\) throughout this chamber. Its value at \(\theta=0\) is \(1\), and at \(\theta=\Theta\) is \(-\tau(\varphi)\). The equation \(f=t\) has a unique solution \(\theta_+\) in the chamber and \(\cos\theta_+=A_+(t,\varphi)\). The equation \(f=-t\) has a solution \(\theta_-\le\Theta\) if and only if \(t\le\tau\), and then \(\cos\theta_-=A_-(t,\varphi)\). The spherical area of \(|f|\ge t\) in the chamber is therefore
\[
\int_0^{\pi/4}\left[(1-\cos\theta_+)+\mathbf1_{\{t<\tau\}}(\cos\theta_- -\cos\Theta)\right]d\varphi.
\]
Multiplying by \(48/(4\pi)=12/\pi\) produces \(G(t)=\Pr(|a-b-c|\ge t)\). The change \(t=\sqrt{3-r^2}\) proves the complete cumulative law. Each positive threshold level has zero spherical area, so the distribution has no atoms, including its endpoints.

**3. First interior transition.** The threshold \(\tau(\varphi)\) increases strictly from zero to \(t_*=1/\sqrt3\) on \([0,\pi/4]\). The positive branch \(G_+\) is analytic near \(t_*\); only the negative branch turns on below \(t_*\). Write \(\eta=t_*-t>0\), and \(h=\pi/4-\varphi\). Taylor expansion gives
\[
\tau(\pi/4-h)=t_*-\frac4{3\sqrt3}h+O(h^2).
\]
At the corner \((\varphi,\theta)=(\pi/4,\Theta(\pi/4))\), the derivative of \(f\) in \(\theta\) is \(-2\sqrt{2/3}\), while \(\sin\Theta=\sqrt{2/3}\). Consequently
\[
A_-(t,\varphi)-B(\varphi)=\frac12(\tau(\varphi)-t)+O((\tau(\varphi)-t)^2+|h|(\tau(\varphi)-t))
\]
uniformly on the shrinking contributing interval \(0\le h\le (3\sqrt3/4)\eta+O(\eta^2)\). Integrating gives the extra mass
\[
\frac{12}{\pi}\left(\frac12\int_0^{(3\sqrt3/4)\eta}(\eta-\tfrac4{3\sqrt3}h)\,dh+O(\eta^3)\right)
=\frac{9\sqrt3}{4\pi}\eta^2+O(\eta^3).
\]
There are no other interior transitions because \(\tau\) is strictly monotone and the integral boundaries and integrands are smooth away from its endpoint. Since \(dt/dr=-r/t=-2\sqrt2\) at \(r_*\), the additional right-hand quadratic coefficient for the cumulative law is \(18\sqrt3/\pi\), yielding the claimed second-derivative jump.

**4. Lower endpoint.** Near each of the six coordinate axes on \(S^2\), use tangent coordinates \((y,z)\). The gap has \(|a-b-c|=1-|y|-|z|+O(y^2+z^2)\). Thus \(\Pr(|a-b-c|\ge1-\delta)=6\cdot(2\delta^2)/(4\pi)+o(\delta^2)=3\delta^2/\pi+o(\delta^2)\). Substituting \(\delta=1-\sqrt{3-(\sqrt2+\varepsilon)^2}=\sqrt2\varepsilon+O(\varepsilon^2)\) gives \(6\varepsilon^2/\pi\).

**5. Upper endpoint.** The event \(|a-b-c|<t\) is exactly the union of four spherical bands \(|v\cdot U|<t\), one for each of the four unoriented cube body-diagonal sign vectors \(v\) of norm \(\sqrt3\). The normalized scalar product \(v\cdot U\) is uniform on \([-\sqrt3,\sqrt3]\), so each band has probability \(t/\sqrt3\). Distinct bands intersect along transversely crossing great circles and their pairwise overlap has area \(O(t^2)\). Inclusion-exclusion therefore gives \(\Pr(|a-b-c|<t)=4t/\sqrt3+O(t^2)\). At \(r=\sqrt3-\varepsilon\), \(t=\sqrt{2\sqrt3\varepsilon-\varepsilon^2}\); the upper endpoint coefficient follows. \(\square\)

## Verification
The accompanying standalone script `verify.py` uses only Python's standard library. It checks the deterministic formula against all eight projected cube vertices on 25,000 random directions, compares the exact integral with 100,000 independently generated Haar normals across multiple quantiles, verifies its monotonicity and endpoints, and numerically tests both boundary coefficients and the interior onset coefficient. Its successful marker is `CUBE_SHADOW_RADIUS_PHASE_LAW_OK`. The proof is analytic; finite simulations and numerical quadrature are corroboration, not a substitute for proof or a demonstration of novelty.

## Relationship to prior work
Finch's *Planar Projections and Second Intrinsic Volume* (2012, arXiv:1203.2464), inspected in its available full HTML text, computes moments and joint behavior of area and perimeter of planar cube shadows, not their circumradius distribution or its singularity. The published *Exact inradius law for random planar projections of the regular octahedron* is a different polar statistic: it gives the circumradius of a **central cube section**, rather than that of a **cube projection**. The published *Exact Haar diameter law for central sections of the regular octahedron* is dual to the **inradius of a cube projection**, not to its circumradius. In contrast, polarity maps the present radius to the reciprocal of the **inradius of a central octahedron section**. Width laws, projection area moments, and face-count laws likewise do not imply a circumradius law without additional information. Classical spherical area integration and the radial reduction are standard ingredients; the complete cubical shadow law and sharp singularity statement are the proposed contribution.

## Limitations
The result is specifically for the Euclidean orthogonal projection of the three-dimensional cube, with Haar-distributed planes and the stated side-length normalization. It does not address affine sections, nonuniform viewing directions, or shadows of general convex bodies. Full historical priority remains provisional: earlier stereology or integral-geometry work may contain an equivalent tetrahedral great-circle band law under different terminology. No independent audit or validation has been performed.

## References
- S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464 (first posted 2012-03-12), https://arxiv.org/abs/1203.2464.
- M. Henk and K. Böröczky, *Random projections of regular polytopes*, Archiv der Mathematik (2000), doi:10.1007/s000130050424; background on different projection invariants.
- Published geometric research, *Exact inradius law for random planar projections of the regular octahedron*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-inradius-law-for-random-planar-projections-of-the-regular--5fbcddcea5e5.
- Published geometric research, *Exact Haar diameter law for central sections of the regular octahedron*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-diameter-law-for-central-sections-of-the-regular-octa--4948185eba2f.
