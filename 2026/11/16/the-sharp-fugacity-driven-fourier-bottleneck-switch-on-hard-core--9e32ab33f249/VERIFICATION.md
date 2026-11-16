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

# Reproducibility and verified scope

The included `checker.py` uses Python 3, SymPy, and NumPy. From its containing folder run `python checker.py`. It independently checks exact symbolic formulas for the four endpoint multipliers, the two factorized comparisons, the threshold, the exact condition-ratio derivative jump, and both formulas for the limiting condition ratio. It enumerates all 3-state cyclic rung words of lengths 3 through 9 at activities 1/2, 1, and 3, and checks weighted occupation moment numerators exactly against transfer traces. It compares full finite Fourier arrays to the continuum limits at lengths 32, 64, 96, 128 for five activities.

The finite computations are finite evidence, not a replacement for the Perron-transfer, geometric correlation, uniform limit, and positivity proof. The asserted limit takes length to infinity with activity fixed; no joint limit and no exact finite-length crossover are verified. Independent audit and independent validation have not been performed.
