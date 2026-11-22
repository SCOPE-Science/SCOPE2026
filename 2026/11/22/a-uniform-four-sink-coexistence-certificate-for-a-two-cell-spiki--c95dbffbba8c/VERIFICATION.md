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

Run `python3 checker.py` with Python 3 standard library. The program evaluates the strict Poincaré–Miranda signs on all 36 rectangle faces with rational interval arithmetic. It proves the required rational exponential lower bounds by truncated Taylor sums with all positive omitted terms and checks the uniform derivative, determinant, and inverse estimates.

The analytic proof is not a finite alpha sweep: monotonicity of tanh, artanh, and of the relevant alpha-weighted exponential envelopes turns these checks into bounds for all real gains at least six. The checker does not enumerate all possible equilibria or claim sharpness of the lower gain threshold.

This verification is within the supplied mathematical package and is not independent validation.
