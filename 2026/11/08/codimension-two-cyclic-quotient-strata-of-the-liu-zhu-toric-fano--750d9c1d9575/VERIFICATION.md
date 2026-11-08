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

Run `python CHECK.py` in a Python 3 environment without third-party modules. The verifier uses exact integer arithmetic. It enumerates edges from active facets for dimensions \(3\) through \(9\), verifies that all edges fall into precisely the two asserted classes, checks the saturating two-row minors and their gcds, and checks the HJ fractions and quotient ages.

The observed terminal line was `ALL_FAN_EDGE_AND_QUOTIENT_CHECKS_OK`.

The all-dimensional proof is symbolic and is given in `RESULT.md`. Finite enumerations are supplementary checks; they do not prove the universal statement. Full-text priority comparison for the later Wu preprint was not possible. No independent audit or external validation has been carried out.
