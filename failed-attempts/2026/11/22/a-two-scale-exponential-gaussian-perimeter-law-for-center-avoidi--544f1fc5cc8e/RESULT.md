# A two-scale exponential–Gaussian perimeter law for center-avoiding random cyclic polygons

## Finding
For each integer \(n\ge3\), independently sample \(n\) points uniformly on the Euclidean unit circle, and let \(K_n\) be their convex hull. Condition on the *center-avoidance event* \(E_n=\{0\notin K_n\}\), whose probability is \(n/2^{n-1}\). Let \(P_n\) be its perimeter and \(A_n\) its area. On \(E_n\), exactly one circular angular gap exceeds \(\pi\); write its size as \(\pi+\delta_n\), and put \(L_n=\pi-\delta_n\). Define the **inner-arc polygonization deficit**
\[
 D_n=L_n+2\cos(\delta_n/2)-P_n\ge0.
\]
This is precisely the length of the occupied circular arc minus the sum of the chords joining its successive observed vertices; it excludes the single closing chord.

Let \(E\sim\operatorname{Exp}(1)\) and \(Z\sim\mathcal N(0,5\pi^6/8)\) be independent. Then, under the conditional law given \(E_n\),
\[
\boxed{\left(n\delta_n,\ n[(\pi+2)-P_n],\ n[\pi/2-A_n],\ n^2\left\{(\pi/2-A_n)-[(\pi+2)-P_n]\right\},\ n^{5/2}\left[D_n-\frac{L_n^3}{4n(n+1)}\right]\right)
\ \xrightarrow{\mathrm d}\left(\pi E,\pi E,\pi E,\frac{\pi^3-\pi^2 E^2}{4},Z\right).}
\]
In particular, the first-order area and perimeter deficits share the same exponentially distributed random gap. Their second-order difference has a non-Gaussian law involving \(E^2\). After *exact conditional-mean centering*, the remaining arc polygonization error has an independent nondegenerate Gaussian law at the sharper scale \(n^{-5/2}\).

## Assumptions and scope
All angles are in radians. Circle points are independent, arclength-uniform and almost surely distinct. The Euclidean polygon is the convex hull of the complete sample and its boundary connects circularly consecutive vertices. The conditional limit is for \(n\to\infty\), not a limit holding under the unconditioned measure. Endpoints of all events have probability zero. The subtraction \(L_n^3/[4n(n+1)]\) is the exact conditional expectation of \(D_n\)'s leading cubic approximation, **not** the exact conditional expectation of \(D_n\) itself; the difference between those means is negligible at scale \(n^{-5/2}\). The Gaussian variable \(Z\) is independent of the limiting exponential \(E\), not asserted independent of finite-sample \(\delta_n\) without conditioning.

## Proof
**1. Exact conditioning.** For a uniform circular sample the \(n\) cyclic angular spacings divided by \(2\pi\) have the symmetric \(\operatorname{Dirichlet}(1,\ldots,1)\) law. Center avoidance is equivalent to a spacing greater than \(\pi\); such a spacing is almost surely unique. A specified spacing exceeds \(\pi\) with probability \(2^{1-n}\), so the union of these disjoint events has probability \(n2^{1-n}\), in agreement with Wendel's theorem. On this event the occupied arc is shorter than a semicircle. Elementary conditioning of the constant Dirichlet density on a component exceeding one-half gives the independent representation
\[
\frac{\delta_n}{\pi}=T_n\sim\operatorname{Beta}(1,n-1),\qquad
(G_{n,1},\ldots,G_{n,n-1})=L_n(V_1,\ldots,V_{n-1}),
\]
where \((V_1,\ldots,V_{n-1})\sim\operatorname{Dirichlet}(1,\ldots,1)\) and is independent of \(T_n\). Specifically, for \(0\le t\le1\),
\[
 \Pr(T_n>t\mid E_n)=(1-t)^{n-1},
\]
whence \(n\delta_n\Rightarrow\pi E\), while \(L_n\to\pi\) in conditional probability.

**2. Exact geometry.** The long-gap closing chord has length \(2\sin[(\pi+\delta_n)/2]=2\cos(\delta_n/2)\). The shoelace area formula gives the exact identities
\[
 P_n=2\cos(\delta_n/2)+2\sum_{j=1}^{n-1}\sin(G_{n,j}/2),\quad
 A_n=\frac12\left(-\sin\delta_n+\sum_{j=1}^{n-1}\sin G_{n,j}\right),
\]
\[
 D_n=\sum_{j=1}^{n-1}\big(G_{n,j}-2\sin(G_{n,j}/2)\big).
\]
Set \(\Delta P_n=(\pi+2)-P_n\) and \(\Delta A_n=\pi/2-A_n\). Since \(\sum_jG_{n,j}=L_n\),
\[
 \Delta P_n=\delta_n+2(1-\cos(\delta_n/2))+D_n,
\qquad
 \Delta A_n=\frac{\delta_n+\sin\delta_n}{2}+\frac12\sum_j(G_{n,j}-\sin G_{n,j}).
\]

**3. Exact moments and multiscale remainders.** Put \(m=n-1\) and \(Q_m=\sum_{j=1}^m V_j^3\). Symmetric Dirichlet moments yield, for \(m\ge2\),
\[
\mathbb E Q_m=\frac6{(m+1)(m+2)},\qquad
\operatorname{Var}Q_m=\frac{72(m-1)(5m+11)}{(m+1)^2(m+2)^2(m+3)(m+4)(m+5)}.
\]
Taylor's inequalities, applied to \(0\le G_{n,j}\le\pi\), imply
\[
 D_n=\frac{L_n^3}{24}Q_m+O\!\left(\sum_jG_{n,j}^5\right),\qquad
\frac12\sum_j(G_{n,j}-\sin G_{n,j})=\frac{L_n^3}{12}Q_m+O\!\left(\sum_jG_{n,j}^5\right).
\]
The deterministic absolute-error constants are universal. Conditional on \(\delta_n\), Dirichlet moment integration gives
\[
\mathbb E\left[\sum_j G_{n,j}^5\mid\delta_n,E_n\right]
=L_n^5\frac{120}{(m+1)(m+2)(m+3)(m+4)}=O(n^{-4}),
\]
uniformly over the possible \(\delta_n\). Thus the Taylor errors are \(o_{L^1}(n^{-5/2})\), in particular negligible for both the quadratic and Gaussian normalizations. Also \(Q_m=O_{\Pr}(n^{-2})\) and \(\delta_n=O_{\Pr}(n^{-1})\) under the conditional law. Substitution in Step 2 therefore yields the first three coordinates and
\[
 n^2(\Delta A_n-\Delta P_n)
=\frac{n^2L_n^3}{24}Q_m-\frac{n^2\delta_n^2}{4}+o_{\Pr}(1)
\Rightarrow\frac{\pi^3-\pi^2E^2}{4},
\]
since \(n^2 Q_m\to6\) in probability by the displayed moments.

**4. Independent Gaussian fluctuation.** Let \(W_j\) be iid unit exponentials. The distributional representation \(V_j=W_j/\sum_{i=1}^mW_i\) gives
\[
 m^2 Q_m=\frac{m^{-1}\sum_{j=1}^mW_j^3}{(m^{-1}\sum_{j=1}^mW_j)^3}.
\]
The bivariate ordinary central limit theorem and delta method at the mean vector \((6,1)\) yield
\[
 m^{5/2}\big(Q_m-\mathbb EQ_m\big)\Rightarrow\mathcal N(0,360),
\]
with influence function \(W^3-18W+12\), whose variance equals \(360\). (The exact expression for \(\mathbb EQ_m\) differs from \(6m^{-2}\) by only \(O(m^{-3})\).) Since \(L_n\to\pi\), the Taylor control from Step 3 and \(\mathbb EQ_m=6/[n(n+1)]\) give
\[
 n^{5/2}\left[D_n-\frac{L_n^3}{4n(n+1)}\right]
=\frac{L_n^3}{24}n^{5/2}(Q_m-\mathbb EQ_m)+o_{\Pr}(1)
\Rightarrow\mathcal N\left(0,\frac{360\pi^6}{24^2}\right)
=\mathcal N(0,5\pi^6/8).
\]
For each finite \(n\), the normalized Dirichlet vector \(V\) is independent of \(T_n\). Their independent joint convergence, followed by Slutsky's theorem with \(L_n\to\pi\), makes this Gaussian coordinate asymptotically independent of \(E\). Every coordinate has now been established jointly, proving the asserted vector convergence.

## Verification
Run `python3 verify.py` with standard-library Python 3 from this directory. It checks 248 exact-rational symmetric Dirichlet moment identities, 188 exact beta-moment identities, and 2000 independent geometric evaluations of the perimeter/area identities. It also samples the conditional distribution at two growing polygon orders, comparing approximate Gaussian fluctuation variances against \(5\pi^6/8\). These finite checks are corroborative only; the infinite-dimensional limit and all constants follow from the analytical argument above.

## Relationship to prior work
Wendel (1962) proves the exact center-exclusion probability; it supplies no conditional polygonization law. Bélisle (2011) and Xu–Meng–Li (2019) study area and perimeter of *unconditioned* uniformly sampled cyclic polygons. Koroleva–Nikitin (arXiv:1301.1360, first posted 2013-01-07) study the extremal perimeter/area among *subsets* of vertices, not the whole hull conditioned on missing the center. The previously described center-clearance limit for center-avoiding random polygons concerns distance from the center to the hull and does not give the rare-event perimeter, area, or independent fine Gaussian fluctuation. Likewise, a semicircular hull conditioned on an acute angle has a different rare event and limiting geometry. None of these individually implies the five-coordinate conditional law. The conditional Dirichlet reduction is standard; the contribution is the joint centered multiscale law and the precise independent fluctuation.

## Limitations
The theorem assumes exactly uniform points on a round unit circle. It does not cover arbitrary symmetric convex curves, biased angular sampling, joint convergence of the *whole perimeter process*, or moderate deviations. The older Bélisle full text was unavailable for examination, leaving a residual historical-priority risk; a missed equivalent theorem cannot be excluded by database searches. The Gaussian term is centered on the leading cubic conditional mean, not the exact expected nonlinear chord deficit, whose difference is negligible at the claimed scale. Independent verification of historical priority has not been performed.

## References
- James G. Wendel, “A Problem in Geometric Probability,” *Mathematica Scandinavica* **11** (1962), 109–111, https://doi.org/10.7146/math.scand.a-10655 (public year verified, exact first public day not established).
- Claude Bélisle, “On the polygon generated by n random points on a circle,” *Statistics & Probability Letters* **81** (2011), 236–242, https://doi.org/10.1016/j.spl.2010.11.012 (full text not inspected).
- E. V. Koroleva and Ya. Yu. Nikitin, “U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons,” arXiv:1301.1360, first publicly posted 2013-01-07, https://arxiv.org/abs/1301.1360.
- W.-Q. Xu, T. Meng and X. Li, “Random Polygons and Estimations of π,” *Mathematics* (2019), https://doi.org/10.1515/math-2019-0049.
