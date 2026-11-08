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

# Computational verification

Run `python check.py` with Python 3.10 or later; no third-party dependencies are needed. The program rederives signed partition discrepancy independently, enumerates *all feasible integer vertex values* for small clique windmills (not merely aggregate counts), compares with the closed norm formula using exact `Fraction` arithmetic, and exercises further signed-capacity identities and the strict integer discrepancy envelope. Successful local replay produced:

```
INDEPENDENT_EXHAUSTIVE_VERTEXWISE_VALUES_OK 23
INDEPENDENT_EXACT_SIGNED_CAPACITY_STATES_OK 67
EXACT_TWO_BLADE_PHASE_IDENTITIES_OK 9801
DISCREPANCY_ENVELOPE_STRICT_MONOTONICITY_OK 79401
ALL_WINDMILL_PARTITION_DISCREPANCY_CHECKS_OK
```

The independent vertexwise enumeration includes every integer-valued feasible anchored assignment, not every real-valued feasible function. The separate analytic tight-edge argument is what proves real maximizers are integer-valued. Finite enumeration does not prove the arbitrary-size-vector result or uniqueness in the literature. The paper gives the full noncomputational universal proof and the exact domain and normalization. No independent audit or external validation is claimed.
