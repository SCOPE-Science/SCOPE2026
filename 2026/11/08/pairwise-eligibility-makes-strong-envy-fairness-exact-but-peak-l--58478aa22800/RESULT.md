# Pairwise eligibility makes strong envy fairness exact, but peak load can grow linearly

## Finding

Consider a finite set \(V\) of \(n\ge2\) agents and a finite sequence of indivisible jobs. Every job has a nonempty eligibility set containing at most two agents; it must be assigned to an eligible agent. Each job has a common strictly positive processing time for its eligible agents. For any distinct agents \(i,j\), the *pair-restricted load* of \(i\) is the total size of jobs assigned to \(i\) for which both \(i\) and \(j\) were eligible. Strong EF1 requires that for each ordered pair \((i,j)\), the load of \(i\), after deleting at most one of its pair-relevant assigned jobs, is at most the pair-restricted load of \(j\).

**Pairwise eligibility theorem.** Every such arbitrary-weight stream admits a deterministic irrevocable online assignment satisfying strong EF1 after *every prefix*, without foreknowledge of job sizes or the stream. For unit-size jobs it satisfies the stronger condition strong EFX after every prefix.

There is also an exact offline peak-load optimum in the unit-size case. Write \(s_i\) for the number of singleton-eligible jobs forced to agent \(i\), and \(q_{ij}\) for the number of jobs with eligibility set exactly \(\{i,j\}\). Define
\[
 b_i=s_i+\sum_{j\ne i}\left\lfloor\frac{q_{ij}}2\right\rfloor,
 \qquad H=\bigl(V,\{\{i,j\}:q_{ij}\text{ is odd}\}\bigr).
\]
Here \(H\) is a simple graph, even though multiple original jobs can share the same pair. The **minimum makespan among all complete strong-EF1 allocations** is the integer
\[
 \boxed{T_{\mathrm{SEF1}}=\max_{\varnothing\ne S\subseteq V}
 \left\lceil\frac{\sum_{i\in S}b_i+|E(H[S])|}{|S|}\right\rceil.}
\]
An allocation attaining this optimum is computable in polynomial time by an integral maximum flow. The theorem applies equally to unit-size eligible goods, with the direction of envy reversed, because the pairwise strong-EF1 constraints reduce to the same inequalities.

The optimality cost of this fairness requirement can grow linearly with the number of agents. For \(n\ge3\), take a star with \(n-1\) leaves and exactly two unit jobs eligible for each center--leaf pair. The unrestricted optimal makespan is \(2\), whereas the unique pairwise-balanced assignment has strong-EF1 makespan \(n-1\), giving a ratio \((n-1)/2\).

## Assumptions and scope

* There are at least two agents; any finite, possibly empty, job sequence is allowed. Eligibility sets are nonempty and of size at most two, and jobs must go to an eligible agent. No third-party transfers, fractional jobs, or discarded jobs are allowed.
* Strong EF1 uses *both-sided pair restriction*: for each pair, count only jobs for which both agents are eligible, on both agents' assigned sides. For chores, a higher pair-restricted load means envy. Deleting a job means disregarding it for comparison, not actually reallocating it.
* All eligible agents incur the **same** strictly positive size for a given job. The online strong-EF1 assertion admits heterogeneous sizes across jobs. The strong-EFX and exact peak-load formula require all sizes to equal one.
* Strong EFX here means that deleting **any** positive pair-relevant job assigned to the envying agent eliminates pair-restricted envy. When one side has no pair-relevant jobs, its corresponding deletion condition is vacuous.
* Singleton-eligible jobs affect total makespan, but not strong envy between distinct agents. Their counts appear in the base loads \(b_i\).

## Proof

**1. Independent pair streams.** For every unordered pair \(\{i,j\}\), maintain the two pair-specific accumulated loads \(L_{i|ij},L_{j|ij}\). When a new job is eligible for exactly \(i\) and \(j\), irrevocably assign it to whichever endpoint has the smaller *pair-specific* load, breaking ties arbitrarily. Singleton-eligible jobs must go to their sole eligible agent. These choices for distinct pairs affect disjoint sets of jobs; an assignment for one pair never changes the loads used in the comparison for another pair.

**2. Strong EF1 after each prefix.** Fix one pair and an arbitrary time. If one endpoint has a larger pair load, let \(e\) be the most recently assigned job to that endpoint. Immediately before \(e\), that endpoint had pair load no larger than the other endpoint, by the greedy rule. Removing \(e\) leaves exactly that endpoint's pre-\(e\) pair load, which is no larger than the other endpoint's load *at that earlier time*, hence no larger than the other's current load. This supplies a legitimate one-job EF1 witness. If the loads are equal, there is no strong envy. The argument applies independently to every pair at every prefix, for arbitrary positive job sizes. It is an online theorem; it makes no claim of global ordinary EF1 in which singleton or other-pair jobs are included in envy comparisons.

**3. Exact unit-size fairness constraints.** Fix pair \(\{i,j\}\) with \(q_{ij}\) unit jobs. Let \(x_{ij}\) be the number assigned to \(i\), and \(q_{ij}-x_{ij}\) the number assigned to \(j\). The requirement that removing at most one unit from the higher side eliminate envy in both directions is equivalent to
\[
 |2x_{ij}-q_{ij}|\le1.
\]
Thus, in every strong-EF1 allocation, the pair splits into \(\lfloor q_{ij}/2\rfloor\) jobs for each endpoint and, exactly when \(q_{ij}\) is odd, one additional job assigned to exactly one endpoint. Conversely every such splitting is strong EF1. Because all pair-relevant jobs have identical unit size, removing *any* one of the higher endpoint's pair jobs has the same effect, so strong EF1 and strong EFX coincide on this domain.

**4. Reduction to bounded orientations.** The forced half-splits and singleton jobs give load \(b_i\). Each pair of odd multiplicity contributes one residual unit job, represented by one edge of \(H\); orient its edge toward the endpoint receiving that residual job. Thus the complete family of strong-EF1 unit allocations corresponds exactly to orientations of \(H\), with final loads \(b_i+\operatorname{indeg}_H(i)\).

For a proposed integer makespan \(T\), define capacity \(c_i=T-b_i\). There exists such an orientation with maximum load at most \(T\) exactly when \(c_i\ge0\) for every vertex and
\[
 |E(H[S])|\le\sum_{i\in S}c_i\qquad
   \text{for every nonempty }S\subseteq V.
\]
Necessity follows because every edge internal to \(S\) must be assigned to some endpoint inside \(S\). For sufficiency, form a bipartite graph with a left node for each edge of \(H\) and a right node for each vertex; a left edge-node is adjacent precisely to its two endpoints, with right-node capacity \(c_i\). For any set of left nodes, all of their endpoints lie in a set \(S\), and their number is at most \(|E(H[S])|\), which the displayed bound makes at most the sum of endpoint capacities. The capacitated Hall theorem, or an integral max-flow, assigns every edge-node to an endpoint. This proves sufficiency without assuming that a fractional allocation can be rounded arbitrarily.

Since \(c_i=T-b_i\), these necessary and sufficient inequalities are exactly
\[
 T\ge\frac{\sum_{i\in S}b_i+|E(H[S])|}{|S|}
 \quad\text{for all nonempty }S\subseteq V.
\]
Singleton subsets enforce \(T\ge b_i\), so no extra condition is missing. Taking the smallest integer \(T\) proves the boxed formula. The set constraints are a characterization, not a proposed exponential-time algorithm: binary search over \(T\), using integral max flow for each feasibility test, yields a polynomial-time optimum and a realizing orientation.

**5. Efficiency separation.** In the two-job-per-spoke star, strong EF1 requires exactly one of the two jobs on each spoke at each endpoint, so the center receives \(n-1\) jobs and each leaf receives one. The fair makespan is exactly \(n-1\). Without this constraint, assign both jobs on every spoke to its leaf, giving makespan \(2\). Since the total number of jobs is \(2(n-1)\), a makespan of one would allow at most \(n\) jobs, but \(2(n-1)>n\) for every \(n\ge3\); hence the unrestricted optimum is exactly \(2\).

## Verification

The companion script `verify.py` independently computes the displayed subset maximum and directly enumerates all assignments of pair jobs, filtering the resulting assignments by the literal two-sided strong-EF1 conditions. Its exact checks covered all \(3{,}375\) three-agent profiles with three pair multiplicities in \(\{0,1,2,3,4\}\) and three singleton counts in \(\{0,1,2\}\). It also compared \(3{,}500\) reproducibly sampled four-agent instances, and directly checked strong EF1 after each prefix of \(1{,}200\) random arbitrary-positive-weight online streams. All checks passed when executed with Python 3.

Reproduce with `python3 verify.py`. The script uses only the Python standard library. These finite checks are a cross-check, **not a proof** of the unbounded theorem; the five proof steps above supply the proof.

## Relationship to prior work

Biburger, Megow and Shahkarami (arXiv:2610.08064, first publicly posted 6 October 2026) introduce strong and weak eligibility-aware envy. Their Section 5 and Appendix D establish general strong-EF1 nonexistence and an online impossibility using a job eligible for three machines; their positive online guarantee concerns *weak* EF1. The present theorem concerns the rank-two subdomain, gives prefixwise strong EF1 (and unit strong EFX), and determines the exact cost-minimizing fair allocation. Their theorem does not imply the positive pairwise result.

Sun, Wang and Li (arXiv:2602.18098) investigate proportionality, equitability, and ordinary envy in graph orientations. Ordinary chore EF1 is **not** the same as strong pair-restricted EF1, because it compares the whole recipient load, not only the jobs jointly eligible to the compared pair; their results do not give this max-load formula. The final bounded-orientation feasibility step is a classical capacitated Hall / Hakimi--Frank--Gyárfás fact: it is **not claimed as a new graph-orientation theorem**. The contribution is the exact identification of the strong-fairness feasible set and its sharp application to online fairness and load optimization under pairwise eligibility.

## Limitations

The exact density formula applies only to **unit-size** jobs. For unequal positive sizes, pairwise greedy still guarantees online strong EF1 but the feasible set need not be an orientation of a parity graph. Strong EFX cannot be guaranteed online for arbitrary sizes even with two universally eligible machines and arriving sizes \(1,1,2\). The linear price example is a lower-bound family, not a claimed universal worst-case approximation ratio. Different notions called EF1 in graphical fair-division papers may include jobs on which the compared agent is ineligible; those are expressly outside the present claim. No assertion of a new general Hall theorem, randomized lower bound, or independent audit is made.

## References

1. J. Biburger, N. Megow and G. Shahkarami, *Online Fair Division under Eligibility Constraints*, arXiv:2610.08064 (first posted 2026-10-06), https://arxiv.org/abs/2610.08064 ; relevant full-text Sections 5 and Appendix D.
2. A. Sun, R. Wang and B. Li, *Fair Orientations: Proportionality and Equitability*, arXiv:2602.18098 (first posted 2026-02-20), https://arxiv.org/pdf/2602.18098 ; relevant introductory classification and Section 5.
3. S. L. Hakimi, *On the degrees of the vertices of a directed graph*, J. Franklin Inst. 279 (1965), 290–308, https://doi.org/10.1016/0016-0032(65)90340-6.
4. A. Frank and A. Gyárfás, *How to orient the edges of a graph*, cited in the degree-bounded orientation theorem summary at https://lemon.cs.elte.hu/egres/open/Orientation_with_degree_bounds .
5. K. Hsu and V. King, *Polynomial-Time Algorithms for Fair Orientations of Chores*, ECAI 2025 proceedings (online 2026), https://doi.org/10.3233/FAIA251225 .
