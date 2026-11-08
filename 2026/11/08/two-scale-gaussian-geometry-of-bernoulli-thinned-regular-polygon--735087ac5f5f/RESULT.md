# Two-scale Gaussian geometry of Bernoulli-thinned regular polygons

## Finding

Fix a retention parameter \(p\in(0,1)\). For every integer \(N\ge3\), independently retain each vertex of the radius-one regular \(N\)-gon with probability \(p\), and take the convex hull \(K_N\). Let \(L_N\) and \(A_N\) be its Euclidean perimeter and area, both set to zero when fewer than two vertices remain. Define the circle deficits
\[
X_N=2\pi-L_N,\qquad Y_N=\pi-A_N.
\]
Let \(G\) be a positive geometric random variable, \(\Pr(G=k)=p(1-p)^{k-1}\) for \(k=1,2,\ldots\). For \(r\in\{3,5\}\), put
\[
\rho_r=p\,\mathbb E G^r,\qquad
\sigma_{rs}=p\,\mathbb E\big[(G^r-\rho_rG)(G^s-\rho_sG)\big],
\quad r,s\in\{3,5\}.
\]
Write \(c_3=\pi^3/3\) and \(c_5=\pi^5/10\). Then the anisotropically scaled joint deficit has a **nondegenerate** Gaussian limit:
\[
\boxed{\begin{pmatrix}
N^{5/2}\big(X_N-c_3\rho_3/N^2\big)\\
N^{9/2}\big(Y_N-2X_N+c_5\rho_5/N^4\big)
\end{pmatrix}
\Longrightarrow
\mathcal N_2\!\left(0,
\begin{pmatrix}
 c_3^2\sigma_{33}&-c_3c_5\sigma_{35}\\
 -c_3c_5\sigma_{35}&c_5^2\sigma_{55}
\end{pmatrix}\right).}
\]
The covariance matrix is positive definite for every fixed \(0<p<1\). Moreover the **unscaled geometric covariance** satisfies
\[
\boxed{\lim_{N\to\infty}N^{14}
\det\operatorname{Cov}(X_N,Y_N)=
 c_3^2c_5^2(\sigma_{33}\sigma_{55}-\sigma_{35}^2)>0.}
\]
In particular, the leading area and perimeter fluctuations are perfectly correlated, but the first nonvanishing transverse fluctuation survives four further powers in the covariance determinant. Quantitatively,
\[
\boxed{\lim_{N\to\infty}N^4
\big(1-\operatorname{Corr}(X_N,Y_N)\big)=
\frac{c_5^2(\sigma_{33}\sigma_{55}-\sigma_{35}^2)}
{8c_3^2\sigma_{33}^{2}}>0.}
\]
The first-order deterministic deficits satisfy \(N^2X_N\to c_3\rho_3\) and \(N^2Y_N\to2c_3\rho_3\) in probability.

For example, at \(p=1/2\), the coefficients are exactly
\[
\rho_3=13,\qquad\rho_5=541,\qquad
(\sigma_{33},\sigma_{35},\sigma_{55})=(3240,465480,98058600),
\]
and \(\sigma_{33}\sigma_{55}-\sigma_{35}^2=101038233600\).

## Assumptions and scope

The ambient space is the ordinary Euclidean plane, with circular radius exactly one. The deletion indicators are independent with the same fixed probability \(p\in(0,1)\), while the original vertex count \(N\) tends to infinity. The random polygon can be empty or degenerate; our conventions make its perimeter and area zero in that event. The exceptional event of at most one retained vertex has probability exponentially small in \(N\), and does not affect any limit stated above. The covariance is taken over all deletion patterns, without conditioning on a fixed retained count. For two retained vertices, the perimeter is twice their Euclidean distance and the area is zero. All random quantities are bounded for fixed \(N\).

## Proof

**1. Exact cyclic-gap geometry.** Condition temporarily on at least one selected vertex. List selected vertex indices in increasing cyclic order and let \(g_1,\ldots,g_M\) be their positive integer gaps, including the final wrap-around. Thus \(\sum_jg_j=N\). The chord lengths and oriented shoelace formula give, exactly, including the one- and two-vertex cases,
\[
L_N=2\sum_{j=1}^{M}\sin(\pi g_j/N),\qquad
A_N=\frac12\sum_{j=1}^{M}\sin(2\pi g_j/N).
\]
For \(r\ge1\) put \(R_r(N)=\sum_jg_j^r\). Taylor's theorem, using \(|\sin x-(x-x^3/6+x^5/120)|\le |x|^7/7!\) for real \(x\), yields the deterministic expansions
\[
\begin{aligned}
X_N&=\frac{\pi^3}{3N^3}R_3(N)-\frac{\pi^5}{60N^5}R_5(N)
+O\big(N^{-7}R_7(N)\big),\\
Y_N&=\frac{2\pi^3}{3N^3}R_3(N)-\frac{2\pi^5}{15N^5}R_5(N)
+O\big(N^{-7}R_7(N)\big).
\end{aligned}
\]
Subtraction eliminates the cubic term **exactly** and leaves
\[
Y_N-2X_N=-\frac{\pi^5}{10N^5}R_5(N)
+O\big(N^{-7}R_7(N)\big).
\]
The inequalities underlying the \(O\)-terms hold for every possible gap, not merely for small angles.

**2. Cyclic gaps versus ordinary geometric renewals.** Put independent Bernoulli variables on the nonnegative integer sites and introduce an artificial retained vertex at the origin. The gaps between successive successes are i.i.d. copies of \(G\). Up to level \(N\), the corresponding renewal reward sum is \(\sum_{j\le M_N}G_j^r\), where \(M_N=\max\{k:G_1+\cdots+G_k\le N\}\). Under the natural coupling with the periodic sample on the \(N\)-gon, the only changed rewards arise from the gap crossing the cut and at most its two artificially split pieces. The distances from the cut to the nearest successes on either side have geometric tails uniformly in \(N\). Consequently, for each fixed positive integer \(r\), the difference between the cyclic reward and the renewal reward is bounded in every fixed \(L^q\) norm as \(N\to\infty\) (on the exponentially likely nonempty event). The empty event can be handled separately by its exponentially small probability.

For \(r\in\{3,5\}\), define the centered cycle reward \(W_r(G)=G^r-\rho_rG\). Since \(\mathbb E G=1/p\), we have \(\mathbb EW_r=0\). The strong law gives \(M_N/N\to p\). The multivariate i.i.d. central limit theorem and the random-time-change theorem for renewal rewards therefore yield
\[
\frac1{\sqrt N}
\begin{pmatrix}
R_3(N)-\rho_3N\\
R_5(N)-\rho_5N
\end{pmatrix}
\Longrightarrow\mathcal N_2\!\left(0,
\begin{pmatrix}\sigma_{33}&\sigma_{35}\\\sigma_{35}&\sigma_{55}\end{pmatrix}\right).
\]
The overshoot contributes only a bounded-in-moment correction. The same convergence holds in second moments: all geometric cycle rewards have finite moments of every order, while stopped centered sums have fourth moments \(O(N^2)\) by the martingale fourth-moment inequality applied at the first renewal past \(N\). The final overshoot and boundary corrections have at worst logarithmically growing fixed moments, which are negligible after division by \(\sqrt N\). Thus the squared normalized rewards are uniformly integrable. This also establishes the precise covariance limits used below.

**3. Remainders and the two scales.** The largest gap in the Bernoulli ring is \(O_{L^q}(\log N)\) for each fixed \(q\), by a union bound over possible runs of absent vertices. Since \(\sum_j g_j=N\),
\[
R_r(N)\le N\,\big(\max_jg_j\big)^{r-1}
=O_{L^q}\big(N(\log N)^{r-1}\big).
\]
Hence the fifth-order term in \(X_N\) vanishes after multiplying by \(N^{5/2}\), and the seventh-order remainder in \(Y_N-2X_N\) vanishes after multiplication by \(N^{9/2}\), both in \(L^2\). Inserting the renewal-reward central limit theorem into the expansions in Step 1 proves the displayed joint Gaussian law and convergence of its covariance matrix.

**4. Positive definiteness and sharp covariance determinant.** If the renewal-reward covariance matrix were singular, there would exist nonzero constants \(a,b\) such that
\[
a(G^3-\rho_3G)+b(G^5-\rho_5G)=0
\quad\text{almost surely}.
\]
Because the geometric law assigns positive probability to every positive integer, the degree-five polynomial on the left would vanish at infinitely many integers. Thus \(a=b=0\), a contradiction. So \(\det\Sigma>0\).

The exact linear identity \(Y_N=2X_N+(Y_N-2X_N)\) implies
\[
\det\operatorname{Cov}(X_N,Y_N)=
\det\operatorname{Cov}\big(X_N,Y_N-2X_N\big).
\]
The \(L^2\) covariance convergence from Steps 2–3 and the different scaling exponents imply the stated limit after multiplication by \(N^{14}\). Also \(\operatorname{Var}(X_N)\sim c_3^2\sigma_{33}N^{-5}\), \(\operatorname{Var}(Y_N)\sim4c_3^2\sigma_{33}N^{-5}\), and \(\operatorname{Corr}(X_N,Y_N)\to1\). The identity \(1-\operatorname{Corr}^2=\det\operatorname{Cov}/(\operatorname{Var}X_N\operatorname{Var}Y_N)\) gives the sharp \(N^{-4}\) correlation correction.

**5. Closed constants.** Ordinary geometric moments are rational functions of \(p\). Explicitly,
\[
\mathbb E G^3=\frac{p^2-6p+6}{p^3},\qquad
\mathbb E G^5=\frac{p^4-30p^3+150p^2-240p+120}{p^5}.
\]
All entries of \(\Sigma\) follow from geometric moments through degree ten. Alternatively, the falling-factorial identity
\[
\mathbb E(G)_{j}=j!(1-p)^{j-1}/p^j\qquad(j\ge1)
\]
and Stirling-number conversion provide an exact rational recipe. At \(p=1/2\), this gives the displayed integer constants and strictly positive determinant.

## Verification

The accompanying self-contained standard-library Python program `verify_polygon.py` implements an independent Cartesian shoelace/perimeter computation and the cyclic-gap formulas. It exhaustively checks all nonempty subsets for the regular polygons with \(3\le N\le9\), checks the gap-power cancellation on random samples for larger \(N\) against a deterministic Taylor bound, and independently calculates all renewal moments as exact rational numbers. Its reproducible Monte Carlo consistency test compares the finite-sample reward covariance with the predicted limit at \(p=1/2\). Run `python verify_polygon.py`; the completion marker is `BERNOULLI_POLYGON_TWO_SCALE_CHECKS_PASSED`. These finite computations test the exact geometry and constants; the CLT, arbitrary-parameter positivity and asymptotic covariance determinant rely on the analytic proof above.

## Relationship to prior work

Turchi and Wespi (2017) establish marginal intrinsic-volume central limit theorems for an independent sample from the **continuous boundary of a fixed smooth convex body**. Their setting does not provide the discrete Bernoulli vertex-retention model, the coupled cubic/quintic gap rewards, or the rank-recovering two-scale normalization of area and perimeter.

Madras and KC (2006) derive expected area and perimeter formulas for triangles formed by three uniformly chosen regular-polygon vertices. Those three-vertex expectation identities are acknowledged, not claimed as new. They do not give the joint fluctuation law as the retained count grows proportionally to the original vertex count, nor the covariance determinant and correlation asymptotics. Standard multivariate renewal-reward central limit theory supplies one analytical ingredient, but requires the geometric cancellation and both sharp normalizations to obtain this statement.

Wang, Li and Xu (2023) develop **fifth-gap extrapolation** and central limit laws for *Dirichlet-distributed circular spacings*. Thus cancellation of the cubic term and Gaussian fluctuations of fifth-order spacing rewards are preexisting ideas in a different random polygon model and are not independently claimed as novel. The present claim is instead the independent-vertex Bernoulli lattice model, with its random retained count, geometric renewal covariance, and exact anisotropic covariance determinant and correlation rates. The Dirichlet results assume a fixed number of normalized gamma spacings and do not contain or imply the Bernoulli-renewal coefficient matrix.

The published records for boundary-sampled random polygons in the Hausdorff metric, and for simultaneous area/perimeter density optimization in ellipses, study different randomization mechanisms and different functionals. They do not imply the two-scale Bernoulli polygon theorem. The novelty assessment remains provisional with respect to unindexed work on cyclic Bernoulli spacings and random polygon reliability.

## Limitations

The theorem is an asymptotic result for fixed \(p\in(0,1)\), not a finite-\(N\) distribution formula or a uniform limit as \(p\to0\) or \(p\to1\). It assumes independent, identically distributed deletions on a circular lattice and radius-one regular geometry. The covariance limit does not give a quantitative normal-approximation rate. The self-review cannot establish complete historical priority and does not replace independent mathematical review.

## References

1. N. Turchi and F. Wespi, *Limit theorems for random polytopes with vertices on convex surfaces*, arXiv:1706.02944, first public 9 June 2017. https://arxiv.org/abs/1706.02944
2. A. Madras and S. KC, *Randomly Generated Triangles whose Vertices are Vertices of a Regular Polygon* (2006), Sections 4–5, full-text rendering https://scholar.rose-hulman.edu/rhumj/vol7/iss2/12/
3. J. Prochno, C. Schütt, M. Sonnleitner and E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870, first public 3 April 2024. https://arxiv.org/abs/2404.02870
4. K. J. Böröczky, F. Fodor and D. Hug, *Intrinsic volumes of random polytopes with vertices on the boundary of a convex body*, arXiv:1103.4978, first public 2011. https://arxiv.org/abs/1103.4978
5. Classical renewal-reward central limit theorem and random-time-change theorem, used as standard probability tools; the geometric formulas and the two-scale conclusion are derived here.

6. S. Wang, Z. Li and W.-Q. Xu, *Nonlinear random extrapolation estimates of pi under Dirichlet distributions*, Journal of Numerical Analysis and Approximation Theory, published 22 December 2023. https://ictp.acad.ro/jnaat/journal/article/view/1360/1463
