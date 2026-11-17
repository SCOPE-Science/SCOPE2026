# The endpoint-chord Crofton disk: intrinsic anisotropy and its boundary metric

## Finding
Let \(B=\{x\in\mathbb R^2:|x|<1\}\). Sample independently two uniform angles on \([0,2\pi)\) and join their corresponding points on the unit circle by a chord \(C\). For any \(x,y\in\overline B\), put
\[
d(x,y)=\Pr\bigl(C\cap[x,y]\ne\varnothing\bigr).
\]
For \(n_\phi=(\cos\phi,\sin\phi)\), this probability defines a continuous metric on the **closed** disk, and admits the exact two-point formula
\[
 d(x,y)=\frac1{\pi^2}\int_0^\pi\left|\arcsin(x\cdot n_\phi)-\arcsin(y\cdot n_\phi)\right|\,d\phi.\tag{1}
\]
Straight Euclidean segments are its unique unparametrized shortest paths in the open disk. Its infinitesimal norm is the smooth, strongly convex, reversible projective Finsler norm
\[
 F_x(v)=\frac1{\pi^2}\int_0^\pi\frac{|v\cdot n_\phi|}{\sqrt{1-(x\cdot n_\phi)^2}}\,d\phi,\qquad x\in B.\tag{2}
\]
At \(x=(r,0)\), \(0<r<1\), the two Euclidean unit directions tangent and normal to the radius satisfy
\[
 F_x(e_r)=\frac{2\operatorname{artanh}r}{\pi^2r},\qquad
 F_x(e_\tau)=\frac{2\arcsin r}{\pi^2r}.\tag{3}
\]
The ratio \(\mathcal A(r)=F_x(e_r)/F_x(e_\tau)=\operatorname{artanh}(r)/\arcsin(r)\) increases strictly from \(1\) to infinity. Thus the center is the **unique locally isotropic point**, and, away from the center, this **single ratio of orthogonal local lengths determines the Euclidean radius**. For every noncentral \(x\), the indicatrix of \(F_x\) is **not an ellipse**, so the metric is not induced by a Riemannian metric on any nonempty open subset.

Writing \(\operatorname{Li}_2(z)=\sum_{k\ge1}z^k/k^2\), the exact center-to-radius distance and boundary distance are
\[
 d(0,re_1)=\frac{\operatorname{Li}_2(r)-\operatorname{Li}_2(-r)}{\pi^2}\quad(0\le r\le1),\qquad
 d(e^{i\theta},e^{i(\theta+\alpha)})=\frac{\alpha(2\pi-\alpha)}{2\pi^2}\quad(0\le\alpha\le\pi).\tag{4}
\]
In particular, the open disk is not complete in this intrinsic distance: its metric completion is the closed disk, and every boundary point has distance \(1/4\) from the center. The interior radial density diverges only logarithmically as \(r\uparrow1\), while the tangential density tends to \(1/\pi\). Furthermore, the **full metric isometry group of the completed disk is exactly the Euclidean orthogonal group** \(O(2)\); there are no hidden nonlinear isometries.

## Assumptions and scope
The chord model is **uniform independent endpoints**, not translation-invariant random lines or uniform random chord midpoints. The probability in \(d\) is under one fresh random chord for each pair \(x,y\). The endpoints \(x,y\) may lie on the boundary; tangent or endpoint coincidences have probability zero. The metric and its completion statement refer to the disk with this probability distance, not Euclidean arclength or a hyperbolic metric. Claims about \(F_x\) concern \(x\in B\) and nonzero tangent vectors. Formula (3) is interpreted continuously at \(r=0\), when both expressions equal \(2/\pi^2\).

## Proof
**1. Exact chord-line measure and (1).** Write the unoriented line containing the chord as \(\{z:z\cdot n_\phi=s\}\), with \(0\le\phi<\pi\) and \(-1<s<1\). Rotation invariance makes \(\phi\) uniform on \([0,\pi)\), independent of \(s\). The smaller endpoint-angle difference is uniform on \([0,\pi]\), so the absolute distance of the chord from the origin has distribution \(\Pr(|s|\le u)=2\arcsin(u)/\pi\). Symmetry of the signed normal offset then gives density \(1/(\pi\sqrt{1-s^2})\) for \(s\), independent of \(\phi\). A line crosses the segment \([x,y]\) precisely when \(s\) lies between \(x\cdot n_\phi\) and \(y\cdot n_\phi\). Integrating the arcsine density followed by uniform \(\phi\) proves (1), including the boundary by dominated convergence.

**2. Metric, geodesics, and completion.** For any fixed line, the indicator of separating \(x,y\) satisfies the triangle inequality pointwise; its integral is (1). Since the line measure has strictly positive density for every line through the open disk, any distinct pair is separated by an open, positive-measure family of lines, so \(d(x,y)>0\). If \(z\in[x,y]\), the separating-line indicator is the sum of indicators for \([x,z]\) and \([z,y]\) almost surely, yielding \(d(x,y)=d(x,z)+d(z,y)\). If \(z\notin[x,y]\), there is a nonempty open family of lines strictly separating \(z\) from both \(x,y\); for these lines the sum of the two separation indicators exceeds that for \(x,y\) by two. Thus the triangle inequality is strict for such \(z\). All shortest curves are therefore monotone reparametrizations of the Euclidean segment. The integral (1) is continuous on \(\overline B\times\overline B\). Its restriction to the compact closed disk is a metric inducing the Euclidean topology, and the open disk is dense in it, proving the completion statement.

**3. Finsler norm and strong convexity.** For interior \(x\), differentiate (1) along \(x+tv\), uniformly on compact subsets of the open disk, to obtain (2). Positivity and triangle inequality of \(F_x\) follow from its integral representation, and it is smooth off the zero section. For a Euclidean unit tangent vector \(e_\psi\), write \(h_x(\psi)=F_x(e_\psi)\). Differentiation of \(|\cos(\phi-\psi)|\), whose distributional second derivative plus itself consists of two-sided point masses at right angles, gives the exact curvature identity
\[
 h_x(\psi)+h_x''(\psi)=\frac{2}{\pi^2\sqrt{1-(x\cdot n_{\psi+\pi/2})^2}}>0.\tag{5}
\]
A planar positive support function with positive \(h+h''\) describes a smooth strictly convex co-unit oval, and \(\frac12F_x^2\) has positive-definite fiber Hessian. The segment-additivity above identifies its induced length distance with \(d\), using the uniform local first-order expansion of (1).

**4. Local anisotropy, strictly increasing recovery, and non-Riemannian rigidity.** At \(x=re_1\), substitute \(u=\sin\phi\) in (2) for the radial direction, and \(u=\cos\phi\) for the tangential direction. The resulting elementary integrals are respectively \(2\operatorname{artanh}(r)/r\) and \(2\arcsin(r)/r\), with common factor \(1/\pi^2\), establishing (3). If \(a(r)=\operatorname{artanh}r\), \(b(r)=\arcsin r\), then
\[
 b(r)-\sqrt{1-r^2}\,a(r)>0\quad(r>0),
 \qquad \frac{d}{dr}\left[b(r)-\sqrt{1-r^2}\,a(r)\right]=\frac{r\,a(r)}{\sqrt{1-r^2}}>0.
\]
It follows directly that \((a/b)'(r)>0\); its endpoint limits give the claimed bijection \([0,1)\to[1,\infty)\).

At nonzero \(r\), reflection symmetry forces any hypothetical Riemannian tangent norm to have the form \(h(\psi)=\sqrt{A\cos^2\psi+B\sin^2\psi}\), with \(A,B>0\). Direct differentiation yields \(h+h''=AB/h^3\), so \((h+h'')^{-2/3}\) must be affine in \(\sin^2\psi\). But (5) makes this function proportional to \((1-r^2\sin^2\psi)^{1/3}\), which is strictly concave rather than affine when \(r>0\). Contradiction. The radial and tangential values differ for all \(r>0\), while at \(r=0\) (2) is the Euclidean norm multiplied by \(2/\pi^2\). Hence the center is the unique isotropic point.

**5. Radial and boundary formulas.** Integrating the radial length element from (3) along its unique minimizing segment gives
\[
 d(0,re_1)=\frac2{\pi^2}\int_0^r\frac{\operatorname{artanh}t}{t}\,dt
 =\frac{\operatorname{Li}_2(r)-\operatorname{Li}_2(-r)}{\pi^2}.
\]
At \(r=1\) the Euler dilogarithm values \(\operatorname{Li}_2(1)=\pi^2/6\) and \(\operatorname{Li}_2(-1)=-\pi^2/12\) give \(1/4\). For two boundary points with minor angular separation \(\alpha\), the random chord intersects their joining chord exactly when its endpoints fall in opposite arcs of proportions \(\alpha/(2\pi)\) and \(1-\alpha/(2\pi)\). Their crossing probability is twice the product, yielding (4). Finally \(\operatorname{artanh}r\sim\frac12\log(2/(1-r))\) and \(\arcsin r\to\pi/2\) give the boundary-density statements.

**6. Intrinsic isometry rigidity.** An isometry of the completed disk is a homeomorphism and preserves its topological boundary. By the strictly increasing boundary distance in (4), any boundary restriction preserves the usual shorter angular distance, hence equals the restriction of some unique element of \(O(2)\). Compose with that orthogonal isometry to make the boundary action the identity. The center is then fixed: it is the unique metric midpoint of any diametral boundary pair \(u,-u\), by segment uniqueness and reflection symmetry of the radial distance. The isometry preserves the unique geodesic segment \([0,u]\) pointwise as a set, and the strictly increasing function \(r\mapsto d(0,ru)\) then fixes every point on it. Varying \(u\) covers the disk. Thus the composed isometry is the identity, and the original isometry is orthogonal.

## Verification
Run \(\texttt{python3 checker.py}\) with a standard Python 3 installation. The checker performs composite-Simpson quadrature on the exact two-point and infinitesimal formulas; compares three radial values with the independently evaluated absolutely convergent dilogarithm series; compares three boundary distances to the direct combinatorial formula; checks two finite-difference slopes; and independently simulates the original pair of endpoint angles for three segments (300,000 trials per segment, deterministic seed). The recorded run terminated with \(\texttt{CHORD_CROFTON_FINSLER_METRIC_CHECK_OK}\). These numerical checks are diagnostics; the exact assertions follow from the proof above, not from sampling or quadrature.

## Relationship to prior work
The fact that a positive line-separation measure defines a projective metric is classical and is **not** claimed here. Schneider's survey gives this metric construction explicitly, while Aramyan develops the inverse Crofton framework and Álvarez Paiva studies projective Finsler metrics in a substantially broader setting. The random-endpoint arcsine law is also a standard sampling fact (Bertrand's paradox). Bortolotto and Souza compute a **two-random-chord intersection-location** distribution, not the fixed-pair line-separation distance. The assessed claim is the evaluated endpoint-chord disk model as a single explicit geometric structure: two-point kernel, uniquely characterized intrinsic isotropy and strictly invertible two-direction radial signature, proof of non-Riemannian character away from the center, and precise boundary completion. These statements are not inferred from the titles of prior publications, and the general Crofton theorem is explicitly acknowledged as prior coverage.

## Limitations
This is a theorem for one specified chord measure and a round Euclidean disk. No analogous radial formula is claimed for arbitrary convex curves or other endpoint densities. General projective-Finsler existence and straight-geodesic results are known; their rederivation is explanatory only. The position-recovery statement assumes identification of the radial and tangential Euclidean directions, and the intrinsic center is characterized by its isotropic norm. No claim is made that this construction exhausts all metrics with straight geodesics. Historical priority over unindexed special-model computations cannot be guaranteed by finite searches. No independent audit has been performed.

## References
1. R. Aramyan, *Reconstruction of Crofton Measures from Projective Finsler Metrics in R3*, arXiv:1103.4088 (first posted 2011-03-21), https://arxiv.org/abs/1103.4088.
2. R. Schneider, *On integral geometry in projective Finsler spaces*, mathematical preprint, https://home.mathematik.uni-freiburg.de/rschnei/IG.proj.Finsler.pdf; in particular Section 1, which credits the classical line-separation characterization.
3. J.-C. Álvarez Paiva, *Asymmetry in Hilbert's Fourth Problem*, arXiv:1301.2524 (2013), https://arxiv.org/abs/1301.2524.
4. C. Bortolotto and V. Souza, *Intersections of random chords of a circle*, arXiv:2504.12866 (2025), https://arxiv.org/abs/2504.12866; the two-independent-chord intersection problem is distinct from the fixed-pair separation problem treated here.
5. L. A. Santaló, *Integral Geometry and Geometric Probability*, 1976, for classical Crofton measures and the need to specify the sampling rule.
