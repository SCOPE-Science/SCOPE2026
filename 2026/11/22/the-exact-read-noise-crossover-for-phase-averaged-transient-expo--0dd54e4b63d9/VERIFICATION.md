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

The theorem is established analytically in `RESULT.md`. The accompanying standalone `check.py` independently forms pulse/exposure intersections and tests the phase-average formula against direct phase quadrature, exact rational simplifications, stationary-point conditions, and a range of candidate exposure ratios. A successful execution prints `PASS 3713 assertions`.

These checks are finite diagnostics. They do not certify the all-real-parameter statement, prove historical priority, evaluate unknown-phase false-alarm effects, or substitute for field validation. The theorem's global scope relies on the explicit derivative-sign proof in `RESULT.md`.
