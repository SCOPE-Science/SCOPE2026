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

Run `python3 verify.py` with a standard Python 3 interpreter from the directory containing this file. On the reviewed execution the code reported `PASS: 114 finite assertions; exact cardinal identities, unique-root estimates, and logarithmic scales`.

The checker independently compares the one-node-update formula against product-form Lagrange cardinal functions on small grids, verifies partition of unity, solves the unique root by bisection for several angular displacement fractions, and compares larger-grid finite differences with the predicted asymptotic coefficient. This numerical evidence is diagnostic only: neither finite samples nor floating-point tests prove the existence of the limit or its global sharpness. The rigorous argument is contained in `RESULT.md`, in its exact replacement identities, two-sided harmonic estimates, away-from-center reduction, and one-dimensional maximization. In particular, no independent mathematical audit or external formal certification has been performed.
