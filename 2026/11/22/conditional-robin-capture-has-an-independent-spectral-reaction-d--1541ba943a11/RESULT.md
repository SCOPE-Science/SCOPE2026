# Conditional Robin capture has an independent spectral reaction delay

## Finding
Consider one-dimensional Brownian diffusion of diffusivity \(D>0\) on \([0,L]\), \(L>0\), with a partially reactive endpoint at \(0\) of radiation reactivity \(\kappa>0\), and an absorbing escape endpoint at \(L\). Start at \(x\in(0,L)\). Let \(T_\kappa\) be the reaction time conditioned on reaction at \(0\) before escape at \(L\). Then
\[
T_\kappa\ \stackrel{d}{=}\ \tau_x+W_\kappa,
\]
where the summands can be independent, \(\tau_x\) is the first hitting time of \(0\) by a Brownian motion absorbed at both endpoints conditioned on hitting \(0\) first, and \(W_\kappa\) does not depend on \(x\).

Write \(\eta=\kappa L/D\). For every integer \(n\ge1\), let \(z_n\) be the unique solution of \(z_n\cot z_n=-\eta\) in \(((n-\tfrac12)\pi,n\pi)\), and set
\[
\rho_n=\frac{Dz_n^2}{L^2},\quad \nu_n=\frac{Dn^2\pi^2}{L^2},\quad p_n=1-\frac{\rho_n}{\nu_n}.
\]
Then the *full delay law* is the almost surely convergent independent sum
\[
W_\kappa\stackrel{d}{=}\sum_{n=1}^{\infty}B_nE_n,
\qquad B_n\sim\operatorname{Bernoulli}(p_n),\quad E_n\sim\operatorname{Exp}(\rho_n),
\]
with every variable on the right independent. The first \(N\ge1\) terms give an approximation \(W_{\kappa,N}\) satisfying the uniform, explicit coupling bound
\[
W_1\bigl(\mathcal L(W_\kappa),\mathcal L(W_{\kappa,N})\bigr)
\le\mathbb E[W_\kappa-W_{\kappa,N}]\le\frac{2L^2}{D\pi^2N^2}.
\]
For any \(\kappa_2>\kappa_1>0\) there is a coupling of the success-conditioned times, with the same initial position, such that \(T_{\kappa_2}<T_{\kappa_1}\) almost surely. In particular, larger reactivity gives strict first-order stochastic ordering (the distributions differ, with the usual non-strict cumulative inequality at every threshold).

The success probability is \(\kappa(L-x)/(D+\kappa L)\); it vanishes as \(\kappa\downarrow0\), although the conditional time laws converge to a finite, nondegenerate limit. The exact first two moments are
\[
\mathbb ET_\kappa=\frac{x(2L-x)}{6D}+\frac{L^2}{3D(1+\eta)},
\]
\[
\operatorname{Var}(T_\kappa)=\frac{L^4-(L-x)^4}{90D^2}+\frac{L^4}{D^2}\left(\frac{2}{45(1+\eta)}+\frac{1}{9(1+\eta)^2}\right).
\]

## Assumptions and scope
The diffusion generator is \(D\,d^2/dx^2\), with zero bulk drift, constant positive diffusivity, finite interval and zero initial local time. A Robin reaction at \(0\) is implemented by a boundary-local-time threshold with exponential reactivity \(\kappa\); reaching \(L\) causes irreversible escape. Conditioning requires \(\kappa>0\) and \(0<x<L\), giving a positive success probability. No results are asserted for position-dependent potential or diffusivity, multiple reacting boundaries, or coherent dynamics.

## Proof
**1. Exact conditional transform.** Let \(G_s(x)=\mathbb E_x[e^{-sT};\text{reaction before escape}]\). The backward problem \(DG_s''=sG_s\), \(G_s(L)=0\), \(DG_s'(0)=\kappa(G_s(0)-1)\) has, writing \(q=\sqrt{s/D}\), solution
\[
G_s(x)=\frac{\kappa\sinh(q(L-x))}{Dq\cosh(qL)+\kappa\sinh(qL)},
\quad G_0(x)=\frac{\kappa(L-x)}{D+\kappa L}.
\]
The limiting formulas at \(s=0\) are by continuity. Thus \(G_s/G_0\), the conditional Laplace transform, factors exactly as
\[
\underbrace{\frac{L\sinh(q(L-x))}{(L-x)\sinh(qL)}}_{\mathbb E e^{-s\tau_x}}
\cdot\underbrace{\frac{\kappa+D/L}{\kappa+Dq\coth(qL)}}_{\mathbb E e^{-sW_\kappa}}.
\]
The first factor solves the standard fully absorbing two-endpoint hitting problem conditioned on reaching the left endpoint.

**2. Positive random-time construction and coupling.** The partial-fraction identity for \(\coth\) gives the *nonnegative* Laplace exponent
\[
\phi(s)=Dq\coth(qL)-D/L
=\frac{2D}{L}\sum_{n\ge1}\frac{s}{s+\nu_n}.
\]
It is the Laplace exponent of a subordinator \(S_a\) with Lévy measure
\[
\Pi(dt)=\frac{2D}{L}\sum_{n\ge1}\nu_n e^{-\nu_n t}\,dt.
\]
Indeed, \(\int_0^\infty(1\wedge t)\Pi(dt)<\infty\), using \(\sum\nu_n^{-1}<\infty\), and \(\int(1-e^{-st})\Pi(dt)=\phi(s)\). If \(H_\kappa\) is independent exponential time of rate \(a_\kappa=\kappa+D/L\), then \(\mathbb E e^{-sS_{H_\kappa}}=a_\kappa/(a_\kappa+\phi(s))\), proving that \(W_\kappa\) exists and equals \(S_{H_\kappa}\) in distribution. Choose one uniform \(U\) and couple \(H_\kappa=-\log U/a_\kappa\) across reactivities, with the same subordinator and the same independent \(\tau_x\). The Lévy measure has infinite total mass, so this subordinator is strictly increasing almost surely on every nonempty time interval. Consequently the conditional times obey the claimed strict almost-sure ordering.

**3. Spectral independent-sum law.** The entire even function \(F(z)=\cosh z+\eta\sinh(z)/z\) has value \(1+\eta\) at zero. Its nonzero zeros are precisely \(\pm iz_n\): they are simple Robin–Dirichlet Sturm–Liouville eigenvalues, and the equation \(z\cot z=-\eta\) has one solution in each indicated half-period. By the canonical product for this order-one even entire function and its normalization,
\[
\frac{F(z)}{1+\eta}=\prod_{n\ge1}\left(1+\frac{z^2}{z_n^2}\right),\qquad
\frac{\sinh z}{z}=\prod_{n\ge1}\left(1+\frac{z^2}{n^2\pi^2}\right).
\]
With \(z=L\sqrt{s/D}\), the delay transform is therefore
\[
\mathbb E e^{-sW_\kappa}=\prod_{n\ge1}\frac{1+s/\nu_n}{1+s/\rho_n}.
\]
Each factor equals \(\mathbb E e^{-sB_nE_n}\) with the displayed Bernoulli probability and exponential rate; the infinite sum exists since \(\sum p_n/\rho_n<\infty\). Equality of Laplace transforms yields the distributional representation. Since \(z_n>(n-\tfrac12)\pi\), one has \(p_n<1/n\) and \(\rho_n>D\pi^2n^2/(4L^2)\). Hence \(\sum_{n>N}p_n/\rho_n\le4L^2(D\pi^2)^{-1}\sum_{n>N}n^{-3}\le2L^2/(D\pi^2N^2)\). The coupling induced by using the same summands gives the stated \(W_1\) bound.

**4. Moment and weak-reaction limits.** Differentiating the logarithm of the conditional transform at \(s=0\), using \(\sum n^{-2}=\pi^2/6\) and \(\sum n^{-4}=\pi^4/90\), gives the two moment formulas. As \(\kappa\downarrow0\), the delay transform tends to \((D/L)/(Dq\coth(qL))\); this is a probability law with the same finite-moment formula evaluated at \(\eta=0\). By Laplace-transform continuity the conditional total time converges in law. The separately computed reaction-before-escape probability tends to zero, so the finite conditional limit is not an unconditional absorption-time limit.

## Verification
The accompanying standalone \(\texttt{check.py}\) compares the reaction-flux boundary-value transform against the subordinator transform and a truncated Robin spectral product for twelve positive-discount/parameter combinations; it also checks the two moments by small-discount polynomial fitting. The script ran successfully with \(30\) tested comparisons; these finite numerical checks corroborate, but do not replace, the analytic infinite-series and coupling arguments. Reproduce with \(\texttt{python check.py}\) in an environment with NumPy and SciPy.

## Relationship to prior work
Wu, *Before the First Bond* (2026, arXiv:2611.01321, first public 31 October 2026), supplies the Robin/escape model, the general Laplace boundary-value problem, the flat-profile success probability, and conditional **mean** by quadrature; none is claimed new here. Its full text, including the conditional-time section and Appendix C, does not state the all-law independent delay, its Robin-spectral Bernoulli–exponential representation, an explicit uniform truncation error, or the almost-sure cross-reactivity coupling. Bressloff (2022, arXiv:2205.08929) develops the established encounter-based local-time and Dirichlet-to-Neumann spectral framework; those general methods are credited. The new point is the joint distributional/coupling result under competing escape, rather than the existence of a Robin Laplace boundary-value problem. Related surface-reaction and resetting models address different target outcomes or observables.

## Limitations
The result is for the exactly homogeneous, one-dimensional Brownian submodel; it does not establish equivalent independence for heterogeneous mobility, nonzero drift/depletion potentials, or multiple interacting targets. Stochastic ordering of successful times must not be confused with ordering of *unconditional* reaction times or with increased success probability. The weak-reaction limit conditions on increasingly rare events. Spectral/local-time methods are classical, and an implicit earlier derivation of these combined distributional statements cannot be categorically excluded without a broader archival audit. No independent scientific validation has been performed.

## References
- H. Wu, *Before the First Bond: Depletion-Assisted Stochastic Capture at the Onset of Endocytosis*, arXiv:2611.01321v1, 31 October 2026, https://arxiv.org/abs/2611.01321
- P. C. Bressloff, *Spectral theory of diffusion in partially absorbing media*, arXiv:2205.08929v1 (2022), https://arxiv.org/abs/2205.08929
- E. R. Whitehouse, M. R. Evans, S. N. Majumdar, *Effect of Partial Absorption on Diffusion with Resetting*, arXiv:1301.2489 (2013), https://arxiv.org/abs/1301.2489
