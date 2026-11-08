# Two-median conservation and exact relaxation on bipartite opinion networks

## Finding

In the continuous-time weighted-median opinion model, two groups that each listen to a common weighted profile of the opposite group admit an exact solution whenever both initial group medians are unique. The sum of their two evolving weighted medians is constant; their difference decays precisely at rate \(2\), while every within-group opinion difference decays precisely at rate \(1\). The selected consensus is **the arithmetic mean of the two initial group medians**, independent of the groups' cardinalities and of the initial non-median opinions.

Specifically, with the definitions below, put \(c=(u+v)/2\) and \(q=e^{-t}\). For every \(t\geq0\), the unique solution is
\[
\begin{aligned}
x_i(t)&=c+\frac{u-v}{2}q^2+(a_i-u)q,&&i\in A,\\
y_j(t)&=c-\frac{u-v}{2}q^2+(b_j-v)q,&&j\in B.
\end{aligned}
\]
Thus \(\lim_{t\to\infty}x_i(t)=\lim_{t\to\infty}y_j(t)=c\) for every agent. These are the exact global trajectories, rather than just an asymptotic approximation. A complete bipartite network with odd-sized parts and uniform opposite-part weights satisfies the hypotheses for every initial opinion profile, including repeated values. For example, the two uniform-weight groups with initial opinions \(0,1,9\) and \(2,4,5,8,10\) select consensus \(3\), not the overall arithmetic mean \(39/8\).

## Assumptions and scope

Let \(A,B\) be nonempty disjoint finite vertex sets, with sizes \(m,n\). For each \(i\in A\), define its influence weights by \(W_{ij}=\beta_j>0\) for \(j\in B\) and zero otherwise; for each \(j\in B\), define \(W_{ji}=\alpha_i>0\) for \(i\in A\) and zero otherwise, where \(\sum_{i\in A}\alpha_i=\sum_{j\in B}\beta_j=1\). All agents within one group therefore use exactly the same positive, normalized influence weights on the opposite group; the group profiles \(\alpha\) and \(\beta\) may differ.

For a finite weighted profile \((z_k,\rho_k)\), a *weighted median* is an **observed value** \(z_\ell\) for which the total weights of strictly smaller and strictly larger values are each at most \(1/2\). If several observed values qualify, the continuous-time model chooses the qualifying value closest to the updating agent's current opinion, as in Han et al. The equation is \(\dot z_i=\operatorname{Med}_i(z;W)-z_i\); no self-weights are present in this two-group specialization.

Write \(a_i=x_i(0)\) and \(b_j=y_j(0)\). Assume that \(u\), the \(\alpha\)-weighted median of \((a_i)_{i\in A}\), is unique, and that \(v\), the \(\beta\)-weighted median of \((b_j)_{j\in B}\), is unique. Equivalently, at each of \(u,v\), the total mass of values strictly below and strictly above is strictly less than \(1/2\). All initial opinions are arbitrary real numbers. No generic-position condition between the two groups is needed.

## Proof

**Step 1: affine equivariance of unique weighted medians.** For any \(r>0\), a common transformation \(z_k\mapsto s+r z_k\) preserves all strict and non-strict order comparisons and their corresponding weights. If \(u\) is the unique weighted median of \((z_k)\), then \(s+ru\) is the unique weighted median of the transformed profile. This remains valid when initial opinions coincide, because weights at equal opinion values aggregate without changing the inequalities.

**Step 2: construct and identify the two evolving group medians.** Define
\[
P(t)=c+\tfrac12(u-v)e^{-2t},\qquad
Q(t)=c-\tfrac12(u-v)e^{-2t}.
\]
Consider the trajectories in the Finding section. Each \(A\)-opinion is the common shift \(P(t)\) plus \(e^{-t}(a_i-u)\). By Step 1, its group \(\alpha\)-weighted median is exactly \(P(t)\). Likewise, the \(B\)-profile has unique \(\beta\)-weighted median \(Q(t)\). Because all \(A\)-agents listen to \(B\), the median driving every \(A\)-agent is \(Q(t)\), while the median driving every \(B\)-agent is \(P(t)\).

**Step 3: verify the differential equations and initial data.** Direct differentiation gives
\[
P'(t)=-(u-v)e^{-2t}=Q(t)-P(t),\qquad
Q'(t)=(u-v)e^{-2t}=P(t)-Q(t).
\]
Consequently,
\[
\dot x_i=P'(t)-e^{-t}(a_i-u)=Q(t)-x_i(t),\qquad
\dot y_j=Q'(t)-e^{-t}(b_j-v)=P(t)-y_j(t),
\]
which are precisely the original weighted-median differential equations. At \(t=0\) the formulas give \(x_i(0)=a_i\), \(y_j(0)=b_j\). The global non-expansiveness of the selected weighted-median map, established in the initiating paper, makes the vector field globally Lipschitz and hence guarantees uniqueness of solutions. Alternatively, the constructed path remains entirely in an open unique-median regime for each finite time, so no tie selection enters it.

**Step 4: exact invariants, rates, and selection.** By Step 2, the two group medians are \(P(t),Q(t)\). Therefore
\[
P(t)+Q(t)=u+v,\qquad P(t)-Q(t)=(u-v)e^{-2t}.
\]
Within each group, common shifts cancel, giving \(x_i(t)-x_k(t)=e^{-t}(a_i-a_k)\), and similarly \(y_j(t)-y_\ell(t)=e^{-t}(b_j-b_\ell)\). Thus the rates \(1\) and \(2\) are sharp whenever their respective mode coefficients are nonzero, and the common limit is \(c=(u+v)/2\). For uniform weights and odd group sizes, each group's ordinary middle order statistic is a unique weighted median, irrespective of ties among opinion values.

**Boundary of the uniqueness hypothesis.** The uniform \(K_{2,2}\) example \(a=(-1,1)\), \(b=(-2,2)\), with the closest-**observed**-median rule, has instead the explicit solution
\[
\begin{aligned}
x(t)&=\bigl(-\tfrac32+\tfrac12e^{-2t},\ \tfrac32-\tfrac12e^{-2t}\bigr),\\
y(t)&=\bigl(-\tfrac32-\tfrac12e^{-2t},\ \tfrac32+\tfrac12e^{-2t}\bigr).
\end{aligned}
\]
For every finite time, each agent selects the closer one of the opposite group's two **observed** opinions, and direct differentiation verifies the equation. These trajectories converge to the two distinct opinion clusters \(-3/2\) and \(3/2\), not to consensus. This shows that the unique-median hypothesis cannot simply be deleted from the universal selection claim.

## Verification

The standalone, standard-library-only program `verify.py` uses exact rational arithmetic. It reproduces the affine-median and differential identities for \(1{,}289\) admissible instances, including exhaustive small uniform odd-sized profiles and deterministic heterogeneous positive weights for part sizes through \(8\). It separately checks four exact rational times in the nonunique-median boundary example. Run with `python verify.py`; the expected completion message is `VERIFY_OK exact_cases=1289 boundary_cases=4`. Finite tests corroborate but do not replace the preceding proof for arbitrary finite networks and arbitrary real initial values.

## Relationship to prior work

Han, Chen, Dörfler, and Mei introduced this continuous-time weighted-median vector field in the first public release of arXiv:2404.16318 (April 25, 2024). Its convergence theorem and its subsequent revision establish general equilibrium, Lyapunov, and consensus criteria without this two-community **initial-condition-to-limit map** or its two closed-form transient modes. The present theorem is an explicit structured-network specialization that extracts the conserved median sum, the exact selection law, and the sharp rates. It does not claim novelty for the general well-posedness or convergence results.

The earlier asynchronous weighted-median process studied by Mei and collaborators is discrete-time and updates agents to selected opinions; its random update trajectory does not provide the continuous-time formula here. Mohr, Hjorth, and Porter analyze a distinct synchronous weighted-median updating model and a mean-field approximation. Equivalence with an unindexed result is a residual publication-priority risk; absence of a matching title is not proof of novelty.

## Limitations

All rows belonging to the same group must have identical cross-group weights; heterogeneous rows within a group are not covered. Strict uniqueness is imposed on each group's initial weighted median, and the \(K_{2,2}\) example shows why tie cases require separate treatment. No stochastic update process is being solved. Exponential rate \(2\) (respectively \(1\)) is an active decay mode only when the initial group medians differ (respectively at least one group has nonidentical initial opinions). The publication-priority assessment is best-knowledge and not an independent literature audit.

## References

- Yi Han, Ge Chen, Florian Dörfler, Wenjun Mei, *The Continuous-Time Weighted-Median Opinion Dynamics*, arXiv:2404.16318v1 (first public April 25, 2024). https://arxiv.org/html/2404.16318v1
- Yi Han, Julien M. Hendrickx, Ge Chen, Wenjun Mei, *Modeling, Analysis, and Control of Continuous-Time Weighted-Median Opinion Dynamics*, arXiv:2404.16318v3 (revision, November 26, 2025). https://arxiv.org/html/2404.16318v3
- Wenjun Mei and collaborators, *Convergence, Consensus and Dissensus in the Weighted-Median Opinion Dynamics*, arXiv:2212.08808 (2022). https://arxiv.org/abs/2212.08808
- Lasse Mohr, Poul G. Hjorth, Mason A. Porter, *Long-Time and Short-Time Dynamics in a Weighted-Median Opinion Model on Networks*, arXiv:2406.17552v3. https://arxiv.org/html/2406.17552v3
