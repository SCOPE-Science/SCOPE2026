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

Exact-arithmetic checks: `python verify.py` (Python 3 standard library). The script uses `fractions.Fraction`, solves exact Gram equations, compares all half-range residual squares in dimensions 2 through 12 against the analytic formula for five signed boundary pairs, verifies relative Krylov ranks, and checks full curves for constant and one-sided ramp forcing. It is an independent finite regression test, not a proof over all dimensions. The symbolic spectral-grade, interpolation, and asymptotic arguments in RESULT.md prove the unrestricted statements. Independent human mathematical audit has not been performed.
