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

Run `python verify.py` with Python 3 (standard library only). The result is `VERIFIED checks= 6557`. The script checks finite exact Bernoulli path enumerations and exact benchmark inequalities; general statements in RESULT.md require the independently written algebraic, contraction and cylinder-dimension arguments there. No external proof assistant or certification is claimed.

Limits: every finite enumeration has a specified horizon. The general continuous-parameter uniqueness, all-step mean identity and infinite invariant measure are proved analytically, not inferred from computations. Independent scientific audit has not been performed.
