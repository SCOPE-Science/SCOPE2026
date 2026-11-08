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

Run `python3 verify_stumps.py` in the directory containing the script. Only the Python standard library is needed. The supplied `verification_output.txt` records the exact deterministic replay.

Two independent programs in the script count realizable matrices: a recurrence updating trace-coverage masks coordinate by coordinate and a direct, full enumeration of all possible \(q\)-ary \(m\)-row coordinate arrays. Twelve small parameter combinations are compared. Critical-family probabilities for \(q=3,4,5\) and small \(m\) use exact decimal inclusion–exclusion and a separate explicit upper bound on other missing traces.

A line `ALL_CATEGORICAL_LITERAL_CHECKS_PASS 12 exact exhaustive cases` indicates the finite cases agree. These tests do not certify a limit law or the completeness of a historical literature search. The mathematical proof requires the disjoint-target factorial moments and the uniform union bound stated in the result.
