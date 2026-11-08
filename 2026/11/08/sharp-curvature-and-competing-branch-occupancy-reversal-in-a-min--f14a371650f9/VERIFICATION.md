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

The derivation uses a renewal sum of complete center-leaf-center excursions and an independent Poisson reset integral. For any positive Laplace argument, both sojourn transforms lie strictly between zero and one, so the geometric resolvent converges and the final probabilities are normalized. All derivatives are ordinary derivatives for positive parameters. The branch occupation derivative has the exact factor \(F_\nu\); its derivative sign and its endpoint limits guarantee the uniqueness assertion without a root-finder. The finite-memoryless limit \(\nu=1\) is affine, whereas the two-stage case yields \(\lambda_*=\sqrt{r(r+a)}-k\) precisely when it is positive.

The standalone `verify_gamma_star.py` checker was executed with NumPy available and reported 384 passing deterministic assertions, including direct stationary-generator solutions for integer shapes one through four and sign/peak tests for noninteger shapes. This independently checks algebraic evaluations but cannot establish a theorem for all continuous gamma shape parameters. The proof above supplies that general conclusion.

Scientific limitations: resets must restart age and occur as an independent Poisson process; branch decisions are independent of sojourn lengths; both leaves have the same exponential return rate; all parameters are strictly positive. The novelty comparison has a residual literature-completeness risk and does not constitute independent verification.
