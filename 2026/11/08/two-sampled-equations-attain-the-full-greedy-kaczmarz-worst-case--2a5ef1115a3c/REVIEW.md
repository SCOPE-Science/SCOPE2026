# Self-review

**Claim:** Two sampled equations attain the full greedy Kaczmarz worst-case guarantee on regular-simplex frames. The exact sharp conditional one-step relative squared-error decrement on unit regular-simplex frames is \(1/n\) for all sample sizes in odd dimension; in even dimension it is \(1/n\) for one sampled row and \((n+1)/n^2\) for any sample size from two through \(n+1\).

## Correctness — PASS

The proof reduces sampled Kaczmarz energy loss to the order statistic of a zero-sum tight-frame analysis vector. The critical odd-cardinality inequality is established analytically, not inferred from enumeration. Both parities have exact realizing error vectors, and uniform random subset monotonicity covers all sample sizes. Exact-arithmetic verifier checks pass. Valid for all dimensions \(n\ge2\), all current nonzero errors, and uniformly sampled *distinct* rows; no multi-step or noisy assertion is made.

## Originality — PASS (qualified)

Closest literature: De Loera–Haddock–Needell, arXiv:1605.01418 (original sampling method, 2016), and Haddock–Ma, arXiv:1912.03544 (general sampled-greedy convergence bounds, first public December 7, 2019). These papers were checked at their definitions, theorems, and relevant specialization passages. Neither delivers the parity-separated exact one-step minimax law or the two-sample/full-greedy equality. The closest published coherence residual-spike analysis concerns total residual rather than squared error and was compared at its accessible record; inaccessible full text and older equivalent norm inequalities remain residual risks. See AUDIT.json for the actual four overlap comparisons and source inspections.

## Value — PASS

The exact degree of sampling needed before worst-case improvement saturates is an intrinsic design issue for sampled maximum-residual Kaczmarz. Two residual evaluations reach the same sharp one-step guarantee as evaluating all rows in the canonical minimally redundant tight frame, while the parity effect proves that in odd dimension further greediness has no worst-case benefit at all. This is a structural all-dimensional theorem, not an arbitrary fixed-size table.

## Limitations

One-step worst-case squared Euclidean error only; not equivalent trajectories or rates, not generic frames, and not inconsistent/noisy systems. Earlier equivalent work may remain outside accessible comparisons.

Self-review: passed. Independent audit: not yet performed.
