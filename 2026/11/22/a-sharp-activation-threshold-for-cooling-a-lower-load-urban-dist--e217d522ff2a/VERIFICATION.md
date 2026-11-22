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

The full proof and the exact example are in `RESULT.md`. The standalone file `checks/verify.py` uses only Python's standard library and prints a `PASS` line when its checks succeed. Run from the package root with `python3 checks/verify.py`.

The checker verifies thousands of exact-rational instances of the stationary derivative identity, rational comparison inequalities at a fixed physically interpretable boundary case, rational bracketing of the optimal allocation, and seeded numerical tests for the general optimizer, activation threshold, positivity, and the peak objective. The universal result is proved analytically by positivity of the determinant, strict increase of the derivative numerator, and a unique crossing of its boundary sign. Finite checking alone is not a proof for real-valued parameters. No independent external verification has been performed. The mathematical model has not been experimentally calibrated to real cities.
