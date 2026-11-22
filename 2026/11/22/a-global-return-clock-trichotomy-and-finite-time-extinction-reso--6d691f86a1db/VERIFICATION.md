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

# Reproducibility and verification

The finite checks were run with `python3 check_focus_return.py`, yielding `MIXED_TRACE_RETURN_VERIFY_OK`. They used exact rational arithmetic on the map with \(r=1,d=3\), all positive-gain grid values specified in the checker, a full-plane rational initial grid, the explicit nilpotent gain \(b=3/2\), and seeded random tests at right-focus parameter choices. The checker does not prove an infinite-parameter result: the mathematical argument is in the five proof steps of `RESULT.md`.

The proof independently establishes the exact first exit, bounded reset to a ray, complete ray first return, uniqueness of finite-time extinction, and multiplier-based global behavior. It does not compute the sharp minimal annihilation index across all parameters or validate systems with nonzero forcing. Independent mathematical audit has not been performed.
