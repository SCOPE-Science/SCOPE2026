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

Run `python check.py` with Python 3, SciPy, and SymPy installed. It checks mass balance and the exact quotient derivative, exact rational initial-rate and limiting-sign inequalities, and numerical trajectory conservation, one sampled derivative sign change and limiting root consistency. Those numerical checks do not prove all-time uniqueness; the moving-nullcline crossing argument in RESULT.md supplies the proof. No independently commissioned or externally certified audit has been performed.
