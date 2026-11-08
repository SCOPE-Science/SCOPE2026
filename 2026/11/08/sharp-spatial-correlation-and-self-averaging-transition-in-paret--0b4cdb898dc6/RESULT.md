# Sharp spatial-correlation and self-averaging transition in Pareto-reset Glauber chains

## Finding

Consider the infinite one-dimensional, zero-field nearest-neighbor kinetic Ising chain, initialized with independent symmetric spins and **globally** returned to that same initial spin configuration at independent Pareto-renewal times. For every reset exponent \(\alpha>1\) and cutoff \(\tau_0>0\), the stationary **annealed**, connected, equal-time spin correlation \(C_n=\mathbb E[\sigma_0\sigma_n]\), \(n\ge1\), has the following sharp distance laws.

At any fixed positive temperature, write \(\gamma=\tanh(2\beta J)\in(0,1)\), \(\eta=\tanh(\beta J)\in(0,1)\), and \(q=\alpha-1\). Then

\[
 C_n\sim K_+(\alpha,\tau_0,\gamma)\,n^{-q}\eta^n,\qquad
 K_+=\frac{\tau_0^q}{\alpha}\bigl(2\sqrt{1-\gamma^2}\bigr)^q.
\]

At strictly zero temperature (\(\gamma=1\)), the same resetting protocol instead gives an algebraic law

\[
 C_n\sim K_0(\alpha,\tau_0)n^{-2q},\qquad
 K_0=\frac{(4\tau_0)^q\Gamma(q+\tfrac12)}{\alpha\sqrt\pi}.
\]

Consequently, at zero temperature the integrated spatial connected correlation \(\chi_{\mathrm{sp}}=1+2\sum_{n\ge1}C_n\) is finite **if and only if** \(\alpha>3/2\). Let \(M_L=L^{-1}\sum_{i=1}^{L}\sigma_i\) be the stationary magnetization of an \(L\)-site observation window, not a separately periodic \(L\)-site Markov chain. Its exact leading annealed variance is

\[
 \operatorname{Var}(M_L)\sim
 \begin{cases}
 \displaystyle\frac{2K_0}{(3-2\alpha)(4-2\alpha)}L^{-2(\alpha-1)},&1<\alpha<3/2,\\[4pt]
 \displaystyle 2K_0\frac{\log L}{L},&\alpha=3/2,\\[4pt]
 \displaystyle\frac{\chi_{\mathrm{sp}}}{L},&\alpha>3/2.
 \end{cases}
\]

Thus the finite-mean reset regime has a separate and sharp spatial self-averaging threshold at \(\alpha=3/2\). Any fixed positive temperature restores exponential clustering and ordinary \(L^{-1}\) block-variance decay.

## Assumptions and scope

Spins \(\sigma_i\in\{-1,+1\}\), indexed by \(i\in\mathbb Z\), interact with coupling \(J>0\) and no field. Between resets they follow Glauber single-spin flips with rate

\[
 w_i(\sigma)=\frac12\left(1-\frac\gamma2\sigma_i(\sigma_{i-1}+\sigma_{i+1})\right),
 \quad \gamma=\tanh(2\beta J),
\]

where \(\beta\in(0,\infty]\), with \(\gamma=1\) when \(\beta=\infty\). An initial configuration \(\sigma^{(0)}\) is sampled once from independent fair spins, and **the entire infinite configuration** is returned simultaneously to that same \(\sigma^{(0)}\) at each reset. Between resets, fresh independent Glauber randomness is used. Reset interarrivals are iid and independent of the spins, with density

\[
 \rho(t)=\alpha\tau_0^\alpha t^{-\alpha-1}\mathbf1_{\{t\ge\tau_0\}},\qquad \alpha>1.
\]

The observation is in the stationary equilibrium-renewal version of the resetting clock. Expectations average over the initial spin configuration, stationary reset clock and Glauber evolution (**annealed**). The one-spin mean vanishes by global spin-flip symmetry, so \(C_n\) is connected. Limits \(n\to\infty\) and \(L\to\infty\) are taken at fixed \(\alpha,\tau_0,\beta J\); no joint low-temperature scaling or finite-ring thermodynamic-limit interchange is asserted.

## Proof

**1. Exact spin-pair evolution and a killed hitting-time representation.** By applying the spin-flip generator to \(\sigma_0\sigma_n\), translation invariance gives, for the no-reset dynamics,

\[
 \dot c_n(t)=-2c_n(t)+\gamma(c_{n-1}(t)+c_{n+1}(t)),\quad n\ge1;
 \qquad c_0(t)=1,\quad c_n(0)=0\ (n\ge1).
\]

Let \(T_n^{(\gamma)}\) denote the first hitting time of zero by a continuous-time simple symmetric nearest-neighbor walk starting at \(n\), jumping to **each** neighbor at rate \(\gamma>0\). With \(\delta=2(1-\gamma)\), the bounded solution of this initial-boundary-value problem is

\[
 c_n(t)=\mathbb E_n\big[e^{-\delta T_n^{(\gamma)}}\mathbf1_{\{T_n^{(\gamma)}\le t\}}\big]. \tag{1}
\]

Indeed, the backward equation for the killed hitting probability is \(\partial_tc_n=\gamma\Delta c_n-\delta c_n\), precisely the displayed Glauber equation, and the boundary and initial values coincide. Recurrence gives finiteness of the walk hitting time almost surely. Solving the second-order recurrence for the Laplace transform, with the bounded root at infinity, yields for \(s\ge0\)

\[
 \mathbb E_n e^{-sT_n^{(\gamma)}}=e^{-n\kappa_\gamma(s)},\qquad
 \kappa_\gamma(s)=\operatorname{arcosh}\!\left(1+\frac{s}{2\gamma}\right). \tag{2}
\]

The first hitting time from \(n\) decomposes by the strong Markov property into a sum of \(n\) iid one-step-down hitting times. This provides an independent probabilistic derivation of the power \(n\) in (2).

**2. Exact stationary renewal-age mixing.** The mean interarrival equals \(\mu=\alpha\tau_0/(\alpha-1)\). The stationary backward age \(A\) has density \(\Pr(W>a)/\mu\), where \(W\) is a reset interarrival. Its tail is exactly

\[
 H(a)=\Pr(A\ge a)=
 \begin{cases}
 1-a/\mu,&0\le a\le\tau_0,\\
 \displaystyle\frac{\tau_0^q}{\alpha}a^{-q},&a\ge\tau_0,
 \end{cases}\qquad q=\alpha-1>0. \tag{3}
\]

Conditioning the stationary system on its age and using (1), Tonelli's theorem (all integrands are nonnegative) gives the **exact** identity

\[
 C_n=\mathbb E_n\big[e^{-\delta T_n^{(\gamma)}}H(T_n^{(\gamma)})\big]. \tag{4}
\]

In particular (4), not only the subsequent limits, is valid at every integer separation and all permitted parameters. For the no-reset hitting time, the density is \(n e^{-2\gamma t}I_n(2\gamma t)/t\), giving a directly reproducible Bessel-integral representation of (4).

**3. Fixed positive temperature.** Suppose \(0<\gamma<1\), and let \(\delta=2(1-\gamma)>0\). By (2),

\[
 \mathbb E e^{-\delta T_n^{(\gamma)}}=\eta^n,
 \quad \eta=e^{-\kappa_\gamma(\delta)}=\frac{1-\sqrt{1-\gamma^2}}{\gamma}=\tanh(\beta J).
\]

Exponential tilting by \(e^{-\delta T_n^{(\gamma)}}/\eta^n\) defines a probability law under which the \(n\) one-step hitting times remain iid. Each has finite mean

\[
 m_\gamma=\kappa_\gamma'(\delta)
 =\frac1{\sqrt{\delta(\delta+4\gamma)}}
 =\frac1{2\sqrt{1-\gamma^2}}>0.
\]

Thus \(T_n^{(\gamma)}/n\to m_\gamma\) in tilted probability. The left-tail event \(T_n^{(\gamma)}<nm_\gamma/2\) has exponentially small tilted probability by a Chernoff bound, since each tilted summand is positive and has a Laplace transform near zero. On its complement, formula (3) implies that \(n^q H(T_n^{(\gamma)})\) is bounded by \(\tau_0^q2^q/(\alpha m_\gamma^q)\) for sufficiently large \(n\). Its limit in probability is \(\tau_0^q/(\alpha m_\gamma^q)\); the exceptional contribution is at most \(n^q e^{-cn}\), because \(H\le1\). Bounded convergence in probability therefore proves

\[
 \frac{C_n}{\eta^nn^{-q}}\longrightarrow
 \frac{\tau_0^q}{\alpha}m_\gamma^{-q}=K_+.
\]

This also shows \(0<C_n\le\eta^n\), so spatial correlations are summable at every fixed positive temperature.

**4. Zero temperature and exact power-law constant.** If \(\gamma=1\), then \(\delta=0\). Set \(T_n=T_n^{(1)}\). For each fixed \(r>0\) and all integers \(n>r\), Mellin--Laplace inversion and (2) give

\[
 \mathbb E[T_n^{-r}]
 =\frac1{\Gamma(r)}\int_0^\infty s^{r-1}
  e^{-n\operatorname{arcosh}(1+s/2)}\,ds.
\]

Substitute \(v=n\operatorname{arcosh}(1+s/2)\), so \(s=2(\cosh(v/n)-1)\). Dominated convergence applies after multiplying by \(n^{2r}\): on compact \(v\)-intervals the integrand tends to \(2v^{2r-1}e^{-v}/\Gamma(r)\); for sufficiently large \(n\), \(\sinh(x)\ge x\), \(\sinh(x)\le xe^x\), and \(\cosh(x)\le e^x\) give an integrable bound consisting of a constant times \(v^{2r-1}e^{-v/2}\). Therefore

\[
 \lim_{n\to\infty}n^{2r}\mathbb E[T_n^{-r}]
 =\frac{2\Gamma(2r)}{\Gamma(r)}
 =\frac{4^r\Gamma(r+1/2)}{\sqrt\pi}. \tag{5}
\]

The event \(T_n<\tau_0\) requires at least \(n\) jumps by time \(\tau_0\); it is bounded by \(\Pr(\operatorname{Poisson}(2\tau_0)\ge n)\), superexponentially small in \(n\). Cauchy--Schwarz together with (5) for \(r=2q\) shows that even \(\mathbb E[T_n^{-q};T_n<\tau_0]=o(n^{-2q})\). Thus replacing \(H(T_n)\) in (4) by \(\tau_0^q T_n^{-q}/\alpha\) changes the result by \(o(n^{-2q})\). Setting \(r=q\) in (5) yields precisely \(C_n\sim K_0n^{-2q}\).

An exact finite-distance check of the critical inverse-moment argument is \(\mathbb E[T_n^{-1}]=2/(n^2-1)\) for \(n\ge2\), obtained by integrating (2) at \(r=1\). It agrees with the \(r=1\) constant in (5).

**5. The block-variance transition.** Spin-flip symmetry gives \(\mathbb E\sigma_i=0\). Hence for every \(L\ge1\), exactly

\[
 \operatorname{Var}(M_L)=\frac1{L^2}
 \left[L+2\sum_{n=1}^{L-1}(L-n)C_n\right]. \tag{6}
\]

Write \(p=2q\). When \(0<p<1\), the Riemann-sum asymptotic
\(\sum_{n<L}(L-n)n^{-p}\sim L^{2-p}/[(1-p)(2-p)]\) gives the first variance case. For \(p=1\), the same sum is \(L\log L+O(L)\), giving the middle case. For \(p>1\), dominated convergence in (6) yields \(L\operatorname{Var}(M_L)\to1+2\sum_{n\ge1}C_n\). Since \(K_0>0\), the convergence or divergence of \(\chi_{\mathrm{sp}}\) is exactly determined by \(p>1\), equivalent to \(\alpha>3/2\). At finite positive temperature, \(C_n\le\eta^n\), and the same summable case always applies.

## Verification

Run `python check.py` with the dependency in `requirements.txt`. The checker uses the independently evaluable first-passage Bessel density, the equilibrium-age formula, a closed exact inverse-moment identity, and several parameter/separation regimes. On the packaged version it passed 324 deterministic assertions. This is a finite numerical and algebraic corroboration; equations (1)--(6), the exponential-tilt argument, and the dominated-convergence argument furnish the proofs of the infinite-distance and thermodynamic-window statements.

## Relationship to prior work

The February 17, 2026 first-public preprint by Anagha V K and Apoorva Nagar, *Ising Model with Power Law Resetting* (arXiv:2602.15495), establishes the Pareto-renewal setting and analyzes the distribution of **magnetization** under global resets. It does not provide stationary equal-time two-spin distance asymptotics or the \(\alpha=3/2\) spatial self-averaging threshold. Its later journal date is not the first-public date used here.

Magoni, Majumdar and Schehr, *Ising model with stochastic resetting* (arXiv:2002.04867), provide the global-reset Glauber-renewal framework for **Poisson** clock intervals; their conclusion explicitly raises the structure of two-point correlations as a further question. Glauber's 1963 kinetic-Ising correlation closure is foundational and is not new here. Grange, *Voter model under stochastic resetting* (arXiv:2207.08590), studies two-point functions under **independent sitewise Poisson** resetting to initial opinions, rather than the common Pareto clock used here. The hitting-time solution of the Glauber equations and standard renewal-age formula are also antecedent tools. The contribution claimed here is their combined, sharp, spatially resolved Pareto law with both temperature-dependent prefactors and the resulting exact nonstandard block-variance regimes.

## Limitations

All assertions are annealed over the initially sampled reset configuration and are for the infinite chain observed through finite blocks. They do not assert a fixed-environment quenched correlation law, a thermodynamic susceptibility defined by an equilibrium fluctuation--dissipation identity, a dynamic time-correlation theorem, finite-ring scaling at coupled limits, or a joint \(\beta\to\infty\), \(n\to\infty\) crossover. The case \(\alpha\le1\), for which the renewal mean is infinite and no stationary equilibrium-age clock exists, is excluded. Exact mathematical correctness does not independently establish publication priority: an unindexed general renewal-coarsening theorem might subsume the result.

## References

1. Anagha V K and Apoorva Nagar, *Ising Model with Power Law Resetting*, first-public arXiv:2602.15495v1 (2026-02-17), https://arxiv.org/html/2602.15495v1 .
2. M. Magoni, S. N. Majumdar and G. Schehr, *Ising model with stochastic resetting*, arXiv:2002.04867 (2020), https://arxiv.org/abs/2002.04867 .
3. P. Grange, *Voter model under stochastic resetting*, arXiv:2207.08590 (2022), https://arxiv.org/pdf/2207.08590 .
4. R. J. Glauber, *Time-Dependent Statistics of the Ising Model*, Journal of Mathematical Physics 4, 294--307 (1963), https://doi.org/10.1063/1.1703954 .
