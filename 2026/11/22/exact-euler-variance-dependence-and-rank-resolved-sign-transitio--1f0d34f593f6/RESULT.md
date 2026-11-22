# Exact Euler–variance dependence and rank-resolved sign transitions for uniform interval samples

## Finding
Let \(n\ge2\) and let \(U_1,\ldots,U_n\) be independent uniform random variables on \((0,1)\). Let \(U_{(1)}<\cdots<U_{(n)}\) be their order statistics, \(D_k=U_{(k+1)}-U_{(k)}\) for \(1\le k\le n-1\), and \(S_n^2=(n-1)^{-1}\sum_i(U_i-\overline U)^2\). For \(0<t<1\), the Euler characteristic of the union of closed radius-\(t/2\) intervals about the observations equals the number of connected components,
\[
\chi_n(t/2)=1+\sum_{k=1}^{n-1}\mathbf1\{D_k>t\}.
\]
Define \(b_{n,k}=k(n-k)/[n(n-1)]\). Then, for **every** integer \(n\ge2\), internal rank \(1\le k\le n-1\), and real \(0<t<1\),
\[
\boxed{\operatorname{Cov}(\mathbf1\{D_k>t\},S_n^2)=t(1-t)^n\left[\frac{n+t}{n+1}b_{n,k}-\frac{2-t}{12}\right].}\tag{1}
\]
The bracket is strictly increasing in \(t\). At any fixed gap rank it can change sign at most once, and changes from negative to positive precisely when
\[
\frac{n}{n+1}b_{n,k}<\frac16\quad\text{and}\quad b_{n,k}>\frac1{12}.
\]
In that case its unique zero is
\[
\boxed{t^*_{n,k}=\frac{2(n+1)-12n b_{n,k}}{n+1+12b_{n,k}}\in(0,1).}\tag{2}
\]
For the first interior gap, a strict sign reversal occurs **exactly when \(6\le n\le11\)**. In particular, \(t^*_{6,1}=2/9\) and \(t^*_{11,1}=11/12\). For \(n\le4\) this rank covariance is positive throughout \((0,1)\); for \(n=5\) it is still positive for every \(t>0\) but its bracket vanishes at \(t=0\). For \(n\ge12\) it is negative throughout \((0,1)\), with a bracket zero at the excluded endpoint \(t=1\) when \(n=12\). For example, at \(n=8,t=1/2\), the first internal gap has covariance \(-1/73728\) whereas the fourth internal gap has covariance \(73/258048\).

Despite the mixed rank-specific signs, the **entire Euler characteristic curve** has strictly positive covariance with sample variance:
\[
\boxed{\operatorname{Cov}(\chi_n(t/2),S_n^2)=\frac{t(1-t)^n}{12}\,[2+(n+1)t]>0.}\tag{3}
\]
For every fixed \(c>0\), the natural sparse radius choice \(t=c/n\) yields
\[
n\operatorname{Cov}(\chi_n(c/(2n)),S_n^2)\longrightarrow\frac{c(2+c)e^{-c}}{12}.
\]
If \(k/n\to u\in(0,1)\) with \(t\) held fixed, the sign bracket in (1) tends to \(u(1-u)-(2-t)/12\), giving an explicit interior rank-sign band.

## Assumptions and scope
All observations are independent and exactly uniform on \((0,1)\). The tested null distribution is fully specified, ties occur with probability zero, the sample size is an integer \(n\ge2\), and sample variance uses divisor \(n-1\). The radius is the **unscaled Euclidean radius** \(r=t/2\) with \(0<t<1\). In implementations using sample-size-rescaled point coordinates, the corresponding radius is multiplied by the sample-size factor. The topological identity uses the one-dimensional Čech or Alpha complex and is valid at all radii except probability-zero gap equality events. End gaps to \(0\) and \(1\) are included in the Dirichlet law but do not affect the number of sample-set components.

## Proof
Set \(D_0=U_{(1)}\) and \(D_n=1-U_{(n)}\). The full spacing vector \((D_0,\ldots,D_n)\) has the symmetric Dirichlet law \(\operatorname{Dirichlet}(1,\ldots,1)\). Every internal gap greater than \(t\) separates two clusters of intersecting radius-\(t/2\) intervals, giving the Euler identity in the finding.

The unbiased sample variance satisfies the pairwise-distance identity
\[
S_n^2=\frac1{n(n-1)}\sum_{1\le a<b\le n}\left(\sum_{j=a}^{b-1}D_j\right)^2=\sum_{i,j=1}^{n-1}Q_{ij}D_iD_j,
\]
where \(Q\) is symmetric with
\[
Q_{kk}=\frac{k(n-k)}{n(n-1)}=b_{n,k},\qquad \sum_{j=1}^{n-1}Q_{kj}=\frac{k(n-k)}{2(n-1)}=\frac n2b_{n,k}.
\]
The diagonal identity counts the \(k(n-k)\) observation pairs that cross gap \(k\). For the row sum, a crossing pair \((a,b)\) contributes \((b-a)/[n(n-1)]\), and \(\sum_{a\le k<b}(b-a)=nk(n-k)/2\). Under the uniform null, \(\mathbb ES_n^2=1/12\).

The uniform-simplex translation identity states that for each \(0<t<1\),
\[
\Pr(D_k>t)=(1-t)^n,\qquad (D_j\mid D_k>t)\ \overset d=\ t\mathbf1_{\{j=k\}}+(1-t)Z_j,
\]
where the complete vector \(Z\) is again \(\operatorname{Dirichlet}(1,\ldots,1)\) on \(n+1\) coordinates. Using \(\mathbb EZ_j=1/(n+1)\) and the previous quadratic representation yields
\[
\mathbb E[S_n^2\mid D_k>t]=\frac{(1-t)^2}{12}
+\frac{t(1-t)n b_{n,k}}{n+1}+t^2b_{n,k}.
\]
Thus \(\operatorname{Cov}(\mathbf1\{D_k>t\},S_n^2)\) equals \((1-t)^n\) times the preceding conditional expectation minus \(1/12\); collecting terms proves (1).

After removing the positive prefactor \(t(1-t)^n\), the bracket has derivative \(b_{n,k}/(n+1)+1/12>0\), starts at \(n b_{n,k}/(n+1)-1/6\), and ends at \(b_{n,k}-1/12\). This proves the sign criterion and solving the linear equation gives (2), including all endpoint cases. When \(k=1\), substituting \(b_{n,1}=1/n\) gives the explicit zero \(2n(n-5)/(n^2+n+12)\). Comparing it to \(0\) and \(1\) gives the exact integer range \(6\le n\le11\).

Finally, \(\sum_{k=1}^{n-1}b_{n,k}=(n+1)/6\). Summing (1) over all internal ranks produces (3). The sparse-scale limit follows from \((1-c/n)^n\to e^{-c}\) and \(n(c/n)[2+(n+1)c/n]\to c(2+c)\). The bulk sign claim follows directly from \(b_{n,k}\to u(1-u)\).

## Verification
The self-contained Python standard-library script `check_topo_variance.py` constructs the quadratic matrix \(Q\) independently by counting squared pairwise differences. It evaluates conditional moments using **exact rational** Dirichlet second moments, independently of the simplified theorem formula, and verifies equality for every gap rank at sample sizes \(2\le n\le17\) and five rational thresholds. Additional assertions check row and diagonal sums, aggregate covariance, exact sign boundaries and two special crossings. The run completed with `PASS EXACT ASSERTIONS 1210`. These finite exact-arithmetic calculations corroborate but do not replace the all-size algebraic proof. Reproduce with `python3 check_topo_variance.py`.

## Relationship to prior work
Dłotko, Hellmer, Stettner and Topolnicki [1] introduce goodness-of-fit tests based on Euler characteristic curves and note that finite-sample ECC laws remain incompletely understood; their published one-sample test compares the curve to its null expectation. Their full-text methods and discussion do not establish the joint covariance of the Euler curve with sample variance or its rank-resolved signs.

Previously published exact uniform-spacing calculations [2] give \(\operatorname{Cov}(D_k,S_n^2)\), a **linear** gap moment, whereas (1) is the nonlinear indicator \(\mathbf1\{D_k>t\}\) for every threshold. Linear mixed moments do not determine threshold mixed moments. A published nested-component result [3] treats \(\operatorname{Cov}(\chi_n(r),\chi_n(s))\), not dispersion. The universal spacing-count/convex-additive-statistic law [4] concerns \(\sum f(D_i)\) and does not imply this result because sample variance is a quadratic form with nonzero cross-gap interactions and rank-dependent coefficients. Classical parent-distribution stochastic comparisons of spacings and dispersion [5] concern a different comparison. The Dirichlet simplex law, the pairwise variance identity, and one-dimensional Euler-component interpretation are standard; the contribution assessed here is their exact joint finite-sample relation, including the sign-classified rank resolution and positive aggregated identity.

## Limitations
The claim covers only the fully specified uniform distribution on one interval, the one-dimensional Euler/component curve, fixed finite-sample covariances, and the displayed sequentially defined sparse-scale covariance limit. Covariance is not independence and does not provide the joint null distribution, simultaneous confidence bands, new critical values, or improved test power. It does not apply automatically to other densities, circles, higher-dimensional complexes, or estimated-null parameters. Previously available general spacing-moment theory may contain equivalent expressions not located by the targeted comparisons; historical priority has not been independently established.

## References
1. P. Dłotko, N. Hellmer, Ł. Stettner, R. Topolnicki, *Topology-Driven Goodness-of-Fit Tests in Arbitrary Dimensions*, arXiv:2210.14965, first posted 2022-10-25, https://arxiv.org/abs/2210.14965; *Statistics and Computing* 34, article 34 (2024), doi:10.1007/s11222-023-10333-0.
2. *Exact uniform-spacing/sample-variance covariance and its Pell-zero ranks*, published mathematical record (2026-10-25), https://github.com/published-finding corpus/2026.
3. *One sign reversal across scales for component counts in a one-dimensional random geometric graph*, published mathematical record (2026-11-02), https://github.com/published-finding corpus/2026.
4. *A universal one-switch covariance law for large spacings and convex spacing tests*, published mathematical record (2026-11-02), https://github.com/published-finding corpus/2026.
5. S. C. Kochar, *On stochastic orderings between distributions and their sample spacings*, *Statistics & Probability Letters* 42 (1999), 345–352, doi:10.1016/S0167-7152(98)00224-7.
