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
# Verification and reproducibility

The claim is established analytically in RESULT.md. Run `python3 verify.py` with Python 3.8 or later; no external libraries are needed. It compares the exact sample-to-sample complex multiplier with its trigonometric squared norm, computes intersections of stabilization windows directly in the sampling-period coordinate, checks the piecewise beat limit and sharp minimizer, and checks long-horizon irrational averages. `verification_output.txt` records the corresponding execution. Finite numerical tests have floating-point rounding and cannot certify statements quantified over all positive horizons or detunings. The proof's averaging error and global minimization are self-contained in RESULT.md. Independent audit has not been performed.
