# Mathematical review

## Correctness — PASS

For each differentiability point \(z\) of the finite convex function with \(p=f'(z)
e0\), the exact semigroup identity at \(x=z+(s+t)p\) gives \(p\in\partial f(z+sp)\) for all \(s>0\). This forces every positive slope to persist on the whole right ray, and every negative slope on the left ray. Monotonicity of scalar subgradients then yields only a negative affine ray, a possibly degenerate zero-slope interval, and a positive affine ray, or one globally affine slope. Conversely, direct clipped-translation formulas prove the identity for all permitted penalties, including zero coefficients and time zero. An independent branchwise computation of the kink proximal map establishes the signed and absolute defects; the sharp witnesses are \(x=tb\) for strictly positive slopes and \(x=ta\) for strictly negative slopes. All parameter quantifiers and boundary cases are included. The standalone standard-library verifier supplied with the result passed 16,529 exact-rational checks; these finite checks are supplementary.

## Originality — PASS, qualified

Relevant literature comparisons focus on implication, not title. Bungert–Burger–Chambolle–Novaga (arXiv:1901.06979, Section 4.2, Theorem 4.5) provide sufficient one-homogeneous gradient-flow/variational equivalence conditions; the scalar theorem here is a necessary-and-sufficient classification over all finite convex functions without a homogeneity hypothesis. Planiden–Wang (arXiv:1909.05795, Corollary 4.11) describe proximal operators of piecewise cubic scalar functions but do not identify the exact all-time semigroup subclass or an optimized one-kink composition defect in the materially inspected sections. Combettes (arXiv:2209.06200, introduction) concerns a linear-map-based proximal-composition operation, distinct from step-parameter addition. These comparisons support an original formulation and derivation within the examined material. Historical priority is not certified: an equivalent older scalar monotone-resolvent classification might exist under unfamiliar indexing, and limited inspection of some sources cannot exclude every appendix or unstated corollary.

## Mathematical value — PASS

The exact time-additivity issue determines whether sequential quadratic proximal regularization and a single combined regularization have identical trajectories. The full scalar convex classification isolates the only admissible functional geometry, and the sharp nonminimizing-kink defect measures precisely how failure arises even for a basic two-slope nonsmooth convex loss. This is a structural boundary with a measurable obstruction, not a routine perturbation of a previously tabulated coefficient. Its limits are scalar and finite-valued.

## Verification and limits

The complete proof and piecewise formulas appear in RESULT.md. `verify_scalar_prox.py` can be run with Python 3 and no dependencies; a successful replay reports 16,529 exact-rational checks. Exhaustive mathematical quantifiers are established in the proof, not by enumeration. The checked source sections and historical-priority risks are identified above and in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
