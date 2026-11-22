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

# Verification of the displayed theorem

Execute `python verify.py` with Python, SymPy and SciPy installed. The script tests exact polynomial identities for orders zero through eight, including covariance endpoint normalization, the signed-coefficient inflection polynomial, and the two leading boundary derivatives. Supplementary scalar-optimization examples for two high-noise levels per order check the predicted asymptotic location to a broad finite-noise tolerance. The last observed output was `PASS: 99 exact and supplementary checks across orders 0..8`.

The independent all-order justification appears in RESULT.md: integration of the Brownian covariance, a binomial expansion for the derivative of the risk-reduction functional, a one-sign-change proof for its second derivative, and the asymptotic endpoint-integral expansion. Finite orders and numerical optimization do not establish any statement about all orders; the analytic sign argument does. No finite test can establish publication priority or rule out mathematically equivalent historical results. No external independent audit is claimed.
