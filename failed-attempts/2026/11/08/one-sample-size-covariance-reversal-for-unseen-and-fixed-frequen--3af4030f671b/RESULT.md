# One sample-size covariance reversal for unseen and fixed-frequency categories under symmetric Pólya sampling

## Finding

Let \(m\ge 3\), \(\alpha>0\), and an integer \(r\ge2\) be fixed. For each integer \(N\ge r\), let \(Y=(Y_1,\ldots,Y_m)\) be the occupancy vector after \(N\) exchangeable Pólya draws with equal initial weight \(\alpha\) in every category. Put
\[
U_0=\sum_{i=1}^{m}{\bf1}_{\{Y_i=0\}},\qquad U_r=\sum_{i=1}^{m}{\bf1}_{\{Y_i=r\}}.
\]
There is a unique real \(t_{m,r,\alpha}>r\), given as the root of the explicit gamma-function equation \((m-1)Q(t)=m\) below, for which **all integer sample sizes** obey
\[
\operatorname{Cov}(U_0,U_r)\begin{cases}>0,&r\le N<t_{m,r,\alpha},\\=0,&N=t_{m,r,\alpha},\\<0,&N>t_{m,r,\alpha}.\end{cases}
\]
In particular, there can be at most one integer sample size of exact zero covariance. In the uniform weak-composition case \(\alpha=1\),
\[
t_{m,r,1}=\frac{m(r-1)+2}{2},\qquad
\operatorname{Cov}(U_0,U_r)= m p_0p_r\frac{m(r-1)+2-2N}{N-r+m-2},
\]
where \(p_0=\Pr(Y_1=0)>0\) and \(p_r=\Pr(Y_1=r)>0\). Thus the zero is an attainable integer precisely when \(m(r-1)\) is even. For example, with three categories, uniform weak compositions and \(r=2\), the covariance is \(1/4\) at \(N=2\), but \(-3/25\) at \(N=3\).

For the independent uniform multinomial limit \(\alpha\to\infty\), the real crossing point tends to
\[
t_{m,r,\infty}=r+\frac{(r-1)\log\bigl(m/(m-1)\bigr)}{\log\bigl((m-1)^2/[m(m-2)]\bigr)}.
\]
For fixed \(r\ge2\) and large \(m\), the crossing locations therefore have respective leading terms \(m(r-1)/2\) at \(\alpha=1\) and \(m(r-1)\) in the multinomial limit. No monotonicity in \(\alpha\) is asserted.

## Assumptions and scope

The draw sequence follows the symmetric Pólya rule: conditional on the first \(k\) draws, category \(i\) receives the next draw with probability \((\alpha+Y_i)/(m\alpha+k)\). Equivalently, first draw \(P\sim\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\), then draw \(N\) conditionally independent categories with law \(P\). The number of categories \(m\), the fixed target frequency \(r\), and \(\alpha\) remain fixed when \(N\) varies. The rising factorial is \((x)^{\overline{k}}=\Gamma(x+k)/\Gamma(x)\), with \((x)^{\overline0}=1\).

When \(N<r\), \(U_r=0\) deterministically, so the covariance is zero without a sign transition. For \(r=1\), the covariance is zero at \(N=1\) and strictly negative for integers \(N\ge2\) when \(m\ge3\). The degenerate two-category case differs: for \(r\ge2\) it is positive at \(N=r\) and strictly negative at \(N>r\); for \(r=1\) it is zero at \(N=1\) and negative at \(N>1\).

## Proof

For integers \(N\ge r\) and \(m\ge3\), Dirichlet-multinomial integration gives the single-category probabilities
\[
p_0=\frac{((m-1)\alpha)^{\overline N}}{(m\alpha)^{\overline N}},\quad
p_r=\binom Nr\frac{(\alpha)^{\overline r}((m-1)\alpha)^{\overline{N-r}}}{(m\alpha)^{\overline N}},
\]
and the two-distinct-category joint probability
\[
p_{0r}=\Pr(Y_1=0,Y_2=r)=\binom Nr\frac{(\alpha)^{\overline r}((m-2)\alpha)^{\overline{N-r}}}{(m\alpha)^{\overline N}}.
\]
The events \(Y_i=0\) and \(Y_i=r\) are disjoint for the same \(i\). Exchangeability therefore yields
\[
\operatorname{Cov}(U_0,U_r)=m(m-1)p_{0r}-m^2p_0p_r
=m p_0p_r\bigl((m-1)Q_N-m\bigr),
\]
with the strictly positive ratio
\[
Q_N=\frac{p_{0r}}{p_0p_r}=
\frac{((m-2)\alpha)^{\overline{N-r}}(m\alpha)^{\overline N}}
{((m-1)\alpha)^{\overline{N-r}}((m-1)\alpha)^{\overline N}}.
\]
A direct cancellation proves the decisive recurrence
\[
\frac{Q_{N+1}}{Q_N}=
1-\frac{\alpha(r+\alpha)}{(N-r+(m-1)\alpha)(N+(m-1)\alpha)}\in(0,1).
\]
At \(N=r\), \(Q_r=(m\alpha)^{\overline r}/((m-1)\alpha)^{\overline r}>m/(m-1)\) for \(r\ge2\); strictness follows from the additional factors beyond the first. As \(N\to\infty\), the gamma-ratio asymptotics give
\[
Q_N\longrightarrow\frac{\Gamma((m-1)\alpha)^2}{\Gamma((m-2)\alpha)\Gamma(m\alpha)}<1
\]
by the strict log-convexity of \(\Gamma\). Thus precisely one sign reversal occurs between the initially positive and eventually negative regimes.

For the claimed **unique real** crossing, replace integer \(N\) by real \(t\ge r\) in the gamma representation of \(Q\). With \(g(x)=\psi(x+\alpha)-\psi(x)\), where \(\psi\) is the digamma function, \(g\) is positive and strictly decreasing for positive \(x\), since its derivative is \(\psi'(x+\alpha)-\psi'(x)<0\). Differentiation yields
\[
\frac{d}{dt}\log Q(t)=-g(t-r+(m-2)\alpha)+g(t+(m-1)\alpha)<0,
\]
so continuity and the endpoint bounds give exactly one real root. Every integer sign is determined by its location relative to this root.

At \(\alpha=1\), rising-factorial cancellation reduces the ratio to
\[
Q_N=\frac{(m-2)(N+m-1)}{(m-1)(N-r+m-2)}.
\]
Substituting this into the covariance factorization proves the displayed linear sign formula and critical sample size, with the parity statement following because \(N\) must be integral.

Finally, at fixed \(m,r,N\), letting \(\alpha\to\infty\) in the rising factorials gives
\[
Q_N\longrightarrow\left(\frac m{m-1}\right)^r
\left(\frac{m(m-2)}{(m-1)^2}\right)^{N-r}.
\]
Solving \((m-1)Q_N=m\) gives the displayed multinomial crossing. Both the Pólya and the multinomial real roots are simple, so the roots converge, using pointwise convergence together with strict monotonicity and bracketing. The large-\(m\) comparison is an elementary logarithmic expansion.

For \(r=1\), the first-factor equality \(Q_1=m/(m-1)\), followed by the same strict ratio decay, proves the boundary statement. For \(m=2\), both designated cells can be respectively empty and \(r\)-occupied only when \(N=r\); direct two-cell marginal probabilities prove the remaining cases.

## Verification

The standalone standard-library checker `verify_polya.py` enumerates every weak composition in its finite test ranges and integrates the Dirichlet-multinomial mass with exact rational arithmetic, independently of the derived covariance identity. It also independently checks the exact ratio recurrence, strict decrease, and the explicit \(\alpha=1\) sign threshold. A fresh execution passed 36,936 asserted rational comparisons across different category counts, sample sizes, target frequencies, and integer/fractional concentrations. These finite tests corroborate, but do not substitute for, the all-parameter analytic proof.

To reproduce: `python3 verify_polya.py` (Python standard library only).

## Relationship to prior work

Keener and Wu, *On Dirichlet Multinomial Distributions* (2006), study occupancy-frequency sums in the symmetric Dirichlet-multinomial model. Their Theorem 1 and Corollary 1 concern asymptotic normality and approximate marginal covariances in a regime where the number of categories and draws grow together; they do not give the finite fixed-\(m\) mixed unseen-versus-\(r\)-frequency sample-size crossing. Chen's earlier 1980–1981 papers develop the urn and general size-distribution limit framework. Cummins, Paik and Lv (arXiv:1502.00804v1, first publicly posted February 3, 2015) use the Dirichlet-compound multinomial for term burstiness, without the covariance sign result. Published results for independent uniform occupancy concern other parameter directions, including a sign switch across frequency at fixed sample size; they are not the same statement and do not imply this Pólya law without further work.

## Limitations

The theorem assumes symmetric positive concentrations and fixed finite \(m\). It does not treat unequal category weights or growing-\(m\) uniformity of the root expansion. No new central limit theorem or statistical estimator is asserted. Deriving this result from an alternative older general formula has not been ruled out across all historical literature; priority remains subject to broader scholarly review. The explicit \(\alpha=1\) sample-size threshold is an exact model-specific result, not an assertion about all random composition models.

## References

- Keener, R. W., and Wu, W. B. (2006), *On Dirichlet Multinomial Distributions*, open full-text manuscript: https://www.stat.uchicago.edu/~wbwu/papers/keener.pdf.
- Chen, W.-C. (1981), *Limit theorems for general size distributions*, *Journal of Applied Probability* **18**, 139–147. https://doi.org/10.2307/3213174.
- Chen, W.-C. (1981), *Some local limit theorems in the symmetric Dirichlet-multinomial urn models*, *Annals of the Institute of Statistical Mathematics* **33**, 405–415. https://doi.org/10.1007/BF02480951.
- Cummins, R., Paik, J. H., and Lv, Y. (2015), *A Polya Urn Document Language Model for Improved Information Retrieval*, arXiv:1502.00804v1 (2015-02-03). https://arxiv.org/abs/1502.00804.
