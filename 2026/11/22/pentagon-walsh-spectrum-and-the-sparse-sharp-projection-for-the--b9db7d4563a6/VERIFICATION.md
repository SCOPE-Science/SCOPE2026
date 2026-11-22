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

## Checks performed

Running `python3 verify.py` reproduces the 12 pentagons from canonical five-vertex walks, then independently from complements of the six perfect matchings. It verifies the six-dimensional binary cycle code, the complete 64-character Walsh table, the full 32,768-character transform, and the explicit signed inverse-support kernel. Integer assertions also test the exact autocorrelation on codewords and the least surviving multiplier magnitude.

The analytic proof in `RESULT.md` shows why the 64-character quotient is exhaustive and why translation averaging makes the computed endpoint norm optimal over arbitrary real or complex projections. The verification does not cover all cubic graphs or establish historical uniqueness. No independent mathematical audit has been carried out.
