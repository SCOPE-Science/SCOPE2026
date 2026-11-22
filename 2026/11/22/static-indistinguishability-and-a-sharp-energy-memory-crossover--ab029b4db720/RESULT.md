# Static indistinguishability and a sharp energy-memory crossover for two reset protocols in switching diffusion

## Finding

Two Poisson-reset protocols for a Brownian tracer with a stationary, symmetrically switching diffusivity possess **the same entire stationary joint one-time distribution** of position and diffusivity, but strictly different squared-position autocovariances at every positive lag. One protocol retains the hidden diffusivity across resets (P); the other independently redraws it from equilibrium upon each position reset (F). Their exact energy-memory functions exhibit a sharp three-way relaxation classification, with a critical reset rate equal to twice the diffusivity-switch rate.

For the parameters defined below, set
\[
V=\frac{20d^2}{r^2}+\frac{24h^2}{r(r+2k)},\qquad
B=\frac{4h^2}{r+2k}.
\]
For every lag \(t\geq0\), the stationary covariances \(C_{\mathrm P}(t)=\operatorname{Cov}_{\mathrm P}(X_0^2,X_t^2)\) and \(C_{\mathrm F}(t)=\operatorname{Cov}_{\mathrm F}(X_0^2,X_t^2)\) are
\[
C_{\mathrm P}(t)=V e^{-rt}+B\int_0^t e^{-r(t-u)}e^{-2ku}\,du,
\]
\[
C_{\mathrm F}(t)=V e^{-rt}+B\int_0^t e^{-r(t-u)}e^{-(r+2k)u}\,du.
\]
In particular, \(C_{\mathrm P}(t)>C_{\mathrm F}(t)>0\) for every \(t>0\), despite their identical one-time laws. The retained-environment protocol has the sharp asymptotics
\[
C_{\mathrm P}(t)\sim
\begin{cases}
\left(V+\dfrac{B}{2k-r}\right)e^{-rt},&0<r<2k,\\
Bt e^{-rt},&r=2k,\\
\dfrac{B}{r-2k}e^{-2kt},&r>2k.
\end{cases}
\]
The full-reinitialization protocol satisfies
\[
C_{\mathrm F}(t)\sim\left(V+\frac{B}{2k}\right)e^{-rt}\qquad (t\to\infty).
\]
Thus \(C_{\mathrm P}(t)/C_{\mathrm F}(t)\) tends to a finite constant greater than one for \(r<2k\), diverges linearly at \(r=2k\), and diverges exponentially for \(r>2k\). This is an exact separation between equality of stationary position measurements and inequivalence of temporal energy measurements.

## Assumptions and scope

Take real parameters \(r>0\), \(k>0\), and \(d>h>0\). Let \(S_t\in\{-1,+1\}\) be a continuous-time symmetric two-state Markov chain whose sign flips at rate \(k\), initially in its unique equilibrium distribution \((1/2,1/2)\). Between resets the real position satisfies the Itô stochastic differential equation
\[
dX_t=\sqrt{2(d+hS_t)}\,dW_t,
\]
where \(W\) is Brownian motion independent of the internal-state and reset clocks. An independent Poisson clock of rate \(r\) triggers one of the following interventions:

- **P (position only):** \(X\mapsto0\); the current sign \(S\) is unchanged.
- **F (full):** \(X\mapsto0\), and \(S\) is independently sampled uniformly from \(\{-1,+1\}\).

All claims concern the unique stationary laws of these well-defined jump diffusions, with the same parameters and the same resetting frequency. The observable is the centered autocovariance of squared *position*, not a stochastic-thermodynamic entropy-production rate. A reset jump contributes through its effect on position but is not counted as a continuous displacement.

## Proof

**Existence and equal-time identity.** The autonomous hidden sign is stationary and ergodic in both protocols: in P it flips at rate \(k\); in F its sign is refreshed uniformly at each reset in addition to those flips. Since position resets occur at rate \(r\), the stationary backward time \(A\) from a reset is exponential with parameter \(r\). Its value is independent of the autonomous Markov sign process in P. In F, the sign at a reset is independent and at equilibrium, and the free sign path after that reset starts from the same equilibrium law as the P sign segment. Conditional on the age \(A=a\), the **entire** sign path since the last reset therefore has the same probability law under P and F, as does the Brownian integral producing position. Consequently the joint stationary one-time law \(\mathcal L(X_t,S_t)\) is identical in the two protocols.

More explicitly, set \(Q=\begin{psmallmatrix}-k&k\\k&-k\end{psmallmatrix}\), \(D=\operatorname{diag}(d-h,d+h)\), \(\pi=(1/2,1/2)\), and let \(\mathbf 1=(1,1)^\top\). The common marginal characteristic function is
\[
\mathbb E(e^{i\xi X})
=r\,\pi(rI-Q+\xi^2D)^{-1}\mathbf 1.
\]
This establishes the entire one-time identity rather than merely equality of a finite collection of moments. Regeneration at a positive rate guarantees existence and uniqueness of the invariant law for F. For P, coupling the internal states and then using a subsequent position reset establishes convergence and uniqueness. Uniformly positive, bounded diffusivities give all stationary polynomial moments.

**Identical stationary moments.** Write \(Y=X^2\), and let \(\mathcal L\) be the backward generator. Under either protocol,
\[
\mathcal L Y=2d+2hS-rY,
\qquad
\mathcal L(YS)=2h+2dS-(r+2k)YS,
\]
\[
\mathcal L(X^4)=12(d+hS)X^2-rX^4.
\]
Because the stationary sign has zero mean, applying the stationary generator identity to these three observables gives
\[
\mathbb EY=\frac{2d}{r},\quad
\mathbb E(YS)=\frac{2h}{r+2k},\quad
\mathbb EX^4=\frac{24d^2}{r^2}+\frac{24h^2}{r(r+2k)}.
\]
Subtracting the squared mean yields \(\operatorname{Var}(Y)=V\).

**Different propagation through time.** The essential distinction is that
\[
\mathcal L_{\mathrm P}S=-2kS,
\qquad
\mathcal L_{\mathrm F}S=-(r+2k)S.
\]
For either protocol, conditioning on \((Y_0,S_0)\), writing \(m(t)=\mathbb E[Y_t\mid Y_0,S_0]\), and using the backward generator yields the closed linear equation
\[
m'(t)=2d-rm(t)+2hS_0e^{-\lambda t},\qquad m(0)=Y_0,
\]
where \(\lambda=2k\) for P and \(\lambda=r+2k\) for F. Its solution is
\[
m(t)=e^{-rt}Y_0+\frac{2d}{r}(1-e^{-rt})
+2hS_0\int_0^t e^{-r(t-u)}e^{-\lambda u}\,du.
\]
Multiplying by \(Y_0\), averaging over the stationary joint distribution, subtracting \((\mathbb EY)^2\), and inserting \(\mathbb E(Y_0S_0)=2h/(r+2k)\) yields precisely the two displayed integral formulas stated in the Finding section. For each \(u>0\), \(e^{-2ku}>e^{-(r+2k)u}\), proving strict ordering when \(h>0\).

**Asymptotic classification.** Direct integration gives, for \(r\ne2k\),
\[
C_{\mathrm P}(t)=Ve^{-rt}
+B\frac{e^{-2kt}-e^{-rt}}{r-2k};
\]
at \(r=2k\), the continuous extension is \(e^{-rt}(V+Bt)\). Similarly,
\[
C_{\mathrm F}(t)=Ve^{-rt}
+\frac{B}{2k}e^{-rt}(1-e^{-2kt}).
\]
All constants are positive under the stated assumptions. Comparing the distinct exponential rates and, at coalescence, the linear-in-time factor completes the exact three-regime statement.

## Verification

A standalone \(\texttt{CHECK.py}\) file accompanies the result. Running \(\texttt{python CHECK.py}\), with Python, SymPy, NumPy, and SciPy installed, checks the generator identities and covariance normalization symbolically. It then compares the formulas against an independently exponentiated closed generator matrix on the polynomial basis \((1,S,X^2,SX^2)\) at eighty independently selected parameter points, including both reset protocols. Additional independent two-state resolvent calculations verify the one-time characteristic function and its small-frequency variance. The completed check gives 380 passing numerical assertions and 14 symbolic checks. The all-parameter theorem is proved by the preceding generator argument, not by numerical sampling.

## Relationship to prior work

Bressloff, *Switching diffusions and stochastic resetting* (2020), DOI: 10.1088/1751-8121/ab97e0, studies the same two-diffusivity setting with the internal state jointly redrawn from equilibrium at positional resets, deriving a stationary sum-of-exponentials density and first-passage statistics. Its first-page preview and abstract support that identification; the entire 16-page text could not be inspected. Therefore the already-known stationary distribution and its general resolvent method are not asserted as new. The additional result here is the exact **comparison of P and F temporal squared-position covariances**, their strict all-lag inequality, and the exact critical \(r=2k\) crossover.

Grebenkov, *A unifying approach to first-passage time distributions in diffusing diffusivity and switching diffusion models* (arXiv:1812.07249, 2018), supplies a general switching-diffusivity propagator and integrated-diffusivity moment method **without the paired reset interventions**. Kumar, Sadekar, and Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting* (arXiv:2008.03294, 2020), compare position-only and position–orientation resetting for self-propelled motion, where the latter orientation is fixed by the reset and stationary spatial anisotropy generally distinguishes the protocols. Lux, *Estimation of regime-switching diffusions via Fourier transforms* (2024), concerns recovery of hidden diffusion parameters from transition distributions, without resetting. These settings do not directly imply the claimed identical-stationary-law/different-energy-memory classification for symmetric Markov-switching diffusivity.

## Limitations

This theorem treats only positive symmetric switching rate, positive diffusivity contrast, Poisson resetting, and one-dimensional Brownian motion. If \(h=0\), the strict temporal inequality vanishes. It does not establish finite-sample statistical power for discriminating the protocols, and does not treat non-exponential reset clocks or internal-state-dependent resetting. Although the stationary laws are mathematically identical, observation of the hidden sign trajectory itself would of course distinguish the protocols. The closest full publication of Bressloff (2020) was not available beyond its publisher preview; stronger implicit prior coverage remains a publication-priority uncertainty. The embedded numerical checks cannot certify universal statements independently of the analytic proof.

## References

1. P. C. Bressloff, “Switching diffusions and stochastic resetting,” *Journal of Physics A* **53**, 275003 (2020), published 17 June 2020, https://doi.org/10.1088/1751-8121/ab97e0.
2. D. S. Grebenkov, “A unifying approach to first-passage time distributions in diffusing diffusivity and switching diffusion models,” arXiv:1812.07249v1 (18 December 2018), https://arxiv.org/html/1812.07249v1.
3. V. Kumar, O. Sadekar, U. Basu, “Active Brownian Motion in two-dimensions under Stochastic Resetting,” arXiv:2008.03294v1 (7 August 2020), https://arxiv.org/html/2008.03294v1.
4. T. Lux, “Estimation of regime-switching diffusions via Fourier transforms,” *Statistics and Computing* (2024), https://doi.org/10.1007/s11222-024-10397-6.
