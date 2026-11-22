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

The embedded `check.py` script was executed with Python 3. It checked the exact polynomial factorization at 494 consecutive indices; tested the three polynomial branch maps as permutations modulo powers two through exponent nine; and exhaustively enumerated every target and checked periodicity and half-period failure for exponents one through eleven. All assertions passed. The full theorem is justified by an all-level argument in `RESULT.md`, not by the finite tests. No independent audit has been conducted.
