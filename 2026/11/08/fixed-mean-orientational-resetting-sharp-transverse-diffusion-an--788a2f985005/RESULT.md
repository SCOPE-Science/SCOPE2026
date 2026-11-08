# Fixed-mean orientational resetting: sharp transverse diffusion and longitudinal anisotropy reversal

## Finding

Fix any swimming speed \(v>0\), rotational diffusivity \(d>0\), translational diffusivity \(D\geq0\), and prescribed mean orientational-reset interval \(\mu>0\). Let successive strictly positive intervals \(T\) be independent, identically distributed, and satisfy \(\mathbb E T=\mu\) and \(\mathbb E T^3<\infty\). Between resets a planar swimmer has orientation \(\theta_t\) evolving as Brownian motion with generator \(d\partial_{\theta\theta}\) on the circle, and spatial velocity \(v(\cos\theta_t,\sin\theta_t)\) plus independent isotropic Brownian diffusion \(D\). At a reset only the orientation changes, to angle zero; the spatial position does not reset. Take the equilibrium-renewal stationary orientation/clock initialization. Define \(u=\lim_{t\to\infty}\mathbb E(X_t-X_0)/t\) and \(\mathcal D_{\parallel},\mathcal D_{\perp}\) by

\[
\mathcal D_{\parallel}=\lim_{t\to\infty}\frac{\operatorname{Var}(X_t-X_0)}{2t},\qquad
\mathcal D_{\perp}=\lim_{t\to\infty}\frac{\operatorname{Var}(Y_t-Y_0)}{2t}.
\]

**Theorem (complete transverse protocol range and anisotropy reversal).** With

\[
H_d(t)=\frac{t}{d}-\frac{4(1-e^{-dt})}{3d^2}+\frac{1-e^{-4dt}}{12d^2},
\qquad
h_*(\mu)=D+\frac{v^2}{2\mu}H_d(\mu),
\]

the exact attainable set at fixed \(\mu,d,v,D\) is

\[
\boxed{\mathcal D_{\perp}\in\left[h_*(\mu),\ D+\frac{v^2}{2d}\right).}
\]

Equality at the lower end holds **if and only if** resets are deterministic, \(T=\mu\) almost surely. Every larger value below the sharp upper end is attained by a strictly positive, finite-support interval law. The supremum is unattainable by any permissible law.

For deterministic intervals the strict long-time anisotropy obeys

\[
\boxed{\mathcal D_{\parallel}-\mathcal D_{\perp}
=-\frac{v^2}{12\mu d^2}(1-e^{-d\mu})^3(3+e^{-d\mu})<0.}
\]

Nevertheless, **with the same fixed mean \(\mu\)** there are two-point strictly positive laws for which \(\mathcal D_{\parallel}\to\infty\), while \(\mathcal D_{\perp}\to h_*(\mu)\). Thus the sign of transport anisotropy can reverse, and no finite fixed-mean upper bound exists for the longitudinal effective diffusivity, even though transverse diffusivity has the universal sharp upper bound above. The diverging longitudinal diffusivities occur for individual finite-support laws, each of which has an ordinary finite diffusive long-time limit.

## Assumptions and scope

Use independent Brownian motions \(W^{(x)},W^{(y)},B\), with successive angular Brownian increments renewed independently after every reset. Within the cycle beginning at a reset,

\[
d\theta_s=\sqrt{2d}\,dB_s,\quad \theta_0=0,\quad
dX_s=v\cos(\theta_s)ds+\sqrt{2D}\,dW_s^{(x)},\quad
dY_s=v\sin(\theta_s)ds+\sqrt{2D}\,dW_s^{(y)}.
\]

Reset instants form an independent renewal process, not necessarily Poisson. A random stationary cycle phase is used for lattice/deterministic interval laws; no pointwise convergence from a common synchronized phase is asserted. The finite third moment ensures residual-cycle mean squares are uniformly controlled under equilibrium renewal initialization. All results concern long-time fluctuation coefficients, not finite-sample inference or spatial stationary distributions (position is unconfined).

Write \(\phi(q)=\mathbb E[e^{-qT}]\), \(m_2=\mathbb E[T^2]\), and

\[
K_d(t)=\frac{t}{d}-\frac{2(1-e^{-dt})}{3d^2}-\frac{1-e^{-4dt}}{12d^2},
\quad A_d(t)=\frac{1-e^{-dt}}{d}.
\]

The exact drift and the complementary longitudinal coefficient are

\[
\boxed{u=\frac{v}{\mu}\mathbb E A_d(T)=\frac{v[1-\phi(d)]}{d\mu},\qquad
\mathcal D_{\perp}=D+\frac{v^2}{2\mu}\mathbb E H_d(T),}
\]

\[
\boxed{\mathcal D_{\parallel}=D+\frac{v^2\mathbb E K_d(T)
-2uv\mathbb E[T A_d(T)]+u^2m_2}{2\mu}.}
\]

These identities also specify the exact domain and normalization of the claims above.

## Proof

**1. Cycle Fourier moments.** For \(0\le s\le t\), angular Gaussian increments starting at zero give

\[
\mathbb E[e^{i\theta_s}]=e^{-ds},\qquad
\mathbb E[\cos\theta_s\cos\theta_t]=\tfrac12\{e^{-d(t-s)}+e^{-d(t+3s)}\},
\]

\[
\mathbb E[\sin\theta_s\sin\theta_t]=\tfrac12\{e^{-d(t-s)}-e^{-d(t+3s)}\}.
\]

Integrating over both triangular halves of the time square of side \(t\) yields, for the active displacement of one cycle of deterministic duration \(t\),

\[
\mathbb E J_x(t)=vA_d(t),\quad \mathbb E J_y(t)=0,\quad
\mathbb E J_x(t)^2=v^2K_d(t),\quad\mathbb E J_y(t)^2=v^2H_d(t).
\]

Here \(J_x(t)=v\int_0^t\cos\theta_s\,ds\) and \(J_y(t)=v\int_0^t\sin\theta_s\,ds\). Translational Brownian variance over one cycle is \(2Dt\) in each coordinate, independently of the active part.

**2. Long-time renewal covariance.** For iid cycles \((T_j,J_{x,j},J_{y,j})\), the renewal-reward drift is \(u=\mathbb EJ_x(T)/\mu\). The independent centered cycle rewards \(J_x(T)-uT\) and \(J_y(T)\) have zero means and finite variances. In the equilibrium-renewal construction the current cycle age has second moment \(\mathbb E T^3/(3\mu)\). Because the active speed is bounded by \(v\), the centered unfinished-cycle contribution has bounded mean square, and its cross term with a completed-cycle sum is \(O(\sqrt t)\); the completed-cycle sum has variance \((t/\mu+o(t))\mathbb E[(J_x-uT)^2]\) or \((t/\mu+o(t))\mathbb E[J_y^2]\). The stationary initial partial cycle similarly contributes only \(o(t)\) to variance. An independent translational Brownian motion adds exactly \(2Dt\). The displayed formulas for the drift and both effective diffusivities follow by expanding the centered reward variance. This argument also applies to deterministic intervals with a uniform stationary phase.

**3. Strict convexity and attainable sharp transverse range.** Twice differentiating the integrated angular kernel gives

\[
H_d''(t)=\frac43(e^{-dt}-e^{-4dt})>0\quad (t>0).
\]

Strict Jensen implies \(\mathbb EH_d(T)\ge H_d(\mu)\), with equality exactly for deterministic \(T\). Also \(H_d(t)<t/d\) for every \(t>0\), because \(1-e^{-4dt}\le4(1-e^{-dt})\). Hence \(\mathbb EH_d(T)<\mu/d\), the stated universal strict upper bound.

To approach the upper end let \(n\to\infty\) and choose two reset intervals \(a_n=\mu/n^2\) and \(b_n=n\mu\) with \(\Pr(T=b_n)=(\mu-a_n)/(b_n-a_n)\). Then \(\mathbb ET=\mu\), both atoms are positive, and \(\mathbb EH_d(T)\to\mu/d\) since \(H_d(a_n)\to0\), \(H_d(b_n)=b_n/d+O(1)\), and \(\Pr(T=b_n)b_n\to\mu\). Convexly mixing the deterministic law with any such two-point law varies \(\mathbb EH_d(T)\) continuously between their values without changing the mean, and establishes attainability of all intermediate values by finite-support laws.

**4. Deterministic anisotropy and reversal.** At \(T=\mu\), subtracting the two cycle variances and using the square of \(\mathbb EJ_x\) produces

\[
\mathcal D_{\parallel}-\mathcal D_{\perp}
=\frac{v^2}{12\mu d^2}(e^{-d\mu}-1)^3(e^{-d\mu}+3)<0.
\]

For the converse direction take integers \(n\ge2\), \(b_n=n\mu\), \(p_n=n^{-3/2}\), and

\[
a_n=\frac{\mu-p_nb_n}{1-p_n}=\mu\frac{1-n^{-1/2}}{1-n^{-3/2}}.
\]

Set \(\Pr(T=b_n)=p_n\) and \(\Pr(T=a_n)=1-p_n\). Then \(a_n>0\), \(\mathbb ET=\mu\), \(a_n\to\mu\), and \(\mathbb ET^2\sim\mu^2\sqrt n\), whereas \(u_n\to u_*=v(1-e^{-d\mu})/(d\mu)>0\). Since \(K_d(t)=t/d+O(1)\) and \(0\le A_d(t)\le1/d\), both \(\mathbb EK_d(T)\) and \(\mathbb E[T A_d(T)]\) stay uniformly bounded. Consequently the exact longitudinal formula gives

\[
\mathcal D_{\parallel}(n)\sim \frac{\mu u_*^2}{2}\sqrt n\to\infty.
\]

Meanwhile \(H_d(t)=t/d+O(1)\) and \(p_nb_n\to0\), so \(\mathbb EH_d(T)\to H_d(\mu)\) and \(\mathcal D_{\perp}(n)\to h_*(\mu)\). For sufficiently large \(n\), longitudinal diffusivity exceeds transverse diffusivity, reversing the deterministic sign.

## Verification

A standalone Python 3 standard-library checker named `checker.py` independently integrates the angular Fourier correlation kernels (numerical Simpson quadrature), checks the two closed cycle-moment functions, verifies the strict fixed-mean inequalities over reproducible two-point laws, checks the deterministic anisotropy identity, verifies the published Poisson-reset transport coefficients as a special case, and evaluates the explicit anisotropy-reversal sequence. It reports 1,626 successful assertion groups. The analytic inequalities and infinite asymptotics above, not finite numerical samples, establish the theorem.

As an exact-scale example, setting \(v=d=\mu=1\), \(D=0\), deterministic resets give \((u,\mathcal D_{\parallel},\mathcal D_{\perp})\approx(0.632120559,0.048601432,0.119489809)\). The same mean with the two-point reverse-anisotropy construction at \(n=256\) gives approximately \((0.608579601,2.997002153,0.134968162)\).

To reproduce: run `python3 checker.py` in the directory containing this file and the checker; no third-party packages or input files are required.

## Relationship to prior work

Baouche, Franosch, Meiners and Kurzthaler (2024) provide the exact orientational-reset model, general renewal equations and, upon choosing exponential intervals, the long-time diffusivities and drift. Their Eqs. (19)--(20) agree with the present coefficient formulas when \(T\) is exponential. They do not state a fixed-mean extremal interval, a unique deterministic minimizer over general renewal laws, nor the two-point divergence and sign reversal. The general renewal equations are credited and are a strong precursor; the added assertion concerns optimization over the interval distribution and its singular longitudinal fluctuations, not merely a replacement of resetting parameters.

Kumar, Sadekar and Basu (2020) establish orientation-only Poisson resetting and long-time diffusion regimes, but do not optimize over renewal interarrival laws. Chaki, Olsen and Löwen (2024) and the related Ghosh--Mandal work (first publicly available 2025) analyze shape-anisotropic Brownian transport under constant-rate orientational resetting; their particle model and fixed-rate results differ from the self-propelled fixed-mean distributional range here. General renewal-resetting theory establishes the underlying renewal formalism and is not claimed as new.

## Limitations

Every particular admissible protocol has finite \(\mathbb ET^3\) and finite diffusivities; the longitudinal divergence occurs only across a family whose moments are not uniformly bounded. The process is not studied under angular torque, finite reset durations, spatial resetting, reset errors, velocity randomness, or interactions. The transverse optimum is specific to fixed mean reset time and perfect heading resetting; it is not an optimum under another budget such as reset energetic cost. These are analytic long-time coefficients, not claims about finite-time tracking uncertainty. The comparison with publicly accessible literature and record searches cannot rule out all unindexed equivalent results.

## References

1. Y. Baouche, T. Franosch, M. Meiners and C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769, first public 2024-05-10, https://arxiv.org/abs/2405.06769 .
2. V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294, first public 2020-08-07, https://arxiv.org/abs/2008.03294 .
3. S. Chaki, K. S. Olsen and H. Löwen, *Anisotropic Brownian particles under resetting*, arXiv:2406.17550, first public 2024-06-25, https://arxiv.org/abs/2406.17550 .
4. A. Ghosh and S. Mandal, *Anisotropic active Brownian particle in two dimensions under stochastic resetting*, arXiv:2501.05149, first public 2025-01-09, https://arxiv.org/abs/2501.05149 .
5. General renewal-reward variance theorem (standard regenerative-process identity; applied here with bounded cycle velocities and finite third interval moment).
