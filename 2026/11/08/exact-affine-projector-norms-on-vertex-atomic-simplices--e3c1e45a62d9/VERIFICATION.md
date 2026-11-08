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
# Reproducibility and verification boundaries

Run `python checker.py` with Python 3 and no external packages. It checks exact rational Gram inversion for 24 weighted examples with \(2\le m\le7\), constant reproduction and kernel signs, plus separately implemented rational integration of the continuous positive kernel on the segment and triangle. It verifies exact single-atom identities for \(2\le m\le14\) at five rational atom weights per dimension and tests strict inequalities at positive weights. Expected final line: `ALL_SIMPLEX_ATOMIC_PROJECTION_CHECKS_PASSED`.

The universal result follows from the inverse-Gram identity, simple geometric cap-volume integration, strict sign mismatch between vertex kernels, and an elementary derivative calculation. The checker neither proves uniqueness of a bibliographic result nor replaces a universal proof. The arbitrary-weight norming indices are determined by evaluating the stated finite formula, not by an unproved sorting conjecture. Independent mathematical verification has not been performed.
