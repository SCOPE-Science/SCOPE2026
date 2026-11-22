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

# Reproducibility and evidence boundaries

The theorem uses exact scalar flow primitives and the proven single-hump displacement sign. The critical expressions are unique implicit roots, not numerical conjectures. Run `python verify.py` from this package directory under Python 3. Only the standard library is required; the reviewed execution returned `VERIFY_OK assertions= 2331`.

The checker computes exact-flow numeric evaluations by bisection, verifies the sign equivalence for representative parameter points, and checks the phase-boundary claim across 450 seeded random admissible configurations. Finite tests do not establish existence, uniqueness or originality; those claims are supported by the analytic proof and literature comparison in RESULT.md, and independent scientific validation has not been performed. The underlying model has idealized continuous lateral loading and need not fit measured water-quality responses.
