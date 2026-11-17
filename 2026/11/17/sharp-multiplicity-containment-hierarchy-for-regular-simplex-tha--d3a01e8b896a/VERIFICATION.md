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

The analytic calculation in `RESULT.md` proves the all-dimensional theorem. The accompanying `check_hierarchy.py` independently constructs regular simplex vertices with standard-library arithmetic, evaluates the sharp contact points against direct Euclidean ball inequalities and simplex facet gauges, checks their index types and counts, and tests randomly sampled directions against the same bound. Run `python3 check_hierarchy.py`; it returned `PASS: 284683 deterministic floating-point assertions, d=2..11`. Numerical validation does not assert exhaustive verification of real parameter spaces or replace the proof. No independent audit was performed.
