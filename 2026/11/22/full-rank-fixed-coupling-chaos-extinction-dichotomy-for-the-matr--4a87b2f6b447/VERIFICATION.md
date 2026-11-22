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

# Verification record

The analytic proof uses matrix functional calculus on \([0,1]\), the Loewner bound \(H(I-H)\preceq H\), a literal equality of two positive-definite coupling products, a two-step matrix order inequality, and the established logistic-map entropy result. These steps imply the full-time claims without any finite sampling.

Run `python3 checker.py` with Python's standard library from the exact contents of this package. It prints `FIXED_PD_COUPLING_EXACT_OK 1779` after checking the rational equalities and finite sample trajectories. The checker is supplementary; its finite tests are not certificates for statements over every initial state, every time, or real parameter. No independent audit has been performed.
