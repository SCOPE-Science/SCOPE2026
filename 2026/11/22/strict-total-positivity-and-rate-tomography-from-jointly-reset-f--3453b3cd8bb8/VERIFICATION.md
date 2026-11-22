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

Run `python3 verify.py`; Python's standard library suffices. The script directly compares the conditional-variance Laplace computation with the closed covariance formula for every pair of five distinct rational decay rates, computes **all** row/column Cauchy minors of orders one through five by the Leibniz determinant formula using exact fractions, and verifies their positive double-alternant products. It also tests each two-mode normalized inverse algebraically and evaluates four covariance integrals numerically by quadrature under a uniform transformed reset age. On the supplied parameters all **608** assertions pass. These calculations validate implementation and normalization; the continuum positive-minor and monotone inverse statements are proved analytically in RESULT.md.

The verification does not cover colored noise, partial resetting, nonlinear interfaces, or finite-sample statistical error, and does not constitute independent review.
