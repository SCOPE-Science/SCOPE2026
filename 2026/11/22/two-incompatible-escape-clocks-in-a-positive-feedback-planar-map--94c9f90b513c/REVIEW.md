# Self-review

## Correctness (PASS)

The global bound is obtained directly from the relation \(y_{n+1}+r y_n=cx_n\) with \(r=5/4\), a triangle inequality and the product expansion. Every parity then satisfies a divergent quadratic lower recurrence, proving actual infinite-time escape, not just sampled growth. An invariant-probability argument follows using compactly supported test functions. At \(a=r\) the explicitly invariant cone has an exact two-step factorization for its vertical coordinate, and both the boundary quadratic recurrence and the interior Fibonacci recurrence have analytic positive finite normalized logarithmic limits. The separate exact rational checker passed 472 cases; it corroborates identities but does not replace the analytic proof.

## Originality (PASS, within inspected evidence)

The full accessible text of Zhou et al. (2021), equation (1), sections 2–6, establishes the model, fixed-point formulas, numerical dynamics and amplitude control, but does not present the sharp all-orbit escape theorem or either asymptotic clock. The source's fixed-point existence condition alone is weaker than an all-initial-state escape classification. The positive-feedback parameters printed in Figure 10(b) provide a concrete motivation for distinguishing the formula-defined map from numerical illustrations; the theorem does not infer what implementation generated that figure. The published published-finding corpus records found under the actual searches concern other planar absolute-value maps, even-degree secant models, and different escape thresholds; none imply this exact two-clock statement. Silverman's algebraic canonical-height framework is a general conceptual comparator, not a statement giving these real nonsmooth boundary and interior dynamics. An unindexed or uninspected stronger general orbit-growth theorem remains a publication-priority risk.

## Mathematical value (PASS)

The problem is natural for the original family: the sign of the multiplicative feedback determines whether nonzero fixed points can coexist with unbounded growth, while the linear gain equality \(a=r\) produces invariant boundary rays. The theorem identifies the sharp global escape boundary, a quantitative universal growth floor, and two rigorously different superexponential orbital scales in one parameter regime. It therefore gives structural information unavailable from finite Lyapunov or bifurcation plots, without claiming a general negative-feedback classification.

## Limits and literature

The theorem is real, forward-time, and exact on the stated parameter region; cone-specific asymptotics do not extend automatically to arbitrary initial points. Primary-source full text was inspected and the closest indexed records compared by implication. General orbit-height work may require a later independent priority assessment.

Self-review: passed. Independent audit: not yet performed.
