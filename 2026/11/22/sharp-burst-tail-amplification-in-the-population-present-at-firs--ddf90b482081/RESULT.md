# Sharp burst-tail amplification in the population present at first target binding

## Finding

Consider independent mortal searchers released in Poisson production batches, starting with no searchers. The *pre-binding population* counts all particles still alive immediately before the first particle reaches the target, including that first successful particle. If a production batch has size \(J\geq1\) with \(0<\mu=\mathbb E[J]<\infty\), then, conditional on an arbitrarily early first binding, the number of living particles converges in distribution to the \(J\)-size-biased batch law:
\[
\lim_{t\downarrow0}\Pr(N_{T-}=j\mid T=t)=\frac{j\Pr(J=j)}{\mu},\qquad j\ge1.
\]
In particular, the early conditional mean converges to \(\mathbb E[J^2]/\mu\) when the second moment is finite, and diverges when it is infinite, even though the unconditioned population has finite mean at each finite time.

For a Brownian searcher of diffusivity \(D>0\), born a distance \(L>0\) from an absorbing target, suppose \(\Pr(J=j)\sim c j^{-1-\alpha}\) for some \(c>0\) and \(\alpha>1\). As \(t\downarrow0\), the conditional expected population obeys the **sharp three-regime classification**
\[
\mathbb E[N_{T-}\mid T=t]\sim
\begin{cases}
\displaystyle\frac{c\Gamma(2-\alpha)}{(\alpha-1)\mu}
\left(\frac{2\sqrt{Dt}}{\sqrt\pi L}e^{-L^2/(4Dt)}\right)^{\alpha-2}, &1<\alpha<2,\\[8pt]
\displaystyle\frac{cL^2}{4D\mu\,t},&\alpha=2,\\[8pt]
\displaystyle\frac{\mathbb E[J^2]}{\mu},&\alpha>2.
\end{cases}
\]
Thus an unbounded *exponential-in-inverse-time* conditional population for \(1<\alpha<2\) changes to an inverse-time law at the critical tail exponent \(2\), and to a finite limit above it. The leading laws do not depend on the Poisson production rate or the positive finite mortality rate.

## Assumptions and scope

Production times form a homogeneous Poisson process of rate \(b>0\) starting at time zero, without an initial batch. Each event produces an independent positive-integer batch \(J\), identically distributed with probability generating function \(\psi(z)=\mathbb E[z^J]\) and finite mean \(\mu\). Particles from all batches move independently. Each particle has an independent exponential death time of rate \(d>0\), independent of its motion, and a hypothetical target-hitting time \(H\) in the absence of death. The population process stops when the first live particle hits an absorbing target, at time \(T\). The random variable \(N_{T-}\) is the count just *before* that binding, including the binding particle. There are no interactions, crowding, birth-location fluctuations, or multi-particle reactions. For the general joint-law lemma below, \(H>0\) almost surely has a continuous density \(f_H\), and its cumulative hitting probability is positive for all sufficiently small positive times. One-dimensional Brownian motion on the positive half-line, born at \(L>0\), meets these assumptions with generator \(D\partial_x^2\).

For any age \(u\ge0\), define
\[
\begin{aligned}
F(u)&=\Pr(H\le u,H<\mathrm{death})=\int_0^u e^{-dv}f_H(v)\,dv,\\
q(u)&=1-F(u),\qquad \rho(u)=e^{-du}f_H(u)=-q'(u),\\
\ell(u)&=e^{-du}\Pr(H>u),\qquad w(u)=q(u)-\ell(u).
\end{aligned}
\]
Here \(q\) is single-particle no-binding probability, \(\ell\) the probability of being alive without binding, and \(w\) the probability of having died without binding. For any \(t>0\) with \(F(t)>0\), conditioning on \(T=t\) means the regular conditional distribution obtained from the joint time-density.

## Proof

**1. A joint probability-generating function.** For \(0\le z\le1\), every batch born at age \(u\) contributes the no-binding/surviving-particle generating weight \(\psi(w(u)+z\ell(u))\). Poisson marking gives
\[
G_t(z):=\mathbb E[z^{N_t};T>t]
=\exp\left\{b\int_0^t[\psi(w(u)+z\ell(u))-1]\,du\right\}.
\]
Here \(N_t\) is defined by the unrestarted construction on the event of no binding. For a specified batch to contain the *first* hitting particle at age \(u\), exactly one particle hits at that instant (ties have probability zero), with density \(\rho(u)\), and its other \(J-1\) particles must not have hit previously. A direct marked-Poisson/Palm decomposition therefore gives the joint time-density generating function
\[
\lim_{\Delta\downarrow0}\frac{\mathbb E[z^{N_{T-}}\mathbf1_{\{t<T\le t+\Delta\}}]}{\Delta}
=bz\,G_t(z)\int_0^t\rho(u)\psi'(w(u)+z\ell(u))\,du.
\]
At \(z=1\), \(G_t(1)=\exp\{-b\int_0^t[1-\psi(q(u))]\,du\}\), and the integral equals \(1-\psi(q(t))\) by \(\rho=-q'\). Thus the first-binding density is \(bG_t(1)[1-\psi(q(t))]\), matching the established no-reaction law. Dividing the joint generating function by that density and by \(z\) yields the exact conditional generating function of the other \(N_{T-}-1\) living particles:
\[
K_t(z)=\frac{G_t(z)}{G_t(1)}\,
\frac{\int_0^t\rho(u)\psi'(w(u)+z\ell(u))\,du}{1-\psi(q(t))}.
\tag{1}
\]
This is an exact finite-time joint observable, not obtained from the marginal no-reaction probability alone.

**2. An exact conditional mean and its integrability.** Differentiating (1) at \(z=1\) gives
\[
\mathbb E[N_{T-}\mid T=t]
=1+b\int_0^t\ell(u)\psi'(q(u))\,du
+\frac{\int_0^t\rho(u)\ell(u)\psi''(q(u))\,du}{1-\psi(q(t))}.
\tag{2}
\]
The formula remains valid when \(\mathbb E[J^2]=\infty\): the potentially singular numerator is finite for every fixed \(t>0\) because \(0\le\ell(u)\le1\) and
\[
\int_0^t\rho(u)\psi''(q(u))\,du
=\psi'(1)-\psi'(q(t))\le\mu<\infty.
\tag{3}
\]
Thus an infinite second batch-size moment does *not* make the conditional mean infinite at any fixed positive binding time.

**3. The sharp early-binding amplification.** Since \(\ell(u)\to1\), \(w(u)\to0\), \(q(u)\to1\) uniformly on \([0,t]\) as \(t\downarrow0\), continuity of \(\psi'\) on \([0,1]\) and (1) imply \(K_t(z)\to\psi'(z)/\mu\) for \(0\le z\le1\). This proves the size-biased distributional limit. In (2), the first integral is at most \(b\mu t\). Equation (3) and the uniform convergence of \(\ell\) to one show that the second numerator is asymptotic to \(\mu-\psi'(1-F(t))\) whenever it is nonzero. Meanwhile
\[
1-\psi(1-F(t))\sim\mu F(t).
\tag{4}
\]
If \(\mathbb E[J^2]<\infty\), Taylor expansion (or monotone convergence for the derivative quotient) gives \(\lim_{t\downarrow0}\mathbb E[N_{T-}\mid T=t]=\mathbb E[J^2]/\mu\). If the second moment is infinite, monotone convergence applied to \(\{\mu-\psi'(1-F)\}/F\) proves that the conditional mean diverges.

For the power tail \(\Pr(J=j)\sim c j^{-1-\alpha}\), the numerator satisfies
\[
\mu-\psi'(1-F)
=\sum_{j\ge1}j\Pr(J=j)\{1-(1-F)^{j-1}\}.
\]
If \(1<\alpha<2\), a Riemann-sum comparison after scaling \(x=Fj\) gives
\[
\mu-\psi'(1-F)\sim cF^{\alpha-1}
\int_0^\infty x^{-\alpha}(1-e^{-x})\,dx
=\frac{c\Gamma(2-\alpha)}{\alpha-1}F^{\alpha-1}.
\tag{5}
\]
The integral is finite at both ends in exactly this exponent range. At \(\alpha=2\), split the sum at \(j\asymp F^{-1}\): the lower range contributes \(cF\log(1/F)\), the upper range is \(O(F)\). Above \(2\), the second moment is finite. Combining these three facts with (2)–(4) establishes the general three regimes as functions of \(F(t)\).

**4. Brownian conversion.** For Brownian hitting from distance \(L\),
\[
\Pr(H\le t)=\operatorname{erfc}\!\left(\frac{L}{\sqrt{4Dt}}\right)
\sim\frac{2\sqrt{Dt}}{\sqrt\pi L}\exp\!\left(-\frac{L^2}{4Dt}\right).
\]
Because \(e^{-dt}\Pr(H\le t)\le F(t)\le\Pr(H\le t)\), the two are asymptotically equivalent. Substitution in (5) yields the first regime; for \(\alpha=2\), \(\log(1/F(t))\sim L^2/(4Dt)\). All displayed constants follow, including independence of \(b\) and \(d\) at leading order.

## Verification

`CHECK.py` uses an independent finite-state killed birth–death master equation for exponential individual hitting clocks, comparing its joint time-density generating function with (1) for three different batch laws at multiple finite times and generating variables. It also checks the early size-biased limit and finite-second-moment conditional mean numerically. The checker performs 54 successful comparisons when run as `python3 CHECK.py`. A second standalone `python3 TAIL_CHECK.py` makes six finite power-tail comparisons near \(\alpha=3/2\), \(\alpha=2\), and \(\alpha=3\), with direct series sums and explicit small tail approximations. These finite checks do not establish the asymptotic statements: the proof is the Poisson decomposition, estimate (3), Riemann sums, and Brownian first-passage asymptotics above.

## Relationship to prior work

Boyer and Mercado-Vásquez (arXiv:2611.04843, first submitted 3 November 2026) derive the particle-density law, marginal no-reaction probability, bursty synthesis comparison, and mean first-passage times for precisely this production–degradation model. Those results, including the survival law corresponding to \(G_t(1)\), are prior work. The present claim instead conditions the *live population at the first binding*, derives the full joint time/count generating function, and classifies its extreme-early mean in the heavy-burst regime. Mercado-Vásquez and Boyer (arXiv:2602.11095) treat the earlier unit-production first-passage problem. General Poisson marking and size bias are standard mathematical tools, not claimed as inventions here; the assessed content is their specific first-binding joint law and three-regime quantitative amplification. Relevant bursty birth–death threshold literature concerns molecule-count thresholds rather than arrival of an independently diffusing particle at a spatial target.

## Limitations

The power-law constants require pointwise asymptotic batch probabilities \(\Pr(J=j)\sim cj^{-1-\alpha}\), not merely an unspecified heavy tail. The conditional limit \(T=t\) is a regular density-based conditioning, not conditioning on a positive-probability event. The early-time binding event is exceedingly rare for a Brownian source at positive distance; none of the results establishes finite-sample feasibility, robustness to copy-count noise, interactions, delayed birth registration, nonexponential deaths, or arbitrary renewal production clocks. For arbitrary finite-mean batch laws with infinite second moment, divergence is proved without a universal rate. The early conditional count remains finite at each fixed positive time.

## References

- D. Boyer and G. Mercado-Vásquez, *Stochastic synthesis and degradation of arbitrary diffusive processes*, arXiv:2611.04843v1 (3 November 2026), https://arxiv.org/abs/2611.04843.
- G. Mercado-Vásquez and D. Boyer, *Stochastic synthesis-degradation processes: first-passage properties and connections with resetting*, arXiv:2602.11095v1 (11 February 2026), https://arxiv.org/abs/2602.11095.
- *A stochastic vs deterministic perspective on the timing of cellular events*, Nature Communications (2024), https://www.nature.com/articles/s41467-024-49624-z (different bursty birth–death threshold setting).
