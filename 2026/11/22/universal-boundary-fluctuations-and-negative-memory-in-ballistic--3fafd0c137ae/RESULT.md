# Universal boundary fluctuations and negative memory in ballistic threshold resetting

## Finding

A threshold-reset ballistic particle has a uniform stationary position law, yet every bounded position-only observable has *zero extensive time-average variance*. Its centered time integral is an exact regenerative boundary term rather than a sum of independent cycle fluctuations. This yields an endpoint-difference, inverse-observation-time limit law (non-Gaussian in the normalized-position case), an exact variance coefficient, and compulsory negative-lag temporal correlation for every nonconstant Lipschitz spatial observable.

**Theorem.** Fix \(L>0\). On each excursion independently draw a speed \(V>0\), travel at that constant speed from \(L\) toward zero, and instantaneously restart at \(L\) upon hitting zero. Write \(T=L/V\) for an excursion duration. Assume that \(T\) has an absolutely continuous law, \(0<\mathbb E T<\infty\), and \(\mathbb E T^3<\infty\). Construct the stationary, two-sided renewal version of the process.

For any bounded measurable \(g:[0,L]\to\mathbb R\), put
\[
\mu_g=\frac1L\int_0^L g(x)\,dx,\qquad
H_g(u)=\int_0^u\bigl[g(L(1-z))-\mu_g\bigr]dz,\quad0\le u\le1.
\]
Let \(T^*\) have the length-biased law \(\Pr(T^*\in dt)=t\Pr(T\in dt)/\mathbb ET\), and let \(U\) be independent uniform on \([0,1]\). Denote \(Z_g=T^*H_g(U)\), and take \(Z_g',Z_g''\) as independent copies. Then for every \(h\ge0\),
\[
\int_0^h[g(X_s)-\mu_g]ds=F_g(h)-F_g(0),
\quad F_g(t)=T_{\rm cur}(t)H_g\!\left(\frac{A_t}{T_{\rm cur}(t)}\right),
\]
where \(A_t\) is the age and \(T_{\rm cur}(t)\) the full duration of the current excursion. Consequently, as \(h\to\infty\),
\[
h\left(\frac1h\int_0^h g(X_s)ds-\mu_g\right)
\ \Longrightarrow\ Z_g''-Z_g',
\]
and
\[
\lim_{h\to\infty}h^2\operatorname{Var}\left(\frac1h\int_0^h g(X_s)ds\right)
=2\left[\frac{\mathbb ET^3}{\mathbb ET}\int_0^1 H_g(u)^2du
-\left(\frac{\mathbb ET^2}{\mathbb ET}\int_0^1H_g(u)du\right)^2\right].
\]
In particular, the limiting extensive variance rate is zero. For every nonconstant Lipschitz \(g\), the stationary covariance \(\operatorname{Cov}(g(X_0),g(X_t))\) is strictly negative at **some** positive lag.

For the normalized position \(g(x)=x/L\), the last coefficient is
\[
\frac{\mathbb ET^3}{60\mathbb ET}-\frac{(\mathbb ET^2)^2}{72(\mathbb ET)^2}.
\]
If the excursion duration is exponential with rate \(\lambda>0\), it equals \(2/(45\lambda^2)\); this includes the speed density \(\phi(v)=\lambda L v^{-2}\exp(-\lambda L/v)\) for \(v>0\).

## Assumptions and scope

The process is one-dimensional, moves monotonically from a fixed reset point to one threshold at a fixed speed during each excursion, redraws speeds independently, and resets instantaneously. There is no diffusion, refractory period, spatially dependent speed within an excursion, or interaction between particles. Stationary initialization is part of the theorem. The continuous excursion-time law excludes synchronized deterministic periods; a finite third moment provides the stated limiting second moments. The time-average result is for fixed bounded spatial observables and does not assert uniformity over an expanding class of observables.

## Proof

**1. Each excursion is uniform in traversed position.** On a cycle of duration \(T\), at cycle age \(a\in[0,T]\) one has \(X=L(1-a/T)\). Hence
\[
\int_0^T g(X_s)ds=T\int_0^1g(L(1-z))dz=T\mu_g.
\]
Thus the centered reward is **exactly zero on every completed cycle**, not only in expectation. The stationary one-point law is uniform: the equilibrium cycle is length biased, and conditional on its duration the fraction already elapsed is uniform.

**2. An exact pathwise coboundary.** Define \(F_g=T H_g(a/T)\) inside each excursion. Almost everywhere along an excursion, \(dF_g/dt=g(X_t)-\mu_g\). Since \(H_g(0)=H_g(1)=0\), \(F_g\) is continuous at every resetting instant, even though \(X_t\) jumps. Integrating over arbitrary finite intervals proves the endpoint identity without a renewal approximation. For bounded \(g\), \(|F_g|\le2T\|g\|_\infty\).

**3. Endpoint law and mixing.** In stationary renewal theory the current interval has size-biased duration \(T^*\) and its age fraction is independent uniform \(U\). Hence every fixed-time \(F_g\) has law \(Z_g\). An absolutely continuous, finite-mean renewal law is nonarithmetic and its stationary regenerative process is mixing: distant equilibrium cycle observations become independent. Applying this fact to bounded test functions of the two endpoint variables gives their joint convergence to \((Z_g',Z_g'')\). The exact coboundary then proves the distributional limit. Since \(\mathbb E[(T^*)^2]=\mathbb ET^3/\mathbb ET<\infty\), truncation in \(L^2\) upgrades endpoint decorrelation to convergence of covariances and establishes the variance formula.

**4. Negative covariance cannot be avoided.** For nonconstant Lipschitz \(g\), \(C_g(0)=\operatorname{Var}(g(U_L))>0\), where \(U_L\) is uniform on \([0,L]\), and \(C_g(t)\) is continuous at zero. If \(C_g(t)\ge0\) for every \(t\ge0\), the stationary covariance identity
\[
\operatorname{Var}\left(\int_0^h(g(X_s)-\mu_g)ds\right)
=2\int_0^h(h-t)C_g(t)dt
\]
would diverge at least linearly with \(h\). This contradicts its bounded limit \(2\operatorname{Var}(Z_g)\). Thus some strictly negative lag exists. This does not prove a unique crossing or a fixed sign for every later lag.

**5. Explicit normalized-position moments.** For \(g(x)=x/L\), \(H_g(u)=u(1-u)/2\). Elementary integration gives \(\int_0^1H_g(u)du=1/12\) and \(\int_0^1H_g(u)^2du=1/120\), yielding the displayed expression. Exponential duration moments are \(\mathbb ET^k=k!/\lambda^k\), which give \(2/(45\lambda^2)\). The limit for normalized position is non-Gaussian: each endpoint variable is nonnegative and nondegenerate, hence cannot be Gaussian; Cramér's Gaussian-convolution theorem excludes a Gaussian difference of two independent copies.

## Verification

The fully standalone `check.py` reproduces the pathwise endpoint identity on 2,400 random equilibrium-start trajectory segments, using both normalized position and the indicator of the upper half of the interval. It independently checks the exact exponential-duration moment reduction and a size-biased equilibrium Monte Carlo test with 220,000 samples. Run `python3 check.py`; no nonstandard packages are required. Numerical experiments corroborate finite identities and moments; the infinite-time limit is proved above by renewal mixing and is not inferred from simulation.

## Relationship to prior work

Das, Majumdar and Pal (2026), arXiv:2611.16733v1, introduce the same ballistic threshold-reset model and derive its universal one-time uniform stationary density, relaxation and shock behavior. Those results do not give the centered occupation-integral coboundary, its non-Gaussian endpoint fluctuation limit, the exact inverse-time variance coefficient, or the compulsory negative-lag covariance. General renewal-reward theory supplies cycle averages and stationary age laws, which are acknowledged as inputs; the key model-specific structural step is the simultaneous zero centered reward for **every** spatial observable and its continuous pathwise primitive. Threshold-reset sluggish diffusion studies a diffusive excursion, whose centered reward is not identically zero on each cycle and therefore does not imply this theorem.

## Limitations

The finding does not address noisy or discretely sampled positions, finite reset duration, acceleration, imperfect resetting, interacting particles, or any observable depending on velocity or renewal age rather than position alone. Without a finite third duration moment the pathwise coboundary remains true but the variance coefficient may be infinite. With perfectly periodic deterministic durations endpoint mixing fails and the stated independent-copy limit need not hold. Generic coboundary and renewal-reward theories remain sources of possible implicit prior coverage; the argument claims no independent audit or priority guarantee.

## References

1. R. Das, S. N. Majumdar, A. Pal, *Freezing transition and shock-like transients in ballistic random walks under threshold resetting*, arXiv:2611.16733v1 (first publicly posted 2026-11-12), https://arxiv.org/html/2611.16733v1 .
2. R. G. Gallager, *Discrete Stochastic Processes*, Chapter 4.4, *Renewal-Reward Processes and Time-Averages*, https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Signal_Processing_and_Modeling/Discrete_Stochastic_Processes_%28Gallager%29/04%3A_Renewal_Processes/4.04%3A_Renewal-Reward_Processes_and_Time-Averages .
3. *Renewal Limit Theorems*, Random Services, section on key renewal theorems and equilibrium ages, https://www.randomservices.org/random/renewal/LimitTheorems.html .
4. T. D. Frimpong et al., *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962 (2026), https://arxiv.org/abs/2610.21962 .
