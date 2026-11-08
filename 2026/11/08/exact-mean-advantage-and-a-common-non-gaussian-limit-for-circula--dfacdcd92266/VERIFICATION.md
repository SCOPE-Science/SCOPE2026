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

Run `python3 check.py` with Python 3 and no third-party dependencies. The executable reproduces exact finite \(n\) central-binomial and beta-binomial identities using rational arithmetic, verifies the covariance polynomial by deterministic numerical quadrature, and performs seeded simulations of odd and even gap-based mechanisms, with results compared against the proved unconditional means. The executable is a reproducibility aid; the infinite-population process limit is established in `RESULT.md` using a functional central limit argument and weak convergence of the selection measures. The Gaussian-series representation and nondegeneracy follow analytically from the covariance and antipodal symmetry. Numerical trials alone cannot certify that asymptotic law.
