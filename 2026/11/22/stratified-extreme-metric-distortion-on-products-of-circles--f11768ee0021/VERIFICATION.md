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

For the claimed all-dimensional theorem, the proof in `RESULT.md` verifies the metric identities, complete maximizer set, analytic corner normal form, simplex integrals, two-term order accounting, and AM–GM equality case. Numerical tests are additional reproducibility checks only.

From the directory containing `RESULT.md`, run `python checks/verify_clifford_tail.py`. Requirements: Python 3.10 or later and SciPy 1.9 or later. This program independently integrates the two-dimensional exceedance set near each of the three distinct maximizing corners, compares it with both asymptotic terms, checks sample higher-dimensional sharp constants and compares random angular values with the global bound. Executing the embedded program produced `CLIFFORD_STRATIFIED_TAIL_CHECKS_OK 2436`.

A finite set of tests does not establish an infinite theorem, historical priority, or independent mathematical verification. The asymptotic remainder depends on fixed positive radii, and full-text access to some related archival research summaries was unavailable.
