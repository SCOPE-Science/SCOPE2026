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

# Reproducibility and verification

Run `python CHECK.py` from the directory containing the supplied files (Python 3 standard library only). The program executes exact rational signed-displacement tests, exact integer resultant-determinant checks, rational threshold examples, and numerical boundary spot checks, then reports the assertion count.

The universal mathematical conclusions are proved in RESULT.md. Finite diagnostic outputs do not certify every real parameter or every initial condition. One-season sigmoidal response, constant deterministic alternating coefficients, nonnegative initial population, and absence of environmental randomness are essential assumptions. The mathematical identity for the discriminant is also explicit in RESULT.md, permitting independent algebraic reconstruction.
