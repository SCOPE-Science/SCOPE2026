# Exact two-sided bootstrap certification of middle-action adoption

## Finding

For a finite network exchanging one of three ordered public actions, a robust middle-action seed has a **precisely computable** set of agents guaranteed to adopt that middle action permanently from **every admissible initial private-opinion profile**. Compute the two strict bootstrap closures obtained by testing exposure against the lower and upper action thresholds **separately**. The set of guaranteed permanent middle-action adopters is **exactly their intersection**. In contrast, a single cascade that requires an outsider to exceed both exposure thresholds at once can stop prematurely: a four-agent rational network has a robust two-agent seed, a stalled combined cascade, and guaranteed eventual middle-action consensus for all agents. Four is the minimum possible network size for this strict incompleteness when there are no self-loops.

## Assumptions and scope

Let \(V=\{1,\ldots,n\}\), \(n\ge2\). Fix \(-1\le a_1<a_2<a_3\le1\), a nonnegative row-stochastic matrix \(W\) with \(W_{ii}=0\), and inertias \(0<\alpha_i<1\). Each agent has \(-1<\theta_{i,1}<\theta_{i,2}<1\) satisfying \(a_1<\theta_{i,1}\le a_2<\theta_{i,2}\le a_3\). Its public action is the right-continuous, nondecreasing three-bin map

\[
q_i(x)=\begin{cases}
a_1,&x<\theta_{i,1},\\
a_2,&\theta_{i,1}\le x<\theta_{i,2},\\
a_3,&x\ge\theta_{i,2}.
\end{cases}
\]

Private opinions \(x_i(t)\in[-1,1]\) obey the synchronous update

\[
x_i(t+1)=\alpha_i x_i(t)+(1-\alpha_i)\sum_{j\in V}W_{ij}q_j(x_j(t)).
\]

Choose a nonempty **robust seed** \(S\subseteq V\): agents in \(S\), once expressing \(a_2\), keep expressing \(a_2\) forever regardless of outsiders. This is ensured by the explicitly checkable condition below. Initial opinions of seed agents are arbitrary within their own middle bins; outsider initial opinions can be arbitrary in \([-1,1]\). Define \(w_i(C)=\sum_{j\in C}W_{ij}\), and

\[
\kappa_i^-={\theta_{i,1}-a_1\over a_2-a_1},\qquad
\kappa_i^+={a_3-\theta_{i,2}\over a_3-a_2}.
\]

Both parameters lie in \((0,1]\) and \([0,1)\), respectively; under the displayed assumptions actually \(\kappa_i^+\in[0,1)\). Seed robustness follows from \(w_i(S)\ge\max\{\kappa_i^-,\kappa_i^+\}\) for every \(i\in S\). For the upper-threshold boundary, equality preserves the middle bin from below; lower-bound equality preserves it from above.

Starting from \(C_0^-=C_0^+=S\), define simultaneous strict one-sided bootstrap updates

\[
C_{k+1}^{\pm}=C_k^{\pm}\cup
\{i\in V\setminus C_k^{\pm}:w_i(C_k^{\pm})>\kappa_i^{\pm}\}.
\]

Each closure stabilizes after at most \(n-|S|\) rounds. Call its terminal set \(C^-\), respectively \(C^+\). An agent is *guaranteed* when, for every allowed initial opinion profile with seed action \(a_2\), there exists a finite time after which that agent always expresses \(a_2\).

**Theorem.** The guaranteed set is exactly \(G=C^-\cap C^+\). Moreover there is a common finite time after which all members of \(G\) express \(a_2\), uniformly over the allowed initial opinions. The one-threshold-at-a-time closures are necessary and sufficient; the combined closure using \(\max\{\kappa_i^-,\kappa_i^+\}\) is in general only sufficient.

## Proof

**Step 1: robust seed and comparison.** If all seed agents express \(a_2\), their social input lies between \(a_1+(a_2-a_1)w_i(S)\) and \(a_3-(a_3-a_2)w_i(S)\). The displayed robust-seed inequality places this interval inside \([\theta_{i,1},\theta_{i,2}]\). At the right boundary \(\theta_{i,2}\), the strict inequality \(x_i(t)<\theta_{i,2}\) and \(0<\alpha_i<1\) imply \(x_i(t+1)<\theta_{i,2}\); the left endpoint remains allowed. Induction fixes all seed public actions permanently. Consequently the outsider evolution is an autonomous coordinatewise nondecreasing map \(F\), because all quantizers are nondecreasing and all weights are nonnegative.

**Step 2: extremal trajectories.** Fix any permitted seed initial opinions. Run the outsider subsystem once from all outsiders equal to \(-1\), and once from all outsiders equal to \(+1\). In the lower run, monotonicity and \(F(-\mathbf 1)\ge-\mathbf1\) make every outsider opinion nondecreasing. Since the seed action is \(a_2\), the interval \([-1,a_2]\) is invariant for each outsider; no outsider ever emits \(a_3\). In the upper run, all outsider opinions are nonincreasing, remain in \([a_2,1]\), and never emit \(a_1\). Every admissible outsider trajectory is coordinatewise between these two extremal trajectories at all times.

**Step 3: lower closure is exact.** In the lower run, once each agent of \(C_k^-\) emits \(a_2\), an outsider \(i\) with \(w_i(C_k^-)>\kappa_i^-\) receives social input at least

\[
a_1+(a_2-a_1)w_i(C_k^-)>\theta_{i,1}.
\]

Even if its opinion begins below \(\theta_{i,1}\), repeated convex relaxation toward an input bounded strictly above that threshold makes it cross the threshold in finite time; because the lower-run opinions are nondecreasing, it then emits \(a_2\) permanently. Inductively every member of \(C^-\) eventually does so. Conversely take \(B=V\setminus C^-\). For every \(i\in B\), the terminated closure satisfies \(w_i(C^-)\le\kappa_i^-\). If all agents in \(B\) emit \(a_1\), the input to such an agent is at most

\[
a_1+(a_2-a_1)w_i(C^-)\le\theta_{i,1}.
\]

Starting from \(-1<\theta_{i,1}\), convex relaxation keeps its opinion strictly below \(\theta_{i,1}\) for every finite time, so all members of \(B\) keep emitting \(a_1\). The eventual lower-run middle-action set is exactly \(C^-\).

**Step 4: upper closure is exact.** In the upper run, agents of \(C_k^+\) emitting \(a_2\) provide input at most

\[
a_3-(a_3-a_2)w_i(C_k^+)<\theta_{i,2}
\]

for every newly eligible \(i\), forcing a finite-time crossing downward and permanent emission of \(a_2\). For \(i\notin C^+\), terminality gives \(w_i(C^+)\le\kappa_i^+\), hence input at least \(\theta_{i,2}\) whenever all such outsiders emit \(a_3\). Starting at \(+1\), those agents stay at or above \(\theta_{i,2}\), and so keep emitting \(a_3\). The eventual upper-run middle-action set is exactly \(C^+\).

**Step 5: if and only if and uniform time.** Every admissible trajectory is sandwiched by the extremal ones. When both extremal actions equal \(a_2\), the middle action of the sandwiched trajectory must equal \(a_2\). Each extremal closure completes in finitely many threshold-crossing times, so their maximum gives one uniform time for all initial outsider opinions and for all permitted seed opinions (seed actions do not depend on seed private opinions). If \(i\notin C^-\), the lower extremal trajectory furnishes an initial condition with permanent action \(a_1\); if \(i\notin C^+\), the upper extremal trajectory furnishes one with permanent action \(a_3\). Hence no agent outside \(C^-\cap C^+\) is guaranteed.

**Step 6: sharp four-agent witness.** Set \((a_1,a_2,a_3)=(-1,0,1)\), \(S=\{1,2\}\),

\[
W=\begin{pmatrix}
0&4/5&1/5&0\\
4/5&0&0&1/5\\
1/2&0&0&1/2\\
0&1/2&1/2&0
\end{pmatrix},
\]

and threshold pairs, ordered by agent,

\[
(\theta_{i,1},\theta_{i,2})\in
\{(-2/5,2/5),(-2/5,2/5),(-3/4,1/4),(-1/4,3/4)\}.
\]

The lower and upper threshold vectors respectively are \((3/5,3/5,1/4,3/4)\) and \((3/5,3/5,3/4,1/4)\). Each seed agent places weight \(4/5\) on the other seed, exceeding both \(3/5\) thresholds, so \(S\) is robust. Both outsiders have initial seed exposure \(1/2\). The combined closure cannot add either outsider because its threshold is \(3/4\). The lower closure adds agent 3, then agent 4; the upper closure adds agent 4, then agent 3. Thus \(C^-=C^+=V\), and **every admissible initial profile reaches middle-action consensus**, whereas the combined cascade returns only \(S\).

For minimality, positive \(\kappa_i^-\) and \(W_{ii}=0\) imply a nonempty robust seed must have at least two agents. On at most three agents there is at most one outsider. If its seed exposure exceeds both one-sided thresholds it also enters the combined cascade. Otherwise the outsider is not guaranteed by the already proved exact characterization. Hence four agents are necessary and the witness proves sharpness.

## Verification

Run `python3 verify.py` in a directory containing this file and the standalone checker. The checker verifies every matrix row, the robustness inequalities, the exact rational closure sequences, threshold equality noncrossing, and \(4900\) exact-rational trajectories under four choices of inertia and varied initial opinions. The infinite-time, all-network theorem is proved above; this finite checker only independently checks the explicit witness and boundary behaviors, not the universal quantifiers.

## Relationship to prior work

Munif and collaborators (July 2026) establish strategically motivated quantized public communication embedded in discrete network opinion updates. The present theorem concerns a **mathematical three-bin extension**, not a claim that its arbitrary heterogeneous thresholds are all strategic equilibria. A later preprint by Munif and collaborators (November 16, 2026) defines robust action clusters and proves a *sufficient* combined-threshold cascade. Its multi-action setting does **not** supply the present necessity-and-sufficiency result; it explicitly distinguishes the exact two-action case from sufficient-only general-action cascades. The exact two-sided decomposition and four-agent counterexample fill that precise gap. Classical binary linear-threshold contagion and continuous-time quantized-consensus models use different adoption dynamics and neither establishes this intersection characterization for permanent middle-action guarantees. Prior claims were compared at the level of implications rather than matching titles.

## Limitations

The guarantee is conditional on a pre-existing robust seed and on monotone right-continuous three-bin quantizers, nonnegative static row-stochastic weights, no self-loops, and positive but subunit inertia. It does not classify transient oscillations or convergence of agents outside the guaranteed set, nor does it show arbitrary threshold sets are Nash/cheap-talk equilibria. The four-agent result concerns the smallest **gap between exact guaranteed adoption and the combined sufficient cascade**; it is not the smallest network admitting middle-action consensus. The foundational July manuscript's full text could not be independently examined during this review; its public abstract and model description were checked, and the closely related November manuscript's relevant full text was read. These leave some residual historical-priority uncertainty. No independent scientific validation is claimed.

## References

- H. Munif, A. Couthures, V. S. Varma, S. Lasaulce and T. Başar, *Network-Induced Strategic Communication in Opinion Dynamics*, arXiv:2607.16036v1, first public July 17, 2026. https://arxiv.org/abs/2607.16036
- H. Munif, A. Couthures, V. S. Varma, S. Lasaulce and I.-C. Morărescu, *Robust Action Clusters and Cascades in Opinion Dynamics with Heterogeneous Action Thresholds*, arXiv:2611.21446v1, first public November 16, 2026. This later preprint is cited for scientific comparison; the older model foundation is dated July 17, 2026. https://arxiv.org/abs/2611.21446
- L. Arditti et al., *Robust Coordination of Linear Threshold Dynamics on Directed Weighted Networks*, arXiv:2109.12685. https://arxiv.org/abs/2109.12685
- F. Ceragioli and P. Frasca, *Consensus and Disagreement: The Role of Quantized Behaviors in Opinion Dynamics*, SIAM J. Control Optim., DOI:10.1137/16M1083402.
