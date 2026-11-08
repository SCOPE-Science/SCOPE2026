# A rank-one-threshold law for Greenwood dependence in uniform spacings

## Finding
For \(m\ge2\) random points independently uniform on a unit circle, list the \(m\) cyclic arc lengths as \(X_1,\ldots,X_m\). Let \(Y_{m,1}\ge\cdots\ge Y_{m,m}\) be the ranked lengths and \(G_m=\sum_{i=1}^m X_i^2\) be the Greenwood spacing statistic. Define
\[
A_{m,k}=\sum_{j=k}^m\frac1j,\qquad B_{m,k}=\sum_{j=k}^m\frac1{j^2}.
\]
Then the **entire rank-indexed covariance profile** is
\[
\boxed{\operatorname{Cov}(Y_{m,k},G_m)=\frac{A_{m,k}^2+B_{m,k}-2A_{m,k}}{m(m+1)(m+2)}},\qquad 1\le k\le m.
\]
For every \(m\ge2\) there is a single sign transition from positive to negative in increasing rank, with at most one exactly zero intermediate rank. With \(J_m=\#\{k:\operatorname{Cov}(Y_{m,k},G_m)>0\}\),
\[
\lim_{m\to\infty}\frac{J_m}{m}=e^{-2}.
\]
More strongly, when integers \(k_m\) satisfy \(k_m/m\to\alpha\in(0,1)\),
\[
\lim_{m\to\infty}\operatorname{Corr}(Y_{m,k_m},G_m)
=\frac{\log^2(1/\alpha)-2\log(1/\alpha)}{2\sqrt{\alpha^{-1}-1-\log^2(1/\alpha)}}.
\]
This limit changes sign at precisely \(\alpha=e^{-2}\approx0.135335\). A ranked arc near the upper \(13.5\%\) of sizes has a positive limiting correlation with Greenwood concentration; ranks below this cutoff have a negative limiting correlation.

## Assumptions and scope
The distribution of \((X_1,\ldots,X_m)\) is uniform on the simplex \(\{x_i\ge0,\sum_i x_i=1\}\), or equivalently \(\mathrm{Dirichlet}(1,\ldots,1)\). For circular points, the starting point is irrelevant because the ranked gaps are permutation-invariant. There are no ties with positive probability. Rank \(k=1\) means the largest gap; \(k=m\) means the smallest. Covariance and Pearson correlation use their usual centered definitions. No assertion is made for nonuniform Dirichlet parameters, for fixed-rank asymptotic correlations, or for other power statistics.

## Proof
**Step 1: exact ranked-simplex representation.** Let \(E_1,\ldots,E_m\) be independent unit exponentials, \(T=\sum_iE_i\), and \(P_j=E_j/T\). Exponential order-statistic increments are independent, and the gap between the \(j\)-th and \((j+1)\)-th largest exponential order statistics has the law \(E_j/j\). Since the sum of all exponentials is \(T\), the joint ordered Dirichlet vector has the representation
\[
(Y_{m,k})_{k=1}^m\ \stackrel{d}{=}\ \left(\sum_{j=k}^m\frac{P_j}{j}\right)_{k=1}^m,
\qquad (P_1,\ldots,P_m)\sim\mathrm{Dirichlet}(1,\ldots,1).
\]
In the same coupling, the squared-length sum is
\[
G_m=\sum_{k=1}^m\left(\sum_{j=k}^m\frac{P_j}{j}\right)^2
=\sum_{a,b=1}^m\frac{P_aP_b}{\max(a,b)}.
\]
The last identity counts the number \(\min(a,b)\) of ranks contributing to each product.

**Step 2: third Dirichlet moments.** Write \(C_{ab}=1/\max(a,b)\), \(R_j=\sum_b C_{jb}\). The elementary sums are
\[
\sum_a C_{aa}=H_m,\quad \sum_{a,b}C_{ab}=2m-H_m,\quad R_j=1+H_m-H_j,
\]
where \(H_j=\sum_{r=1}^j1/r\), with \(H_0=0\). Uniform-simplex integration gives
\[
\mathbb E[P_jP_aP_b]=\frac{1+\mathbf1_{j=a}+\mathbf1_{j=b}+\mathbf1_{a=b}+2\mathbf1_{j=a=b}}{m(m+1)(m+2)}.
\]
Since \(\mathbb EG_m=2/(m+1)\) and \(\mathbb EP_j=1/m\), direct substitution yields
\[
\operatorname{Cov}(P_j,G_m)=\frac{2(H_m-H_{j-1}-1)}{m(m+1)(m+2)}.
\]
Linearity now reduces the desired covariance to \(2\sum_{j=k}^m(H_m-H_{j-1}-1)/j\) over the same denominator. The identity
\[
\sum_{j=k}^m\frac{H_m-H_{j-1}}{j}
=\frac12\left[A_{m,k}^2+B_{m,k}\right]
\]
follows by counting ordered pairs \(k\le j\le r\le m\) in the double harmonic sum. This proves the displayed exact formula for every integer \(m,k\) in scope.

**Step 3: one finite sign transition.** Put \(T_{m,k}=(A_{m,k}^2+B_{m,k}-2A_{m,k})/2\), and \(T_{m,m+1}=0\). Then
\[
T_{m,k}-T_{m,k+1}=\frac{A_{m,k}-1}{k}.
\]
Because \(A_{m,k}\) decreases strictly with \(k\), the sequence \(T_{m,k}\) first decreases and then increases (either part may be empty). At \(k=1\), \(T_{m,1}>0\): this holds at \(m=2\) and increases with \(m\), since adding \(1/m\) to \(H_{m-1}\) increases \(H_m^2+H_m^{(2)}-2H_m\) by \(2(H_{m-1}-1+1/m)/m>0\). At \(k=m\), \(T_{m,m}=(1-m)/m^2<0\). On the increasing tail its values remain negative because the endpoint \(T_{m,m+1}\) is zero. Thus the positive ranks form a nonempty initial segment, the negative ranks a nonempty terminal segment, and at most one intermediate rank can have zero covariance.

**Step 4: limiting correlation and the universal cutoff.** Dirichlet second and fourth moments supply the exact variances
\[
\operatorname{Var}(Y_{m,k})=\frac{mB_{m,k}-A_{m,k}^2}{m^2(m+1)},\qquad
\operatorname{Var}(G_m)=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)}.
\]
If \(k_m/m\to\alpha\in(0,1)\), Riemann sums imply \(A_{m,k_m}\to L=\log(1/\alpha)\) and \(mB_{m,k_m}\to\alpha^{-1}-1\). Hence the covariance multiplied by \(m^3\) tends to \(L^2-2L\), while the two variances multiplied by \(m^3\) tend to \(\alpha^{-1}-1-L^2\) and \(4\), respectively. Their first limit is strictly positive, since \(e^L-1>L^2\) for \(L>0\). Dividing yields the claimed correlation profile. Its numerator changes sign only at \(L=2\), i.e. \(\alpha=e^{-2}\). Since finite covariance signs have a single rank transition, pointwise limiting signs on either side force \(J_m/m\to e^{-2}\).

## Verification
A standalone, standard-library-only checker is included as `verify_rank_greenwood.py`. Run `python3 verify_rank_greenwood.py` to independently evaluate the Dirichlet polynomial expectations using exact fractions and factorial integrals and compare them with the closed form over all \(2\le m\le17\) and every rank. It also checks exact endpoint variances, one-transition sign ordering through \(m=99\), and numerical convergence at larger sizes. These finite checks corroborate the analytic argument but are not used as infinite proofs.

## Relationship to prior work
Holst (1980) establishes the ordered-uniform-spacing exponential representation and marginal rank facts used in Step 1; the new claim is the mixed rank–Greenwood covariance, its complete finite sign structure, and the sharp rank-fraction correlation transition. Schlemm (2014, originally public May 23, 2014) treats moments and limit law of the largest circular gap rather than the ranked mixed covariance profile. Ghosh and Jammalamadaka (1998) study approximations for spacing-statistic marginals, including Greenwood's statistic. Erdmann-Pham, Terhorst and Song (2020/2022) analyze a different two-sample **rank-spacing count** model and associated weighted norms, rather than the ranked lengths of continuous Dirichlet spacings. General tools for extracting mixed moments exist; priority beyond the specifically inspected material cannot be guaranteed.

## Limitations
The law is specific to symmetric unit-parameter Dirichlet spacings. At the critical \(k/m\to e^{-2}\) fraction, the limiting correlation vanishes; it does not specify the finer finite-rank sign in a shrinking critical window. The proof does not assert conditional association, independence, or monotonicity of individual paths. Independent scholarly audit and exhaustive historical-priority verification have not been performed.

## References
- L. Holst, *On the Lengths of the Pieces of a Stick Broken at Random*, Journal of Applied Probability 17 (1980), 623–634. https://doi.org/10.2307/3212956
- E. Schlemm, *Limiting distribution of the maximal distance between random points on a circle: A moments approach*, arXiv:1405.6114v1, May 23, 2014. https://arxiv.org/abs/1405.6114
- K. Ghosh and S. R. Jammalamadaka, *Small sample approximations for spacing statistics*, Journal of Statistical Planning and Inference 69 (1998), 245–261. https://jammalam.faculty.pstat.ucsb.edu/html/Some%20Publications/1998_SmallSample%20AppoxSpacings_JSPI.pdf
- D. D. Erdmann-Pham, J. Terhorst and Y. S. Song, *Exact and arbitrarily accurate non-parametric two-sample tests based on rank spacings*, arXiv:2008.06664 (2020), version of 2022. https://arxiv.org/abs/2008.06664
