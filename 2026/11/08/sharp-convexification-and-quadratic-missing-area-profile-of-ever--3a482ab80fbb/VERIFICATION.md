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
Run `python3 trapezoid_convexification_verify.py` with Python 3 (no external packages). Expected output is `EXACT_RATIONAL_OK 39919`. The verifier computes actual membership by enumerating the four homothetic vertex translates and testing the remaining point against the inequalities of the normalized trapezoid, then compares that independent membership with the analytical gap criterion. It also verifies rational sharpness witnesses and the algebraic area identity.

# Limits of computation
A deterministic finite grid and a finite list of rational shapes do not certify the result for all real base ratios or all real dilation parameters. The universal argument is the full horizontal-section proof in `RESULT.md`. No external proof assistant, independent reviewer, or third-party certification is claimed.
