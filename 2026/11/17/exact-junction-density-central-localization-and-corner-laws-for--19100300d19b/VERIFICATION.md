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

The change-of-variables proof verifies the exact endpoint bounds, the positive Jacobian, the symmetry reduction and normalization. The exact side marginal is estimated analytically to get the logarithmic coefficient; the corner-square limit follows by dominated convergence. The included `check.py` (NumPy and SciPy) was run directly from the supplied package directory with a fixed seed. It numerically normalizes the density, compares direct Cartesian endpoint samples with independently integrated spatial rectangle probabilities, and checks local limits. It printed `FORCED_SQUARE_TRANSVERSAL_DENSITY_CORNER_AND_LAYER_OK`.

Numerical simulations support but do not certify the analytic statements. The self-review status concerns this written proof and its local checks only. An independent mathematical audit or definitive prior-art certification has not been performed.
