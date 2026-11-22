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

# Reproducibility notes

The proof uses two exact algebraic slack identities, not estimates obtained by data fitting. Both identities are expanded in RESULT.md. To check rational instances, execute `python3 checks/exact_profile_check.py` in a directory containing the packaged files. It prints `PASS: 75261 exact rational assertions; all identities agree.` when all assertions succeed. The checker requires Python standard-library `fractions` only.

Actual checked boundaries: one equal-axis endpoint on each side; the geometric-progression endpoint for square-ratio instances; the two root involution; the explicit tetrahedron with semiaxes `(2,2,1)` and roundness squared `2/27`. The full real-parameter result and its quantified stability follow from the written algebra, monotonicity and asymptotics, not from the finite checker. No separate independent verification was undertaken.
