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

# Verification notes

Run `python3 -S checker.py` with standard-library Python. It compares forty sampled spiral convex hulls against the closed perimeter/area formulas, and six hundred random support directions against the predicted terminal-arc support, printing `PASS` if all diagnostics meet tolerances.

The mathematical proof is not based on these finite checks: the critical global step is domination of the latest exponential spiral support maximum, proved for all angles and finite \(T\) in RESULT.md. The root uniqueness, Green integral and derivative identities are analytic. Tests cover selected pitch values, not the entire continuum.
