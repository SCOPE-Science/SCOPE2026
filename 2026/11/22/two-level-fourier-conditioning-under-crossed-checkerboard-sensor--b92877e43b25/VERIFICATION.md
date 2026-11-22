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

The complete Gram-matrix computation follows from parity sums of roots of unity, yielding the exact two-by-two matching decomposition and \(H^2=s^2I\) for all even grid sizes. Execute `python3 checker.py` to reproduce finite checks of the full Gram entries, matching structure, and quadratic matrix identity. The checker does not constitute an exhaustive verification over arbitrary side lengths or real displacements; the analytic proof carries that quantifier. No independent mathematical review has been performed.
