# A sharp parity law for oscillatory selection under increasing public-goods returns

## Finding

**Theorem (sharp parity-dependent selection reversals).** Let \(n\ge2\) and \(N\ge n+1\) be integers. For a finite well-mixed two-strategy public-goods game with unit contribution cost, positive **strictly increasing** multiplication factors
\[
0<r(1)<r(2)<\cdots<r(n)=\frac{n(N-1)}{N-n},
\]
let \(\Delta_i\) be the average payoff of a cooperator minus that of a defector when exactly \(i\) of the \(N\) individuals cooperate. Among the nonzero entries in \((\Delta_1,\ldots,\Delta_{N-1})\), the number of successive sign changes is at most
\[
\begin{cases}
n-1,&n\text{ even},\\
n-2,&n\text{ odd}.
\end{cases}
\]
For **every** \(n\), this bound is attained by a rational, strictly increasing, positive schedule already at \(N=n+1\). The total public-good benefit \(k r(k)/n\) is strictly increasing with the number \(k\) of contributors. Each attaining example has equal single-mutant cooperator and defector fixation probabilities at every positive Fermi selection intensity, giving exactly half cooperative and half defective homogeneous-state occupation in the rare-mutation limit.

Thus, even strict economies of scale and a terminal return that fixes the long-run comparison do not limit the local selection pattern to one crossover. The parity effect is an exact finite-population constraint, rather than a numerical observation.

## Assumptions and scope

There are \(N\) individuals, two strategies \(C,D\), and a random interaction group of size \(n\) containing the focal player and \(n-1\) uniformly sampled distinct co-players. If the interaction group has \(k\) cooperators, everyone receives benefit \(a_k=kr(k)/n\), with \(a_0=0\); cooperators additionally pay cost one. The payoffs \(P_C(i),P_D(i)\) are expected over hypergeometric co-player sampling at fixed total population count \(i\in\{1,\ldots,N-1\}\), and \(\Delta_i=P_C(i)-P_D(i)\). A sign change is counted between successive *nonzero* entries (zero entries are omitted). For the fixation corollary, individuals imitate by the usual pairwise Fermi probability \((1+\exp[-\beta(P_Y-P_X)])^{-1}\) at \(\beta>0\), with symmetric opportunity to compare opposite types; mutation is absent when computing fixation, followed by the rare symmetric-mutation limit.

The bound is uniform in all admissible strictly increasing positive \(r(k)\) with the displayed fixed terminal return. Sharpness requires existence at some admissible \(N\), not the assertion of sharpness for each larger fixed \(N\).

## Proof

**Step 1 (an exact sampling reduction).** Fix one focal cooperator and one focal defector in the same mixed population with \(i\) cooperators. Each focal player's set of other potential participants contains the opposite-type focal individual and the common \(N-2\) others. In the payoff *difference*, those cases where the opposite-type individual is selected cancel, because then both groups have \(J+1\) cooperators for a common sample of \(n-2\). With the remaining probability \(\alpha=(N-n)/(N-1)\), neither group includes the other focal individual. Their common \(n-1\) sampled co-players then contain
\[
J\sim\operatorname{Hypergeom}(N-2,i-1,n-1)
\]
cooperators. Hence, exactly,
\[
\Delta_i=-1+\alpha\sum_{j=0}^{n-1}
\frac{\binom{i-1}{j}\binom{N-i-1}{n-1-j}}{\binom{N-2}{n-1}}
(a_{j+1}-a_j).\tag{1}
\]
We use the convention \(\binom{u}{v}=0\) for integer \(u\ge0\) and \(v\notin\{0,\ldots,u\}\).

**Step 2 (degree and endpoint signs).** Each hypergeometric numerator in (1), viewed as a function of the real variable \(i\) through falling-factorial polynomials, has degree at most \(n-1\). Therefore \(i\mapsto\Delta_i\) is the restriction of a real polynomial of degree at most \(n-1\). Moreover, when \(i=1\), the sample has \(J=0\), and when \(i=N-1\), it has \(J=n-1\). As \(r(n)=n/\alpha\) and the schedule is strictly increasing,
\[
\Delta_1=-1+\frac{\alpha r(1)}n<0,
\quad
\Delta_{N-1}=-1+\frac\alpha n\bigl[nr(n)-(n-1)r(n-1)\bigr]>0.\tag{2}
\]
Every strict sign change between evaluated states forces a distinct real zero in the intervening open interval, so there can be at most \(n-1\). Since the first and last entries have opposite signs, the number of changes (after omitting zeros) is odd. If \(n\) is odd, \(n-1\) is even and the largest permitted odd number is \(n-2\). This proves both upper bounds.

**Step 3 (attaining schedules).** For any \(n\ge2\), take \(N=n+1\), \(\varepsilon=1/4\), and define rational numbers
\[
\begin{aligned}
d_1&=-\varepsilon,\\
d_k&=\varepsilon(-1)^k2^{-k},&&2\le k\le n-1,\\
d_n&=-\sum_{k=1}^{n-1}d_k,\\
S_k&=\sum_{j=1}^kd_j,\qquad
r(k)=n^2\left(1+\frac{S_k}{k}\right),&&1\le k\le n.
\end{aligned}\tag{3}
\]
The middle range is empty at \(n=2\). For every \(k<n\),
\[
-\varepsilon\le S_k\le-\varepsilon/2<0,
\]
so every multiplier is positive and \(d_n=-S_{n-1}>0\). Also \(S_n=0\), giving \(r(n)=n^2=n(N-1)/(N-n)\). To prove strict increase, calculate for \(2\le k\le n\),
\[
\frac{r(k)-r(k-1)}{n^2}=\frac{d_k-S_{k-1}/(k-1)}{k}.\tag{4}
\]
For every even \(k<n\), \(d_k>0>S_{k-1}\), so (4) is positive. For every odd \(3\le k<n\),
\[
d_k=-\frac\varepsilon{2^k}>-\frac\varepsilon{2(k-1)}\ge\frac{S_{k-1}}{k-1},
\]
using \(2^k>2(k-1)\). At \(k=n\), \(d_n>0>S_{n-1}\) again. Thus \(0<r(1)<\cdots<r(n)\).

From (3), \(a_k=kr(k)/n=n(k+S_k)\), so \(a_k-a_{k-1}=n(1+d_k)>0\) for all \(k\). As \(N=n+1\), the common sample in (1) is all \(n-1\) other individuals, giving \(J=i-1\) deterministically and \(\alpha=1/n\). Consequently
\[
\boxed{\Delta_i=-1+\frac{a_i-a_{i-1}}n=d_i\qquad(1\le i\le n).}\tag{5}
\]
The signs \(d_1,\ldots,d_{n-1}\) strictly alternate starting negative, while \(d_n>0\). They therefore change \(n-1\) times for even \(n\), and \(n-2\) times for odd \(n\), attaining both upper bounds.

For an explicit six-player-group example, \(n=6,N=7\) gives
\[
(r(1),\ldots,r(6))=\left(27,\frac{261}{8},\frac{267}{8},\frac{2187}{64},\frac{5517}{160},36\right)
\]
and
\[
(\Delta_1,\ldots,\Delta_6)
=\left(-\frac14,\frac1{16},-\frac1{32},\frac1{64},-\frac1{128},\frac{27}{128}\right).
\]
All five successive signs change.

**Step 4 (the exact neutral fixation comparison).** Under symmetric pairwise Fermi comparisons the birth–death transition ratio is \(T_i^+/T_i^-=\exp(\beta\Delta_i)\). The standard absorbing birth–death recurrence yields
\[
\frac{\rho_C}{\rho_D}
=\prod_{i=1}^{N-1}\frac{T_i^+}{T_i^-}
=\exp\left(\beta\sum_{i=1}^{N-1}\Delta_i\right).
\]
For the schedules (3), the sum is \(S_n=0\). Thus \(\rho_C=\rho_D\) for every \(\beta>0\) and the rare symmetric-mutation two-state embedded chain gives cooperative stationary fraction \(\rho_C/(\rho_C+\rho_D)=1/2\). This fixation identity is standard; the new assertion is its coexistence with sharp alternating selection under increasing returns.

## Verification

The attached `checker.py` is standard-library-only and uses exact fractions and independently constructed focal-hypergeometric payoffs. Running `python checker.py` passed for all \(2\le n\le20\) and checked the exact prescribed sign-reversal count, strict multiplier increase, strict total-benefit increase, terminal criticality, and equality between the direct and reduced payoff formulas. It also verified vanishing degree-\(n\) forward differences for independent schedules with \(2\le n\le8\). The proof, not the finite checker range, establishes the statements for every integer \(n\ge2\) and \(N\ge n+1\).

## Relationship to prior work

Wang, Liu, Chen and Szolnoki (2026) derive the finite-population hypergeometric return model and show that the *aggregate* payoff advantage under weak selection depends only on the fully cooperative return. The present classification instead asks how often the individual mixed-state payoff advantage can reverse while that same terminal return and strictly increasing multiplier are fixed. Their displayed theorem does not provide this parity-sharp attainable classification.

Hauert and McAvoy (2024) analyze nonlinear public-goods returns, particularly linear frequency dependence, including economies of scale. Their marginal-benefit equation explains why nonlinear schedules matter, but the linearly dependent multiplier subclass does not entail arbitrarily many reversals. Wu, Traulsen and Gokhale (2013) explicitly note that \(n\)-player hypergeometric payoffs have degree at most \(n-1\); the general polynomial upper bound is therefore **not** claimed as new. The additional claim is the sharp parity improvement for odd \(n\) and simultaneous realization under strictly increasing positive returns and terminal neutrality for all group sizes.

## Limitations

This is a well-mixed finite-population theorem with an arbitrary (though strictly increasing) discrete return schedule; it does not say typical empirically measured return schedules attain the maximum. The sharp construction uses groups of size \(N-1\), and is not asserted sharp for every fixed larger population. The result describes **signs of instantaneous expected payoff differences**, not recurrent oscillations of an individual stochastic trajectory. Equal homogeneous-state occupation is a rare-symmetric-mutation statement and does not imply neutral fixation from each intermediate state, equal fixation times, or a half-cooperator population at ordinary nonzero mutation. Historical priority is based on searched accessible literature, not an exhaustive proof of uniqueness; no independent validation is claimed.

## References

- Qiushuang Wang, Yuyuan Liu, Xiaojie Chen, and Attila Szolnoki, *Evolutionary dynamics in public goods games with general frequency-dependent returns* (first posted 2026-07-18), https://arxiv.org/abs/2607.16809, especially Section 2 and Proposition 2.1.
- Christoph Hauert and Alex McAvoy, *Frequency-dependent returns in nonlinear public goods games*, *Journal of the Royal Society Interface* **21** (2024), 20240334, https://doi.org/10.1098/rsif.2024.0334 and https://pmc.ncbi.nlm.nih.gov/articles/PMC11521596/.
- Bin Wu, Arne Traulsen, and Chaitanya S. Gokhale, *Dynamic Properties of Evolutionary Multi-player Games in Finite Populations*, *Games* **4** (2013), 182–199, https://doi.org/10.3390/g4020182.
