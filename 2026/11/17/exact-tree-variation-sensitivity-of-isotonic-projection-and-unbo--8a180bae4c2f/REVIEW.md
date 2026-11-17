# Scientific review: Exact tree-variation sensitivity of isotonic projection and unbounded cubic-branch amplification

## Correctness — PASS

The proof first identifies connected active blocks as local averaging operators and exhibits strict-complementarity witnesses realizing every connected partition. A tree cut-indicator decomposition turns each block-averaging operator norm into a finite boundary-count expression, and a finite branch-selection argument establishes the universal upper bound. Explicit witnesses establish matching lower bounds, not merely estimates. Rooted-tree knapsack computes the exact optimum. Direct combinatorial arguments establish the path, star and cubic-caterpillar cases. Exact rational tests and 1,504 KKT perturbation witnesses corroborate the universal reasoning; sampled trees alone are not proof.

## Originality — PASS, qualified

Németh–Németh (arXiv:1201.4677 and arXiv:1503.08458) concern isotonicity and order-cone structure. Yang–Barber (arXiv:1706.01852) establish seminorm contraction for chain isotonic regression, already covering the path-special case. Chen–Li–Su (arXiv:2304.00244) develop active-set algorithms for generalized tree problems, including graph-TV as a penalized objective; that is not a perturbation norm theorem. The closest published sharp \(\ell_p\) isotonic stability result measures vertex \(\ell_p\), rather than graph edge variation. None of those inspected claims implies the new cut-envelope and unbounded bounded-degree amplification. The original full text of Kolmogorov–Pock–Rolinek (2016) was not inspected; its abstract concerns a different TV-penalized optimization problem. The possibility of an unindexed earlier formulation using active-set methods remains a historical-priority limitation, not a demonstrated coverage result.

## Mathematical value — PASS

This gives a computable exact stability invariant for a natural nonlinear shape-restricted estimator on every oriented finite tree. The degree-three caterpillar law shows that branching topology, not merely maximum degree or local regularity, controls graph-variation sensitivity, and it quantifies a new instability regime while completely classifying the finite-tree constant.

## Limitations

Uniform vertex weights and Euclidean projection, arbitrary orientation of a finite tree, unweighted edge-total-variation seminorm, real signals. Graphs with cycles, nonuniform weights and other objectives remain outside the claim. Although every extremal connected cut has local norming pairs, a separate classification of all global maximizing pairs is not given. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
