# Sharp positive-temperature spatial correlation prefactor in globally Pareto-reset Glauber chains

## Finding

Consider the infinite, translation-invariant, zero-field nearest-neighbor Glauber–Ising chain on \(\mathbb Z\), started from one independent symmetric spin configuration and globally reset to **that same initial configuration** at iid Pareto-renewal times. Let the reset waiting-time density be \(\rho(t)=\alpha\tau_0^\alpha t^{-\alpha-1}\mathbf1_{\{t\ge\tau_0\}}\), with \(\alpha>1\) and \(\tau_0>0\), and observe the stationary equilibrium-age, annealed law.

For every **fixed strictly positive and finite temperature**, with coupling \(J>0\) and \(0<\beta J<\infty\), write
\[
 \gamma=\tanh(2\beta J)\in(0,1),\qquad \eta=\tanh(\beta J),\qquad q=\alpha-1>0.
\]
The annealed connected two-spin correlation at separation \(n\) satisfies the **sharp asymptotic with exact coefficient**
\[
 \boxed{\mathbb E[\sigma_0\sigma_n]\sim
 \frac{\tau_0^q}{\alpha}\bigl(2\sqrt{1-\gamma^2}\bigr)^q\;n^{-q}\eta^n}\qquad(n\to\infty).
\]
For every positive integer \(n\), it also obeys the exact killed first-passage/renewal identity stated in the proof and the bound \(0<C_n\le\eta^n\). Hence \(\chi_{\rm sp}=1+2\sum_{n\ge1} C_n<\infty\), and the block-average magnetization of \(L\) consecutive sites has variance \(\chi_{\rm sp}/L+o(L^{-1})\). The novel quantitative statement is the **nontrivial polynomial factor and its explicit constant at every fixed positive temperature**; the last, summability consequence is routine once exponential clustering is known.

## Precise scope

Spins take values \(\sigma_i\in\{-1,+1\}\), \(i\in\mathbb Z\). Between globally synchronized resets, the generator flips spin \(i\) at rate
\[
 w_i(\sigma)=\frac12\left(1-\frac\gamma2\sigma_i(\sigma_{i-1}+\sigma_{i+1})\right).
\]
The initial configuration is sampled once with iid fair spins, and every reset returns the *entire infinite chain* to this same configuration. Fresh Glauber noise is used between resets, independently of the reset clock and initial spins. Both the covariance and stationarity are annealed over all randomness, with the reset age distributed according to the equilibrium renewal law. The limit is over separation \(n\to\infty\), for fixed \(\alpha,\tau_0,\beta J\). There is **no uniform joint low-temperature scaling claim**, and this result does not assert a new zero-temperature theorem, local sitewise resetting, a quenched identity, or a finite-ring approximation.

## Proof

**1. Closed pair evolution and killed hitting time.** By the Glauber generator and translation invariance the no-reset pair correlation \(c_n(t)\), starting from independent fair spins, is the unique bounded solution of
\[
 \dot c_n=-2c_n+\gamma(c_{n-1}+c_{n+1}),\quad n\ge1;
 \qquad c_0(t)=1,\quad c_n(0)=0\ (n\ge1).
\]
Let \(T_n\) be the hitting time of zero of the continuous-time symmetric walk starting at \(n\), jumping **in each direction at rate \(\gamma\)**. Set \(\delta=2(1-\gamma)>0\). The backward equation and the same boundary/initial values give the exact representation
\[
 c_n(t)=\mathbb E_n\left[e^{-\delta T_n}\mathbf1_{\{T_n\le t\}}\right].\tag{1}
\]
The walk hits zero almost surely. Writing \(\kappa_\gamma(s)=\operatorname{arcosh}(1+s/(2\gamma))\), the unique bounded root of the second-order hitting-time recurrence yields
\[
 \mathbb E_n[e^{-sT_n}]=e^{-n\kappa_\gamma(s)},\qquad s\ge0.\tag{2}
\]
By the strong Markov property the time from \(n\) to zero is a sum of \(n\) iid copies of the time from one to zero (on the full half-line with absorbing zero).

**2. Exact renewal mixing.** For waiting times with the stated Pareto density, the mean is \(\mu=\alpha\tau_0/(\alpha-1)\). The equilibrium backward age \(A\), independent of the dynamics in the last interval, has survival function
\[
 H(t):=\Pr(A\ge t)=\begin{cases}
 1-t/\mu,&0\le t\le\tau_0,\\[2pt]
 (\tau_0^q/\alpha)t^{-q},&t\ge\tau_0.
 \end{cases}\tag{3}
\]
The two formulas match at \(t=\tau_0\). Conditioning on \(A\), using (1) and nonnegative Tonelli integration gives the exact finite-distance identity
\[
 C_n=\mathbb E[c_n(A)]=\mathbb E_n[e^{-\delta T_n}H(T_n)].\tag{4}
\]
The spin mean is zero by global flip symmetry, so this pair expectation is connected.

**3. Exponential tilt and exact prefactor.** Evaluate (2) at \(s=\delta\):
\[
 \mathbb E_n[e^{-\delta T_n}]=e^{-n\kappa_\gamma(\delta)}=\eta^n,
 \qquad \eta=\frac{1-\sqrt{1-\gamma^2}}\gamma=\tanh(\beta J).
\]
Tilting the law of \(T_n\) by \(e^{-\delta T_n}/\eta^n\) preserves its decomposition into \(n\) iid tilted one-step passage times. Their finite positive mean is
\[
 m_\gamma=\kappa_\gamma'(\delta)
 =\frac1{\sqrt{\delta(\delta+4\gamma)}}
 =\frac1{2\sqrt{1-\gamma^2}}.
\]
By the strong law, \(T_n/n\to m_\gamma\) in tilted probability. The tilted one-step time has a Laplace transform in a neighborhood of zero, so the lower-tail event \(T_n<nm_\gamma/2\) has tilted probability at most \(e^{-cn}\) for some \(c>0\). On its complement, for all sufficiently large \(n\), (3) yields
\[
 n^qH(T_n)=\frac{\tau_0^q}{\alpha}(T_n/n)^{-q}
 \le \frac{\tau_0^q}{\alpha}(m_\gamma/2)^{-q}.
\]
The right-hand expression converges in tilted probability to \(\tau_0^q/(\alpha m_\gamma^q)\). The excluded lower tail contributes at most \(n^qe^{-cn}\) since \(H\le1\). Dominated convergence in probability on the bounded remainder therefore establishes
\[
 \lim_{n\to\infty}\frac{C_n}{\eta^nn^{-q}}
 =\frac{\tau_0^q}{\alpha m_\gamma^q}
 =\frac{\tau_0^q}{\alpha}(2\sqrt{1-\gamma^2})^q,
\]
which proves the main claim. The exact inequality \(0<C_n\le\eta^n\) follows from (4), \(0<H\le1\), and (2). The identity for block variance is
\[
 \operatorname{Var}\left(L^{-1}\sum_{i=1}^{L}\sigma_i\right)
 =L^{-2}\left[L+2\sum_{n=1}^{L-1}(L-n)C_n\right];
\]
absolute summability gives \(\chi_{\rm sp}/L+o(L^{-1})\) by dominated convergence.

## Prior work and originality boundary

The **zero-temperature** power-law spatial correlation coefficient, critical \(\alpha=3/2\) susceptibility transition, and full three-regime block-variance asymptotics are already established by the earlier result *Algebraic spatial correlations and a sharp susceptibility threshold in a globally reset kinetic Ising chain*, published 2026-11-02, https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-algebraic-spatial-correlations-and-a-sharp-susceptibility-thresh--da40ba33c965 . Its zero-temperature theorem is even more general in allowing nonzero mean initial spins. **None of those zero-temperature claims is presented as new here.** Classical Glauber pair evolution and renewal-age mixing are also acknowledged antecedents.

Anagha V. K. and Apoorva Nagar, *Ising model with power law resetting*, Physical Review Research 8, 023197 (2026), DOI:10.1103/d3hg-bgmh, https://journals.aps.org/prresearch/pdf/10.1103/d3hg-bgmh , analyzes magnetization distributions under global heavy-tail resetting and motivates studying spatial correlations. Earlier work on Poisson resetting or independent sitewise resetting changes the reset-clock geometry. The original kinetic pair equations are due to R. J. Glauber, *Time-Dependent Statistics of the Ising Model* (1963), DOI:10.1063/1.1703954.

The contribution here is confined to the **positive-temperature exact exponential-times-power coefficient** for common Pareto renewal resetting. An unindexed general theorem about tilted coalescence/renewal may still imply this asymptotic; no guarantee of historical priority is made.

## Limitations and verification

The formulas depend on the specified generator time normalization and on equilibrium-age, annealed resetting to one frozen iid configuration. The positive-temperature result does not commute uniformly with a zero-temperature limit. Finite first-passage integrations or simulations can corroborate, but do not prove, the asymptotic. The proof is entirely analytic, relying on explicit renewal survival, the walk Laplace transform, and a tilted law of large numbers with an exponential lower-tail bound. A claim of formal verification, expert attestation, or independent external certification is not made.
