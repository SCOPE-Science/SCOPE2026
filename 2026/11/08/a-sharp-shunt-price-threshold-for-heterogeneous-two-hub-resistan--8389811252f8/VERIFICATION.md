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

# Reproducibility and scope

Run `python verify_design.py` in a local environment with Python 3, NumPy, SciPy and SymPy installed. The verifier was run from its actual source path and produced `VERIFY_OK 2035` during preparation. It checks exact rational Kirchhoff index identities against direct graph Laplacian inversion, mixed-price optimal-budget and KKT conditions on both sides of the shunt threshold, comparison to independently sampled fully asymmetric feasible allocations, and equal-price threshold values.

The finite cases do not establish the infinite-dimensional parameter quantifiers or a publication-priority conclusion. Those rely on the all-size strict-convexity, decomposition and KKT arguments documented in RESULT.md. No external independent check has been performed.
