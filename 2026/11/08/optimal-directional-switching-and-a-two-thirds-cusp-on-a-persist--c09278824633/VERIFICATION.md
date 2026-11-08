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

Run `python verify.py` after installing `numpy` and `scipy`, for example `python -m pip install -r requirements.txt`. The checker constructs an independent complete generator (rather than using the analytic Fourier formula as matrix input) and checks 1,344 numerically diagonalized state spaces, \(4\le n\le27\), seven bias values and eight reversal-scale ratios. It then performs local numerical maximization for each parameter pair and prints numerical checks of the small-bias exponent. All checks passed on the reported package contents.

The exact result for all \(n\ge4\), including the uniqueness of the optimum and the \(2/3\)-power expansion, follows from the theorem's symbolic proof; finitely many matrix calculations alone cannot certify it. Spectral gaps are not nonnormal transient or mixing-time guarantees. The symmetric model's critical-point optimization is already in the literature. Historical priority for the asymmetric exact cubic remains provisional; independent audit has not been performed.
