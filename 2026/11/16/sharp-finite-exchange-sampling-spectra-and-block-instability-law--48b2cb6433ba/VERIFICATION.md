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

# Verification and reproducibility

Run `python CHECK.py` with Python 3, NumPy and mpmath. The script verifies Cauchy determinant identities using exact fractions, the exact inverse Cauchy interpolation formula, and selected finite-dimensional principal-angle eigenvalues; arbitrary-precision tests check the normalized smallest-singular-value convergence for four fixed block sizes. All tested domains are explicitly finite. The proof of the infinite-dimensional parity-coordinate representation relies on [1] in RESULT.md, while the all-finite-set and all-fixed-size-block statements follow from the exact two-projection and inverse-Cauchy arguments in that document. Numerical consistency is not an independent audit or a proof of universal statements.
