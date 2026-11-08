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

## Reproduction

Run `python verify.py` with Python 3.10 or later. It uses only the Python standard library. The program constructs the exact reset-interval law, calculates renewal masses, and independently updates the full age-state probability vector using the age-dependent reset hazard. The calculations compare parity and nontrivial complex phase observations at finite horizons. It checks the alternating-series eta amplitudes against computed coherence at selected large finite times.

At package creation, the script passed 936 finite diagnostic assertions over the parameters 0.25, 0.50 and 0.75. In the 0.75 case, the asymptotic leading term converges slowly because a subdominant oscillatory contribution is still visible, so the finite-time diagnostic is deliberately loose; the stated asymptotic limit is analytically proved, not certified numerically. No external or independent scientific audit is asserted.
