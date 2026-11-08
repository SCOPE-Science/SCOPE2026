# A sharp Bernoulli transition and counting law for strong committee representation

## Finding

Fix integers \(m>k\ge2\), and let \(n\ge1\) voters independently approve each of \(m\) candidates with probability \(q\in(0,1)\), independently across every voter–candidate pair. A candidate is *cohesive* if at least \(\lceil n/k\rceil\) voters approve it. Let \(H\) be the random set of cohesive candidates, and let \(\mathcal S_n\) and \(\mathcal T_n\) denote, respectively, the families of size-\(k\) committees satisfying **strong justified representation** (SJR) and **semi-strong justified representation** (SSJR).

Set
\[
\rho=q(1-q)^{m-1},\qquad b_n=\Pr\{\operatorname{Bin}(n,q)\ge\lceil n/k\rceil\},\qquad \varepsilon_n=m(1-\rho)^n.
\]
With probability at least \(1-\min\{1,\varepsilon_n\}\), the following *entire solution-set identity* holds:
\[
\boxed{\mathcal S_n=\mathcal T_n=\{W\subseteq C:|W|=k,\ H\subseteq W\}.}
\]
In particular, if \(Z_n\sim\operatorname{Bin}(m,b_n)\), and \(Y_n=\binom{m-Z_n}{k-Z_n}\) for \(Z_n\le k\), with \(Y_n=0\) otherwise, then each of the two random counts \(|\mathcal S_n|\) and \(|\mathcal T_n|\) has total-variation distance at most \(\min\{1,\varepsilon_n\}\) from the law of \(Y_n\). Their existence probabilities each differ by at most that amount from
\[
B_{m,k}(b_n)=\sum_{j=0}^{k}\binom mj b_n^j(1-b_n)^{m-j}.
\]
Moreover, \(\Pr\{\mathcal S_n\ne\mathcal T_n\}\le\min\{1,\varepsilon_n\}\).

Holding \(m,k\) fixed as \(n\to\infty\), the probability that either SJR or SSJR is satisfiable tends to \(1\) if \(q<1/k\), and to \(0\) if \(q>1/k\). At the sharp critical value \(q=1/k\), the limit is
\[
\boxed{2^{-m}\sum_{j=0}^{k}\binom mj.}
\]
More precisely, if \(q_n=1/k+\lambda/\sqrt n\), with fixed real \(\lambda\) and \(n\) sufficiently large, the limiting satisfiability probability is
\[
\boxed{B_{m,k}\left(\Phi\left(\frac{\lambda}{\sqrt{k^{-1}(1-k^{-1})}}\right)\right),}
\]
where \(\Phi\) is the standard normal distribution function. Under the additional condition that there is at least one cohesive candidate, the critical limiting feasibility probability is \(\big(\sum_{j=1}^k\binom mj\big)/(2^m-1)\), and throughout the Gaussian window the corresponding conditional limit is \(\sum_{j=1}^k\binom mj u^j(1-u)^{m-j}/[1-(1-u)^m]\), where \(u=\Phi(\lambda/\sqrt{k^{-1}(1-k^{-1})})\).

For example, with \(m=4\) and \(k=2\) at the critical point, feasibility tends to \(11/16\); conditional on at least one cohesive candidate it tends to \(2/3\). The limiting common number of satisfying committees has values \(6,3,1,0\) with probabilities \(1/16,4/16,6/16,5/16\), respectively.

## Assumptions and scope

A profile consists of labeled candidates \(C\), labeled voters \(N\), and arbitrary approval subsets \(A_i\subseteq C\), including the empty set. A group \(G\subseteq N\) is cohesive when \(|G|\ge n/k\) and \(\bigcap_{i\in G}A_i\ne\emptyset\). SJR demands that for every cohesive \(G\), some *single elected candidate* lies in \(\bigcap_{i\in G}A_i\). SSJR demands that every voter in every cohesive \(G\) approves at least one elected candidate. The committee has exactly \(k\) distinct candidates. There are no strategic responses or correlations in the approval model.

The finite-probability bound holds for each \(n\ge1\), each integer pair \(m>k\ge2\), and every fixed \(q\in(0,1)\); the asymptotics hold for fixed \(m,k\). The Gaussian-window assertion has a varying parameter \(q_n\), but all approval entries remain independent within each electorate.

## Proof

**1. Deterministic reduction to cohesive candidates.** Write \(N_c=\{i:c\in A_i\}\), and \(H=\{c:|N_c|\ge\lceil n/k\rceil\}\). If a size-\(k\) committee contains \(H\), then for every cohesive group \(G\) choose a candidate \(c\in\bigcap_{i\in G}A_i\). Since \(N_c\supseteq G\), one has \(c\in H\subseteq W\), so every voter in \(G\) approves the same elected candidate. Thus \(W\) satisfies SJR and SSJR.

Call a voter a *private supporter* of \(c\) if her ballot is exactly \(\{c\}\). Suppose every candidate has at least one private supporter. If \(c\in H\setminus W\), then \(N_c\) is a cohesive group containing a private supporter of \(c\). That voter approves no member of \(W\), violating SSJR, and the intersection of ballots within \(N_c\) contains no elected candidate, violating SJR. Therefore, on this private-supporter event, a committee satisfies either axiom if and only if it includes every candidate in \(H\). This proves the displayed solution-set identity, including the empty-family case \(|H|>k\).

**2. Probability of the reduction event.** Under the independent Bernoulli model a given voter is a private supporter of a specified candidate with probability \(\rho=q(1-q)^{m-1}>0\). Across voters these events are independent, so a specified candidate has no private supporter with probability \((1-\rho)^n\). A union bound over the \(m\) candidates gives failure probability at most \(\varepsilon_n\). Since failure probability is also at most one, the total-variation and set-disagreement bounds follow by coupling the actual solution families with the deterministic function of \(H\) on the same probability space.

**3. Exact proxy law.** Each popularity count \(|N_c|\) is distributed as \(\operatorname{Bin}(n,q)\). Approval columns of distinct candidates are mutually independent, so the indicators \(\mathbf1_{\{c\in H\}}\) are independent Bernoulli variables with success probability \(b_n\). Consequently \(|H|\) has the exact \(\operatorname{Bin}(m,b_n)\) distribution. The number of size-\(k\) committees containing \(H\) is \(\binom{m-|H|}{k-|H|}\) if \(|H|\le k\), and zero otherwise. The proxy count and feasibility formulas follow. No independence between the private-supporter event and \(H\) is claimed or needed.

**4. Sharp transition and window.** For fixed \(q<1/k\), the law of large numbers gives \(b_n\to0\); for \(q>1/k\), it gives \(b_n\to1\). Since \(m>k\), the binomial-tail feasibility proxy tends respectively to \(1\) and \(0\); the coupling error vanishes exponentially. At \(q=1/k\), the central limit theorem gives \(b_n\to1/2\), yielding the stated binomial sum. If \(q_n=1/k+\lambda/\sqrt n\), then the triangular-array Bernoulli central limit theorem gives \(b_n\to\Phi(\lambda/\sqrt{(1/k)(1-1/k)})\). Since \(\rho_n=q_n(1-q_n)^{m-1}\) stays bounded away from zero, the coupling error again tends to zero exponentially. The conditional formulas follow by dividing the joint feasibility and positive-cohesion probabilities by \(\Pr(|H|>0)=1-(1-b_n)^m\), whose window limit is positive.

## Verification

Run the self-contained integer/rational checker using `python3 verify.py`. It independently enumerates all approval ballots for eight small parameter triples, checks SJR and SSJR both directly over **all cohesive voter groups** and via their maximal supporter sets, verifies the common-family count whenever every candidate has a private supporter, and checks the exact binomial proxy probability and finite error inequality at \(q=1/2\). The tests cover \(78{,}664\) labeled profiles in total, with no arbitrary sampling and no external modules. All tests returned `ALL_EXHAUSTIVE_CHECKS_PASS`.

The exhaustive tests are finite corroboration only. The general claim follows from the four analytical steps above, not extrapolation from enumeration.

## Relationship to prior work

Chingoma, Grossi, Lindeboom, and Maly (2026) formalize and optimize SJR and SSJR scores, prove worst-case hardness and special-domain algorithms, and experimentally compare the feasibility of the two axioms. Their accessible Sections 2–5 and 8 do not establish a fixed-candidate Bernoulli phase diagram, a total-variation coupling for the entire family of satisfying committees, or a Gaussian critical-window law. The present analysis supplies those probabilistic results for their canonical strong-representation notions.

Elkind and coauthors (2021) prove a sharp impartial-culture threshold for *ordinary JR* justifying groups, via the probability that a voter approves an omitted candidate but none of a proposed committee. That result applies to the weaker JR criterion, under which a cohesive group needs only **one** represented voter; it does not imply the strong/semistrong solution-set identity or feasibility threshold. Brill, Israel, Micha, and Peters (2024) empirically study the related stronger individual-representation axiom under several sampling models and observe frequent compatibility with SSJR; they do not give the present strong/semistrong exact joint law. Grossi, Lisowski, and Papasotiropoulos (2026) prove deterministic SJR/SSJR coincidence on *liquid delegation profiles*, which impose correlated transitive ballots and are not the independent Bernoulli domain here.

Han, Tao, Xia, Zhang, and Zhou (2025) analyze *average justified representation* (AJR) in the identical independent-approval model and prove an existence trichotomy with an additional recovery phase at high approval density. Their AJR quantifies average group satisfaction across all cohesion levels, rather than requiring an elected common candidate (SJR) or representation of every member of every one-cohesive group (SSJR). In particular, AJR can become feasible again at high density even as the private-supporter obstruction makes SJR and SSJR asymptotically infeasible. Their Theorem 2.2 therefore neither implies nor contradicts the present solution-family count and one-threshold law, but it is an important self-review.

The new statement is neither an algorithmic approximation result nor a worst-case complexity improvement. Its full-ballot independent sampling model allows arbitrary approval-set sizes, unlike sparse-ballot restricted-domain results.

## Limitations

The result concerns fixed \(m,k\), independent uniform-edge approval probability, and the indicated one-level SJR/SSJR axioms, not all-level strong EJR or individual representation. It says nothing about growing \(m\), correlated or fixed-size approval ballots, candidate-specific probabilities, strategic voting, or the quality of a particular rule that must find the committee. The finite error bound can be loose when private ballots are rare; its usefulness is asymptotic. Near \(q=0\) or \(q=1\) on scales depending on \(n\), the private-supporter coupling need not be effective, and at \(q=1\) the stated sharp phase transition does not apply. Ordinary JR may remain feasible when both stronger axioms fail.

## References

- J. Chingoma, D. Grossi, F. Lindeboom, and J. Maly, *Diverse Representation in Approval-Based Committee Voting*, arXiv:2609.29332, first posted 2026-09-24, version 2 posted 2026-10-28. https://arxiv.org/abs/2609.29332
- E. Elkind, P. Faliszewski, A. Igarashi, P. Manurangsi, U. Schmidt-Kraepelin, and W. Suksompong, *Justifying Groups in Multiwinner Approval Voting*, arXiv:2108.12949 (2021), Theorem 3.1. https://arxiv.org/abs/2108.12949
- M. Brill, J. Israel, E. Micha, and J. Peters, *Individual Representation in Approval-Based Committee Voting*, Social Choice and Welfare, first published 2024-11-08, DOI:10.1007/s00355-024-01563-w. https://doi.org/10.1007/s00355-024-01563-w
- D. Grossi, G. Lisowski, and G. Papasotiropoulos, *Representation in Peer Selection: A Liquid Democracy Perspective*, arXiv:2608.13085 (2026). https://arxiv.org/abs/2608.13085
- Q. Han, B. Tao, L. Xia, C. Zhang, and H. Zhou, *Likelihood of the Existence of Average Justified Representation*, arXiv:2510.18718 (2025), Theorem 2.2 and Sections 2–5. https://arxiv.org/abs/2510.18718
- H. Aziz, M. Brill, V. Conitzer, E. Elkind, R. Freeman, and T. Walsh, *Justified Representation in Approval-Based Committee Voting*, Social Choice and Welfare 48 (2017), 461–485. https://doi.org/10.1007/s00355-016-1019-3
