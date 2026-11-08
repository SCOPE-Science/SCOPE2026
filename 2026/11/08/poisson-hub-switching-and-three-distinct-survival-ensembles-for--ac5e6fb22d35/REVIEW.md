# Mathematical review: Poisson hub switching on stars

## Correctness

PASS. Every full collision-free state is in one of the two hub classes. A rate-one star walk has exactly \(k\) safe class-A exits and \(r=(n-k)/(n-1)\) safe class-B exits, with killing rate \(k-r\) in B. The exact killed generator gives the stated hyperbolic survival functions. The positive function \(h(A)=\sqrt k\), \(h(B)=\sqrt r\) solves the full killed generator eigenvalue equation, and its Doob transform has precisely equal rate \(s=\sqrt{kr}\) in both directions. Distinct conditioning protocols then produce the advertised stationary/terminal probabilities. The exhaustive small-graph checker verifies the key equations on actual labelled state spaces; the analytic argument proves all sizes.

## Originality

PASS under the available comparisons, with residual priority risk. The 2026 Shiatis article establishes the broad h-transform representation and gives explicit cycle and line examples, not the star-specific eigenvalue, Poisson hub-switching process, or exact separation of the three hub laws. Primary-text inspection and targeted searches did not identify a dominating star-specific theorem. Generic finite-state quasistationarity and the use of Doob transforms are prior methods; the claim is limited to the concrete solved family. The readily computable two-class reduction means priority could still be implicit in unpublished or unindexed examples.

## Value

PASS. Stars are the canonical extreme-bottleneck graphs where independent walkers often collide at a single hub. Exact full-parameter characterization of collision survival and three distinct conditional hub laws is motivated by the difference between suppressing and conditioning collisions: the never-collide process has *Poisson* hub transitions and exactly one-half stationary hub occupancy, whereas exclusion produces alternating unequal waiting rates and a hub occupation tending to one in dense particle regimes. The separation can approach one-half in total variation on a directly observable statistic. This is not a reparameterization of a one-particle walk or a numerical special case.

## Coverage and limitations

Compared with R. Shiatis, *Exclusion vs Noncolliding dynamics in Markov processes* (arXiv:2610.00741v1), Section 1.1–1.4 and the Section 2 conditioning formulation; Darroch–Seneta (1967) supplies classical finite-state quasi-stationarity background. The general conditioning theorem is acknowledged. Claim scope is restricted to a star, equal rate-one walkers, \(2\le k<n\), and projected hub observables. The full labelled process can be reducible when \(k=n-1\). Historical priority remains potentially incomplete.

Self-review: passed. Independent audit: not yet performed.
