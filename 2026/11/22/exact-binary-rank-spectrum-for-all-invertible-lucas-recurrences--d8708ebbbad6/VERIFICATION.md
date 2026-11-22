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

# Reproducibility

Run `python3 verify.py` alongside the other files. It calculates each Lucas recurrence from the initial state modulo every \(2^a\), for \(1\le a\le8\), and checks exact multiplicities against the symbolic formulas, examining 43,690 parameter pairs in total. This code does not substitute for the all-exponent valuation and counting proof in `RESULT.md`. The reported self-review is not independent validation.
