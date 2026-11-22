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

Run `python verify.py` with Python 3.10 or later; no third-party packages are required. On the prepared source files the program returned `PASS 3937 high-precision cases; 12 rate-two exactness cases`. It independently multiplies the two 3-by-3 exact stochastic substep matrices, uses Decimal arithmetic at precision 65, and checks the explicit hypoexponential CDF, the two formulas for the signed hyperbolic bias, ordering inequalities and exact rate-two cases.

The analytic evidence is the closed-form matrix row reduction, the reflection argument over the waiting-time square, and strict monotonicity of \(\sinh(z)/z\) in \(|z|\), as proved in RESULT.md. The finite grid provides consistency checking only; it cannot demonstrate uniqueness or universal inequalities over a continuum. The limiting large-step ratios are derived from explicit exponentials, not inferred from finite numerics. No outside audit or publication-priority certification has been performed.
