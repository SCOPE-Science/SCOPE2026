---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification checks and limits

`python3 verify.py` constructs all pointed singular transformations at the tested sizes, checks the arc-based criterion on all nonroot tournaments at \(n=4,5\), checks the cyclic strong tournament at \(n=6\), and tests the small idempotent examples and the strong-tournament recurrence. Its recorded output is in `VERIFY_OUTPUT.txt`; it does not test the ordinary rank at \(n=3\).

`python3 verify_n3.py` enumerates all seven singular maps fixing \(0\) on three points, tests closure of candidate generating subsets, and checks the explicit ordinary three-generator witness from `RESULT.md`. It reports ordinary rank 3 and idempotent rank 4. Both programs use the Python standard library. The all-size theorem is proved by the kernel bound, pointed factorization and Howie's unpointed criterion; the finite computations verify only the cases they enumerate.
