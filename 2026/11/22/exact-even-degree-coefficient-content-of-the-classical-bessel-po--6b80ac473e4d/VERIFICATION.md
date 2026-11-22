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

# Verification and limits

The proof uses a coefficient identity, Legendre's factorial valuation formula, and Lucas's binary no-carry criterion. These establish every prime valuation of the gcd for all integers \(n\ge2\). There are no inferred infinite conclusions from finite computation.

Run `python3 CHECK.py` from the directory containing the standalone checker. The exact-integer checker was executed successfully and returned `PASS: 34000 exact assertions; n=2..256, all coefficients via independent recurrence.` The independent verification status remains not performed; the checks recorded here are mathematical and computational reproducibility checks for the claim itself.
