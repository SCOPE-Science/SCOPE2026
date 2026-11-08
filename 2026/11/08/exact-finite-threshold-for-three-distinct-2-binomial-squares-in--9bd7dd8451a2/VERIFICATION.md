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

# Verification record

The finite theorem is reduced to exact exhaustive enumeration by the suffix-extension recurrence, with a monotone stopping condition at four distinct square strings.

Executed with Python 3 standard library:

```
python3 check_bfs.py
python3 check_dfs.py
```

Both programs reported PASS. The breadth-first program checks both binary extensions of every retained prefix, outputs four admissible words at length 43 and none at length 44, and checks exact intermediate layers. The depth-first program checks literal counts of all six length-one and length-two subsequences and, after a justified complement symmetry reduction, finds exactly two zero-initial words of length 43 and no word of length 44. This check is complete because the state property is prefix-monotone.

No independently executed scientific audit has been performed. The result does not establish bounds under any other repetition notion.
