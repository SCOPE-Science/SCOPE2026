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

# Verification

The proof establishes the Loewner-sandwich reduction, invariant-subspace spectrum, monotonicity and exact clipping formulas. For the rational \(4\times4\) matrix in the example, a standalone checker verifies the polynomial identity at five points (degree four), its exact two-by-two quotient eigenvalues, and the predicted optimal condition number. It also generates 3,000 admissible synthetic parameter sets and tests 25 nearby scale choices in each set with floating-point arithmetic. The finite tests are not an exhaustive proof of optimality; the written analytic argument is necessary.

Run `python check_preconditioning.py` from the extracted package directory. This checker uses only the Python standard library. Scientific publication-precedence and generalizations outside positive two-community compound-symmetry matrices are not independently verified.
