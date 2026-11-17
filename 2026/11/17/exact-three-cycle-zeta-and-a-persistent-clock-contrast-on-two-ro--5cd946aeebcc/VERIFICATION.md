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
# Exact reproducibility

Reconstruct the integer transfer matrix and verify its full characteristic polynomial using `python3 verification/transfer.py` (requires SymPy). Independently verify all 81 coefficients using only the standard library by `python3 verification/independent_certificate.py`. Compile the independent direct simulator with `g++ -std=c++17 -O3 verification/direct.cpp -o /tmp/ghm_2row_direct` then execute it. Each produced standard output matches the corresponding `verification/*.out` file. The direct simulation tests all \(3^{2n}\) configurations for \(n=3,4,5,6\); the unlimited claim follows from the exact integer polynomial identity and the bijection, not extrapolation of finite tests. There is no external independent verification.
