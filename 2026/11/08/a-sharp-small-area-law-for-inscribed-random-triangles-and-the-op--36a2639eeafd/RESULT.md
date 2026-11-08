# A sharp small-area law for inscribed random triangles and the optimal affine sampling density

## Finding
Let \(\Gamma\) be a positively oriented, simple, closed, strictly convex \(C^3\) plane curve, parametrized by Euclidean arclength \(s\in\mathbb R/L\mathbb Z\), with perimeter \(L>0\) and curvature \(\kappa(s)>0\). Let \(f\) be any strictly positive \(C^1\) probability density with respect to \(ds\). Sample three independent points on \(\Gamma\) with density \(f\), and let \(T\) be the (unsigned) Euclidean area of their triangle. Define
\[
B=B(1/3,1/3)=\frac{\Gamma(1/3)^2}{\Gamma(2/3)},\qquad K=3\,4^{2/3}B.
\]
Then the exact leading small-area law is
\[
\boxed{\lim_{t\downarrow0}\frac{\Pr(T\le t)}{t^{2/3}}=K\int_0^L f(s)^3\kappa(s)^{-2/3}\,ds.}
\]
The coefficient is finite and positive. Among all such probability densities, it is uniquely minimized by the normalized affine arclength density
\[
\boxed{f_*(s)=\frac{\kappa(s)^{1/3}}{S},\qquad S=\int_0^L\kappa(s)^{1/3}\,ds,\qquad C(f_*)=\frac{K}{S^2}.}
\]
For uniform arclength sampling \(f=1/L\), at fixed \(L\) the coefficient satisfies the sharp circle inequality
\[
\boxed{C(1/L)=\frac{K}{L^3}\int_0^L\kappa(s)^{-2/3}\,ds\ \ge\ \frac{K}{(2\pi)^{2/3}L^{4/3}},}
\]
with equality precisely for circles. Moreover, for every real \(p>0\), \(\mathbb E[T^{-p}]<\infty\) if and only if \(p<2/3\).

## Assumptions and scope
The curve is embedded, closed, counterclockwise, and \(C^3\) with everywhere positive Euclidean curvature. Sampling is independent with a fixed (not \(t\)-dependent), positive \(C^1\) arclength density \(f\), normalized by \(\int_0^L f=1\). The triangle's area is ordinary unsigned Euclidean area; the threshold \(t\) has units of area. The result is a limit for a fixed curve and density, not uniform over families approaching zero curvature or over density sequences. The constant \(K\) is universal. When \(f=1/L\), the circle inequality compares curves of the same Euclidean perimeter, not equal area.

## Proof
**1. Exact gap parametrization.** Label the first sampled arclength coordinate \(s\), and order the two remaining sampled coordinates counterclockwise from it, writing \(s+a\) and \(s+a+b\) modulo \(L\), with \(a,b>0\) and \(a+b<L\). Accounting for the two assignments of the remaining labels gives, for any symmetric triple event \(E\),
\[
\Pr(E)=2\int_0^L\!ds\int_{\substack{a,b>0\\a+b<L}}\!da\,db\ f(s)f(s+a)f(s+a+b)\,{\bf1}_E.
\]
The three cyclic gaps are \(a,b,c=L-a-b\). Their degeneracy locations are the three corners where two gaps simultaneously approach zero, plus the open edges where just one gap approaches zero.

**2. Uniform local determinant.** Let \(\gamma\) be the unit-speed parametrization, and \(V(u)=\gamma'(u)\). The positively oriented triangular area of the consecutive points is
\[
T(s,a,b)=\tfrac12\int_0^a\!du\int_a^{a+b}\!dv\,\det(V(s+u),V(s+v)).
\]
For \(a+b\le\delta\), the turning angle of \(V\) is the integral of \(\kappa\), and \(\det(V(s+u),V(s+v))=\sin(\int_{s+u}^{s+v}\kappa(z)dz)\). Since \(\kappa\) is continuous and positive on the compact curve, uniformly in \(s\) and \(0\le u\le a\le v\le a+b\le\delta\), this equals \(\kappa(s)(v-u)(1+o_\delta(1))\), where \(o_\delta(1)\to0\) as \(\delta\downarrow0\). The elementary double integral is \(\int_0^a\int_a^{a+b}(v-u)\,dv\,du=ab(a+b)/2\). Hence
\[
T(s,a,b)=\frac{\kappa(s)}4\,ab(a+b)\,(1+o_\delta(1))
\]
uniformly including highly unequal \(a,b\) (for positive \(a,b\)). Analogous expansions hold at the other two gap-simplex corners after cyclically choosing the local starting point. The density product there is \(f(s)^3(1+o_\delta(1))\).

**3. Area of the universal cusp sublevel set.** For \(u,v>0\), put \(w=u+v\) and \(z=u/(u+v)\). The Jacobian is \(w\), while \(uv(u+v)=z(1-z)w^3\). Thus
\[
\begin{aligned}
\operatorname{Leb}_2\{(u,v)>0:uv(u+v)\le1\}
&=\frac12\int_0^1[z(1-z)]^{-2/3}\,dz\\
&=\frac12 B(1/3,1/3).
\end{aligned}
\]
The integral is finite at both endpoints. The region \(ab(a+b)\le 4t/\kappa(s)\) therefore has full-quadrant area \(\tfrac12 B(4t/\kappa(s))^{2/3}\). Restricting to \(a+b<\delta\) does not change its leading coefficient: scale \((a,b)=t^{1/3}(u,v)\) and apply monotone convergence to the integrable full-quadrant indicator.

**4. All noncorner configurations are lower order.** Fix \(0<\delta<L/5\), and separate the three regions where two cyclic gaps are below \(\delta\). Outside these regions, either all three gaps are bounded away from zero, or exactly one gap tends to zero while the other two remain separated by \(\delta\). Strict convexity makes the area strictly positive on the compact all-separated set. Along the compact interior of each simplex edge, the area vanishes linearly in the unique small gap: its coefficient is the positive distance from the noncolliding third boundary point to the tangent at the colliding pair (times the appropriate positive factor). Uniform compactness gives a lower bound \(T\ge c_\delta\min(a,b,c)\) for sufficiently small single gaps. Since \(f\) is bounded, the sublevel probability contributed by this complement is \(O_\delta(t)=o(t^{2/3})\).

**5. Combine the three corners.** For each fixed small \(\delta\), the determinant/density bounds sandwich each corner contribution between factors converging to one as \(\delta\downarrow0\), times
\[
2\cdot\frac{B}{2}\,4^{2/3}t^{2/3}\int_0^L f(s)^3\kappa(s)^{-2/3}ds.
\]
There are three corners with identical integrated contribution (translate the local starting point cyclically). The complement is negligible by Step 4. First take \(t\downarrow0\), then \(\delta\downarrow0\). This yields \(3\cdot4^{2/3}B\int f^3\kappa^{-2/3}\) as claimed.

**6. Optimal density.** Hölder's inequality, with \(S=\int\kappa^{1/3}\,ds\), gives
\[
1=(\int f\,ds)^3\le\left(\int f^3\kappa^{-2/3}ds\right)S^2.
\]
Equality forces \(f(s)\propto\kappa(s)^{1/3}\) almost everywhere, hence everywhere by continuity. Normalization gives the displayed unique optimizer and coefficient \(K/S^2\).

**7. Sharp circle inequality.** The turning-tangent theorem gives \(\int_0^L\kappa\,ds=2\pi\). Jensen applied to the strictly convex function \(x\mapsto x^{-2/3}\) gives \(L^{-1}\int\kappa^{-2/3}ds\ge(2\pi/L)^{-2/3}\), with equality only for constant curvature, hence a circle. Substitution proves the fixed-perimeter inequality.

**8. Negative moments.** A bounded positive random variable with \(\Pr(T\le t)\sim Ct^{2/3}\), where \(0<C<\infty\), has \(\mathbb E[T^{-p}]<\infty\) precisely when \(p<2/3\), by the layer-cake integral at zero. This completes the proof.

## Verification
A standalone checker `verify.py` independently evaluates the circular law by one-dimensional quadrature of the exact circular-gap area expression, tests convergence of \(\Pr(T\le t)/t^{2/3}\) to \(C_{\mathrm{circle}}=3\,2^{-2/3}B/\pi^2\approx1.01485466525844\) for the unit circle, calculates ellipse coefficients by independent numerical integration of their curvature and speed, and compares direct Monte Carlo triangle areas against the derived coefficients.

For an ellipse \((a\cos\theta,b\sin\theta)\), \(S=2\pi(ab)^{1/3}\). With semiaxes \((a,b)=(2,1)\), arclength-uniform sampling gives \(C\approx0.73668626639\), while the unique optimal affine-arclength density corresponds to uniform \(\theta\) and gives \(C_*\approx0.63931837767\). At threshold \(t=0.0007\), direct simulation of 1,500,000 triangles per sampling law gave ratios to \(Ct^{2/3}\) of approximately \(0.9753\) and \(1.0115\) respectively; the unit-circle control gave \(1.0007\). Finite simulations do not prove a limiting law.

Reproduce using `python verify.py` with NumPy and SciPy. The exact constants and analytical convergence require no external code.

## Relationship to prior work
The standard circle-triangle area identity, integral moments, and the arclength-uniform circle model are classical (Weisstein's MathWorld entry; additional moment discussion on MathOverflow). The special circle case by itself is not claimed as new: known full moment sequences determine its compactly supported distribution. Craizer, Teixeira, and da Silva (arXiv:1103.2722, first posted 2011-03-14) study convex equal-area polygons and approximation by equidistributed affine-arclength points, but do not establish the three-independent-point rare-area probability, the general \(\int f^3\kappa^{-2/3}\) coefficient, or its variational optimization. Jiang, Li, and Vitányi (arXiv:math/9902043, first posted 1999-02-05) study the minimum-area triangle among many interior-uniform points in a square, not three boundary-independent samples on a smooth curve. The present conclusion connects the familiar affine arclength measure with a different, explicitly quantified rare-event optimality problem.

## Limitations
No rate of convergence beyond \(o(t^{2/3})\) is asserted. The theorem does not cover flat points, corners, self-intersections, correlated points, arbitrary singular sampling measures, or curves with vanishing curvature. The circle-tail behavior is a known-model consistency check and is not independently claimed as original. Historical priority over unindexed general geometric sublevel-distribution results is unverified; independent mathematical validation has not been performed.

## References
1. M. Craizer, R. C. Teixeira, M. A. H. B. da Silva, *Affine Properties of Convex Equal-Area Polygons*, arXiv:1103.2722 (first public version 2011-03-14), especially Sec. 2 and Sec. 3.3. https://arxiv.org/abs/1103.2722
2. T. Jiang, M. Li, P. Vitányi, *The Average-Case Area of Heilbronn-Type Triangles*, arXiv:math/9902043 (first public version 1999-02-05). https://arxiv.org/abs/math/9902043
3. E. W. Weisstein, *Circle Triangle Picking*, MathWorld. https://mathworld.wolfram.com/CircleTrianglePicking.html
4. J. Propp, I. Pinelis, J. C. Baez, and contributors, *Moments of area of random triangle inscribed in a circle*, MathOverflow, 2018. https://mathoverflow.net/questions/304970/moments-of-area-of-random-triangle-inscribed-in-a-circle
