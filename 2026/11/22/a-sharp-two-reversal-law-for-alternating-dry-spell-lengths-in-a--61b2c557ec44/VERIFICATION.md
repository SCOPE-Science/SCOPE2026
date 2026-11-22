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

# Verification procedure

With `RESULT.md` and `checker.py` in the same folder, run `python3 checker.py`. The checker requires only the Python 3 standard library and uses deterministic parameter grids; its expected output starts with `PASS: 2504 deterministic numerical assertions` and reports the special-case critical half-gap and the three illustrative comparisons. The script evaluates both original event-reward formulas and the independent hyperbolic rearrangements, brackets the two-stage threshold and root counts, tests the strict sign regions, and separately tests the one-stage cutoff.

The mathematical validity for the full continuum of parameters follows from the written proof rather than finite tests. In particular, the exact inequality based on the integral of \(\coth\) shows the comparison function exceeds its threshold at its unique maximum, and the derivative of Erlang-two CDF elasticity proves uniqueness of the half-gap transition. Floating-point tests alone cannot certify root counts, priority over all mathematics, or validity beyond this model's assumptions.
