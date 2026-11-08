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

# Verification

The result is an infinite-family proof built on a cited finite-graph cycle criterion and an explicit finite sum over normalized integer heights. The two supplied standard-library verification programs were actually run from the paths in this package before acceptance:

- `python verify_lifts.py` checked height-lift cycle consistency for all labelled three-colour starts on 22 graph instances, sizes \(n=3,4,5,6\), matching-deletion sizes \(t=0,\ldots,n\), against the stated exact census. Its last output line is `ALL_PASS`.
- `python verify_dynamics.py` used two separate synchronous CA update rules directly, with eight full updates per start, on all 390,015 labelled initial states for 15 cases at \(n=3,4,5\). Its last output line records `DYNAMICS_PASS`.

The scripts use Python 3 standard library only; no external packages, solver, hidden inputs or datasets are required. The two `.out` files record the actual observed outputs. These finite checks do **not** certify the theorem for unbounded \(n\); the proof supplies that step. Historical originality and an independent audit are not certified.
