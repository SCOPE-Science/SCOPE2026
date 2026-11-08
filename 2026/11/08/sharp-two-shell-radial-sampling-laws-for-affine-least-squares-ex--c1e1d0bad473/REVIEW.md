# Scientific review: radial affine extrapolation

## Correctness

**PASS.** Rotation-invariant covariance gives the affine kernel exactly, without a smooth-density assumption. A direct density calculation establishes the derivative formulas for the spherical absolute-value kernel. The unique root is proved by the sign of the derivative of the tangency function. The resulting convex-to-concave envelope is an exact sharp concave majorant; Jensen's equality cases force each radial optimizer. The disk phase partition and dimension-three case follow algebraically. Finite computation checks representative envelopes and direct angular integrals, but the proof does not rely on finite search.

## Originality

**PASS, with literature risk.** The cited Piñar–Xu paper studies unit-ball orthogonal polynomial equations, Xu derives radial-weight reproducing kernels, and Figueroa proves weighted Sobolev approximation bounds. Those techniques provide antecedents for the kernel, not the moment-constrained optimization over arbitrary radial Borel laws. The closest general uniform-body affine projection norms and uniform-simplex norms do not imply a two-shell classification at fixed radial second moment. Searches also covered synonymous terms such as Lebesgue constants, least-squares radial design, affine extrapolation, fixed covariance and concave-envelope moment optimization. Equivalent unindexed optimal-design literature is a genuine unresolved possibility.

## Mathematical value

**PASS.** Projection stability depends on how sampling weight is distributed in radius, not solely on covariance. Fixing covariance makes the comparison mathematically nonvacuous. The theorem solves the resulting global distributional optimization, proves unique extremizers and exhibits two sharp, explicitly computable design changes in the disk. The full-ball output norm is essential for extrapolation beyond observed sampling shells.

## Limits

The measure must be rotation invariant, the fitted space affine, and the output measured uniformly over the entire ball. The literature comparison is not an independent audit and does not certify uniqueness of publication.

Self-review: passed. Independent audit: not yet performed.
