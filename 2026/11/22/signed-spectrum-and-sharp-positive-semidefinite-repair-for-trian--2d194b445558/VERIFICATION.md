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

Run `python verify_splitmask.py` with a recent NumPy installation. The embedded standalone program returned `VERIFY_OK 1870`. It checks depth-one-through-forty sine eigenpairs, full matrix spectra, inertia, the Brownian squared identity, explicit Gram truncation bounds, exact-rational determinants, and small symmetric binary mask families. These finite tests do not certify the universal mathematical statements, for which the proof in RESULT.md is required.

The evidence concerns exact-arithmetic split-product coefficients, not rounded hardware outputs or claims that arbitrary positive vectors arise from a particular digital splitter. Independent audit has not been performed.
