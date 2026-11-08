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

The package contains `artifacts/verify.py`, a standalone standard-library Python 3 program. Run from the extracted package root as `python3 artifacts/verify.py`. The verifier exhausts all pebble configurations of all sizes through the claimed threshold on \(F_1,F_2,F_3\), using exact reachability, and separately verifies the claimed obstruction through \(F_7\). It also checks local blade reduction for several masses and the integer hub-credit inequality. This is a finite consistency test, not a replacement for the universal proof in RESULT.md.

Exact observed output at package creation:
```
LOCAL_HIGH_BLADE_REDUCTION_OK s=4..22
LOCAL_INDUCTION_OK
ARITHMETIC_RESOURCE_BOUND_OK r=1..4
FULL_CONFIGURATIONS_OK r=1 threshold=4
FULL_CONFIGURATIONS_OK r=2 threshold=8
FULL_CONFIGURATIONS_OK r=3 threshold=12
OBSTRUCTION_OK r=2 mass=7
OBSTRUCTION_OK r=3 mass=11
OBSTRUCTION_OK r=4 mass=15
OBSTRUCTION_OK r=5 mass=19
OBSTRUCTION_OK r=6 mass=23
OBSTRUCTION_OK r=7 mass=27
VERIFY_OK
```

No independent mathematical audit was performed. An unindexed equivalent infinite-family theorem is a residual priority risk.
