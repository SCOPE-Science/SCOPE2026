# A critical parabolic half-lens law for random circle-centered disk intersections

## Finding

Let \(U_1,\ldots,U_n\) be independent points with uniform angular law on the unit Euclidean circle, with \(n\ge3\). Write \(H_n\) for the event that all sampled centers lie in an open semicircle. On this event, their unique shortest containing arc has length \(\pi-\delta_n\), where \(0<\delta_n<\pi\). For fixed \(\gamma\ge0\), set \(b_n=1+\gamma/n^2\), and form
\[
K_{n,\gamma}=\bigcap_{j=1}^{n}\overline B(U_j,b_n).
\]
Orient the plane so that the positive horizontal axis bisects the occupied shortest arc, and set
\[
\widetilde K_{n,\gamma}=\{(nx,n^2y):(x,y)\in K_{n,\gamma}\}.
\]
Conditional on \(H_n\), the joint random variable and compact convex set
\[
(n\delta_n,\widetilde K_{n,\gamma})
\quad\Longrightarrow\quad
(Q,\mathcal P_{\gamma,Q}),\qquad Q\sim\operatorname{Exp}(\text{mean }\pi),
\]
converge in distribution for the ordinary Euclidean coordinate and Hausdorff distance on compact subsets, where
\[
\boxed{\mathcal P_{\gamma,q}=
\{(X,Y): X\ge0,\ 2|Y|\le 2\gamma+qX-X^2\}.}
\]
In particular, the conditional area has the **critical radius-window law**
\[
\boxed{n^3\operatorname{Area}(K_{n,\gamma})\mid H_n
\ \Longrightarrow\
\mathcal A_\gamma(Q)=
\frac{Q^3+(Q^2+8\gamma)^{3/2}}{12}+\gamma Q.}
\]
Here the notation \(Z_n\mid H_n\Longrightarrow Z\) means convergence of the conditional distribution of \(Z_n\) given \(H_n\). At \(\gamma=0\), \(\mathcal A_0(Q)=Q^3/6\) and \(\mathcal P_{0,Q}\) meets the vertical axis at a pointed corner at the origin, with opening angle \(2\arctan(Q/2)\) almost surely. For fixed \(\gamma>0\), the limit instead has a strictly positive area floor \(4\sqrt2\gamma^{3/2}/3\), and its boundary intersects the vertical axis in a nondegenerate segment. Thus the radius displacement of order \(n^{-2}\) changes both the conditional area law and the limiting geometry.

The following finite-sample identities provide an exact base case, **not a separate novelty claim**:
\[
\Pr(H_n)=n2^{1-n},\qquad
\Pr(\delta_n>s\mid H_n)=(1-s/\pi)^{n-1},\quad 0\le s\le\pi,
\]
and for disks of radius exactly one,
\[
\operatorname{Area}(K_{n,0})=
\begin{cases}\delta_n-\sin\delta_n,&H_n,\\0,&H_n^c.
\end{cases}
\]

## Assumptions and scope

The centers are independent and *angularly uniform on the circumference*, not uniformly distributed in the interior of a disk. Each radius is deterministic and shared by all disks. The parameter \(\gamma\ge0\) is fixed as \(n\to\infty\); no uniformity for growing \(\gamma\) is asserted. Conditioning is specifically on the positive-probability center-containment event \(H_n\), which occurs with probability \(n2^{1-n}\), and is independent of the choice of radius. On \(H_n\), the unique long circular gap determines the occupied arc and the random coordinate system. Degenerate equalities have probability zero. All areas use planar Lebesgue measure; all set limits are for nonempty compact convex sets in the rescaled coordinates.

## Proof

**1. Circular spacings and their rare-event mark.** For each labeled center, consider the event that the other \(n-1\) centers are clockwise within angle \(\pi\) of it. These events are disjoint almost surely: such a starting center follows a circular gap longer than \(\pi\), and at most one gap can be this long. Their union is \(H_n\). For \(0\le s\le\pi\), requiring all the other centers to have clockwise displacement less than \(\pi-s\) from the starting center gives probability \(((\pi-s)/(2\pi))^{n-1}\) for each label, by independence and rotation invariance. Summing and dividing gives
\[
\Pr(H_n)=n2^{1-n},\quad
\Pr(\delta_n>s\mid H_n)=(1-s/\pi)^{n-1}.
\]
Consequently, \(Q_n=n\delta_n\) converges in law to the exponential random variable \(Q\) of mean \(\pi\). On the event indexed by the starting center, the other displacements are independent uniform draws from \((0,\pi)\). Given the maximum and its label, the remaining \(n-2\) displacements are independent uniform on the interval from zero to the maximum (by the order-statistic density). The middle arc of angular displacement at most \(\pi/4\) from the bisector occupies at least half that interval. Thus with conditional probability at least \(1-2^{-(n-2)}\), there is a center in that middle arc.

**2. Exact reduction to endpoint disks in the right half-plane.** In coordinates aligned with the occupied arc, its extreme centers are
\[
u_\pm=(\sin(\delta_n/2),\ \pm\cos(\delta_n/2)).
\]
For every point \(p=(x,y)\) with \(x\ge0\), the minimum of \(u\cdot p\) over unit vectors \(u\) whose angles lie between the two extreme angles is attained at an extreme: their angular separation from the direction of \(p\) ranges within \([0,\pi]\), where cosine decreases with the absolute separation. Since membership in \(\overline B(u,b_n)\) is equivalent to \(|p|^2-2u\cdot p\le b_n^2-1\), the intersection of all \(n\) disks **restricted to \(x\ge0\)** is exactly the intersection of the two extreme disks, restricted to that half-plane.

Set \(x=X/n\) and \(y=Y/n^2\). Combining the two endpoint inequalities gives the **exact** single inequality
\[
X^2+Y^2/n^2-2n\sin(\delta_n/2)X
+2\cos(\delta_n/2)|Y|
\le 2\gamma+\gamma^2/n^2.\tag{1}
\]
For any sequence with \(Q_n=n\delta_n\to q\in[0,\infty)\), the right-half-plane portions of (1) converge as convex compact sets to
\[
\{(X,Y):X\ge0,\ X^2-qX+2|Y|\le2\gamma\}=\mathcal P_{\gamma,q}.
\]
The same inequality uniformly bounds \(|X|\) and \(|Y|\) on events \(Q_n\le M\) for all sufficiently large \(n\), because the quadratic part controls \(X\) and \(\cos(\delta_n/2)\) is bounded away from zero. For the Hausdorff assertion, any cluster point of feasible points satisfies the limiting inequality. In the nondegenerate case \(q+\gamma>0\), there is a point with \(X>0\) and strict limiting inequality. Every point of \(\mathcal P_{\gamma,q}\) is approached by points on its segment to this strict point; each nontrivial mixture with the strict point has strict inequality by convexity and is eventually feasible. Compactness then gives the other directed Hausdorff bound. When \(q=\gamma=0\), the limit is just the origin, which is feasible at every \(n\). The same argument with the limiting inequalities in place of (1) shows continuity of \(q\mapsto\mathcal P_{\gamma,q}\).

**3. The excluded negative half-plane collapses.** On the high-probability event identified in step 1, there is a center with angle \(|\theta|\le\pi/4\), hence \(\cos\theta\ge1/\sqrt2\). Any \((X,Y)\) belonging to its disk satisfies
\[
X^2+Y^2/n^2-2nX\cos\theta-2Y\sin\theta
\le2\gamma+\gamma^2/n^2.
\]
With \(|X|,|Y|\) already bounded by (1), the right-hand side and all but \(-2nX\cos\theta\) remain bounded. Therefore \(X\ge -C_M/n\) uniformly on \(Q_n\le M\). For any sequence of such configurations with \(Q_n\to q\), every cluster point of the full rescaled set has \(X\ge0\) and satisfies the limit of (1), and the full set contains the right-half portion shown to converge in step 2. This gives Hausdorff convergence of the full sets to \(\mathcal P_{\gamma,q}\). By compactness of \([0,M]\) and continuity of \(q\mapsto\mathcal P_{\gamma,q}\), the Hausdorff distance between the full set and \(\mathcal P_{\gamma,Q_n}\) tends uniformly to zero on these configurations: a violating sequence would have a subsequence with \(Q_n\to q\). Tightness of \(Q_n\) and the conditional high-probability center event then give this distance tending to zero in conditional probability. The continuous-mapping theorem and this convergence in probability give the claimed joint conditional limit.

**4. Area of the parabolic half-lens.** Its horizontal range is \(0\le X\le r\), with
\[
r=\frac{q+\sqrt{q^2+8\gamma}}2.
\]
At such a fixed \(X\), its vertical section has length \(2\gamma+qX-X^2\). Thus
\[
\operatorname{Area}(\mathcal P_{\gamma,q})
=\int_0^r(2\gamma+qX-X^2)\,dX
=\frac{q^3+(q^2+8\gamma)^{3/2}}{12}+\gamma q.
\]
The convergence of compact convex bodies inside a common bounded region implies convergence of their areas. Substituting the limiting exponential variable gives the distributional formula. At \(q=0\) and \(\gamma>0\), the area expression equals \(4\sqrt2\gamma^{3/2}/3\).

**5. Exact radius-one base case.** When \(b_n=1\) and the centers lie in the short occupied arc, the two extreme unit disks meet in a lens completely contained in \(x\ge0\), so step 2 proves equality of the full intersection and this lens. The centers' separation is \(2\cos(\delta_n/2)\); its standard circular-segment area equals \(\delta_n-\sin\delta_n\). If the centers are not contained in any semicircle, their convex hull contains the origin; a nonzero point lying in all unit disks would have positive dot product with every center, which is impossible by convex separation. The intersection is then only the origin and has zero area. This completes the exact identity and is consistent with \(n^3(\delta_n-\sin\delta_n)\to Q^3/6\).

## Verification

The independent standard-library program `verify.py` reproduces the unit-radius lens identity for 56 seeded circular samples, compares a circular-gap quadrature against a separate pointwise-minimum radial integral for 12 radius/configuration pairs, and verifies convergence of scaled areas for \(\gamma\in\{0,0.5,2\}\) at four increasing sample sizes. It also simulates 30,000 circular configurations to test the exact rare-event probability and conditional gap survival probability. The performed diagnostic returned `ALL_CHECKS_PASSED`; these finite checks validate representative computations, not the limiting theorem. For the analytic certification, inspect the exact endpoint inequality (1), the semicircle gap distribution and the area integral in the preceding proof.

## Relationship to prior work

The complete deterministic circular-gap formula for intersections of congruent disks with centers on a circle, and its fixed-radius \(b>1\) random mean and Gaussian limit, were previously published in *Exact circular-gap area laws and Gaussian fluctuations for intersecting congruent disks*. That theorem's exact formula applies when each finite \(b_n>1\), so it is a substantive covering representation, **not merely a similarly titled result**. It does not explicitly establish the rare conditional **joint rescaled shape** and area transition at \(b_n=1+\gamma/n^2\); the present theorem isolates this singular boundary layer, proves that nearly semicircular samples force the half-plane truncation, and evaluates the limiting random half-lens. The \(b=1\) finite-n formula and the exponential spacing mark alone are background consequences of classical gaps and are not a new finding.

The published *Anisotropic semicircle containment and the Gaussian–von Mises crossover for random enclosing disks* includes uniform/anisotropic semicircle containment, a conditional exponential gap mark and random smallest-enclosing-disk geometry. Its limit concerns a *smallest enclosing disk of sampled points*, rather than the area and shape of an *intersection of disks centered at those points*. Its exponential mark is used here, not claimed as original.

The published *A critical-window law for the two-vertex event in random disc-polygons* also uses a disk-radius displacement of order \(n^{-2}\), but studies the ball-convex hull of independently sampled **interior** points and a two-vertex event. Neither its probability law nor its geometric object yields the half-lens law here. Paouris–Pivovarov and Fodor–Kevei–Vígh investigate random ball-polyhedra and disc-polygons with sampling laws in the **ambient disk**; their main statements do not provide the singular circle-boundary conditional limit.

## Limitations

The result only concerns independent uniform centers **on a fixed unit circle**, disks of equal radii \(1+\gamma/n^2\), and conditioning on the centers lying in a semicircle. No assertion is made for arbitrary centers, nonuniform angular densities, higher dimensions, or the unconditioned large-sample shape. The joint law is weak convergence of sets and areas, not a claimed total-variation rate. Historical priority remains provisional: the known all-radius circular-gap identity can be a starting point for equivalent singular-limit arguments, and an unindexed earlier limit theorem could subsume this result. No formal verification or expert attestation is claimed.

## References

1. G. Paouris and P. Pivovarov, *Random ball-polyhedra and inequalities for intrinsic volumes*, arXiv:1510.07292, first public version 2015-10-25, https://arxiv.org/abs/1510.07292. Archival mathematical geometry foundation; its ambient-density sampling differs from the present setting.
2. F. Fodor, P. Kevei and V. Vígh, *On Random Disc Polygons in Smooth Convex Discs*, published 2014, https://www.cambridge.org/core/journals/advances-in-applied-probability/article/on-random-disc-polygons-in-smooth-convex-discs/4910C36245F859DC5F2D618B261400CB. Ambient-sampling disc-polygon literature.
3. *Exact circular-gap area laws and Gaussian fluctuations for intersecting congruent disks*, publicly indexed mathematical result, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-circular-gap-area-laws-and-gaussian-fluctuations-for-inter--1c25b18e16e8/RESULT.md. Exact deterministic covering formula and fixed-radius laws.
4. *Anisotropic semicircle containment and the Gaussian–von Mises crossover for random enclosing disks*, publicly indexed mathematical result, https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-anisotropic-semicircle-containment-and-the-gaussian-von-mises-cr--3ac5a9371126/RESULT.md. Conditional semicircle gap and enclosing-disk marks.
5. *A critical-window law for the two-vertex event in random disc-polygons*, publicly indexed mathematical result, https://github.com/Resultary/2026/blob/main/2026/11/1/SCOPE-a-critical-window-law-for-the-two-vertex-event-in-random-disc-po--2d426710b5ce/RESULT.md. Distinct interior-sampling critical-window event.
6. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–112, https://doi.org/10.7146/math.scand.a-10655. Classical convex-hull/semicircle probability.
