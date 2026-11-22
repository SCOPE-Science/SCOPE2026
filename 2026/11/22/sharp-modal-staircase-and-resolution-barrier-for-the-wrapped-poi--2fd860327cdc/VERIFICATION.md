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

The probability model and all quantifiers are defined in `RESULT.md`. Run `python3 verify_wpl_modes.py` in this directory; it requires no third-party packages. The bundled program completed with `CHECK_OK 3863`.

Exact-rational checks verify the six-sector polynomial sign interval, probability normalization, adjacent-ratio formulas, and strict finite-index inequalities at rational parameter values. Finite numerical diagnostics check direct wrapped-series approximations and the large-resolution rate.

The proof of strict monotonicity on the full positive real parameter domain, the exact number of transition roots for every resolution, and the asymptotic limit all rely on the analytic arguments written in `RESULT.md`, not on the finite checker. No external mathematical audit or computer-assisted proof certification has been performed.
