# Unimodality and weakest-signal selection in common-signal proxy voting

## Finding

With one expert and an even number of conditionally identical nonexperts, the ex-ante probability of a correct strict-majority decision is unimodal in the number of nonexperts who delegate to the expert, provided the nonexpert competence exceeds one half in every signal state. The expert may be better than the nonexperts in some states and worse in others. The exact increments up to the point where the expert acquires a strict majority suffice to find a global maximizer.

If there is a unique state minimizing nonexpert competence, its prior is fixed and positive, and its expert-to-nonexpert log-odds ratio is not an integer, then the maximizing delegation count is eventually unique as the electorate grows. It equals the single-state log-odds count for that least-competent state, however small its fixed prior. Without the above-half competence condition, unimodality can fail even in a five-voter committee.

## Assumptions and scope

There are \(2h+1\) unit votes, with integer \(h\ge1\), one expert and \(2h\) nonexperts. A finite nonempty state set \(\mathcal S\) has fixed priors \(\pi_s>0\), \(\sum_s\pi_s=1\). Delegation is decided before the signal is seen. Conditional on state \(s\), the original votes are independent, and the expert and each nonexpert are correct with probabilities \(r_s\in(0,1)\) and \(q_s\in(1/2,1)\), respectively. The expert casts the expert's own vote and all delegated votes as one block. The voting rule is strict simple majority.

Let \(P_h(t)\) be the ex-ante correctness for \(t\in\{0,\dots,2h\}\) delegators. Their identities do not matter by conditional homogeneity. Write \(T_{m,q}(k)=\Pr\{\operatorname{Bin}(m,q)\ge k\}\), with the conventions \(T_{m,q}(k)=1\) for \(k\le0\) and \(T_{m,q}(k)=0\) for \(k>m\). For \(0\le t\le h\),
\[
P_h(t)=\sum_s\pi_s\big[r_s T_{2h-t,q_s}(h-t)+(1-r_s)T_{2h-t,q_s}(h+1)\big].
\]
For \(h\le t\le2h\), the expert has at least \(h+1\) votes and \(P_h(t)=\sum_s\pi_s r_s\) is constant. The nontrivial increments \(\Delta_h(t)=P_h(t+1)-P_h(t)\), for \(0\le t<h\), are
\[
\boxed{\Delta_h(t)=\binom{2h-t-1}{h}\sum_s\pi_s[q_s(1-q_s)]^{h-t-1}
\big[r_s(1-q_s)^{t+2}-(1-r_s)q_s^{t+2}\big].}
\]

**Finite-state unimodality.** The sequence is nondecreasing up to a maximum and nonincreasing thereafter. In the prefix of increments indexed by \(0\le t<h\), there is an initial block of positive increments, then at most one zero, then only negative increments; any of these blocks may be empty. One can choose a global maximizer by taking the first \(t<h\) with \(\Delta_h(t)\le0\), or \(h\) if there is no such \(t\). If the sequence reaches \(h\) without a negative increment, the constant suffix is optimal as well. A point of the constant suffix can otherwise be a nonglobal weak local maximum, so equality with adjacent values is not a sufficient optimality test.

**Least-state selection.** If a unique state \(s_*\) minimizes \(q_s\), set
\[
\alpha_* = \frac{\log(r_{s_*}/(1-r_{s_*}))}{\log(q_{s_*}/(1-q_{s_*}))}.
\]
If \(\alpha_*\notin\mathbb Z\), for all sufficiently large \(h\) the unique maximizing count is
\[
\boxed{t_* = \max\{0,\lfloor\alpha_*-1\rfloor\}.}
\]
The threshold for \(h\) may depend strongly on the prior \(\pi_{s_*}\). At integer ratios the leading least-state increment can vanish; a tie or its resolution by other states is not covered by the unique-count theorem.

For example, set \(\pi_0=1/1000\), \(q_0=11/20\), \(r_0=9/10\), \(\pi_1=999/1000\), \(q_1=4/5\), and \(r_1=9/10\). Since \((11/9)^{10}<9<(11/9)^{11}\), the eventual optimum is \(t=9\). Exact increment signs give this same optimum at \(h=100,150,200\).

**Failure below one half.** At \(h=2\) take
\[
(\pi_0,q_0,r_0)=(1/5,1/20,1/4),\qquad (\pi_1,q_1,r_1)=(4/5,9/10,19/20).
\]
Here the expert is individually more competent in both states, but the tail formula gives \(P_2(0)=6366953/8000000\), \(P_2(1)=15911/20000\), and \(P_2(2)=81/100\). Thus \(P_2(0)>P_2(1)<P_2(2)\), contradicting unimodality.

## Proof

**Increment formula.** Fix a signal state and abbreviate \(q=q_s\), \(r=r_s\). When one more person delegates, let \(B\sim\operatorname{Bin}(2h-t-1,q)\) count the correct votes of the remaining direct nonexperts, and \(X\sim\operatorname{Ber}(q)\) be the additional delegator's withdrawn vote, independent of \(B\) and the expert. When the expert is correct, the change in correctness probability is
\[
\Pr(B\ge h-t-1)-\Pr(B+X\ge h-t)=(1-q)\Pr(B=h-t-1).
\]
When the expert is wrong, the change is \(\Pr(B\ge h+1)-\Pr(B+X\ge h+1)=-q\Pr(B=h)\). The two point-mass binomial coefficients are equal because their lower indices sum to \(2h-t-1\). Weighting the gain and loss by \(r,1-r\) and then averaging over states gives the boxed formula, including \(t=h-1\).

**Single crossing.** Removing the positive binomial coefficient leaves \(A_t-B_t\), where
\[
A_t=\sum_s\pi_sr_s q_s^{h-t-1}(1-q_s)^{h+1},\qquad
B_t=\sum_s\pi_s(1-r_s)q_s^{h+1}(1-q_s)^{h-t-1}.
\]
For \(t+1<h\), each positive term in \(A_t\) increases by a factor \(1/q_s<2\) and each in \(B_t\) increases by a factor \(1/(1-q_s)>2\). Thus \(A_t\le B_t\) gives \(A_{t+1}<B_{t+1}\). This proves the sign pattern and, with the constant suffix, the unimodality and scan rule. For example, with one state, \(h=2\), \(r=1/2\), and \(q=3/4\), one has \(P_2(1)=45/64\) and \(P_2(2)=P_2(3)=P_2(4)=1/2\). Here \(t=3\) is a weak local maximum but is not globally optimal.

**Selection for large electorates.** The state summand in the increment, without the common coefficient, is \(\pi_s[q_s(1-q_s)]^{h-t-1}G_s(t)\), with \(G_s(t)=r_s(1-q_s)^{t+2}-(1-r_s)q_s^{t+2}\). On \((1/2,1)\), the function \(q\mapsto q(1-q)\) is strictly decreasing. For fixed \(t\), dividing the sum by the least state's positive exponential factor leaves a limit \(\pi_{s_*}G_{s_*}(t)\), whose sign is nonzero when \(\alpha_*\notin\mathbb Z\). Because the number of states is finite, all their \(G_s(T)\) are strictly negative at some fixed integer \(T\): each ratio \(q_s/(1-q_s)\) exceeds one and each expert competence is less than one. For \(h>T\), the negative increment at \(T\) and single crossing exclude all maximizing counts greater than \(T\), including the constant suffix. Thus only finitely many fixed-\(t\) signs are needed. For the least state the sign is positive exactly when \(t+2<\alpha_*\). Counting the strictly positive increments before the first negative one yields \(\max\{0,\lfloor\alpha_*-1\rfloor\}\). The rare-state result follows because its positive fixed prior does not affect that eventual sign.

## Verification

The companion `verify.py` uses Python 3 and the standard library. It compares the pivotal formula with exact binomial tails in 5,760 cases and checks 1,280 rational finite-state environments for unimodality. It also tests the five-voter example and checks the rare-state example by exact rational increment signs at the three declared sizes. In its scalar log-odds grid, the integer case is skipped; it uses floating logarithms to choose the noninteger cutoff to test against exact signs. These are finite diagnostics; the theorem follows from the proof.

## Relationship to prior work and limitations

Gilbert et al. develop common-signal liquid democracy and study state-conditioned concentration, safe graph delegation mechanisms, and failures of averaging competence. In the accessible full preprint, the model and mechanism contributions (pp. 1–3), statewise intersection mechanism (Theorem 1, p. 10), accuracy conditions (p. 13), and discussion (p. 17) concern different claims from optimizing the number of delegators in this one-expert star. Dhillon et al., arXiv:2306.03960v1, Proposition 3, already give the scalar log-odds proxy count for a single expert in their neutral-equilibrium setting, with a cap from finite electorate size. The one-state formula is not a novelty claim. The distinction here is the preservation of unimodality under finite common-signal mixtures and selection by their least nonexpert competence state under the stated nondegeneracy condition. The literature comparison is not an exhaustive priority claim.

The result does not cover arbitrary delegation graphs, heterogeneous nonexperts within a signal state, endogenous delegation, voting rules other than the stated strict majority, or priors varying with electorate size. The finite-state model with one expert and an odd total number of votes is essential to the argument as presented.

## References

1. S. Gilbert, S. Schmid, S. Schnell, J. Svoboda, and M. X. Yeo, *Liquid democracy under vote correlation: On the fallacies of averaging and the excluded middle*, https://arxiv.org/abs/2608.16738. Brief announcement: https://doi.org/10.4230/LIPIcs.DISC.2026.64.
2. A. Dhillon, G. Kotsialou, D. Ravindran, and D. Xefteris, *Information aggregation with delegation of votes*, https://arxiv.org/abs/2306.03960v1; journal DOI 10.1111/iere.70126.
3. K. Chatterjee, S. Gilbert, S. Schmid, J. Svoboda, and M. X. Yeo, *When is liquid democracy possible? On the manipulation of variance*, PODC 2025, https://doi.org/10.1145/3732772.3733544.
