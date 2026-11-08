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

# Verification

Run `python3 verify_degree_subtree.py` using Python 3 standard library. The checker constructs every uniformly probable parent-choice sequence for tree sizes 2 through 9, computes direct degrees and complete descendant-subtree sizes, obtains mixed covariances as `fractions.Fraction`, and compares all entries to the analytic formula. It additionally checks direct-degree means and the exact conservation of each covariance column through size 109.

Observed stdout when replayed from this candidate's current standalone artifact:

```
PASS 6322 exact checks; all recursive trees with <=9 nodes enumerated
```

All-size correctness comes from the independent-insertion conditioning and the telescoping proof in `RESULT.md`, not from finite enumeration. The program is ordinary reproducibility code, not an external or independent certification.
