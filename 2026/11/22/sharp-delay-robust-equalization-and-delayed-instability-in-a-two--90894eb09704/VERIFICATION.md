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

# Verification scope

`python3 verify.py` performs exact-rational checks comparing the original two-agent normalized shares with the scalar rational reduction, and finite numerical checks of contractive behavior and linear characteristic roots. The analytic steps that establish the all-history and all-delay theorem are in `RESULT.md`; no finite grid is interpreted as a universal proof. The software uses only the Python standard library. The exact iteration is verified for representative rational coefficients and integer delays, and the critical endpoint relies on the stated omega-limit equality argument, not simulation. Independent scientific validation is not yet performed.
