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

# Reproducibility and verification

The package contains `RESULT.md` with the analytical proof and `CHECKER.py` (Python 3 standard library only). Run `python CHECKER.py` in the extracted package directory. The checker was executed on the source packaged here and passed 177 deterministic checks, covering quartic-profile normalization, exact cost integrals, scalarized Euler condition, strict ordering, competitors, the homogeneous and singular endpoint constants, and the singular-endpoint Laplace-series normalization.

The mathematical argument, not the finite checker, proves the global infinite-dimensional variational result. The fixed-profile first-arrival law for regular diffusions is supplied by Lawley (arXiv:1909.09883). The absorbing singular-endpoint diffusion is justified separately in the proof through its transformed generator and exact Laplace transform; no simulation-only premise is used. No finite-population exact optimizer, noise-stability bound or independent external audit is claimed.
