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

The analytical proof is in `RESULT.md`. In this package, `verify.py` uses Python's exact rational arithmetic to check all three cell identities and the three-node noncancellation statement, then supplements them with finite numerical optimizer and sharp-bound tests. Execute `python3 verify.py` to reproduce the saved `verify_output.txt`. The program's actual result was `PASS: 7579 exact identities / finite-grid / asymptotic checks`. Finite tests are neither exhaustive over real grids nor independent validation; universal claims require the analytic proof.
