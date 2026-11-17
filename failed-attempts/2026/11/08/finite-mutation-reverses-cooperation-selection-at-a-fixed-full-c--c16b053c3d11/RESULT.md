# Finite mutation reverses cooperation selection at a fixed full-cooperation return

## Finding

Consider a well-mixed population of four individuals playing three-person public-goods games, with cooperation cost one. If a game group contains exactly \(j\) cooperators, its total contributions are multiplied by \(r_j\) and shared equally. Set \(r_1=1\), \(r_3=9\), and \(1\le r_2\le9\). Under independent, symmetric strategy-flip mutation with probability \(0<\mu<1\), and pairwise Fermi imitation of selection strength \(\delta\ge0\), let \(F(\delta)\) be the unique stationary expected fraction of cooperators.

With the explicit update convention in the next section, \(F\) is analytic near \(\delta=0\) and

\[
\boxed{F'(0)=\frac{2\mu(1-\mu)(r_2-5)}{3(3+13\mu)(1+15\mu)}.}
\]

Hence, at **every fixed positive nonunit mutation probability**, two nondecreasing return profiles with the same full-cooperation return \(r_3=9\), namely \((r_1,r_2,r_3)=(1,1,9)\) and \((1,8,9)\), favor opposite strategies for all sufficiently small positive selection intensities. The transition is exactly \(r_2=5\) at first order. At \(r_2=5\), the stationary fraction is **exactly \(1/2\) for every finite selection strength**, not merely to first order.

This difference is also demonstrable without any weak-selection approximation: at \(\mu=1/2\) and \(\delta=9\log 2\), respectively,

\[
\boxed{F_{r_2=1}=\frac{599130841}{1318051952}<\frac12
<\frac{141053}{264124}=F_{r_2=8}.}
\]

By contrast, for each fixed finite selection strength the rare-mutation limit \(\lim_{\mu\downarrow0}F(\delta)=1/2\) holds for all these return profiles. Thus positive mutation reveals a selection difference that the boundary-return criterion cannot detect in its rare-mutation regime.

## Assumptions and scope

There are exactly four players and two strategies, \(C\) (cooperate) and \(D\) (defect). To calculate a player's expected payoff, uniformly draw two distinct *other* players, without replacement, to form a three-person group with that focal player. In a group with \(j\) cooperators, a defector gets \(jr_j/3\), and a cooperator gets \(jr_j/3-1\). A defector-only group has zero benefit. All payoffs for strategy comparison are expectations conditional on the current population composition.

At every update choose a focal player uniformly. Independently, with probability \(\mu\) flip its strategy. With probability \(1-\mu\), choose a role model independently and uniformly from all four players (including the focal player). If their strategies differ, adopt the role model's strategy with probability \(L(\delta(P_{\mathrm{model}}-P_{\mathrm{focal}}))\), where \(L(z)=1/(1+e^{-z})\). Self-comparisons cause no state change. This last, with-replacement role-model convention is part of the theorem; other sampling conventions change the quantitative coefficient.

Let \(i\in\{0,1,2,3,4\}\) be the number of cooperators. For \(0<\mu<1\), the resulting birth–death Markov chain on these five states is irreducible and has a unique stationary distribution \(\pi_i(\delta)\). Its average fraction is \(F(\delta)=\frac14\sum_{i=0}^4 i\pi_i(\delta)\). The main differential formula concerns \(r_1=1\), \(r_3=9\), and \(1\le r_2\le9\), with no large-population approximation.

## Proof

**Step 1: conditional payoffs.** Direct hypergeometric group sampling yields the payoff differences \(\Delta_i=P_C(i)-P_D(i)\), for states \(i=1,2,3\),

\[
\Delta_1=\frac{r_1-9}{9},\qquad
\Delta_2=\frac{-r_1+2r_2-9}{9},\qquad
\Delta_3=\frac{-2r_2+3r_3-9}{9}.
\]

With \(r_1=1\), \(r_3=9\), these are \((-8/9,(2r_2-10)/9,(18-2r_2)/9)\). Their sum is zero for *all* \(r_2\), explaining why a rare-mutation comparison loses the intermediate return.

**Step 2: the finite-mutation chain.** Write \(q_i=i(4-i)/16\), and \(\ell_i=L(\delta\Delta_i)\). For \(i=1,2,3\) the one-step increasing and decreasing probabilities are exactly

\[
T_i^+=\mu\frac{4-i}{4}+(1-\mu)q_i\ell_i,\qquad
T_i^-=\mu\frac{i}{4}+(1-\mu)q_i(1-\ell_i).
\]

At the endpoints \(T_0^+=\mu\), \(T_4^-=\mu\), and the outward moves are absent. Every neighboring transition is strictly positive. The unique stationary weights satisfy detailed balance: choose \(w_0=1\), then

\[
w_i=\prod_{k=1}^{i}\frac{T_{k-1}^+}{T_k^-},\qquad
\pi_i=\frac{w_i}{\sum_{j=0}^4w_j}.
\]

**Step 3: differentiation at neutrality.** At \(\delta=0\), \(\ell_i=1/2\). Set \(a=3+5\mu\), \(b=3+21\mu\), \(c=1+3\mu\). The neutral weights reduce exactly to

\[
(w_0,w_1,w_2,w_3,w_4)=
\left(1,\frac{32\mu}{a},\frac{8\mu b}{ac},\frac{32\mu}{a},1\right).
\]

Their normalized mean count is two. For \(L_i=\left.\partial_\delta\log w_i\right|_{\delta=0}\), differentiating the products in Step 2 and using \(\ell'_i(0)=\Delta_i/4\) gives \(L_0=0\) and

\[
\begin{aligned}
L_1&=\frac{3(1-\mu)}{2a}\Delta_1,\\
L_2-L_1&=\frac{3(1-\mu)}{2b}\Delta_1+\frac{1-\mu}{2c}\Delta_2,\\
L_3-L_2&=\frac{1-\mu}{2c}\Delta_2+\frac{3(1-\mu)}{2b}\Delta_3,\\
L_4-L_3&=\frac{3(1-\mu)}{2a}\Delta_3.
\end{aligned}
\]

Differentiating \(F=\sum_i iw_i/(4\sum_iw_i)\) gives the weighted covariance

\[
F'(0)=\frac{1}{4\sum_iw_i}\sum_{i=0}^4(i-2)w_iL_i.
\]

Substitution of the displayed neutral weights and the three payoffs, followed by cancellation, gives precisely

\[
F'(0)=\frac{2\mu(1-\mu)(r_2-5)}{3(3+13\mu)(1+15\mu)}.
\]

The denominator is positive for \(0<\mu<1\). Thus \(r_2<5\) implies \(F(\delta)<1/2\) for all sufficiently small \(\delta>0\), while \(r_2>5\) implies \(F(\delta)>1/2\). Each assertion follows from analyticity and the nonzero derivative for that fixed \(\mu\); no uniform-in-\(\mu\) interval is claimed.

**Step 4: exact neutral middle case at all selection strengths.** When \(r_2=5\), the three payoff differences are \((-8/9,0,8/9)\), so \(\Delta_{4-i}=-\Delta_i\). The symmetric mutation terms and \(L(-z)=1-L(z)\) imply \(T_i^+=T_{4-i}^-\). Reflection of the unique stationary measure under \(i\mapsto4-i\) is therefore the same stationary measure, forcing \(F(\delta)=1/2\) for every \(\delta\ge0\).

**Step 5: exact finite-strength witnesses.** For \(\delta=9\log2\), each \(9\Delta_i\) is an integer in the profiles \((1,1,9)\) and \((1,8,9)\). Consequently \(L(\delta\Delta_i)=2^{9\Delta_i}/(1+2^{9\Delta_i})\) is rational. With \(\mu=1/2\), the five-state detailed-balance recurrence in Step 2 gives respectively \(599130841/1318051952\) and \(141053/264124\). Both comparisons against \(1/2\) are strict. These are exact fractions, not numerical estimates.

**Step 6: rare-mutation boundary.** At zero mutation the endpoint states are absorbing, so a stationary law is not unique; we take the limit from \(\mu>0\). Standard birth–death fixation identities give \(\rho_C/\rho_D=\prod_{i=1}^3T_i^+/T_i^-=\exp(\delta\sum_{i=1}^3\Delta_i)=1\) when mutation is absent. As \(\mu\downarrow0\) at fixed finite \(\delta\), the unique stationary law places asymptotically equal mass on the two endpoints, hence \(F\to1/2\). This establishes the stated contrast, not a claim of a unique zero-mutation invariant law.

## Verification

Run `python3 CHECK.py` using Python's standard library. It constructs hypergeometric expected payoffs and rational detailed-balance weights directly. It verifies the displayed payoff and first-derivative identities at 72 rational parameter combinations, as well as reflection neutrality, and independently computes both exact finite-strength fractions. The recorded execution reports `PASS: 72 exact payoff/derivative comparisons and exact finite-selection witnesses`. The derivation in Steps 1–6 is the proof of the parameter-wide conclusions; finitely many checks do not prove the infinite statements.

## Relationship to prior work

Wang, Liu, Chen and Szolnoki (2026), first publicly posted July 18, establish a boundary-return formula under rare mutation and weak selection for arbitrary composition-dependent public-goods returns. In particular, their Proposition 2.1 gives the sum of payoff differences, which equals zero in this construction; the present finite-mutation stationarity calculation concerns a different regime and specifies when the unobserved intermediate return becomes decisive.

Hauert and McAvoy (2024) present both Fermi imitation and mutation transitions for nonlinear public-goods games, but their explicitly analysed return factors are affine in the number of cooperators. At the endpoints \(r_1=1\), \(r_3=9\), their affine assumption fixes \(r_2=5\), exactly the neutral middle case; it cannot generate the two opposing intermediate profiles. Antal and collaborators' established mutation-selection abundance results for pairwise matrix games show why finite-mutation analysis is natural, but their pairwise-payoff specification does not imply this three-person nonlinear return threshold. McAvoy and Hauert (2015) provide a general multiplayer-game weak-selection structure-coefficient framework; it implies that first-order abundance is linear in the payoff entries but does not state the present game-specific finite-mutation coefficient, reflection threshold, or finite-strength fractions. Standard birth–death reversibility is used rather than claimed new.

## Limitations

The selection-sign theorem near \(\delta=0\) is for a fixed positive \(\mu<1\); at \(\mu\to0\) or \(\mu\to1\) the linear response vanishes. The two exact fractions hold at the specific stated positive selection intensity. The model assumes four individuals, three-person uniformly sampled interactions, symmetric payoff-independent strategy flips, independent with-replacement imitation models and expected-payoff Fermi decisions. Generality across arbitrary mutation kernels, population sizes, network structures, or all selection intensities is not asserted. This is a mathematical stationary-abundance result, not a claim about field behavior or an empirical prediction.

## References

1. Q. Wang, Y. Liu, X. Chen, and A. Szolnoki, *Evolutionary dynamics in public goods games with general frequency-dependent returns*, arXiv:2607.16809 (first version July 18, 2026), https://arxiv.org/abs/2607.16809.
2. C. Hauert and A. McAvoy, *Frequency-dependent returns in nonlinear public goods games*, Journal of the Royal Society Interface 21 (2024), 20240334, https://pmc.ncbi.nlm.nih.gov/articles/PMC11521596/.
3. T. Antal, M. A. Nowak, and A. Traulsen, *Strategy abundance in \(2\times2\) games for arbitrary mutation rates*, Journal of Theoretical Biology 257 (2009), 340–344, https://arxiv.org/abs/0809.2804.
4. T. Antal, A. Traulsen, H. Ohtsuki, C. E. Tarnita, and M. A. Nowak, *Mutation–selection equilibrium in games with multiple strategies*, Journal of Theoretical Biology 258 (2009), 614–622, https://arxiv.org/abs/0811.2009.
5. A. McAvoy and C. Hauert, *Structure coefficients and strategy selection in multiplayer games*, Journal of Mathematical Biology (2015), https://doi.org/10.1007/s00285-015-0882-3.
