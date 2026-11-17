# Arithmetic rigidity of best-of-both-worlds fairness for identical chores

## Finding

**Theorem (phase transition and arithmetic rigidity).** Let \(n\ge2\) and \(m\ge1\) be integers. There are \(m\) distinct indivisible chores, each costing every one of the \(n\) agents exactly one unit. Entitlements \(w_1,\ldots,w_n\) are strictly positive and satisfy \(\sum_i w_i=1\). A lottery is *admissible* if it is weighted envy-free in expectation (ex-ante WEF) and each supported deterministic allocation is weighted envy-free up to one chore (ex-post WEF1). Then:

1. For \(m<n\), an admissible lottery exists **if and only if** \(m w_i\le1\) for every \(i\). Thus the feasible entitlement set contains a relatively open subset of the weight simplex.
2. For \(m=n\), an admissible lottery exists **if and only if** all weights equal \(1/n\).
3. For \(m=n+1\), precisely \(2^n-1\) entitlement vectors are admissible. They correspond bijectively to the nonempty subsets \(S\subseteq\{1,\ldots,n\}\): writing \(t=|S|\), their weights are
   \[
   w_i=\begin{cases}\dfrac{t+1}{t(n+1)},&i\in S,\\[3pt]\dfrac1{n+1},&i\notin S.\end{cases}
   \]
   A realizing lottery gives every agent one chore and assigns the single remaining chore uniformly to one member of \(S\).
4. For **every fixed** \(m\ge n\), the set of all admissible positive weight vectors is **finite**, and **every** admissible weight is rational. In particular, the feasible entitlement set has measure zero in the weight simplex for \(m\ge n\).
5. For \(n=2\), writing \(w_1=p\), \(w_2=1-p\) with \(0<p<1\), admissibility is equivalent to
   \[
   mp\in\mathbb Z\quad\text{or}\quad(m-1)p\in\mathbb Z.
   \]
   Thus, for \(m\ge2\), exactly \(2m-3\) distinct values of \(p\) work; for \(m=1\), every \(p\in(0,1)\) works.

The theorem concerns **existence** of such a lottery; it does not require strategyproofness, independence of random allocations, or universal feasibility for all entitlement vectors. Because each chore has the same unit cost to every agent, every complete allocation is also fractionally Pareto optimal.

## Assumptions and scope

A deterministic allocation assigns every chore to exactly one agent. Denote the number assigned to agent \(i\) by \(x_i\in\mathbb Z_{\ge0}\), with \(\sum_i x_i=m\). For homogeneous unit costs, weighted envy-freeness up to one chore is equivalent to the scalar condition
\[
\forall i,j\quad x_i>0\Longrightarrow\frac{x_i-1}{w_i}\le\frac{x_j}{w_j}.\tag{1}
\]
Since every removal reduces cost by exactly one, WEF1 and weighted EFX coincide on this domain. Weighted ex-ante envy-freeness requires that \(\mathbb E[X_i]/w_i\le\mathbb E[X_j]/w_j\) for all \(i,j\). Therefore all ratios coincide, and summing expected chore counts gives the equivalent condition
\[
\mathbb E[X_i]=m w_i\quad\text{for all }i.\tag{2}
\]
For completeness, the sum of agents' unit costs is always \(m\), including under fractional reallocations. Therefore no fractional reallocation can make all agents weakly better off and at least one strictly better off.

## Proof

**Reduction to count vectors.** Chores are interchangeable for all the fairness and efficiency conditions, so a lottery over allocations is determined for present purposes by a probability distribution on the nonnegative integer vectors \(x\) summing to \(m\). Equations (1) and (2) give necessary and sufficient feasibility conditions.

**Case \(m<n\).** Every count vector has a zero coordinate \(x_j=0\). Equation (1) then forbids any \(x_i\ge2\), because \((x_i-1)/w_i>0=x_j/w_j\). Conversely, any \(0\)-\(1\) count vector satisfies (1). The possible expectations are exactly the polytope
\[
\left\{v\in[0,1]^n:\sum_i v_i=m\right\}.
\]
To see this directly, a vertex cannot have two strictly fractional coordinates (perturb one up and the other down); it cannot have exactly one because the sum is integral. Hence all vertices are indicators of \(m\)-subsets. Equation (2) is feasible precisely when \(m w_i\le1\) for every coordinate. The uniform weight vector obeys these inequalities strictly when \(m<n\).

**Case \(m\ge n\): no empty recipient.** If a WEF1 count vector had some \(x_j=0\), the preceding argument would give \(\sum_i x_i\le n-1\), a contradiction. Hence every \(x_i\ge1\). For \(m=n\), this forces \(x_i=1\) for every agent; equation (2) forces the uniform weight vector, which is feasible.

**Case \(m=n+1\).** A WEF1 vector has one coordinate equal to two and all others equal to one. If agent \(i\) receives the additional chore, (1) with any \(j\ne i\) gives \(1/w_i\le1/w_j\), so only agents with maximal weight can be extra recipients. Let \(q_i\) be the lottery probability that \(i\) receives this extra chore. By (2),
\[
q_i=(n+1)w_i-1,\qquad \sum_iq_i=1.
\]
Let \(S=\{i:q_i>0\}\), which is nonempty. Outside \(S\), \(w_i=1/(n+1)\); inside \(S\), all weights are equal (they must all be maximizers), hence all positive \(q_i\) are equal to \(1/|S|\). This proves the displayed formula. Conversely, the explicit uniform lottery over \(S\) satisfies (1) and (2). The weight vectors from different nonempty subsets \(S\) are distinct, including \(S\) equal to the whole population, giving the count \(2^n-1\).

**Rational rigidity for every \(m\ge n\).** Fix any admissible lottery, and let \(\mathcal S\) be its finite nonempty set of positively supported count vectors. Every coordinate of every \(x\in\mathcal S\) is at least one. Take distinct \(x,y\in\mathcal S\), and choose indices \(i,j\) with \(x_i>y_i\) and \(x_j<y_j\); both types exist because the vectors have equal total sum. By integrality and (1),
\[
\frac{y_i}{w_i}\le\frac{x_i-1}{w_i}\le\frac{x_j}{w_j}\le\frac{y_j-1}{w_j}\le\frac{y_i}{w_i}.
\tag{3}
\]
All inequalities in (3) are equalities. In particular,
\[
x_i=y_i+1,\qquad y_j=x_j+1,\qquad \frac{w_i}{w_j}=\frac{y_i}{x_j}\in\mathbb Q_{>0}.\tag{4}
\]
Construct an undirected graph on agents, joining \(i,j\) whenever some two vectors in \(\mathcal S\) increase coordinate \(i\) and decrease coordinate \(j\) in opposite directions. By (4), each edge fixes the positive rational ratio of its two endpoint weights. For any two distinct vectors \(x,y\), every increasing coordinate is joined to every decreasing one, so all coordinates that change between \(x\) and \(y\) belong to one connected component of this graph. Their changes sum to zero. Thus, for each connected component \(C\), the integer sum \(\sum_{i\in C}x_i=N_C\) is the same for every \(x\in\mathcal S\). Equation (2) gives
\[
\sum_{i\in C} w_i=\frac{N_C}{m}.\tag{5}
\]
The rational edge ratios on the connected component, together with (5), uniquely determine **all** its weights, and make them rational. The argument applies also to isolated vertices, where (5) determines the single weight. Therefore any fixed nonempty support set \(\mathcal S\) determines at most one entitlement vector, which is rational. There are only \(\binom{m+n-1}{n-1}\) possible count vectors, hence only finitely many possible support sets. This proves assertion 4 without assuming or deriving any unproved generic-position or continuity property.

**Exact two-agent arithmetic law.** Put \(x_1=x\) and \(x_2=m-x\), with \(w_1=p\). Both WEF1 conditions, including the endpoint cases \(x=0,m\), reduce to
\[
mp-p\le x\le mp+1-p.\tag{6}
\]
The interval (6) has length exactly one, and the ex-ante target is \(\mathbb E[x]=mp\). If \(mp\) is integral, the deterministic allocation \(x=mp\) works. Otherwise, the only integers capable of bracketing the expectation are \(\lfloor mp\rfloor\) and \(\lceil mp\rceil\); both lie in (6) exactly when \(\{mp\}=p\), equivalent to \((m-1)p\in\mathbb Z\). A two-point lottery then realizes the desired expectation. For \(m\ge2\), the two families of interior solutions are \(p=k/m\) with \(1\le k\le m-1\) and \(p=\ell/(m-1)\) with \(1\le\ell\le m-2\). They are disjoint since consecutive denominators are coprime, giving \(2m-3\). For \(m=1\), the second integrality condition is automatic.

## Verification

The standalone file `verify_homogeneous_chore_rigidity.py` uses exact `Fraction` arithmetic to evaluate (1) and the exchange-chain equalities. It additionally uses SciPy's linear programming solver as a numerical cross-check of whether the target \((mw_1,\ldots,mw_n)\) belongs to the convex hull of WEF1 count vectors. It checked 658 rational-grid instances, 2,939 exchange-rigidity comparisons, 528 two-person integrality cases, and the closed-form \(n+1\) profiles for population sizes two through six. All executed checks passed. Numerical linear programming is **corroboration only**; the universal implications, sufficiency, finiteness and rationality are proved in the preceding paragraphs, not inferred from bounded tests.

Run from a Python environment with SciPy installed:

```bash
python verify_homogeneous_chore_rigidity.py
```

## Relationship to prior work

Lin, Wu and Zhou [1, Section 4] establish nonexistence of an ex-ante WEF/ex-post WEF1 lottery in the particular homogeneous instance with **two agents, two chores and unequal entitlements**. This matches the \(n=m=2\) boundary here. Their equal-entitlement result concerns general binary additive costs and does not classify all entitlements across homogeneous chore counts. The current theorem supplies the full \(m<n\) regime, the precise \(n+1\)-chore classification and an arithmetic rigidity result for all \(m\ge n\), which are not stated in the inspected primary text.

Wu, Zhang and Zhou [2] establish deterministic WEF1 existence for general indivisible chores via weighted picking sequences, but deterministic WEF1 existence does not imply an ex-ante WEF lottery supported on WEF1 allocations. Hoefer, Schmalhofer and Varricchio [3] establish a general weighted best-of-both-worlds guarantee with the weaker ex-post transfer relaxation \(\mathrm{WEF}(1,1)\) and counterexamples to stronger universal guarantees. Chakraborty, Schmidt-Kraepelin and Suksompong [4] study weighted picking sequences and apportionment methods; those methods' deterministic feasibility criteria do not themselves supply the ex-ante convex-hull characterization. Lin, Liu, Tao and Zhou [5] study a weaker transfer guarantee for mixed manna; only their abstract was materially accessible at inspection. An equivalent unindexed apportionment or allocation characterization cannot be excluded.

## Limitations

The result assumes **identical unit chore costs**, strict positivity of normalized weights, complete allocations, no eligibility restrictions, and exact weighted fairness in expectation. It does **not** extend directly to agent-dependent binary costs or real-valued heterogeneous chore costs. Finiteness holds for each fixed pair of integers \((m,n)\), not uniformly over unbounded chore counts. The source comparison is not a mathematical proof of global novelty; some source materials were inaccessible. No independent external audit has been performed.

## References

1. Z. Lin, X. Wu and S. Zhou, *Revisiting EFX and fPO Allocations for Binary Chores*, arXiv:2609.13970 (first public 2026-09-12), https://arxiv.org/abs/2609.13970.
2. X. Wu, C. Zhang and S. Zhou, *Weighted EF1 Allocations for Indivisible Chores*, arXiv:2301.08090, https://arxiv.org/abs/2301.08090.
3. M. Hoefer, M. Schmalhofer and G. Varricchio, *Best of Both Worlds: Agents with Entitlements*, arXiv:2209.03908, https://arxiv.org/abs/2209.03908.
4. M. Chakraborty, U. Schmidt-Kraepelin and W. Suksompong, *Picking Sequences and Monotonicity in Weighted Fair Division*, arXiv:2104.14347, https://arxiv.org/abs/2104.14347.
5. *Almost Envy-Freeness for Additive Mixed Manna with Entitlements: Deterministic and Randomized Guarantees*, arXiv:2609.02724, https://arxiv.org/abs/2609.02724 (abstract inspected; full text inaccessible).
