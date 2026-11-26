# A nonconcentrating Beta law for the age of extreme untrapped excursions

## Finding
Consider a stationary Brownian particle (or any finite vector of particles exposed to the same switching environment) in a harmonic trap that switches completely off and on. Conditional on finding the particle at a position increasingly distant from the trap center, the trap is overwhelmingly likely to be off. Nevertheless, the age of the present untrapped excursion, divided by distance, does **not** concentrate on a deterministic value. It converges to a nondegenerate Beta distribution:

\[
\left.\frac{2\sqrt{aD}\,T}{\|X\|}\ \right|\ (X=x,S=\mathrm{off})
\quad\Longrightarrow\quad \operatorname{Beta}\!\left(1,\frac{b}{2k}\right),\qquad \|x\|\to\infty.
\]

Here \(k\) is the active trap relaxation rate, \(D\) the diffusivity, \(a\) the off-to-on switching rate, \(b\) the on-to-off switching rate, and \(T\) the elapsed time since the most recent on-to-off switch. The limit applies in every fixed finite spatial dimension. Moreover, the exact limiting trap-state posterior is

\[
\Pr(S=\mathrm{on}\mid X=x)\sim\frac{\sqrt{aD}}{k\|x\|}.
\]

These statements describe the *history conditional on an extreme spatial observation*, rather than only the already-studied stationary spatial distribution. In particular, an extreme displacement retains a random fraction of its large effective variance from the **current** free-diffusion episode, with the complementary fraction inherited from earlier episodes.

## Assumptions and scope
Fix \(d\in\{1,2,\ldots\}\) and parameters \(D,k,a,b>0\). The stationary two-state continuous-time Markov chain \(S_t\in\{\mathrm{on},\mathrm{off}\}\) jumps on-to-off at rate \(b\), off-to-on at rate \(a\), independently of a standard \(d\)-dimensional Brownian motion \(W_t\). Define the unique stationary solution

\[
 dX_t=-k\mathbf1_{\{S_t=\mathrm{on}\}}X_t\,dt+\sqrt{2D}\,dW_t.
\]

The result is conditional on a point \(X=x\) through the continuous regular conditional densities. Let \(T\) be the backward residence time in the current off-state episode, defined on \(\{S=\mathrm{off}\}\). Define \(A=a/(2k)\), \(B=b/(2k)\), and the dimensionless observation radius \(R=\sqrt{k/D}\,\|x\|\). All limits hold for fixed \(d,D,k,a,b\), and no switching-rate or dimension limit is taken. The vector case is equivalently a finite number of independent Brownian particles subject to the same on/off trap history.

## Proof

**Stationary Gaussian mixture.** Because the stationary Markov environment visits the confining state for a positive asymptotic fraction of time, its past-integrated linear propagator decays. Consequently, the stationary stochastic convolution exists and, conditional on the whole past of the environment, is centered Gaussian with isotropic variance

\[
 V_t=2D\int_{-\infty}^{t}\exp\!\left[-2k\int_s^t\mathbf1_{\{S_u=\mathrm{on}\}}du\right]ds.
\]

Introduce the nonnegative excess-variance coordinate \(U=kV/D-1\). On an on-state interval it satisfies \(\dot U=-2kU\); on an off-state interval \(\dot U=2k\). Put \(G_m(u)=A^m u^{m-1}e^{-Au}/\Gamma(m)\) for \(u>0\). The stationary transport equations with zero total flux then give the joint densities

\[
 \Pr(S=\mathrm{on},U\in du)=\frac{A}{A+B}G_B(u)\,du,\qquad
 \Pr(S=\mathrm{off},U\in du)=\frac{B}{A+B}G_{B+1}(u)\,du.
\]

Indeed the modewise probability fluxes are \(-2ku f_{\mathrm{on}}\) and \(2k f_{\mathrm{off}}\), so vanishing total flux requires \(f_{\mathrm{off}}=uf_{\mathrm{on}}\). Either stationary transport equation then yields \(f_{\mathrm{on}}\propto u^{B-1}e^{-Au}\); normalizing with the invariant mode probabilities proves the formulas. These static Gaussian mixture laws are consistent with the prior stationary characteristic functions [1] and related Gaussian-mixture formulations [2,3]; they are not asserted as new findings.

**Exact current-excursion decomposition.** Condition on the off state at a stationary observation time. Since off holding times are exponential with rate \(a\), the backward age \(T\sim\operatorname{Exp}(a)\). The on-state environment and its excess variance immediately *before* the last transition to off are independent of the new off holding time. The switching hazard \(b\) is constant, so the excess variance \(U_0\) at the start of off has the on-state gamma law \(G_B\), independently of \(T\). While the trap is off, \(U=U_0+2kT\). Thus

\[
 U_0\sim\operatorname{Gamma}(B,A),\quad 2kT\sim\operatorname{Gamma}(1,A),\quad U_0\perp T.
\]

Here the second gamma parameter denotes *rate*, not scale. The classical gamma-to-Beta change of variables yields the exact factorization

\[
 J:=\frac{2kT}{U}\sim\operatorname{Beta}(1,B),\qquad J\perp U,
 \qquad (U\mid S=\mathrm{off})\sim\operatorname{Gamma}(B+1,A).
\]

Given the environment, \(X\) is Gaussian with covariance \((D/k)(1+U)I_d\). Its likelihood depends only on \(U\), not on the gamma fraction \(J\). Hence **\(J\) and \(X\) remain exactly independent conditional on \(S=\mathrm{off}\)**, not merely asymptotically.

**Posterior concentration of the *total* excess variance.** Let \(Y=\sqrt{k/D}X\) and \(R=\|Y\|\). Conditional on \(Y=y\) and \(S=\mathrm{off}\), \(U\) has density proportional to

\[
 u^B e^{-Au}(1+u)^{-d/2}\exp\!\left(-\frac{R^2}{2(1+u)}\right),\qquad u>0.
\]

On writing \(u=Rv\), its exponential weight on each compact interval \(0<\epsilon\le v\le M\) is \(\exp[-R\{Av+(2v)^{-1}\}+O(1)]\), times positive polynomial factors. The strictly convex rate \(I(v)=Av+(2v)^{-1}\) has unique minimizer \(v_*=1/\sqrt{2A}=\sqrt{k/a}\). The integrals outside any fixed neighborhood of \(v_*\) are exponentially negligible: \(Av\) controls \(v\to\infty\), and \(R^2/[2(1+Rv)]\) controls \(v\downarrow0\). Standard two-sided Laplace estimates therefore give

\[
 \left.\frac{U}{R}\ \right|\ (Y=y,S=\mathrm{off})\ \xrightarrow{\Pr}\ \sqrt{\frac{k}{a}}.
\]

Because \(J\) is independent of \(Y\) and \(U\) in this conditioning, Slutsky's theorem applies to \(2kT=JU\). In original coordinates,

\[
 \frac{2\sqrt{aD}\,T}{\|x\|}
 =\sqrt{\frac ak}\,J\frac UR\Longrightarrow J\sim\operatorname{Beta}(1,B),
\]

proving the first conclusion for all finite \(d\).

**Recovery of the trap state from a far-field observation.** Denote by \(\mathcal L_R(u)=(2\pi(1+u))^{-d/2}\exp[-R^2/(2(1+u))]\) the positional likelihood, omitting a common scale factor. Let

\[
 M_R=\frac{\int_0^\infty uG_B(u)\mathcal L_R(u)du}
 {\int_0^\infty G_B(u)\mathcal L_R(u)du}.
\]

The density relation \(f_{\mathrm{off}}=uf_{\mathrm{on}}\) yields the **exact** posterior identity

\[
 \Pr(S=\mathrm{on}\mid X=x)=\frac{1}{1+M_R}.
\]

The same Laplace argument, now with polynomial exponent \(B-1\) instead of \(B\), gives \(M_R/R\to\sqrt{k/a}\). Therefore \(\Pr(S=\mathrm{on}\mid X=x)\sim\sqrt{a/k}/R=\sqrt{aD}/(k\|x\|)\). This also justifies applying the off-state conditional limit to rare observations without preselecting the current trap state: the probability of the on state becomes negligible.

## Verification
The accompanying `verify.py` independently integrates the on/off gamma-Gaussian posterior densities in several dimensions and unequal-rate parameter regimes. It tests the exact posterior-odds identity against two separately normalized integrals; the predicted far-field variance saddle and inverse-distance mode posterior; and the beta-gamma moment factorization. The reported finite-radius numerical comparisons are consistency checks, not a replacement for the analytic large-radius proof. Run with `python verify.py` using Python, SciPy, and NumPy (though no randomness is used).

## Relationship to prior work
Santra, Das, and Nath [1], especially Appendix B, derived the exact stationary on/off Fourier transforms for unequal switching rates. Those static formulas imply the modewise gamma-Gaussian mixture above and were incorporated, not republished as novel. Frydel [2] analyzed equilibrium-strength Gaussian mixtures and exponential position tails for symmetric switching. Biroli, Kulkarni, Majumdar, and Schehr [3] derived finite-particle joint distributions and collective extreme-value statistics for switching harmonic traps, including strictly positive low stiffness and a resetting limit. Their published results explain the common-variance mechanism and spatial extremes, but the inspected analyses do not supply the backward **current-off residence-time** law conditioned on a single extremely distant spatial observation, nor the nonconcentrating Beta fraction. The present conclusion concerns that specific path statistic at fixed positive trap stiffness, not a new stationary position distribution. Its proof uses the familiar beta-gamma identity, combined with the environment's stationary Palm decomposition and a conditional large-displacement Laplace principle.

## Limitations
The observation is in the stationary regime, with strictly positive constant switching rates and full trap-off intervals. The asymptotic is for a fixed finite number of spatial coordinates; it is not uniform as dimension, switching rates, or stiffness change. The Beta law specifies the backward age of the **current** off interval only, not the entire prior switching path, a finite-threshold sampling error, or a pathwise law of large numbers. The on-state posterior constant is an asymptotic statement and not an exact identity at finite distance. No independent scholarly originality audit has been performed; closely related general hidden-state filtering or gamma-mixture calculations might yield an equivalent conditional-age result.

## References
[1] I. Santra, S. Das, and S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609 (first posted 2021-04-01), especially Appendix B, equations (B.1)–(B.4). Author-accepted manuscript: https://eprints.whiterose.ac.uk/id/eprint/176114/1/Brownian_harmonic_sujit.pdf.

[2] D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213 (first posted 2024-07-17), especially Sections III–VI.

[3] M. Biroli, M. Kulkarni, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570 (first posted 2023-12-05), main text and supplemental Sections I, IV, V.
