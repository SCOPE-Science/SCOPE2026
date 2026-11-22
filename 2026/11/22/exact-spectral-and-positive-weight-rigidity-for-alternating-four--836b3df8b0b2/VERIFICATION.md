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

The exact block-diagonal reduction and transitive symmetry average are proved in `RESULT.md`. The checker `CHECK.py` is a standalone Python 3 standard-library program and was run from the same package with the result `PASS: 846 supplementary checks`. It verifies the Fourier Gram minimal polynomial, determinant, normalized and unnormalized squared Gram defect and representative nonuniform positive-weight comparisons for finite even sample sizes. These are finite numerical checks rather than an exhaustive verification of the theorem over every order and continuum of weights. The determinant and equality cases follow analytically from Vandermonde invertibility and arithmetic-geometric mean, not from this program. External independent audit has not been performed.
