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

The theorem was checked via explicit differentiation of \(r=y/x^2\) and \(h=-zx\), exact boundary signs, comparison for positivity/global continuation, and integral asymptotics. `check.py` verifies those formulas symbolically and repeats three numerical integrations to time \(100000\), including invariance and convergence diagnostics. The numerical tests are not a substitute for the proof. The asymptotic scope is exactly the given initial region; no other initial states or forcings have been certified.
