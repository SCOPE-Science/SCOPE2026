# A moving-symmetry two-clock law for rapid-reset Brownian interval coverage

## Finding

A reflected Brownian searcher covers a finite interval by visiting its two endpoints, while Poisson resets return it to a prescribed site **without erasing endpoint visits**. A narrow reset-location window of order \(\sqrt{D/r}\) around the midpoint produces a non-exponential, tunable limit for the *full cover-time distribution*. In that window the limiting cover time is the maximum of two independent, unequally rated exponential clocks.

Fix \(L,D>0\) and \(\delta\in\mathbb R\). For sufficiently large \(r>0\), let the starting and resetting position be
\[
z_r=\frac L2+\delta\sqrt{\frac Dr},\qquad s_r=\frac L2\sqrt{\frac rD},\qquad \theta_r=r e^{-s_r}.
\]
Let \(T_r\) be the first time **both** endpoints have been visited, with endpoint-visit history retained through every reset. Then
\[
\boxed{\quad \theta_r T_r\ \Longrightarrow\ \max(E_+,E_-),\quad E_+\sim\operatorname{Exp}(e^\delta),\quad E_-\sim\operatorname{Exp}(e^{-\delta})\quad}
\]
where \(E_+\) and \(E_-\) are independent. Equivalently, for every \(t\ge0\),
\[
\boxed{\lim_{r\to\infty}\Pr(\theta_rT_r>t)=e^{-e^\delta t}+e^{-e^{-\delta}t}-e^{-2\cosh(\delta)t}.}
\]
For **every real \(q>0\)**, the \(q\)-th moment also converges to that of this limiting maximum. In particular,
\[
\lim_{r\to\infty}\theta_r\mathbb ET_r=2\cosh\delta-\frac1{2\cosh\delta},
\]
\[
\lim_{r\to\infty}\theta_r^2\mathbb ET_r^2
=4\cosh(2\delta)-\frac1{2\cosh^2\delta}.
\]
At exact symmetry \(\delta=0\), the limiting mean, variance, and coefficient of variation are \(3/2\), \(5/4\), and \(\sqrt5/3\), respectively. The \(3/2\) mean constant is known in earlier research; the result assessed here is the **whole moving-site distributional crossover and its moment control**, not that previously known constant.

## Assumptions and scope

The motion is standard one-dimensional Brownian diffusion reflected at both ends of \([0,L]\), with generator \(D\partial_{xx}\) (so free variance rate \(2D\)). The initial state is \(z_r\), and an independent Poisson clock of rate \(r\) instantaneously resets position to \(z_r\), with no refractory period. The indicator of whether each endpoint has ever been visited survives resets. Every \(\delta\in\mathbb R\) is fixed as \(r\to\infty\); the formula for \(z_r\) is used only for sufficiently large rates for which it belongs to the interval. No simultaneous-resets coupling of separate particles is assumed.

## Proof

**1. Three exact nonreset passage transforms.** Let \(\tau_+\), \(\tau_-\), and \(\tau_{\pm}\) be the first hits, under *nonreset* reflected Brownian motion started at \(z\), of the right endpoint, the left endpoint, and either endpoint, respectively. The solutions of \(Df''=qf\) with Dirichlet boundary at a target and Neumann at the other reflected end are
\[
\begin{aligned}
F_+(q;z)&=\mathbb E_z e^{-q\tau_+}=\frac{\cosh(\sqrt{q/D}\,z)}{\cosh(\sqrt{q/D}\,L)},\\
F_-(q;z)&=\mathbb E_z e^{-q\tau_-}=\frac{\cosh(\sqrt{q/D}\,(L-z))}{\cosh(\sqrt{q/D}\,L)},\\
F_{\pm}(q;z)&=\mathbb E_z e^{-q\tau_{\pm}}=\frac{\cosh(\sqrt{q/D}\,(z-L/2))}{\cosh(\sqrt{q/D}\,L/2)}.
\end{aligned}
\]
For the either-end event, both endpoints are absorbing; this explains its different denominator. All transforms are positive for real \(q>0\).

**2. Exact reset-renewal resolvent.** Let \(\tau_{j,r}\) denote the first reset-process hit of target event \(j\in\{+,-,\pm\}\), and \(S_{j,r}(t)=\Pr(\tau_{j,r}>t)\). Renewal at the first reset gives, for \(u\ge0\),
\[
\widehat S_{j,r}(u)=\int_0^\infty e^{-ut}S_{j,r}(t)\,dt
=\frac{1-F_j(r+u;z_r)}{u+r F_j(r+u;z_r)}.
\]
This identity comes directly from \(\widehat S_0(r+u)=[1-F_j(r+u)]/(r+u)\) and the geometric reset renewal \(\widehat S_r=\widehat S_0/(1-r\widehat S_0)\). Because both endpoint visits are remembered, \(T_r=\max(\tau_{+,r},\tau_{-,r})\) **pathwise** and its survivor function is exactly
\[
S_{T_r}(t)=S_{+,r}(t)+S_{-,r}(t)-S_{\pm,r}(t).
\]
The intersection of the events that the left and right endpoints remain unvisited is exactly the event that neither endpoint has yet been visited. Independence of the finite-rate hitting times is neither assumed nor true in general.

**3. Singular scaling of the three rates.** Write \(s=s_r\) and \(\kappa=\sqrt{r/D}\), so \(\kappa z_r=s+\delta\), \(\kappa(L-z_r)=s-\delta\) and \(\kappa(z_r-L/2)=\delta\). For any fixed \(u\ge0\), \(\sqrt{(r+u\theta_r)/D}=\kappa[1+O(e^{-s})]\), and elementary \(\cosh\)-asymptotics yield
\[
\begin{aligned}
e^sF_+(r+u\theta_r;z_r)&\longrightarrow e^\delta,\\
e^sF_-(r+u\theta_r;z_r)&\longrightarrow e^{-\delta},\\
e^sF_{\pm}(r+u\theta_r;z_r)&\longrightarrow 2\cosh\delta.
\end{aligned}
\]
For example, \(\cosh(s+\delta)/\cosh(2s)\sim e^{-s+\delta}\). The numerator of the renewal resolvent tends to one, while its denominator divided by \(\theta_r\) tends to \(u+\lambda_j\), where \(\lambda_+=e^\delta\), \(\lambda_-=e^{-\delta}\) and \(\lambda_{\pm}=\lambda_++\lambda_-\). Hence
\[
\theta_r\widehat S_{j,r}(u\theta_r)\longrightarrow\frac{1}{u+\lambda_j}.
\]
Equivalently \(\mathbb E e^{-u\theta_r\tau_{j,r}}=1-u\theta_r\widehat S_{j,r}(u\theta_r)\to\lambda_j/(u+\lambda_j)\), the exponential Laplace transform. By continuity of Laplace transforms, each scaled first-passage time converges in law to its stated exponential. Therefore the three survival probabilities converge pointwise to \(e^{-\lambda_j t}\) for all \(t\ge0\). Substituting into the **exact** survivor inclusion–exclusion identity gives the asserted cover-time limit. Since \(\lambda_{\pm}=\lambda_++\lambda_-\), this is precisely the survival function of the maximum of independent exponentials with rates \(\lambda_+\) and \(\lambda_-\). This establishes a distributional identity in the limit, **not** finite-rate independence.

**4. Uniform integrability and moment convergence.** Fix \(0<\varepsilon<\min(e^\delta,e^{-\delta})\). The same asymptotics apply to \(F_j(r-\varepsilon\theta_r;z_r)\), and show that for either single-target event
\[
rF_j(r-\varepsilon\theta_r;z_r)>\varepsilon\theta_r
\]
for all sufficiently large \(r\). Thus the geometrically renewed single-target hitting time has a finite positive exponential moment at \(\varepsilon\theta_r\). Indeed the discounted weight of an unsuccessful reset cycle is
\[
\int_0^\infty r e^{-(r-\varepsilon\theta_r)t}\Pr(\tau_j>t)dt
=\frac{r[1-F_j(r-\varepsilon\theta_r;z_r)]}{r-\varepsilon\theta_r}<1.
\]
The renewal geometric series converges, and the continuation of Step 2 to \(u=-\varepsilon\theta_r\) gives
\[
\mathbb E e^{\varepsilon\theta_r\tau_{j,r}}
=1+\varepsilon\theta_r\frac{1-F_j(r-\varepsilon\theta_r;z_r)}{rF_j(r-\varepsilon\theta_r;z_r)-\varepsilon\theta_r}
\longrightarrow\frac{\lambda_j}{\lambda_j-\varepsilon}.
\]
Since \(e^{\varepsilon\theta_rT_r}\le e^{\varepsilon\theta_r\tau_{+,r}}+e^{\varepsilon\theta_r\tau_{-,r}}\), these exponential moments are uniformly bounded. Every positive power is uniformly integrable, proving moment convergence for all \(q>0\). Integration of the three limiting exponentials gives the stated first and second moments and the symmetric coefficient of variation.

## Verification

Run the standalone `verify.py` using Python 3, without third-party dependencies. It independently evaluates the three boundary-value passage transforms and their rate derivatives, the exact finite-rate renewal resolvents, the previously published arbitrary-site mean expression, all reflection symmetries, the asymptotic amplitudes, and the two leading moments across several sites and rates. It reports 222 deterministic passed tests. These finite checks corroborate the formulas but are not a proof of infinite-rate convergence; Steps 1–4 provide the analytic argument.

## Relationship to prior work

Linn and Lawley (2024) give arbitrary-site mean cover-time formulas and frequent-reset moment bounds; they explicitly identify the \(3/2\) symmetric **mean** prefactor and the farthest-target-dominated asymmetric case. These results are not new here. Their bounds and fixed-distance comparisons do not give the family of **distributional** limits as the site moves \(O(r^{-1/2})\) from symmetry, nor the associated entire family of moment limits. Ghosh and Sabhapandit (2026) calculate the exact midpoint cover-time law and transform; the \(\delta=0\) case is therefore an asymptotic consequence of prior exact formulas and is not asserted as an independent new distributional formula. The new assessed mathematical content is the **nonconstant detuning parameter \(\delta\)** and a sharp continuum of competing-clock laws with uniform-integrability control. Existing exact resetting renewal transforms and elementary asymptotic analysis are credited as essential proof ingredients.

Two related published interval-reset studies determine an exact all-site finite-rate cover-time variance and a mean-location versus tail-rate optimization conflict. They use the same Brownian model but neither establishes this near-midpoint high-reset law, and their fixed-rate design conclusions do not imply the displayed scaling distribution. A 2023 cover-time thesis discusses endpoint-hit ordering and search-location effects but was not found to state this detuned scaling limit.

## Limitations

The theorem is asymptotic as the Poisson reset rate tends to infinity, with fixed detuning \(\delta\). It is not an exact finite-rate independence theorem and does not characterize the joint hitting-time process at all times. The motion has perfect reflecting endpoints, instantaneous full position resets, retained endpoint-visit memory, and fixed positive diffusivity and interval length. No error bound uniform over all unbounded \(\delta\), no non-Poisson renewal resetting, no imperfect target detection, and no optimization claim is established. The explicit finite-rate cover-time distribution at exact midpoint and the symmetric mean prefactor belong to prior work. The key novelty is subject to independent publication-priority verification, particularly for unindexed extensions of high-reset multi-target rare-event theory. No independent scientific audit has been performed.

## References

1. A. Ghosh and S. Sabhapandit, *Cover time statistics of one-dimensional Brownian motion under stochastic resetting*, arXiv:2605.31207v1, first publicly submitted 2026-05-29, https://arxiv.org/abs/2605.31207 .
2. S. Linn and S. D. Lawley, *Cover times with stochastic resetting*, arXiv:2406.12154, first publicly submitted 2024-06-17, https://arxiv.org/abs/2406.12154 .
3. *Exact cover-time variance and a mean–risk conflict in Brownian resetting* (2026), published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-cover-time-variance-and-a-mean-risk-conflict-in-brownian-r--98d226a79bdc .
4. *Exact mean–tail reset-location conflict in Brownian interval coverage* (2026), published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-mean-tail-reset-location-conflict-in-brownian-interval-cov--c9ad586108f6 .
5. Y. Maziya, *The coupon collector's problem, the cover time problem, and the first passage time problem*, doctoral thesis, 2023, https://spiral.imperial.ac.uk/entities/publication/df647a5d-b775-4d1b-8e40-e6fdbf83e219 .
