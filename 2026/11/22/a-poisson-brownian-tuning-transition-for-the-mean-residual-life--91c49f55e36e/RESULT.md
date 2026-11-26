# A Poisson–Brownian tuning transition for the mean-residual-life exponentiality statistic

## Finding

Let \(X_1,\ldots,X_n\) be independent exponential observations with an arbitrary common positive rate. Put \(Y_i=X_i/\overline X_n\), so \(\sum_iY_i=n\), and define the mean-residual-life goodness-of-fit statistic of Baringhaus–Henze, in the equivalent representation of Ebner,
\[
T_{n,a}=n\int_0^\infty \left[\frac1n\sum_{i=1}^n(Y_i-y-1)\mathbf1_{\{Y_i>y\}}\right]^2 e^{-ay}\,dy,\qquad a>0.
\]
For **every deterministic sequence** \(a_n\to\infty\), let \(Q_n=a_n^2T_{n,a_n}\). The following three cases exhaust the possibilities whenever \(a_n/n\) converges:

1. If \(a_n/n\to0\), then
\[
Q_n\ \Longrightarrow\ Q_0:=\int_0^\infty B(u)^2e^{-u}\,du,
\]
where \(B\) is standard Brownian motion.
2. If \(a_n/n\to c\in(0,\infty)\), then
\[
Q_n\ \Longrightarrow\ Q_c:=c\int_0^\infty\bigl(\Pi(u/c)-u/c\bigr)^2e^{-u}\,du,
\]
where \(\Pi\) is a standard rate-one Poisson process. Its moments are exactly
\[
\mathbb E Q_c=1,\qquad \operatorname{Var}(Q_c)=1+\frac c2.
\]
3. If \(a_n/n\to\infty\), then \(Q_n\to0\) **in probability**, although
\[
\mathbb E Q_n\longrightarrow1.
\]
The last regime is a genuine failure of uniform integrability, not convergence in mean. For every fixed \(n\) and every fixed positive sample,
\[
\lim_{a\to\infty}a^3T_{n,a}=2n.
\]
Also \(\mathbb E Q_0=1\) and \(\operatorname{Var}(Q_0)=1\), and the limit family itself interpolates: \(Q_c\Rightarrow Q_0\) as \(c\downarrow0\), whereas \(Q_c\to0\) in probability as \(c\uparrow\infty\), despite its invariant mean and diverging variance. Thus \(a\asymp n\) is the exact boundary between Gaussian-process and Poisson-process null calibration for this published test.

## Assumptions and scope

The null is fully exponential with unknown scale fitted by the sample mean. The observations are independent, strictly positive and continuous, \(n\ge2\); the tuning sequence \(a_n\) is deterministic, positive and divergent. All limits above are null limits, not claims about power under alternatives. The first public version of the motivating 2022 paper was submitted September 12, 2022. Its primary mathematical classification is nonparametric goodness-of-fit, MSC2020 62G10.

## Proof

**1. Exact count-process reduction.** For a realized mean-normalized sample let
\[
N_n(y)=\sum_i\mathbf1_{\{Y_i\le y\}},\quad H_n(y)=\sum_i(Y_i-y-1)\mathbf1_{\{Y_i>y\}}.
\]
Using \(\sum_i(Y_i-1)=0\) and \(\sum_i(y-Y_i)_+=\int_0^yN_n(t)\,dt\), one obtains the exact pathwise identity
\[
H_n(y)=N_n(y)-ny+\int_0^yN_n(t)\,dt.
\]
The substitution \(u=ay\) therefore gives
\[
a^2T_{n,a}=\frac an\int_0^\infty H_n(u/a)^2e^{-u}\,du.\tag{1}
\]
No population-scale estimation is suppressed in this identity.

**2. Tightness of the exponential-weight tail.** Under the exponential null, \((Y_1/n,\ldots,Y_n/n)\) is Dirichlet with all shape parameters one. For \(0\le y\le n\), let \(r=(1-y/n)_+\), \(s=(1-2y/n)_+\). The exact one- and two-coordinate survivor probabilities are \(r^{n-1}\) and \(s^{n-1}\). As \(s\le r^2\), the coordinate threshold indicators are negatively correlated, yielding
\[
\operatorname{Var}N_n(y)\le \mathbb EN_n(y)\le n\min(y,1).
\]
A beta-integral also gives \(\mathbb EH_n(y)=-y(1-y/n)^{n-1}\) for \(y\le n\), and \(H_n(y)=0\) for \(y\ge n\). Minkowski's inequality applied to the count identity implies a universal \(C\) such that
\[
\mathbb EH_n(y)^2\le
\begin{cases}
Cny+y^2,&0\le y\le1,\\
Cn(1+y)^2+y^2,&y>1.
\end{cases}\tag{2}
\]
For \(a\to\infty\), multiplication by \(a/n\), substitution \(y=u/a\), and integration against \(e^{-u}\) show
\[
\lim_{M\to\infty}\limsup_{\substack{n\to\infty\\a\to\infty}}
\frac an\int_M^\infty\mathbb EH_n(u/a)^2e^{-u}\,du=0.
\tag{3}
\]
The contribution for \(u\le a\) is bounded by \(C\int_M^\infty(u+u^2/(na))e^{-u}du\); the contribution for \(u>a\) is \(O((a+1)e^{-a})\). This bound holds without any bound on \(a/n\).

**3. Critical Poisson window.** Write \(X_i\) as independent mean-one exponentials using scale invariance. Then \(\overline X_n\to1\) almost surely, and the point process \(\sum_i\delta_{nY_i}\) converges vaguely to a homogeneous rate-one Poisson point process: first apply the rare-event Poisson limit to \(nX_i\), then use the asymptotically unit random rescaling. Therefore, if \(a_n/n\to c>0\), on every compact interval of \(u\),
\[
N_n(u/a_n)\Rightarrow \Pi(u/c).
\]
The integration remainder satisfies \(\int_0^{u/a_n}N_n(t)dt=O_P(n^{-1})\), uniformly for compact \(u\), while \(nu/a_n\to u/c\). Equation (1), the integral continuous-mapping theorem away from the finitely many jump times, and tail bound (3) yield the stated \(Q_c\).

**4. Brownian local-count window.** If \(a_n\to\infty\) but \(n/a_n\to\infty\), the centered local count process for the original independent exponentials satisfies
\[
\sqrt{\frac{a_n}{n}}\left(\sum_i\mathbf1_{\{X_i\le u/a_n\}}-n(1-e^{-u/a_n})\right)\Rightarrow B(u)
\]
in the Skorokhod topology on each compact interval. To see this, put \(F(v)=1-e^{-v}\), use an infinite sequence of independent mean-one exponentials, and replace the first \(n\) observations by the first \(M_n\), where \(M_n\sim\mathrm{Poisson}(n)\) is independent of the sequence. The resulting count process in \(u\) has the law of a rate-one Poisson process at times \(nF(u/a_n)\). Put \(b_n=n/a_n\to\infty\). The centered rate-one Poisson process satisfies \((\Pi(b_n t)-b_n t)/\sqrt{b_n}\Rightarrow B(t)\); the deterministic time change \(nF(u/a_n)/b_n=a_nF(u/a_n)\) converges uniformly to \(u\) on compacts. With the same centering \(nF(u/a_n)\), the expected uniform difference between the two unscaled counts on \([0,M]\) is bounded by \(F(M/a_n)\mathbb E|M_n-n|\le (M/a_n)\sqrt n\), since only the observations in the differing prefix can contribute. Once multiplied by \(\sqrt{a_n/n}\), the bound tends to zero, proving the local limit for the fixed sample size.

Write \(s=\overline X_n\). The count based on the standardized data is the original count evaluated at \(us/a_n\). The continuous local functional limit and \(s\to1\) show that this time change leaves the centered limit unchanged on compacts; independence of \(s\) and the process is not needed. In the count identity the compensator at \(y=u/a_n\) is
\[
 n\left(F(sy)-y+\int_0^y F(st)\,dt\right)=n(1-1/s)F(sy).
\]
As \(F(sy)\le sy\) and \(s-1=O_P(n^{-1/2})\), its normalized uniform size on a compact \(u\)-interval is \(O_P(a_n^{-1/2})\). The centered integrated-count term, under the same normalization, is \(o_P(1)\) since its integrand is uniformly \(O_P(1)\) after normalization and the window has length \(O(a_n^{-1})\). Consequently \(\sqrt{a_n/n}\,H_n(u/a_n)\Rightarrow B(u)\) locally, and (1),(3) give \(Q_0\).

**5. Supercritical collapse.** If \(a_n/n\to\infty\), then for fixed \(M\), \(\mathbb P(N_n(M/a_n)>0)\le nM/a_n\to0\). On the complementary event, \(H_n(u/a_n)=-nu/a_n\) for every \(u\le M\). Its contribution to (1) is bounded by \((n/a_n)\int_0^M u^2e^{-u}du\to0\). Bound (3) controls the remainder. This proves convergence in probability to zero.

**6. Exact limiting moments and nonvanishing expected mass.** With \(Z_c(u)=\Pi(u/c)-u/c\), the Poisson cumulant formula gives
\[
\mathbb E Z_c(u)^2=u/c,\qquad
\operatorname{Cov}(Z_c(u)^2,Z_c(v)^2)
=2\frac{\min(u,v)^2}{c^2}+\frac{\min(u,v)}c.
\]
For independent unit exponentials \(E_1,E_2\), their minimum has first and second moments \(1/2\) and \(1/2\), giving \(\mathbb E Q_c=1\) and \(\operatorname{Var}Q_c=1+c/2\). Brownian Wick's formula gives the \(c=0\) values. The same martingale functional CLT applied to \(\sqrt c(\Pi(u/c)-u/c)\) as \(c\downarrow0\) yields \(Q_c\Rightarrow Q_0\); for \(c\uparrow\infty\), on each compact \(u\)-interval there is no Poisson jump with probability tending to one, giving convergence to zero, and the weighted-tail expectation is uniformly \(\int_M^\infty ue^{-u}du\).

To prove \(\mathbb EQ_n\to1\) for **every** divergent tuning sequence, use the Dirichlet survivor formulas to obtain the exact finite-sample moment
\[
\mathbb EH_n(y)^2=n\left[\frac{2n}{n+1}r^{n+1}-2r^n+r^{n-1}\right]
+n(n-1)\left[\frac n{n+1}s^{n+1}-2s^n+s^{n-1}\right].\tag{4}
\]
Here both powers with exponent \(n-1\) are valid for \(n=2\) as well. For \(0<y\le1/2\), \(1-r^{n-1}=y(1-1/n)+O(y^2)\) with an absolute error constant. Also \(r^2-s=y^2/n^2\), so \(|s^{n-1}-r^{2(n-1)}|\le (n-1)y^2/n^2\). Summing the single-indicator and distinct-pair contributions gives \(\operatorname{Var}N_n(y)=ny(1+O(y)+O(1/n))\). As \(\operatorname{Var}N_n(t)\le nt\), the centered integrated count has \(L^2\) norm at most \(\int_0^y\sqrt{nt}\,dt=(2/3)\sqrt n\,y^{3/2}\). Its variance and its cross term with the centered count sum to \(O(ny^2)\) in absolute value by Cauchy–Schwarz. As \(|\mathbb EH_n(y)|\le y\), (4) is consequently \(ny(1+o(1))\) in the joint limit \(n\to\infty\), \(y\downarrow0\). For each fixed \(u>0\), with \(y=u/a_n\), therefore \((a_n/n)\mathbb EH_n(u/a_n)^2\to u\). The domination in (2) on compact \(u\)-intervals and (3) on the tail permit integration, giving \(\mathbb EQ_n\to\int_0^\infty ue^{-u}du=1\). This proves escape of expectation in the supercritical regime.

Finally, for fixed \(n\) and a fixed strictly positive sample, \(H_n(y)=-ny\) below its positive minimum. The remainder beyond that minimum is exponentially negligible, so \(a^3T_{n,a}\to2n\).

## Verification

The included `verification.py` implements the pathwise count formula and integrates its piecewise quadratic-exponential segments independently of adaptive numerical quadrature. It checks these against each other for varied finite samples and checks the exact Dirichlet second-moment formula against Monte Carlo. Poisson/Wick integral identities are checked algebraically. The reproducibility script uses deterministic pseudorandom seeds; the stochastic runs are supplementary and do not constitute proof of any weak convergence. Execute with `python verification.py` with Python 3, NumPy, and SciPy.

## Relationship to prior work

Baringhaus and Henze (2008) introduced the weighted mean-residual-life exponentiality statistic. In addition to its fixed-tuning null limit, their Section 2 gives a sharper **fixed-sample** high-weight expansion governed by the sample minimum. The displayed limit \(a^3T_{n,a}\to2n\) at fixed \(n\) is a consequence of that expansion and is included for comparison, not claimed as new. Ebner (first public preprint September 12, 2022, arXiv:2209.05153) gives the exactly equivalent representation used here and proves a **fixed-tuning** Gaussian-process null limit, with fixed-alternative and local-Bahadur analyses; its Section 5 leaves data-adaptive tuning open. The present theorem holds along diverging deterministic \(a_n\) and captures an order-\(n\) Poisson transition, the explicit limiting variance \(1+c/2\), and failure of uniform integrability above the threshold. General local empirical-process Poisson/Gaussian convergence is classical (e.g., Einmahl, 1997) and is **not** claimed as new; establishing the weighted integral remainder, fitted-scale effect, moment formula and escape of mass is the statistic-specific content.

## Limitations

The theorem addresses null calibration and does not imply a choice of tuning optimizing power, adaptive tuning validity, or fixed-alternative efficiency. The Poisson and Brownian limits require deterministic divergent tuning; only sequences with convergent \(a_n/n\) are classified. The critical law is given as a Poisson-process functional, not a closed-form CDF. Weak convergence does not imply moment convergence in the supercritical regime; here the mean limit is established separately. Historical-priority uncertainty remains concerning generic weighted-local-process theorems and inaccessible earlier full-text sources; no claim of independent expert validation is made.

## References

1. Baringhaus, L., and Henze, N. (2008). A new weighted integral goodness-of-fit statistic for exponentiality. *Statistics & Probability Letters* 78, 1006–1016. DOI:10.1016/j.spl.2007.09.060. Accepted manuscript: https://hal.science/hal-00616538v1.
2. Ebner, B. (2022, first public preprint September 12). *The test of exponentiality based on the mean residual life function revisited*. arXiv:2209.05153, https://arxiv.org/abs/2209.05153. Journal of Nonparametric Statistics 35 (2023), 601–621. DOI:10.1080/10485252.2023.2178831.
3. Einmahl, J. H. J. (1997). Poisson and Gaussian approximation of weighted local empirical processes. *Stochastic Processes and Their Applications* 70, 31–58. DOI:10.1016/S0304-4149(97)00055-0.
