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

The proof establishes global critical-point completeness using the strictly decreasing ratio of two positive Poisson derivative terms. It calculates the exact threshold, valley location, global minimum, quartic critical contact, and leading constants of both near-threshold asymptotics. All parameter boundaries are included in the statement, with the single-source endpoint excluded from the valley formula.

To reproduce the finite diagnostic computations run `python3 CHECK.py`. The checker is self-contained and makes 1,972 diagnostic assertions for representative integer dimensions, radii, mass imbalances, derivative signs, inversion and critical expansions. Finite diagnostics do not prove the universal theorem. Published mathematical priority and independent validation have not been certified.
