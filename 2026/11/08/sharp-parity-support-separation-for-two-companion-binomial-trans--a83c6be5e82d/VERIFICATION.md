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

# Verification notes

The package includes `checker.py` (Python 3 standard library only) and its actual `checker-output.txt`. To rerun, execute `python3 checker.py` from the directory containing those files; a successful execution ends in `CHECKER_OK`. No external libraries or network are needed.

The checker reconstructs the underlying recurrence parity for 64 indices per transform, checks all 1024 arguments below \(2^{10}\) directly from binomial coefficients by Lucas's bitwise criterion, and independently enumerates every binary word up to 14 digits to compare with the exact rational-series recurrences. It checks strict support inclusion for all arguments below \(2^{15}\), as well as the witness \(n=1\). It approximates the unique positive polynomial roots and their analytic leading constants and checks their agreement with length-24 counts.

Finite tests do not prove the infinite claim. The proof separately establishes exact period five, the unique run decomposition, both generating functions, uniqueness and simplicity of each dominant pole, and the passage from dyadic asymptotics to all cutoffs. No external audit or formal proof certification is claimed.
