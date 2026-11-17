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

# Verification of analytic cut reduction

The standalone `checker.py` performs exhaustive full binary-cut tests for \(1\le m\le7\) using exact fractions. It also enumerates all distinct pair-count orbits through \(m=100\), confirms the cut identity, exact bound, and strict increasing family coefficients. It is not an infinite proof. The analytic proof in RESULT.md covers all integers and arbitrary real signals.

No independent audit has been performed.
