# Unimodality and weakest-signal selection in common-signal proxy voting

## Finding

In a finite common-signal voting environment with one expert and an even number of conditionally identical nonexperts, the ex-ante probability of a correct strict-majority decision is **unimodal in the number of nonexperts delegating to the expert**, as long as every nonexpert's competence in every signal state exceeds one half. This holds even when an expert's advantage reverses between signal states. Consequently, the optimal number of delegated votes can be found by a single scan of an exact pivotality formula; a local maximum is global.

More unexpectedly, if the signal states are finite and have distinct nonexpert competencies, then as the electorate grows the maximizing delegation count eventually depends **only on the least competent signal state with positive prior**, regardless of how rare that state is. In the nondegenerate case this number is the single-state log-odds delegation count of that state, even when other states dominate the ex-ante probability.

The competence condition is substantive: a rational five-voter, two-state example violating it has a strict local *minimum* at one delegation, so unimodality can fail.

## Assumptions and scope

Fix an integer \(h\ge1\) and a finite nonempty state set \(\mathcal S\). A committee has \(2h+1\) odd-numbered votes: one expert and \(2h\) statistically identical nonexperts. Signal state \(s\in\mathcal S\) occurs before voting with fixed prior \(\pi_s>0\), \(\sum_s\pi_s=1\). Delegation decisions are made before seeing the signal. Conditional on state \(s\), the expert casts the correct binary vote with probability \(r_s\in(0,1)\), and every nonexpert does so with probability \(q_s\in(1/2,1)\). The original (nondelegated) votes are independent conditional on \(s\). Votes are aggregated by strict simple majority and the expert casts all delegated voting weights as one block.

For each integer \(t\in\{0,\ldots,2h\}\), let \(P_h(t)\) denote ex-ante majority correctness when exactly \(t\) nonexperts delegate to the expert, the other nonexperts vote directly, and each person has unit weight before delegation. Identity of the \(t\) nonexperts does not matter because their conditional law is homogeneous. Let \(T_{m,q}(k)=\Pr\{\operatorname{Bin}(m,q)\ge k\}\) with probability \(1\) for \(k\le0\) and \(0\) for \(k>m\).

For \(0\le t\le h\):
\[
 P_h(t)=\sum_{s\in\mathcal S}\pi_s\bigl[r_sT_{2h-t,q_s}(h-t)+(1-r_s)T_{2h-t,q_s}(h+1)\bigr].
\]
For \(h\le t\le2h\), the expert has a strict majority of the original voting weights, so \(P_h(t)=\sum_s\pi_sr_s\) is constant.

Define \(\Delta_h(t)=P_h(t+1)-P_h(t)\). Then for \(0\le t<h\) the exact increment is
\[
\boxed{\Delta_h(t)=\binom{2h-t-1}{h}\sum_s\pi_s[q_s(1-q_s)]^{h-t-1}\bigl[r_s(1-q_s)^{t+2}-(1-r_s)q_s^{t+2}\bigr].}
\]

**Finite-state unimodality.** For every \(h\ge1\), the sequence \(P_h(0),\ldots,P_h(2h)\) is nondecreasing up to a maximum and nonincreasing thereafter. Among \(0,\ldots,h\), there can be at most one zero increment, followed by strictly negative increments. The constant suffix after \(h\) is forced by majority dictatorship; if this suffix begins after a positive increment it is also optimal. No monotonicity assumption on expert competence across signal states is needed.

**Rare-state selection.** Assume further that some unique \(s_\star\) minimizes \(q_s\), and set
\[
\alpha_\star=\frac{\log(r_{s_\star}/(1-r_{s_\star}))}{\log(q_{s_\star}/(1-q_{s_\star}))}.
\]
If \(\alpha_\star\notin\mathbb Z\), then for all sufficiently large \(h\) the unique maximizing delegation count is
\[
\boxed{t_\star=\max\{0,\lfloor\alpha_\star-1\rfloor\}.}
\]
This conclusion is insensitive to \(\pi_{s_\star}\), provided it is fixed and positive as \(h\) grows. The threshold population size may depend strongly on this prior. Integer log-odds ratios can produce an adjacent pair of optimal counts; their eventual tie-breaking may depend on the other states and is not asserted here.

For example, take \(\pi_0=1/1000\), \(q_0=11/20\), \(r_0=9/10\), and \(\pi_1=999/1000\), \(q_1=4/5\), \(r_1=9/10\). For all sufficiently large \(h\), the unique optimum is \(t=9\), although the rarer state occurs only one time in a thousand. Exact computations verify \(t=9\) at \(h=100,150,200\).

If the condition \(q_s>1/2\) is dropped, unimodality can fail even when the expert is individually more competent than the nonexperts in both states. At \(h=2\), let
\[
(\pi_0,q_0,r_0)=(1/5,1/20,1/4),\qquad
(\pi_1,q_1,r_1)=(4/5,9/10,19/20).
\]
Then \(P_2(0)=6366953/8000000\), \(P_2(1)=15911/20000\), and \(P_2(2)=81/100\), so \(P_2(0)>P_2(1)<P_2(2)\).

## Proof

**Increment identity.** Consider a fixed state \(s\) and a transition from \(t\) to \(t+1\) delegated nonexperts. Write \(B\sim\operatorname{Bin}(2h-t-1,q_s)\) for the votes from the remaining direct voters, and let \(X\sim\operatorname{Ber}(q_s)\) be the vote of the additional potential delegator, independent of \(B\) and the expert. If the expert is correct, the change in success probability is
\[
 \Pr(B\ge h-t-1)-\Pr(B+X\ge h-t)=(1-q_s)\Pr(B=h-t-1).
\]
If the expert is wrong, the change is
\[
 \Pr(B\ge h+1)-\Pr(B+X\ge h+1)=-q_s\Pr(B=h).
\]
Since \(\binom{2h-t-1}{h-t-1}=\binom{2h-t-1}{h}\), substitution of the binomial point masses, averaging by \(r_s\) and \(\pi_s\), and factoring out the binomial coefficient yields the boxed expression. This is an identity for all declared indices, not an approximation.

**Single crossing.** For \(0\le t<h\) define the nonnegative quantities
\[
 A_t=\sum_s\pi_sr_sq_s^{h-t-1}(1-q_s)^{h+1},\qquad
 B_t=\sum_s\pi_s(1-r_s)q_s^{h+1}(1-q_s)^{h-t-1}.
\]
The increment has the sign of \(A_t-B_t\). For \(t+1<h\), the assumption \(q_s>1/2\) gives \(A_{t+1}<2A_t\) because each summand is multiplied by \(1/q_s<2\), and \(B_{t+1}>2B_t\) because each summand is multiplied by \(1/(1-q_s)>2\). All terms are strictly positive. Thus \(A_t\le B_t\) implies \(A_{t+1}<B_{t+1}\). There cannot be a change from a negative increment to a later positive increment, or two zero increments. This proves the asserted unimodality for the nonconstant prefix. For \(t\ge h\), the expert already holds at least \(h+1\) votes, which proves the final constant suffix.

**Selection by the weakest state.** Write the state summand of the boxed increment, omitting its common positive binomial coefficient, as
\[
 [q_s(1-q_s)]^{h-t-1}G_s(t),\quad
 G_s(t)=r_s(1-q_s)^{t+2}-(1-r_s)q_s^{t+2}.
\]
For each fixed integer \(t\), \(q_s(1-q_s)\) is strictly decreasing over \(q_s\in(1/2,1)\). Unique minimality of \(q_{s_\star}\) therefore implies that, as \(h\to\infty\), the sign of \(\Delta_h(t)\) eventually equals the sign of \(G_{s_\star}(t)\), provided the latter is nonzero. The noninteger condition on \(\alpha_\star\) ensures this nonvanishing for all integers \(t\ge0\).

The use of fixed \(t\) is justified uniformly as follows. As \(q_s/(1-q_s)>1\) and \(r_s<1\), there exists a finite integer \(T\) such that \(G_s(T)<0\) for **every** state. For every \(h>T\), the increment at \(T\) is negative, and the single-crossing theorem forces all later increments (up to \(h-1\)) to be negative. Hence all maximizing counts are in the finite set \(\{0,\ldots,T\}\). On this finite set, eventual signs coincide with the least-competent state's signs. Its sign is positive exactly when
\[
 t+2<\alpha_\star.
\]
Because these signs cross once and no tie occurs, the optimum is \(\max\{0,\lfloor\alpha_\star-1\rfloor\}\) for all sufficiently large \(h\). Notice that the factor \(\pi_{s_\star}>0\) only modifies the finite crossover population, not the limiting optimizer.

**Sharpness example.** Substitution of the displayed rational parameters into the binomial-tail formula gives the three exact fractions above; their inequalities are strict, so the claimed failure of unimodality follows without numerical approximation.

## Verification

Run `python3 verify.py` with Python 3 and only the standard library. The script checks the exact incremental identity against independently summed binomial tails in 5,760 state/parameter/increment cases; checks unimodality in 1,280 randomly seeded but exactly rational finite-state instances; checks the rational non-unimodal boundary example; tests the eventual rare-state optimizer at three electorate sizes with exact rational signs; and compares the single-state cutoff against direct exact signs. This finite verification supports, but does not replace, the infinite proofs above. Inputs and outputs are deterministic.

## Relationship to prior work

Gilbert et al. (2026, arXiv:2608.16738; short peer-reviewed proceedings version DOI:10.4230/LIPIcs.DISC.2026.64) introduce the signal-conditioned liquid-democracy model and study safe delegation mechanisms, failures of average-competence reductions, and conditional concentration. The six-page proceedings text was examined in full. It does not state an optimizer for the number of proxies in a symmetric single-expert star, a finite-signal unimodality theorem, or rare-state asymptotic selection. The longer arXiv preprint could not be read and remains an explicit overlap risk.

Dhillon et al. (arXiv:2306.03960; 2026 open-access article DOI:10.1111/iere.70126, Section 5.3.1) already characterize optimal proxy counts for a *single independent competence environment* using the ratio of log odds. The one-state specialization here is **not** claimed as new. The additional result is the nontrivial ex-ante mixture theorem: optimizing a mixture of majority probabilities is not in general the same as averaging or selecting their component-wise optimizers, and the common-signal model supplies a specific structure preserving unimodality while inducing least-state asymptotic selection. The earlier 2025 work by Chatterjee et al. concerns performance guarantees for network-based mechanisms in the scalar competence setting.

## Limitations

The theorem is limited to one expert, equally competent nonexperts within each signal state, conditionally independent votes, odd total voter counts, pre-signal delegation and simple majority. It does not analyze equilibria, endogenous choices by individual voters, heterogeneous nonexpert competencies, or arbitrary delegation graphs. Positive competence above one half in every state is essential to the general unimodality guarantee; if the probability distribution over signals changes with electorate size, the rare-state asymptotic law need not hold. The long version of the closest 2026 common-signal paper was not accessible for full-text overlap comparison, so independent originality verification remains necessary.

## References

1. S. Gilbert, S. Schmid, S. Schnell, J. Svoboda, and M. X. Yeo, *Liquid democracy under vote correlation: On the fallacies of averaging and the excluded middle*, arXiv:2608.16738, initially public 2026-08-17. https://arxiv.org/abs/2608.16738
2. The same authors, *Brief Announcement: Liquid Democracy Under Vote Correlation*, LIPIcs DISC 2026, Article 64, published 2026-11-02. https://doi.org/10.4230/LIPIcs.DISC.2026.64
3. A. Dhillon, G. Kotsialou, D. Ravindran, and D. Xefteris, *Information aggregation with delegation of votes*, arXiv:2306.03960, initially public 2023-06-06; journal version 2026. https://arxiv.org/abs/2306.03960 and https://onlinelibrary.wiley.com/doi/10.1111/iere.70126
4. K. Chatterjee, S. Gilbert, S. Schmid, J. Svoboda, and M. X. Yeo, *When is liquid democracy possible? On the manipulation of variance*, PODC 2025. https://doi.org/10.1145/3732772.3733544
