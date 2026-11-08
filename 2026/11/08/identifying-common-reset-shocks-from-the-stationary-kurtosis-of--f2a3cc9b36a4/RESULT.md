# Identifying common reset shocks from the stationary kurtosis of a diffusing-diffusivity tracer

## Finding
Consider a Brownian tracer and its stochastic diffusivity with three independent Poisson reset clocks: position-only, diffusivity-only, and common position-and-diffusivity resets. For prescribed positive marginal reset intensities, the stationary diffusivity distribution and tracer variance are **independent of the common reset intensity**, but the tracer kurtosis increases strictly with that intensity and identifies it exactly.

More precisely, fix \(\Lambda>0\), position-only intensity \(r_x\ge0\), diffusivity-only intensity \(r_\omega\ge0\), and common intensity \(c\ge0\). Put
\[
R=r_x+c>0,\qquad Q=r_\omega+c>0.
\]
The unique stationary law has moments
\[
\mathbb E[\Omega^2]=\frac{2\Lambda^2}{Q},\qquad
\mathbb E[X^2]=\frac{4\Lambda^2}{RQ},\qquad
\mathbb E[X^4]=\frac{96\Lambda^4(6R+Q)}{R^2Q^2(R+Q-c)}.
\]
Consequently its ordinary (non-excess) kurtosis is
\[
K=\frac{\mathbb E[X^4]}{(\mathbb E[X^2])^2}
=\frac{6(6R+Q)}{R+Q-c}.
\]
Furthermore, for every time lag \(t\ge0\) the entire stationary second-order two-time covariance matrix is
\[
\operatorname{Cov}\big((X_0,\Omega_0),(X_t,\Omega_t)\big)
=\begin{pmatrix}
\dfrac{4\Lambda^2}{RQ}e^{-Rt}&0\\[3pt]
0&\dfrac{2\Lambda^2}{Q}e^{-Qt}
\end{pmatrix}.
\]
Thus even observing all two-time covariances of both variables cannot distinguish the common-clock coupling at fixed \(R,Q\). Fourth-order position moments can.

For **every** fixed \(R,Q>0\), the admissible coupling intensities are precisely \(0\le c\le\min\{R,Q\}\); the **sharp attainable kurtosis interval** is
\[
\frac{6(6R+Q)}{R+Q}\le K\le
\frac{6(6R+Q)}{\max\{R,Q\}},
\]
with equality only at \(c=0\) and \(c=\min\{R,Q\}\), respectively. Every intermediate value has exactly one realization in this three-clock family. If \(\Lambda\) is known, the three exact stationary statistics \(m_\omega=\mathbb E[\Omega^2]\), \(m_x=\mathbb E[X^2]\), and \(K\) recover all rates uniquely:
\[
Q=\frac{2\Lambda^2}{m_\omega},\qquad
R=\frac{2m_\omega}{m_x},\qquad
c=R+Q-\frac{6(6R+Q)}{K},\quad
r_x=R-c,\quad r_\omega=Q-c.
\]
These formulas plus the displayed kurtosis interval are a necessary and sufficient realizability test for any positive triplet \((m_\omega,m_x,K)\) in the specified family.

In particular, at equal total reset intensities \(R=Q=\gamma>0\), \(K=42\gamma/(2\gamma-c)\). Completely independent reset clocks (\(c=0\)) and completely synchronized reset clocks (\(c=\gamma\)) have identical \(\Omega\)-marginals and identical \(\mathbb E[X^2]=4\Lambda^2/\gamma^2\), but \(K=21\) versus \(K=42\). Their fourth moments therefore differ **by exactly a factor of two** despite matching the aforementioned lower-order observations.

## Assumptions and scope
Between jump times, the real-valued process solves the Itô equations
\[
dX_t=\sqrt2\,\Omega_t\,dW_t,\qquad d\Omega_t=\sqrt2\,\Lambda\,dB_t,
\]
where \(W,B\) are independent standard Brownian motions, independent of three independent homogeneous Poisson clocks. At a position-only event set \(X=0\) and preserve \(\Omega\); at a diffusivity-only event set \(\Omega=0\) and preserve \(X\); at a common event set both to zero. Every clock may have zero intensity, provided \(R,Q>0\). The physical instantaneous diffusivity is \(\Omega_t^2\), so the sign of \(\Omega\) does not change the conditional tracer variance. Moments refer to the unique stationary law, not to an initial-value transient. Kurtosis is ordinary kurtosis, not excess kurtosis.

## Proof
**Stationarity and finite moments.** In a two-sided stationary construction the \(\Omega\) process is Brownian motion restarted at zero by the union of the diffusivity-only and common clocks, a Poisson process of positive intensity \(Q\). Its stationary distribution is centered Laplace with density
\[
f_\Omega(w)=\frac{\sqrt Q}{2\Lambda}\exp\!\left(-\frac{\sqrt Q\,|w|}{\Lambda}\right).
\]
Given the stationary entire past of \(\Omega\), the position at time zero is the Itô integral from its last position-reset epoch to zero, with respect to independent \(W\). Its position-reset age is finite almost surely because \(R>0\). Coupling copies using identical future clocks and Brownian increments first erases all initial \(\Omega\) values at a diffusivity reset and then erases all initial \(X\) values at a subsequent position reset. This proves uniqueness. Exponential tails of reset ages and the finite Gaussian moments of Brownian increments give finite stationary mixed moments through fourth order (and in fact of every fixed polynomial order).

**Moment equations.** The generator on smooth polynomial test functions is
\[
\mathcal L f=\Lambda^2 f_{\omega\omega}+\omega^2 f_{xx}
+r_x[f(0,\omega)-f(x,\omega)]
+r_\omega[f(x,0)-f(x,\omega)]
+c[f(0,0)-f(x,\omega)].
\]
Let \(A=\mathbb E[\Omega^2]\), \(B_4=\mathbb E[\Omega^4]\), \(C=\mathbb E[X^2]\), \(H=\mathbb E[X^2\Omega^2]\), and \(J=\mathbb E[X^4]\). Stationarity applied successively to \(\omega^2,\omega^4,x^2,x^2\omega^2,x^4\) yields
\[
QA=2\Lambda^2,\qquad QB_4=12\Lambda^2A,\qquad
RC=2A,\qquad (R+Q-c)H=2B_4+2\Lambda^2C,\qquad RJ=12H.
\]
The mixed-moment reset loss is \(r_x+r_\omega+c=R+Q-c\), because a common event annihilates the product **once**, not twice. Solving this triangular system gives
\[
H=\frac{8\Lambda^4(6R+Q)}{RQ^2(R+Q-c)},
\qquad J=\frac{96\Lambda^4(6R+Q)}{R^2Q^2(R+Q-c)},
\]
and hence the stated moments and kurtosis.

**Second-order time-series indistinguishability.** The generator also obeys \(\mathcal Lx=-Rx\) and \(\mathcal L\omega=-Q\omega\). Hence \(\mathbb E[X_t\mid X_0,\Omega_0]=e^{-Rt}X_0\) and \(\mathbb E[\Omega_t\mid X_0,\Omega_0]=e^{-Qt}\Omega_0\). By symmetry of the driving Brownian noise \(W\), \(\mathbb E[X_0\Omega_0]=0\). The lagged covariance matrix follows from conditioning, including vanishing off-diagonal entries. This establishes the stronger second-order nonidentifiability assertion with no Gaussian approximation. In particular, exponential lag decay can reveal \(R,Q\) without prior knowledge of \(\Lambda\); at known \(R,Q\), the fourth-order kurtosis alone then identifies \(c\).

**Strict ordering and inverse problem.** At fixed positive \(R,Q\), nonnegative individual clock intensities are equivalent to \(0\le c\le\min(R,Q)\). The derivative
\[
\frac{\partial K}{\partial c}=\frac{6(6R+Q)}{(R+Q-c)^2}>0
\]
is strict across the entire closed admissible interval, yielding sharp endpoint values and unique inversion. The formulas for \(R\) and \(Q\) follow from the second moments. The inverse \(c\) lies in the admissible interval if and only if the measured \(K\) satisfies the stated bounds; subtracting it from \(R,Q\) gives nonnegative individual rates. Conversely those reconstructed rates define the stated process, whose calculated moments are exactly the observed triplet. For \(R=Q=\gamma\), direct substitution yields the explicit \(21\)-to-\(42\) example.

**Independent stochastic-integral check.** Let \(T\) be the backward time since the last position reset and \(V=\int_{-T}^{0}\Omega_s^2\,ds\). Conditioned on the complete \(\Omega\) path and the reset clocks, \(X\) is Gaussian with variance \(2V\); thus \(\mathbb E[X^4]=12\mathbb E[V^2]\). On an interval conditioned to contain no position resets, the internal \(\Omega\) resets at the *exclusive* rate \(q=Q-c\), while its starting law is the full-rate \(Q\) stationary law. With the usual continuous limit at \(q=0\), an independent Poisson-survival calculation gives
\[
\mathbb E[V^2]=\frac2R\int_0^\infty e^{-Rs}\left[
 e^{-qs}\,\mathbb E[\Omega^4]
 +2\Lambda^2\frac{1-e^{-qs}}{q}\,\mathbb E[\Omega^2]
\right]ds
=\frac{8\Lambda^4(6R+Q)}{R^2Q^2(R+Q-c)}.
\]
This reproduces the fourth moment without using its generator equation.

## Verification
The self-contained \(\texttt{checker.py}\) reproduces the five exact generator identities with symbolic algebra, checks the derivative and endpoint identities, independently numerically integrates the Poisson-survival representation at 72 parameter settings, and verifies exact rational inversion and feasibility across a finite parameter grid. It reports 680 integral and rational assertions in addition to the symbolic assertions. The analytical proof establishes all parameter values; finite diagnostics are not claimed as an exhaustive proof.

Run with \(\texttt{python checker.py}\) using Python 3, SymPy and mpmath. No external data, network access, random sampling, or nonincluded artifacts are needed.

## Relationship to prior work
Santra, Basu and Sabhapandit (arXiv:2205.00549, first public May 1, 2022) study the same stochastic-diffusivity Brownian equations with a **single common reset clock** that restarts both position and diffusivity. Their main stationary position laws, tails and dimensional analysis are prior work. Their conclusion explicitly identifies position-only and diffusivity-only resetting as extensions to explore; it does not specify the shared/independent-clock kurtosis interpolation or its exact inverse. The synchronized endpoint here is consistent with that model, and its stationary second/fourth moments can also be obtained from their known renewal characteristic function. The novelty claim is the nontrivial dependence on the **overlap intensity** when marginal rates are held fixed, the sharp feasible interval, and unique identification of the overlap intensity.

Kuśmierz and Gudowska-Nowak (arXiv:1812.08489) distinguish complete and position-only resets in **subdiffusive continuous-time random walks**, using a power-law waiting-time mechanism rather than Brownian-squared diffusivity with an additional independent internal reset clock. Their underlying propagator and mean-squared-displacement results do not imply this stationary fourth-moment clock-coupling law. Zhan and Wang (Physical Review E 109, 044115, 2024) give general diffusivity-correlation criteria for ergodicity, not a published three-clock kurtosis formula in the accessible abstract. Olsen (arXiv:2310.04840, 2023) derives exact steady-state moment recurrences when complete system memory is erased and the reset location follows a distribution; those assumptions do not encompass clocks that separately reset position or stochastic volatility. A broader unindexed result on correlated reset clocks remains an originality risk.

## Limitations
The theorem concerns exact stationary moments of this specified Markov jump diffusion, not an arbitrary volatility process or a finite-sample estimator. Its parameter identification assumes that \(\Lambda\) is known and that stationary diffusivity variance and tracer second/fourth moments are observable exactly. If only \(X\) is observed and \(\Lambda\) or reset totals are unknown, the stated three-statistic identification is not asserted. The result does not provide full stationary tracer densities for partially overlapping clocks, detailed-balance properties, or a statistical detection error bound. Independent scientific validation has not been performed.

## References
1. I. Santra, U. Basu and S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient*, arXiv:2205.00549 (first public 2022-05-01), https://arxiv.org/abs/2205.00549.
2. Ł. Kuśmierz and E. Gudowska-Nowak, *On subdiffusive continuous time random walks with stochastic resetting*, arXiv:1812.08489 (first public 2018-12-20), https://arxiv.org/abs/1812.08489.
3. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (first public 2023-10-07), https://arxiv.org/abs/2310.04840.
4. Z. Zhan and X. Wang, *Ergodic criterion of a random diffusivity model*, Physical Review E 109, 044115 (2024), https://doi.org/10.1103/PhysRevE.109.044115 (abstract consulted; full article not accessible in this review).
