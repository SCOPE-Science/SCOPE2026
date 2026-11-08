# Scientific assessment

## Correctness — PASS
The theorem treats all symmetric nonnegative stochastic matrices with every internal clique edge fixed at the specified probability, not only matrices initially assumed invariant. Averaging over the graph's vertex-permutation group does not increase \(\|P-J\|_{\mathrm{op}}\) and preserves fixed entries. The three nontrivial eigenvalue formulas then give an exact interval feasibility problem. All lower-versus-upper endpoint comparisons have been included, including the nonnegativity of the upper endpoint, which contributes the branch \(st-1\). The seven-affine formula is both necessary and constructive. Exact-rational independent breakpoint minimization agrees in 3332 cases; 180 full matrices pass eigenspace tests; and 3001 points verify the four-piece example. Finite computation is supporting evidence, not the infinite-domain proof.

## Originality — PASS on inspected evidence, with residual risk
The 2004 convex SDP formulation contains the *optimization problem* but not this formula. The 2007 complete-bipartite closed form covers only the fixed-weight boundary \(t=0\). The 2020 clique-lifting theorem gives an unrestricted internal-clique optimum and is a strong comparison: the constrained optimum can be sharply worse, for instance \(3/5\) versus \(1/6\) for a five-core, two-leaf graph at zero fixed clique weight. The 2019 work explicitly studies fixed edge probabilities and a Pareto trade-off, but its friendship graph has a different adjacency structure and its formulas are not a covering result for the complete split graph. Relevant semantic research-record searches identified no covering claim. The remaining risk is uncatalogued specialist work; absence in indexed search does not establish priority.

## Mathematical value — PASS
Fixing mandatory peer-to-peer transition probabilities while optimizing all other network couplings is a natural constrained consensus and Markov-chain design problem. The closed-form frontier identifies when requiring additional core interaction improves, leaves unchanged, or damages mixing. The explicit four-regime example has exact breakpoints \(1/25\), \(1/10\), and \(1/6\), including a nontrivial optimal plateau. This is a global analytic constrained optimum for an infinite family, not a recomputation of one isolated graph or a mere reformulation of the unconstrained SDP.

## Limitations and comparison
The theorem concerns symmetric uniform-stationary chains only. Endpoints with isolated vertices have SLEM one and are included as spectral-design cases rather than mixing chains. It does not classify all possible noninvariant optimizers or establish independent literature priority. The exact proof applies to every integer \(s,m\ge2\) and every admissible real fixed weight, while computational checks sample finite rational cases.

Self-review: passed. Independent audit: not yet performed.
