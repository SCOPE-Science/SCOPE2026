# Self-review

## Correctness — PASS
The complete proof defines the stopped discrete sample and auxiliary exponential variables with correct rates. Independent marked-type Poissonization establishes both exact terminal frequency and time-weighted moments. The strict log-convexity of positive unbounded exponential-sum moments proves exactly one frequency sign transition, allowing a zero at its boundary. A gamma-ratio moment-generating function and uniform integrability under growing polynomial size-biasing prove the \(\log n\) transition. The exact-rational stopped-occupancy checker independently reproduces the finite identities for all \(2\le n\le8\), \(1\le r\le6\). The finite checks do not replace the analytic argument.

## Originality — PASS, qualified
The closest prior work of Myers–Wilf (2003) explicitly establishes the joint completion-time/singleton law: the \(r=1\) specialization is therefore already implied and is not asserted novel. Doumas–Papanicolaou (2014) establishes means of cumulative deficits indexed by siblings, and Long (2026) proves mixed-moment limits among fixed-index deficits and exact Poissonization formulas. Neither examined material contains the complete mixed completion-time-by-exact-multiplicity sign profile or the moving logarithmic threshold. published-finding corpus semantic searches for aliases and closely related models produced static-occupancy and set-partition sign-switch findings, but not the stopped coupon-collection theorem. Historical generating-function coverage is a real residual risk, not disproved by search.

## Value — PASS
This identifies a natural full-sample dependence profile between the time to complete a uniform collection and the exact multiplicity spectrum at that stopping time. The sign reversal at \(r\sim\log n\) distinguishes rare low-frequency types from heavily repeated types and is a motivated structural asymptotic boundary, not an arbitrary finite parameter slice. It is useful for interpreting stopped occupancy vectors and for comparison to sibling-coupon statistics.

## Closest sources and limitations
- Myers–Wilf (2003), arXiv:math/0304229, section 4: joint completion time versus singletons; already covers \(r=1\).
- Doumas–Papanicolaou (2014), arXiv:1412.4346, sections 1–2: mean terminal sibling deficits; no explicit mixed completion-time covariance in inspected material.
- Long (2026), arXiv:2606.29635, sections 1, 2 and 6: Poissonization, fixed-index joint limits of sibling deficits; the moving-index completion-time covariance is a different assertion.

No nonuniform-coupon extension, variance-normalized correlation limit, or additive constant for the threshold is proved. The possibility of an implicit equivalent statement in older multivariate generating functions remains.

Self-review: passed. Independent audit: not yet performed.
