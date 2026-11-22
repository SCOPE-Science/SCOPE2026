# Quartic circularity and square-root flattening for random Steiner inellipses

## Finding

Let \(Z_1,Z_2,Z_3\) be independent uniformly distributed points on the unit circle in \(\mathbb R^2\). Almost surely they form a nondegenerate triangle \(T\). Let \(E(T)\) be its Steiner inellipse: the unique ellipse contained in \(T\), tangent to all three sides at their midpoints, and of maximal area among ellipses in \(T\). Write \(a_E\ge b_E>0\) for its semiaxes, \(R=b_E/a_E\) for its axis ratio, and \(e=\sqrt{1-R^2}\) for its usual eccentricity.

**Theorem.** Both endpoints of the eccentricity distribution have exact, different powers:
\[
\Pr(e<t)=\frac{3\sqrt3}{16\pi}t^4+o(t^4),\qquad
\Pr(e>1-t)=\frac{4\sqrt6}{\pi}t^{1/2}+o(t^{1/2})
\quad(t\downarrow0).
\]
Equivalently, its thin-axis tail is
\[
\Pr(R<\eta)=\frac{4\sqrt3}{\pi}\eta+o(\eta)
\quad(\eta\downarrow0).
\]

The two rare events have different **marked total-variation limits**:

1. For \(e<t\), after fixing the first vertex as angular origin, the other two angles lie near one of the two labelled equilateral configurations, each with limiting probability \(1/2\). With their deviations from that configuration divided by \(t^2\), the joint law converges in total variation to the uniform law on
\[
\mathcal E=\{(u,v)\in\mathbb R^2:u^2+v^2-uv<9/16\}.
\]
The overall rotation of the triangle is independent and uniform throughout.
2. For \(R<\eta\), there is with conditional probability tending to one exactly one pair of vertices with angular gap of order \(\eta\). Its unordered label is asymptotically uniform among the three possible pairs. Orient the gap by increasing labels, with signed principal angle \(\Delta\), and write \(\gamma\) for the lower-labelled point's angle and \(\tau\) for the third point's angle relative to \(\gamma\). Conditional on the rare event, \((\Delta/\eta,\gamma,\tau)\) converges in total variation to independent uniforms on \((-4/\sqrt3,4/\sqrt3)\), \([0,2\pi)\) and \([0,2\pi)\), respectively. The same marked limit for \(e>1-t\) uses gap scale \(\sqrt t\) and interval \((-4\sqrt{2/3},4\sqrt{2/3})\).

## Assumptions and scope

All angles are taken modulo \(2\pi\), and a signed short angular gap is in \((-\pi,\pi]\). The sampling is iid uniform angular measure, equivalently Euclidean arclength on the unit circle. All probability statements concern labelled independent points. Zero-probability coincidences and degenerate triangles can be defined arbitrarily. The limits are for fixed unit-circle geometry as the stated scalar threshold decreases to zero. The use of total variation is for the explicit marked coordinates above, not for the original unscaled sample law versus a singular support.

## Proof

**Step 1: express the optimal inellipse axes through centered triangle geometry.** Write \(p_j\in\mathbb R^2\) for the vertices, \(g=(p_1+p_2+p_3)/3\), \(v_j=p_j-g\), and \(S=\sum_{j=1}^3v_jv_j^{\mathsf T}\). A parametrization of the Steiner circumellipse is
\[
g+v_1\cos\theta+\frac{v_2-v_3}{\sqrt3}\sin\theta.
\]
Indeed it passes through all three vertices at \(\theta=0,2\pi/3,4\pi/3\), and by the usual affine image of an equilateral triangle its half-scaled ellipse about \(g\) is the Steiner inellipse. The matrix defining these semiaxes is
\[
 v_1v_1^{\mathsf T}+\tfrac13(v_2-v_3)(v_2-v_3)^{\mathsf T}=\tfrac23 S.
\]
Hence the squared semiaxis ratio of the inellipse equals the ratio of the smaller to larger eigenvalue of \(S\).

Let \(\ell_{ij}=|p_i-p_j|\), \(\Sigma=\ell_{12}^2+\ell_{23}^2+\ell_{31}^2\), and \(A_T\) denote the unsigned Euclidean area of \(T\). Centering identities and Cauchy–Binet give
\[
\operatorname{tr}S=\frac\Sigma3,\qquad \det S=\frac{4A_T^2}{3}.
\]
On the unit circumcircle, \(4A_T=\ell_{12}\ell_{23}\ell_{31}\). Consequently, setting
\[
 K=\frac{2\sqrt{\det S}}{\operatorname{tr}S}
 =\frac{\sqrt3\,\ell_{12}\ell_{23}\ell_{31}}\Sigma
\]
yields the **exact** axis-ratio identities
\[
K=\frac{2R}{1+R^2},\qquad
R=\frac{K}{1+\sqrt{1-K^2}},\qquad e=\sqrt{1-R^2}.
\]
All denominators are positive for a nondegenerate triangle, \(0<K\le1\), and \(K=1\) holds precisely for equilateral triangles.

**Step 2: localize circularity near the equilateral configurations.** Rotational invariance allows the first angle to be zero; the second and third are then independent uniform angles on \([0,2\pi)\). The only circular inellipses correspond to the two configurations \((2\pi/3,4\pi/3)\) and its reversal. In either neighborhood, write their angular deviations as \(u,v\), using the corresponding order of the two cube roots of unity. Put \(\omega=e^{2\pi i/3}\) and identify \(p_j\) with \(z_j\). The complex trace-free entry of \(S\) is
\[
 B=\sum_j(z_j-g)^2=\sum_jz_j^2-\frac{(\sum_jz_j)^2}{3}.
\]
The eigenvalue contrast \(Q=(\lambda_+-\lambda_-)/(\lambda_++\lambda_-)\) equals \(|B|/\operatorname{tr}S\). Taylor expansion at the displayed equilateral configuration gives
\[
B=2i(\omega^2u+\omega v)+O(u^2+v^2),\qquad
Q=\frac23\sqrt{u^2+v^2-uv}+O(u^2+v^2).
\]
Because \(e^2=2Q/(1+Q)\), the threshold \(e<t\) after scaling \((u,v)=t^2(U,V)\) converges to the ellipse \(U^2+V^2-UV<9/16\). The quadratic form has determinant \(3/4\), so that ellipse has area \(9\pi/(8\sqrt3)\). The two configuration neighborhoods have joint angular density \((2\pi)^{-2}\). Therefore
\[
 \lim_{t\downarrow0}\frac{\Pr(e<t)}{t^4}
 =\frac{2}{(2\pi)^2}\frac{9\pi}{8\sqrt3}
 =\frac{3\sqrt3}{16\pi}.
\]
The local reparameterized densities are bounded constants times indicators of convergent bounded domains. Their \(L^1\) convergence proves the stated marked total-variation limit. Uniform overall rotation is exact by symmetry.

**Step 3: localize flattening at pair collisions.** Choose a shortest side of length \(d\) and write the other two side lengths as \(b\le c\). The triangle inequality gives \(d\le b\le c\le b+d\le2b\). Therefore
\[
 K=\frac{\sqrt3dbc}{d^2+b^2+c^2}\ge\frac{\sqrt3}{6}d,
 \qquad R\ge K/2\ge \frac{\sqrt3}{12}d.
\]
So \(R<\eta\) forces some vertex pair to have chordal separation less than \(4\sqrt3\eta\). In particular the entire rare event is contained in three width-\(O(\eta)\) pair-collision neighborhoods.

Fix one such pair, place its first point at angle \(\gamma\), the second at \(\gamma+\Delta\), and the third at relative angle \(\tau\). Uniformly for \(\tau\) bounded away from \(0\) modulo \(2\pi\), the three chord lengths are \(|\Delta|+O(|\Delta|^3)\) and two copies of \(2|\sin(\tau/2)|+O(|\Delta|)\). Substituting into the exact formula for \(K\) gives
\[
K=\frac{\sqrt3}{2}|\Delta|+O_{\tau}(\Delta^2),
\qquad R=\frac{\sqrt3}{4}|\Delta|+O_{\tau}(\Delta^2).
\]
Thus the window \(R<\eta\) has limiting signed-gap width \(8\eta/\sqrt3\), independently of the third vertex's location as long as it stays away from the collision. A given pair has probability
\[
\frac{8\eta/\sqrt3}{2\pi}+o(\eta)=\frac4{\pi\sqrt3}\eta+o(\eta).
\]
There are three possible pairs. For any fixed angular exclusion \(\rho>0\), the portion where the third point lies within \(\rho\) of the colliding pair has probability \(O(\rho\eta)\), uniformly for small \(\eta\), because the above global localization already forces a pair gap \(O(\eta)\). Multiple competing close-pair windows are \(O(\eta^2)\). First letting \(\eta\downarrow0\), then \(\rho\downarrow0\), establishes
\[
 \lim_{\eta\downarrow0}\eta^{-1}\Pr(R<\eta)
 =3\frac4{\pi\sqrt3}=\frac{4\sqrt3}{\pi}.
\]
The same uniform-window argument, with localization of the negligible triple-collision set, gives \(L^1\) convergence of conditional marked densities and the claimed total-variation limit.

**Step 4: convert axis ratio to eccentricity.** By definition, \(e>1-t\) is equivalent to \(R<\sqrt{2t-t^2}\). Inserting \(\eta=\sqrt{2t-t^2}\) in Step 3 yields the square-root law with coefficient \(4\sqrt6/\pi\) and the corresponding marked law.

## Verification

The standalone `checker.py` implements the exact chord-product expression independently of the centered covariance eigenvalue calculation. It asserts agreement for 1000 nondegenerate deterministic triples and verifies the collision differential for six third-vertex positions. Its deterministic Sobol quadrature of \(2^{22}\) triples checks convergence toward the constants \(3\sqrt3/(16\pi)\) and \(4\sqrt3/\pi\). In particular, the scaled small-eccentricity coefficients observed at thresholds \(0.30,0.20,0.14\) are approximately \(0.11409,0.10788,0.10551\), approaching \(0.10337416789\ldots\). At axis-ratio threshold \(0.04\), the observed coefficient is approximately \(2.20033\), compared with \(2.20531558169\ldots\). These finite numerical checks do not replace Steps 1–4 of the proof.

To reproduce, install `requirements.txt` and run `python checker.py` with Python 3. The checker is a standalone diagnostic, not a formal theorem prover.

## Relationship to prior work

The Steiner inellipse, its maximal-area property and the derivative-root interpretation of its foci are classical (Siebeck–Marden; Minda–Phelps; Rohe). They are **premises**, not new results here. The cited sources address geometric constructions, algebraic foci and triangle ellipses, not the iid circle-boundary sampling law and its two extreme marked distributions. Random cyclic-triangle area and random interior-triangle shape distributions are different statistics or different sampling measures and do not alone determine the eccentricity law. The new claims are the two sharp probability coefficients/powers and the corresponding conditional limits, not the existing ellipse construction.

## Limitations

The result is restricted to three iid arclength-uniform boundary points of a circle and the Euclidean eccentricity of their maximum-area Steiner inellipse. The tail limits are pointwise; no uniform law is claimed for nonuniform sampling, ellipse-host boundaries or increasing sample size. The source comparison is broad but not exhaustive: Scimemi (2010) was identifiable by an index and abstract, while its original full text was inaccessible during examination. No independent mathematical audit or historical priority certification has been performed.

## References

1. D. Minda and S. Phelps, *Triangles, Ellipses, and Cubic Polynomials*, American Mathematical Monthly **115** (2008), 679–689. DOI: https://doi.org/10.1080/00029890.2008.11920581 . Public author-supplied text: https://www.researchgate.net/publication/228698127_Triangles_Ellipses_and_Cubic_Polynomials .
2. B. Scimemi, *Simple Relations Regarding the Steiner Inellipse of a Triangle*, Forum Geometricorum **10** (2010), 55–77. Bibliographic record: https://portal.mardi4nfdi.de/wiki/Simple_relations_regarding_the_Steiner_inellipse_of_a_triangle .
3. K. Rohe, *Visualizing Marden's theorem with Scilab*, arXiv:1502.01367 (first public version 2015-02-04), https://arxiv.org/abs/1502.01367 .
4. E. W. Weisstein, *Circle Triangle Picking*, Wolfram MathWorld, https://mathworld.wolfram.com/CircleTrianglePicking.html (reference for the boundary-random cyclic-triangle measure, not the inellipse statistic).
