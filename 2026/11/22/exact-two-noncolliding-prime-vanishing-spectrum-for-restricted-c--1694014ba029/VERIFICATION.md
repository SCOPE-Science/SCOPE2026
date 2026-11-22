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

# Reproduction and scope

Run `python3 verify.py` alongside `small_support_certificate.csv`. The checker recomputes all 207 rows using prime divisibility, exact integer GCDs, and exhaustive unordered prime-pair masks; compares every numeric column; checks the 8/109/82/8 split by colliding count; and directly evaluates the five witness products. It prints `RESTRICTED_COPRIME_J2_OK` on success.

The published infinite necessary bounds are taken from Salazar, arXiv:2611.10059v1, Theorem 4.9. The verifier does not prove these analytic inequalities or certify priority against inaccessible literature. No independent mathematical audit has been performed.
