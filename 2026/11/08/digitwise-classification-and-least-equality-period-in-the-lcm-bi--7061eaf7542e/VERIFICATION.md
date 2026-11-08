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

The exact-integer checker `artifacts/verify.py` recomputes the original lcm/binomial expression for 11,786 input pairs and independently tests the digit criterion. It also enumerates accepted residues and rules out all proper-divisor candidate periods for 15 moderate columns. Diagnostic output begins `VERIFY_OK direct_lcm_binomial_comparisons=11786` and prints representative exact densities/periods.

This finite program is a corroboration, not an infinite proof. The unrestricted identity, exact least period, density, and decay estimate are justified in RESULT.md. An independent audit was not performed.
