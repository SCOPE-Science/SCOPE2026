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

# Reproducibility and limits

Run `python3 verify.py` (Python standard library only). This independently computes all prefix palindromic lengths up to \(n=4096\) by center expansion, checks the first \(256\) by a separate interval-palindrome recurrence, and checks the exact constructive factorization, general bounds, dyadic predecessor values and canonical pair-block endpoints. Expected last line:

`VERIFY_OK prefixes= 4096 independent= 256 dyadic_scales= 10 claims_checked= 4113`

The proof's infinite claims follow from symbolic arguments in RESULT.md, not from extrapolation of the finite tests. No independent mathematical validation, proof assistant or external certification was performed.
