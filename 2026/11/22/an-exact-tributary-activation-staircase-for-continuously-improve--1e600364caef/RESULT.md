# An exact tributary-activation staircase for continuously improved fish passage

## Finding

Consider a river mouth, one downstream passage barrier, and \(m\) terminal tributaries, each separated from their spawning habitat by one additional barrier. For distinct positive quality-adjusted habitat weights \(w_1>\cdots>w_m>0\), independent barrier passage probabilities \(p(x)=1-e^{-x}\), and total divisible improvement effort \(B>0\), the expected accessible habitat is
\[
F(x_0,x_1,\ldots,x_m)=(1-e^{-x_0})\sum_{i=1}^m w_i(1-e^{-x_i}),\qquad x_i\ge0,\quad\sum_{i=0}^m x_i=B.
\]
There is exactly one global maximizer. Its active tributaries are precisely the first \(k=k(B)\) in weight order, where
\[
 k(B)=1+\#\{j\in\{2,\ldots,m\}:B>B_j\},\qquad
 B_j=\log\left(\frac{\sum_{i<j}w_i}{w_j}-(j-2)\right)+\sum_{i<j}\log\frac{w_i}{w_j}.
\]
These thresholds are strictly increasing. At \(B=B_j\), tributary \(j\) still receives zero effort; it receives positive effort immediately above the threshold. Put \(W_k=\sum_{i=1}^k w_i\), \(P_k=\prod_{i=1}^k w_i\). Let \(z>1\) be the unique solution of
\[
 z(z+k-1)^k=\frac{e^B W_k^k}{P_k},
\]
and define \(\tau=W_k/(z+k-1)\). Then the exact optimum is
\[
 x_0=\log z,\qquad x_i=\begin{cases}\log(w_i/\tau),&i\le k,\\0,&i>k.\end{cases}
\]
For \(k=1\), the downstream barrier and best tributary each get \(B/2\). As soon as a second tributary activates, the downstream barrier receives *strictly more* effort than every tributary.

For a countably infinite set of tributaries with geometric habitat weights \(w_i=q^{i-1}\), \(0<q<1\), the unique optimum has finitely many active tributaries at every finite budget. Writing \(L=-\log q\), its transition budgets satisfy the sharper exact asymptotic
\[
 B_j=\frac L2(j-1)(j+2)-\log(1-q)+O(jq^{j-1}),\qquad
 k(B)\sim\sqrt{\frac{2B}{L}}\quad(B\to\infty).
\]
This is a square-root diversification law despite linearly growing total improvement effort.

## Assumptions and scope

The topology is one downstream barrier common to all routes, followed by one barrier on each of \(m\) terminal tributaries. All fish enter from the river mouth. A successful route requires passage through the common barrier and its own terminal barrier. Passages are independent; no density limitation, dispersal, habitat feedback, or additional internal tributary barriers are modeled. The quality-adjusted expected habitat payoff is additive across accessible terminal tributaries, not the probability that *every* or *at least one* tributary succeeds. Improvement cost is linear in nonnegative effort, without a fixed activation cost, and every barrier has the same idealized exponential effort-to-passability curve. The strict weight order ensures no ambiguity over tributary labels.

The finite-tributary result applies to every integer \(m\ge1\), all such positive weights, and every budget \(B>0\). In the infinite case the weights are exactly geometric and the optimization is over nonnegative summable allocations with total effort at most \(B\). The infinite-branch objective converges absolutely because \(\sum_iw_i<\infty\).

## Proof

**1. Existence, concavity and uniqueness for finitely many tributaries.** Each \(u(t)=1-e^{-t}\) is strictly increasing and strictly concave on \([0,\infty)\). Let \(G(x_1,\ldots,x_m)=\sum_i w_i u(x_i)\). For positive payoff, \(\log F=\log u(x_0)+\log G\). Both terms are concave: the logarithm is increasing and concave, and its arguments are concave and positive on the positive-payoff region. They are strictly concave in their respective variables because \(u\) and \(G\) are strictly concave; hence \(\log F\) is strictly concave wherever \(F>0\). The compact simplex has a positive-payoff feasible point for every \(B>0\), so a maximizer exists, has \(x_0>0\) and \(G>0\), and is unique. Strict monotonicity in every positive direction implies all budget is spent.

**2. KKT equations and active-set order.** At an optimal positive-payoff allocation define \(\tau>0\) by equality of marginal branch benefits: active tributaries obey \(w_i e^{-x_i}=\tau\) and inactive ones obey \(w_i\le\tau\). Thus the active set is the first \(k\) weights, with \(x_i=\log(w_i/\tau)\) for \(i\le k\). The total branch payoff is \(G=W_k-k\tau\). The marginal logarithmic benefits of trunk and an active branch are respectively
\[
 \frac{1}{e^{x_0}-1},\qquad \frac{\tau}{G}.
\]
Equality gives \(e^{x_0}=W_k/\tau-(k-1)=z\). Combining the budget identity with \(\tau=W_k/(z+k-1)\) gives the displayed degree-\((k+1)\) equation. The left side is strictly increasing for \(z\ge1\); the actual active \(k\) ensures a root \(z>1\). Conversely, a feasible candidate satisfying these equal-marginal and inactive-marginal inequalities is globally optimal by concavity, so this solution characterizes the unique optimizer.

**3. Exact, strictly ordered activation budgets.** For a fixed active set, its budget is the strictly decreasing function of \(\tau\):
\[
 \mathcal B_k(\tau)=\log\left(\frac{W_k}{\tau}-(k-1)\right)+\sum_{i=1}^k\log\frac{w_i}{\tau}.
\]
Every term decreases strictly as \(\tau\) increases while the active-set constraints hold. At the point \(\tau=w_j\) where branch \(j\) first becomes active, branch \(j\) has zero effort. Evaluating the \(j-1\) active formula gives precisely \(B_j\). At that boundary, the expressions on both sides agree, so the optimal \(\tau\) decreases continuously as the budget increases from zero; distinct decreasing weights give strictly increasing thresholds. At equality, branch \(j\) is still inactive. This also proves that no activation is later reversed.

**4. The strict downstream priority.** For \(k=1\), the equation gives \(x_0=x_1=B/2\). For \(k\ge2\),
\[
 e^{x_0}-e^{x_1}=\sum_{i=2}^k\left(\frac{w_i}{\tau}-1\right)>0
\]
because each active tributary satisfies \(w_i>\tau\). Thus \(x_0>x_1\ge x_2\ge\cdots\ge x_k>0\). As \(B\to\infty\) for fixed \(m\), all tributaries activate, \(\tau\to0\), and \(x_0-x_1\to\log(W_m/w_1)>0\).

**5. Infinitely many geometrically weighted tributaries.** For \(w_i=q^{i-1}\), the same candidate construction is finite at each finite budget because \(B_j\to\infty\). For this finite-support candidate, the derivative of \(\log F\) in every omitted coordinate is at most the common active marginal because \(w_i\le\tau\). The supporting-hyperplane inequality from concavity proves its optimality against every finite-support competitor. Finite truncations approximate any admissible summable competitor, both in total effort and in objective (the latter uniformly because \(\sum_iw_i<\infty\)); continuity extends the inequality to all admissible allocations. Strict concavity gives uniqueness. Finally
\[
 \sum_{i<j}\log\frac{q^{i-1}}{q^{j-1}}=\frac L2 j(j-1),
\]
and
\[
 \frac{\sum_{i<j}q^{i-1}}{q^{j-1}}-(j-2)=\frac{q^{-(j-1)}}{1-q}\left[1-q^{j-1}\bigl(1+(j-2)(1-q)\bigr)\right].
\]
Taking logarithms yields the stated expansion and inverting the strictly increasing activation thresholds yields \(k(B)\sim\sqrt{2B/L}\).

## Verification

The standalone standard-library script `checker.py` reconstructs active sets, solves the monotone scalar equation by bisection, verifies feasibility, downstream priority, random-allocation inequalities, threshold ordering, and the exact geometric-budget identity. Its actual execution passed 39,710 supplementary numerical checks. These checks are *not* substitutes for the all-parameter proof above. In the three-tributary example \((w_1,w_2,w_3)=(9,3,1)\), the two exact thresholds are \(B_2=\log9\) and \(B_3=\log297\). At \(B=4\) precisely two tributaries activate; at \(B=7\), all three activate.

## Relationship to prior work

The cumulative passability product and habitat-weighted sum are established ecological connectivity concepts, particularly in King and O'Hanley (2014, accepted manuscript, sections 1–2), King et al. (2017), and Ioannidou et al. (2023, methods). Those works optimize discrete barrier projects or evaluate geographic indices and uncertainty, whereas this theorem classifies the full continuously divisible exponential-effort optimizer for a shared downstream bottleneck with arbitrary ranked tributaries. Virbickas and Kesminas (2024, methods and discussion) substantiate the relevance of habitat quality, passability and the importance of downstream barriers but do not derive the budget thresholds. Kettelle (1962, pp. 261–262, full text inspected) supplies an explicit optimization of the **sum of exponential stage-unavailabilities** for a serial reliability system, with an approximation bound for the product-based system reliability; it does not optimize the habitat-weighted shared-trunk product of a sum of branch passabilities treated here. Ordinary KKT/water-filling theory supplies part of the proof technique. The present claims are the **complete rooted-tributary activation staircase, strict common-barrier dominance, and the geometric-weight square-root law** rather than the underlying generic method. No claim of broad priority over all reliability or nonlinear resource-allocation literature is made.

## Limitations

This idealized program excludes mandatory fixed costs, baseline passability above zero, heterogeneous barrier improvement curves, intermediate spawning habitat on the common trunk, correlated crossing failures, management uncertainty and temporal population dynamics. Its quantitative prescription must not be transferred directly to a real fishway without calibrating the response curves and costs. Generic nonlinear optimization and historical reliability theory are plausible sources of equivalent transformations; the historical-literature comparison remains provisional. No exhaustive review of every monograph or unpublished result has been completed.

## References

- Virbickas, T., and Kesminas, V. (2024). *Prioritisation of Barriers According to Their Impact on Migratory Fish in the Lowland River Basin District*. Fishes **9**, 113. First public date 2024-03-22. https://doi.org/10.3390/fishes9040113
- King, S., and O'Hanley, J. R. (2014). *Optimal Fish Passage Barrier Removal—Revisited*. River Research and Applications. https://doi.org/10.1002/rra.2859 ; accepted manuscript https://kar.kent.ac.uk/46452/1/FPBRP%20Revisited%20R1.pdf
- King, S., O'Hanley, J. R., Newbold, L. R., Kemp, P. S., and Diebel, M. W. (2017). *A toolkit for optimizing fish passage barrier mitigation actions*. Journal of Applied Ecology **54**, 599–611. https://doi.org/10.1111/1365-2664.12706
- Ioannidou, C. T., Neeson, T. M., and O'Hanley, J. R. (2023). *Boosting large-scale river connectivity restoration by planning for the presence of unrecorded barriers*. Conservation Biology **37**, e14093. https://doi.org/10.1111/cobi.14093
- Burch, C. A., Jardine, S. L., Lewis-Smith, C., and Van Deynze, B. (2024). *Who prioritizes what? A cross-jurisdictional comparative analysis of salmon fish passage strategies in Western Washington*. Conservation Science and Practice **6**, e13102. https://doi.org/10.1111/csp2.13102
- Kettelle, J. D. (1962). *Least-Cost Allocations of Reliability Investment*. Operations Research **10**, 249–265. https://doi.org/10.1287/opre.10.2.249
