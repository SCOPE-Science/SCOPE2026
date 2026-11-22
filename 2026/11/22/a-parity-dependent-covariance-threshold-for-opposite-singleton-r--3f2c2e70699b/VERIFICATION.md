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

The supplied `check.py` uses only Python's standard library. Execute `python3 check.py` to recompute exact word-enumeration covariances and expectations at selected rational probabilities, verify integer-size parity signs through length 12, and check deterministic bisection/asymptotic diagnostics. A successful replay reports 11,174 checks and the limiting constant. The infinite quantifiers, one-crossing theorem, and asymptotic scale are proved analytically in `RESULT.md`; finite checks do not independently establish them. No independent audit has been performed.
