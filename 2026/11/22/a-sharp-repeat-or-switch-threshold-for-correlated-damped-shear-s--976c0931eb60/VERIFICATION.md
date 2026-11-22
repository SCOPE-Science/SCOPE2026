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

# Reproducibility

Run `python verify.py` with Python 3.9 or later; no third-party dependencies are used. The script recomputes pair matrix products using exact rational arithmetic and verifies the two scalar second-moment identities over eight rational shear strengths, five rational repeat probabilities, and all three-block outcomes for three rational starting vectors. The observed output was `VERIFICATION_OK 440 rational identities and block tests`.

The exact argument in `RESULT.md` is the evidence for all real parameters and all positive block counts. The script does not certify historical novelty, infinite parameter ranges, almost-sure stability, or accuracy against the exact deterministic flow. Positive damping is an exact scalar factor and is not numerically approximated in the rational matrix checks; two strict stability witnesses follow from elementary rational bounds on \(e\).
