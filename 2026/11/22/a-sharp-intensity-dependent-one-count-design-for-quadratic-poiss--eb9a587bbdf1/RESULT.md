# A sharp intensity-dependent one-count design for quadratic Poisson-path energy

## Finding
Let \(N=(N_t)_{0\le t\le1}\) be a homogeneous Poisson counting process of known intensity \(\lambda>0\). The nonlinear path energy is
\[
Q=\int_0^1N_t^2\,dt.
\]
For exactly one preselected, noiseless count observation \(K=N_x\), at \(x\in[0,1]\), estimate \(Q\) under mean-square loss by its conditional mean. For every intensity \(\lambda>0\), the **unique globally optimal observation time** \(x_\lambda\) is the unique zero in \((2/3,\sqrt{3/5})\) of
\[
\begin{aligned}
0=P_\lambda(x)={}&27x^2-72x+36\\
&+\lambda(176x^3-360x^2+72x+72)\\
&+\lambda^2(20x^4-72x^2+36).
\end{aligned}
\]
Moreover \(x_\lambda\) increases strictly with \(\lambda\) and approaches the endpoints according to
\[
x_\lambda=\frac23+\frac{82}{243}\lambda+O(\lambda^2)
\quad(\lambda\downarrow0),
\]
\[
x_\lambda=\sqrt{\frac35}+\frac{37/20-\sqrt{15}/2}{\lambda}+O(\lambda^{-2})
\quad(\lambda\to\infty).
\]
At large intensity, the optimal asymptotic risk coefficient is
\[
\lim_{\lambda\to\infty}\frac{\inf_x\mathbb E[(Q-\mathbb E[Q\mid N_x])^2]}{\lambda^3}
=\frac8{15}-\frac{16\sqrt{15}}{125}\approx0.03759146502.
\]
By comparison, observation at the classical intensity-independent linear-integral design time \(x=2/3\) has coefficient \(542/10935\approx0.04956561500\). Thus the optimally positioned one-count observation reduces this high-intensity Bayes risk by \(24.1581789704\ldots\%\).

## Assumptions and scope
A process realization has a finite number of unit jumps on \([0,1]\) almost surely, with known homogeneous rate \(\lambda>0\), no observation noise, and one deterministic observation time \(x\) selected before the process is realized. An estimator may be *any* square-integrable measurable function of the observed count \(K=N_x\). The conditional expectation minimizes its mean-square loss; there are no estimator-class restrictions beyond measurability and square integrability. The objective averages over the Poisson law. At \(x=0\), the count is identically zero; all formulas below use their continuous endpoint extension. Neither adaptive observation nor unknown-rate inference is included.

Write \(\widehat Q_x=\mathbb E[Q\mid N_x]\) and \(R_\lambda(x)=\mathbb E[(Q-\widehat Q_x)^2]\). Then the conditional expectation is a computable quadratic polynomial in the observed integer \(k\):
\[
\widehat Q_x(k)=\left(1-\frac{2x}{3}\right)k^2
+\left(\frac{x}{6}+\lambda(1-x)^2\right)k
+\frac{\lambda(1-x)^2}{2}+\frac{\lambda^2(1-x)^3}{3}.
\]
The unconditional target variance and the *exact finite-intensity risk* are
\[
\begin{split}
\operatorname{Var}Q&=\frac{\lambda}{3}+\frac{7\lambda^2}{6}+\frac{8\lambda^3}{15},\\
R_\lambda(x)&=\operatorname{Var}Q-V_\lambda(x),\\
V_\lambda(x)&=\frac{\lambda x}{36}\left\{
\lambda^2(4x^4-24x^2+36)\\
&\qquad+\lambda(44x^3-120x^2+36x+72)
+9x^2-36x+36\right\}.
\end{split}
\]
Here \(V_\lambda(x)=\operatorname{Var}(\widehat Q_x)\) is the explained variance.

## Proof
**1. The Bayes estimator.** Condition on \(N_x=k\). For \(0\le t\le x\), the bridge count is binomial \(N_t\mid N_x=k\sim\mathrm{Bin}(k,t/x)\), so
\[
\mathbb E[N_t^2\mid N_x=k]=k\frac tx\left(1-\frac tx\right)+k^2\frac{t^2}{x^2}.
\]
For \(x\le t\le1\), independent increments give \(N_t=k+Z\), with \(Z\sim\mathrm{Pois}(\lambda(t-x))\), whence
\[
\mathbb E[N_t^2\mid N_x=k]=k^2+2k\lambda(t-x)+\lambda(t-x)+\lambda^2(t-x)^2.
\]
Integrating these two expressions proves the displayed \(\widehat Q_x\). Orthogonality of conditional expectation proves that this estimator is optimal for fixed \(x\).

**2. Explained and total variances.** Set \(m=\lambda x\) and \(A=1-2x/3\), \(B=x/6+\lambda(1-x)^2\). The Poisson moments give
\[
\operatorname{Var}(K^2)=4m^3+6m^2+m,\qquad
\operatorname{Cov}(K^2,K)=2m^2+m.
\]
Because additive constants do not affect variance,
\[
V_\lambda(x)=A^2(4m^3+6m^2+m)+B^2m+2AB(2m^2+m).
\]
Algebraic expansion gives the polynomial in the scope section. Independently, for \(0\le s\le t\le1\), write \(N_t=N_s+Z\) with independent Poisson increments. This gives
\[
\operatorname{Cov}(N_s^2,N_t^2)=4\lambda^3s^2t+\lambda^2(4s^2+2st)+\lambda s.
\]
Twice integrating on the lower triangle of the unit square gives the stated \(\operatorname{Var}Q\). The conditional-variance identity \(R_\lambda(x)=\operatorname{Var}Q-\operatorname{Var}(\widehat Q_x)\) establishes the risk formula.

**3. Sharp uniqueness.** Differentiate the displayed polynomial:
\[
V_\lambda'(x)=\frac{\lambda}{36}P_\lambda(x),\qquad
P_\lambda=P_0+\lambda P_1+\lambda^2P_2,
\]
with
\[
\begin{split}
P_0(x)&=27(x-2/3)(x-2),\\
P_1(x)&=176x^3-360x^2+72x+72,\\
P_2(x)&=20(x^2-3/5)(x^2-3).
\end{split}
\]
On \([0,2/3]\), \(P_0\ge0\) and \(P_2>0\), while \(P_1>0\). For an explicit positivity certificate, setting \(x=2u/3\), \(u\in[0,1]\), the cubic \(P_1(2u/3)\) has degree-three Bernstein coefficients \(72,88,152/3,328/27\), all positive. Consequently \(P_\lambda>0\) on \([0,2/3]\) for \(\lambda>0\).

Let \(s=\sqrt{3/5}\). On \([s,1]\), \(P_0<0\), \(P_2\le0\), and \(P_1<0\): indeed \(P_1'(x)=528x^2-720x+72<0\) on \([2/3,1]\) and \(P_1(s)=-144+888\sqrt{15}/25<0\). Hence \(P_\lambda<0\) on \([s,1]\). On the intervening interval \([2/3,s]\), all three derivatives \(P_0',P_1',P_2'\) are strictly negative, so \(P_\lambda\) is strictly decreasing and crosses zero exactly once. Therefore \(V_\lambda\) increases strictly up to \(x_\lambda\) and decreases strictly thereafter, proving global uniqueness of the risk minimizer on the entire closed interval.

**4. Intensity monotonicity.** At the interior zero, \(P_0(x_\lambda)<0\) and \(P_2(x_\lambda)>0\). Implicit differentiation gives
\[
\frac{dx_\lambda}{d\lambda}=-\frac{P_1(x_\lambda)+2\lambda P_2(x_\lambda)}{P_\lambda'(x_\lambda)}.
\]
The denominator is negative. If \(P_1(x_\lambda)\ge0\), the numerator is positive directly. If \(P_1(x_\lambda)<0\), the root identity gives \(P_1+2\lambda P_2=-P_1-2P_0/\lambda>0\). Thus \(dx_\lambda/d\lambda>0\). At \(\lambda\downarrow0\), the interior root tends to the relevant zero \(2/3\) of \(P_0\); at \(\lambda\to\infty\), it tends to the zero \(s\) of \(P_2\). Ordinary simple-root implicit expansions yield the two displayed asymptotic corrections.

**5. Sharp large-intensity comparison.** The coefficient of \(\lambda^3\) in \(V_\lambda(x)\) is \(x(x^2-3)^2/9\). Its unique maximizing point in \([0,1]\) is \(s\). Subtracting the maximal coefficient from \(8/15\) yields \(8/15-16\sqrt{15}/125\), while substituting \(2/3\) yields \(542/10935\). Their ratio proves the stated risk reduction. This is an asymptotic comparison for \(\lambda\to\infty\), not a universal finite-intensity percentage.

## Verification
Run `python3 verification/verify.py` in an environment with Python 3 and SymPy (see `verification/requirements.txt`). It reconstructs the conditional-moment integrals for 96 exact rational parameter-count triples, checks symbolic variance and derivative identities and asymptotic constants, checks 7 finite-intensity root cases, and uses an independent seeded jump-time simulation to cross-check the explained-variance identity. A captured output is in `verification/verification_output.txt`. The analytic calculations in the proof establish the results for **all** \(\lambda>0\); finite root checks and Monte Carlo are supplemental, not exhaustive proof.

## Relationship to prior work
Samaniego's 1976 theorem and Cressie's 1978 full-text treatment optimize sampling for the **linear** path integral \(\int_0^1X_t\,dt\) of processes with stationary independent increments, giving the single-site optimum \(2/3\). Cressie's formulas explicitly use first-order conditional moments and linear-integral covariance, not \(\int N_t^2\,dt\). Our nonlinear target produces an intensity-dependent optimal time, strictly different from \(2/3\) for every positive rate.

Przybyłowicz (2017, first publicly posted January 28) establishes globally optimal finite-information approximation of jump-diffusion *trajectories* using Poisson and Wiener observations, in a different information/cost setting. Przybyłowicz, Sobieraj and Stępień (2021) treat pointwise approximation of SDE solutions with Poisson random measures and randomized Euler schemes. Their inspected primary material does not imply the single-count Bayes design for quadratic Poisson energy. Published Poisson-path random-stratum quadrature work addresses the **linear** counting-path integral with many random samples and coupling-dependent variance, not the one exact count nonlinear conditional estimator here. Beentjes' specialist paper on Poisson-bridge variance-reduction simulations was available only by abstract during this comparison; it remains a priority uncertainty, not evidence of coverage. These differences are claims about inspected material, not a proof of historical uniqueness.

## Limitations
The theorem assumes homogeneous known intensity, the specific quadratic integrated count functional, exactly one error-free ex ante count observation, and unconditional squared loss. It does not give the optimal design for unknown rates, multiple observations, noise, adaptive rules, different path powers or general jump diffusions. The high-rate percentage is an asymptotic value. Independent literature review and historical-priority verification have not been performed.

## References
- F. J. Samaniego (1976), *The optimal sampling design for estimating the integral of a process with stationary independent increments*, IEEE Transactions on Information Theory 22(3), 375–376, https://doi.org/10.1109/TIT.1976.1055551 .
- N. Cressie (1978), *Estimation of the integral of a stochastic process*, Bulletin of the Australian Mathematical Society 18, 83–93, https://doi.org/10.1017/S0004972700007838 .
- P. Przybyłowicz (2017), *Optimal sampling design for global approximation of jump diffusion SDEs*, arXiv:1701.08311, first posted 2017-01-28, https://arxiv.org/abs/1701.08311 .
- P. Przybyłowicz, M. Sobieraj and Ł. Stępień (2021), *Efficient approximation of SDEs driven by countably dimensional Wiener process and Poisson random measure*, arXiv:2108.02394, first posted 2021-08-05, https://arxiv.org/abs/2108.02394 .
- C. H. L. Beentjes (2021), *Optimising Poisson bridge constructions for variance reduction methods*, https://doi.org/10.1515/mcma-2021-2090 .
