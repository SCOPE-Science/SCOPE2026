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

The full symbolic second-moment closure was evaluated with SymPy and compared against independently generated generator identities. The polynomial identities for pair covariances hold for symbolic parameters; rational test cases for sizes 3–5 and refresh rates 1/2, 3/2, and 6 pass.

Run `python verify.py` with SymPy to reproduce the general algebraic checks. Infinite-size signs and limits are mathematical deductions in RESULT.md, not based on finite enumeration. Independent external audit has not been conducted.
