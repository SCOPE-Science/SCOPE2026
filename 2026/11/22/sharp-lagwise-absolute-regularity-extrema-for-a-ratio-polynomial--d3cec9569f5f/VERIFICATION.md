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

The accompanying checker can be executed with Python 3 and SymPy using `python check_beta_envelope.py`. It checks exact algebraic identities, the rational boundary and strict comparison inequalities, and finite numerical sanity tests for selected lags. The mathematical proof separately establishes all real admissible parameters and every positive integer lag, including the unique maximizers and the limiting envelope. The finite tests are supporting evidence rather than an exhaustive or independent proof.
