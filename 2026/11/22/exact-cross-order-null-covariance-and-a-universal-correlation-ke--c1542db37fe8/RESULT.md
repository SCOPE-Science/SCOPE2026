# Exact cross-order null covariance and a universal correlation kernel for overlapping squared-Gini spacings

## Finding

Let \(n\ge4\), let \(n-1\) independent uniform observations in \((0,1)\) be ordered, and include the two endpoint gaps, giving \(n\) spacings \(D_1,\ldots,D_n\). For an order \(1\le r\le\lfloor n/2\rfloor\), write \(N_r=n-r+1\), \(T_{i,r}=D_i+\cdots+D_{i+r-1}\) for \(1\le i\le N_r\), and define the overlapping squared-Gini statistic

\[
G_{n,r}=\frac{2}{N_r(N_r-1)}\sum_{1\le i<j\le N_r}(nT_{i,r}-nT_{j,r})^2.
\]

The following results concern **two possibly different orders** \(r,s\) evaluated on the same uniform sample. Let \(B_r\) be the \(N_r\)-by-\(n\) zero-one matrix with \((B_r)_{ij}=1\) precisely when \(i\le j<i+r\); set \(H_r=I_{N_r}-\mathbf1\mathbf1^{\mathsf T}/N_r\) and \(A_r=B_r^{\mathsf T}H_rB_r\). Define

\[
 t_r=\operatorname{tr}A_r,\quad
 w_{rs}=\operatorname{tr}(A_rA_s),\quad
 v_{rs}=\sum_{j=1}^n(A_r)_{jj}(A_s)_{jj},\quad
 (n)_{\overline j}=n(n+1)\cdots(n+j-1).
\]

The **exact finite-sample cross-order covariance** is

\[
\boxed{\operatorname{Cov}(G_{n,r},G_{n,s})=
\frac{4n^4}{(N_r-1)(N_s-1)}
\left[\frac{t_rt_s+2w_{rs}+6v_{rs}}{(n)_{\overline4}}
-\frac{t_rt_s}{(n)_{\overline2}^{\,2}}\right].}
\]

For every fixed pair of positive orders \(r,s\), as \(n\to\infty\), write \(p=\min(r,s)\), \(q=\max(r,s)\). Then

\[
\boxed{n\operatorname{Cov}(G_{n,r},G_{n,s})\longrightarrow
 C(r,s)=8\left[rs+p^2q-\frac{p(p^2-1)}3\right].}
\]

Moreover, the vector \(\sqrt n(G_{n,r}-\mathbb EG_{n,r},G_{n,s}-\mathbb EG_{n,s})\) converges to a centered bivariate Gaussian with covariance entries \(C(r,r),C(r,s),C(s,s)\), where \(C(r,r)=8r(r+1)(2r+1)/3\). Its limiting correlation is therefore

\[
\rho(r,s)=\frac{rs+p^2q-p(p^2-1)/3}
{\sqrt{r(r+1)(2r+1)s(s+1)(2s+1)}/3}.
\]

In the **sequential scale limit** (first \(n\to\infty\) at fixed orders, then both orders grow with \(p/q\to u\in[0,1]\)), this becomes the universal profile

\[
\boxed{\rho(r,s)\longrightarrow\frac{\sqrt u(3-u)}2.}
\]

For fixed \(r\) and \(s\to\infty\), the more precise relation is \(\rho(r,s)\sim3\sqrt{r(r+1)}/\sqrt{2(2r+1)s}\). The two-scale limit is deliberately **not** asserted to hold for every simultaneous growth regime \(r=r(n),s=s(n)\).

## Assumptions and scope

The null is a fully specified continuous distribution transformed to uniformity by its known cdf, or directly \(n-1\) independent \(\mathrm{Uniform}(0,1)\) observations. There are exactly \(n\) **linear, non-circular** gaps, including both endpoint gaps. Only overlapping windows completely contained in these gaps are used. The finite-sample formula holds for all integers \(n\ge4\) and \(1\le r,s\le\lfloor n/2\rfloor\). The Gaussian limit and the leading covariance formula hold for every fixed pair \(r,s\), without estimated parameters. This is the squared pairwise-difference statistic, not the uncentered sum of squared windows.

## Proof

**1. Exact quadratic-form representation.** The uniform gap vector \(D=(D_1,\ldots,D_n)^{\mathsf T}\) has \(\operatorname{Dirichlet}(1,\ldots,1)\) law. For any vector \(z\in\mathbb R^{N_r}\), \(\sum_{i<j}(z_i-z_j)^2=N_rz^{\mathsf T}H_rz\). Consequently,

\[
G_{n,r}=\frac{2n^2}{N_r-1}D^{\mathsf T}A_rD,
\qquad A_r\mathbf1=0.
\]

**2. Fourth-order Dirichlet identity.** Write \(D_i=E_i/S\) with independent rate-one exponentials \(E_i\), \(S=\sum_iE_i\), and set \(Z_i=E_i-1\). Then \(S\) and \(D\) are independent, \(\mathbb ES^j=(n)_{\overline j}\), and for any symmetric matrices \(A,B\) satisfying \(A\mathbf1=B\mathbf1=0\), \(E^{\mathsf T}AE=Z^{\mathsf T}AZ\). The centered exponential has variance one and fourth cumulant six. Expanding the independent centered fourth moments gives

\[
\mathbb E[(Z^{\mathsf T}AZ)(Z^{\mathsf T}BZ)]
=\operatorname{tr}A\operatorname{tr}B+2\operatorname{tr}(AB)
+6\sum_iA_{ii}B_{ii}.
\]

Dividing by \(\mathbb ES^4\) proves the corresponding Dirichlet fourth-order identity. Similarly \(\mathbb E(D^{\mathsf T}AD)=\operatorname{tr}A/(n)_{\overline2}\). Substituting \(A_r,A_s\) proves the exact finite-sample covariance and the exact expectation \(\mathbb EG_{n,r}=2n^2t_r/[(N_r-1)(n)_{\overline2}]\). There are no approximations in this step.

**3. Fixed-order Gaussian fluctuations.** For each fixed \(r\), define \(Y_{i,r}=Z_i+\cdots+Z_{i+r-1}\). By the same quadratic representation, using the empirical variance of the moving window sums and the expansion \((n/S)^2=1-2n^{-1}\sum_iZ_i+O_{\mathbb P}(n^{-1})\),

\[
\sqrt n\{G_{n,r}-2r\}
=\frac2{\sqrt n}\sum_{i=1}^{n}
\{Y_{i,r}^2-r-2rZ_i\}+o_{\mathbb P}(1),
\]

where only \(O_{\mathbb P}(n^{-1})\) endpoint corrections occur in the unscaled expression. All summands can be defined on a two-sided iid exponential sequence. Every finite linear combination for fixed orders is a finite-range-dependent, stationary, centered sequence with moments of every order. The standard finite-dependence central limit theorem and Cramér–Wold theorem give joint Gaussian convergence. The exact mean above differs from \(2r\) by \(O_r(n^{-1})\), so its use as the center does not change the limit.

**4. Long-run covariance and overlap sum.** Let \(c_{rs}(h)\) denote the number of common indices in \(\{1,\ldots,r\}\) and \(\{h+1,\ldots,h+s\}\). Independence, \(\mathbb EZ_i^2=1\), \(\mathbb EZ_i^3=2\), and fourth cumulant six give

\[
\operatorname{Cov}(Y_{0,r}^2,Y_{h,s}^2)
=2c_{rs}(h)^2+6c_{rs}(h).
\]

Because \(\sum_hc_{rs}(h)=rs\), the three linear-normalization correction terms contribute \(-4rs-4rs+4rs=-4rs\) to the long-run covariance of the bracketed influence functions. Hence that covariance is \(2\sum_hc_{rs}(h)^2+2rs\). The overlap counts have one plateau of height \(p\) and two ramps \(1,2,\ldots,p-1\), so

\[
\sum_hc_{rs}(h)^2=(q-p+1)p^2+2\sum_{j=1}^{p-1}j^2
=p^2q-\frac{p(p^2-1)}3.
\]

The outer factor \(2\) from each influence function yields precisely \(C(r,s)=8(rs+\sum_h c_{rs}(h)^2)\). This also independently derives the limit of the exact finite-sample formula: \(\operatorname{tr}A_r=nr+O_r(1)\), \(\operatorname{tr}(A_rA_s)=n\sum_hc_{rs}(h)^2+O_{r,s}(1)\), and \(v_{rs}=nrs+O_{r,s}(1)\), which give the same coefficient by expansion of the rising factorials.

**5. Scale-ratio profile.** Substitute \(p\le q\) in the explicit \(C\) and divide by the square root of the two diagonal constants. If \(p,q\to\infty\) with \(p/q\to u\), the dominant terms are \(p^2q-p^3/3\) in the numerator and \((2/3)(pq)^{3/2}\) in the denominator, yielding \(\sqrt u(3-u)/2\). The formula remains valid at \(u=0\) by the bound \(\rho\le O(\sqrt{p/q})\). Keeping \(p=r\) fixed instead gives the stated sharper \(s^{-1/2}\) coefficient. The fixed-pair limiting correlation lies strictly between zero and one for distinct orders, by the positive long-run variance of their nonproportional quadratic moving-average influence functions.

## Verification

Run `python3 check_multiscale_spacings.py` with Python 3 and its standard library. The checker reconstructs the centered window matrices exactly in rational arithmetic for \(4\le n\le9\), verifies all matrix row sums, and independently integrates each four-index Dirichlet monomial (not merely re-evaluating the matrix fourth-cumulant identity). It verifies overlap-count polynomials for 361 ordered pairs of window lengths, tests the fixed-order constants including the known single-order formula, and performs a deterministic-seed Monte Carlo comparison on an independent exponential-to-Dirichlet simulation. The recorded run completed **989 assertions**. The analytic proof, rather than finite enumeration or the simulation, establishes the quantifiers over all admissible integers and the large-sample limit.

## Relationship to prior work

Singh and Misra (first public arXiv posting October 20, 2021) define this overlapping squared-Gini statistic and establish single-order asymptotic normality and local optimality. Their Theorem 1 and equations (5)–(6) supply the statistic and marginal context, not the exact mixed-order finite-sample covariance or the explicit cross-order correlation kernel. Rao and Kuo (1984) study asymptotic efficiencies of higher-order Greenwood statistics and multivariate dependence among **offset blocks at one fixed order**; their printed theorem does not provide covariance between different window lengths of the non-circular squared-Gini statistic. Guttorp and Lockhart (1989) derive exact moments and weighted-chi-square approximations for a **circularized single-order** Greenwood statistic, not these linear mixed-order covariances. Mirakhmedov (2025) studies marginal asymptotics and efficiencies when the order grows, including comparisons between orders based on efficacy; its theorems do not directly report a same-sample joint covariance kernel. No contribution is claimed for the Dirichlet spacing law, fourth-moment identity, individual-order Gaussian limits, or routine general CLT tools.

## Limitations

The explicit scale profile is a sequential asymptotic statement; a simultaneous \(r(n),s(n)\) triangular-array central limit theorem is not proved here. Exact critical values and joint power against alternatives are not derived. Results apply to fully specified continuous nulls and to unwrapped overlapping spacings, without fitted distribution parameters. Earlier equivalent general quadratic-form theorems may provide another route to the exact identity, and independent historical-priority review remains appropriate.

## References

1. Rahul Singh and Neeraj Misra, *U-statistic based on overlapping sample spacings*, first public arXiv posting 2021-10-20, https://arxiv.org/abs/2110.10737 .
2. J. S. Rao and Morgan Kuo, *Asymptotic Results on the Greenwood Statistic and Some of its Generalizations*, JRSS B **46** (1984), 228–237, https://escholarship.org/content/qt9b00w65w/qt9b00w65w_noSplash_da50acc4f3d0182348ff623b32140d2b.pdf .
3. Peter Guttorp and Richard A. Lockhart, *On the Asymptotic Distributions of High-Order Spacings Statistics*, Canadian Journal of Statistics **17** (1989), 419–426, https://www.sfu.ca/~lockhart/Research/Papers/GuttorpLockhartCJS89.pdf .
4. Sherzod M. Mirakhmedov, *Asymptotic properties of goodness of fit tests based on higher order overlapping spacings*, first public arXiv posting 2025-08-26, https://arxiv.org/abs/2508.18965 .
