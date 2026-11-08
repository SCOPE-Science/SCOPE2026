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

# Reproducibility and proof boundaries

Run `python3 artifacts/verify_signed_stencil.py` from the extracted finding's root directory; no third-party packages or data downloads are needed. Its actual execution completed 3977 deterministic exact-rational and Fourier/sampling checks.

The check reconstructs the five-point stencil by squaring the three-point difference operator; verifies the strict rational radius-16 negative moment and majorant inequalities; checks the Fourier symbol on finite cycles; and compares periodic heat kernels over finite dimensions and times. The all-time and all-dimension claims are supported by the Laurent-series, compactness, and weighted-alias proofs in `RESULT.md`, not inferred from the finite computations.

This is a reproducibility certificate for the stated mathematical computations only. Independent audit and independent validation have not been performed. The precise first grid size for the conservative linear lower bound, optimal lower-bound constant and an exact sharp recovery horizon are not established.
