# Self-review

**Finding:** Exact-oracle tie-breaking creates an unbounded one-step distance transient under gradient-radius initialization.

## Correctness — PASS

The domain, exact local linear minimization objective, gradient-radius initializer and clipped short-step agree with the primary algorithm. The nontied KKT multipliers are nonnegative and the tangential slope enforces uniqueness; substituting the resulting oracle into the accepted step proves the squared-distance expression and the strict sharp bound \(R<2\). In the tied case, all exact oracle points lie on one vertical feasible disk section. The clipped rational step has two monotone branches, giving the claimed complete piecewise maximum, minimum and the fixed-objective amplification family. The argument covers the stated boundaries \(a=0\), \(a=p\), and the one-sided nontied limit. Finite checks are supporting evidence only.

## Originality — PASS (with residual risks)

The closest primary comparison is Kolzenburg--Richtárik, arXiv:2611.11354v1, which supplies the exact short-step algorithm and objective convergence, but not this first-step point-error sharp classification. The earlier exact local-oracle Fejér bounds of arXiv:2605.08850 and arXiv:2609.33383 require controlled admissible/Polyak radii, unlike the default gradient radius used here. The earlier negative distance construction with a relaxed oracle does not logically imply the exact-oracle tied-face result. Scientific record searches and full accessible primary-text comparisons did not locate the particular formula or fixed-problem discontinuity. Older implicit equivalences and incompletely accessible related records remain real priority risks; a failed search is not a novelty certificate.

## Value — PASS

The result separates objective convergence from one-step solution-distance stability under the *actual default initialization* and *exact* oracle hypothesis. For a fixed, unit-conditioned strongly convex quadratic, two valid exact tie choices can respectively land at the optimizer or send the point error arbitrarily many times farther away, even while objective error contracts; the nontied case is sharply capped at squared factor two. This is a precise boundary for selecting exact local linear minimizers and interpreting point-error diagnostics, not an arbitrary parameter-table computation.

## Scope and remaining limitations

The proof concerns only one update on the given halfspace and quadratic family. It does not imply failure of eventual convergence or quantify floating-point tie perturbations. A mathematical priority review beyond the inspected primary literature and accessible research records is still desirable; no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
