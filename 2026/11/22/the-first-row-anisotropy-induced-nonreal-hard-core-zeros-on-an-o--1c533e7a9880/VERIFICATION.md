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

# Reproducibility and scope

Run `python verify.py` with Python 3 and SymPy 1.10 or newer. Expected terminal line: `ALL_EXACT_CHECKS_PASSED`.

The script counts legal configurations directly for five open ladder lengths at four exact positive rational row ratios, verifies polynomial identities through length five, proves the displayed algebraic discriminant identities by exact symbolic equality, checks the Descartes polynomial and exact rational sign brackets, and computes a nonproof numerical approximation to the unique critical ratio.

The all-positive-ratio theorem follows analytically from the discriminant signs, Descartes' rule and real-root continuity in `RESULT.md`. The finite rational sample cannot itself verify every real parameter. No external audit or formal proof-assistant validation is claimed.
