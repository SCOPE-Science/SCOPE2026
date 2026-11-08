# Exact localization autocorrelation and renewal-clock reconstruction under Poisson resetting

## Finding

Consider a continuous-time random walk (CTRW) on the real line with independent spatial increments having a non-atomic law. Its independent, identically distributed positive holding times have a continuous survival function \(\Psi(t)=\Pr(W>t)\), with \(\Psi(0)=1\) and \(\Pr(W<\infty)=1\). The walk is reset to zero by an independent Poisson process of rate \(r>0\); each reset also discards its previous renewal clock and draws a new holding time. For its unique stationary law, let \(I_t=\mathbf{1}_{\{X_t=0\}}\), \(m=\mathbb E I_0\), \(R(t)=\operatorname{Corr}(I_0,I_t)\), and
\[
\mu_r=\int_0^\infty e^{-ru}\Psi(u)\,du.
\]
Then \(0<m=r\mu_r<1\), and for every \(t\geq0\),
\[
\boxed{\operatorname{Cov}(I_0,I_t)=(1-m)r\int_t^\infty e^{-ru}\Psi(u)\,du,\quad
R(t)=\frac{\int_t^\infty e^{-ru}\Psi(u)\,du}{\mu_r}.}
\]
In particular, the stationary atom \(m\) together with the complete lag-correlation curve \(R\) **jointly identifies the unknown reset rate and the entire holding-time law**, without knowing the spatial jump distribution:
\[
\boxed{r=-mR'(0+),\qquad \Psi(t)=e^{rt}\frac{R'(t)}{R'(0+)}\quad(t\ge0).}
\]
The inverse identity also holds at right derivatives if the survival function is right-continuous but not continuous.

For the Lomax holding-time family \(\Psi(t)=(1+t/a)^{-\beta}\), \(a,\beta>0\), the normalized autocorrelation is exactly
\[
R(t)=\frac{\Gamma(1-\beta,r(t+a))}{\Gamma(1-\beta,ra)}
\]
where \(\Gamma(s,z)=\int_z^\infty u^{s-1}e^{-u}\,du\) for \(z>0\), including negative \(s\). Its integrated correlation time \(\tau_{\mathrm{int}}=\int_0^\infty R(t)\,dt\) satisfies the five sharp weak-reset regimes, as \(r\downarrow0\) with \(a,\beta\) fixed:
\[
\tau_{\mathrm{int}}\sim
\begin{cases}
(1-\beta)/r,&0<\beta<1,\\
1/[r\log(1/(ra))],&\beta=1,\\
(\beta-1)\Gamma(2-\beta)a^{\beta-1}r^{\beta-2},&1<\beta<2,\\
a\log(1/(ra)),&\beta=2,\\
a/(\beta-2),&\beta>2.
\end{cases}
\]
Thus the first and second holding-time moment thresholds appear as two distinct temporal decorrelation boundaries, even though the stationary localization mass exists for all \(r>0\) and \(\beta>0\).

## Assumptions and scope

All resets are *complete* (they restore the spatial position and the renewal clock). Reset events are independent of the CTRW. Holding times are strictly positive almost surely, finite almost surely, and independent of all spatial jumps and resets; their survival function is continuous and takes the value one at zero. Jump increments are independent and non-atomic. These hypotheses ensure that, at any fixed observation instant, \(X_t=0\) if and only if no spatial jump has taken place since the last reset, almost surely. There is no assumption of a finite unreset mean holding time or finite spatial-jump variance. The theorem is for stationary **independent** Poisson resetting, not for preferential, extremal, partial-clock, or interacting reset rules. Time \(t\) and rate \(r\) are physical (not rescaled). A unique stationary version exists because every positive-rate reset regenerates the full process; the stationary age since the last reset is exponential with rate \(r\).

## Proof

**1. Renewal age and stationary localization.** Let \(A\sim\mathrm{Exp}(r)\) denote the backward time since the most recent reset. The holding time \(W\) drawn at that reset is independent of \(A\). Non-atomic jumps ensure the localization indicator equals \(\mathbf{1}_{\{A<W\}}\), so
\[
m=\int_0^\infty re^{-ra}\Psi(a)\,da=r\mu_r.
\]
The assumptions on \(W\) imply \(0<m<1\).

**2. Two-time probability by partitioning on the last reset.** Write \(F(u)=e^{-ru}\Psi(u)\). Start a fresh copy at a reset and let \(f(t)\) be the probability that it is still localized at time \(t\). Conditioning on the last reset in \((0,t]\) (or no reset) gives the exact identity
\[
f(t)=F(t)+r\int_0^t F(u)\,du.
\]
At stationarity, condition on the absence or occurrence of a reset in \((0,t]\). If none occurs, both observations are at the origin precisely when the holding time associated with the reset before time zero exceeds the backward reset age plus \(t\); this event has probability
\[
B(t)=\int_0^\infty re^{-ra}e^{-rt}\Psi(a+t)\,da
=r\int_t^\infty F(u)\,du.
\]
If one or more resets occur, the last reset before \(t\) erases all information about the indicator at time zero. The probability of \(I_0=I_t=1\) contributed by those histories is \(m\,r\int_0^t F(u)\,du\). Hence
\[
\mathbb E(I_0I_t)=B(t)+mr\int_0^tF(u)\,du
=m^2+(1-m)B(t).
\]
Subtracting \(m^2\) proves the covariance. Since \(\operatorname{Var}(I_0)=m(1-m)\), division gives \(R(t)=B(t)/m\).

**3. Nonparametric identifiability.** For continuous \(\Psi\), the correlation curve is continuously differentiable on \([0,\infty)\), with
\[
R'(t)=-e^{-rt}\Psi(t)/\mu_r,\qquad R'(0+)=-1/\mu_r.
\]
Using \(m=r\mu_r\) gives \(r=-mR'(0+)\); division of the two derivative identities gives the stated formula for \(\Psi\). Consequently two different admissible pairs \((r,\Psi)\) cannot have the same stationary localization mass and full lag correlation. This is population-level identification, not a finite-sample statistical guarantee.

**4. Power-law exact form and temporal phases.** For \(\Psi(u)=(1+u/a)^{-\beta}\), the substitution \(z=r(u+a)\) yields
\[
\int_t^\infty e^{-ru}\Psi(u)\,du
=e^{ra}a^\beta r^{\beta-1}\Gamma(1-\beta,r(t+a)).
\]
The ratio proves the gamma formula. Tonelli's theorem gives
\[
\tau_{\mathrm{int}}
=\frac{\int_0^\infty u e^{-ru}\Psi(u)\,du}{\int_0^\infty e^{-ru}\Psi(u)\,du}
=-\partial_r\log\mu_r.
\]
For \(0<\beta<1\), rescaling \(z=ru\) yields denominator \(a^\beta\Gamma(1-\beta)r^{\beta-1}(1+o(1))\) and numerator \(a^\beta\Gamma(2-\beta)r^{\beta-2}(1+o(1))\). At \(\beta=1\), the denominator is \(a\log(1/(ra))(1+o(1))\) and numerator is \(a/r(1+o(1))\). For \(1<\beta<2\), the denominator tends to \(a/(\beta-1)\), while the numerator is \(a^\beta\Gamma(2-\beta)r^{\beta-2}(1+o(1))\). At \(\beta=2\), the denominator tends to \(a\) and numerator is \(a^2\log(1/(ra))(1+o(1))\). For \(\beta>2\), both limits exist and integration of the Lomax tail yields numerator \(a^2/[(\beta-1)(\beta-2)]\) and denominator \(a/(\beta-1)\). Division proves all five cases, including their boundary constants.

## Verification

Run `python3 CHECKER.py` (standard Python library only). The checker compares the exact covariance and inversion with independent exponential- and fixed-holding-time formulas, independently integrates the power-law profile, checks the integrated-correlation formula in all five parameter ranges, and simulates stationary two-time indicator pairs for an exponential and a Lomax holding law. It is a finite, reproducible diagnostic, not a substitute for the all-parameter proof above. The source's stationary atom formula is separately matched by \(m=1-\mathbb E[e^{-rW}]\) using integration by parts.

## Relationship to prior work

Vilk (arXiv:2601.13595v1, first public January 20, 2026), section “Independent resetting” and Supplement S1, derives the mixed stationary one-time distribution, including its atom \(m=1-\widehat\psi(r)\), and discusses macroscopic localization and collective-reset aging. That spatial law is prior work. The present result addresses the distinct **stationary two-time origin occupancy**, its inverse reconstruction of both the reset rate and full waiting-time survival law, and the five weak-reset integrated-correlation regimes. Kuśmierz and Gudowska-Nowak (2019) study subdiffusive CTRWs under complete versus incomplete resetting, emphasizing propagators, moments and first hitting times. Bodrova and Sokolov (2020) study power-law reset intervals, a different reset-clock model. General alternating-renewal two-time identifiability can fail without the reset-clock structure: the restricted inverse formula here exploits both the known Poisson form and the observable stationary atom, rather than asserting generic two-state identifiability.

## Limitations

The inference is ideal population-level: derivatives at time zero and an entire lag curve may be unstable to sampling noise. Without the full renewal-clock reset, or if the jump law has spatial atoms permitting positive probability of returning exactly to zero, the localization indicator no longer means “no jump since last reset” and the proof need not apply. The theory does not infer the spatial jump kernel. The exact correlation identity is a specialization of general regenerative and renewal techniques; a more general indexed theorem may subsume it. No independent audit or experimental validation is claimed.

## References

- O. Vilk, “Macroscopic localization and collective memory in Poisson renewal resetting,” arXiv:2601.13595v1 (first posted 2026-01-20). https://arxiv.org/html/2601.13595v1
- Ł. Kuśmierz and E. Gudowska-Nowak, “On subdiffusive continuous time random walks with stochastic resetting,” arXiv:1812.08489 (2019); Phys. Rev. E 99, 052116. https://arxiv.org/abs/1812.08489
- A. S. Bodrova and I. M. Sokolov, “Continuous-time random walks under power-law resetting,” arXiv:2001.01350 (2020); Phys. Rev. E 101, 062117. https://arxiv.org/abs/2001.01350
- O. Vilk and B. Meerson, “Collective behavior of independent scaled Brownian particles with renewal resetting,” arXiv:2512.21061v1 (2025). https://arxiv.org/html/2512.21061v1
