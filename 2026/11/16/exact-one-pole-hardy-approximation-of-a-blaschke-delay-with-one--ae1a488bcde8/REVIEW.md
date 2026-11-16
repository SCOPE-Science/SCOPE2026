# Scientific review

## Correctness — PASS

The exact Hilbert projection is onto an orthogonal two-vector space and equals a single complex-parameter objective. The Möbius modulus has a strictly preferred antipodal angle when the displaced zero is nonzero. Its radial logarithmic derivative is strictly decreasing across the entire disk, with opposite endpoint signs, so it has a unique global maximum. All coefficients and endpoints are computed with explicit normalization. Implicit differentiation gives both parameter monotonicities; the analytic implicit-function expansion produces the sharp two-term capture law. The packaged finite checker independently tests exact formulas and candidate optimization samples but is not treated as an infinite certificate.

## Originality — PASS relative to inspected evidence

The inspected full-text passages of the motivating paper (Baratchart et al., arXiv:2603.16295, especially sections 4–6) supplies general lower bounds, an optimization framework, and numerical tests, but not the globally exact displaced-zero one-pole solution, unique pole geometry, monotonicity, or two-term asymptotic. Wang–Qian, arXiv:2012.06184, sections 1 and 2.1, supplies general kernel projection and existence, so those tools are explicitly treated as prior work rather than claimed innovations. Related one-state model reduction literature supplies general critical-point conditions, but no inspected result implies the precise antipodal maximization and explicit family law. Semantic-index searches covered one-pole approximation, Blaschke shifts, pure delays and model reduction; no matching stronger theorem was found. This is evidence of relative originality, not proof of universal publication priority.

## Mathematical value — PASS

A one-state stable rational model of a nearly pure delay is a basic and motivated approximation benchmark. The explicit solution gives the exact global performance, a unique geometric pole-placement rule despite complex degrees of freedom, strict sensitivity to a displaced Blaschke zero, and the optimal \(1/(eN)\) capture law with displacement-sensitive correction. The recent lower-bound paper explicitly highlights the difficulty of exact approximant computation. The derived finite-degree solution can calibrate approximate optimization algorithms and lower-bound quality; it is not merely a reparametrization of an already tabulated constant.

## Closest work and residual risks

The existence/variational structure is classical; the precise family-specific global optimization is the contribution. An equivalent unpublished or older special-case computation in rational system identification remains plausible. The result is restricted to a single movable zero, type-(1,1) stable rationals and scalar Hardy norm; its asymptotic is at fixed displacement. No human or independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
