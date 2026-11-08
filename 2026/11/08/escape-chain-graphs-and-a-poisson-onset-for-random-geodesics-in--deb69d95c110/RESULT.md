# Escape-chain graphs and a Poisson onset for random geodesics in reflex spherical sectors

## Finding

Fix \(d\ge2\), \(n\ge2\), and an azimuthal sector of the unit sphere \(S^d\) with opening \(0<\alpha<2\pi\). Sample \(n\) independent points with independent uniform azimuths in the sector. A pair is joined in the *escape graph* exactly when its shorter great-circle geodesic leaves the sector. **Every escape edge is determined by the two azimuths alone**: it occurs if and only if their numerical difference exceeds \(\pi\). Thus the random escape graph is always a bipartite chain graph, independently of ambient dimension and of all conditional coordinate distributions. In particular, its edge-free probability and edge-count variance are exactly computable; at the nonconvexity onset its full nontrivial random-graph limit is a two-process Poisson corner graph.

For \(0<\alpha\le\pi\), the graph is edgeless. For \(\pi<\alpha<2\pi\), put \(q=1-\pi/\alpha\in(0,1/2)\) and let \(M\) be its number of edges. Then
\[
\Pr\{M=0\}=n(1-q)^{n-1}-(n-1)(1-q)^n,\qquad
\mathbb E M=\binom n2 q^2,
\]
\[
\operatorname{Var}(M)=\binom n2 q^2(1-q^2)+6\binom n3\left(\frac23q^3-q^4\right).
\]
For the critical sequence \(\alpha_n=\pi(1+\lambda/n)\), \(\lambda\ge0\) fixed, delete isolated vertices from \(G_n\). The remaining finite graph converges in distribution to the following object: take two independent unit-intensity Poisson processes \(\mathcal P_-\), \(\mathcal P_+\) on \([0,\lambda]\), and connect points in opposite parts whenever \(s+t<\lambda\) (then again delete isolated vertices). In particular
\[
\Pr\{M_n=0\}\to(1+\lambda)e^{-\lambda},\quad
\mathbb E M_n\to\lambda^2/2,\quad
\operatorname{Var}(M_n)\to\lambda^2/2+2\lambda^3/3.
\]
This is a complete finite-sample zero-escape law, with an exact first-escape scaling window of width \(1/n\).

## Assumptions and scope

Write \(S^d=\{x\in\mathbb R^{d+1}:\|x\|_2=1\}\). For \(x_1^2+x_2^2>0\), let \(\phi(x)\in[0,2\pi)\) be the usual argument of \(x_1+ix_2\). Define the *reflex sector* \(L_\alpha\) using \(0\le\phi\le\alpha\). The polar axis \(x_1=x_2=0\) has zero probability under the permitted sampling laws; we may adjoin it to the sector without changing the results. The samples \(X_1,\ldots,X_n\) are independent and have azimuths \(\phi(X_i)\) independent and identically uniform on \([0,\alpha]\). No condition is placed on the conditional distribution of other coordinates given an azimuth, except that sampled points are almost surely not identical or antipodal; the latter follows automatically for independent uniform azimuths unless the conditional distribution creates a special non-atomicity failure on a probability-zero azimuth equality event. In particular, normalised spherical area measure and any restriction of an axisymmetric absolutely continuous measure satisfy the hypotheses. Here \(d\ge2\), \(n\ge2\); no claim is made for \(\alpha=2\pi\), which is the whole sphere rather than a sector with a missing seam.

A *chain graph* is a bipartite graph in which the neighborhoods of vertices within either part are nested, equivalently a bipartite graph with no induced pair of disjoint edges. Isolated vertices are permitted.

## Proof

**1. Projected shorter-arc criterion.** Take non-antipodal \(x,y\in S^d\), with spherical distance \(\theta=\arccos\langle x,y\rangle\in(0,\pi)\). The unique shorter geodesic is
\[
\gamma(t)=\frac{\sin((1-t)\theta)x+\sin(t\theta)y}{\sin\theta},\quad0\le t\le1.
\]
For \(0<t<1\), both coefficients are strictly positive. Projecting onto the first two coordinates therefore traces the positive cone between the two nonzero planar vectors \(P(x)\) and \(P(y)\). Their positive coefficient ratio runs strictly from zero to infinity: indeed, \(\sin(t\theta)/\sin((1-t)\theta)\) has derivative \(\theta\sin\theta/\sin^2((1-t)\theta)>0\). When the numerical azimuth difference \(\Delta=|\phi(x)-\phi(y)|\) is below \(\pi\), all projected directions lie between the two given azimuths and hence in \([0,\alpha]\). When \(\Delta>\pi\), they traverse the complementary planar angular interval of size \(2\pi-\Delta<\pi\), crossing azimuths outside \([0,\alpha]\). The exceptional equal/opposite azimuth pairs have probability zero. Thus
\[ij\in E(G)\iff |\phi(X_i)-\phi(X_j)|>\pi.\]
For \(\alpha\le\pi\), the inequality is impossible.

**2. Deterministic chain-graph structure.** Assume \(\pi<\alpha<2\pi\), and put \(h=\alpha-\pi\in(0,\pi)\). All edges join an azimuth in \([0,h)\) to one in \((\pi,\alpha]\); vertices in the intervening interval are isolated. If the low-part azimuths are sorted increasingly, the upper-part neighbor sets are \(\{v:v>u+\pi\}\), and are nested decreasingly. Hence \(G\) is bipartite and contains no induced \(2K_2\), independently of sample size, dimension and other coordinates.

**3. Exact empty-graph law.** For \(U_1,\ldots,U_n\overset{\rm iid}{\sim}\operatorname{Unif}[0,\alpha]\), no escape edge is equivalent to \(\max_i U_i-\min_i U_i\le\pi\). For \(0<w<\alpha\), the joint density of the minimum \(a\) and maximum \(b\) is \(n(n-1)(b-a)^{n-2}/\alpha^n\). Integrating over \(0\le a\le b\le\alpha\) with \(b-a\le w\), or differentiating the familiar range distribution, gives
\[\Pr\{\max U-\min U\le w\}=n(w/\alpha)^{n-1}-(n-1)(w/\alpha)^n.\]
Set \(w=\pi\); this yields the displayed formula.

**4. Mean and variance.** Let \(I_{ij}=\boldsymbol1\{|U_i-U_j|>\pi\}\). The two disjoint corner triangles of the square \([0,\alpha]^2\) have combined area \(h^2\), so \(p=\mathbb E I_{12}=h^2/\alpha^2=q^2\). Given \(U_1=u\), the conditional edge probability is
\[
g(u)=\frac{(h-u)_++(u-\pi)_+}{\alpha}.
\]
Because \(h<\pi\), its two supports are disjoint and
\[\mathbb E\,g(U_1)^2=\frac{2h^3}{3\alpha^3}=\frac23q^3.\]
Thus two distinct edge indicators sharing one vertex have covariance \(2q^3/3-q^4\); those with disjoint endpoint sets are independent. There are \(\binom n2\) single indicators and \(3\binom n3\) unordered pairs of overlapping indicators. Expand \(\operatorname{Var}\sum_{i<j}I_{ij}\) to obtain the variance formula.

**5. Sharp Poisson boundary layer.** Let \(\alpha_n=\pi(1+\lambda/n)\), so \(h_n=\alpha_n-\pi\) and \(n h_n/\alpha_n\to\lambda\). Rescale the low-end azimuths to \(s_i=nU_i/\alpha_n\) and the high-end azimuths to \(t_j=n(\alpha_n-U_j)/\alpha_n\), keeping only those in \([0,n h_n/\alpha_n]\). Counts in disjoint small subintervals are multinomial with cell probabilities equal to their lengths divided by \(n\); their joint probability generating functions converge to those of independent unit-intensity Poisson processes on \([0,\lambda]\). An escape edge satisfies \(U_j-U_i>\pi\), i.e. \(s_i+t_j<n h_n/\alpha_n\). Almost surely the limiting Poisson points have no equality \(s+t=\lambda\), so the finite bipartite escape graph with its isolated vertices removed converges in distribution to the asserted Poisson corner graph. Independently, substitution \(q_n=\lambda/(n+\lambda)\) into the exact formulas proves the displayed limits for the empty event, expectation and variance. For any fixed \(\alpha>\pi\), the empty probability decays exponentially; for \(\alpha\le\pi\), it equals one. Hence the \(1/n\) angular window is sharp.

## Verification

Run the standard-library checker using `python3 check.py`. It independently constructs great-circle interpolants in dimensions 2, 3 and 6 and verifies the azimuthal escape criterion away from a stated finite-grid boundary buffer. It compares finite-sample edge means, variances and empty-graph probabilities against deterministic-seed Monte Carlo data; checks nested neighborhoods for randomly generated configurations; and checks the explicit critical-window limits. The checker is supporting finite evidence, not a substitute for the proof above. It reports `SPHERICAL_SECTOR_GEODESIC_ESCAPE_GRAPH_CHECK_OK` on the packaged run.

## Relationship to prior work

Lassak's *Width of spherical convex bodies* (publicly online 2013-12-06) develops spherical convexity and the conventional, convex (hemispherical-intersection) notion of a lune, not random minimizing arcs in a **reflex** sector. Bárány–Hug–Reitzner–Schneider study random convex hulls inside a hemisphere. Besau–Gusakova–Reitzner–Schütt–Thäle–Werner study facet asymptotics for the **convex right-angle spherical wedge**, a different sampling region and observable. The interval-threshold random-graph model in McColm is closely related after taking a complement; the present result explicitly uses elementary range statistics and does not claim those probabilistic tools are new. What is asserted here is the exact spherical-geometric reduction, the measure- and dimension-invariant escape-chain graph, and its explicit sharp first-escape window in the native spherical setting. Searches did not identify an exact prior equivalence; this is not a proof of historical priority.

## Limitations

This concerns ambient shorter great-circle arcs, not shortest paths restricted *within* the sector. The conditional sampling law must have uniform azimuth marginal; nonuniform azimuths change the numerical probabilities. The conclusion does not extend automatically to arbitrary spherical convex/nonconvex regions, arbitrary Riemannian metrics, or non-great-circle connecting curves. The whole-sphere endpoint \(\alpha=2\pi\) is discontinuous as an escape event: a missing seam persists for every \(\alpha<2\pi\) but disappears exactly at \(2\pi\). The established interval random-geometric-graph literature may imply additional probability identities; novelty of the spherical formulation remains subject to human review. No claim of independent certification is made.

## References

- M. Lassak, *Width of spherical convex bodies*, Aequationes Math. 89 (2015), 555–567; first published online 2013-12-06. DOI: 10.1007/s00010-013-0237-3.
- I. Bárány, D. Hug, M. Reitzner and R. Schneider, *Random points in halfspheres*, arXiv:1505.04672 (2015), later Random Struct. Algorithms 50 (2017), 3–22.
- F. Besau, A. Gusakova, M. Reitzner, C. Schütt, C. Thäle and E. M. Werner, *Spherical convex hull of random points on a wedge*, Math. Ann. 389 (2024), 2289–2316, first online 2023. DOI: 10.1007/s00208-023-02704-9.
- G. L. McColm, *Threshold functions for random graphs on a line segment*, Combin. Probab. Comput. 13 (2004), 373–387. DOI: 10.1017/S0963548304006121.
