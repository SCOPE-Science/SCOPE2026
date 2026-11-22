# Scientific assessment: renewal cargo–interval coupling

## Correctness — PASS

For every admissible iid pair \((W,J)\), the defective per-particle target-arrival delay has eventual failure probability \(a\), and its success-after-age tail is bounded by \(e^{-du}\). Positive minimum separation between births bounds the total multiplicative influence of unfinished successful searches uniformly in observation time, giving the exact sandwich \(F(t)\le Q(t)\le CF(t)\). The tilted product \(M_n=e^{\theta S_n}a^{\sum_{i\le n}J_i}\) is a martingale because the full *joint* moment \(\mathbb E[e^{\theta W}a^J]\) equals one. The bounded first-overshoot stopping time yields matching exponential bounds and proves the limit. A two-by-two exchange proves rearrangement at each positive parameter, and monotonicity of the joint transform orders its unique roots. The Brownian diffusion–mortality success probability and the three algebraic two-point roots were checked independently. The package contains the complete proof and a standalone checker; finite tests do not stand in for the proof.

## Originality — PASS, with publication-priority uncertainty

The November 2026 synthesis–degradation source establishes Poisson births and independent burst sizes and does not establish optimal correlation between a *preceding* renewal waiting time and its burst size. The previously published renewal-production note gives a one-searcher renewal exponent and Jensen/convex-order comparisons over the **interval law**, but not the universal sharp maximum/minimum over **couplings of two fixed marginals**. The vesicle activation article considers concentration thresholds rather than first target arrival by any diffusing particle. The 2024 dependent renewal–reward article is the closest broad mathematical predecessor and may imply a joint-transform root, but its abstract discusses transforms and reward-threshold first passage, not the asserted sharp coupling-order physical result; its full text was not obtainable for complete inspection. No claim is made that classical renewal tilting or rearrangement is new. Closest literature raises a residual risk of an overlooked general rearrangement theorem formulated in another application.

## Value — PASS

Joint coupling is a physically meaningful scheduling degree of freedom in bursty synthesis: the interval distribution, burst distribution, average interval and average production flux can all remain fixed while the long-time probability of never triggering a target is changed sharply. For the smallest nontrivial binary margins, the best rate exceeds the worst by \(21.9319668\ldots\%\), and every intermediate coupling is bounded globally by two realized endpoints. This gives an exact, interpretable design boundary not supplied by marginal variability comparisons. The finding is not a claim of finite-time dominance or optimal mean encounter time.

## Closest coverage and limitations

The root in the one-searcher limit is previously known; novelty is assigned to the fixed-marginal **dependent burst–interval coupling envelope** and a measurable Brownian mortal-search realization. The classical dependent renewal–reward theory could provide an equivalent transform statement; the published abstract was inspected but not its inaccessible full proof. Assumptions of bounded iid pairs, independent particles and exponential mortality are essential to the stated simple uniform bounds. No exact prefactor, feedback-dependent process, or independent priority validation is claimed.

Self-review: passed. Independent audit: not yet performed.
