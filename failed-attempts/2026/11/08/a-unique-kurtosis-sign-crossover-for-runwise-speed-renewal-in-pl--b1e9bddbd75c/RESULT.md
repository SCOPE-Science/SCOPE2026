# A unique kurtosis-sign crossover for runwise speed renewal in planar active motion

## Finding

Consider a planar run-and-tumble particle which redraws **both** its speed and an independent uniform heading at every Poisson tumble. Let the new speed \(R\geq0\) have \(0<\mathbb E R^2<\infty\) and \(\mathbb E R^4<\infty\), and put
\[
\rho=\frac{\mathbb E R^4}{(\mathbb E R^2)^2}\geq1.
\]
At stationary initialization, define the radial displacement excess kurtosis
\[
\mathcal K(t)=\frac{\mathbb E|\mathbf X_t|^4}{2(\mathbb E|\mathbf X_t|^2)^2}-1,\qquad t>0.
\]
The result is a complete, exact sign classification for **all times** and **all** such speed laws, even with arbitrary independent translational Brownian diffusivity \(D\geq0\):

1. If \(\rho\leq4/3\), then \(\mathcal K(t)<0\) for every \(t>0\).
2. If \(\rho\geq2\), then \(\mathcal K(t)>0\) for every \(t>0\).
3. If \(4/3<\rho<2\), exactly one positive time \(t_c\) has \(\mathcal K(t_c)=0\). The excess kurtosis is strictly negative before \(t_c\) and strictly positive after it.

The unique crossing is specified by \(\rho=\rho_c(\alpha t_c)\), where
\[
\rho_c(s)=\frac23\left(1+2\frac{J(s)}{I(s)}\right),\qquad
I(s)=\int_0^s(s-u)e^{-u}\frac{u^2}{2}\,du,
\]
\[
J(s)=\int_0^s(s-u)e^{-u}\int_0^u(u-w)e^{-w}\,dw\,du.
\]
The function \(\rho_c\) is strictly decreasing from \(2\) at \(s=0^+\) to \(4/3\) at \(s=\infty\). This is a **unique temporal sign transition**, not a thermodynamic phase transition.

For illustration, a stop/go speed law \(\mathbb P(R=v)=p\), \(\mathbb P(R=0)=1-p\), with \(v>0\), has \(\rho=1/p\). Therefore the one-crossing regime is precisely \(1/2<p<3/4\); \(p=2/3\) is a simple example.

## Assumptions and scope

Fix a Poisson rate \(\alpha>0\), a diffusivity \(D\geq0\), and an independent planar standard Brownian motion \(\mathbf B\). At time zero and at each event of a rate-\(\alpha\) Poisson process, independently draw \(R\) from a **fixed** law supported on \([0,\infty)\) and \(\Theta\) uniformly on \([0,2\pi)\). Between events the velocity is constant,
\[
\mathbf V_s=R_s(\cos\Theta_s,\sin\Theta_s),\qquad
\mathbf X_t=\int_0^t\mathbf V_s\,ds+\sqrt{2D}\,\mathbf B_t.
\]
All marks, tumble times and Brownian increments are independent; \(\mathbf X_0=0\). The initial mark is drawn from the same law as later marks, so the velocity is stationary. The result is for a **freely moving noninteracting particle** and for the unconditioned position at a fixed time, not first passage, interacting swarms, velocity-correlated tumbling, or non-Poisson waiting times.

## Proof

**1. Reduction to a scalar fourth cumulant.** Choose a Cartesian projection \(Y_t\) of \(\mathbf X_t\), with projected active velocity \(U_s=R_s\cos\Theta_s\). Its stationary even moments are
\[
m_2=\mathbb E U^2=\frac{\mathbb E R^2}{2}>0,\qquad
m_4=\mathbb E U^4=\frac{3\mathbb E R^4}{8},
\]
while all odd moments through order three vanish. Isotropy and zero mean give exactly
\[
\mathcal K(t)=\frac{\operatorname{cum}_4(Y_t)}{3\operatorname{Var}(Y_t)^2}.
\]
Indeed \(\mathbb E Y_t^2=\mathbb E|\mathbf X_t|^2/2\) and \(\mathbb E Y_t^4=3\mathbb E|\mathbf X_t|^4/8\). The independent Gaussian Brownian term changes the variance but contributes zero fourth cumulant.

**2. Exact ordered-time cumulant.** For \(s_1<s_2<s_3<s_4\), put \(g_j=s_{j+1}-s_j\). Independence after each fresh mark and the zero odd mark moments give
\[
\begin{aligned}
\mathbb E(U_{s_1}U_{s_2}U_{s_3}U_{s_4})
&=m_4e^{-\alpha(g_1+g_2+g_3)}\\
&\quad +m_2^2e^{-\alpha(g_1+g_3)}(1-e^{-\alpha g_2}).
\end{aligned}
\]
Subtract the three covariance pairings. Since \(\mathbb E U_{s_i}U_{s_j}=m_2 e^{-\alpha(s_j-s_i)}\) for \(i<j\), the connected four-time cumulant is
\[
(m_4-m_2^2)e^{-\alpha(g_1+g_2+g_3)}
-2m_2^2e^{-\alpha(g_1+2g_2+g_3)}.
\]
The coincidence hyperplanes have zero integration measure. Fubini's theorem applies since the fourth mark moment is finite. Integrating over the four ordered times and multiplying by \(4!\) yields
\[
\boxed{\operatorname{cum}_4(Y_t)
=\frac{24}{\alpha^4}\big[(m_4-m_2^2)I(\alpha t)-2m_2^2J(\alpha t)\big].}
\]
The integral formulae for \(I,J\) follow by fixing the total span \(u=s_4-s_1\) and integrating the three intervening gaps. They are strictly positive for every \(s>0\). Independently, the covariance integration yields
\[
\operatorname{Var}(Y_t)=2Dt+
\frac{2m_2}{\alpha^2}\big(\alpha t-1+e^{-\alpha t}\big)>0.
\]
Consequently,
\[
\operatorname{sgn}\mathcal K(t)
=\operatorname{sgn}\big(\rho-\rho_c(\alpha t)\big),
\]
because \(m_4/m_2^2=3\rho/2\). This proves that translational diffusivity affects the magnitude but not the kurtosis sign.

**3. Strict threshold monotonicity.** For \(u>0\), define
\[
h(u)=\frac{2}{u^2}\int_0^u(u-w)e^{-w}\,dw
=2\int_0^1(1-z)e^{-uz}\,dz.
\]
The latter representation shows \(h\) is strictly decreasing, with \(0<h(u)<1\). Moreover, \(J(s)/I(s)\) is the average of \(h(u)\) under the density proportional to \((s-u)u^2e^{-u}\) for \(0<u<s\). If \(s'>s\), the ratio of these unnormalized densities on their common support is
\[
\frac{s'-u}{s-u},
\]
which is strictly increasing in \(u\), and the larger interval places additional positive mass above \(s\). Therefore these span distributions increase strictly in the monotone-likelihood-ratio/stochastic order, so the expectation of strictly decreasing \(h\) decreases strictly. Hence \(J/I\) and \(\rho_c\) are strictly decreasing.

The small-\(s\) expansions \(I(s)\sim s^4/24\), \(J(s)\sim s^4/24\) give \(\rho_c(0^+)=2\). Dominated convergence in the defining integrals gives \(I(s)/s\to1\), \(J(s)/s\to1/2\), and thus \(\rho_c(\infty)=4/3\). Continuity and strict monotonicity establish all three cases, including the uniqueness and direction of the sign change.

**4. Long-time and boundary orders.** Put \(D_{\mathrm{eff}}=D+m_2/\alpha\). From \(I(s)=s-3+o(1)\) and \(J(s)=s/2-5/4+o(1)\), the exact cumulant formula gives
\[
\mathcal K(t)=\frac{3\mathbb E R^4-4(\mathbb E R^2)^2}
{4\alpha^3D_{\mathrm{eff}}^2}\,t^{-1}+O(t^{-2})
\quad(\rho\ne4/3).
\]
At the sharp boundary \(\rho=4/3\), the leading coefficient vanishes but the next term is strictly negative:
\[
\boxed{\lim_{t\to\infty}t^2\mathcal K(t)
=-\frac{m_2^2}{\alpha^4D_{\mathrm{eff}}^2}<0.}
\]
This finishes the classification without relying on numerical root counts.

## Verification

The accompanying `verify_kurtosis.py` compares the derived cumulant and variance independently against a six-variable linear moment ODE for a family of two-speed stop/go laws at multiple rates and times. It also checks the threshold's numerical ordering and an explicit negative-to-positive crossover. Execute from a directory containing the standalone file with `python verify_kurtosis.py` (requires Python, NumPy and SciPy). The successful run reported 395 deterministic checks, including 252 independently evaluated ODE/moment comparisons. These finite checks validate identities at selected parameters; the monotonic-likelihood-ratio argument, not numerical sampling, proves uniqueness for every admissible law and time.

## Relationship to prior work

Britton, Zhang, Han and Bertrand (2026) analyze general angular reorientation kernels but fix the propulsion speed within and across runs. They calculate a fourth spatial moment for that different velocity process and observe kurtosis tending to zero. Their result does not cover arbitrary speed redrawn **with** an independent fresh heading at every tumble; it does not state the two sharp speed-moment thresholds or a unique sign crossing.

Mori, Le Doussal, Majumdar and Schehr (2020) explicitly introduce the same runwise random-speed isotropic RTP model. Their main theorems concern survival, time of maximum and record statistics, universal in the speed law, rather than the speed-law-sensitive signed fourth cumulant. Thus **the process is not new**, but the sharp sign classification is distinct from the stated record/persistence results. Their general trajectory representation may provide an alternative derivation; priority for the specific classification is not independently certified.

Shee and Chaudhuri (2021) show positive/negative kurtosis crossovers in a different active Brownian model with continuously evolving Ornstein–Uhlenbeck speed and angular diffusion. Santra, Olsen and Gupta (2024) study switching/finite-state velocity processes and their cumulants. Neither of those analyzed dynamics is the Poisson complete-velocity-refresh model with arbitrary nonnegative runwise speed distribution and a monotone universal sign threshold. The underlying connection between speed heterogeneity and kurtosis sign is therefore previously known; the claim here is the exact classification for this specific stochastic model.

## Limitations

The conclusion is about fourth moments, not the entire displacement density or the sign of its pointwise tails. It assumes **joint renewal** of speed and uniform heading at each tumble and stationary initial mark; modifying either assumption may destroy the thresholds. A finite fourth speed moment is necessary for the displayed kurtosis. At very small times, the thermal Brownian variance may obscure the magnitude of the signal without altering its sign. No assertion is made about swimming interactions, finite-width velocity relaxation, non-Poisson renewal, empirical identifiability from finite samples, or a thermodynamic singularity. Independent publication-priority assessment and mathematical audit have not been performed.

## References

1. C. Britton, Z. Zhang, S. Han and T. Bertrand, *Run-and-tumble particles with preferred reorientation*, arXiv:2608.23519, first posted 2026-08-24, https://arxiv.org/abs/2608.23519 .
2. F. Mori, P. Le Doussal, S. N. Majumdar and G. Schehr, *Universal Properties of a Run-and-Tumble Particle in Arbitrary Dimension*, arXiv:2006.06989 (2020), https://arxiv.org/abs/2006.06989 .
3. A. Shee and D. Chaudhuri, *Active Brownian motion with speed fluctuations in arbitrary dimensions: exact calculation of moments and dynamical crossovers*, arXiv:2108.12228 (2021), https://arxiv.org/abs/2108.12228 .
4. I. Santra, K. S. Olsen and D. Gupta, *Dynamics of switching processes: general results and applications in intermittent active motion*, *Soft Matter* 20, 9360–9372 (2024), https://doi.org/10.1039/D4SM01054J and https://arxiv.org/abs/2408.16643 .
