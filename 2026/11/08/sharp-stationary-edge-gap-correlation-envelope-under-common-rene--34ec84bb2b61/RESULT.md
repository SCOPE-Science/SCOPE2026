# Sharp stationary edge-gap correlation envelope under common renewal resetting

## Finding
Consider an equilibrium renewal-reset gas of \(N\) independent Brownian particles, jointly returned to the origin at every reset. For any two **distinct, fixed** ranks \(k,\ell\geq1\), write \(\Delta_{k,N}=M_{k,N}-M_{k+1,N}\) for the gap between the \(k\)-th and \((k+1)\)-th rightmost stationary positions. If the independent reset intervals \(T\) satisfy \(\Pr(T>0)=1\), \(0<\mathbb E T<\infty\), and \(\mathbb E T^2<\infty\), then

\[
\lim_{N\to\infty}\operatorname{Corr}(\Delta_{k,N},\Delta_{\ell,N})
=\frac{9-8\kappa_T}{18-8\kappa_T},\qquad
\kappa_T=\frac{(\mathbb E T^{3/2})^2}{\mathbb E T\,\mathbb E T^2}.
\]

The exact, sharp attainable interval over **all** such renewal laws is

\[
\boxed{\left[\frac1{10},\frac12\right).}
\]

The lower endpoint is attained **if and only if** the reset interval is deterministic. Every number strictly between the endpoints is attained by a two-point inter-reset law; the upper endpoint is never attained but can be approached arbitrarily closely. This conclusion does not depend on the two distinct fixed ranks, the diffusivity, or the time-scale of the clock. In particular, even an exactly periodic common reset clock leaves a strictly positive \(1/10\) asymptotic correlation between different edge gaps.

## Assumptions and scope
Fix \(D>0\). There are \(N\geq\max\{k,\ell\}+1\) particles independently following \(dX_i=\sqrt{2D}\,dB_i\) between reset events, with Brownian motions independent of the renewal clock and one another. At each common reset event, all positions are set to zero. The stationary observation is taken in the **equilibrium renewal ensemble**, not by synchronizing observation to a reset. \(T\) is an arbitrary positive inter-reset interval, including deterministic and lattice laws, with finite nonzero mean \(\mu=\mathbb E T\) and finite second moment. The ranks \(k\neq\ell\) are fixed as \(N\to\infty\); no bulk-rank or growing-rank claim is made. Pearson correlations are well-defined for each \(N\) under these moment assumptions.

The stationary backward recurrence age \(A\) has density
\[
 f_A(a)=\frac{\Pr(T>a)}{\mu},\qquad a>0,
\]
and moments \(\mathbb E A^p=\mathbb E T^{p+1}/((p+1)\mu)\) whenever the right side is finite. Conditional on \(A=a\), the positions are independent centered Gaussians of variance \(2Da\). Equivalently, for independent standard normals \(Z_i\) independent of \(A\), their stationary joint law is \((X_i)_{i\leq N}\stackrel d=\sqrt{2DA}(Z_i)_{i\leq N}\).

## Proof
**Step 1: a joint edge-spacing limit with moment convergence.** Let \(b_N=\Phi^{-1}(1-1/N)\) for \(N\geq3\), and let \(G_{k,N}\) be the \(k\)-th descending adjacent gap in \(N\) independent standard Gaussians. Classical Gumbel-domain exponential-spacing theory, or the representation of upper-order Gaussian tail uniforms, gives for any finite collection of fixed ranks
\[
 (k b_NG_{k,N})_{k\leq m}\ \Longrightarrow\ (E_k)_{k\leq m},
\]
where \(E_1,\ldots,E_m\) are independent unit-mean exponential variables. We require moment convergence, not just weak convergence. Here is a direct uniform-integrability bound.

Set \(U_i=1-\Phi(Z_i)\), and let \(U_{(j)}\) be their increasing order statistics. On the event \(U_{(k)}\geq N^{-2}\) and \(U_{(k+1)}\leq N^{-1/2}\), the inverse-tail derivative and the Gaussian Mills bound imply, for a constant \(C_k\) independent of sufficiently large \(N\),
\[
 0\leq k b_NG_{k,N}\leq C_k\log\frac{U_{(k+1)}}{U_{(k)}}.
\]
The ratio \(U_{(k)}/U_{(k+1)}\) is exactly \(\operatorname{Beta}(k,1)\), so the logarithm has an exponential distribution with rate \(k\), uniformly in \(N\). The exceptional event has probability \(O(N^{-k})+O(e^{-c\sqrt N})\): use a binomial union bound for the first part and a binomial lower-tail bound for the second. Its contribution to any fixed moment vanishes by Hölder's inequality and the standard bound \(\mathbb E[\max_{i\le N}|Z_i|^p]=O((\log N)^{p/2})\). Thus \(k b_NG_{k,N}\) are uniformly integrable to every fixed moment order, and their first, second and pairwise mixed moments converge to those of the independent exponentials. This justifies every covariance passage below.

**Step 2: mixing over the renewal age.** The exact stationary Gaussian-scale representation gives
\[
 \frac{k b_N\Delta_{k,N}}{\sqrt{2D}}
 \stackrel d=\sqrt A\,(k b_NG_{k,N}).
\]
The factor \(A\) is independent of all Gaussian gaps. Since \(\mathbb E A<\infty\), Step 1 proves joint weak convergence together with first and second moments:
\[
 \left(\frac{k b_N\Delta_{k,N}}{\sqrt{2D}}\right)_{k\le m}
 \Longrightarrow (\sqrt A E_k)_{k\le m}.
\]
For distinct indices, the limiting covariance is \(\mathbb E A-(\mathbb E\sqrt A)^2\), while either marginal variance is \(2\mathbb E A-(\mathbb E\sqrt A)^2\). Hence the limiting correlation is
\[
 \frac{\mathbb E A-(\mathbb E\sqrt A)^2}
 {2\mathbb E A-(\mathbb E\sqrt A)^2}.
\]
With \(\mathbb E A=\mathbb E T^2/(2\mu)\) and \(\mathbb E\sqrt A=2\mathbb E T^{3/2}/(3\mu)\), this simplifies to the claimed rational function of \(\kappa_T\).

**Step 3: sharp global optimization and all interior values.** Cauchy–Schwarz applied to \(T^{1/2}\) and \(T\) yields \(0<\kappa_T\leq1\). Equality holds exactly when \(T^{1/2}\) is proportional to \(T\) almost surely, which for \(T>0\) means that \(T\) is constant almost surely. The function \((9-8\kappa)/(18-8\kappa)\) is strictly decreasing in \(\kappa\), so it ranges from \(1/10\) to, but not including, \(1/2\).

For sharpness and attainability, take \(T_R\) on \(\{1,R\}\) with \(\Pr(T_R=R)=R^{-3/2}\), \(R\ge1\). At \(R=1\), the law is deterministic and \(\kappa_{T_R}=1\). As \(R\to\infty\), \(\mathbb E T_R\to1\), \(\mathbb E T_R^{3/2}\to2\), and \(\mathbb E T_R^2\sim R^{1/2}\), so \(\kappa_{T_R}\to0\) and the correlation tends to \(1/2\). The continuous image of the connected parameter interval \([1,\infty)\), including its lower value and with values approaching its supremum, attains every value in \([1/10,1/2)\). These arguments are exact and do not rely on a numerical truncation.

## Verification
The standalone `checker.py` (Python 3 with NumPy and SciPy) checks the exact deterministic endpoint, the exponential-clock special case \(\rho=(4-\pi)/(8-\pi)\), the two-point near-supremum sequence, the Cauchy–Schwarz envelope over 10,000 randomized discrete laws, 120 exact finite-sample reset-age scale-cancellation tests, and finite-size Brownian-gas simulations for deterministic and exponential reset ages. It passed all assertions. Finite Monte Carlo is illustrative, **not** a proof of the \(N\to\infty\) limit, nor of the sharp optimization. The analytical steps above carry those claims.

For an independent reproducibility check, define \(Q_{k,N}=k b_N\Delta_{k,N}/\sqrt{N^{-1}\sum_i X_i^2}\). The Gaussian radial/angular decomposition makes the finite-\(N\) vector \((Q_{k,N})_{k\le m}\) independent of the common age and of the empirical energy, and its distribution is unaffected by the clock and \(D\). Its limiting coordinates are independent \(\operatorname{Exp}(1)\) variables. This supporting pivot distinguishes common-scale gap dependence from intrinsic Gaussian-order dependence.

## Relationship to prior work
Biroli, Larralde, Majumdar and Schehr (arXiv:2211.00563, initially public November 1, 2022) derived the correlated Brownian-reset gas and individual spacing distributions for Poisson resetting. De Mauro, Biroli, Majumdar and Schehr (arXiv:2509.06658, initially public September 8, 2025), especially Sections III and V and Eqs. (124)–(132), derived the general renewal-reset stationary conditionally independent Gaussian-mixture law and **single-gap** scaling functions. Nagaraja, Bharath and Zhang (arXiv:1702.05910) established joint classical extreme-order-spacing limits. These ingredients are credited here. What they do not separately state is the sharp **cross-gap** correlation envelope over all renewal laws, the deterministic lower obstruction, the unattainable universal upper endpoint, and realization of every intermediate dependence level. The finite-second-moment clock optimization and equality cases supply the new classification, beyond changing a single-gap scaling function.

## Limitations
The theorem concerns stationary equilibrium-renewal observations and fixed edge ranks; it does not describe synchronized periodic snapshots, correlations across distinct physical observation times, bulk spacings, growing ranks, independent per-particle reset clocks, or clocks with infinite second moment. Its correlation range is an asymptotic-in-particle-number statement, not a finite-\(N\) exact inequality. Existing full stationary joint-density formulas in the literature imply the underlying Gaussian mixture; the sharp optimization is the specific derived contribution. Broader unindexed correlation inequalities could affect publication priority, and independent review has not been performed.

## References
1. M. Biroli, H. Larralde, S. N. Majumdar, G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563 (first posted November 1, 2022), https://arxiv.org/abs/2211.00563 .
2. G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (first posted September 8, 2025), https://arxiv.org/abs/2509.06658 .
3. H. N. Nagaraja, K. Bharath, F. Zhang, *Spacings Around An Order Statistic*, arXiv:1702.05910 (first posted February 20, 2017), https://arxiv.org/abs/1702.05910 .
