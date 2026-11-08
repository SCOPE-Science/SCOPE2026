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

Run `python verify.py` in the same directory with SymPy installed. It uses an independently implemented stationary generator recurrence for mixed position–active-force moments through total degree six. It compares the resulting standardized fourth/sixth cumulants against the closed rational formulas, checks all derivative polynomial identities and the thermal-invariant ratio derivative, checks the exact endpoint polynomial evaluations, and performs 65 exact rational and interval-root checks.

The global assertions are proved by exact sign variations, positivity bounds, and comparison of logarithmic derivatives in `RESULT.md`. Finite computed roots only corroborate the formulas and illustrate parameter values; they cannot establish universal root uniqueness or the global strict ordering. The program does not produce an independent peer/expert audit.
