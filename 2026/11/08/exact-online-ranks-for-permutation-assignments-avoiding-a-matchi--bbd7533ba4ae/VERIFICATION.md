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

# Reproducible checks

Run `python3 verify.py` with Python 3.10+ from the directory containing this file and the checker. The finite test was actually executed, and its output was:

```text
MATCHING_DELETION_ONLINE_PASS 18 rank_cases n6_derangement_rank 5 base8leaf (2, 1, 2, 2, 1, 1, 1, 1)
```

The checker enumerates all \(18\) parameter pairs for \(2\le n\le5\) and \(0\le t\le n\). It independently compares exhaustive online-rank recursion against the theorem, checks all possible matching candidate supports for VC shattering in those same cases (nonmatching supports are impossible by all-positive labeling), and checks the depth-three base tree leaf by leaf. It separately calculates the derangement online rank at \(n=6\).

These are finite tests, not a substitute for the all-order induction and the Hall proof. No external mathematical audit or mechanized proof-system certification has been conducted.
