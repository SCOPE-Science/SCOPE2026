# Scientific review

## Correctness — PASS

The claimed distribution is verified by a bijection from a uniformly sampled row-label string to the independent switch-indicator string and the exact cosine factor of two one-dimensional orthogonal projections. Conditional expectation makes the mean-normalized squared error a unit-mean martingale; the strong law proves decay to zero. At first passage, bounded optional stopping gives the exact expected terminal payoff, not merely a bound. Positive-probability all-up and one-down-then-up paths force a lattice ratio, while the skip-free upward jump proves sufficiency. Strict convexity gives exactly one nonunit algebraic root for every integer parameter. The extracted verifier checks finite special cases and exact algebra, but the proof alone establishes the infinite-horizon result.

## Originality — PASS, qualified

The closest source [1] gives a time-uniform Kaczmarz high-probability inequality and a general repeated-row lower bound; it does not determine the entire exact crossing law for this two-row construction or classify equality angles. The generic zero-overshoot criterion and its martingale proof are established prior theory, especially [2]; these are acknowledged and not claimed as new. The scientifically distinct step is the complete parameterized Kaczmarz realization, its exact binomial path law, and the necessity-and-sufficiency classification of the lattice angles. Relevant published records on deterministic/cyclic two-row overrelaxation concern different iteration laws, not iid row sampling and infinite-horizon concentration. A possible unindexed special-case treatment in earlier projection or gambler's-ruin literature is a residual historical-priority risk.

## Value — PASS

The motivating time-uniform guarantee raises a concrete sharpness question for stochastic numerical solvers: is the usual reciprocal-confidence loss actually attained by an algebraically elementary, nonsingular randomized linear-system solver? This finding answers that question exactly at the natural conditional-mean contraction rate, and classifies every two-row angle and confidence threshold at which equality is possible. The complete staircase law is a benchmark for interpreting time-uniform error certificates; it also prevents an unsupported universal tightening of the reciprocal-confidence factor in this instance-specific class. This is not a claim of sharpness for the different general operator-norm rate in [1].

## Closest literature and limitations

[1] T. Anderson et al., *Beyond Expectation: Concentration Inequalities for Randomized Iterative Methods*, arXiv:2511.20877v1, Sections 2.2–2.3, https://arxiv.org/html/2511.20877.

[2] S. R. Howard et al., *Time-uniform Chernoff bounds via nonnegative supermartingales*, arXiv:1808.03204, Section 5.1 and Proposition 3, https://arxiv.org/html/1808.03204v8.

[3] W. Koolen-Wijkstra et al., *A generalisation of Ville's inequality to monotonic lower bounds and thresholds*, https://doi.org/10.1016/j.spl.2025.110577, Sections 2.1–2.2 were inspected: general floor-hugging martingale sharpness, without a two-row Kaczmarz construction or an angle-equality classification. Its general existence theorem is acknowledged, not attributed as a new result here.

The result is restricted to exact orthogonal projections on a two-equation consistent system, uniform iid sampling, and one initial vector. It is not a statement about a general-dimensional worst-case contraction rate.

Self-review: passed. Independent audit: not yet performed.
