# Synchronization-induced current tails in a one-sided Brownian gas

## Finding

**Theorem (shared-clock current, sharp tails, and noncommuting limits).** In the one-sided Poisson Brownian gas defined below, changing independent Poisson resets into a *single simultaneous reset clock* leaves each one-particle distribution and the mean net integrated current unchanged at every time, but changes the annealed current from Poisson to a non-degenerate Poisson mixture. At every positive observation time this change is strict in convex order. Its stationary current has an exact Rayleigh mixing law and the following sharp right-tail asymptotic: for every fixed \(\lambda>0\), as integers \(q\to\infty\),

\[
\Pr(Q_{\mathrm G}(\infty)=q)
=\frac{1+o(1)}{\sqrt{2}}
\left(\lambda\sqrt{\frac{e}{2q}}\right)^q
\exp\left(-\lambda\sqrt{\frac q2}+\frac{\lambda^2}{8}\right).
\]

By contrast, the independently resetting current is Poisson at every time. The common-clock high-count limit has a *noncommuting time and count limit*: at each fixed positive finite time the leading negative-log probability is \(q\log q\), whereas in the stationary distribution it is \(\tfrac12q\log q\). A precise fixed-time formula and all moments appear below.

## Assumptions and scope

Fix \(D>0\), \(r>0\), \(\rho>0\). At time zero, the points \(-x_i\), with \(x_i>0\), form a homogeneous Poisson point process of intensity \(\rho\) on the negative half-line. Each particle follows independent one-dimensional Brownian motion with generator \(D\partial_{xx}\) between resetting events, returning to its *own initial point* at each reset. The Brownian noises and initial point process are independent of all reset events.

Two protocols are compared: the **independent-clock protocol** \(\mathrm I\), where every particle has its own rate-\(r\) Poisson clock, and the **shared-clock protocol** \(\mathrm G\), where a single rate-\(r\) Poisson clock resets all particles simultaneously. The observation is the *net* current \(Q_{\mathrm I}(t)\), respectively \(Q_{\mathrm G}(t)\): the number of particles strictly to the right of the origin at time \(t\). This is a net-crossing observable, not the infinite number of individual Brownian crossings. The point process is locally finite and both counts are almost surely finite at every fixed time.

Write

\[
 c=\rho\sqrt{D/\pi},\qquad
 \lambda=c/\sqrt r=\rho\sqrt{D/(\pi r)},\qquad
 m_t=\frac\rho2\sqrt{\frac Dr}\operatorname{erf}(\sqrt{rt}),\qquad
 m_\infty=\frac{\lambda\sqrt\pi}{2}.
\]

For every \(t>0\), the following assertions hold.

1. \(Q_{\mathrm I}(t)\sim\operatorname{Poisson}(m_t)\). The backward time \(A_t\) since the last event of the shared clock, with \(A_t=t\) if no event has yet occurred, has distribution

   \[
   \Pr(A_t=t)=e^{-rt},\qquad
   \Pr(A_t\in du)=r e^{-ru}\,du\quad(0<u<t).
   \]

   Conditional on \(A_t\), \(Q_{\mathrm G}(t)\sim\operatorname{Poisson}(c\sqrt{A_t})\), and \(\mathbb EQ_{\mathrm G}(t)=m_t\). For every nonaffine convex function \(\phi:\mathbb Z_{\ge0}\to\mathbb R\) for which both expectations are finite,

   \[
   \mathbb E\phi(Q_{\mathrm I}(t))<\mathbb E\phi(Q_{\mathrm G}(t)).
   \]

2. Put \(a_t=c\sqrt t\). At each *fixed* \(t>0\), as integers \(q\to\infty\),

   \[
   \Pr(Q_{\mathrm G}(t)=q)
   =e^{-rt}\frac{e^{-a_t}a_t^q}{q!}
   \left(1+\frac{2rt}{q}+O_{t,D,r,\rho}(q^{-2})\right).
   \]

   Thus the no-reset atom dominates arbitrarily large finite-time currents, even though its probability is exponentially small in time.

3. The stationary random current \(Q_{\mathrm G}(\infty)\), defined as the limit in law as \(t\to\infty\), is a Poisson mixture with \(Q_{\mathrm G}(\infty)\mid Y\sim\operatorname{Poisson}(\lambda Y)\), where \(Y>0\) has Rayleigh density \(2y e^{-y^2}\). For \(z\in[0,1]\), letting \(b=\lambda(z-1)\), its probability-generating function is

   \[
   \mathbb E z^{Q_{\mathrm G}(\infty)}
   =1+\frac{\sqrt\pi b}{2}e^{b^2/4}\operatorname{erfc}(-b/2).
   \]

   Its falling factorial moments are \(\mathbb E[(Q_{\mathrm G}(\infty))_{\underline{k}}]=\lambda^k\Gamma(1+k/2)\) for every integer \(k\ge0\), so

   \[
   \mathbb EQ_{\mathrm G}(\infty)=m_\infty,\qquad
   \operatorname{Var}(Q_{\mathrm G}(\infty))
   =m_\infty+\lambda^2(1-\pi/4).
   \]

   The independent-clock stationary law is \(\operatorname{Poisson}(m_\infty)\), with variance \(m_\infty\). Moreover \(d_{\rm TV}(\mathcal L(Q_{\mathrm G}(t)),\mathcal L(Q_{\mathrm G}(\infty)))\le e^{-rt}\).

4. For fixed positive \(D,r,\rho\), the stationary probability mass satisfies the sharp asymptotic in the opening statement. In particular,

   \[
   \lim_{q\to\infty}\frac{-\log\Pr(Q_{\mathrm G}(t)=q)}{q\log q}=1\quad(0<t<\infty),\qquad
   \lim_{q\to\infty}\frac{-\log\Pr(Q_{\mathrm G}(\infty)=q)}{q\log q}=\frac12.
   \]

   For the independent-clock protocol the latter limit is \(1\) even at stationarity.

5. At fixed positive \(D,r\), taking \(\rho\to\infty\) with each protocol's initial intensity equal to \(\rho\),

   \[
   \frac{Q_{\mathrm G}(\infty)}\rho\ \Longrightarrow\sqrt{\frac{D}{\pi r}}\,Y,\qquad
   \frac{Q_{\mathrm I}(\infty)}\rho\ \longrightarrow\frac12\sqrt{\frac Dr}
   \quad\text{in probability}.
   \]

   Thus common resetting leaves a nondegenerate density-scale current fluctuation, unlike independent resets.

## Proof

**1. Integrability, thinning, and the shared age.** For Brownian motion of diffusivity \(D\) started at \(-x\), the probability to be positive after a reset-free interval of duration \(u>0\) is \(p_u(x)=\tfrac12\operatorname{erfc}(x/\sqrt{4Du})\). Direct integration gives

\[
 \int_0^\infty p_u(x)\,dx=\sqrt{Du/\pi}.
\]

The Poisson thinning theorem shows that, conditional on a common reset age \(u\), the positive particles form a finite Poisson point process with total intensity \(c\sqrt u\). The backward-age law follows directly by the probability of no rate-\(r\) events during the last \(u\) time units, with an atom for no event on the whole interval. For independent clocks, thinning the initial Poisson process by each particle's independently sampled end-position mark instead yields an unconditional Poisson law with parameter \(\mathbb E(c\sqrt{A_t})\). Integration by parts gives

\[
 \mathbb E\sqrt{A_t}
 =e^{-rt}\sqrt t+\int_0^t re^{-ru}\sqrt u\,du
 =\frac{\sqrt\pi}{2\sqrt r}\operatorname{erf}(\sqrt{rt}),
\]

proving the common parameter \(m_t\). Existence of both finite counts follows from this finite expected parameter. The identical one-particle marginals follow because each particle's marginal reset clock is rate-\(r\) Poisson under either protocol.

**2. Strict convex ordering.** For any integrable convex \(\phi\) on nonnegative integers, \(h(u)=\mathbb E[\phi(\operatorname{Poisson}(u))]\) is convex: differentiation of the Poisson series yields \(h''(u)=\mathbb E[\phi(N_u+2)-2\phi(N_u+1)+\phi(N_u)]\ge0\), with \(N_u\sim\operatorname{Poisson}(u)\). If \(\phi\) is nonaffine, one second difference is strictly positive; since Poisson probabilities are positive at every integer for \(u>0\), \(h\) is strictly convex there. Jensen's inequality is strict for the nondegenerate parameter \(c\sqrt{A_t}\) for every \(t>0\), while its mean is \(m_t\). Truncation supplies the usual justification for convex functions with finite mixture expectations. This establishes the claim, including \(\operatorname{Var}(Q_{\mathrm G}(t))=m_t+\operatorname{Var}(c\sqrt{A_t})>m_t\).

**3. Fixed-time endpoint asymptotics.** The no-reset event has weight \(e^{-rt}\) and gives a \(\operatorname{Poisson}(a_t)\) component. For each integer \(q\ge0\), divide the continuous-age contribution to \(\Pr(Q_{\mathrm G}(t)=q)\) by this atomic contribution, and substitute \(v=\sqrt{u/t}\). The ratio is exactly

\[
 R_q(t)=2rt\int_0^1 v^{q+1}
 \exp\left(rt(1-v^2)+a_t(1-v)\right)dv.
\]

The exponential multiplier is smooth on \([0,1]\) and equals one at the right endpoint, so endpoint integration (or one integration by parts with bounded remainder) gives \(R_q(t)=2rt/q+O(q^{-2})\). This proves the entire relative asymptotic, not merely its logarithmic exponent.

**4. Stationary mixture and generating function.** The shared age converges in law to \(E\sim\operatorname{Exp}(r)\), and the two age laws can be coupled to agree except on the no-reset event, of probability \(e^{-rt}\), yielding the stated total-variation bound after conditional thinning. If \(Y=\sqrt{rE}\), then \(\Pr(Y>y)=e^{-y^2}\) and \(Y\) has density \(2ye^{-y^2}\). The conditional Poisson law gives \(\mathbb Ez^{Q}=\mathbb E e^{\lambda(z-1)Y}\); completing the square and integrating \(2ye^{-y^2+by}\) gives the displayed generating function. Conditional factorial moments yield \(\lambda^k\mathbb EY^k=\lambda^k\Gamma(1+k/2)\). The first two produce the displayed mean and variance; the independent-protocol stationary law is Poisson with the same mean.

**5. Sharp stationary current tail.** The exact stationary mass function, with \(q\ge0\), is

\[
 p_q=\frac{2\lambda^q}{q!}\int_0^\infty y^{q+1}e^{-y^2-\lambda y}\,dy
 =\frac{\lambda^q\Gamma(q/2+1)}{\Gamma(q+1)}
  \mathbb E\left[e^{-\lambda\sqrt{U_q}}\right],
 \quad U_q\sim\operatorname{Gamma}(q/2+1,1).
\]

For integer \(q\), \(U_q\) has the distribution of half the squared Euclidean norm of a standard Gaussian vector in dimension \(q+2\). The central limit theorem and delta method imply \(\sqrt{U_q}-\sqrt{q/2}\Longrightarrow N(0,1/4)\). The norm divided by \(\sqrt2\) is a \(1/\sqrt2\)-Lipschitz function of this Gaussian vector, so Gaussian concentration gives uniformly bounded exponential moments of every fixed order after centering. Also \(\mathbb E\sqrt{U_q}-\sqrt{q/2}\to0\). Therefore uniform integrability yields the *stronger-than-weak-convergence* asymptotic

\[
 \mathbb E[e^{-\lambda\sqrt{U_q}}]
 =e^{-\lambda\sqrt{q/2}}(e^{\lambda^2/8}+o(1)).
\]

Stirling's formula yields \(\Gamma(q/2+1)/\Gamma(q+1)=2^{-1/2}(e/(2q))^{q/2}(1+o(1))\). Their product proves the sharp stationary formula, including its \(\lambda^2/8\) correction and \(1/\sqrt2\) prefactor. Comparing the finite-time mass with Stirling's formula gives logarithmic exponent one, whereas this formula gives exponent one-half. The independent stationary Poisson mass has exponent one.

**6. High-density limit.** At fixed \(D,r\), conditioned on \(Y\), the shared-clock stationary count has mean \(\rho\sqrt{D/(\pi r)}Y\) and variance equal to its mean. Hence the conditional variance of the count divided by \(\rho\) is \(O(\rho^{-1})\) after averaging over \(Y\), giving convergence to its random limiting intensity. The independently resetting count is Poisson with mean \(\rho\sqrt{D/r}/2\), and Chebyshev's inequality gives convergence in probability to its deterministic normalized mean.

## Verification

The included standalone script `check_current.py` checks the Brownian spatial integral, the closed-form probability-generating function, the first five factorial moments, variance and third factorial cumulant identities, equality of finite-time means, endpoint-tail integral ratios, and the sharp stationary asymptotic against independently integrated saddlepoint expressions. Execute with `python check_current.py` using Python 3 and SciPy. The numerical diagnostics do not substitute for the probability and asymptotic arguments above.

## Relationship to prior work

Di Bello, Hartmann, Majumdar, Mori, Rosso and Schehr (2023), arXiv:2302.06696, analyze independent per-particle resetting under precisely the one-sided step preparation and prove the annealed Poisson current and its stationary mean. Their equations for the independent-clock model are credited here. Biroli, Larralde, Majumdar and Schehr (2022), arXiv:2211.00563, establish the shared-reset-age mixture principle for a *different* finite-particle gas whose particles all start and reset at the origin; they also discuss counting statistics in that geometry. The present claim joins these distinct setups by using a shared clock in the one-sided Poisson step gas and proves the complete finite-time strict convex order, endpoint law, Rayleigh-mixture tail with exact prefactor, density-scale non-self-averaging and noncommutation of high-count and long-time limits.

Valiquette and coauthors (2023), arXiv:2305.17095, study general classes of mixed-Poisson tail behavior. Their broad classifications are compatible with the present result but do not give this model's exact intensity identification, fixed-time endpoint atom, or \(q\)-resolved asymptotic constant. The later de Mauro, Majumdar and Schehr study (2026), arXiv:2606.31634, analyzes simultaneous resets under confinement with particles reset to a common origin; it does not study the one-sided step current.

## Limitations

The theorem is for the **annealed** initial Poisson ensemble. It makes no claim about the quenched fixed-initial-configuration law. Resets are instantaneous, Poisson in physical time, and always return each particle to its own initial point. Brownian motions are mutually independent conditional on the shared clock. The sharp high-current asymptotic holds at fixed positive \(\lambda\) as \(q\to\infty\); it is not a uniform two-parameter asymptotic in time or density. These results are self-contained mathematical deductions, not an independent external certification. Some older general mixed-Poisson literature may contain equivalent tail asymptotics under other names; that publication-priority risk remains.

## References

- C. Di Bello, A. K. Hartmann, S. N. Majumdar, F. Mori, A. Rosso, G. Schehr, *Current fluctuations in stochastically resetting particle systems*, first posted 2023-02-13, https://arxiv.org/abs/2302.06696.
- M. Biroli, H. Larralde, S. N. Majumdar, G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, first posted 2022-11-01, https://arxiv.org/abs/2211.00563.
- S. Valiquette, G. Toulemonde, J. Peyhardi, É. Marchand, F. Mortier, *Asymptotic tail properties of Poisson mixture distributions*, first posted 2023-05-26, https://arxiv.org/abs/2305.17095.
- G. de Mauro, S. N. Majumdar, G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, first posted 2026-06-30, https://arxiv.org/abs/2606.31634 (context only).
