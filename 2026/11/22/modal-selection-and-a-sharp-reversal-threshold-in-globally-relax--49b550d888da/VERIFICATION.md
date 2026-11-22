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

Run `python verify.py` with Python 3 and the standard library only. Expected stdout: `VERIFY_OK 127 checks`. The source `verify.py` is embedded in this package, independent of the historical files. It checks the explicit RK4 algebra in rational arithmetic and cross-validates the modal energy map against a directly evaluated four-stage RK4 step on complex oscillator coordinates. It also samples long-time trajectories on either side of the sharp threshold.

The mathematical certificate is the proof in `RESULT.md`: positive nonzero relaxation coefficient, exact energy recursion, strict weighted Lyapunov identity, bounded-monotone selection argument and opposite-sign quadratic threshold. These prove claims for all finite mode counts and all steps within the stated range; the numerical checks are finite examples and do not constitute exhaustive certification. No independent mathematical audit has been conducted. Public source precedence and novelty are qualified as in `REVIEW.md`.
