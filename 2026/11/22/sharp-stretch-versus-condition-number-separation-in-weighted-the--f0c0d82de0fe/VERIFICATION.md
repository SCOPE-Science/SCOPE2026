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

# Verification instructions and limits

Run `python verify_theta.py` in the same directory as this document (requires NumPy, SciPy, SymPy). It constructs six different pathwise weighted theta graph families, enumerates every possible pair of omitted edges on two separate arms, forms grounded Laplacians, and checks all positive generalized eigenvalues and the total-stretch trace against the closed formulas. It also tests the precise rational/surd phase comparisons for the six-vertex family. A successful execution was recorded as `verification_output.txt`.

The universal proof is the rank-two update and elementary algebra in `RESULT.md`, not the finite numerical tests. Floating generalized eigensolver comparisons use tolerances of \(10^{-10}\), while the seven symbolic comparisons use exact SymPy simplification. The verification is a self-review, not independent audit or certification.
