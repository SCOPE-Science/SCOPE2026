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

The independent, standard-library checker `checks/triangular_crossing_check.py` was executed from the package source in this session, with output `TRIANGULAR_LINE_CROSSING_THIRD_ORDER_RATIONAL_CHECK_OK 8 cases`. It computes eight complete rational phase-cell distributions by polygon clipping and checks the stated algebraic identities. It does not sample random points and has no external dependencies. The unrestricted theorem follows from the algebraic and geometric proof, not finite enumeration.

All end-point cases in the claim are covered analytically; the checker tests selected exact rational boundary cases. Historical novelty is not independently certified; the 1997 Pettineo full text was inaccessible. No external audit has been performed.
