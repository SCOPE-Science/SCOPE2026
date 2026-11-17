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

The analytical rank-one gradient representation and the piecewise strict optimization inequalities are the proof. Execute `python check.py` in this directory to reproduce the exact-rational and finite-grid diagnostics. The finite parameter grids verify many instances but do not establish the global minimum, uniqueness or all-horizon claims without the displayed algebra.

The executable has no nonstandard dependencies. It compares directly iterated vertex updates (not just a reimplementation of the closed edge formula) against exact rational edge-column norms; checks general signed inputs; verifies the universal even-horizon scalar identity; and probes the derived odd-horizon minimizers against a dense parameter grid. For general horizons the induction is supplied by the exact projector power identity, not by finite experimentation.
