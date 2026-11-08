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

# Reproducible verification

The package includes `verify.py`, a Python 3 program requiring no additional packages. From the extracted package directory, execute `python3 verify.py`. The direct run passed **321 exact rational checks**. They compare the Chebyshev-derived transfer polynomial both with matrix multiplication and with a complete direct spin-configuration sum for rational choices of the exponential coupling and field variables. The script also checks the exact central constant or first-derivative coefficient from which the critical thresholds follow.

Analytical proof obligations not settled by this finite script are handled separately in `RESULT.md`: the transfer reduction for arbitrary positive bulk interaction and real impurity interaction, endpoint/interior-node sign pattern for negative defect interaction, the sharp central derivative condition, existence of the imaginary pair, and degree-count exhaustion. The script does **not** independently certify all ring sizes, exhaustive source coverage, or a general unequal-defect result.
