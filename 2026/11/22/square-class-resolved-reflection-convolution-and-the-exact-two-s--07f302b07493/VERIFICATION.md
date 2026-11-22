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

# Verification details and limits

The proof uses Wall's established parametrization of isometries by nondegenerate bilinear forms on their moved spaces, the reflection-shortening theorem, and the spinor homomorphism. The additional calculations are the norm-square-class line census, the count of Wall parameters with nonzero determinant on ternary moved planes, and the exact total-variation summation. All parameters, including the degenerate moved-plane case and small odd fields, are explicit in `RESULT.md`.

Run the packaged Python 3 source `orthogonal_fibers_check.py` without external dependencies. The corresponding captured standard output is `checker_output.txt`. For each of ten selected prime-field and dimension combinations the program explicitly constructs all quadratic reflections, forms all ordered pairs, recovers the Wall spinor through linear algebra, checks the class-resolved predicted fibers, and where feasible generates the full orthogonal group to inspect zero fibers. For dimensions three it also checks each target-fiber multiplicity and the exact total-variation formula. Directly tested fields are prime fields of orders 3, 5, and 7. Finite tests do not certify results for all finite fields or all dimensions; the symbolic proof does that conditional on the cited standard Wall machinery.

No independent review or external formal proof certification has been performed. An arithmetic class-algebra priority comparison remains subject to discovery of additional historical character-theoretic computations.
