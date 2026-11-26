# Premature same-site pair crowding under fitness-dependent local resetting

## Finding
For the locally reset non-conserving zero-range process defined below, the stationary *ordered same-site pair density* has an exact representation in terms of the model's already-known one-particle stationary density. If the local resetting rate vanishes at maximal fitness like \(C(1-\ell)^\nu\), with \(C>0\) and \(0<\nu<1\), then the one-particle density stays finite as the total particle-removal rate approaches maximal fitness, but the same-site pair density has a sharp transition at \(\nu=1/2\).

Write \(\zeta=\beta+\delta-1>0\), with \(\beta>0\) the hopping rate and \(\delta>0\) the annihilation rate. For \(1/2<\nu<1\),
\[
\mathcal P_\zeta\sim A_{\nu,C}\,\zeta^{1/\nu-2},\qquad
A_{\nu,C}=\frac{2\pi C^{-1/\nu}(1-2^{1/\nu-1})}{\nu\sin(\pi/\nu)}>0.
\]
At \(\nu=1/2\),
\[
\mathcal P_\zeta\sim\frac{4}{C^2}\log(1/\zeta).
\]
For \(0<\nu<1/2\), \(\mathcal P_\zeta\) converges to a finite positive value. In every case \(0<\nu<1\), the mean particle density converges to a finite positive value. Thus the pair-divergence threshold strictly precedes the one-particle condensation threshold \(\nu=1\) of the motivating model.

## Assumptions and scope
At fitness \(\ell\in(0,1]\), the finite model has \(v_{\ell}\) distinct sites, each holding \(N\in\mathbb N_0\) particles. At one site, in the mean-field description and conditional on the stationary global density \(\rho_\zeta\), transitions are
\[
N\to N+1\quad\text{at rate }\ell N+u_\ell,\qquad
N\to N-1\quad\text{at rate }(1+\zeta)N,\qquad
N\to0\quad\text{at rate }r(\ell),
\]
with \(u_\ell=[\ell+\beta\rho_\zeta q(\ell)]/v_\ell\). This is the local-resetting process of Grange, arXiv:2311.12414, equations (21)--(25). Here \(q\) is a probability density on \([0,1]\), positive and continuous on \([0,1)\), with \(q(1-\varepsilon)=O(\varepsilon^\alpha)\) as \(\varepsilon\downarrow0\) for some \(\alpha>0\). Assume \(r\) is continuous and strictly positive on \([0,1)\), and \(r(1-\varepsilon)\sim C\varepsilon^\nu\), where \(C>0\) and \(0<\nu<1\).

Define
\[
A_0=\int_0^1\frac{\ell\,d\ell}{1-\ell+r(\ell)},\quad
B_0=\int_0^1\frac{q(\ell)\,d\ell}{1-\ell+r(\ell)},\quad
\beta_c=B_0^{-1}.
\]
Fix \(0<\beta<\min\{1,\beta_c\}\), put \(\delta=1+\zeta-\beta>0\), and let \(\zeta\downarrow0\). The thermodynamic/continuum limit for each fixed \(\zeta>0\) is taken **before** the limit \(\zeta\downarrow0\): first the number of sites at each nonmaximal fitness level tends to infinity, then the number \(L\) of equally spaced fitness levels tends to infinity. At finite \(L\), the uppermost level contributes a distinct term; the asserted critical law does not exchange these limits.

In a network with fitness levels \(k/L\), define the per-level ordered-pair observable by
\[
\mathcal P_{V,L,\zeta}=\frac1L\sum_{k=1}^{L}\sum_{s=1}^{v_k}\mathbb E\!\left[N_{k,s}(N_{k,s}-1)\right].
\]
Its sequential large-network limit is denoted \(\mathcal P_\zeta\). This is a within-site factorial second moment, **not** the variance of total particle number or an independent-site claim.

## Proof
**1. Exact site factorial moments.** Set \(a_\ell=1+\zeta-\ell>0\) and \(u=u_\ell\). Write \(M_1=\mathbb E[N]\), \(M_2=\mathbb E[N(N-1)]\) for the stationary one-site process. Applying its generator to \(N\) and \(N(N-1)\) yields
\[
0=u-(a_\ell+r(\ell))M_1,\qquad
0=2(\ell+u)M_1-(2a_\ell+r(\ell))M_2.
\]
The reset term on \(M_2\) is \(-r(\ell)M_2\), **not** \(-2r(\ell)M_2\), because one reset removes the whole site population. Consequently
\[
M_1=\frac{u}{a_\ell+r(\ell)},\qquad
M_2=\frac{2(\ell+u)u}{(a_\ell+r(\ell))(2a_\ell+r(\ell))}.
\]
For fixed \(\zeta>0\), the process has bounded stationary moments of these orders because the death-minus-linear-birth gap is positive. Multiplying by \(v_\ell\), then taking \(v_\ell\to\infty\) for each \(\ell<1\), gives
\[
\lim_{v_\ell\to\infty}v_\ell M_2
=\frac{2\ell[\ell+\beta\rho_\zeta q(\ell)]}
{(\zeta+1-\ell+r(\ell))[2(\zeta+1-\ell)+r(\ell)]}.
\]
The uppermost single site contributes \(O(L^{-1})\) to the normalized per-level observable at any fixed \(\zeta>0\). Hence, with the stated order of limits,
\[
\boxed{\displaystyle
\mathcal P_\zeta=\int_0^1\frac{2\ell[\ell+\beta\rho_\zeta q(\ell)]}
{[\zeta+1-\ell+r(\ell)][2(\zeta+1-\ell)+r(\ell)]}\,d\ell.}
\]

**2. Bounded one-particle density.** The existing stationary first-moment equation gives
\[
\rho_\zeta=\frac{A_\zeta}{1-\beta B_\zeta},\quad
A_\zeta=\int_0^1\frac{\ell\,d\ell}{\zeta+1-\ell+r(\ell)},\quad
B_\zeta=\int_0^1\frac{q(\ell)\,d\ell}{\zeta+1-\ell+r(\ell)}.
\]
Since \(0<\nu<1\), \(r(1-\varepsilon)\sim C\varepsilon^\nu\), and \(q(1-\varepsilon)=O(\varepsilon^\alpha)\), both integrals have finite limits by domination near \(\varepsilon=0\). The strict inequality \(\beta B_0<1\) implies
\[
\rho_\zeta\longrightarrow\frac{A_0}{1-\beta B_0}\in(0,\infty).
\]
In particular the numerator of the pair-density integrand approaches \(2\) as \(\ell\uparrow1\), uniformly for small \(\zeta\) in the asymptotically important region.

**3. Critical exponents and amplitudes.** Put \(\varepsilon=1-\ell\). For \(0<\nu<1/2\), the integrand is bounded near \(\varepsilon=0\) by a multiple of \(\varepsilon^{-2\nu}\), which is integrable. Dominated convergence proves a finite positive limit.

For \(1/2<\nu<1\), set \(\varepsilon=(\zeta/C)^{1/\nu}x\). On compact \(x\)-intervals, \(\varepsilon/\zeta\to0\) and \(r(1-\varepsilon)/\zeta\to x^\nu\). The scaled integral converges to
\[
\mathcal P_\zeta\sim 2C^{-1/\nu}\zeta^{1/\nu-2}
\int_0^\infty\frac{dx}{(1+x^\nu)(2+x^\nu)}.
\]
The integral's tail is \(O(x^{-2\nu})\), integrable precisely for \(\nu>1/2\). A uniform comparison \(r(1-\varepsilon)\asymp\varepsilon^\nu\) near zero controls the tail and justifies passage to the infinite interval; away from maximal fitness, the contribution is \(O(1)\). With \(p=1/\nu\in(1,2)\), the substitution \(t=x^\nu\) and the beta integral give
\[
\int_0^\infty\frac{dx}{(1+x^\nu)(2+x^\nu)}
=\frac{\pi(1-2^{p-1})}{\nu\sin(\pi p)},
\]
which is strictly positive since both the numerator and sine are negative. This yields the stated \(A_{\nu,C}\).

For \(\nu=1/2\), the matching scale is \(\varepsilon\asymp(\zeta/C)^2\). In the logarithmically broad region \((\zeta/C)^2\ll\varepsilon\ll1\), the integrand is asymptotic to \(2/(C^2\varepsilon)\). Integrating over that region yields
\[
\mathcal P_\zeta\sim\frac{2}{C^2}\log\!\frac{1}{(\zeta/C)^2}
\sim\frac{4}{C^2}\log(1/\zeta).
\]
Uniform upper and lower comparisons obtained from \(r(1-\varepsilon)\sim C\sqrt\varepsilon\), together with bounded contributions away from the high-fitness endpoint, prove that the coefficient is exact. These three cases exhaust \(0<\nu<1\).

## Verification
The accompanying `checks/checker.py` independently solves three truncated stationary birth-death-reset Markov generators and compares both site factorial moments with the formulas. It also performs 40-digit quadrature of \(\rho_\zeta\) and \(\mathcal P_\zeta\) for \(q(\ell)=2(1-\ell)\), \(r(\ell)=1.2(1-\ell)^\nu\), \(\beta=0.3\), and \(\nu\in\{0.4,0.5,0.6,0.75\}\), checking the finite-mean behavior, nonnegative pair counts, asymptotic amplitudes and beta-integral identity. The checker passed 32 numerical consistency assertions with Python, NumPy, SciPy and mpmath. The proof of the infinite-volume and \(\zeta\downarrow0\) statements is analytic; finite-state and finite-precision computations do not prove those limits.

## Relationship to prior work
Grange, *Local resetting in non-conserving zero-range processes with extensive rates* (arXiv:2311.12414, initially public 21 November 2023), defines precisely the local fitness-dependent resetting process, derives its one-site master equation and generating-function evolution, and determines its **first-moment** density and the separate \(\nu=1\) condensation boundary. Those inputs are prior work and are not claimed as new. The derived second factorial moment is a direct stationary generator computation; the claimed extension is its **integrated same-site pair observable**, the sharp earlier transition at \(\nu=1/2\), and the explicit logarithmic/power-law amplitudes in the noncondensed regime. Grange's earlier arXiv:1910.05991 treats global rather than independently local resetting and does not assert this local-reset pair threshold. Searches for alternate second-moment and pair-crowding formulations did not identify an equivalent statement, but absence from search results is not a proof of priority.

## Limitations
The pair observable is an ordered within-site factorial moment, not a susceptibility of the full interacting network, a covariance between sites, or a thermodynamic central limit theorem. The precise mean-field closure and order of the network/continuum limits are assumed; interchanging the size limit with \(\zeta\downarrow0\) may produce a different singularity. The analysis is restricted to \(0<\nu<1\), \(\beta<\min\{1,\beta_c\}\), and positive site-reset rates away from maximal fitness. It neither proves finite-network asymptotics nor a pair-condensation theorem for \(\nu\ge1\). The generating-function formulation in the source is broad enough that moments could be independently differentiated from it; therefore previously unnoticed equivalent analyses remain a priority risk.

## References
1. P. Grange, *Local resetting in non-conserving zero-range processes with extensive rates*, arXiv:2311.12414 (first posted 21 November 2023), https://arxiv.org/abs/2311.12414. Especially equations (21)--(25), (31)--(32), (41)--(49).
2. P. Grange, *Non-conserving zero-range processes with extensive rates under resetting*, arXiv:1910.05991 (2019), https://arxiv.org/abs/1910.05991. Global-resetting and first-moment background.
