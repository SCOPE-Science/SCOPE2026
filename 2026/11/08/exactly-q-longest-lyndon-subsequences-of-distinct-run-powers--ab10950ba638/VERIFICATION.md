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

# Finite verification and proof scope

The proof for every allowed \(q\), \(k\), ordering and positive run-length vector appears in `RESULT.md`. The finite tests below are corroboration and do not certify unbounded cases on their own.

Command: `python3 verify.py` (standard library only).

Output checked:

```
PASS
exhaustive_configurations=1647
seeded_random_configurations=800
total_configurations=2447
single_deletion_candidates_checked=76876
maximum_word_length=145
```

For every profile, the checker evaluates all \(kp\) possible single-position deletions using the literal suffix definition of a Lyndon word, independently of the descent/ascent classification. It asserts equality of the entire qualifying-position set, the total \(p\) qualifying positions and the \(q\) distinct maximizing strings. Its exhaustive cases range over \(q=2,3,4\), all permutations of distinct letters with the least first, lengths \(1\) through \(3\) in each run, and powers \(2,3,4\). The additional cases use seed `12022022` and include up to six distinct symbols and powers up to five. The full-period word is checked to be non-Lyndon in every instance.

The testing script does not prove the completeness of the case split for arbitrary parameters. That is provided by the suffix comparisons in Steps 1–6 of `RESULT.md`. No independent mathematical audit has been performed.
