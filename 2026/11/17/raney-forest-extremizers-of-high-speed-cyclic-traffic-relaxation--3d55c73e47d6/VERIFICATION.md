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

# Verification of the finite and analytic components

The all-parameter proof is in `RESULT.md`; experiments are illustrative corroboration rather than a replacement for the strict global-minimum argument.

- `verify_gap.py` enumerates all gap vectors in 70 bounded parameter cases for speeds 1 through 5 and checks both the sharp maximum and exact extremal count directly under the gap recurrence. Speed 1 is included as a cross-check only, not as a novelty claim. See `gap_check.txt`.
- `verify_binary.py` enumerates all physically occupied binary configurations for eight speed/circumference/census choices, advances cars independently and tests entry to the free-flow regime. See `binary_check.txt`.
- `verify_forest.py` compares a direct ballot-path recursion, a formal power series for forests of full \((v+1)\)-ary trees, and the closed binomial coefficient in 30 cases. See `forest_check.txt`.

All programs require only Python 3 standard library. Run `python3 verify_gap.py`, `python3 verify_binary.py`, and `python3 verify_forest.py` from the directory containing the scripts. The final package includes the exact output text of their completed runs. None of these runs establishes independent expert validation, full archival historical priority, or any behavior outside the theorem's hypotheses.
