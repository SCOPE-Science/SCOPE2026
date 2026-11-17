# Second-order central-hole response in Sylvester’s four-point problem

## Finding
Write \(D=\{x\in\mathbb R^2:\|x\|<1\}\). For \(0<t<1\), let \(X_1,\ldots,X_4\) be independent uniform-area samples from \(D\setminus\sqrt t D\), and let \(Q(t)\) denote the probability that all four lie in strictly convex position. Then, as \(t\downarrow0\),
\[
\boxed{Q(t)=1-\frac{35}{12\pi^2}+
\left(1-\frac{19}{3\pi^2}\right)t+
\left(1-\frac{95}{6\pi^2}\right)t^2+o(t^2).}
\]
The linear response was already known. The new assertion is the exact second-order response: \(1-95/(6\pi^2)=-0.604252074337\ldots<0\). Although removing an infinitesimal central disk initially increases convex-position probability, the response exhibits a strictly negative second-order correction. The phenomenon depends on configurations in which **two** of the four points occupy the shrinking disk. The formula holds, without changing coefficients, for an elliptic outer region with a concentric homothetic elliptic hole.

## Assumptions and scope
All samples use normalized two-dimensional Lebesgue measure on the specified annulus. Strict convex position means that each sample is a vertex of the convex hull of all four samples; degenerate triples have probability zero. The expansion is one-sided at \(t=0\), with \(t\) the **area fraction** of the removed disk (not its radius). The remainder is \(o(t^2)\), and no stronger rate, finite-hole formula, or global concavity is claimed.

## Proof
**1. Condition on removed-disk samples.** Put \(E=\{X_1,X_2,X_3,X_4\text{ are in strictly convex position}\}\), initially with independent points uniform on the entire disk \(D\). Let \(Q_k(t)\) be the convex-position probability when exactly \(k\) specified points are uniform in \(\sqrt tD\) and the other \(4-k\) points are uniform in \(D\), all independently. Since a full-disk point lies in the small disk with probability \(t\), inclusion-exclusion gives the **exact** identity
\[
(1-t)^4 Q(t)=\sum_{k=0}^4(-1)^k\binom4k t^kQ_k(t).
\]
The known disk value is \(Q_0=1-35/(12\pi^2)\). Since all the \(Q_k(t)\) lie between zero and one, the terms with \(k\ge3\) contribute \(O(t^3)\). It remains to evaluate \(Q_1(t)\) to first order and \(Q_2(t)\) to constant order.

**2. Exact one-fixed-point decomposition.** Fix \(q=(u,0)\in D\), and let \(Y_1,Y_2,Y_3\) be independent uniform-disk points. Define \(q_1(u)=\Pr(q,Y_1,Y_2,Y_3\text{ are in convex position})\). The four mutually exclusive ways of failing convex position yield
\[
q_1(u)=1-F(u)-\frac3\pi M(u),\qquad
F(u)=\Pr(q\in\operatorname{conv}(Y_1,Y_2,Y_3)),\quad
M(u)=\mathbb E[\operatorname{area}(\triangle(q,Y_1,Y_2))].
\]
Indeed, each event in which one of the \(Y_i\) lies in the triangle of the other three has conditional probability \(M(u)/\pi\) by the full-disk area law.

**3. Expand the triangle-containment probability.** From \(q\), the radius to the unit circle in direction \(\theta\) is \(R_u(\theta)=-u\cos\theta+\sqrt{1-u^2\sin^2\theta}\). Therefore the direction of a uniform-disk point seen from \(q\) has density
\[
f_u(\theta)=\frac{R_u(\theta)^2}{2\pi}
=\frac{1-2u\cos\theta+u^2\cos(2\theta)}{2\pi}+O(u^3),
\]
uniformly in \(\theta\). Write \(H_u(\theta)=\int_\theta^{\theta+\pi}f_u(\phi)\,d\phi\). Then
\[
H_u(\theta)=\tfrac12+\frac{2u}{\pi}\sin\theta+O(u^3).
\]
For three independent planar directions in general position, the probability of all lying in some open semicircle is \(3\int_0^{2\pi}f_u(\theta)H_u(\theta)^2d\theta\): the anchoring point of a containing semicircle is almost surely unique. Its complement is the event that the origin belongs to the angular triangle, hence
\[
F(u)=1-3\int_0^{2\pi}f_u(\theta)H_u(\theta)^2d\theta
=\frac14-\frac6{\pi^2}u^2+o(u^2).
\]
The last equality follows by integrating the stated trigonometric expansions; odd terms vanish.

**4. Expand the area expectation.** For \(Y,Z\) independent uniform in \(D\), condition on \(Y\) and write \(v=(Y-q)/\|Y-q\|\), with unit normal \(v^\perp\). Put \(g(c)=\mathbb E_Z|Z\cdot v^\perp-c|\), a function independent of \(v\) by rotational symmetry. The disk's one-dimensional marginal gives \(g(0)=4/(3\pi)\), \(g'(0)=0\) and \(g''(0)=4/\pi\). Consequently
\[
M(u)=\frac12\mathbb E_Y\bigl[\|Y-q\|g(q\cdot v^\perp)\bigr].
\]
Elementary differentiation under the integral (the distance Hessian is locally integrable in two dimensions) gives
\[
\mathbb E\|Y-q\|=\frac23+\frac{u^2}{2}+o(u^2),\qquad
\mathbb E\bigl[\|Y-q\|(q\cdot v^\perp)^2\bigr]=\frac{u^2}{3}+o(u^2).
\]
Substitution yields
\[
M(u)=\frac4{9\pi}+\frac{2u^2}{3\pi}+o(u^2).
\]
Together with the preceding step,
\[
q_1(u)=\frac34-\frac4{3\pi^2}+\frac4{\pi^2}u^2+o(u^2).
\]
Since an area-uniform point in \(\sqrt tD\) has squared radius of mean \(t/2\), averaging uniformly over the small disk shows
\[
Q_1(t)=\frac34-\frac4{3\pi^2}+\frac2{\pi^2}t+o(t).
\]
The small-order remainders are uniform on the shrinking radius interval by the local smoothness established above.

**5. Two-point collision law.** For \(Q_2(t)\), write the two near-origin points as \(\sqrt tU,\sqrt tV\), where \(U,V\) are independent uniform on \(D\), and let \(Y,Z\) be independent uniform points on \(D\). Fix a realization with \(Y,Z\ne0\), distinct non-antipodal directions, and \(U\ne V\). Except when the direction of \(U-V\) lies on one of two cone boundaries (a null event), for sufficiently small \(t\) the four points fail convex position precisely when \(U-V\) or \(V-U\) lies in the positive cone generated by \(Y,Z\). Denote by \(\alpha\in(0,\pi)\) the smaller angle between the directions of \(Y,Z\). The direction of \(U-V\) is uniform on the circle and independent of \(Y,Z\), so conditional failure has probability \(\alpha/\pi\), and conditional convexity probability \(1-\alpha/\pi\). The independent directions of \(Y,Z\) are uniform, making \(\alpha\) uniform on \([0,\pi]\). By dominated convergence,
\[
\lim_{t\downarrow0}Q_2(t)=\mathbb E(1-\alpha/\pi)=\frac12.
\]
Notice that the outer points here remain **area-uniform**; the cone argument uses their directions only.

**6. Assemble the second-order term.** Insert the three quantities into the exact inclusion-exclusion identity:
\[
(1-t)^4Q(t)=\left(1-\frac{35}{12\pi^2}\right)
-4\left(\frac34-\frac4{3\pi^2}\right)t
+\left(3-\frac8{\pi^2}\right)t^2+o(t^2).
\]
Since \((1-t)^{-4}=1+4t+10t^2+O(t^3)\), multiplication gives the stated formula. The sign of the new coefficient follows from \(95/(6\pi^2)>1\). An invertible affine map sending a concentric homothetic elliptic annulus to the concentric round annulus preserves normalized area sampling and convex position, proving the elliptic assertion.

## Verification
The self-contained `check_sylvester_annulus.py` numerically tests the exact binomial-coefficient identity, the fixed-point local expansion, the two-near-center collision probability, and the predicted annular convex-position probabilities using independent Cartesian triangle-containment tests. It uses a fixed pseudorandom seed and NumPy. All four diagnostics pass with the embedded tolerances. These finite experiments support but do not prove the displayed expansion; the proof is the integral, cone, and inclusion-exclusion argument above.

## Relationship to prior work
The classical disk value \(1-35/(12\pi^2)\), developed in the Sylvester–Woolhouse–Blaschke tradition, and the disk convex-position recursion in Marckert (2014) are known. Marckert's later treatment (first public 2015) establishes convex-body comparisons; the nonconvex annulus lies outside its stated hypotheses. A previously obtained first-order puncture susceptibility already gives the coefficient \(1-19/(3\pi^2)\); that linear term is **not** claimed as new. The present result concerns the next coefficient and establishes it through the independent two-near-center collision mechanism. Ionașcu's work gives general fixed-point triangle-containment formulas but does not supply the four-sample annulus second-order response. Related thin-*shell* limits concern an inner radius approaching one, not the small-*hole* limit studied here. The source comparisons and novelty statement do not assert historical priority beyond the checked material.

## Limitations
The theorem does not address holes centered away from the origin, unequal inner/outer ellipse centers, higher-point convex-position probabilities, or a globally monotone or concave annulus law. The formula is an asymptotic as the hole area fraction tends to zero; no effective error constant is claimed. The classical baseline, the first variation, and the two-point collision limit separately are not presented as novel. An independent mathematical audit and a definitive historical-priority determination have not been performed.

## References
- J.-F. Marckert, *Probability that n random points in a disk are in convex position*, arXiv:1402.3512, first public 2014-02-14; https://arxiv.org/abs/1402.3512.
- J.-F. Marckert, *Around Sylvester's question in the plane*, arXiv:1511.03658, first public 2015-11-11; https://arxiv.org/abs/1511.03658.
- E. J. Ionașcu, *Random triangles in planar regions containing a fixed point*, arXiv:1612.08619, first public 2016-12-15; https://arxiv.org/abs/1612.08619 (supporting literature, not the archival anchor).
- W. S. B. Woolhouse, *Some Additional Observations on the Four-Point Problem*, Mathematical Questions with Their Solutions from the Educational Times 7 (1867), p. 81; classical disk-area probability.
