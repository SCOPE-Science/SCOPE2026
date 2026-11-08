# A spectral threshold for time-average fluctuations under preferential relocation

## Finding

A confined process can have its equilibrium one-time distribution at **every** time and nevertheless have anomalously slow decay of time-average variance. For the uniform-past relocation model below, the time-average variance of any nonzero real generator eigenobservable has an **exact Beta-mixture formula** and a sharp three-phase transition at the point where the relocation rate equals the eigenvalue.

Let \(\lambda>0\), \(r\geq0\), \(a=\lambda+r\), and \(p=2r/(\lambda+r)\), so \(0\leq p<2\). Let \(v>0\) be the equilibrium variance of an eigenobservable \(f\). For \(t>0\), let \(B\sim\operatorname{Beta}(2-p,1+p)\). Then the variance of its continuous-time trajectory average is exactly

\[
\operatorname{Var}\left(\frac1t\int_0^t f(X_s)\,ds\right)
=\frac{v}{at}\,\mathbb E\left[\frac{1-e^{-atB}}{B}\right]
=v\,{}_2F_2\!\left(\begin{matrix}1,2-p\\2,3\end{matrix};-at\right).
\]

(The hypergeometric notation on the right is optional; the Beta expectation is the primary formula.) As \(t\to\infty\), this variance is asymptotic to

\[
\begin{cases}
\dfrac{2v}{(\lambda-r)t}, &0\leq r<\lambda,\\[5pt]
\dfrac{v}{\lambda}\dfrac{\log((\lambda+r)t)}{t}, &r=\lambda,\\[5pt]
\dfrac{2v}{(p-1)\Gamma(1+p)}[(\lambda+r)t]^{p-2}, &r>\lambda.
\end{cases}
\]

The constants in all three regimes are exact. For a thermal Ornstein–Uhlenbeck particle, \(dX_t=-\lambda X_t\,dt+\sqrt{2D}\,dW_t\), the choice \(f(x)=x\) gives \(v=D/\lambda\). In particular, the critical relocation rate is precisely the harmonic relaxation rate, although the one-time law remains the same Gaussian equilibrium law for every rate.

## Assumptions and scope

Let \((P_t)_{t\geq0}\) be a conservative Markov diffusion semigroup with invariant probability measure \(\pi\) and generator \(\mathcal L\). Suppose there is a real measurable \(f\) in the generator domain, square integrable under \(\pi\), with

\[
\mathcal L f=-\lambda f,\quad \lambda>0,\qquad
v=\int f^2\,d\pi\in(0,\infty).
\]

Invariance implies \(\int f\,d\pi=0\). Assume the usual martingale/Dynkin product identities hold for the observable and the additive integral, as they do for the displayed OU diffusion and for bounded eigenfunctions of regular compact-state diffusions.

Start \(X_0\sim\pi\). Between relocations evolve as the diffusion. At independent Poisson times of rate \(r\), at physical time \(t>0\), draw \(U\) uniformly from \([0,t]\), conditionally independently given the entire trajectory so far, and set \(X_t=X_{U}\). Past history is retained, not erased. The additive functional is \(J_t=\int_0^t f(X_s)\,ds\); relocations cost zero physical duration. All statements refer to ensemble variances of \(J_t/t\), not to a fluctuation limit in distribution.

The one-time marginal \(\pi\) is invariant at every finite time, but the complete path law is not stationary under time translations.

## Proof

**1. Exact one-time equilibrium.** The marginal law obeys the linear memory equation

\[
\partial_t\nu_t=\mathcal L^*\nu_t-r\nu_t+\frac r t\int_0^t\nu_u\,du.
\]

Since \(\mathcal L^*\pi=0\), the constant family \(\nu_t=\pi\) solves this equation with the prescribed initial marginal. Standard uniqueness of this linear Volterra evolution gives \(\nu_t=\pi\) for all \(t\). Consequently, \(\mathbb E[f(X_t)]=0\) and \(\mathbb E[f(X_t)^2]=v\) at every time.

**2. Closed two-moment system.** Put \(S(t)=\mathbb E[J_t^2]\) and \(C(t)=\mathbb E[J_t f(X_t)]\). As \(J_t\) is continuous and has derivative \(f(X_t)\) almost everywhere, \(S'(t)=2C(t)\). Between jumps, the generator contributes \(-\lambda C(t)\) to \(C'\), and the additive-integral product contributes \(v\). A relocation changes \(f(X_t)\) to \(f(X_U)\) but leaves \(J_t\) unchanged, with conditional mean \(t^{-1}\int_0^t f(X_u)du=J_t/t\). Its expected contribution is therefore \(r(S(t)/t-C(t))\). This proves

\[
C'(t)=v-(\lambda+r)C(t)+\frac rt S(t),\qquad
S''(t)+(\lambda+r)S'(t)-\frac{2r}{t}S(t)=2v.
\]

Initially \(S(0)=S'(0)=0\) and \(S(t)=vt^2+o(t^2)\). These conditions single out the regular solution.

**3. Exact solution without an uncontrolled closure.** Write \(a=\lambda+r\), \(p=2r/a\). A convergent power-series solution is

\[
S(t)=vt^2\sum_{n=0}^\infty
\frac{(2-p)_n}{(2)_n(3)_n}(-at)^n.
\]

The coefficient recurrence is obtained by substitution into the ODE: after setting the constant coefficient to \(1\), the \(n\)-th coefficient is \(-a(n+1-p)/[(n+1)(n+2)]\) times the preceding coefficient. It gives the unique solution regular at \(0\).

For \(B\sim\operatorname{Beta}(2-p,1+p)\), the Beta moment identity \(\mathbb E[B^n]=(2-p)_n/(3)_n\) and the exponential series yield

\[
\frac{vt}{a}\mathbb E\left[\frac{1-e^{-atB}}B\right]
=vt^2\sum_{n=0}^\infty \frac{(2-p)_n}{(2)_n(3)_n}(-at)^n.
\]

The interchange is justified at each fixed finite \(t\), since \((1-e^{-atB})/B\le at\), and exponential Taylor series converge absolutely and uniformly on \([0,1]\). Dividing by \(t^2\) establishes the exact result.

**4. Three sharp regimes.** Write \(L=at\), and set \(H(L)=\mathbb E[(1-e^{-LB})/B]\). For \(p<1\), the Beta inverse moment is finite and equals \(\mathbb E[B^{-1}]=2/(1-p)\); dominated convergence yields \(H(L)\to2/(1-p)\), and \(a(1-p)=\lambda-r\).

For \(p=1\), the Beta density is \(2(1-b)\) on \((0,1)\), so \(H(L)=2\log L+O(1)\). As \(a=2\lambda\), the critical coefficient follows.

For \(1<p<2\), the Beta density is

\[
\frac{2}{\Gamma(2-p)\Gamma(1+p)}b^{1-p}(1-b)^p.
\]

With \(y=Lb\), dominated convergence after splitting the integral at a small fixed endpoint gives

\[
L^{1-p}H(L)\longrightarrow
\frac{2}{\Gamma(2-p)\Gamma(1+p)}
\int_0^\infty y^{-p}(1-e^{-y})\,dy
=\frac{2}{(p-1)\Gamma(1+p)}.
\]

The last integral is \(\Gamma(2-p)/(p-1)\), by integration by parts. Substitution into \(\operatorname{Var}(J_t/t)=vH(at)/(at)\) completes all three limits.

## Verification

Run `python3 verify.py` in a standard Python 3 environment. The program independently evaluates the exact hypergeometric series, numerically integrates the closed moment ODE, checks the no-reset OU formula, and simulates finite-grid history relocations with a fixed seed. In the packaged replay, six ODE/series parameter comparisons, a no-reset calibration, and three Monte Carlo comparisons passed (16 assertions). The three simulated relative errors were approximately \(1.45\%\), \(2.00\%\), and \(3.45\%\), respectively.

These finite diagnostics do not prove any asymptotic statement; the Beta-integral argument above does. Numerical simulation discretizes time and is not an exact realization of the continuous-time model.

## Relationship to prior work

Boyer and Majumdar (2024, arXiv:2405.10283) derive the equilibrium one-time density and algebraic relaxation exponents for preferential relocation under confinement, including the harmonic case. Boyer, Evans and Majumdar (2024, arXiv:2411.00641) extend this one-time analysis to general memory kernels. Their full-text model descriptions and conclusions treat one-time marginals rather than the fluctuations of integrated eigenobservables. The present result uses the same model but a different observable: the complete physical-time integrated occupation of an eigenmode, obtaining an exact Beta formula and a critical variance transition. Boyer and Solis-Salas (2014, arXiv:1403.6069) introduced a related discrete-space preferential-relocation walk and developed displacement and visit statistics, not this confined additive-functional law. Stojkoski, Sandev, Kocarev and Pal (2021, arXiv:2107.11686) compute autocorrelations and time averages for canonical resetting to a fixed position. That renewal Markov model differs from relocation to a randomly selected past state, so its ordinary averaging conclusion does not imply the present nonrenewal three-phase variance law.

The variance transition may also be interpreted as a spectral Green–Kubo threshold, but no general independent central-limit or non-central-limit theorem is asserted. Independent verification of publication priority is still needed; broader spectral or reinforced-process results could imply part of the statement.

## Limitations

The finite-time identity assumes equilibrium initialization and a real generator eigenobservable. Nonstationary initial laws, nonlinear observables not satisfying a generator eigenrelation, arbitrary nonuniform memory kernels, higher cumulants, and limiting distributions of the time average are outside the theorem. All limits are for fixed finite \(r\), \(\lambda>0\), \(v>0\); the limit \(r\to\infty\) is not interchanged with \(t\to\infty\). The result determines second moments only and does not assert failure of mean-square ergodicity: the time-average variance still tends to zero in all three regimes.

## References

- D. Boyer and S. N. Majumdar, *Power-law relaxation of a confined diffusing particle subject to resetting with memory*, arXiv:2405.10283, first posted 2024-05-16. https://arxiv.org/abs/2405.10283
- D. Boyer, M. R. Evans and S. N. Majumdar, *Diffusion with preferential relocation in a confining potential*, arXiv:2411.00641, first posted 2024-11-01. https://arxiv.org/abs/2411.00641
- D. Boyer and C. Solis-Salas, *Random Walks with Preferential Relocations to Places Visited in the Past and their Application to Biology*, arXiv:1403.6069, first posted 2014-03-24. https://arxiv.org/abs/1403.6069
- V. Stojkoski, T. Sandev, L. Kocarev and A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686, first posted 2021-07-24. https://arxiv.org/abs/2107.11686
