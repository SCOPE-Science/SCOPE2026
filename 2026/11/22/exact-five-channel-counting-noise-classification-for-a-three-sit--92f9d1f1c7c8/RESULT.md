# Exact five-channel counting-noise classification for a three-site TASEP with Langmuir exchange

## Finding

In the minimal open totally asymmetric simple exclusion chain having a bulk Langmuir site, increasing equal bulk adsorption and desorption rates yields **three different qualitative counting-noise responses**: strictly increasing boundary-event Fano factors, strictly decreasing Langmuir-event Fano factors, and an internal-hop Fano factor with exactly one strict maximum. Simultaneously, all ten cross-covariances among the five physically distinct event counts have fixed, strictly nonzero signs for every positive exchange rate.

Specifically, write the dimensionless bulk exchange rate as \(w>0\) and let the five count labels be \(\mathrm{in},\mathrm{ex},\mathrm{ad},\mathrm{de},\mathrm{hop}\). The last counts **both** successful internal hops. For stationary long-time event counts define
\[
C_{ab}(w)=\lim_{t\to\infty}\frac{\operatorname{Cov}(N_a(t),N_b(t))}{t},\qquad
F_a(w)=\lim_{t\to\infty}\frac{\operatorname{Var}(N_a(t))}{\mathbb E N_a(t)}.
\]
All limits exist and are independent of initial state. The complete off-diagonal sign pattern is

| Count pair(s) | Sign of \(C_{ab}\) |
| --- | --- |
| \((\mathrm{in},\mathrm{ex})\) | positive |
| \((\mathrm{in},\mathrm{hop}),(\mathrm{ex},\mathrm{hop})\) | positive |
| \((\mathrm{ad},\mathrm{hop}),(\mathrm{de},\mathrm{hop})\) | negative |
| \((\mathrm{ad},\mathrm{de})\) | positive |
| \((\mathrm{ex},\mathrm{ad}),(\mathrm{in},\mathrm{de})\) | positive |
| \((\mathrm{in},\mathrm{ad}),(\mathrm{ex},\mathrm{de})\) | negative |

The three distinct Fano functions (each representing the indicated pair of count channels) are, with \(E=2w+1\), \(D=9w+7\), and \(G=3w^2+5w+3\),
\[
\begin{aligned}
F_{\mathrm{in}}=F_{\mathrm{ex}}&=\frac{3240w^6+14688w^5+27890w^4+28080w^3+15475w^2+4270w+429}{2E(6w+5)D^2G},\\
F_{\mathrm{ad}}=F_{\mathrm{de}}&=\frac{54w^4+179w^3+246w^2+161w+42}{2EDG},\\
F_{\mathrm{hop}}&=\frac{270w^3+687w^2+556w+143}{(6w+5)D^2}.
\end{aligned}
\]
The boundary Fano factor increases strictly from \(143/490\) toward \(5/9\); the Langmuir Fano factor decreases strictly from \(1\) toward \(1/2\); and the hopping Fano factor increases then decreases, having its **unique** maximizer at the positive root of
\[
567w^3+711w^2+24w-146=0,
\]
namely \(w_*=0.383801954828959\ldots\), with \(F_{\mathrm{hop}}(w_*)=0.592455854614905\ldots\). Endpoint values are limits as \(w\downarrow0\) or \(w\to\infty\), not members of the asserted strict-positive domain.

## Assumptions and scope

There are three exclusion sites, each having occupancy \(0\) or \(1\), and all events are independent memoryless exponential clocks with the following accepted rates: insertion at an empty first site at rate one; removal from an occupied third site at rate one; a successful rightward hop on either bond \(10\to01\) at rate one; adsorption at the vacant **middle** site at rate \(w\); and desorption from the occupied middle site at rate \(w\). Blocked proposed events are not counted. The units of time are fixed by the hop/boundary rate one. No Langmuir events occur on boundary sites. This is the three-site specialization of the standard open TASEP–Langmuir kinetic rules, with symmetric boundary and bulk rate choices. The five counts record actual accepted events, not net particle-number differences or mere clock attempts.

For any \(w>0\), the eight-state chain is irreducible. Statements are about stationary asymptotic count variances and covariances per physical time, not equal-time occupation covariances and not the finite-time counts at fixed \(t\).

## Proof

Use the ordered state index \(x=n_1+2n_2+4n_3\), where \(n_j\in\{0,1\}\). Let \(Q_{yx}\) be the column-convention Markov generator (each accepted transition of rate \(r\) contributes \(Q_{yx}\gets Q_{yx}+r\) and \(Q_{xx}\gets Q_{xx}-r\)). Let \(J_a\) be the off-diagonal rate matrix restricted to events of count type \(a\). Thus \(Q\) is the sum of all five off-diagonal event matrices minus their total outgoing diagonal rates. Set \(\mathbf 1\) to be the column vector of eight ones.

Solving \(Q\pi=0\) with \(\mathbf1^\top\pi=1\) gives the eight stationary probabilities in increasing index order:
\[
\pi=\frac{1}{2D}\begin{pmatrix}2w+1&4w+3&2(w+1)&4w+3&w+1&2(w+1)&w+1&2w+1\end{pmatrix}^{\!\top}.
\]
In particular, \(\pi\) is strictly positive, consistent with irreducibility. The five mean count rates \(m_a=\mathbf1^\top J_a\pi\) are
\[
m_{\mathrm{in}}=m_{\mathrm{ex}}=\frac{6w+5}{2D},\quad
m_{\mathrm{ad}}=m_{\mathrm{de}}=\frac w2,\quad
m_{\mathrm{hop}}=\frac{6w+5}{D}.
\]

To compute long-time second cumulants without treating unsuccessful attempts as events, tilt the generator by the five event-counting fields:
\[
Q(\mathbf s)=Q+\sum_{a}(e^{s_a}-1)J_a.
\]
Its simple Perron eigenvalue near \(\mathbf s=0\) is the scaled cumulant-generating function. If \(u_a\) is the uniquely normalized solution
\[
Qu_a=(m_a I-J_a)\pi,\qquad\mathbf1^\top u_a=0,
\]
first- and second-order eigenvalue perturbation gives
\[
C_{ab}=\mathbf1^\top(J_a u_b+J_bu_a)\quad(a\ne b),
\qquad C_{aa}=m_a+2\mathbf1^\top J_a u_a,
\qquad F_a=C_{aa}/m_a.
\]
The diagonal \(m_a\) term is the instantaneous jump shot noise, while distinct marks carry no simultaneous-event term.

Direct exact elimination gives the ten off-diagonal expressions below, grouped into six distinct rational functions:
\[
\begin{aligned}
C_{\mathrm{in},\mathrm{ex}}&=\frac{576w^5+2584w^4+4826w^3+4597w^2+2212w+429}{4ED^3G},\\
C_{\mathrm{in},\mathrm{hop}}=C_{\mathrm{ex},\mathrm{hop}}&=\frac{270w^3+687w^2+556w+143}{2D^3},\\
C_{\mathrm{ad},\mathrm{hop}}=C_{\mathrm{de},\mathrm{hop}}&=-\frac{3w}{2D^2},\\
C_{\mathrm{ad},\mathrm{de}}&=\frac{w^2(54w^3+139w^2+134w+47)}{4EDG},\\
C_{\mathrm{ex},\mathrm{ad}}=C_{\mathrm{in},\mathrm{de}}&=\frac{w(180w^4+626w^3+866w^2+555w+138)}{4ED^2G},\\
C_{\mathrm{in},\mathrm{ad}}=C_{\mathrm{ex},\mathrm{de}}&=-\frac{w(180w^4+662w^3+944w^2+621w+156)}{4ED^2G}.
\end{aligned}
\]
Every denominator is strictly positive for \(w>0\), and every explicitly displayed unsigned numerator polynomial has strictly positive coefficients. This proves all ten strict signs without sampling or extrapolation. The same exact correctors give the three rational Fano expressions in the finding.

For the Fano shape statements, the boundary Fano derivative has denominator
\(2E^2(6w+5)^2D^3G^2\) and numerator
\[
23328w^9+616896w^8+3392928w^7+9100080w^6+14537882w^5+14893224w^4+9958683w^3+4230419w^2+1040955w+113301,
\]
strictly positive for \(w>0\). The adsorption Fano derivative has denominator \(2E^2D^2G^2\) and is the **negative** of
\[
1080w^6+6048w^5+14338w^4+18502w^3+13763w^2+5628w+987
\]
divided by that denominator. Finally,
\[
F'_{\mathrm{hop}}(w)=-\frac{4(567w^3+711w^2+24w-146)}{(6w+5)^2D^3}.
\]
The cubic in parentheses is negative at zero, tends to positive infinity, and has strictly positive derivative \(1701w^2+1422w+24\) on the positive half-line. It consequently has exactly one positive zero, with the derivative changing from positive to negative there. This proves the unique strict hopping Fano maximum, with all endpoint limits by leading coefficients.

## Verification

The accompanying executable `verify_counts.py` constructs all eight states and their distinct marked transitions from the model rules; solves the stationary vector and all five centered Poisson equations symbolically; compares every listed mean, all ten cross-covariances, and all five Fano factors to the rational expressions; verifies positivity of coefficient certificates and the unique positive cubic root; and performs separate numerical checks of selected mixed second derivatives of the tilted Perron eigenvalue. Run from the directory containing this document using `python verify_counts.py`; SymPy is required and NumPy/SciPy are required for the optional eigenvalue comparison. The full exact symbolic component requires only SymPy. This is a finite-state exact symbolic proof certificate, not an inference from numerical tests.

## Relationship to prior work

Silva, Carvalho, Almeida and Duarte-Filho (2026, arXiv:2611.07053, first public 4 November 2026) study the same open-chain TASEP–Langmuir *class*, compute stationary profiles and equal-time site-occupation covariances, and develop a finite-size Fock-space framework; those established premises are not claimed as novel. Their read methods/results/conclusion concern \(\operatorname{Cov}(n_i,n_j)\), rather than long-time covariances of five **integrated event counts** or the contrasting Fano-rate responses under symmetric exchange. Parmeggiani, Franosch and Frey (2004) analyze TASEP–Langmuir stationary-density behavior and domain walls. Sato and Nishinari (2016) study periodic exclusion with Langmuir exchange and time-dependent occupation statistics, not this finite open-chain marked-count classification. Established open-TASEP counting-statistics work without Langmuir exchange likewise has no adsorption or desorption count channels.

Published work on time-ordered reaction–transport covariance in *circulation-balanced* exclusion networks with sitewise reservoirs is a relevant conceptual comparison, but its network-balance hypothesis does not hold for the boundary-driven rightward-only open chain here, and the measured quantities are not this full five-mark counting covariance matrix. All implication claims are limited to the inspected materials; publication priority is not certified.

## Limitations

The theorem is exact only for three sites, rate-one injection/extraction/hopping, a single middle Langmuir site, and equal positive bulk exchange rates \(w\). It asserts neither the same signs at arbitrary boundary rates, unequal bulk rates, nor at larger chain lengths. The covariance and Fano results are long-time rates, not finite-time identities. It does not provide experimental estimation bounds or a large-system phase diagram. A more general previously published counting-statistics formula, if found, might imply this specialization; an unindexed or inaccessible result remains a priority risk. Independent external validation has not been performed.

## References

1. L. D. S. Silva, A. M. S. Carvalho, F. A. G. Almeida and G. C. Duarte-Filho, *Langmuir kinetics and totally asymmetric volume exclusion in linear chains via Fock space formalism*, arXiv:2611.07053 (first public 4 November 2026), https://arxiv.org/abs/2611.07053.
2. A. Parmeggiani, T. Franosch and E. Frey, *The Totally Asymmetric Simple Exclusion Process with Langmuir Kinetics*, arXiv:cond-mat/0408034 (2004), https://arxiv.org/abs/cond-mat/0408034.
3. K. Sato and K. Nishinari, *Relaxation dynamics of the asymmetric simple exclusion process with Langmuir kinetics on a ring*, arXiv:1601.02651 (2016), https://arxiv.org/abs/1601.02651.
4. A. Lazarescu and K. Mallick, *An exact formula for the statistics of the current in the TASEP with open boundaries*, Journal of Physics A 44 (2011), https://doi.org/10.1088/1751-8113/44/31/315001.
5. *Exact time-ordered reaction–transport covariance on balanced exclusion networks*, publicly indexed research finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-time-ordered-reaction-transport-covariance-on-balanced-exc--5c264ddb40d9.
