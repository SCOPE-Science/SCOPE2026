---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Fresh independent reduced SQN enumeration reproduces 7776, 16807 and 33872. The endpoint reduction is valid because the objective is affine in the upper partition splits after fixing earlier levels, and explicit feasible partition systems attain all three values. The 2024 primary theorem makes the SQN optimization exact for maximum non-overlapping codes.

## originality

FAIL

The claim is directly covered by a stronger SCOPE result already present earlier in the repository history. The earlier record proves the same three maximum values and additionally gives the numbers of maximum codes and their complete optimal partition profiles. Its import commit precedes the assigned record by 41 seconds and is an ancestor of the assigned record's import commit. Therefore the assigned maximum-only statement has no originality independent of that stronger prior record.

## value

FAIL

The maximum-only statement adds no mathematical content beyond the immediately earlier stronger SCOPE theorem, which already proves the same three values together with counts and full optimal profiles. Repeating a strict projection of an existing theorem is not an independently valuable contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
