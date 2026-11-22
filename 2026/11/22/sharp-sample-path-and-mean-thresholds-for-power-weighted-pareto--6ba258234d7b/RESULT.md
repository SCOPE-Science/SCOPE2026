# Sharp sample-path and mean thresholds for power-weighted Pareto min-characteristic discrepancies

## Finding

Let \(X_1,\ldots,X_n\) be independent Pareto type-I observations with known shape \(\alpha>0\), unit lower endpoint, and \(\Pr(X_i>x)=x^{-\alpha}\) for \(x\ge1\). For \(t>0\), put \(\Psi_n(t)=n^{-1}\sum_{i=1}^n\min\{1,tX_i\}\), \(\Psi_\alpha(t)=\mathbb E_\alpha\min\{1,tX_1\}\), and, for \(\beta>0\), define the possibly extended-real statistic

\[
T_{n,\beta}=n\int_0^1\bigl(\Psi_n(t)-\Psi_\alpha(t)\bigr)^2\,t^{-1-\beta}\,dt.
\]

For **every fixed integer \(n\ge1\)** the following sharp classifications hold:

\[
\Pr(T_{n,\beta}<\infty)=1\quad\Longleftrightarrow\quad 0<\beta<2\min\{\alpha,1\},
\]

\[
\mathbb E_\alpha T_{n,\beta}<\infty\quad\Longleftrightarrow\quad 0<\beta<\min\{\alpha,2\}.
\]

In the finite-mean range, the exact expectation is independent of sample size:

\[
\boxed{\mathbb E_\alpha T_{n,\beta}=\frac{2\alpha}{(\alpha-\beta)(2\alpha-\beta)(2-\beta)(\alpha+1-\beta)}.}
\]

Thus for every \(0<\alpha<2\) there is a nonempty interval
\(\min\{\alpha,2\}\le\beta<2\min\{\alpha,1\}\) of **almost surely finite statistics with infinite null expectation**. For \(\alpha\ge2\) the two finiteness thresholds coincide.

The finite-mean boundary has three different sharp divergences, with \(\beta\) increasing to its upper limit:

\[
\mathbb E_\alpha T_{n,\beta}\sim
\begin{cases}
\dfrac{2}{(2-\alpha)(\alpha-\beta)},&0<\alpha<2,\\[4pt]
\dfrac{2}{(2-\beta)^2},&\alpha=2,\\[4pt]
\dfrac{\alpha}{(\alpha-1)^2(\alpha-2)(2-\beta)},&\alpha>2.
\end{cases}
\]

The sample-path divergence at the other boundary is likewise exact. With \(\overline X_n=n^{-1}\sum_iX_i\), as \(\beta\) increases to \(2\min\{\alpha,1\}\),

\[
T_{n,\beta}\sim
\begin{cases}
\dfrac{n}{(1-\alpha)^2(2\alpha-\beta)},&0<\alpha<1,\\[4pt]
\dfrac{2n}{(2-\beta)^3},&\alpha=1,\\[4pt]
\dfrac{n(\overline X_n-\alpha/(\alpha-1))^2}{2-\beta},&\alpha>1,
\end{cases}
\quad\text{almost surely}.
\]

For \(0<\beta<\min\{\alpha,2\}\), also \(T_{n,\beta}\) converges in distribution, as \(n\to\infty\), to the squared norm of a centered Gaussian element in \(L^2((0,1),t^{-1-\beta}dt)\). The covariance operator is positive and trace-class, with trace equal to the boxed formula. No claim of an explicit eigenvalue list is made.

## Assumptions and scope

The Pareto law is fully specified, including both shape and lower endpoint; neither parameter is estimated or fitted. All statements are for \(n\ge1\), \(\alpha>0\), and \(\beta>0\); the statistic is permitted to equal \(+\infty\). The restriction to \((0,1)\) is exact, not a cutoff approximation: both min-characteristic functions equal one for \(t\ge1\). No general alternative-distribution power statement or composite-null calibration is asserted.

## Proof

**1. Exact first and second truncated moments.** For \(p>0\), \(0<t<1\), set \(M_p(t)=\mathbb E_\alpha[\min(1,tX_1)^p]\). Splitting the Pareto integral at \(1/t\) gives

\[
M_p(t)=\alpha t^p\int_1^{1/t}x^{p-\alpha-1}\,dx+t^\alpha
=\begin{cases}
\dfrac{p t^\alpha-\alpha t^p}{p-\alpha},&p\ne\alpha,\\[4pt]
t^p\bigl(1+p\log(1/t)\bigr),&p=\alpha.
\end{cases}
\]

Consequently \(\Psi_\alpha=M_1\) and \(\operatorname{Var}(\min\{1,tX_1\})=M_2(t)-M_1(t)^2\).

**2. Exact expectation and its sharp domain.** By Tonelli's theorem and independent summands,

\[
\mathbb E_\alpha T_{n,\beta}
=\int_0^1\bigl(M_2(t)-M_1(t)^2\bigr)t^{-1-\beta}\,dt
\quad\text{in }[0,\infty].
\]

For \(0<\alpha<2\), this variance is asymptotic to \(2t^\alpha/(2-\alpha)\) as \(t\downarrow0\), including \(\alpha=1\). For \(\alpha=2\) it is asymptotic to \(2t^2\log(1/t)\), and for \(\alpha>2\) to \(\operatorname{Var}(X_1)t^2\), where \(\operatorname{Var}(X_1)=\alpha/((\alpha-1)^2(\alpha-2))\). These positive equivalents prove finiteness **if and only if** \(\beta<\min\{\alpha,2\}\), including equality divergence. Within that domain, integrate the powers (and, at \(\alpha=1,2\), logarithmic terms) using \(\int_0^1t^{q-1}dt=1/q\) and \(\int_0^1t^{q-1}(\log t)^kdt=(-1)^kk!/q^{k+1}\). Algebraic cancellation yields

\[
\int_0^1(M_2-M_1^2)t^{-1-\beta}dt
=\frac{2\alpha}{(\alpha-\beta)(2\alpha-\beta)(2-\beta)(\alpha+1-\beta)}.
\]

Taking the relevant one-sided limits in this rational formula proves the three mean blow-up equivalents.

**3. Sample-path finiteness.** With probability one, \(X_{(n)}=\max_iX_i<\infty\). For \(0<t<1/X_{(n)}\), every empirical minimum is unsaturated, so \(\Psi_n(t)=t\overline X_n\) exactly. If \(0<\alpha<1\), the population min-characteristic function has \(\Psi_\alpha(t)\sim t^\alpha/(1-\alpha)\), giving \(\Psi_n(t)-\Psi_\alpha(t)\sim-t^\alpha/(1-\alpha)\). If \(\alpha=1\), \(\Psi_\alpha(t)=t(1-\log t)\) and the difference is \(t(\overline X_n-1+\log t)\). If \(\alpha>1\), \(\Psi_\alpha(t)=\alpha t/(\alpha-1)+O(t^\alpha)\); its difference from \(t\overline X_n\) is \(t(\overline X_n-\alpha/(\alpha-1))+o(t)\). The random coefficient in the latter expression is nonzero almost surely because the sample mean has an absolutely continuous distribution. Squaring the three equivalents and comparing with the improper power integral proves the exact pathwise thresholds, including their equality cases. Abelian integration at each threshold gives the three stated sample-path blow-up constants. The integral away from zero is bounded for every sample realization, since the two min-characteristic functions lie in \([0,1]\).

**4. Gaussian quadratic limit in the integrable regime.** Let \(H=L^2((0,1),t^{-1-\beta}dt)\), and define the centered random element \(Z(t)=\min\{1,tX_1\}-\Psi_\alpha(t)\). The preceding Tonelli identity gives \(\mathbb E\|Z\|_H^2=\mathbb ET_{n,\beta}<\infty\), and \(\mathbb EZ=0\) in \(H\). As \(H\) is separable, the iid Hilbert-space central limit theorem implies \(n^{-1/2}\sum_i Z_i\) converges weakly to a centered Gaussian element \(G\in H\). The continuous norm-square map proves \(T_{n,\beta}\Rightarrow\|G\|_H^2\). The Gaussian covariance operator is trace-class with trace \(\mathbb E\|Z\|_H^2\), as claimed. This argument does not assert a comparable result in the infinite-mean range.

## Verification

The standalone `check.py` uses only the Python standard library. Run `python check.py` from its containing directory. It checks 36 exact rational identities obtained by integrating the truncated-moment expressions, seven independent Simpson-integral comparisons, 30 direct Pareto-density integral checks, and 10 positivity checks (83 total). The analytic arguments, not these finite checks, establish the unbounded-parameter and almost-sure assertions.

## Relationship to prior work

Falk and Stupfler introduced the min-characteristic function and gave its exact Pareto form and compact-domain empirical-process convergence. Meintanis, Milošević, and Jiménez-Gamero introduced weighted min-characteristic goodness-of-fit statistics, using exponential weights and a general limit theorem requiring \(\int_0^\infty w(t)dt<\infty\). The present power weights \(t^{-1-\beta}\) are nonintegrable at zero and therefore outside that hypothesis. The known min-characteristic function itself, the generic Hilbert-space CLT, and usual Pareto moment criteria are not presented as new. The proposed contribution is the joint **exact** sample-path/expectation phase diagram, its rational trace and its distinct boundary blow-up laws for the specifically defined simple-null statistic.

## Limitations

No claim is made for estimated Pareto parameters, composite-null tests, other positive distributions, alternative-hypothesis power, or explicit Gaussian covariance eigenvalues. Existing broad weighted-process or fractional-distance theory might imply some partial criteria upon specialization, and historical priority of the complete formula is not independently certified. The checks use exact algebra on a finite rational grid and numerical integration; they are not an exhaustive verification of all real parameters. In the a.s.-finite but infinite-mean window, these results **do not** establish that no other non-Gaussian scaling limit exists.

## References

1. Falk, M., and Stupfler, G. (2019, online). *The min-characteristic function: characterizing distributions by their min-linear projections.* Sankhya A 83, 254–282 (2021). DOI: https://doi.org/10.1007/s13171-019-00184-1. Full author-posted text: https://www.researchgate.net/publication/337496693_The_Min-characteristic_Function_Characterizing_Distributions_by_Their_Min-linear_Projections.
2. Meintanis, S. G., Milošević, B., and Jiménez-Gamero, M. D. (2023, preprint first posted October 18). *Goodness-of-fit tests based on the min-characteristic function.* arXiv:2310.12348, https://arxiv.org/abs/2310.12348; subsequently published in *Computational Statistics & Data Analysis* 197 (2024), article 107988, https://doi.org/10.1016/j.csda.2024.107988.
