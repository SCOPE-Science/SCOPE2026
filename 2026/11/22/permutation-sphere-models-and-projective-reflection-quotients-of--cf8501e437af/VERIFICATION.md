---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and boundaries

Run `python3 checks/verify_spider.py` from the package directory. The standard-library-only test checks the explicit simultaneous fold on all faces in four higher-arm examples and the exact orbit-face correspondence for selected subgroups. It does not test arbitrary parameters or assert that an equivariant homotopy type follows from finitely many examples. The representation-sphere and fixed-space conclusions follow from the general argument in `RESULT.md`.
