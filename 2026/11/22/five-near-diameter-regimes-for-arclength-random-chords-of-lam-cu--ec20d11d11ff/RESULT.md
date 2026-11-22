# Five near-diameter regimes for arclength-random chords of Lamé curves

## Finding

For each fixed real parameter \(p>0\), let
\[
C_p=\{(x,y)\in\mathbb R^2:|x|^p+|y|^p=1\},\qquad
L_p=\mathcal H^1(C_p).
\]
Choose \(X,Y\) independently from normalized Euclidean arclength \(\mathcal H^1|_{C_p}/L_p\), and set \(R_p=\|X-Y\|_2\). The Euclidean diameter is
\[
D_p=\begin{cases}2,&0<p\le2,\\2^{3/2-1/p},&p>2.\end{cases}
\]
As \(\varepsilon\downarrow0\) with \(p\) **fixed**, the near-diameter chord probability obeys the complete five-case law
\[
\mathbb P(R_p>D_p-\varepsilon)\sim
\begin{cases}
\dfrac{8}{L_p^2}\varepsilon^2,&0<p<1,\\[3pt]
\dfrac{16}{L_1^2}\varepsilon^2=\dfrac12\varepsilon^2,&p=1,\\[3pt]
\dfrac{16p^{2/p}\Gamma(1+1/p)^2}{L_p^2\Gamma(1+2/p)}\varepsilon^{2/p},&1<p<2,\\[3pt]
\dfrac2\pi\varepsilon^{1/2},&p=2,\\[3pt]
\dfrac{8\pi 2^{1/2-1/p}}{L_p^2\sqrt{(p-1)(p-2)}}\varepsilon,&p>2.
\end{cases}
\]
The necessary perimeter is explicitly computable for every fixed \(p>0\):
\[
L_p=\frac8p\int_0^{\pi/2}
\sqrt{\sin^2t\cos^{4/p-2}t+\cos^2t\sin^{4/p-2}t}\,dt.
\]
The integral is understood as an improper integral where an endpoint exponent is negative. In particular \(L_{2/3}=6\), \(L_1=4\sqrt2\) and \(L_2=2\pi\). The classical astroid thus has the concrete coefficient \(2/9\) in its quadratic tail; this special-case value is already implied by the established four-cusped hypocycloid law and is used here only as a consistency check. An isolated, exactly doubled quadratic coefficient occurs at the diamond \(p=1\): the fixed-parameter coefficients approaching one from either side tend to \(1/4\), whereas at \(p=1\) the coefficient is \(1/2\). These statements are not uniform in \(p\) near either transition.

The proof also gives **marked total-variation limits**, with endpoint labels chosen as specified below, conditional on \(R_p>D_p-\varepsilon\):

1. For \(0<p\le1\), one of the four ordered opposite axial-tip pairs is asymptotically uniform. Each endpoint has an independent asymptotically fair choice of its two adjacent branches. If \(u_1,u_2\) are the inward axial-coordinate deficits, \((u_1/\varepsilon,u_2/\varepsilon)\) tends to the uniform area distribution on \(\{(s,t):s,t\ge0,\ s+t<1\}\), independent of the finite labels.
2. For \(1<p<2\), the ordered opposite axial-tip pair is asymptotically uniform. If \(y_1,y_2\) denote the signed transverse coordinates in consistently oriented local axes, \((y_1,y_2)/(p\varepsilon)^{1/p}\) tends to normalized area on \(\{(s,t):|s|^p+|t|^p<1\}\), independent of the pair label.
3. For \(p=2\), the first endpoint's polar angle remains uniform on \([0,2\pi)\). Writing the second endpoint angle as the first angle plus \(\pi+\delta\), the mismatch \(\delta/(2\sqrt\varepsilon)\) tends to a uniform variable on \([-1,1]\), independent of the first angle.
4. For \(p>2\), the ordered pair of antipodal diagonal maximizers is asymptotically uniform among four choices. If \(u,v\) are the respective polar-angle offsets from that pair and \(r_p=2^{1/2-1/p}\), the vector \((u,v)/\sqrt\varepsilon\) tends to normalized area on the ellipse
\[
\frac{r_p}{4}\bigl((2p-3)(s^2+t^2)-2st\bigr)<1.
\]
These are limits of the full conditional densities on their rescaled coordinate patches, hence convergence in total variation, not merely weak convergence.

## Assumptions and scope

The sampling law is independent **Euclidean arclength** on the entire closed curve, with ordered endpoints. Neither uniform polar angle, uniform area in the enclosed Lamé region, nor Crofton-invariant line sampling is substituted. The parameter \(p\) is fixed before \(\varepsilon\) tends to zero. The curve is a rectifiable Jordan curve even when \(0<p<1\), but its interior is then nonconvex; only its boundary and Euclidean chord distances are used. All distances and arclengths use the ordinary Euclidean metric. The event is strict; equality occurs with probability zero.

## Proof

**1. Diameter and all maximizers.** In polar coordinates the radial function is \(r_p(\theta)=(|\cos\theta|^p+|\sin\theta|^p)^{-1/p}\). For \(p<2\), the Euclidean norm of a curve point is at most one, with equality precisely at its four axial tips; for \(p>2\), the Euclidean norm is at most \(r_p=2^{1/2-1/p}\), with equality precisely at its four diagonal points. For \(p=2\) the norm is identically one. The inequality \(\|X-Y\|_2\le\|X\|_2+\|Y\|_2\) is sharp precisely when the points are opposite maximizers of the radial norm. This proves the stated diameters and classifies every maximizing ordered pair: four for \(p\ne2\), a circle's worth for \(p=2\). Compactness confines every sufficiently nearly maximal pair to arbitrarily small neighborhoods of those pairs.

**2. The cuspidal cases \(0<p\le1\).** Near the positive axial tip, write a branch as \(x=1-u\), \(y=\sigma[1-(1-u)^p]^{1/p}\), with \(u>0\) and branch sign \(\sigma\in\{-1,1\}\). For fixed \(0<p<1\), \(|y|=(pu)^{1/p}(1+O_p(u))=o(u)\), and \(ds/du=1+o(1)\). An ordered near-opposite pair with inward deficits \(u,v\) satisfies \(2-R_p=u+v+o(u+v)\) uniformly as \(u+v\to0\). The two-dimensional admissible region therefore has leading area \(\varepsilon^2/2\). There are four ordered opposite axial pairs and four branch-sign choices per pair, contributing \(4\cdot4\cdot(\varepsilon^2/2)/L_p^2=8\varepsilon^2/L_p^2\).

At \(p=1\), the same local branches obey \(y=\sigma u\), but the arclength Jacobian becomes exactly \(ds/du=\sqrt2\). Since the distance defect is still \(u+v+O((u+v)^2)\), the product Jacobian is two rather than one, giving \(16\varepsilon^2/L_1^2\). The two neighboring fixed-parameter coefficient limits are \(8/L_1^2=1/4\), because the gamma quotient in the next case tends to \(1/2\) as \(p\downarrow1\). Thus the isolated doubling is real, not a normalization artifact.

**3. Singular-curvature convex arcs \(1<p<2\).** Near the positive axial tip, use the signed transverse coordinate \(y\) and \(x=(1-|y|^p)^{1/p}=1-|y|^p/p+O_p(|y|^{2p})\). Since \(dx/dy\to0\), the local arclength density with respect to \(dy\) is \(1+o(1)\). Between opposite tips, uniformly for both small transverse coordinates,
\[
2-R_p=\frac{|y_1|^p+|y_2|^p}{p}
+O_p\bigl(y_1^2+y_2^2+|y_1|^{2p}+|y_2|^{2p}\bigr).
\]
Because \(p<2\), the remainder is lower order on the event's \(\varepsilon^{1/p}\) coordinate scale. The Euclidean area of the unit \(\ell_p\) disk in two dimensions is \(4\Gamma(1+1/p)^2/\Gamma(1+2/p)\). Rescaling its two coordinates by \((p\varepsilon)^{1/p}\) and summing four ordered tip pairs yields the third coefficient exactly.

**4. Circle.** When \(p=2\), angular coordinates are independent uniform variables. With the second angle \(\pi+\delta\) beyond the first, \(R_2=2\cos(\delta/2)\) near a diameter, giving the exact identity, for \(0<\varepsilon<2\),
\[
\mathbb P(R_2>2-\varepsilon)=\frac2\pi\arccos(1-\varepsilon/2)
=\frac2\pi\sqrt\varepsilon\bigl(1+O(\varepsilon)\bigr).
\]
The permissible signed mismatch interval yields the uniform marked limit.

**5. Smooth diagonal maxima \(p>2\).** Fix a maximizing direction \(\theta_0=\pi/4\), and write the two polar angles \(\theta_0+u\) and \(\theta_0+\pi+v\). Symmetry gives
\[
r_p(\theta_0+w)=r_p\left(1-\frac{p-2}{2}w^2+O_p(w^4)\right).
\]
Expansion of the Euclidean distance of the corresponding vectors yields
\[
D_p-R_p=\frac{r_p}{4}
\left((2p-3)(u^2+v^2)-2uv\right)+O_p((|u|+|v|)^3).
\]
The quadratic form has determinant \(r_p^2(p-1)(p-2)/4>0\), hence its unit sublevel ellipse has area \(2\pi/[r_p\sqrt{(p-1)(p-2)}]\). At either maximizing diagonal \(ds/d\theta=r_p+o(1)\). Multiplication by the two Jacobians, by \(\varepsilon\), and by four ordered diametral pairs gives the last case's coefficient.

**6. Conditional laws and justification of limits.** In every case, the diameter-maximizer classification first localizes the event to disjoint maximizing neighborhoods. The appropriate rescaling renders the distance deficit locally uniform on compact sets as a positive homogeneous limiting form. Its strict unit sublevel set is bounded, with a boundary of two-dimensional measure zero. The rescaled arclength-product Jacobian converges uniformly to the stated positive constant on every bounded subpatch. A bounding comparison between \((1-\eta)\) and \((1+\eta)\) homogeneous sublevels controls the thin boundary shell, and compactness excludes any other contribution. The resulting normalized densities converge in \(L^1\) on the union of finite patches; the circle uses an angular cylinder. This gives both probability coefficients and the marked total-variation limits. The isolated branch labels are equiprobable by the fourfold and reflection symmetries.

## Verification

The accompanying `verify.py` evaluates the perimeter by one-dimensional quadrature and the *unexpanded exact Euclidean chord predicate* by deterministic two-dimensional midpoint quadrature on every ordered maximizing patch. It checks \(p=2/3,0.8,1,1.2,1.5,2,3,4\) as well as the elementary exact perimeters and coefficients. In each noncircular test the raw probability and the leading prediction agree to within the explicitly specified finite-threshold tolerances; the script prints the ratios and ends with `ALL_CHECKS_PASSED`. All numerical tests are supplementary: the proof's localization and integration establish the infinite-limit claims without relying on finite numerical extrapolation.

## Relationship to prior work

Bőröczky, Fodor and Hug's 2011 work on boundary-sampled random polytopes provides the archive-period geometric-probability setting, including the importance of local boundary geometry; it studies expected intrinsic-volume deficits, not this two-point near-diameter probability. Heinrich's 2014 treatment includes superellipsoids but evaluates Crofton-type *line-chord power integrals* rather than distances between independently arclength-uniform endpoints; those probability measures are not equivalent. Koroleva and Nikitin (2013) study extreme perimeter and area of circle-inscribed random polygons and do not supply the Lamé pair-distance laws. Earlier related results treat a near-circle Lamé parameter window, elliptic boundary pairs, and \(\ell_p\)-body invariant-line chords; the existing four-cusped hypocycloid result already covers the astroid specialization, and fixed polygonal-tip geometry covers the standalone diamond calculation. These known special cases and other existing results do not, at the level of their explicit published statements, imply the complete fixed-parameter five-case classification, including the contrast between the two neighboring curved families and the isolated diamond coefficient. These distinctions are about statements and sampling laws, not just titles. Historical priority remains provisional pending scrutiny of any unindexed superellipse distance literature.

## Limitations

These are pointwise fixed-\(p\) asymptotics; no uniform joint limit as \(p\to1\), \(p\to2\), \(p\to\infty\), or \(\varepsilon\to0\) is asserted. The theorem is planar and uses two independent normalized-arclength endpoints; it is not a claim about invariant random lines, interior-area samples, or maximum pair distances in a growing sample. The shapes for \(0<p<1\) are nonconvex. Numerical quadrature does not independently certify infinite asymptotics, and independent mathematical validation has not been performed.

## References

1. K. J. Bőröczky, F. Fodor, D. Hug, *Intrinsic Volumes of Random Polytopes with Vertices on the Boundary of a Convex Body*, arXiv:1103.4978v1, publicly posted 25 March 2011, https://arxiv.org/abs/1103.4978.
2. L. Heinrich, *Lower and Upper Bounds for Chord Power Integrals of Ellipsoids*, Applied Mathematical Sciences **8** (2014), 8257–8269, especially §6, doi:10.12988/ams.2014.411913, https://doi.org/10.12988/ams.2014.411913.
3. E. V. Koroleva, Ya. Yu. Nikitin, *U-Max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1, 7 January 2013, https://arxiv.org/abs/1301.1360.
4. G. Lamé, classical Lamé curves; historical curve definition and standard parameterization documented in E. W. Weisstein, *Superellipse*, MathWorld, https://mathworld.wolfram.com/Superellipse.html.
