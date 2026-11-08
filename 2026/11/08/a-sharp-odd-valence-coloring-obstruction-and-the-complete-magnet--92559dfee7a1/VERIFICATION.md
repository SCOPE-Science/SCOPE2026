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

The finite claim is fully reproducible by compiling and executing `verify_exhaustive.cpp` under a conforming C++17 compiler, and by running `verify_transfer.py` with Python 3 and its standard library.

The C++ verifier enumerates all \(3^{12}=531441\) assignments, verifies a simple thirty-edge five-regular graph construction, the full occupancy-minimum/degeneracy table, the twenty ground-defect edge supports with six configurations each, the six critical-field counts and the exact integer lower-hull inequalities. Its success marker is `EXHAUSTIVE_OK`.

The Python verifier computes the same complete joint bond/occupancy coefficients by a distinct two-pentagon transfer contraction and verifies the sum of multiplicities is exactly \(531441\). Its success marker is `TRANSFER_EXACT_OK`.

The parity obstruction is a direct proof for all closed surface triangulations and is not inferred from the finite computational test. No independent external audit or certification was performed. Field strengths are exact real parameters; comparisons use integer and rational linear inequalities, not floating-point thresholds.
