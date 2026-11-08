# Near-linear optimal time-conscious delegation on interval hierarchies

## Finding
Fix a rooted tree with root \(r\), pointing every nonroot voter \(v\) toward its unique approved immediate representative \(p(v)\). Each voter chooses one time \(t_v\). For a nonroot voter the allowed times form a *single nonempty integer interval* \(D_v=[a_v,b_v]\cap\mathbb Z\); the casting root has its own ballot interval \(D_r\). At each allowed time an integer utility \(w_v(t)\) is prescribed. For every nonroot voter, a time-dependent trust horizon satisfies \(0\le\delta_v(t)\le t-1\) (no monotonicity requirement). The confluence and time-consciousness constraints are
\[
 t_v-\delta_v(t_v)\le t_{p(v)}\le t_v \qquad(v\ne r).
\]
Put \(S=\sum_v|D_v|\), the size of the explicitly listed available-time data. **Theorem.** The exact feasible-time set for each rooted subtree is an integer interval or empty. Feasibility, a maximum-weight confluent time-conscious assignment \(\max\sum_v w_v(t_v)\), and a maximizing choice of times are computable using \(O(S\log(2+S))\) arithmetic/comparison operations and \(O(S)\) memory. The conclusion holds for arbitrary time-varying scores and arbitrarily nonmonotone trust horizons. Individual time-conscious reachability does not suffice for confluence, even on a four-voter rooted tree.

## Assumptions and scope
All rounds are integers in \([1,L]\), with \(L\ge1\). The tree is fixed and known, rather than optimized; every voter other than the root has exactly one possible recipient, approved in an uninterrupted integer interval. The root is the sole casting voter and may vote at any time in its ballot interval (in the original election model this interval is a terminal interval \([s,L]\)). Each available time has an explicitly supplied finite integer score. A voter selects *one* outgoing action/time, reused for all ballots it receives; only the root casts. All scores are summed once per nonroot voter, with root score zero in the voting interpretation. The result concerns time-conscious and confluent delegation on the fixed hierarchy, not choosing a hierarchy or maximizing an alternative voting rule's utility.

## Proof
**1. Exact subtree feasibility intervals.** Let \(I_v\) be the set of outgoing action times at \(v\) extending to a valid assignment throughout the subtree rooted at \(v\). At a leaf, \(I_v=D_v\). Suppose every child \(c\) has \(I_c=[\ell_c,u_c]\cap\mathbb Z\), nonempty. The feasible parent times supplied by that child are
\[
 Q_c=\bigcup_{s=\ell_c}^{u_c}\big([s-\delta_c(s),s]\cap\mathbb Z\big).
\]
Each summand contains its index \(s\); consequently consecutive summands have no missing integer between them, irrespective of the variation of \(\delta_c(s)\). Thus their union is exactly
\[
 Q_c=[q_c,u_c]\cap\mathbb Z,\qquad
 q_c=\min_{\ell_c\le s\le u_c}\big(s-\delta_c(s)\big).
\]
Different child subtrees are disjoint. Therefore the choice at \(v\) admits compatible choices in *every* child subtree precisely when it belongs to
\[
 I_v=D_v\cap\bigcap_{c:p(c)=v}Q_c.
\]
Equivalently, with empty intersection interpreted as impossibility,
\[
 \ell_v=\max\big(a_v,\max_{c:p(c)=v}q_c\big),\qquad
 u_v=\min\big(b_v,\min_{c:p(c)=v}u_c\big).
\]
A child with empty \(I_c\), or an inequality \(\ell_v>u_v\), makes \(I_v\) empty. This proves the interval characterization and gives an exact feasibility test. The continuous availability assumption matters: if a child can act only at \(1\) and \(3\) with zero horizons, it permits only those two distinct parent times, not their entire interval.

**2. Dynamic programming for exact welfare.** Define \(F_v(t)\) to be the maximum of \(\sum_{x\in\mathrm{subtree}(v)}w_x(t_x)\), subject to all internal time-conscious constraints and \(t_v=t\), with \(F_v(t)=-\infty\) when impossible. Leaves satisfy \(F_v(t)=w_v(t)\). Given all child functions,
\[
 F_v(t)=w_v(t)+\sum_{c:p(c)=v}M_c(t),\quad
 M_c(t)=\max_{s\in I_c:\,s-\delta_c(s)\le t\le s}F_c(s)
\]
for \(t\in I_v\), and \(F_v(t)=-\infty\) otherwise. The maximum of an empty set is \(-\infty\). This is exact because, after fixing the action at \(v\), the choices in distinct child subtrees do not interact. The largest value in \(F_r\) is precisely the global optimum. An optimizer is reconstructed top down by choosing, for each child, a time \(s\) attaining \(M_c(t_v)\).

**3. Upper-envelope algorithm and complexity.** For each feasible child time \(s\), form a weighted closed integer interval \([s-\delta_c(s),s]\) with weight \(F_c(s)\). The message \(M_c(t)\) is the maximum weight of all intervals covering \(t\). Sort their left and right-plus-one endpoints and sweep in increasing time, retaining active intervals in a max-heap keyed by weight and deleting expired intervals lazily. Between consecutive event times, the maximum is constant; there are at most twice as many events as candidate child times. For each resulting constant segment, add its value to a difference array on the parent's available time interval, truncating segments at the endpoints of \(D_v\). After all children are processed, one prefix sum over this array, followed by adding \(w_v(t)\), gives every finite entry \(F_v(t)\). The feasibility interval from Step 1 excludes times for which some message is undefined. Every nonroot domain is swept exactly once for its unique parent, and every parent domain is scanned once. Hence the total work is \(O(S\log(2+S))\), space \(O(S)\) (including the input, tables, events and difference arrays), and top-down witness extraction adds only \(O(S)\) work. For rational weights, replace integer arithmetic with exact rational arithmetic; this operation bound excludes bit-complexity of arbitrarily large values.

**4. Strict separation from individual reachability.** Take a four-voter tree \(r\leftarrow p\leftarrow c\) and \(p\leftarrow d\), with time horizon \(L=6\). Allow \(r,p\) in rounds \([1,6]\), \(c\) only at time \(2\), and \(d\) only at time \(5\). Give \(p\) retrospective trust \(\delta_p(t)=t-1\) and the two leaves one-step trust \(\delta_c(t)=\delta_d(t)=\min(1,t-1)\). Then \(c\) requires \(t_p\in[1,2]\) whereas \(d\) requires \(t_p\in[4,5]\). Each leaf independently reaches \(r\) through a suitable choice of \(t_p\) and \(t_r=1\), but the two demands have empty intersection. Therefore no confluent assignment exists.

## Verification
The standard-library `verify.py` explicitly constructs maximum-weight messages by a heap sweep and independently enumerates all action-time tuples for 5,750 pseudorandom small rooted hierarchies. It confirms identical optimum values, correct infeasibility decisions and valid maximizing witnesses. The script also checks the four-voter obstruction and the existence of the individual time-conscious routes. Execute `python3 verify.py` from the extracted package. The proof above, not finite enumeration, establishes the statement for arbitrary finite trees and time horizons.

## Relationship to prior work
Markakis and Papasotiropoulos (2023) introduce the time-consciousness and confluence model and show that general welfare optimization respecting both is NP-hard even for retrospective trust; they offer polynomial-time procedures when an axiom is relaxed and an exponential-in-delegators procedure in a restricted case. Their complete arXiv text, including the theorem statements and appendices, does not give the fixed single-parent hierarchy's exact interval-feasibility profile or the near-linear all-score optimum under arbitrary nonmonotone horizons. Standard tree-constraint dynamic programming motivates Step 2; the claim is its exact interval geometry and sparse weighted-interval-envelope implementation for the stated election model, not the abstract principle of tree dynamic programming. Other temporal-reachability or branching results address paths, waiting-time reachability or distinct branching objectives; their accessible summaries do not establish the claimed full welfare-confluent tree algorithm.

## Limitations
The result requires one prescribed parent and one uninterrupted time interval per voter. It does not solve parent selection, multiple separated approval windows, multiple casting roots, strategic behavior, or complexity when time-dependent scores and horizons are supplied only in a compressed oracle form. Comparisons with all unpublished or inaccessible related work are not exhaustive; the originality assessment remains provisional pending independent literature review. The verifier checks only finite instances; it is not a proof of the all-size theorem.

## References
1. Evangelos Markakis and Georgios Papasotiropoulos. *As Time Goes By: Adding a Temporal Dimension Towards Resolving Delegations in Liquid Democracy*. arXiv:2307.12898v1, publicly released 2023-07-24. https://arxiv.org/html/2307.12898v1
2. Daniela Bubboloni, Costanza Catalano, Andrea Marino, and Ana Silva. *On Computing Optimal Temporal Branchings and Spanning Subgraphs*. arXiv:2312.11390, publicly released 2023-12-18. https://arxiv.org/abs/2312.11390
3. Filippo Brunelli and Laurent Viennot. *Computing Temporal Reachability Under Waiting-Time Constraints in Linear Time*. SAND 2023, DOI:10.4230/LIPIcs.SAND.2023.4. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SAND.2023.4
4. Bruno Escoffier, Hugo Gilbert, and Adèle Pass-Lanneau. *The Convergence of Iterative Delegations in Liquid Democracy in a Social Network*. arXiv:1904.05775, publicly released 2019-04-10. https://arxiv.org/abs/1904.05775
