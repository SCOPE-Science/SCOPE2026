# A double-turn desorption-noise response in a three-site exclusion channel

## Finding

Consider a stationary open, three-site totally asymmetric simple exclusion process with boundary injection and extraction rates one, both forward-bond hopping rates one, center-site adsorption rate \(u>0\), and center-site desorption rate one. For each event class \(k\), let \(N_k(t)\) count successful transitions and define the asymptotic Fano factor
\[
 F_k(u)=\lim_{t\to\infty}\frac{\operatorname{Var}N_k(t)}{\mathbb E N_k(t)}.
\]
The limit is independent of the initial configuration. The four distinct Fano-factor response curves are classified **exactly** for all \(u>0\):

| Count | Global rate-response shape | Exact endpoint limits \(u\downarrow0,\ u\to\infty\) | Critical rates |
|---|---|---|---|
| Accepted injection (equivalently first-bond hops) | Strictly increasing | \(82369/211185,\ 1\) | None |
| Extraction (equivalently second-bond hops) | Decreasing then increasing, unique strict minimum | \(2820413/4792275,\ 1/2\) | \(u\approx2.841725432110\), \(F\approx0.488065533275\) |
| Center adsorption | Decreasing then increasing, unique strict minimum | \(1,\ 5/6\) | \(u\approx2.276602471502\), \(F\approx0.590847358418\) |
| Center desorption | Increasing, decreasing, then increasing | \(3719453/5766975,\ 1\) | Unique strict maximum at \(u\approx0.140280550641\), \(F\approx0.648831281670\); unique strict minimum at \(u\approx0.680873521970\), \(F\approx0.642880653006\) |

In particular, tuning adsorption at fixed desorption produces a **two-turn** noise response in desorption counts, in contrast to the zero or one critical rates of the other three event classes. All critical points are simple and are uniquely specified by exact rational polynomials in the standalone `certificate.json`. The four Fano factors themselves are exactly specified by the numerator and denominator coefficient arrays in that certificate, in descending degree order; this is an exact rational-function statement, not a numerical fit.

## Assumptions and scope

States are triples \(\eta=(\eta_1,\eta_2,\eta_3)\in\{0,1\}^3\). From any state, the allowed events are: \(0\to1\) at site one at rate one; \(1\to0\) at site three at rate one; rightward hops \(10\to01\) across each of the two bonds at rate one; center-site \(0\to1\) at rate \(u\) and \(1\to0\) at rate one. In each case a transition only occurs when the required occupancy pattern is present. Distinct events are counted separately, and an unsuccessful attempted transition is not counted. These six allowed event types give an irreducible finite-state continuous-time Markov chain for every \(u>0\). We count each completed successful event, including adsorption and desorption, not an instantaneous occupancy covariance or the signed net current.

For an open chain, accepted injection and completed first-bond hops differ by at most one at every time (the change in occupancy at site one); likewise extraction and second-bond hops differ by at most one (the change in occupancy at site three). Therefore their asymptotic means and variance growth rates, and hence their Fano ratios, coincide. This leaves exactly the four genuinely different count classes in the table.

## Proof

Order states lexicographically as \(000,001,010,011,100,101,110,111\), represent probability vectors as columns, and construct the eight-by-eight generator \(Q(u)\) by adding the specified positive off-diagonal transition rates and making its columns sum to zero. For event type \(k\), let \(J_k(u)\) contain just its off-diagonal transition rates and zeros elsewhere. For the unique stationary distribution \(\pi\),
\[
 Q\pi=0,\qquad \mathbf1^\mathsf T\pi=1,\qquad
 j_k=\mathbf1^\mathsf T J_k\pi>0.
\]
The exponential tilt of the selected event gives generator \(Q+(e^s-1)J_k\). Differentiating its simple dominant eigenvalue twice at \(s=0\), or equivalently differentiating the count-moment master equations, gives the exact Poisson corrector identity
\[
 Q r_k=-(J_k\pi-j_k\pi),\quad
 \mathbf1^\mathsf T r_k=0,\qquad
 F_k=\frac{j_k+2\mathbf1^\mathsf T J_k r_k}{j_k}.
\]
These formulas hold at every positive \(u\). They are implemented using exact rational arithmetic in `verify.py`; the explicit exact resulting rational numerators and denominators are stored in `certificate.json`. In particular the common denominator of the four mean event rates is
\[
 P(u)=6u^4+65u^3+258u^2+442u+285,
\]
and the four mean rates, in table order, are respectively
\[
\frac{(u+2)(9u^2+47u+65)}{P(u)},\quad
\frac{3u^4+31u^3+112u^2+158u+59}{P(u)},
\]
\[
\frac{u(u+2)(9u^2+60u+107)}{P(u)},\quad
\frac{6u^4+56u^3+180u^2+215u+71}{P(u)}.
\]

For each event class \(k\), exact differentiation of its certified rational Fano function gives
\[
 F_k'(u)=\frac{2p_k(u)}{d_k(u)},
\]
where \(p_k\) is the integer polynomial `derivative_num_primitive`, and \(d_k\) the integer polynomial `derivative_den` in the certificate. Every coefficient of each \(d_k\) is strictly positive; hence \(d_k(u)>0\) throughout \(u>0\). Write polynomial coefficients from highest to lowest degree and let their plus/minus signs be the signs of the integer coefficients. Direct inspection of the fully included exact polynomial coefficient arrays yields:

| Event | Descending coefficient signs of \(p_k\) | Positive roots allowed by Descartes |
|---|---|---|
| Injection | \(+++++++++++++++++\) | 0 |
| Extraction | \(+++++++++---------\) | 1 |
| Adsorption | \(++++++++++-------\) | 1 |
| Desorption | \(++++++++++++++----+\) | 2 or 0 |

For extraction and adsorption, \(p_k(0)<0<p_k(3)\); each has at least one root, so Descartes' rule forces exactly one simple positive root and the negative-to-positive derivative transition. The injection polynomial is strictly positive at every positive \(u\). For desorption, \(p_{\mathrm{de}}(0)>0\), \(p_{\mathrm{de}}(1/4)<0\), and \(p_{\mathrm{de}}(1)>0\). Thus there is at least one root in each of \((0,1/4)\) and \((1/4,1)\), and the two-variation bound proves **exactly two**, both simple. The signs and strict extremum types follow. Finally, leading and constant coefficients of the exact Fano polynomials yield the endpoint limits in the table. The included rational root brackets and exact sign checks establish the quoted decimal values. This proves the complete classification for every \(u>0\).

## Verification

The self-contained `certificate.json` contains every mean-current and Fano numerator/denominator, every normalized derivative numerator and denominator, positive-root rational isolating intervals, and exact endpoint values. The standalone `verify.py` reconstructs the eight-state marked generator, solves the stationary and Poisson equations symbolically and confirms every integer coefficient against the certificate. It independently propagates count moments using a 24-dimensional block ODE at five rational adsorption rates for all four event types. Executing `python verify.py` from this directory with Python 3, SymPy, NumPy and SciPy reports all exact checks and 20 independent moment-propagation comparisons passed. The exact symbolic identities and Descartes arguments, not sampled numerical observations, establish the global assertions.

## Relationship to prior work

Silva, Carvalho, Almeida and Duarte-Filho (arXiv:2611.07053, first publicly submitted November 4, 2026) formulate TASEP–Langmuir open-chain dynamics with independent bulk adsorption and desorption and compute finite-chain stationary density profiles and occupancy correlations. Their Section II gives precisely the transition types used here (specialized to three sites), while Sections IV–V concern static spatial observables rather than long-time event-count variance or its adsorption-rate critical points. The stationary-generator methodology and general tilted-generator counting formulas are established tools and are not asserted to be novel.

The known **equal-adsorption/equal-desorption** three-site count-covariance classification follows the distinct one-parameter path \(\omega_A=\omega_D=w\); it does not fix desorption while varying \(\omega_A=u\), and cannot imply the present two-turn adsorption-scan curve. The published current-fluctuations study of a partially asymmetric exclusion ring with a moving defect (Lobaskin, Evans and Mallick, 2024) has neither the finite open Langmuir channel nor the four distinct attachment, detachment and boundary event-count responses. The claim here is confined to the exact four-channel adsorption-rate response classification and does not claim that generic finite Markov counting formulas are new.

## Limitations

Only one adsorption-rate control parameter is varied, with all other dimensional rates normalized to one; arbitrary boundary asymmetry, longer chains and other adsorption/desorption paths are not classified. The two-turn change in desorption Fano factor is quantitatively modest and is a structural exact response rather than evidence of a large experimentally measurable effect. The count Fano limits are long-time properties and do not imply finite-window monotonicity. No independent scientific audit has been performed. An equivalent derivation in unindexed finite-size full-counting-statistics literature remains a publication-priority risk.

## References

1. L. D. S. Silva, A. M. S. Carvalho, F. A. G. Almeida and G. C. Duarte-Filho, *Langmuir kinetics and totally asymmetric volume exclusion in linear chains via Fock space formalism*, arXiv:2611.07053v1, submitted November 4, 2026, https://arxiv.org/abs/2611.07053.
2. I. Lobaskin, M. R. Evans and K. Mallick, *Current fluctuations in a partially asymmetric simple exclusion process with a defect particle*, Physical Review E 109, 024127 (2024), https://doi.org/10.1103/PhysRevE.109.024127.
3. M. Watanabe, *On perturbation around closed exclusion processes*, arXiv:2406.02675v1, June 4, 2024, https://arxiv.org/abs/2406.02675 (stationary nonconserving exclusion theory, not full counting statistics).
