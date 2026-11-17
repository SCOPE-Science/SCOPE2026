# Sharp tangent-intersection escape and the complete constant-width stability law

## Finding
Let \(K\subset\mathbb R^2\) be a compact strictly convex body with a \(C^3\) support function \(h\) and everywhere positive curvature radius \(\rho=h+h''\). Fix the origin in its interior. Put
\[
 u_\theta=(\cos\theta,\sin\theta),\qquad
 v_\theta=(-\sin\theta,\cos\theta),\qquad
 w(\theta)=h(\theta)+h(\theta+\pi),\qquad
 P=\int_0^{2\pi}\rho(\theta)\,d\theta.
\]
Independently choose two points uniformly in boundary arclength; intersect their complete Euclidean tangent lines at the almost surely unique point \(Z\). Then
\[
 \boxed{\lim_{R\to\infty}R\,\Pr(\lVert Z\rVert>R)=
 C(K):=\frac{2}{P^2}\int_0^{2\pi}\rho(\theta)\rho(\theta+\pi)w(\theta)\,d\theta.}
\]
This coefficient is strictly positive. Consequently, for \(q>0\), the moment \(\mathbb E\lVert Z\rVert^q\) is finite if and only if \(q<1\).

There is also a **marked total-variation law**. Let \(\Theta\) be the first point's outward-normal angle, and let \(\Delta\in(-\pi,\pi]\) be the wrapped difference \(\Theta_2-\Theta-\pi\). On \(\{\lVert Z\rVert>R\}\) define \(S=\operatorname{sgn}(\Delta)\) and \(U_R=R/\lVert Z\rVert\). The conditional law of \((\Theta,S,U_R)\) converges in total variation to the product of (i) the circle-angle density
\[
 \frac{\rho(\theta)\rho(\theta+\pi)w(\theta)}{\int_0^{2\pi}\rho(t)\rho(t+\pi)w(t)\,dt},
\]
(ii) a fair sign on \(\{-1,1\}\), and (iii) an independent \(\operatorname{Uniform}(0,1)\) variable. The direction of \(Z/\lVert Z\rVert\) converges in probability, jointly with these marks, to \(-S v_\Theta\); this last directional statement is **not** asserted in total variation.

**Sharp constant-width classification.** If \(K\) has constant width \(w>0\), the leading coefficient has the exact curvature-defect identity
\[
 \boxed{\frac{w}{\pi}-C(K)=\frac{1}{2\pi^2w}
 \int_0^{2\pi}\bigl(\rho(\theta)-\rho(\theta+\pi)\bigr)^2\,d\theta.}
\]
As \(K\) varies over smooth strictly convex bodies of the same constant width, the complete attainable set of coefficients is precisely \((0,w/\pi]\). The upper endpoint occurs **only** for Euclidean disks (up to translation), and the lower endpoint is unattained but approached by smooth, positively curved constant-width ovals. In particular, equal width and equal perimeter do not determine the tangent-intersection escape law.

For a circle of radius \(a\) and \(R\ge a\), the exact finite-radius benchmark is
\[
 \Pr(\lVert Z\rVert>R)=\frac2\pi\arcsin\!\left(\frac aR\right),
\]
which has coefficient \(2a/\pi=w/\pi\).

## Assumptions and scope
The two tangent points are sampled **independently and uniformly by Euclidean boundary arclength**, not uniformly by normal angle, Crofton line measure, or random-offset halfspaces. The support function is \(C^3\) and \(\rho\) is strictly positive, so the normal parametrization is bijective and \(P\) is the perimeter. The width is positive and continuous. Parallel tangent lines occur on a null event. The asymptotic is for a fixed body and \(R\to\infty\). The origin can be translated without changing the coefficient or the limiting marks, because translating \(Z\) by a fixed vector changes its norm by at most a constant.

## Proof
**1. Exact tangent intersection and its only pole.** Since a support line at angle \(\theta\) has equation \(x\cdot u_\theta=h(\theta)\), its intersection with the line at angle \(\theta+\alpha\) is
\[
 Z=h(\theta)u_\theta+T(\theta,\alpha)v_\theta,\qquad
 T(\theta,\alpha)=\frac{h(\theta+\alpha)-h(\theta)\cos\alpha}{\sin\alpha}.
\]
For \(\alpha\to0\pmod{2\pi}\), the quotient extends continuously with value \(h'(\theta)\), uniformly in \(\theta\). The only unbounded configurations have \(\alpha=\pi+\delta\), \(\delta\to0\). Uniformly in \(\theta\), Taylor's theorem and \(w(\theta)>0\) give
\[
 T(\theta,\pi+\delta)=-\frac{w(\theta)}\delta+O_K(1),\quad
 \lVert Z\rVert=\frac{w(\theta)}{|\delta|}+O_K(1),\quad
 \partial_\delta T=\frac{w(\theta)}{\delta^2}+O_K(1).
\]
The \(C^3\) hypotheses ensure these estimates and the required derivative bounds uniformly. Away from \(\delta=0\), the intersection point is uniformly bounded. Therefore for large \(R\) the event \(\lVert Z\rVert>R\) consists of two short signed intervals with endpoints
\[
 \delta_{R,\pm}(\theta)=\pm\frac{w(\theta)}R+O_K(R^{-2}),
\]
uniformly in \(\theta\). Local monotonicity follows from the derivative estimate; it does not assume monotonicity at finite distances outside this collar.

**2. The probability flux.** Boundary arclength has element \(\rho(\theta)d\theta\), so the two normal angles have independent density \(f(\theta)=\rho(\theta)/P\). The ordered-angle pair has density \(f(\theta)f(\theta+\pi+\delta)d\theta d\delta\) on \(\theta\in[0,2\pi)\), \(\delta\in(-\pi,\pi]\). Integrate over the two intervals from Step 1. Continuity and the uniform endpoint expansion imply
\[
 \Pr(\lVert Z\rVert>R)=\frac2R\int_0^{2\pi}
 f(\theta)f(\theta+\pi)w(\theta)\,d\theta+O_K(R^{-2}).
\]
The integrand is strictly positive, establishing the coefficient and positivity. Integrating the tail against \(qR^{q-1}\) gives the stated sharp moment threshold.

**3. Joint marked law.** On each signed near-antipodal interval, the map \(\delta\mapsto U_R=R/\lVert Z\rVert\) is monotone for sufficiently large \(R\). Its inverse obeys, uniformly for \(\theta\) and \(0<U_R<1\),
\[
 \delta=S\frac{w(\theta)}R U_R+O_K(R^{-2}U_R),\qquad
 \left|\frac{\partial\delta}{\partial U_R}\right|=\frac{w(\theta)}R+O_K(R^{-2}).
\]
The transformed joint density is thus \(R^{-1}f(\theta)f(\theta+\pi)w(\theta)(1+O_K(R^{-1}))\), separately for each sign. Divide by the probability from Step 2. Pointwise and dominated density convergence on the fixed space \([0,2\pi)\times\{-1,1\}\times(0,1)\), or Scheffé's lemma, yields total-variation convergence. Since \(T\sim-w/\delta\) and \(h\) stays bounded, the normalized geometric direction converges in probability to \(-Sv_\Theta\).

**4. Exact rigidity under constant width.** If \(w(\theta)\equiv w\), then \(h(\theta)+h(\theta+\pi)=w\) and \(\rho(\theta)+\rho(\theta+\pi)=w\). Integrating the latter gives \(P=\pi w\) (Barbier's identity). Hence
\[
 \begin{aligned}
 C(K)&=\frac{2}{\pi^2w}\int_0^{2\pi}\rho(\theta)\rho(\theta+\pi)\,d\theta\\
 &=\frac{w}{\pi}-\frac{1}{2\pi^2w}\int_0^{2\pi}\bigl(\rho(\theta)-\rho(\theta+\pi)\bigr)^2d\theta.
 \end{aligned}
\]
The rightmost square vanishes exactly when \(\rho\equiv w/2\); all periodic support functions solving \(h+h''=w/2\) are \(h=w/2+A\cos\theta+B\sin\theta\), the support functions of translated disks. Positive curvature makes \(C(K)>0\) for every admissible body.

**5. Sharpness and every intermediate coefficient.** For \(0\le a<1\), \(k>0\), set
\[
 \rho_{a,k}(\theta)=\frac w2\left(1+a\tanh(k\cos3\theta)\right).
\]
These smooth radii are strictly positive, satisfy \(\rho_{a,k}(\theta)+\rho_{a,k}(\theta+\pi)=w\), and have vanishing first Fourier harmonic by threefold symmetry. Thus the periodic differential equation \(h+h''=\rho_{a,k}\) has a smooth solution; the solution can be chosen without first harmonics. Its positive radius makes it the support function of a strictly convex oval, and the antipodal identity forces width exactly \(w\). Direct substitution gives
\[
 C(K_{a,k})=\frac w\pi\left[1-\frac{a^2}{2\pi}
 \int_0^{2\pi}\tanh^2(k\cos3\theta)\,d\theta\right].
\]
Let \(a\uparrow1\) and \(k\to\infty\). Dominated convergence makes the bracket tend to zero. For each fixed \(k\), the coefficient is continuous in \(a\) and takes its maximum at \(a=0\). By choosing \(k\) sufficiently large and applying the intermediate-value theorem in \(a\), every number strictly between zero and \(w/\pi\) is attained. Zero itself is impossible by positivity.

**6. Exact circular benchmark.** On a circle, the difference between two independent tangent-normal angles is uniform modulo \(2\pi\). The intersection lies at radial distance \(a/|\cos(\alpha/2)|\), so for \(R\ge a\), integration of the angular threshold yields \(2\arcsin(a/R)/\pi\), as claimed.

## Verification
Execute `python verify_tangent_intersections.py` from this package using Python with NumPy and SciPy. This tests the exact circle formula, independently evaluates two-dimensional finite-radius angular integrals for the family \(h(\theta)=1+\varepsilon\cos3\theta\) at three positive radius thresholds, verifies the exact constant-width square-defect identity, and numerically checks a smooth positive-curvature family whose leading coefficient approaches zero. The tested harmonic values are \(\varepsilon=0,0.04,0.09\), all strictly inside the admissible \(|\varepsilon|<1/8\) range. The checker returns `RANDOM_TANGENT_INTERSECTIONS_OK`. The proof, not the finite quadrature, establishes the infinite-radius and complete-range assertions.

## Relationship to prior work
Fodor, Hug and Ziebarth (2014) study large-sample approximation of convex bodies by random halfspaces and give expected volume differences after outer truncation. Their first public arXiv posting is 2014-09-29, with primary classification 52A22. Their theorems concern a growing number of halfspaces with offsets, not the unbounded intersection point of **two exact supporting tangents**.

A published result on the **area** tail of a *bounded* random polygon with \(n\ge3\) supporting tangents gives a different curvature–width integral, involving \(w(\theta)^2\), an additional semicircular sampling factor and a boundedness conditioning. It neither states nor implies the pair-intersection distance tail and its complete constant-width attainable range. Another published tangent-polygon result concerns Gaussian area/perimeter fluctuations as the number of tangents increases, rather than two-line escape. A published normal-line result for two samples concerns **normals**, with coefficient involving the derivative of width, and actually has bounded support for constant-width bodies. In particular its object and its implication are opposite to the present tangent-line phenomenon.

For the circle, the exact formula is elementary and not claimed as a new discovery. Xu (2015) investigates tangent polygons around a circle; its accessible abstract does not address the present general-body sharp identity. Its complete text was not accessible for a decisive priority comparison. More generally, old integral-geometry literature remains a priority risk. The claim of new content is specifically the general two-tangent flux formula together with its marked escape law and the **complete exact constant-width stability and range**; novelty is provisionally assessed, not independently certified.

## Limitations
Curves with corners, vanishing curvature or nonunique tangents are not addressed. The formula is sensitive to the boundary sampling measure: changing to uniform normal angle or Crofton sampling changes its coefficient and its rigidity. The result does not give a finite-radius closed formula for arbitrary convex ovals or an explicit error constant uniform over all ovals. The conditional *intersection direction* is asserted only in probability, not total variation, because its limit is supported on a lower-dimensional graph. Independent mathematical assessment and definitive historical priority remain outstanding.

## References
1. F. Fodor, D. Hug, I. Ziebarth, *The volume of random polytopes circumscribed around a convex body*, arXiv:1409.8105v1 (first public 2014-09-29), https://arxiv.org/abs/1409.8105; full accessible text https://arxiv.org/html/1409.8105v1.
2. *Curvature–width Pareto law for bounded random tangent polygons*, publicly available scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-curvature-width-pareto-law-for-bounded-random-tangent-polygons--df3f4bf5ad69.
3. *Joint tangent-polygon fluctuations detect Euclidean disks*, publicly available scientific result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-joint-tangent-polygon-fluctuations-detect-euclidean-disks--abd27b445ac3.
4. W.-Q. Xu, *Random circumscribing polygons and approximations of π*, Statistics & Probability Letters 106 (2015), 52–57, DOI:10.1016/j.spl.2015.06.026.
5. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, second expanded edition, Cambridge University Press, 2014, for classical support functions and curvature-radius identities.
