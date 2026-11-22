# Angularly invariant surface-to-volume efficiency and a logarithmic cusp for intersecting cylinders

## Finding
Let two infinite solid circular cylinders of radii \(R\ge r>0\) have nonparallel axes meeting at angle \(\beta\in(0,\pi)\), and write \(K\) for their compact convex intersection, \(V=\operatorname{vol}_3(K)\), and \(S=\mathcal H^2(\partial K)\). Their scale-free surface-to-volume efficiency
\[
Q=\frac{rS}{V}
\]
is **independent of the crossing angle** and is a strictly decreasing bijection of the radius ratio \(t=R/r\in[1,\infty)\) onto \((2,3]\). Thus this single dimensionless surface/volume observation determines the unordered ratio of the two cylinder radii without knowledge of the crossing angle. Its complete sharp endpoint behavior is
\[
\boxed{Q(1+\eta)=3-\frac32\eta+\frac34\eta^2\log\frac1\eta+O(\eta^2),\qquad\eta\downarrow0,}
\]
and
\[
\boxed{Q(t)=2+\frac1t-\frac1{4t^2}+O(t^{-3}),\qquad t\to\infty.}
\]
In particular \(Q(1)=3\), the limit \(2\) is unattained at finite radius ratio, and \(Q\) has a right first derivative \(-3/2\) but no finite right second derivative at equal radii. The logarithmic term marks the onset of an unequal-radius cylinder-intersection ridge.

An exact all-parameter representation is
\[
F(t)=8\int_0^1\sqrt{(t^2-y^2)(1-y^2)}\,dy,\qquad
\boxed{V=\frac{r^3}{\sin\beta}F(t),\quad S=\frac{r^2}{\sin\beta}\bigl[3F(t)-(t-1)F'(t)\bigr],\quad Q(t)=3-(t-1)\frac{F'(t)}{F(t)}.}
\]
Here derivatives at \(t=1\) are understood from the right. For \(t>1\), putting \(k=1/t\) and using complete elliptic integrals \(E(k),\mathcal K(k)\) in modulus convention gives another exact evaluation:
\[
V=\frac{8R^3}{3\sin\beta}\left[(1+k^2)E(k)-(1-k^2)\mathcal K(k)\right],
\]
\[
S=\frac{8r^2}{\sin\beta}\left[tE(k)+\frac{E(k)-(1-k^2)\mathcal K(k)}{k^2}\right].
\]
The integral formula is preferred at \(t=1\), where the displayed separate elliptic factors have removable singularities.

## Assumptions and scope
The cylinders are infinite, solid and right circular; their axes are distinct, intersect and are nonparallel. Surface area means the entire Euclidean two-dimensional Hausdorff measure of the boundary of their intersection, including both exposed cylindrical patches; the one-dimensional common-boundary ridge has zero surface measure. The angle may be acute or obtuse and \(\sin\beta>0\). The smaller radius \(r\) is used to make \(Q\) scale-free. The result concerns the Euclidean surface/volume ratio, not John–Löwner ellipsoid ratios or planar sectional area. All limits hold at fixed nonzero crossing angle, and the dimensionless function \(Q\) does not depend on that angle.

## Proof
**1. Affine slice formula and its exact dependence on angle.** Translate the common axial point to the origin. Choose unit transverse normals \(n_1,n_2\) in the axes' common plane, and a unit vector \(e\) normal to that plane. The invertible linear coordinate map \(X\mapsto (n_1\cdot X,n_2\cdot X,e\cdot X)=(x_1,x_2,z)\) has absolute determinant \(\sin\beta\). The intersection becomes
\[
\{(x_1,x_2,z):x_1^2+z^2\le R^2,\quad x_2^2+z^2\le r^2\}.
\]
At each \(|z|\le r\) its coordinate cross-section is a rectangle with side lengths \(2\sqrt{R^2-z^2}\) and \(2\sqrt{r^2-z^2}\). Dividing the product by the coordinate Jacobian and integrating gives
\[
V=\frac8{\sin\beta}\int_0^r\sqrt{(R^2-z^2)(r^2-z^2)}\,dz
=\frac{r^3}{\sin\beta}F(R/r).
\]

**2. Boundary-area first variation, including the common ridge.** Fix \(r\) and increase \(R\) by a small positive amount. The radial level set of the first cylinder moves in its *Euclidean* unit normal direction at speed one. The coarea/first-variation formula therefore identifies \(\partial_R V\) with the area \(S_R\) of the exposed piece of its cylindrical boundary. Similarly \(\partial_r V=S_r\) for the second cylinder. Their common intersection ridge has zero \(\mathcal H^2\)-measure, even at \(R=r\), so \(S=S_R+S_r\). Equivalently, direct differentiation under the integral yields the manifestly positive formulas
\[
S_R=\frac{8R}{\sin\beta}\int_0^r\frac{\sqrt{r^2-z^2}}{\sqrt{R^2-z^2}}\,dz,
\qquad
S_r=\frac{8r}{\sin\beta}\int_0^r\frac{\sqrt{R^2-z^2}}{\sqrt{r^2-z^2}}\,dz.
\]
The integrals remain finite at equal radii; a change of variables \(z=r\sin u\) justifies the endpoint differentiation. Since \(V(R,r)\) is homogeneous of degree three, Euler's identity gives \(RV_R+rV_r=3V\). Inserting \(V=r^3 F(t)/\sin\beta\) gives \(S=r^2[3F-(t-1)F']/\sin\beta\), hence the displayed exact formula for \(Q\) and angle independence. At \(t=1\), \(F(1)=16/3\) and \(F'(1)=8\), so \(Q(1)=3\).

**3. Strict monotonicity without numerical inference.** On \([0,1]\) let \(\mu_t\) be the probability measure with density proportional to \(\sqrt{(t^2-y^2)(1-y^2)}\). Define
\[
g_t(y)=\frac{t(t-1)}{t^2-y^2}.
\]
Differentiation of \(F\) proves \(3-Q(t)=\mathbb E_{\mu_t}[g_t(Y)]\). For \(t>1\), both \(g_t(y)\) and the centered density score \(\partial_t\log\mu_t(y)=t/(t^2-y^2)-\mathbb E_{\mu_t}[t/(t^2-Y^2)]\) are increasing in \(y\). Moreover
\[
\partial_t g_t(y)=\frac{t^2-(2t-1)y^2}{(t^2-y^2)^2}>0,
\]
where the numerator is at least \((t-1)^2\). Differentiating the expectation gives
\[
\frac d{dt}\mathbb E_{\mu_t}g_t
=\mathbb E_{\mu_t}[\partial_t g_t]
+\operatorname{Cov}_{\mu_t}\left(g_t,\frac{t}{t^2-Y^2}\right)>0.
\]
The covariance is nonnegative by the standard independent-copy identity for monotone functions (half the expected product of their pairwise differences). Thus \(Q\) is strictly decreasing. For fixed \(y<1\), \(g_t(y)\to1\) as \(t\to\infty\), and in fact convergence is uniform for sufficiently large \(t\); hence \(Q\to2\). Continuity at \(t=1\) follows from the integral representation. This proves the exact image \((2,3]\) and the unique inverse radius ratio.

**4. Sharp logarithmic equal-radius cusp.** Twice differentiating the integral for \(t>1\) gives
\[
F''(t)=-8\int_0^1\frac{y^2\sqrt{1-y^2}}{(t^2-y^2)^{3/2}}\,dy.
\]
Set \(t=1+\eta\), \(u=1-y\). In a fixed small endpoint neighborhood the integrand including its factor \(-8\) equals
\[
-4\frac{\sqrt u}{(u+\eta)^{3/2}}
+O\!\left(\frac{u^{3/2}+\eta\sqrt u}{(u+\eta)^{3/2}}\right).
\]
The error has uniformly bounded integral, while the leading term integrates to \(-4\log(1/\eta)+O(1)\). Away from the endpoint the integral is uniformly bounded. Consequently
\[
F''(1+\eta)=-4\log(1/\eta)+O(1),\quad
F'(1+\eta)=8-4\eta\log(1/\eta)+O(\eta),
\]
\[
F(1+\eta)=\frac{16}{3}+8\eta+O\bigl(\eta^2\log(1/\eta)\bigr).
\]
Substituting these into \(Q=3-\eta F'/F\) gives the asserted coefficient \(3/4\). The right derivative at equality is \(-3/2\). The positive \(\eta^2\log(1/\eta)\) term rules out a finite second derivative at the endpoint.

**5. Large-radius expansion.** Uniform binomial expansion under the integral gives
\[
F(t)=2\pi t\left(1-\frac1{8t^2}+O(t^{-4})\right),\quad
\frac{F'(t)}{F(t)}=\frac1t+\frac1{4t^3}+O(t^{-5}),
\]
whence \(Q(t)=2+t^{-1}-(4t^2)^{-1}+O(t^{-3})\). The elliptic representations follow from standard complete-elliptic reduction of the same one-variable integrals; they are supplemental, not needed for monotonicity or either asymptotic.

## Verification
The accompanying standalone `check_bicylinder.py` independently evaluates the volume through rectangular slicing and the two separate exposed cylindrical surface patches; it compares numerical quadrature to complete-elliptic representations at multiple radius ratios and crossing angles, checks the equal-radius normalization and first-variation identity, and probes both asymptotic regimes with arbitrary precision. Execute from the directory containing this document using `python3 check_bicylinder.py`. It completed 123 deterministic numerical diagnostics. These finite computations independently corroborate, but cannot certify, the all-parameter monotonicity or singular asymptotics, which are established by the analytical argument above.

## Relationship to prior work
Hubbell's 1965 *Common Volume of Two Intersecting Cylinders* analyzes the general intersecting-cylinder volume, so neither the foundational slice volume nor its elliptic evaluation is claimed as new. The January 19, 2008 Steinmetz-solid exposition explicitly gives the equal-radius surface area and volume and discusses unequal-radius volumes. Those known formulas are compatible with the endpoint \(Q(1)=3\), but do not imply the strict **all-radius** monotonicity and the sharp equal-radius logarithmic cusp without additional analysis. Results on planar central sections of the equal-radius bicylinder, extremal John–Löwner ellipsoids of unequal intersecting cylinders, and partially intersecting displaced cylinders study different invariants and do not contain the stated surface/volume theorem. The present contribution is the full angle-invariant shape-efficiency law, its strict inverse property, and its precise boundary regularity, not the discovery of Steinmetz solids or the volume integral.

## Limitations
The ratio uses the *known smaller radius* to become dimensionless; \(S/V\) alone without any scale does not recover both radii. The crossing angle itself cannot be recovered from this ratio. Nonintersecting or parallel cylinder axes and finite cylinder caps fall outside the theorem. At \(R=r\), second differentiability is understood one-sidedly on the admissible domain \(R\ge r\). This is a mathematical proof with self-review and numerical corroboration, not an independent scientific certification. Earlier engineering and geometry literature may contain equivalent surface-area evaluations; the full text of Moore's 1974 symmetry study could not be accessed to exclude every historical antecedent. The exact day of the earlier 1965 publication was not verified; the dated 2008 source supplies an exact-day archival anchor, not a claim that cylinder geometry began in 2008.

## References
1. J. H. Hubbell, “Common Volume of Two Intersecting Cylinders,” *Journal of Research of the National Bureau of Standards C* **69C** (1965), 139–143, https://nvlpubs.nist.gov/nistpubs/jres/69C/jresv69Cn2p139_A1b.pdf .
2. Ngô Quốc Anh, “Steinmetz Solid,” 2008-01-19, https://anhngq.wordpress.com/2008/01/19/steinmetz-solid/ .
3. Moreton Moore, “Symmetrical intersections of right circular cylinders,” *The Mathematical Gazette* **58** (1974), 181–185, https://doi.org/10.2307/3615957 .
4. F. J. Aschmoneit and B. Cockx, “Volume and Surface Area of two Orthogonal, Partially Intersecting Cylinders: A Generalization of the Steinmetz Solid,” arXiv:2512.22555v1, https://arxiv.org/html/2512.22555v1 .
5. “Complete planar-section area profile of the Steinmetz bicylinder,” published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-planar-section-area-profile-of-the-steinmetz-bicylinder--1bfc7d9fbd11 .
6. “Exact John–Löwner ellipsoids and an angle-independent ratio for intersecting cylinders,” published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-john-l-wner-ellipsoids-and-an-angle-independent-ratio-for--bef1cf01440b .
