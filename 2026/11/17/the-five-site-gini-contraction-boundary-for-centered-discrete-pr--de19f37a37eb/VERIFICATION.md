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
# Reproducibility

Run `python3 check.py` with the Python standard library. It exhaustively checks the binary-cut quotient for all nonempty proper subsets in dimensions two through five, with exact rational arithmetic, and checks analytic singleton ratios for larger finite dimensions as diagnostics. The infinite-family nonexpansivity failure is proved directly by a closed formula, while the all-dimensional upper bound is proved by interval counting. Neither test output nor finite observation is taken to prove an unrestricted identity for the sharp coefficient beyond five vertices.
