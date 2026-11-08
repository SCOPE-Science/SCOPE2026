# A stationary autocovariance identifies an arbitrary refractory clock in partial Brownian resetting

## Finding

A stationary two-time covariance uniquely determines the **entire distribution of otherwise unobserved refractory periods** in a partially reset Brownian diffusion, although its stationary one-time law cannot distinguish refractory distributions having the same mean. A universal, isolated Laplace-frequency crossing provides an additional exact model signature.

Let \(C(t)=\mathbb E[X_0X_t]\) and \(\widehat C(s)=\int_0^\infty e^{-st}C(t)\,dt\), \(s>0\). The known physical parameters are diffusivity \(D>0\), exploration reset rate \(r>0\), and partial-reset factor \(0<a<1\). The unknown refractory duration \(T\) has an arbitrary probability distribution \(W\) on \([0,\infty)\), with finite strictly positive mean \(m=\mathbb E T\). Write

\[
Q=\frac{2D}{r(1-a^2)},\qquad w(s)=\mathbb E[e^{-sT}].
\]

The stationary variance gives the unknown mean: with \(b=C(0)/Q\),

\[
 a^2<b<1,\qquad m=\frac{1-b}{r(b-a^2)}.
\]

For \(s>0\), put

\[
G(s)=\frac{1+rm}{Q}\widehat C(s),\qquad H(s)=G(s)-\frac{a^2rm}{s}.
\]

**Inverse theorem.** Every \(s>0\) other than \(s=ar\) satisfies the exact inversion

\[
\boxed{w(s)=1-\frac{s^2\{1-[s+r(1-a)]H(s)\}}{ar\{s^2H(s)-s+ar(1-a)\}}.}
\]

The apparent singularity at \(s=ar\) is removable by continuity. Hence the complete function \(C(t)\), \(t\ge0\), determines \(W\) uniquely by uniqueness of Laplace transforms, with no finite-mixture or density hypothesis on \(W\).

**Universal blind frequency.** For every refractory distribution with the same mean \(m\),

\[
\boxed{\widehat C(ar)=\frac{Q}{1+rm}\left(\frac1r+am\right).}
\]

More precisely, for two laws \(W_1,W_2\) of the same mean, with Laplace transforms \(w_1,w_2\),

\[
\boxed{\widehat C_1(s)-\widehat C_2(s)=
\frac{Q}{1+rm}\frac{ar^2(1-a)^2(ar-s)[w_1(s)-w_2(s)]}
{s^2[s+r-arw_1(s)][s+r-arw_2(s)]}.}
\]

For the nonidentical deterministic duration \(T=m\) and exponential duration of mean \(m\), the covariances in Laplace space cross **exactly once**, at \(s=ar\): the exponential-duration transform is strictly larger below this point and strictly smaller above it. Thus the blind frequency does not imply observational equivalence across all frequencies.

## Assumptions and scope

The particle diffuses as \(dX_t=\sqrt{2D}\,dB_t\) only during exploration intervals, which end at independent exponential waiting times of rate \(r\). At the end of each exploration interval the instantaneous jump is \(X\mapsto aX\), followed by an independent idle refractory duration \(T\sim W\) in which the position is frozen; exploration then resumes. All Brownian increments, exploration durations, and refractory durations are independent. The stationary process is considered. Its mean is zero and second moments are finite. The parameters \(a,r,D\) are calibrated and known; \(W\), including its mean, is unknown. We require \(0<a<1\) and \(0<m<\infty\), allowing both atoms and continuous components, including an atom at zero.

## Proof

**Stationarity and phase variances.** At the starts of successive exploration intervals, the positions satisfy a contracting random affine recursion \(Z_{n+1}=a(Z_n+\sqrt{2D E_n}\,\xi_n)\), where \(E_n\sim\operatorname{Exp}(r)\), the \(\xi_n\) are standard normal, and the terms are independent. The contraction \(0<a<1\) gives a unique centered invariant distribution of finite variance; with finite mean cycle duration \(r^{-1}+m\), its stationary time version exists. Renewal-reward gives exploration occupancy \(p_E=(1+rm)^{-1}\) and refractory occupancy \(p_R=rm/(1+rm)\). Memorylessness of the exploration clock and independence of refractory duration from position show that the position variance conditional on exploring is

\[
Q=\frac{2D}{r(1-a^2)},
\]

and conditional on refractory phase is \(a^2Q\). Indeed the stationary mean-square balance over an exploration cycle is \(rQ=2D+ra^2Q\); the refractory position is the just-reset value. Therefore

\[
C(0)=\frac{Q(1+a^2rm)}{1+rm}.
\]

The stated strict interval for \(b\) and inversion for \(m\) follow by algebra.

**Two-time covariance reduction.** Let \(N_t\) be the number of multiplicative jumps between times zero and \(t\). Every Brownian increment has zero conditional mean, so conditional on \(X_0\) and all future exploration/refractory switching times, \(\mathbb E[X_t\mid X_0,\text{switching}]=a^{N_t}X_0\). The future switching clock is independent of \(X_0\) within the initial exploration or refractory phase. This remains true for the stationary refractory residual lifetime, because the original duration was selected independently of the position. Hence, with \(F_E(t)=\mathbb E[a^{N_t}\mid\text{fresh exploration}]\) and \(F_{\rm res}(t)\) the corresponding function from a stationary refractory time,

\[
C(t)=\frac{Q}{1+rm}\bigl[F_E(t)+a^2rmF_{\rm res}(t)\bigr].
\]

**Alternating-renewal equations.** Let \(F_R(t)\) denote the same probability-generating function from the start of a fresh refractory interval. Conditioning first on the exponential exploration clock, then on the refractory duration, gives

\[
\begin{aligned}
F_E(t)&=e^{-rt}+\int_0^t re^{-ru}aF_R(t-u)\,du,\\
F_R(t)&=\Pr(T>t)+\int_{[0,t]}F_E(t-u)\,W(du).
\end{aligned}
\]

Taking Laplace transforms (denoted by hats),

\[
\widehat F_E(s)=\frac{s+ar[1-w(s)]}{s[s+r-arw(s)]}.
\]

The equilibrium residual-life transform is \(w_{\rm res}(s)=[1-w(s)]/(ms)\). Consequently,

\[
\widehat F_{\rm res}(s)=\frac1s+\frac{1-w(s)}{ms}\left[\widehat F_E(s)-\frac1s\right],
\]

and

\[
\widehat C(s)=\frac{Q}{1+rm}\left[\widehat F_E(s)+a^2rm\widehat F_{\rm res}(s)\right].
\]

This derivation uses no density, memoryless, or phase-type assumption on the refractory law.

**Explicit inversion and exceptional point.** Substitution of the last expressions and cancellation give

\[
H(s)=\frac{s^2+ar[s-ar(1-a)][1-w(s)]}
{s^2\{s+r(1-a)+ar[1-w(s)]\}}.
\]

Straight algebra yields the inverse formula in the Finding. The denominator factor is

\[
s^2H(s)-s+ar(1-a)=
-\frac{r(1-a)^2(s-ar)}{s+r-arw(s)},
\]

which is nonzero precisely when \(s\ne ar\), because \(s+r-arw(s)>0\). The formula at the exceptional point is determined by continuity of the Laplace transform \(w\), proving injectivity. Substitution of \(s=ar\) in the forward transform gives the blind-frequency identity. Subtracting the forward expressions for any two \(w_1,w_2\) gives the displayed difference formula. Since \((1+sm)^{-1}>e^{-sm}\) for every \(s>0\), the deterministic/exponential strict sign reversal follows.

**Why strict partial resetting matters.** If \(a=0\), every reset sets \(X=0\). During refractory phases \(X\equiv0\), and only paths with no intervening reset contribute to \(C(t)\), giving \(C(t)=\frac{2D}{r(1+rm)}e^{-rt}\), which depends only on \(m\). Thus identifiability from covariance fails for complete resetting. This is a genuine boundary, not a singular case covered by the inverse theorem.

## Verification

The included standalone `checker.py` uses Python's standard library. Run `python checker.py` to test the forward transform against an independently constructed exact-rational finite-state Markov resolvent for exponential, Erlang-2, and hyperexponential refractory clocks. It also checks the inverse reconstruction, the universal blind frequency, and deterministic/exponential sign reversals. The tests are finite diagnostic checks and are not used as proofs of the arbitrary-distribution theorem.

For \(a=1/2\) and \(r=D=m=1\), the exact stationary exploration variance is \(Q=8/3\), the stationary total variance is \(5/3\), and \(\widehat C(1/2)=2\) for every admissible \(W\) of mean one. The precise analytic identities and the renewal derivation above provide the proof for all permitted laws.

## Relationship to prior work

Olsen and Löwen (2024) introduce exactly this partial Poisson-resetting model with general refractory durations, derive the one-time Fourier–Laplace propagator and stationary marginal moments, and show that one-time stationarity depends on the refractory mean. Those baseline results and physical motivation are credited. The present theorem instead identifies the **entire unknown refractory distribution** from the stationary two-time covariance, including the explicit inverse and the isolated crossing frequency. General reset-and-residence work by Masó-Puigdellosas, Campos, and Méndez (2019) treats complete resetting to the origin, for which this covariance inverse is demonstrably impossible. Santra, Olsen, and Gupta (2024) develop one-time position-distribution formulas for broad switching dynamics, not the stated inverse. Taźbierski, Metzler, and Magdziarz (2025) derive two-time laws for complete or translation-shift renewing resets without the same multiplicative jump followed by arbitrary idle periods. The result is therefore a specialized semi-Markov inverse theorem not obtained by renaming those conclusions. An unindexed stronger general inverse-process theorem remains a publication-priority risk.

## Limitations

The theorem assumes exact knowledge of the entire stationary covariance function and calibrated positive \(a,r,D\). It makes no claim about finite-horizon observations, noisy inference, inverse conditioning near \(a=0\) or \(s=ar\), unknown physical parameters, non-independent refractory durations, or processes that continue diffusing while refractory. The universal blind frequency is a **single Laplace-frequency identity** and does not make distributions with equal means globally indistinguishable. Mathematical originality is evaluated against the explicitly inspected sources; no independent audit or comprehensive priority guarantee has been performed.

## References

1. K. S. Olsen and H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039v1 (first posted 2024-06-14), https://arxiv.org/abs/2406.10039 ; *Journal of Physics A: Mathematical and Theoretical* **57** (2024), 485001.
2. J. Masó-Puigdellosas, D. Campos, and V. Méndez, *Stochastic movement subject to a reset-and-residence mechanism: transport properties and first arrival statistics*, arXiv:1811.06742 (2018), https://arxiv.org/abs/1811.06742 .
3. M. R. Evans and S. N. Majumdar, *Effects of refractory period on stochastic resetting*, arXiv:1809.01551 (2018), https://arxiv.org/abs/1809.01551 .
4. I. Santra, K. S. Olsen, and D. Gupta, *Dynamics of switching processes: general results and applications in intermittent active motion*, arXiv:2408.16643 (2024), https://arxiv.org/abs/2408.16643 .
5. K. Taźbierski, R. Metzler, and M. Magdziarz, *Series representation approach to stochastic processes with complete and incomplete renewal resetting*, *New Journal of Physics* **27** (2025), https://www.agnld.uni-potsdam.de/~rmetzler/papers/2025_TazMeMag_NJP27.pdf .
