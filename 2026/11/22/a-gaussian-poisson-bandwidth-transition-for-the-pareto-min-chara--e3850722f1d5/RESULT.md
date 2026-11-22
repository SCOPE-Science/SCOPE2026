# A Gaussian–Poisson bandwidth transition for the Pareto min-characteristic goodness-of-fit statistic

## Finding

Consider the exponential-weight Pareto min-characteristic-function statistic introduced by Meintanis, Milošević and Jiménez-Gamero. **Under the Pareto null, if its weight rate \(\gamma_n\) tends to infinity, its limiting null law changes sharply at \(\gamma_n\) of order the sample size.** This holds after the published two-parameter maximum-likelihood standardization, not merely with known nuisance parameters.

For \(n\ge2\), let \(X_1,\ldots,X_n\) be independent Pareto type-I observations with unknown support endpoint \(c>0\) and shape \(\alpha>0\):
\[
\Pr(X_i>x)=(c/x)^\alpha,\qquad x\ge c.
\]
Set
\[
\widehat c=X_{(1)},\quad
\widehat\alpha=\frac{n}{\sum_{i=1}^n\log(X_i/\widehat c)},\quad
\widehat Y_i=(X_i/\widehat c)^{\widehat\alpha}\ge1.
\]
Define \(\psi_n(t)=n^{-1}\sum_i\min(1,t\widehat Y_i)\) and \(\psi_0(t)=t(1-\log t)\) for \(0<t\le1\), \(\psi_0(t)=1\) for \(t>1\). The exact published weighted statistic is
\[
T_{n,\gamma}=n\int_0^\infty[\psi_n(t)-\psi_0(t)]^2e^{-\gamma t}\,dt.
\]
Let \(H=L^2((0,\infty),u^2e^{-u}\,du)\). Let \(G\) be the centered \(H\)-valued Gaussian element with covariance
\[
K(u,v)=\frac{2+|\log(u/v)|}{\max(u,v)},\quad u,v>0,
\qquad Q=\int_0^\infty u^2e^{-u}G(u)^2\,du.
\]
For \(c_0>0\), let \(\mathcal N\) be a Poisson random measure on \((0,\infty)\) of intensity \(x^{-2}dx\), and use its compensated version to define the \(H\)-valued integral
\[
Z_{c_0}(u)=\int_0^\infty\min(x,c_0/u)\,[\mathcal N(dx)-x^{-2}dx],
\qquad W_{c_0}=c_0^{-1}\int_0^\infty u^2e^{-u}Z_{c_0}(u)^2\,du.
\]
The compensated integral is defined by its \(L^2\) small-jump limit; its expectation as an uncompensated integral is not asserted to exist.

**Theorem.** For every deterministic \(\gamma_n\to\infty\), without a supplementary growth-rate assumption:

1. If \(\gamma_n/n\to0\), then \(\gamma_n^2 T_{n,\gamma_n}\Rightarrow Q\).
2. If \(\gamma_n/n\to c_0\in(0,\infty)\), then \(\gamma_n^2 T_{n,\gamma_n}\Rightarrow W_{c_0}\).
3. If \(\gamma_n/n\to\infty\), then
\[
\frac{\gamma_n^3T_{n,\gamma_n}}{n\{\log(\gamma_n/n)\}^2}\xrightarrow{\Pr}2,
\quad\text{and therefore}\quad \gamma_n^2T_{n,\gamma_n}\xrightarrow{\Pr}0.
\]

The two nondegenerate limits satisfy the **exact moment separation**
\[
\begin{split}
&\mathbb EQ=\mathbb EW_{c_0}=2,\\
&\operatorname{Var}(Q)=24\int_0^1\frac{t^2(2-\log t)^2}{(1+t)^4}\,dt
=6.70464997926537\ldots,\\
&\operatorname{Var}(W_{c_0})=\operatorname{Var}(Q)
+\frac{8c_0}{3}(1-\log2).
\end{split}
\]
In particular the critical law differs from the Gaussian quadratic law for each \(c_0>0\); its variance excess is exactly linear in the cutoff-to-sample ratio.

## Assumptions and scope

The distributional statements concern iid, uncensored observations from the two-parameter Pareto type-I null with fixed positive support and shape. The sample size tends to infinity, and \(\gamma_n\) is positive, deterministic and tends to infinity. Fitted parameters are the likelihood estimators above; the one-observation case is excluded because the fitted shape is undefined. The convergence statements are invariant to the unknown true parameters. The theorem concerns null distributions of the statistic itself; it does not assert power, bootstrap validity, or type-I error for an unspecified calibration.

## Proof

**1. Exact reduction and oracle representation.** By Pareto transformation invariance, \(E_i=\alpha\log(X_i/c)\) are iid exponential variables of rate one. Write \(m_n=\min_i E_i\), \(\beta_n=n/\sum_i(E_i-m_n)\), and \(Y_i=e^{E_i}\). Then \(\widehat Y_i=e^{\beta_n(E_i-m_n)}\). The strong law and exponential concentration give
\[
\beta_n-1=O_{\Pr}(n^{-1/2}),\quad m_n=O_{\Pr}(n^{-1}),\quad
\max_iE_i=O_{\Pr}(\log n).
\]
For the *oracle* observations \(Y_i\), which have \(\Pr(Y_i>y)=y^{-1}\) for \(y\ge1\), put
\[
S_n(u)=\frac1n\sum_{i=1}^n\min(Y_i,\gamma_n/u)
-\left(1+\log(\gamma_n/u)\right),\quad 0<u\le\gamma_n,
\]
and \(S_n(u)=0\) for \(u>\gamma_n\). The exact null minCF is \(t(1-\log t)\) for \(t\le1\); the empirical and theoretical minCFs both equal one for \(t>1\). Changing variables \(u=\gamma_nt\) therefore gives the *identity*
\[
T^{\mathrm{or}}_{n,\gamma_n}=\frac{n}{\gamma_n^3}\|S_n\|_H^2,
\qquad\gamma_n^2T^{\mathrm{or}}_{n,\gamma_n}
=\frac n{\gamma_n}\|S_n\|_H^2.
\tag{1}
\]
For \(v\ge1\), \(\mathbb E\min(Y_i,v)=1+\log v\). For \(1\le a\le b\), direct integration against density \(y^{-2}\) yields
\[
\mathbb E[\min(Y_i,a)\min(Y_i,b)]=2a-1+a\log(b/a).
\tag{2}
\]
Consequently, as \(\gamma_n\to\infty\),
\[
\gamma_n^{-1}\operatorname{Cov}\{\min(Y_i,\gamma_n/u),\min(Y_i,\gamma_n/v)\}
\longrightarrow K(u,v)
\tag{3}
\]
for each fixed positive \(u,v\). Moreover \(\operatorname{Var}\min(Y_i,v)\le2v\), giving \(\mathbb E|S_n(u)|^2\le2\gamma_n/(nu)\) when \(u\le\gamma_n\). The weighted trace is controlled by \(2\int_0^\infty ue^{-u}du=2\).

**2. Gaussian regime.** If \(\gamma_n/n\to0\), define \(G_n=\sqrt{n/\gamma_n}S_n\in H\). It is a sum of independent, centered \(H\)-valued elements, each of norm at most \(\sqrt{\gamma_n/n}\) because \(\min(Y_i,\gamma_n/u)\le\gamma_n/u\). Hence the Hilbert-space Lindeberg condition is automatic. Formula (3), dominated covariance traces, and finite-rank approximation show convergence of the covariance operators in trace norm to that determined by \(K\), establishing \(G_n\Rightarrow G\) in \(H\). Continuous mapping and (1) give the first limit. The bound at zero is \(\int_0^\delta2ue^{-u}du\), and the bound at infinity is \(\int_R^\infty2ue^{-u}du\), so no finite-frequency truncation is silently assumed.

**3. Critical Poisson regime.** If \(c_n=\gamma_n/n\to c_0>0\), write for each fixed \(u\), with \(u\le\gamma_n\),
\[
S_n(u)=\sum_{i=1}^n\left[\min(Y_i/n,c_n/u)
-\mathbb E\min(Y_i/n,c_n/u)\right].
\tag{4}
\]
The empirical point measure \(\sum_i\delta_{Y_i/n}\) converges on sets bounded away from zero to \(\mathcal N\), since \(n\Pr(Y_i/n\in dx)=x^{-2}dx\) for \(x\ge1/n\). Restricting (4) to \(x>\varepsilon\) gives finite-activity Poisson convergence in \(H\). The discarded centered part satisfies, uniformly in \(n\),
\[
\mathbb E\|S_{n,\le\varepsilon}\|_H^2\le
\int_0^\infty u^2e^{-u}\,du\int_0^\varepsilon x^2x^{-2}dx
=2\varepsilon.
\]
The same bound holds for the compensated Poisson integral. Letting \(\varepsilon\downarrow0\) proves \(S_n\Rightarrow Z_{c_0}\) in \(H\) and hence the second limit by (1).

**4. Supercritical regime.** If \(c_n=\gamma_n/n\to\infty\), set \(L_n=\log c_n\). The standard Pareto sum obeys \(n^{-1}\sum_iY_i-\log n=O_{\Pr}(1)\): truncate at \(n\) and use the variance bound in step 1; the excess above \(n\) is tight by the Poisson upper-tail bound and a further truncation at \(Mn\). For \(u\le\gamma_n\), exactly
\[
S_n(u)=-L_n+\left(n^{-1}\sum_iY_i-\log n-1\right)+\log u-R_n(u),
\quad R_n(u)=n^{-1}\sum_i(Y_i-\gamma_n/u)_+.
\tag{5}
\]
Let \(h(r)^2=\int_r^\infty u^2e^{-u}du\). Minkowski yields \(\|R_n\|_H\le n^{-1}\sum_iY_i h(\gamma_n/Y_i)\). For any fixed \(M>0\), the probability that \(\max_iY_i>Mn\) is at most \(1/M\). On the complement, the expectation of the upper bound is no more than
\[
\int_1^{Mn}\frac{h(\gamma_n/y)}y\,dy
=\int_{c_n/M}^{\gamma_n}\frac{h(r)}r\,dr\longrightarrow0.
\]
Thus \(\|R_n\|_H=o_{\Pr}(1)\). Since \(\log u\in H\) and the negligible region \(u>\gamma_n\) has exponentially small \(H\)-mass, (5) gives \(\|S_n\|_H^2/L_n^2\to\|1\|_H^2=2\) in probability. Identity (1) yields both supercritical conclusions; \(\log^2c_n/c_n\to0\).

**5. Why likelihood fitting does not change these regimes.** We now control the actual fitted statistic rather than merely asserting oracle equivalence. Let \(D_n(u)=n^{-1}\sum_i[\min(\widehat Y_i,\gamma_n/u)-\min(Y_i,\gamma_n/u)]\). On events of probability tending to one, \(\max_i|\log(\widehat Y_i/Y_i)|=O_{\Pr}((\log n)/\sqrt n)=o_{\Pr}(1)\), and the elementary truncated-exponential Lipschitz inequality implies
\[
|D_n(u)|\le 2\left(|\beta_n-1|F_n(u)+\beta_nm_n M_n(u)\right),
\]
where \(F_n(u)=n^{-1}\sum_iE_i\min(Y_i,\gamma_n/u)\) and \(M_n(u)=n^{-1}\sum_i\min(Y_i,\gamma_n/u)\). Exact exponential integration, including the \(\gamma_n/u<1\) tail, gives for \(\gamma_n\to\infty\):
\[
\begin{split}
\|F_n\|_H&=O_{\Pr}\left((1+\log\gamma_n)^2+
\sqrt{\gamma_n/n}(1+\log\gamma_n)\right),\\
\|M_n\|_H&=O_{\Pr}\left(1+\log\gamma_n+\sqrt{\gamma_n/n}\right).
\end{split}
\tag{6}
\]
Thus when \(\gamma_n/n\to0\), \(\sqrt{n/\gamma_n}\|D_n\|_H=o_{\Pr}(1)\), using \((\log\gamma_n)^2/\sqrt{\gamma_n}\to0\) and \(\log\gamma_n/\sqrt n\to0\). In the other two regimes a simpler uniform bound applies: the relative difference between every fitted and oracle \(Y_i\) is \(O_{\Pr}((\log n)/\sqrt n)\); because \(n^{-1}\sum_iY_i=O_{\Pr}(\log n)\),
\[
\|D_n\|_H=O_{\Pr}((\log n)^2/\sqrt n)=o_{\Pr}(1).
\]
The centering function \(\psi_0\) and the identity for \(t>1\) are identical in both cases. Therefore the fitted statistic inherits all three limits.

**6. Exact limit moments.** From \(K(u,u)=2/u\), \(\mathbb E\|G\|_H^2=2\). For \(Q=\|G\|_H^2\), Wick's rule gives \(\operatorname{Var}(Q)=2\iint u^2v^2e^{-(u+v)}K(u,v)^2du\,dv\); the change \(v=ut\) on \(u>v\) produces the stated one-dimensional integral. For the compensated-Poisson process the covariance is \(c_0 K\), while the fourth joint cumulant of \(Z_{c_0}(u),Z_{c_0}(u),Z_{c_0}(v),Z_{c_0}(v)\) equals
\[
c_0^3\left(\frac{2}{\max(u,v)^2\min(u,v)}
-\frac{2}{3\max(u,v)^3}\right).
\]
The Poisson product formula gives the Gaussian variance term plus \(c_0B\), with
\[
B=1-\frac83\int_0^1\frac{t^2}{(1+t)^3}\,dt
=\frac83(1-\log2)>0.
\]
All integrals are absolutely finite, as is seen directly from the displayed kernels and the exponential weight.

## Verification

Run `python check.py` with NumPy and SciPy installed. The checker independently evaluates the Pareto minCF by numerical integration, verifies exact truncated cross-moments, tests covariance and fourth-cumulant formulas, compares the derived variance constants to quadrature, and evaluates both oracle and fitted versions on reproducible samples. Its recorded run passed 68 assertions and produced \(\operatorname{Var}(Q)=6.70464997925077\) and \(B=0.81827418517348\) numerically. Finite computations check formulas but do not substitute for the probabilistic arguments above.

## Relationship to prior work

Meintanis, Milošević and Jiménez-Gamero (2023/2024) introduce precisely this minCF statistic and prove null asymptotics for a **fixed** positive exponential weighting parameter, together with MLE equivariance. Their fixed-weight \(V\)-statistic theorem does not imply uniformity under \(\gamma_n\to\infty\). Falk and Stupfler introduced the minCF and studied its empirical process. General truncated-heavy-tail Gaussian and Poisson regimes were investigated by Chakrabarty and Samorodnitsky, and by Tang and Han; those generic mechanisms are not claimed as new. The specific three-regime fitted Pareto **integrated quadratic** limit, its exact critical variance slope and the supercritical typical-value normalization are the present claims. Search limitations and closest-source comparisons are stated in the accompanying review.

## Limitations

The theorem assumes iid data, a correctly specified Pareto null, deterministic \(\gamma_n\), and the stated likelihood estimators. Critical values, rejection power, alternatives, data-driven tuning and joint validity over multiple tuning parameters are not derived. The Gaussian and Poisson limits are for an increasing bandwidth rate; the source's fixed-rate limit remains distinct. The exact \(\operatorname{Var}(W_{c_0})\) concerns the **limit random variable**, not a claim of convergence of finite-sample fourth moments under fitted Pareto data. The displayed asymptotics are supported by analytic proofs, not simulation extrapolation. Independent priority and mathematical audit have not been performed.

## References

1. S. G. Meintanis, B. Milošević and M. D. Jiménez-Gamero, *Goodness-of-Fit Tests Based on the Min-Characteristic Function*, arXiv:2310.12348, first posted 18 October 2023; *Computational Statistics & Data Analysis* **197** (2024), 107988. https://arxiv.org/abs/2310.12348 ; https://doi.org/10.1016/j.csda.2024.107988
2. M. Falk and G. Stupfler, *The Min-characteristic Function: Characterizing Distributions by Their Min-linear Projections*, *Sankhya A* **83** (2021), 254–282. https://doi.org/10.1007/s13171-019-00184-1
3. A. Chakrabarty and G. Samorodnitsky, *Understanding Heavy Tails in a Bounded World or, is a Truncated Heavy Tail Heavy or Not?*, *Stochastic Models* **28** (2012), 109–143. https://doi.org/10.1080/15326349.2012.646551
4. F. Tang and D. Han, *The asymptotic distribution of a truncated sample mean for the extremely heavy-tailed distributions*, *Communications in Statistics – Theory and Methods* **53** (2024), 5168–5185, first online 10 May 2023. https://doi.org/10.1080/03610926.2023.2209231
