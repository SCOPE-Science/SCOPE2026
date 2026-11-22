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
# Verification and scientific limits

The standalone `check.py` uses exact symbolic algebra for the special parameters and verifies the general formulas after substituting the equilibrium identities. It also independently solves the full nonlinear Neumann stationary equation in a cosine collocation basis at two diffusion values and checks that centered second differences approach the proven coefficient (the numerical convergence is diagnostic only). Execute using `python check.py` with Python 3, NumPy, SciPy and SymPy.

Analytical proof steps requiring no computation are the elliptic implicit-function argument, positive steady uniqueness by a ratio maximum, exact integrated inverse-stock identity plus Jensen, and the mode-by-mode second-order derivative expansion. No numerical computation proves an infinite-dimensional inequality. The coefficient at the critical diffusion is zero but no global catch sign is concluded there. No empirical verification or independent review is claimed.
