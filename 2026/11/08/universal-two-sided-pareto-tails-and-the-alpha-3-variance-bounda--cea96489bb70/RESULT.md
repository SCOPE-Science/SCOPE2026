# Universal two-sided Pareto tails and the \(\alpha=3\) variance boundary for conditionally reset quantum walks

## Finding

Let a continuous-time nearest-neighbor quantum walker on \(\mathbb Z\) evolve between resets under
\[
H=-\frac{\gamma}{2}\sum_{m\in\mathbb Z}(|m\rangle\langle m+1|+|m+1\rangle\langle m|),\qquad\gamma>0.
\]
After independent inter-reset durations with Pareto density \(f(t)=\alpha\tau_0^\alpha t^{-1-\alpha}\) for \(t\ge\tau_0>0\), the particle is conditionally reset to either of two finite sites \(n_l<0<n_r\). The conditional choice is determined by the observed side of the origin, with equal splitting at the origin. Assume \(\alpha>1\). Let \(\pi\) denote the unique invariant law of the two-site embedded reset chain and put \(b=\pi_l n_l+\pi_r n_r\).

The time-stationary site occupation \(p_m\) exists and, for positive integers \(n\to\infty\) with the reset sites fixed, obeys the simultaneous two-tail asymptotics
\[
\boxed{p_n=K_\alpha n^{-\alpha}\left(1+\frac{\alpha b}{n}+O(n^{-2})\right),\quad
p_{-n}=K_\alpha n^{-\alpha}\left(1-\frac{\alpha b}{n}+O(n^{-2})\right),}
\]
where the positive, protocol-independent amplitude is
\[
\boxed{K_\alpha=\frac{\alpha-1}{\alpha}(\gamma\tau_0)^{\alpha-1}
\frac{\Gamma(\alpha)}{2^\alpha\Gamma((\alpha+1)/2)^2}.}
\]
In particular, \(p_n/p_{-n}\to1\) even when the reset protocol induces a globally asymmetric stationary profile, and the first relative directional correction is
\[
\frac{p_n-p_{-n}}{p_n+p_{-n}}=\frac{\alpha b}{n}+O(n^{-2}).
\]
For every real \(q>0\), the stationary \(q\)-th absolute position moment is finite **if and only if** \(\alpha>q+1\). Hence the existence of a normalized stationary occupation law for \(\alpha>1\) does not imply a finite stationary mean-squared displacement: the latter requires \(\alpha>3\), and then exactly
\[
\boxed{\mathbb E_{\mathrm{st}}X^2=\pi_l n_l^2+\pi_r n_r^2+
\frac{\gamma^2\tau_0^2(\alpha-1)}{6(\alpha-3)}.}
\]
At the borderline \(\alpha=3\), the spatially truncated stationary second moment has the sharp logarithmic law
\[
\boxed{\sum_{|m|\le N}m^2p_m=\frac{\gamma^2\tau_0^2}{3}\log N+O(1)\qquad(N\to\infty).}
\]

## Assumptions and scope

The lattice is the entire \(\mathbb Z\): there are no reflecting, absorbing, periodic, or finite-size boundaries. Each duration is sampled independently of earlier durations and of the reset location chosen at the *start* of its interval. At the end of the interval, the walker is measured in the site basis and reset to \(n_r\) if the measured site is positive, to \(n_l\) if negative, and with probability \(1/2\) to either if it is zero. A reset starts a new pure site state. Any finite initial site is allowed. No external time-dependent field or coherent cross-cycle memory is retained.

For \(j,k\in\{n_l,n_r\}\), define \(Q_{jk}=\int_{\tau_0}^\infty f(t)\Omega_k(j,t)\,dt\), where
\[
\Omega_{n_r}(j,t)=\sum_{m\ge1}J_{m-j}(\gamma t)^2+\tfrac12J_{-j}(\gamma t)^2,
\quad
\Omega_{n_l}(j,t)=\sum_{m\le-1}J_{m-j}(\gamma t)^2+\tfrac12J_{-j}(\gamma t)^2.
\]
Every entry of \(Q\) is strictly positive, so \(\pi Q=\pi\) and \(\pi_l+\pi_r=1\) have a unique positive solution. In the asymptotic statements the sites, \(\alpha\), \(\gamma\), and \(\tau_0\) remain fixed while \(n\to\infty\). The result extends to any finite reset-site mechanism with an irreducible embedded chain, provided the next waiting time is independent of its starting reset mark.

## Proof

**1. Renewal-age occupation.** The exact site propagator from reset position \(j\) at age \(t\) is \(J_{m-j}(\gamma t)^2\). The mean inter-reset duration is \(\mu=\alpha\tau_0/(\alpha-1)\). Since the holding times are i.i.d., continuous, and independent of the state at the start of each holding interval, the finite-state Markov-renewal theorem and renewal-reward identity yield
\[
p_m=\sum_{j\in\{n_l,n_r\}}\pi_j\int_0^\infty h(t)J_{m-j}(\gamma t)^2\,dt,
\qquad h(t)=\frac{\Pr(\tau>t)}{\mu}.
\]
Explicitly, with \(c=(\alpha-1)\tau_0^{\alpha-1}/\alpha\),
\[
h(t)=\begin{cases}\mu^{-1},&0\le t<\tau_0,\\ct^{-\alpha},&t\ge\tau_0.\end{cases}
\]
Normalization follows by summing the nonnegative terms in \(m\) and using \(\sum_mJ_m(z)^2=1\) and \(\int h=1\). The same renewal theorem gives convergence of each fixed-site occupation probability from any finite initial site.

**2. Mellin integral and its error.** For every sufficiently large positive integer \(k\), the classical Weber--Schafheitlin Bessel-square integral gives
\[
\begin{aligned}
I_k&=\int_0^\infty t^{-\alpha}J_k(\gamma t)^2\,dt\\
&=\frac{\gamma^{\alpha-1}\Gamma(\alpha)}{2^\alpha\Gamma((\alpha+1)/2)^2}
\frac{\Gamma(k+(1-\alpha)/2)}{\Gamma(k+(1+\alpha)/2)},
\qquad 0<\alpha<2k+1.
\end{aligned}
\]
The difference between the actual age integral and \(cI_{|m-j|}\) is confined to \(0<t<\tau_0\). The Bessel series bound \(|J_k(z)|\le(|z|/2)^k e^{|z|^2/4}/k!\) for \(k\ge0\), \(0\le|z|\le\gamma\tau_0\), bounds this difference by a constant times \(C^{2k}/(k!)^2\) multiplied by an algebraic factor in \(k\), hence it is smaller than every inverse power of \(k\). This remains true when the weight \(t^{-\alpha}\) is included, because \(2k+1>\alpha\). Thus, for fixed \(j\),
\[
\int_0^\infty h(t)J_{m-j}(\gamma t)^2\,dt
=cI_{|m-j|}+O_L(|m|^{-L})\quad\text{for every }L>0.
\]
The standard gamma-ratio asymptotic, with shifts \(a=(1-\alpha)/2\) and \(d=(1+\alpha)/2\) satisfying \(a+d=1\), is
\[
\frac{\Gamma(k+a)}{\Gamma(k+d)}=k^{-\alpha}(1+O(k^{-2})).
\]
There is no \(k^{-1}\) correction because \((a-d)(a+d-1)/2=0\).

**3. Two tails and skew.** For \(m=n>0\) and fixed reset mark \(j\), \(|m-j|=n-j\) for all large \(n\), whereas for \(m=-n\), \(|m-j|=n+j\). Hence
\[
(n\mp j)^{-\alpha}=n^{-\alpha}\left(1\pm\frac{\alpha j}{n}+O(n^{-2})\right).
\]
Average over \(\pi\), use \(\sum_j\pi_j=1\), and identify \(b=\sum_j\pi_jj\). This proves both displayed tail expansions and the relative skew.

**4. Sharp moments and the critical logarithm.** The nonnegative stationary occupation has \(p_n+p_{-n}\sim2K_\alpha n^{-\alpha}\), so comparison with \(\sum_{n\ge1}n^{q-\alpha}\) gives the stated necessary-and-sufficient condition for every \(q>0\). At any reset mark \(j\), the exact free-walk identities \(\sum_m(m-j)J_{m-j}(\gamma t)^2=0\) and \(\sum_m(m-j)^2J_{m-j}(\gamma t)^2=\gamma^2t^2/2\) imply \(\sum_m m^2J_{m-j}(\gamma t)^2=j^2+\gamma^2t^2/2\). By Tonelli,
\[
\mathbb E_{\mathrm{st}}X^2=\sum_j\pi_jj^2+\frac{\gamma^2}{2}\int_0^\infty t^2h(t)\,dt.
\]
The age-square integral equals \(\mathbb E\tau^3/(3\mathbb E\tau)=\tau_0^2(\alpha-1)/(3(\alpha-3))\) when \(\alpha>3\) and diverges otherwise. When \(\alpha=3\), the tail constant reduces to \(K_3=\gamma^2\tau_0^2/6\); summing \(m^2p_m\) over \(|m|\le N\) gives \(2K_3\sum_{n\le N}n^{-1}+O(1)\), hence the asserted logarithm.

## Verification

The standalone script `verify_stationary_tails.py` reproduces 90 deterministic numerical assertions: the equilibrium-age normalization; independent finite-cutoff quadrature against the exact Bessel Mellin integral; both directional stationary-tail expansions for \(\alpha=1.4,2.3,3,4.5\); the predicted first skew coefficient and convergence; the finite-age second-moment integral at \(\alpha>3\); the exact \(\alpha=3\) truncated-age logarithm; and the free-walk ballistic second-moment identity. Run with Python, NumPy, and SciPy. The renewal limit, gamma-ratio asymptotics, and infinite-lattice moment divergence are analytic arguments, not claims inferred from these finite computations.

## Relationship to prior work

Acharya and Gupta (2023), arXiv:2308.14040, introduce the conditional two-site reset model, its exact bare Bessel propagator, and the Pareto waiting-time experiment (Sec. V). Their 41-site numerical experiment describes apparent mean-squared-displacement saturation at \(\alpha=3\); this is not an infinite-lattice tail statement. The present theorem concerns the genuinely infinite lattice, gives its missing sharp spatial Pareto tails and reset-bias correction, and establishes the infinite-lattice stationary-moment threshold \(\alpha>3\). No claim is made to rediscover their model or its general stationary occupation phenomenon.

The general renewal propagator of Singh, Górska, and Sandev (2022), arXiv:2203.04046, already establishes the renewal starting point in a fixed-reset diffusion setting. Inserting ballistic free-walk moments into that general method suggests a third-moment threshold; this elementary deduction is not independently claimed as a new theorem. The Weber--Schafheitlin Bessel-product integral itself is a classical identity (DLMF 10.22.57). The contribution assessed here is the *combined, conditional-reset* two-tail asymptotic including its universal leading coefficient and first directional coefficient, together with its exact stationary moment consequence.

## Limitations

This theorem assumes an infinite nearest-neighbor lattice, a finite reset set, complete localization at resets, and independent Pareto inter-reset times. A finite lattice always has bounded position moments, so it cannot test the infinite-volume moment threshold without increasing the lattice size and observation window. The proof concerns time-ensemble site-occupation probabilities, not coherent single-trajectory amplitudes or any measured finite experimental realization. The general renewal propagator and classical Mellin identity create a residual risk of implicit prior derivability; the analysis is limited to the stated model and assumptions.

## References

1. A. Acharya and S. Gupta, *Tight-binding model subject to conditional resets at random times*, arXiv:2308.14040 (first posted 2023-08-27), https://arxiv.org/html/2308.14040v2 . Relevant Sec. III-IV, V, equations for Bessel propagation and Pareto intervals.
2. R. K. Singh, K. Górska, and T. Sandev, *General approach to stochastic resetting*, arXiv:2203.04046 (2022), https://arxiv.org/abs/2203.04046 . General renewal equation and reset propagator.
3. NIST Digital Library of Mathematical Functions, §10.22, equation 10.22.57, https://dlmf.nist.gov/10.22.E57 . Classical Bessel-product Mellin integral.
