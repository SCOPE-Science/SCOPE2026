---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification record

The result is proved analytically in `RESULT.md`. The essential norm equals the tail limit of the scalar norms, by finite-rank truncation and weakly null coordinate norming witnesses. The exact essential-maximal set follows from a compact-space probability-measure concentration argument. Its reverse inclusion requires selecting pairwise distinct remote coordinate indices to realize finite convex combinations. The scalar equality case also handles a vanishing complex-linear part, producing an entire circle. A strict convexity argument recovers the essential-maximal set by taking the convex hull of points of the ordinary essential numerical range on the essential-norm circle. A separate cluster-set realization establishes sufficiency for **every** nonempty compact subset of the essential-norm circle.

Reproducible diagnostic: run `python3 verify_examples.py` from this directory. It tests 3,000 seeded random nondegenerate complex scalar norming equalities and five exact rational perturbation identities, printing a PASS line or raising an assertion. The test was executed successfully in the package source directory. These finite diagnostics are not evidence of completeness of infinite-dimensional limits.

The essential-norm-zero case gives the singleton range. All compact convex sets are treated with the usual Euclidean Hausdorff metric. The standard diagonal example has essential norm one, ordinary essential numerical range a continuously varying disk, and essential-maximal numerical range jumping between a singleton and the closed unit disk. No independent external audit, numerical certification of an infinite claim, or universal result for nondiagonal operators is asserted.
