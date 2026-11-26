# A cubic-root peak in conditional leaf counts of uniform Cayley trees

## Finding

Let \(T_n\) be uniformly distributed among the \(n^{n-2}\) labeled trees on \(\{1,\ldots,n\}\), with \(n\ge3\). Fix distinct labels \(u,v\), let \(D_n=d_{T_n}(u,v)\), and let \(L_n\) be the total number of vertices of degree one (global leaf count). Define \(a_n=(n-1)/n\). For every integer \(1\le k\le n-1\), the **exact conditional leaf profile** is
\[
\boxed{\mu_{n,k}:=\mathbb E[L_n\mid D_n=k]
=\left(n-k-1+\frac{2k}{k+1}\right)a_n^{n-k-2}.}
\tag{1}
\]
The exponent \(-1\) at \(k=n-1\) is intentional, and the expression then equals \(2\).

For every \(1\le k\le n-2\), its finite difference is
\[
\boxed{\mu_{n,k+1}-\mu_{n,k}=
 a_n^{n-k-3}\frac{2n-(k+2)(k^2+1)}{n(k+1)(k+2)}.}
\tag{2}
\]
Consequently the conditional leaf profile increases strictly and then decreases strictly, except possibly for one equality of two neighboring values. The exact equality occurs only when \(2n=(k+2)(k^2+1)\). More precisely, let \(\kappa_n\) be the unique positive real solution of
\[
(\kappa_n+2)(\kappa_n^2+1)=2n.
\]
If \(\kappa_n\) is not an integer, \(\mu_{n,k}\) has its unique maximum at \(k=\lceil\kappa_n\rceil\). If it is an integer, its two and only two maxima occur at \(k=\kappa_n\) and \(k=\kappa_n+1\). The maximizing length thus satisfies
\[
\boxed{k_{\mathrm{max}}=(2n)^{1/3}+O(1),\qquad
\kappa_n=(2n)^{1/3}-\frac23+O(n^{-1/3}).}
\tag{3}
\]
For \(n=3\), both possible distances maximize the constant profile.

Even though the conditional regression initially **increases**, the **unconditional** covariance has the opposite sign:
\[
\boxed{\operatorname{Cov}(L_n,D_n)<0\quad(n\ge4),\qquad
\operatorname{Cov}(L_3,D_3)=0.}
\tag{4}
\]
It has the precise leading-order asymptotic
\[
\boxed{\operatorname{Cov}(L_n,D_n)
\sim-\frac{\sqrt{\pi/2}}{2e}\sqrt n.}
\tag{5}
\]
Equivalently, the correlation decays according to
\[
\boxed{\operatorname{Corr}(L_n,D_n)
\sim-\frac{\sqrt\pi}{2e\sqrt{(e^{-1}-2e^{-2})(4-\pi)}}\,n^{-1/2}.}
\tag{6}
\]
The typical marked-vertex distance has order \(n^{1/2}\), whereas the *conditional* leaf-count maximum occurs at distance of order \(n^{1/3}\).

## Assumptions and scope

Trees are undirected, simple, uniformly sampled and labeled; both marked vertices are distinct fixed labels. The leaves counted by \(L_n\) include the two marked vertices whenever they have degree one, together with all other vertices of degree one. At \(n=3\), every tree has exactly two leaves. The distance law is supported on all integers \(1,\ldots,n-1\). The claim concerns conditional **expectations**, a strict finite-sample covariance sign, and asymptotic covariance/correlation; no stochastic ordering of the entire conditional global-leaf-count distribution is asserted.

## Proof

**1. Classical forest extension.** For any prescribed forest on the \(n\) labels with \(c\) components of sizes \(s_1,\ldots,s_c\), the number of complete labeled trees containing that forest is
\[
n^{c-2}\prod_{j=1}^c s_j.
\tag{7}
\]
This is the classical Cayley–Moon forest-extension formula discussed by Pitman [1]. Fix \(k\), and condition on a particular ordered path \(P\) of length \(k\) from \(u\) to \(v\), with \(k-1\) distinct internal labels. It contains \(r=k+1\) vertices. Applying (7) with the path as one component and each outside vertex isolated gives
\[
\#\{T_n\supset P\}=r n^{n-r-1}.
\tag{8}
\]
Any completion contains that path as its unique \(u\)-to-\(v\) path, so conditioning on the path is legitimate.

For a specified vertex \(w\notin P\), requiring \(w\) to be a leaf amounts to deleting it and choosing its unique neighbor among the remaining \(n-1\) labels. By (7) on \(n-1\) vertices, the number of completions is
\[
(n-1)\,r(n-1)^{n-r-2}=r(n-1)^{n-r-1}.
\]
Dividing by (8) yields
\[
\Pr(w\text{ is a leaf}\mid P)=a_n^{n-r-1}.
\tag{9}
\]
For either path endpoint \(u\) or \(v\), being a leaf requires no other incident edge. Deleting the endpoint leaves a prescribed path of \(r-1\) vertices and exactly
\[
(r-1)(n-1)^{n-r-1}
\]
completions. Hence
\[
\Pr(u\text{ is a leaf}\mid P)=
\Pr(v\text{ is a leaf}\mid P)
=\frac{r-1}{r}a_n^{n-r-1}.
\tag{10}
\]
Every interior path vertex has degree at least two. Summing (9) over the \(n-r\) outside labels and (10) over two endpoints gives
\[
\mathbb E[L_n\mid P]=\left(n-r+\frac{2(r-1)}r\right)a_n^{n-r-1}.
\]
This depends only on \(k=r-1\), not on the path labels. Averaging over the possible paths conditional on \(D_n=k\) proves (1). The counting also covers \(r=n\): in that case a full path has two leaves, and (1) simplifies to \(2\).

**2. Exact shape and maximizing length.** Subtracting consecutive instances of (1), using \(a_n=(n-1)/n\), proves (2). Because \((k+2)(k^2+1)\) is strictly increasing for \(k\ge1\), its comparison with \(2n\) changes sign at most once. For \(n\ge4\), (2) is positive at \(k=1\) and negative near the upper boundary; thus there is a unique maximum or exactly one plateau of length two. Its location is determined by \(\kappa_n\) as stated. Since \((x+2)(x^2+1)=x^3+2x^2+x+2\), polynomial inversion gives \(\kappa_n=(2n)^{1/3}-2/3+O(n^{-1/3})\), proving (3).

**3. Strict negative finite covariance.** Prüfer coding gives
\[
\mathbb E L_n=n(1-1/n)^{n-2}.
\tag{11}
\]
The profile (1) has \(\mu_{n,1}=(n-1)a_n^{n-3}=\mathbb EL_n\). For \(n\ge4\), the first difference in (2) is positive, while \(\mu_{n,n-1}=2<\mathbb EL_n\) (the latter inequality is strict because some labeled trees have more than two leaves). Because the conditional profile has just one increasing phase followed by one decreasing phase, its centered values \(b_k=\mu_{n,k}-\mathbb EL_n\) change sign **once**, from positive to negative, as \(k\) increases beyond 1. Choose a real \(c\) at that crossing; then \((k-c)b_k\le0\) for all \(k\), with strict inequality for some \(k\) of positive probability. Since \(\mathbb E b_{D_n}=0\),
\[
\operatorname{Cov}(L_n,D_n)
=\mathbb E[(D_n-c)b_{D_n}]<0.
\]
At \(n=3\) the leaf count is identically two. This proves (4).

**4. Precise asymptotic covariance.** Counting paths with \(k-1\) ordered intermediate labels by (8) gives
\[
\Pr(D_n=k)=\frac{(k+1)(n-2)_{k-1}}{n^k},
\qquad 1\le k\le n-1,
\tag{12}
\]
where \((x)_j=x(x-1)\cdots(x-j+1)\). Directly from (12), \(D_n/\sqrt n\) converges to a Rayleigh variable \(R\) of density \(x e^{-x^2/2}\) on positive \(x\). Indeed, the product representation
\[
\Pr(D_n=k)=\frac{k+1}{n}\prod_{j=2}^{k}\left(1-\frac jn\right)
\]
converges on the \(\sqrt n\) scale and is bounded by a Gaussian tail. This bound also gives convergence of each fixed nonnegative integer moment of \(D_n/\sqrt n\).

For \(k\le n^{3/5}\), expanding (1) uniformly gives
\[
\mu_{n,k}=\frac ne+\frac1e\left(\frac52-\frac{k^2}{2n}\right)
+O\!\left(\frac{1}{k+1}+\frac{k}{n}+\frac{k^3}{n^2}+\frac1n\right).
\tag{13}
\]
The remainder converges to zero in \(L^2\) under the distance law (12), because \(D_n\to\infty\) in probability, while \(D_n/\sqrt n\) has uniformly bounded moments. The contribution of \(D_n>n^{3/5}\) is negligible since the Gaussian product tail in (12) is \(\exp[-\Omega(n^{1/5})]\) and \(0\le\mu_{n,k}\le n\). Therefore
\[
\left(\frac{D_n}{\sqrt n},\ \mu_{n,D_n}-\frac ne\right)
\longrightarrow
\left(R,\ \frac1e\left(\frac52-\frac{R^2}2\right)\right)
\]
in the moment sense needed for covariance. Because
\[
\mathbb ER=\sqrt{\pi/2},\quad \mathbb ER^2=2,\quad
\mathbb ER^3=3\sqrt{\pi/2},
\]
we have \(\operatorname{Cov}(R,R^2)=\sqrt{\pi/2}\). The tower property yields
\[
\frac{\operatorname{Cov}(L_n,D_n)}{\sqrt n}
=\operatorname{Cov}\!\left(\mu_{n,D_n}-\frac ne,\frac{D_n}{\sqrt n}\right)
\longrightarrow -\frac{\sqrt{\pi/2}}{2e},
\]
proving (5).

Finally, Prüfer coding yields the exact leaf-count variance
\[
\operatorname{Var}(L_n)=n a_n^{n-2}(1-a_n^{n-2})
+n(n-1)\left[(1-2/n)^{n-2}-a_n^{2(n-2)}\right]
\sim (e^{-1}-2e^{-2})n,
\]
and (12) yields \(\operatorname{Var}(D_n)\sim(4-\pi)n/2\). Dividing the covariance asymptotic by these standard deviations proves (6).

## Verification

Run \(\texttt{python3 tree_leaf_distance_verify.py}\) with a standard Python 3 installation; no third-party packages are needed. The standalone checker enumerates all \(280{,}391\) Prüfer codes for \(n=3,\ldots,8\), verifies the exact distance distribution and conditional leaf means using rational arithmetic, checks \(15{,}931\) rational consecutive differences for \(3\le n\le180\), checks the exact global covariance sign for \(n=3,\ldots,100\), identifies all equality cases in that interval, and compares finite-size covariance ratios for \(n=100,1000,10000\) to the derived asymptotic constant. It reports all checks passed. These are finite tests; the proof above establishes the all-\(n\) results.

## Relationship to prior work

The forest extension formula (7) belongs to classical labeled-tree enumeration; Pitman's 1996 report [1] supplies a primary exposition of this counting method. The distance distribution (12), Prüfer marginal leaf law (11), and Rayleigh distance scaling are classical ingredients, not claimed as discoveries.

A published exact endpoint-degree/distance regression result [2] proves that the **degree of one marked vertex** decreases stochastically with distance to the other marked vertex, and gives its conditional law. It does not determine the expected **number of leaves across all vertices** conditioned on that distance. The latter exhibits the opposite *initial* response, a cubic-root maximizer, and a strict negative global covariance. The implication is not obtained by simply substituting one statistic for the other; the leaves outside the marked path must be counted separately.

Aldous' random-tree work [3] develops leaf, degree and distance marginals; Aldous–Pitman [4] examines random-tree structures and limiting laws. Their inspected statements do not establish (1)–(6). See the limitations for residual originality risk.

## Limitations

The model is the uniform **labeled** tree; weighted trees or alternative branching processes need not satisfy (1) or the same shape classification. The proof establishes the mean profile, not stochastic ordering of the full conditional leaf-count distributions. The asymptotic statements require \(n\to\infty\), and finite code checks cannot certify the limits. Older tree-enumeration literature could implicitly encode an equivalent multivariate generating function, even though the materially inspected sources and targeted comparisons did not exhibit the precise cubic-root transition; this is the principal residual originality risk. The open-access text of the Aldous 1990 paper [3] was inspected for the leaf-probability and diameter sections, which address distinct marginal properties. Older general multivariate tree-enumeration works remain a possible source of implicit overlap.

## References

1. J. Pitman, “Coalescent Random Forests,” University of California, Berkeley, Statistics Technical Report 457, publicly dated 1996-09-01; later *Annales de l'Institut Henri Poincaré* 34 (1998), 339–383. https://statistics.berkeley.edu/tech-reports/457
2. “Exact negative regression between endpoint degree and distance in a uniform Cayley tree,” published mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-negative-regression-between-endpoint-degree-and-distance-i--d9ddfb06a9ae
3. D. J. Aldous, “The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees,” *SIAM Journal on Discrete Mathematics* 3 (1990), 450–465. https://doi.org/10.1137/0403039
4. D. J. Aldous and J. Pitman, “A Family of Random Trees with Random Edge Lengths,” Berkeley Statistics Technical Report 526, public record dated 1998-06-01. https://live-statistics.pantheon.berkeley.edu/tech-reports/526
