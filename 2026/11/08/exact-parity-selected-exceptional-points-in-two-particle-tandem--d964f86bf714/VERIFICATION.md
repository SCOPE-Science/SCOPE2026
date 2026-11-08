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

# Verification and limitations

Run `python verify.py` from the same directory with Python 3, NumPy and SciPy. The program generates all two-particle configurations for several odd/even ring lengths, implements the two triple transitions without relying on the block-spectrum proof, checks the active graph and frozen states, compares full-generator eigenvalues against the closed formula, checks a measured staggered expectation through matrix exponentiation, and verifies the size-two nilpotent Jordan remainder at both ratios. It produces a PASS line only after the comparisons succeed.

These computations check finitely many rate pairs and ring sizes. The statements for all \(N\ge5\), all positive rates and every nonnegative time follow from the algebraic argument given in RESULT.md. The claim is not a many-particle or thermodynamic-limit theorem, and no external independent audit is claimed.
