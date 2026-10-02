# Exact dependence of jackknife pseudo-values for U-statistics

## Setup

Let \(X_1,\ldots,X_n\) be iid, let \(n>m\), and let
\[
h:\mathcal X^m\to\mathbb R^d
\]
be a symmetric square-integrable kernel with target \(\theta=\mathbb Eh(X_1,\ldots,X_m)\). Write the complete one-sample U-statistic as
\[
U_n={1\over {n\choose m}}\sum_{|A|=m}h(X_A).
\]
For each \(i\), let \(U_{n-1}^{(-i)}\) be the same degree-\(m\) U-statistic after deleting observation \(i\), and define the usual delete-one pseudo-value
\[
V_i=nU_n-(n-1)U_{n-1}^{(-i)}.
\]

Use the canonical Hoeffding decomposition
\[
h(x_1,\ldots,x_m)=\theta+
\sum_{r=1}^m\ \sum_{|S|=r}h_r(x_S),
\]
and put
\[
\Gamma_r=\operatorname{Cov}\bigl(h_r(X_1,\ldots,X_r)\bigr).
\]
Thus every \(\Gamma_r\) is positive semidefinite; in the scalar case write \(\sigma_r^2=\Gamma_r\).

## Main theorem: exact finite-sample covariance

For every \(i\),
\[
\boxed{
\operatorname{Var}(V_i)=
\sum_{r=1}^m {m\choose r}^2
{r(n-2)+1\over {n-1\choose r}}\,\Gamma_r .
}
\]
For every pair \(i\ne j\),
\[
\boxed{
\operatorname{Cov}(V_i,V_j)=
-\sum_{r=2}^m {m\choose r}^2
{r-1\over {n-1\choose r}}\,\Gamma_r .
}
\]
Consequently, every cross-pseudo-value covariance matrix is negative semidefinite. Moreover,
\[
\operatorname{Cov}(V_i,V_j)=0\quad(i\ne j)
\]
if and only if \(\Gamma_r=0\) for every \(r\ge2\), equivalently the kernel is additive almost surely:
\[
h(x_1,\ldots,x_m)=\theta+\sum_{a=1}^m h_1(x_a).
\]
In this exceptional case
\[
V_i=\theta+m h_1(X_i),
\]
so the pseudo-values are in fact mutually independent and identically distributed. Thus, under the stated square-integrability assumptions, exact pairwise uncorrelatedness of delete-one pseudo-values is equivalent to this additive-kernel case.

### Sharp scalar correlation interval

Suppose \(d=1\), \(m\ge2\), and \(\operatorname{Var}(V_i)>0\). Then
\[
\boxed{
-{m-1\over m(n-2)+1}
\le \operatorname{Corr}(V_i,V_j)\le0,
\qquad i\ne j.
}
\]
Both endpoints are attainable. The upper endpoint occurs for a nonconstant additive kernel. The lower endpoint occurs for a completely \(m\)-degenerate kernel. More generally, if only the canonical Hoeffding component of order \(r\) is nonzero, then
\[
\operatorname{Corr}(V_i,V_j)
=-{r-1\over r(n-2)+1}.
\]
Every value in the displayed interval is attainable by continuously mixing a first-order component and an independent fully \(m\)-degenerate component.

## Exact link to jackknife variance bias

The pseudo-values satisfy the exact identity
\[
{1\over n}\sum_{i=1}^n V_i=U_n.
\]
Define the usual jackknife covariance estimator of \(U_n\) by
\[
\widehat\Sigma_J={1\over n(n-1)}
\sum_{i=1}^n(V_i-U_n)(V_i-U_n)^\top.
\]
Exchangeability of the pseudo-values and the covariance formula above give
\[
\boxed{
\mathbb E\widehat\Sigma_J-\operatorname{Var}(U_n)
=-\operatorname{Cov}(V_1,V_2)
=\sum_{r=2}^m {m\choose r}^2
{r-1\over {n-1\choose r}}\,\Gamma_r\succeq0.
}
\]
Hence, for complete one-sample U-statistics, the finite-sample upward bias of the delete-one jackknife covariance estimator is exactly the magnitude of the negative cross-pseudo-value covariance.

Since
\[
\operatorname{Var}(U_n)=
\sum_{r=1}^m {m\choose r}^2{1\over {n\choose r}}\Gamma_r,
\]
the order-\(r\) bias-to-variance coefficient ratio is
\[
{n(r-1)\over n-r},
\]
which is increasing in \(r\). This yields the sharp matrix inequality
\[
\boxed{
\operatorname{Var}(U_n)
\preceq \mathbb E\widehat\Sigma_J
\preceq {m(n-1)\over n-m}\operatorname{Var}(U_n).
}
\]
The constant is attained by a fully \(m\)-degenerate kernel. For a pure order-\(r\) canonical kernel, the expected jackknife variance inflation factor is exactly
\[
{r(n-1)\over n-r}.
\]

## A basic finite-sample counterexample to exact uncorrelatedness

Let \(X_i\) be iid Rademacher variables and take the degree-two kernel
\[
h(x,y)=xy.
\]
This kernel is completely degenerate. For every \(n\ge3\),
\[
\operatorname{Var}(V_i)=
{2(2n-3)\over(n-1)(n-2)},
\qquad
\operatorname{Cov}(V_i,V_j)=
-{2\over(n-1)(n-2)},
\]
so
\[
\boxed{
\operatorname{Corr}(V_i,V_j)=-{1\over 2n-3}.
}
\]
At \(n=3\) the correlation is \(-1/3\). It tends to zero as \(n\to\infty\), so this finite-sample dependence is fully compatible with asymptotic-independence results.

## Proof

For each canonical order \(r\), write \(H_{r,A}=h_r(X_A)\). The U-statistic decomposition is
\[
U_n-\theta=
\sum_{r=1}^m {m\choose r}{1\over {n\choose r}}
\sum_{|A|=r}H_{r,A}.
\]
After substituting this expansion in \(V_i\), the coefficient of \(H_{r,A}\), apart from the common factor \({m\choose r}\), is
\[
\alpha_r={r\over {n-1\choose r-1}}
\quad\text{if }i\in A,
\qquad
\beta_r={1-r\over {n-1\choose r}}
\quad\text{if }i\notin A.
\]
Canonical Hoeffding terms are orthogonal unless both their order and index set agree. Therefore the order-\(r\) contribution to \(\operatorname{Var}(V_i)\) is
\[
{n-1\choose r-1}\alpha_r^2+{n-1\choose r}\beta_r^2
={r(n-2)+1\over {n-1\choose r}}.
\]
For distinct \(i,j\), partition the \(r\)-subsets according to whether they contain both, exactly one, or neither of \(i,j\). The corresponding cross coefficient is
\[
{n-2\choose r-2}\alpha_r^2
+2{n-2\choose r-1}\alpha_r\beta_r
+{n-2\choose r}\beta_r^2
=-{r-1\over {n-1\choose r}},
\]
which proves the two covariance formulas.

Because every \(\Gamma_r\) is positive semidefinite and every coefficient in the cross covariance for \(r\ge2\) is strictly positive before the minus sign, a zero cross-covariance matrix forces \(\Gamma_r=0\) for all \(r\ge2\). The additive characterization and exact independence then follow immediately from the Hoeffding decomposition.

In the scalar case the negative correlation is a weighted average of
\[
q_r={r-1\over r(n-2)+1},\qquad r=1,\ldots,m,
\]
with nonnegative weights proportional to the order-wise contributions to \(\operatorname{Var}(V_i)\). The sequence \(q_r\) is strictly increasing, from \(0\) to \((m-1)/(m(n-2)+1)\), proving the sharp correlation interval. A kernel on observations \(X=(A,B)\) with independent Rademacher coordinates,
\[
h(x_1,\ldots,x_m)=a\sum_{k=1}^m A_k+b\prod_{k=1}^m B_k,
\]
varies continuously between the two endpoint structures and realizes every intermediate value.

Finally, each degree-\(m\) kernel tuple occurs in exactly \(n-m\) leave-one-out statistics, so \(n^{-1}\sum_iV_i=U_n\). If
\[
D=\operatorname{Var}(V_i),\qquad C=\operatorname{Cov}(V_i,V_j),\quad i\ne j,
\]
then exchangeability gives
\[
\operatorname{Var}(U_n)={D+(n-1)C\over n},
\qquad
\mathbb E\widehat\Sigma_J={D-C\over n}.
\]
Their difference is \(-C\), proving the exact bias identity. Comparing its order-\(r\) coefficient with the standard variance coefficient \({m\choose r}^2/{n\choose r}\) gives \(n(r-1)/(n-r)\), and maximizing this over \(1\le r\le m\) proves the sharp Loewner bound.

## Literature context and originality boundary

The jackknife theory for U-statistics is classical. Arvesen (1969) developed jackknifing for U-statistics; Miller (1974) reviewed the pseudo-value interpretation as approximately iid; Hinkley and Wang (1980) explicitly noted that pseudo-values are generally not independent; and Efron and Stein (1981) established the classical upward-bias phenomenon for jackknife variance estimation using an ANOVA/Hoeffding-type decomposition. These facts and the standard Hoeffding decomposition are not claimed as new.

Later work continued to use approximate or asymptotic pseudo-value independence, including Shi (1984) and jackknife empirical likelihood. A recent U-statistic testing paper states that jackknife pseudo-values are “uncorrelated” as well as asymptotically independent. The formulas above show that an exact finite-sample reading of “uncorrelated” is false for general U-statistics: all nonlinear Hoeffding orders create strictly negative cross-covariance, while the covariance vanishes exactly in the additive case. This does not contradict asymptotic independence, because for fixed kernel degree the displayed correlations vanish as the sample size grows.

To the best of our knowledge, the specific contribution here is the explicit all-order finite-sample cross-pseudo-value covariance decomposition, its negative-semidefinite sign and iff-additive equality characterization, the sharp scalar correlation interval, and the identity equating jackknife covariance bias exactly with minus the cross-pseudo-value covariance, together with the sharp matrix inflation factor. The complete theorem text of Arvesen (1969) and Shi (1984) was not inspected; these are the principal residual originality risks. Efron and Stein (1981) was checked directly for its ANOVA decomposition and jackknife-variance context, and the available Hinkley--Wang and modern U-statistic statements were compared explicitly.

## Limitations

The result is for complete one-sample U-statistics of fixed degree with square-integrable symmetric kernels and the ordinary delete-one jackknife. It does not cover incomplete U-statistics, two-sample U-statistics, delete-\(d\) jackknives, censored pseudo-observations, or general smooth statistics outside the exact U-statistic representation. The covariance formulas are population identities; they do not by themselves give a new optimal estimator or a finite-sample distributional approximation. The originality claim is necessarily qualified by the uninspected full text of Arvesen (1969) and Shi (1984).

## Reproducibility

`artifacts/verify_exact.py` uses exact rational arithmetic to check the coefficient identities on a finite grid, directly enumerates the Rademacher pair-product example, and verifies the order-wise jackknife-bias ratios. `artifacts/VERIFICATION.txt` records the verified output. These computations support the algebraic proof but do not replace it.

## References

1. J. N. Arvesen, “Jackknifing U-Statistics,” *Annals of Mathematical Statistics* 40 (1969), 2076–2100. https://doi.org/10.1214/aoms/1177697287
2. R. G. Miller, “The jackknife—a review,” *Biometrika* 61 (1974), 1–15. https://doi.org/10.1093/biomet/61.1.1
3. D. V. Hinkley and H.-L. Wang, “A Trimmed Jackknife,” *JRSS B* 42 (1980), 347–356. https://doi.org/10.1111/j.2517-6161.1980.tb01135.x
4. B. Efron and C. Stein, “The Jackknife Estimate of Variance,” *Annals of Statistics* 9 (1981), 586–596. https://doi.org/10.1214/aos/1176345462
5. X. Shi, “The approximate independence of jackknife pseudo-values and the bootstrap methods,” *Journal of Wuhan Institute of Hydraulic and Electric Engineering* 2 (1984), 83–90.
6. B.-Y. Jing, J. Yuan, and W. Zhou, “Jackknife empirical likelihood,” *Journal of the American Statistical Association* 104 (2009), 1224–1232. https://doi.org/10.1198/jasa.2009.tm08260
7. Y. Maesono, “Asymptotic representations of skewness estimators of studentized U-statistics,” *Bulletin of Informatics and Cybernetics* 36 (2004), 91–104. https://doi.org/10.5109/12581
8. Y. Zhang and Z. Jin, “High-Dimensional U-Statistics Type Hypothesis Testing via Jackknife Pseudo-Values with Multiplier Bootstrap,” *Mathematics* 12 (2024), 3837. https://doi.org/10.3390/math12233837
