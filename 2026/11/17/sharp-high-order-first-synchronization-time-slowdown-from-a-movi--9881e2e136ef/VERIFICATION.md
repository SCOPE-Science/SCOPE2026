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

Run `python3 verify_fst.py` from this package, using Python's standard library; there are no external dependencies. The expected final status is `VERIFY_OK configurations=3 interaction_orders= 24 integral_and_equilibrium_checks= 48` (spacing may vary only if the print format changes). Checks compare root locations, opposite signs of FST deviations in the large-order samples, and the asymptotic ratios for two exponential rates in three distinct parameter configurations. The source function is exactly the reduced scalar equation in the cited 2026 paper.

The full proof is in RESULT.md. Finite numerical integration does not certify the limits for all parameter choices, and the current self-review is not independent audit or external verification.
