# Opposite correlation optima and a sharp antithetic accuracy scale for stochastic-gradient Leimkuhler–Matthews sampling

## Finding

**Theorem.** Consider the scalar stochastic-gradient Leimkuhler–Matthews (SGLM) step
\[
Z_{k+1}=r Z_k-h\xi_k+\sqrt{h/2}\,(\chi_k+\chi_{k+1}),\qquad r=1-\kappa h,
\]
where \(\kappa>0\), \(\sigma^2>0\), \(0<\kappa h<2\), and \(-1<\rho<1\). The Gaussian sequence \(\chi_k\) is iid standard normal. Independently, \(\xi_k\) is a centered stationary Gaussian AR(1) sequence with \(\operatorname{Cov}(\xi_j,\xi_k)=\sigma^2\rho^{|j-k|}\). Its unique stationary position distribution is \(N(0,V_h(\rho))\), with
\[
V_h(\rho)=\frac1\kappa+\frac{h^2\sigma^2}{1-r^2}\frac{1+r\rho}{1-r\rho}.
\]
For the stationary linear-observable sample mean, define \(L_h(\rho)=\lim_{N\to\infty}N\operatorname{Var}\big(N^{-1}\sum_{k=0}^{N-1}Z_k\big)\). Then
\[
L_h(\rho)=\frac{2}{\kappa^2h}+\frac{\sigma^2}{\kappa^2}\frac{1+\rho}{1-\rho}.
\]
The map \(\rho\mapsto L_h(\rho)\) is strictly increasing for every admissible step. Both \(V_h(\rho)\) and the Wasserstein-2 distance between the stationary distribution and \(N(0,\kappa^{-1})\) are strictly increasing if \(0<\kappa h<1\), constant if \(\kappa h=1\), and strictly decreasing if \(1<\kappa h<2\). Thus for \(1<\kappa h<2\), *every two distinct correlation choices reverse their strict ordering* for invariant-law accuracy versus sample-mean efficiency. Indeed \(L_h(\rho)\to\infty\) as \(\rho\uparrow1\) while \(V_h(\rho)\downarrow\kappa^{-1}+h^2\sigma^2/(1-r)^2\).

For fixed \(\kappa,\sigma^2\) and an arbitrary admissible step-dependent \(\rho_h\),
\[
V_h(\rho_h)-\kappa^{-1}=O(h^2)\quad\Longleftrightarrow\quad1+\rho_h=O(h)\quad(h\downarrow0).
\]
In particular, when \(1+\rho_h\sim c h\) for some \(c>0\),
\[
V_h(\rho_h)-\kappa^{-1}\sim\frac{\sigma^2(\kappa+c)}{4\kappa}h^2.
\]
For any *fixed* \(\rho>-1\), the excess variance instead has leading order \(\frac{\sigma^2}{2\kappa}\frac{1+\rho}{1-\rho}h\). The second-order condition concerns the entire colored-oracle covariance, not a change to the intrinsic thermal increments.

For example, let \(\kappa=\sigma^2=1\) and \(h=3/2\). At \(\rho=1/2\), \((V_h,L_h)=(14/5,13/3)\); at \(\rho=-1/2\), \((V_h,L_h)=(6,5/3)\). Positive persistence improves Gaussian invariant accuracy but increases long-run uncertainty of the linear sample mean.

## Assumptions and scope

The target density is proportional to \(\exp(-\kappa z^2/2)\); its variance is \(\kappa^{-1}\). The gradient used at step \(k\) is \(\kappa Z_k+\xi_k\). The error is generated externally: its dynamics do not depend on the position and its driving noise is independent of all thermal noises. A stationary realization is \(\xi_{k+1}=\rho\xi_k+\sigma\sqrt{1-\rho^2}\,\eta_{k+1}\), with iid standard Gaussian \(\eta_k\) independent of the iid thermal sequence \(\chi_k\). This does not assume statistical independence of \(Z_k\) and \(\xi_k\): in stationarity the position depends on past errors that are correlated with the current error. Only \(-1<\rho<1\) is allowed; boundary correlations appear solely as limits. The joint state \((Z_k,\xi_k,\chi_k)\) is taken in its unique stationary law when evaluating variances, which exists because its linear transition eigenvalues \(r,\rho,0\) all have modulus less than one. The long-run coefficient concerns the linear observable \(z\), not nonlinear sample means.

## Proof

Write \(t=\sqrt{h/2}\), \(C=\operatorname{Cov}(Z_k,\xi_k)\), and \(B=\operatorname{Cov}(Z_k,\chi_k)\) under stationarity. Since the current Gaussian increment enters the previous update only through \(t\chi_k\), \(B=t\). Independence of the thermal and oracle innovation streams implies \(\operatorname{Cov}(\chi_k,\xi_k)=0\). Covarying the position recurrence at time \(k-1\) with the AR(1) recurrence gives
\[
C=\rho r C-\rho h\sigma^2=-\frac{h\rho\sigma^2}{1-r\rho}.
\]
Taking variances in the position update yields
\[
(1-r^2)V=h^2\sigma^2+2t^2+2rtB-2rh C
=h(1+r)+h^2\sigma^2\frac{1+r\rho}{1-r\rho}.
\]
As \(1-r^2=\kappa h(1+r)\), this proves the asserted stationary variance. Strict positivity of the excess follows from \(|r\rho|<1\); hence the one-dimensional Gaussian Wasserstein distance is exactly \(\sqrt{V}-\kappa^{-1/2}\), monotone in \(V\).

Summing the recurrence and using \(1-r=\kappa h\) gives the *exact* finite-sum identity
\[
\kappa h\sum_{k=0}^{N-1}Z_k=Z_0-Z_N-h\sum_{k=0}^{N-1}\xi_k+t\bigl(\chi_0+\chi_N+2\sum_{k=1}^{N-1}\chi_k\bigr).
\]
The stationary Gaussian linear process has absolutely summable autocovariances and bounded second moments. Hence the endpoint term contributes zero after the \(N\)-scaled variance limit (including its cross-covariances by Cauchy–Schwarz). The two innovation streams are independent, so the asymptotic numerator variances add. The AR(1) integrated autocovariance equals \(\sigma^2(1+\rho)/(1-\rho)\), while the thermal sum has variance asymptotic to \(4t^2N=2hN\). Dividing by \(\kappa^2h^2\) proves \(L_h\).

At fixed \(h\),
\[
\frac{\partial V}{\partial\rho}=\frac{2r h^2\sigma^2}{(1-r^2)(1-r\rho)^2},\qquad
\frac{\partial L}{\partial\rho}=\frac{2\sigma^2}{\kappa^2(1-\rho)^2}>0.
\]
The first sign is exactly \(\operatorname{sgn}(1-\kappa h)\), proving the sharp reversal and the non-domination claim. The \(\rho\uparrow1\) limit of the variance is obtained from the displayed fraction; the integrated covariance diverges like \(2\sigma^2/[\kappa^2(1-\rho)]\).

Finally set \(\delta_h=1+\rho_h\in(0,2)\). For sufficiently small \(h\), \(r=1-\kappa h>0\) and
\[
\frac{1+r\rho_h}{1-r\rho_h}=
\frac{\kappa h+r\delta_h}{2-\kappa h-r\delta_h}.
\]
Because \(h^2/(1-r^2)\asymp h\), an \(O(h^2)\) variance error requires the displayed ratio to be \(O(h)\). Its denominator is at most \(2\), so \(\kappa h+r\delta_h=O(h)\) and hence \(\delta_h=O(h)\). Conversely, that condition makes numerator \(O(h)\) and denominator \(2+O(h)\), giving the same order for the ratio and \(O(h^2)\) for the error. When \(\delta_h\sim ch\), substitution gives the stated sharp asymptotic coefficient. Fixed \(\rho>-1\) yields the separate first-order coefficient. This proves every claim.

## Verification

The standalone Python 3 script `sglm_ar1_checker.py` uses only `fractions.Fraction` and exact Gaussian elimination. It constructs the three-state Markov transition for \((Z_k,\xi_k,t\chi_k)\), solves all nine rational Lyapunov equations independently of the moment proof, and evaluates the zero-frequency spectral variance through the innovation covariance. It checks 2,567 exact-rational assertions across stable steps, both correlation signs and small-step choices. Run `python3 sglm_ar1_checker.py`. The proof, rather than the finite checks, establishes the universal quantifiers and asymptotics.

## Relationship to prior work

Ye, Wang, Lin and Kong introduce SGLM and prove general error bounds and numerical bias expansions for *fresh independent gradient estimates*. Their earlier publicly available version also specifies the same adjacent-Gaussian update. The present theorem instead fixes a correlated AR(1) oracle while keeping its one-step variance constant and simultaneously compares *two different long-run quality criteria*. The new sharp sign threshold arises from the numerical multiplier \(1-\kappa h\). Earlier analysis of SGLD bias and variance by Vollmer, Zygalakis and Teh uses a different independent-gradient Euler scheme. More general linear-filter and Green–Kubo formulas supply standard proof tools, but do not themselves state this SGLM-specific correlation-design classification or its quadratic-accuracy scaling. Related published mathematical findings on midpoint constraints, stochastic Runge–Kutta samplers and correlated stochastic optimization use different update operators and goals.

## Limitations

The gradient error is an externally prescribed AR(1) Gaussian process without feedback from the position, not necessarily a realizable minibatch-index law or a conditionally unbiased fresh sample. The conditions of published independent-minibatch bounds do **not** automatically apply. The theorem is scalar and quadratic, and covers the linear-observable asymptotic variance and Gaussian-target Wasserstein-2 distance only. It does not provide a guarantee for nonlinear targets, arbitrary state-dependent gradients, time-dependent step schedules or finite-length empirical accuracy. Endpoints \(\rho=\pm1\) are excluded; claims about these are limiting statements. This result establishes no runtime improvement.

## References

1. X. Ye and Y. Wang, *Stochastic Gradient Leimkuhler–Matthews Integrator with Second Order Discretization Error*, original public preprint (11 October 2026), https://ai.vixra.org/abs/2610.0030 (v1).
2. X. Ye, Y. Wang, G. Lin and C. X. Kong, *Stochastic Gradient Leimkuhler–Matthews Integrator with Second Order Discretization Error*, arXiv:2610.24781v1 (17 October 2026), https://arxiv.org/abs/2610.24781.
3. S. J. Vollmer, K. C. Zygalakis and Y. W. Teh, *Exploration of the (Non-)Asymptotic Bias and Variance of Stochastic Gradient Langevin Dynamics*, JMLR 17(159), 2016, https://jmlr.org/papers/v17/15-494.html.
