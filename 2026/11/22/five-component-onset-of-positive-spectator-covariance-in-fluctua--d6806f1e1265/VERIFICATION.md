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

The file `verify.py` provides a standalone exact-rational check of the signs of the high-loading covariance coefficients. Run `python3 verify.py`; it prints four interval certificates (three negative, one positive) and a final assertion. It has no dependencies beyond the standard Python library.

The mathematical steps requiring proof rather than computation are: (1) Poisson shift identity with strict unique-minimum condition; (2) two integer minimum tail sums; (3) small-loading expansion; (4) multivariate Poisson-to-Gaussian convergence with uniformly bounded fourth moments; (5) exact Gaussian moment integration by parts and standard two-/three-variable orthant probabilities. Each is reconstructed in `RESULT.md`.

The check does not certify arbitrary numbers of species, uniqueness of the finite-loading sign crossing, or exact finite-loading sign outside small and large regimes. It is not independent scientific validation.
