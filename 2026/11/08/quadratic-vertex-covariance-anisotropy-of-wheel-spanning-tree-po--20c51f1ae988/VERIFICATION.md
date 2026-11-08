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

# Reproducible checks

Run `python3 verify.py` using Python 3.9 or later and no third-party modules. The script independently enumerates all spanning-tree incidence vectors for \(3\le m\le7\), computes exact rational covariance entries from the uniform vertex distribution, and independently computes the inverse-Laplacian covariance. It asserts all entries agree. This exhaustively accounts for 1,343 spanning-tree vertices over five wheel sizes.

It then forms the actual wheel covariance in two cyclic blocks and checks the Hermitian Fourier eigenspectrum, the constant-vector zero eigenvalue and the strictly positive other modes on 495 nonconstant block instances for \(3\le m\le32\). An explicit Green-kernel Fourier-block calculation matches all 525 finite block eigenvalue pairs in that range. For seven larger sizes up to \(m=320\), it compares both limiting branches and the scaled condition number against the derived constant. A passing run prints `WHEEL_SPANNING_TREE_INERTIA_CHECKS_PASSED`.

The asymptotic \(\lim\kappa(C_m)/m^2=4/(5\pi^2)\), the eventual extrema, and the infinite-family finite block representation are established analytically in RESULT.md. Finite enumerations and floating-point comparisons are diagnostic only and do not constitute infinite proofs. No independent audit has been performed.
