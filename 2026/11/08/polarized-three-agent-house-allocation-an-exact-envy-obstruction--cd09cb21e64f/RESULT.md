# Polarized three-agent house allocation: an exact envy obstruction and its stock-law corollary

## Finding

Let \(m\ge3\), and let agents 1 and 2 rank \(h_1,\ldots,h_m\) in opposite orders: agent 1 prefers smaller indices and agent 2 prefers larger indices. Agent 3 has an arbitrary strict ranking \(\pi\). Give each agent one distinct house and allow unused houses. For an assignment \(A\), let \(e_i(A)\) be the number of other assigned houses agent \(i\) prefers to her own, and put
\[
 E(A)=\#\{i:e_i(A)>0\},\qquad P(A)=\sum_i e_i(A),\qquad X(A)=\max_i e_i(A).
\]
There is an envy-free assignment if and only if there are indices \(i<j<k\) such that \(h_j\succ_\pi h_i\) and \(h_j\succ_\pi h_k\). The three optima \(\min_A E(A),\min_A P(A),\min_A X(A)\) are all zero in that case and all one otherwise. In both cases a single assignment attains all three optima. Failure of the triple condition is exactly strict single-dippedness on the displayed axis: from best to worst the ranking removes an endpoint of the remaining axis interval at every step.

**Uniform-ranking corollaries.** At fixed \(m\), for a uniform third ranking the probability that all three optima are one equals \(2^{m-1}/m!\). For the coherent growing inventory \(h_1,h_2,\ldots\), keep the two opposite orders and let the third agent's utilities be **independent and identically distributed from a common atomless law**. Let \(T\) be the first prefix length admitting an envy-free assignment, with \(T=\infty\) if no prefix admits one. Then \(T<\infty\) almost surely, and
\[
 \Pr(T=m)=\frac{2^{m-2}(m-2)}{m!}\quad(m\ge3),\qquad
 \mathbb ET=\frac{e^2+1}{2},\qquad
 \operatorname{Var}(T)=\frac{8e^2+1-e^4}{4}.
\]

## Assumptions and scope

Houses and agents are labeled, preferences are strict, and envy compares only houses actually assigned. The deterministic result needs no randomness. The finite probability conditions on the first two orders and randomizes only the third. For the stock law it suffices that the third agent's rankings are coherent restrictions of one ranking and are uniform on each finite prefix. I.i.d. atomless utilities ensure this by permutation symmetry and the absence of ties, almost surely on all prefixes. Independence and atomlessness without identical laws do not suffice: independent \(U_j\sim\mathrm{Unif}(2j,2j+1)\) make the third ranking follow agent 2's reverse axis on all prefixes, so no envy-free triple occurs and \(T=\infty\) almost surely.

## Proof

**Triple criterion and common optimum.** For three selected houses in axis order \(h_i,h_j,h_k\), envy-freeness forces agent 1 to get \(h_i\) and agent 2 to get \(h_k\). Agent 3 gets \(h_j\), and she has no envy exactly when she ranks it above both others. Conversely those assignments have no envy whenever the triple meets that condition.

On any selected triple, give the third agent her favorite of the three. If it is the middle house, give the two axis agents their preferred endpoints and there is no envy. If it is \(h_i\), assign \((h_j,h_k,h_i)\) to agents \((1,2,3)\), so only agent 1 envies agent 3. If it is \(h_k\), assign \((h_i,h_j,h_k)\), so only agent 2 envies agent 3. Thus all three objectives are at most one under the same assignment. If no triple meets the envy-free condition, each objective is at least one for every assignment. The criterion can be tested in linear time from the ranking array: at each interior index compare its rank to the worst ranks attained strictly to its left and right, computed by prefix and suffix scans. Here a lower rank number means more preferred. The positions of those worst ranks supply witness endpoints when the two comparisons succeed.

**Obstruction count.** If the most preferred house in the third ranking were interior, it would be favored over the two endpoints and give an envy-free triple. Thus a ranking with no such triple starts with an endpoint, and induction on the remaining interval gives endpoint deletion. Conversely, at the first deletion of a member of any triple, its middle house cannot be an endpoint of the remaining interval if both other members are still there. So endpoint deletion implies no triple works. There are \(2^{m-1}\) such rankings, since each deletion offers two distinct choices until the last house. Dividing by \(m!\) gives the fixed-stock probability.

**Stock law.** An envy-free triple remains feasible when additional houses are available, so \(T>m\) holds exactly when the prefix at size \(m\) contains no envy-free triple. With \(q_m=\Pr(T>m)\), uniform prefixes give \(q_m=2^{m-1}/m!\) for \(m\ge2\), with \(q_0=q_1=q_2=1\). These tails tend to zero. For \(m\ge3\), the mass is \(q_{m-1}-q_m=2^{m-2}(m-2)/m!\). By the integer tail-sum identities,
\[
 \mathbb ET=\sum_{m\ge0}q_m=2+\tfrac12(e^2-3),\qquad
 \mathbb ET^2=\sum_{m\ge0}(2m+1)q_m=4+\tfrac12(5e^2-7).
\]
Subtracting the square of the first moment from the second gives the variance. Factorial decay gives absolute convergence of both sums.

## Verification

The accompanying `check.py` enumerates each third-agent permutation and each injective assignment for \(3\le m\le8\), checks the three minima and compares the obstruction and first-success counts to the formulas. Run `python3 check.py` with the supporting script. This is a finite diagnostic; it neither proves the general theorem nor tests that an arbitrary utility model induces uniform rankings. The proof above supplies the all-size conclusions.

## Relationship to prior work

Hosseini, Roy and Sethia [1, Lemma 4.10] prove that a globally single-dipped profile has at most two envy-free agents. Both opposite axis orders are single-dipped, so their lemma already implies the obstruction in the endpoint-deletable case. The converse for an arbitrary third ranking and simultaneous optimality for the three objectives are the structural assertions here. The combinatorial count itself is known: reversing an endpoint-deletion ordering produces a permutation whose every initial segment forms an integer interval, enumerated by OEIS A000079 with the appropriate index shift [3]. The stock formulas are consequences of that count and the conditional allocation criterion. Gan, Suksompong and Voudouris [2] give a general polynomial-time decision procedure and a high-probability result in a different model with independently uniform rankings for all agents, not the conditional fixed-opposite-orders classification.

## Limitations

The result is specific to exactly three agents, two exactly opposite orders, and at most one house per agent. It does not cover ties, cardinal costs, perturbations of the opposite orders, or arbitrary nonuniform utility models. No historical-priority claim is made.

## References

1. H. Hosseini, S. Roy and A. Sethia, *Fair Societies: Algorithms for House Allocations*, arXiv:2511.07022v1, §4.2, Lemma 4.10, https://arxiv.org/html/2511.07022v1.
2. J. Gan, W. Suksompong and A. A. Voudouris, *Envy-Freeness in House Allocation Problems*, arXiv:1905.00468v2, §2, https://arxiv.org/abs/1905.00468v2.
3. OEIS A000079, comment of David Callan, 25 July 2008, on permutations all of whose initial segments are integer intervals, https://oeis.org/A000079.
