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

Execute `python verify.py` with Python 3 (standard library only). The program represents \(n^2D_{p,q}\) as a Laurent polynomial in the independent circle characters and computes expectations as constant-term coefficients. It checks 11 frequency configurations at each of \(n=2,3,4\), including all four covariance regimes, for 33 exact-rational comparisons against the proposed formula. Twelve additional exact-rational assertions compare the rectangular variance with a direct combinatorial covariance sum. All 45 assertions passed at package construction.

The independently derived analytic proof in `RESULT.md` applies for all \(n\ge2\) and every nonzero integer frequency. The program checks selected finite cases only and is not a proof of untested cases or a statistical accuracy certificate. The uniform-marginal null, fixed sample size and frequency assumptions are essential. Independent audit: not performed.
