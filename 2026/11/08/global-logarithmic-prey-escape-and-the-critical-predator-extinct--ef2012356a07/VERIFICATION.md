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
The analytic proof establishes universal statements. `CHECK.py` is a standalone standard-library finite-iteration sanity check for three parameter configurations and multiple horizons. It checks positive iterates, declining predator population, and qualitative approach of the normalized prey residual and predator logarithmic clocks. In floating-point arithmetic the predator count may underflow after many iterations; the log-multiplier sum is tracked separately, and the exact proof is unaffected.

No external or independent certification is performed. The script does not prove the asymptotic limits, which require the analytical comparison and time-change argument in `RESULT.md`.
