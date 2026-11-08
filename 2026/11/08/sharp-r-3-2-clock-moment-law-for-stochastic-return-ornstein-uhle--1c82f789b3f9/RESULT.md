# Sharp \(r^{-3/2}\) clock-moment law for stochastic-return Ornstein–Uhlenbeck search

## Finding

For fast **arbitrary positive resetting clocks**, not just exponential clocks, the mean completion time of a two-stiffness Ornstein–Uhlenbeck search approaches the pure-return first-passage mean with the sharp, distribution-sensitive law
\[
M_r=M_2+(k_1-k_2)S_2\sqrt{\pi}\,
\frac{\mathbb E[W^2]}{\mathbb E[\sqrt W]}
\,r^{-3/2}+o(r^{-3/2}).
\]
Here \(W\) is the dimensionless waiting time and \(S_2=\int_0^1e^{k_2y^2/2}\,dy\). For equal-mean clocks, the leading coefficient depends only on the *second* and *square-root* clock moments. In particular, a deterministic clock \(W=1\) has multiplier \(\sqrt\pi S_2\), whereas a unit-mean exponential clock has multiplier \(4S_2\); the latter is \(4/\sqrt\pi\) times as large in magnitude, for unequal stiffnesses. If \(k_1=k_2\), the mean is exactly \(M_2\) at **every** clock scale, not merely asymptotically.

## Assumptions and scope

Fix \(k_1\ge0\), \(k_2>0\), and independent standard Brownian motions within successive excursions. During each search excursion a process starts at \(0\) and solves \(dX_t=-k_1X_t\,dt+\sqrt2\,dB_t\) until it reaches the absorbing target \(1\) or an independent clock \(R_r=W/r\), where \(r>0\). Assume \(W>0\) almost surely, \(\mathbb E[W^2]<\infty\), and each clock and diffusion excursion is independently resampled. If the clock rings before the target is hit, the same position begins a *return* OU diffusion of stiffness \(k_2\), with unchanged diffusion coefficient. This return is stopped on hitting the origin or target; target detection continues during return. Hitting \(0\) restarts a statistically independent search excursion, and hitting \(1\) completes the process. Denote the total expected completion time by \(M_r\). The theorem concerns the limit \(r\to\infty\) at fixed stiffnesses and fixed clock law; it does not require an exponential clock.

Define
\[
K(x)=e^{k_2x^2/2}\int_{-\infty}^{x}e^{-k_2z^2/2}\,dz,\qquad
S(x)=\int_0^xe^{k_2y^2/2}\,dy,\qquad
S_2=S(1),\qquad M_2=\int_0^1K(y)\,dy.
\]
Then \(M_2\) is the mean time for uninterrupted OU dynamics of stiffness \(k_2\), starting from \(0\), to hit \(1\). All these quantities are finite and \(S_2>0\).

## Proof

**1. The pure-return potential.** For \(x<1\) define \(U(x)=\int_x^1K(y)\,dy\). Direct differentiation gives \(K'(x)=1+k_2xK(x)\), so
\[
(\partial_x^2-k_2x\partial_x)U=-1,\quad U(1)=0,\quad U(0)=M_2.
\]
Consequently \(U(x)\) is the unrestricted return-OU mean hitting time of the target from \(x\). On \((0,1)\), the return diffusion hits \(1\) before \(0\) with probability \(H(x)=S(x)/S_2\), by the scale-function equation. Put \(H(x)=0\) for \(x\le0\). The return stopped at \(0\) or \(1\) has finite mean duration for every initial \(x<1\), since \(k_2>0\). Its expected terminal potential is \((1-H(x))M_2\).

**2. Exact cycle identity for every clock law.** Let \(\tau=\inf\{t\ge0:X_t=1\}\) under the search process, and let \(\mathcal L_1=\partial_x^2-k_1x\partial_x\). Define the per-cycle success probability
\[
p_r=\Pr(\tau<R_r)+\mathbb E[\mathbf1_{\{R_r<\tau\}}H(X_{R_r})]
\]
and the occupation functional
\[
A_r=\mathbb E\int_0^{\tau\wedge R_r}X_tK(X_t)\,dt.
\]
Both are finite, and \(p_r>0\). As \(U'(x)=-K(x)\), the generator difference is exactly
\[
1+\mathcal L_1U(x)=(k_1-k_2)xK(x).
\]
Apply Dynkin's formula until \(\tau\wedge R_r\), then apply the return-stage mean-hitting-time identity from step 1 at the random search endpoint. A complete cycle has mean duration \(p_rM_2+(k_1-k_2)A_r\) and succeeds with probability \(p_r\). Renewal over independent cycles therefore proves, *without a Poisson assumption*,
\[
\boxed{M_r-M_2=(k_1-k_2)\frac{A_r}{p_r}.}
\]
This also establishes the exact equality \(M_r=M_2\) for \(k_1=k_2\). Finite mean cycle duration follows from \(\mathbb E[W^2]<\infty\) and the logarithmic-or-better growth of return-OU hitting times toward the negative half-line, while positive per-cycle success gives finite total mean.

**3. Fast search excursions.** Define
\[
g(t)=\mathbb E_0[X_tK(X_t);\tau>t],\quad
h(t)=\mathbb E_0[H(X_t);\tau>t].
\]
At short times the absorbing boundary at \(1\) changes Gaussian OU expectations by an exponentially small term in \(1/t\). Since \(F(x)=xK(x)\) satisfies \(F(0)=0\) and \(\mathcal L_1F(0)=F''(0)=2\), the short-time diffusion semigroup yields
\[
g(t)=2t+O(t^2).
\]
The centered search OU position has variance \(2t+O(t^2)\). As \(H(x)=x/S_2+O(x^3)\) for small positive \(x\), and \(H(x)=0\) for negative \(x\), a half-Gaussian first-moment calculation gives
\[
h(t)=\frac{\sqrt t}{S_2\sqrt\pi}+O(t^{3/2}).
\]
Furthermore, \(g(t)\) is bounded by \(Ct\) for all \(t>0\) (the function \(F\) is bounded on the killed domain), and \(0\le h(t)\le C\sqrt t\). The direct success probability satisfies \(\Pr(\tau\le t)\le Ct^2\) for all \(t>0\), by the small-time Gaussian boundary tail and the trivial bound at large times.

**4. Passage to an arbitrary fast clock.** Conditioning on \(W\) gives
\[
A_r=\mathbb E\int_0^{W/r}g(t)\,dt,
\qquad
p_r=\mathbb E[\Pr(\tau\le W/r)]+\mathbb E[h(W/r)].
\]
The bounds of step 3 and \(\mathbb E[W^2]<\infty\) justify dominated convergence, yielding
\[
\lim_{r\to\infty}r^2A_r=\mathbb E[W^2],
\qquad
\lim_{r\to\infty}\sqrt r\,p_r=
\frac{\mathbb E[\sqrt W]}{S_2\sqrt\pi}.
\]
The direct search-success term is \(O(r^{-2})\) and thus does not contribute to the second limit. Dividing these limits in the exact identity from step 2 proves the stated asymptotic with the exact nonzero coefficient whenever \(k_1\ne k_2\). For \(W\equiv1\), \(\mathbb E W^2=\mathbb E\sqrt W=1\). For \(W\) exponential with mean one, \(\mathbb E W^2=2\) and \(\mathbb E\sqrt W=\sqrt\pi/2\), giving the two displayed multipliers.

## Verification

Run \(\texttt{python CHECKER.py}\) with Python, SciPy, and NumPy installed. The script independently evaluates the killed Brownian heat kernel for deterministic and two-point clock distributions and the killed Brownian resolvent for an exponential clock, using \(k_1=0\), \(k_2=2\), and target \(1\). It verifies both the exact cycle-potential identity (by an independent return-duration renewal integral) and the distinct predicted moment-ratio limits. It prints a PASS line and the numerical limiting multipliers. Finite numerical tests support the analytic derivation but do not prove its arbitrary-clock extension.

## Relationship to prior work

Dubey and Pal (arXiv:2610.18814v1, first public 13 October 2026) introduced and analyzed this switching harmonic-potential model with **Poisson resetting**, gave a general all-rate MFPT expression and observed its high-rate saturation to the return-OU MFPT. That exact Poisson expression and its saturation are pre-existing results, not claimed here. The present statement concerns a **non-exponential, arbitrary finite-second-moment clock family** and identifies its universal leading fast-clock correction through two fractional clock moments. Biswas, Kundu and Pal (arXiv:2307.16294) already developed an arbitrary-clock, stochastic-return renewal framework; the cycle framework itself is not new. Biswas, Dubey, Kundu and Pal (arXiv:2406.08975v1) studied drift-diffusion search with a linear return potential and a separate optimization question. Neither the renewal framework nor the Poisson-only switching-trap formula directly states the present two-moment high-frequency law.

## Limitations

This theorem applies to the specified one-dimensional diffusion with unchanged noise strength, positive harmonic return stiffness, independent renewal cycles and strictly positive clock scale variables with finite second moment. It is pointwise in the fixed stiffnesses and clock law, not uniform over clock distributions or a vanishing return stiffness. No optimal resetting clock or full finite-rate ordering is asserted; only the leading fast-clock coefficient and the exact equal-stiffness identity are proved. A stronger or unindexed earlier fast-clock theorem could change publication priority. The numerical checks do not substitute for the infinite-rate proof.

## References

1. A. Dubey and A. Pal, *Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols*, arXiv:2610.18814v1 (13 October 2026), https://arxiv.org/html/2610.18814v1 .
2. A. Biswas, A. Kundu and A. Pal, *Search with stochastic home-returns can expedite classical first passage under resetting*, arXiv:2307.16294 (2023), https://arxiv.org/abs/2307.16294 .
3. A. Biswas, A. Dubey, A. Kundu and A. Pal, *Drift-diffusive resetting search process with stochastic returns: speed-up beyond optimal instantaneous return*, arXiv:2406.08975v1 (2024), https://arxiv.org/html/2406.08975v1 .
