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

Run `python verify.py` in this directory with SymPy installed. The checker recomputes the complete short-relation matrix and compares it against the embedded integer certificate, computes exact Smith normal form and ranks modulo 3 and 101, tests parameter-pattern equality for 7 sample parameters, checks the 13 one-step omissions, and verifies the distinct t=93 boundary example. The proof covers all parameters by disjoint interval inequalities and an integral chain-homotopy comparison; finite tests are corroborative, not the infinite proof. No independent mathematical audit has been performed.
