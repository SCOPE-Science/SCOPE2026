# Thin-ellipse separation of acuteness and center enclosure

## Finding
Let \(L\ge1\). Independently sample \(\Theta_1,\Theta_2,\Theta_3\) uniformly on \([0,2\pi)\), and let \(P_i=(L\cos\Theta_i,\sin\Theta_i)\). Write \(A_L\) for the event that their nondegenerate Euclidean triangle is strictly acute, and \(C_L\) for the event that its interior contains the origin (the ellipse's center). Then
\[
\boxed{\lim_{L\to\infty}L^2\Pr(A_L\cap C_L)=\frac{6\log2}{\pi^2}.}
\]
The origin-enclosure probability is exactly \(1/4\) for every \(L\). The *previously established* marginal acuteness law is \(\Pr(A_L)=\tfrac14-\frac{3}{2\pi^2}\operatorname{Li}_2(((L^2-1)/(L^2+1))^2)\), and it gives \(\Pr(A_L)\sim12\log L/(\pi^2L^2)\). Combining this existing result with the new joint law yields
\[
\boxed{\Pr(C_L\mid A_L)\sim\frac{\log2}{2\log L}.}
\]
Thus the circle's identity between strict acuteness and enclosure of the curve's center fails maximally in the thin affine-ellipse limit.

There is also a **conditional marked limit**. Let \(x_i=\cos\Theta_i\). On \(A_L\cap C_L\), choose the pair whose \(x_i\)-values are closest (a.s. unique), let \(c_L\) be the mean of their two \(x_i\)-values, and let \(d_L\) be the remaining \(x_i\). Then, conditioned on \(A_L\cap C_L\), \((R_L,U_L)=(|d_L|,|c_L|/|d_L|)\) converges in total variation, as \(L\to\infty\), to **independent** random variables \(R,U\) with densities
\[
\boxed{ f_R(r)=\frac{2}{\pi\sqrt{1-r^2}}\mathbf1_{(0,1)}(r),\qquad
f_U(u)=\frac{1}{(1+u)\log2}\mathbf1_{(0,1)}(u). }
\]
The asserted total-variation convergence is on the two-dimensional mark distribution, with mass outside \((0,1)^2\) tending to zero. The exact coefficient and this marked geometric law are a single joint finding; the known marginal acuteness formula is background rather than a second novelty claim.

## Assumptions and scope
The ellipse has semiaxes \(L\) and \(1\); any ellipse with aspect ratio \(L\) is equivalent by similarity. The sampling is the pushforward of *uniform angular sampling* on the unit circle, also called equiaffine arclength on an ellipse. This is not ordinary Euclidean-arclength sampling on a noncircular ellipse. Strict right angles, coincident vertices, boundary enclosure, and exact ties in the closest pair are null events. The theorem assumes three independent points and takes \(L\to\infty\) through positive finite aspect ratios.

## Proof
**1. Coordinate law and center enclosure.** Put \(x_i=\cos\Theta_i\) and \(y_i=\sin\Theta_i\). Each \(x_i\) has arcsine density \((\pi\sqrt{1-x^2})^{-1}\) on \((-1,1)\), and conditional on \(x_i\), the sign of \(y_i=\pm\sqrt{1-x_i^2}\) is fair and independent. Affine linear maps preserve convex-hull containment. Three uniform points on a circle enclose its center exactly when none of their three circular gaps exceeds \(\pi\). The elementary gap-simplex calculation gives \(\Pr(C_L)=1/4\).

**2. Necessary near-vertical pair.** Order the three distinct abscissas as \(x_{(1)}<x_{(2)}<x_{(3)}\), with consecutive gaps \(g_1,g_2\). At the middle-abscissa vertex, the ordinary Euclidean inner product of its two edge vectors is
\[
-L^2g_1g_2+(y_{(1)}-y_{(2)})(y_{(3)}-y_{(2)}).
\]
Thus acuteness forces \(L^2g_1g_2<4\). Origin enclosure forces \(x_{(1)}<0<x_{(3)}\). In any region where one of \(g_1,g_2\) stays bounded away from zero, the other is \(O(L^{-2})\). The simultaneous-small-gap corner gives no contribution at scale \(L^{-2}\): if \(x_{(1)}=-a<0<x_{(3)}=b\), the permitted interval for \(x_{(2)}\) has length at most \(\min(a+b,\,O(L^{-2}/(a+b)))\). Integrating this over \(a+b<h\), where all three arcsine densities are bounded for fixed small \(h\), gives \(O(hL^{-2})+O(L^{-3})\). Then \(h\downarrow0\). This establishes the required one-pair localization; configurations away from the limiting opposite-sign branches or close to the arcsine endpoints are handled by truncating \(|x|\le1-\eta\) and applying the integrable majorant obtained below before letting \(\eta\downarrow0\).

**3. The local angular-pair integral.** Fix one of the three possible close pairs and choose the two opposite sine branches. Their abscissas tend to a common value \(c\in(-1,1)\), their ordinates to \(s=\sqrt{1-c^2}\) and \(-s\), and the third point is \((Ld,t)\) with \(d=\cos\phi\), \(t=\sin\phi\). Write \(\delta=x_2-x_1\), ordering the pair so the first ordinate tends to \(s\). The two acute-angle inequalities at the close vertices, after multiplication by positive factors, reduce to the asymptotic interval
\[
2s(t-s)<L^2\delta(d-c)<2s(t+s).
\]
Its width in \(\delta\) is \(4s^2/(L^2|d-c|)\). The third angle is automatically acute when \(d\ne c\) as \(L\to\infty\). If the near pair lies on the *same* sine branch, its ordinate difference vanishes, and its local acute interval has vanishing \(L^{-2}\)-scaled length.

The origin is inside the limiting triangle precisely when \(cd<0\) and \(|d|>|c|\): the segment from the third vertex to the near-vertical chord passes through the origin exactly when the required vertical-coordinate intersection belongs to \((-s,s)\). Equivalently \(|ct|<|d|s\), which simplifies to \(c^2<d^2\). For opposite sine branches the two-angle Jacobian is \(dc\,d\delta/(1-c^2)\) to leading order, cancelling the factor \(s^2\) from the interval width.

Counting three choices of close pair and two orders of its sine branches, the resulting limit is
\[
\lim_{L\to\infty}L^2\Pr(A_L\cap C_L)
=\frac{3}{\pi^3}\int_{-1}^1\int_0^{2\pi}
\frac{\mathbf1\{cd<0,\ |d|>|c|\}}{|d-c|}\,d\phi\,dc,
\quad d=\cos\phi.
\]
For justification beyond compactly separated parameter sets, note that after switching to \(r=|d|,\ u=|c|\), the positive kernel is bounded by a constant multiple of \(\mathbf1\{0<u<r<1\}/[(u+r)\sqrt{1-r^2}]\). Its integral is finite. The boundary corner at \(u=r=0\) and the arcsine endpoints may therefore be exhausted by dominated convergence; the simultaneous-small-gap error from Step 2 closes the localization. These bounds apply as well to bounded test functions of the marks, giving \(L^1\) convergence of their densities.

**4. Constant and marks.** By symmetry and the two preimages of each cosine value,
\[
J:=\int_{-1}^1\int_0^{2\pi}
\frac{\mathbf1\{cd<0,\ |d|>|c|\}}{|d-c|}\,d\phi\,dc
=4\int_0^1\frac{dr}{\sqrt{1-r^2}}\int_0^r\frac{du}{u+r}.
\]
The inner integral is \(\log2\), so \(J=2\pi\log2\), proving the coefficient. Conditional on the rare event, the limiting positive variables \((|c|,|d|)\) have joint density proportional to \(\mathbf1\{0<u<r<1\}/[(u+r)\sqrt{1-r^2}]\). On setting \(v=u/r\), the Jacobian cancels the \(r\) factor and the normalized density factors as
\[
\frac{2}{\pi\sqrt{1-r^2}}\,\frac{1}{(1+v)\log2},\qquad 0<r,v<1.
\]
The localization and the integrable density majorant yield convergence in \(L^1\), hence total variation, not merely convergence of expectations. Finally the displayed marginal acuteness asymptotic is a consequence of the already-known dilogarithmic formula, and division proves the conditional probability.

## Verification
Execute `python checker.py` with Python 3 and NumPy/SciPy installed. It checks the analytic two-dimensional kernel normalization by independent quadrature and samples six million independently generated triples at aspect ratios \(5,10,20\), evaluating all three Euclidean dot products and the independent angular-gap center-enclosure criterion. At aspect ratios \(5,10,20\), its fixed-seed scaled joint frequencies were \(0.410875,0.415700,0.418600\), approaching \(6\log2/\pi^2=0.42138296\ldots\). At aspect ratio 20, the empirical conditional mark means were \(0.64113,0.43252\), compared with exact limiting means \(2/\pi=0.63662\ldots\) and \(1/\log2-1=0.44270\ldots\). Numerical experiments are corroboration only; the localization and density argument proves the limit.

## Relationship to prior work
The previously published equiaffine-ellipse acuteness result provides the **marginal** dilogarithmic law and its thin-ellipse asymptotic, but its event probability alone does not specify how often acute triangles contain the ellipse center. Uniform-circle enclosure has the classical probability \(1/4\). The off-center circle-enclosure dilogarithm formula is a different event and does not imply the present same-triangle joint limit. An earlier arclength-uniform ellipse calculation concerns a different sampling measure. Koroleva and Nikitin's 2013 full text analyzes extreme perimeters and areas of *circular* random polygons, not the present joint acute-center event. The contribution is the sharp joint coincidence law and its independently factorized conditional shape distribution, not a new marginal acuteness calculation.

## Limitations
The result applies to exactly three independent uniform-eccentric-anomaly points on a nondegenerate ellipse as its axis ratio diverges. It is not an exact finite-aspect-ratio joint distribution, does not cover ordinary Euclidean-arclength ellipse sampling, and makes no assertion about nonelliptic convex curves. An explicit convergence rate in total variation is not claimed. Search-based novelty assessment and numerical checks are not independent validation.

## References
1. *Sharp dilogarithmic acuteness law for affine-uniform ellipse triangles* (public mathematical result, 2026), identifier `a5911e351b92`.
2. *Dilogarithmic acute-triangle law for equiaffine-uniform ellipses* (public mathematical result, 2026), identifier `0b2e5b1aac57`.
3. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, first posted 2013-01-07, https://arxiv.org/abs/1301.1360.
4. J. Tan Jie Rui, solution to *Probability that a random triangle with vertices on a circle contains an arbitrary point inside said circle*, published 2018-02-10, https://math.stackexchange.com/questions/2641793/probability-that-a-random-triangle-with-vertices-on-a-circle-contains-an-arbitra.
5. C. Boilley, answer to *Probability that Triangle on Ellipse is Acute* (2025-01-24, ordinary Euclidean-arclength sampling), https://math.stackexchange.com/questions/5014676/probability-that-triangle-on-ellipse-is-acute.
