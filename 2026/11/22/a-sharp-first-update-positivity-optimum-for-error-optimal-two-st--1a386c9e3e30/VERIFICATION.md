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

# Verification of the mathematical package

Run `python check.py` with Python 3.10 or later (no external packages). The execution produced `VERIFY_OK 101 exact-rational identities; 8,000 recurrence checks; 1,001 boundaries`. Rational tests verify normalization and order-two coefficient identities; floating-point diagnostics compare direct LMM recurrence against the derived numerator and bracket the sharp tangency constants. The analytic proof in `RESULT.md`, not the finite tests, supports uniqueness and the all-parameter sign conclusions.

The proof covers only a first-update positivity property for exact positive scalar-decay starting values. It does not establish positivity of further outputs, a general SSP coefficient or a property of nonlinear ODEs. Independent audit is not performed.
