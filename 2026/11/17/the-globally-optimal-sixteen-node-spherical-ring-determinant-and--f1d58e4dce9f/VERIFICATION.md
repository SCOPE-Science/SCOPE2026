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

# Verification of the sixteen-node spherical ring determinant classification

Run `python CHECKER.py` with Python 3.10 or later. It uses `fractions.Fraction` and no third-party packages. The checks are exact integer/rational assertions and stop if any inequality fails. The certificate covers six rational sample points, their chamber membership, six squared-gradient bounds, five ordered comparisons of **the true maxima** via a globally valid concavity bound, the optimum/runner-up ratio enclosure, and the strict factor-four gap.

The proof of the block-triangular Fourier/Vandermonde factorization and the global Hessian bound is in `RESULT.md`. Those analytic steps are needed to transfer the finite certificate to all real latitudes; the certificate alone is not an exhaustive search of a continuum and a successful process exit is not a substitute for the analytic proof.

The result does not certify the best arbitrary 16-node spherical Fekete set or numerical conditioning. The sharp ratio is enclosed but the exact algebraic ratio is not given in radicals. Independent mathematical validation has not been performed.
