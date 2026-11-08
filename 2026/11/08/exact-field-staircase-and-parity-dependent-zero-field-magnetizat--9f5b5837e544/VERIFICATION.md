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

# Reproducibility and limits

Run `python verification/check_rook.py` using a standard Python 3 installation. The script enumerates every spin configuration on the eight boards \((2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),(5,3)\), checking every fixed-population cut maximum and every equality case, zero-field sectors and rational-field energy minimization. It also evaluates the finite discrete concavity and zero-field optimum on 323 boards and the critical-field gcd count on 361 boards. Expected markers: `EXHAUSTIVE_OK`, `ENVELOPE_OK`, `GCD_THRESHOLD_COUNT_OK`. The exact finite computations support, but do not constitute, an all-size theorem proof; that proof is given in RESULT.md. Historical priority and any broader generalization are not independently certified.
