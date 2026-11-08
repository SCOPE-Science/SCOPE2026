# Scientific review

## Correctness

**PASS.** Exact expansion reduces the ETDRK2 update to a scalar multiplier, and elementary inequalities show that the output magnitude is no smaller than its input for nonnegative starts. A finite rational certificate proves the complementary inequality that the sum of the squared input and output does not exceed two. The accompanying standard-library checker constructs the polynomial and verifies 729 Bernstein coefficients exactly; the smallest is \(1/8\). The original-energy factorization then gives dissipation. Conversely, the derivative at the well equilibrium exceeds one for a sufficiently large step whenever the stabilization parameter is below one; nearby interior initial data gain energy. The proof does not rely on numerical trials.

## Originality

**PASS, with stated historical risk.** The October 2026 study addresses general conditional energy dissipation and references earlier stabilized ETDRK2. The inspected 2024 primary full text provides the classical recurrence and sufficient generic conditions, not the exact scalar if-and-only-if stabilization constant. Searches for the exact scalar statement and corresponding aliases revealed no equivalent or dominating result. A highly relevant 2022 predecessor could be assessed at abstract and later-literature level, but its full text could not be inspected. This limits historical-priority certainty; no claim of exhaustive uniqueness is made.

## Value

**PASS.** The threshold is a genuine method-selection boundary for a named numerical integrator on the canonical quartic gradient flow. It is not a substitution into a known theorem: its sufficiency needs a nonlinear exact certificate, and its necessity distinguishes bounded-step behavior from arbitrary-step behavior. The overshoot example also separates one-step energy descent from interval preservation, preventing an incorrect full-trajectory inference.

## Scientific limitations

Only the scalar, untruncated reaction equation and one step with input in \([-1,1]\) are proved. Other phase-field models and spatially coupled methods are not covered. Full historical priority against an inaccessible 2022 predecessor is not established. Numerical experiments alone do not prove the theorem.

Self-review: passed. Independent audit: not yet performed.
