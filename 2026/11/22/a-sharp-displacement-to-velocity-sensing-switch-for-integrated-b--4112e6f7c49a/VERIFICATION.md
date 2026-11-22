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

# Reproducibility and limits

The included `verification.py` was executed successfully against the packaged mathematical identities. It independently integrates the two explicit covariance kernels, uses exact rational arithmetic for the crossover bracket and derivative Bernstein certificate, and solves a degree-seven polynomial by certified root isolation. It also performs 32 numerical quadratures of original covariance products and 10 numerical comparisons across sample noise levels.

The proof of uniqueness for *all* positive noise levels is analytic: the time derivatives have the stated one-crossing structure, and the logarithm of the two optimized gains has a strictly negative derivative. Finite numerical tests illustrate and stress-test but do not establish that universal claim. The scope is one scalar observation with one of two calibrated modes, common noise variance, and integrated posterior risk for an integrated standard Brownian bridge. Independent audit has not been performed.
