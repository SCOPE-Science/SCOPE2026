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

# Reproducibility

Run `python verify.py` using Python 3. Only the standard library is required. The exact-rational checker reconstructs the 38-entry support, verifies its seven-perfect-matching cover, solves the signed-incidence Gram system, and checks the asserted rational row norm and positive excess. It also verifies exact bistochastic constraints, strictly positive face entries, and the strict off-support KKT slacks for two explicitly defined finite input matrices at perturbation size \(10^{-6}\).

The code establishes a lower bound for the global maximum-entry Lipschitz coefficient; it does not enumerate all faces or establish global sharpness, historical uniqueness, or an independent audit.
