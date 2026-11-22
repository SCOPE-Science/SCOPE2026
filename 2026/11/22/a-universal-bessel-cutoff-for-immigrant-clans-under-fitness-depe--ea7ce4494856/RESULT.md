# A universal Bessel cutoff for immigrant clans under fitness-dependent local clearing

## Finding

Consider a subcritical birth–death–immigration level with many individually cleared microscopic sites, as defined below. Its stationary total occupation approaches a **compound-Poisson law** when the number of sites tends to infinity at fixed total immigration input. The positive-jump intensities have an explicit one-founder branching representation. In the near-optimal-fitness, near-critical regime, the entire large-clan cutoff converges to the universal modified-Bessel profile
\[
\boxed{\lim_{\substack{\ell\uparrow1,\ n\to\infty\\n r(\ell)\to s}} n\Lambda_n(\ell,0)=2\sqrt{s}\,K_1(2\sqrt{s}),\qquad s\in(0,\infty).}
\]
Here \(\Lambda_n\) is the compound-Poisson intensity of a jump of size \(n\), and \(K_1\) is the standard modified Bessel function of the second kind. The convergence holds for any clearing law satisfying \(r(1-w)\sim Cw^\nu\) with \(C>0\) and \(0<\nu<1\), and for the admissible self-consistent immigration profile below. Its scaling shape does not involve \(C\), \(\nu\), or the mutation parameter once the clan size is measured in units of \(1/r(\ell)\). The profile tends to one as \(s\downarrow0\) and obeys \(2\sqrt{s}K_1(2\sqrt{s})\sim\sqrt\pi\,s^{1/4}e^{-2\sqrt{s}}\) as \(s\to\infty\).

## Assumptions and scope

Let \(q\) be a continuous nonnegative probability density on \([0,1]\), with \(q(1-w)=O(w^\alpha)\) for some \(\alpha>0\). Let \(r\) be continuous, positive on \([0,1)\), and satisfy \(r(1-w)\sim Cw^\nu\) for \(0<\nu<1\). Fix \(\beta>0\) such that
\[
\beta\int_0^1\frac{q(\ell)}{1-\ell+r(\ell)}\,d\ell<1,\qquad 0<\beta<1.
\]
For \(\zeta\ge0\), define \(\delta=1+\zeta-\beta>0\) and the finite mean-field density and level input
\[
\rho_\zeta=\frac{\displaystyle\int_0^1\frac{\ell\,d\ell}{\zeta+1-\ell+r(\ell)}}{\displaystyle1-\beta\int_0^1\frac{q(\ell)\,d\ell}{\zeta+1-\ell+r(\ell)}},\qquad
 a_\zeta(\ell)=\ell+\beta\rho_\zeta q(\ell).
\]
For each fixed interior fitness \(\ell\in(0,1)\), introduce \(v\) independent identical stationary continuous-time chains with occupations in \(\mathbb N_0\). A chain at occupation \(j\) has upward rate \(\ell j+a_\zeta(\ell)/v\), downward rate \((1+\zeta)j\), and independent total clearing to zero at rate \(r(\ell)\). Let \(Y_{v,\ell,\zeta}\) be their sum. This is the independently factorized level-marginal model associated with the large-network equations of Grange (2023); no joint finite-network assertion is made. The multiplicity limit \(v\to\infty\) is taken first at fixed \(\ell<1\) and fixed \(\zeta\ge0\). Only then is \(\zeta=0\) fixed and the double limit \(\ell\uparrow1\), \(n\to\infty\), \(n r(\ell)\to s>0\) taken.

## Proof

**1. Stationary microscopic law and rare immigration.** Write \(\lambda=\ell\), \(\mu=1+\zeta\), \(g=\mu-\lambda>0\), \(R=r(\ell)>0\), and \(a=a_\zeta(\ell)\). The process without immigration consists of independent continuous-time branching families, each originating from a single individual, with per-individual birth rate \(\lambda\) and death rate \(\mu\). Denote such a one-founder process by \(Z_t\), started from \(Z_0=1\).

A stationary clearing age \(T\) is exponential with rate \(R\). Conditional on \(T=t\), independently arriving founders of intensity \(a/v\) over the interval since clearing produce a Poisson cluster superposition. Hence its stationary single-site probability generating function satisfies, for \(0\le z\le1\),
\[
 G_v(z)=\int_0^\infty R e^{-Rt}\exp\!\left[\frac av\int_0^t\bigl(\mathbb E z^{Z_u}-1\bigr)\,du\right]dt.
\]
For fixed \(R>0\), the inner integral is bounded by \(t\), and its exponential moments under \(\mathrm{Exp}(R)\) permit differentiation at immigration intensity zero. In particular,
\[
G_v(z)=1+\frac av\int_0^\infty e^{-Ru}\bigl(\mathbb E z^{Z_u}-1\bigr)du+o(v^{-1}).
\]
By independence of the \(v\) site chains, \(\mathbb E z^{Y_{v,\ell,\zeta}}=G_v(z)^v\), which converges to
\[
\exp\!\left[\sum_{n\ge1}\Lambda_n(\ell,\zeta)(z^n-1)\right],\qquad
\Lambda_n(\ell,\zeta)=a_\zeta(\ell)\int_0^\infty e^{-r(\ell)t}\Pr\{Z_t=n\}\,dt.
\]
The intensities are nonnegative, and \(\sum_{n\ge1}\Lambda_n\le a/R<\infty\), so the displayed exponent defines a proper compound-Poisson law. Convergence of the probability generating functions gives convergence in distribution.

**2. One-founder distribution.** Put \(u_t=e^{-gt}\). The elementary branching backward equation gives, for every integer \(n\ge1\),
\[
\Pr\{Z_t=n\}=\frac{g^2u_t}{(\mu-\lambda u_t)^2}
\left[\frac{\lambda(1-u_t)}{\mu-\lambda u_t}\right]^{n-1}.
\]
This is the geometric conditional law of the positive surviving population; it has mass \(1-\mu(1-u_t)/(\mu-\lambda u_t)\) on positive integers. It follows either by substituting the linear-fractional generating function into the birth–death backward equation or from the Riccati equation for the generating function; this step is independent of the stationarity argument.

**3. Edge scaling.** Set \(\zeta=0\), \(w=1-\ell\), \(R=r(\ell)\), and take sequences with \(nR\to s\in(0,\infty)\). Since \(R\sim Cw^\nu\) with \(\nu<1\), we have \(nw=(nR)(w/R)\to0\). For fixed \(y>0\), substitute \(t=ny\) in the preceding exact mass formula. Elementary expansions at \(nw\to0\) give
\[
 n^2\Pr\{Z_{ny}=n\}\longrightarrow y^{-2}e^{-1/y}.
\]
For completeness, a uniform integrable bound is available. With \(\lambda=1-w\ge1/2\) and \(t\ge0\), the positive-state geometric prefactor is at most \(C_0(1+t)^{-2}\), and its geometric parameter is no larger than \(t/(1+t)\). To justify the limit under the integral, split \(y\in(0,1/n)\), \(y\in[1/n,1]\), and \(y\ge1\). On the first interval, the geometric ratio is at most \(1/2\), and the contribution to the scaled integral is \(O(n2^{-n})\). On the middle interval, the bound on the ratio yields an envelope \(C_1y^{-2}e^{-1/(4y)}\); on the last interval, the envelope \(C_1y^{-2}\) is integrable. These estimates, together with \(Rn\to s>0\), justify dominated convergence after discarding the vanishing first interval. Moreover, the finiteness of \(\rho_0\) and \(q(1-w)\to0\) yield \(a_0(1-w)\to1\). Consequently,
\[
 n\Lambda_n(1-w,0)\longrightarrow\int_0^\infty y^{-2}e^{-1/y-sy}\,dy
 =2\sqrt{s}\,K_1(2\sqrt{s}).
\]
The final equality follows from the standard integral representation of \(K_1\), and the endpoint claims follow from its classical small- and large-argument asymptotics. This completes the single compound-Poisson/Bessel-cutoff theorem.

## Verification

The standalone `CHECK.py` implements exact rational generator checks for the stationary factorial-moment recursion and independently evaluates the one-founder distribution under near-critical size scaling. It passes 319 checks, including three examples where the scaled Lévy intensities approach the Bessel-kernel integral and an independent numerical value at \(s=1\). These checks probe normalization and scaling but do not replace the infinite-site or double-limit arguments above. Run `python CHECK.py` with the Python standard library.

## Relationship to prior work

Grange (arXiv:2311.12414v1, first available 2023-11-21) defines the local-clearance fitness model, derives its site generating-function evolution and mean density, and analyzes the mean-density condensation boundary. Kapodistria, Phung-Duc and Resing (Eurandom preprint 2015-006, Section 3.2 and total-catastrophe Section 5.3) derive stationary factorial moments for the underlying linear birth–immigration–death chain; neither the pointwise factorial recurrence nor the earlier mean-density formula is claimed as new. A published study of the same local-reset fitness model already establishes the integrated second factorial-moment transition, and a separate prior result gives the full higher-order integrated factorial intensity hierarchy; **neither hierarchy is part of the present novelty claim**. The present theorem instead determines the *jump-size distribution* of the dilute-site compound-Poisson limit, and its universal moving-size Bessel cutoff. Lambert's earlier work on neutral immigrant-family abundance gives classical log-series \(1/n\) behavior; no novelty is claimed for the log-series alone. The finite-cutoff Bessel law is a stronger joint near-critical statement than a fixed-order moment calculation. Full bibliographic search cannot establish absolute publication priority.

## Limitations

This statement concerns stationary independently factorized level marginals with fixed deterministic self-consistent input. It does not establish a simultaneous finite-network mean-field/fluctuation limit or independence among fitness levels in a finite population. The Bessel scaling requires \(0<\nu<1\), \(\zeta=0\), and size \(n\) tending to infinity jointly with \(\ell\uparrow1\); fixed-fitness large-size tails may differ. No asymptotic error rate, uniformity at \(s=0\) or \(s=\infty\), or extension to non-Poisson resetting is asserted. The cutoff kernel is conditional on the stated model and is not a claim about a universal family-size distribution under all branching laws.

## References

1. P. Grange, *Local resetting in non-conserving zero-range processes with extensive rates*, arXiv:2311.12414v1, first posted 2023-11-21, https://arxiv.org/abs/2311.12414 . See Sections 3–5 and Appendix C.
2. S. Kapodistria, T. Phung-Duc and J. Resing, *Linear birth/immigration-death process with binomial catastrophes*, Eurandom Preprint 2015-006, 2015-03-16, https://www.eurandom.tue.nl/reports/2015/006-report.pdf . See Lemma 3.1 and Section 5.3; journal DOI https://doi.org/10.1017/S0269964815000297 .
3. *A hidden co-occupation threshold below fitness condensation*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-hidden-co-occupation-threshold-below-fitness-condensation--b88c55090541 .
4. A. Lambert, *Species abundance distributions in neutral models with immigration or mutation and general lifetimes*, arXiv:1009.0118, first posted 2010-09-01, https://arxiv.org/abs/1009.0118 .
5. N. Dori et al., *Family-size variability grows with collapse rate in a birth-death-catastrophe model*, Phys. Rev. E 98 (2018), 012416, https://doi.org/10.1103/PhysRevE.98.012416 .
