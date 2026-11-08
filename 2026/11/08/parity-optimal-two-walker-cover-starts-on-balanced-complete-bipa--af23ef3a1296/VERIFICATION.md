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

Run `python3 verify.py` with Python 3 standard library. During the local check the script returned:

```
CHECK_OK {'full_labeled_state_vs_coupon': 81, 'strict_deadline_checks': 672, 'ordered_stirling_checks': 378}
```

The first group enumerates all pairs of labeled walk positions and all visited-vertex masks on unweighted balanced complete bipartite graphs with side sizes 2, 3 and 4 at every deadline 0 through 8, including split, two distinct same-part and duplicate starts. All probabilities are exact rational numbers.

The second group checks both strict optimal-placement inequalities and their boundary thresholds at all side sizes from 2 through 17 and even base deadlines 0 through 40. The third checks integer log-concavity inequalities for ordered surjection counts through 27 labeled draws.

These finite checks are supplementary, not proofs of the all-parameter theorem. The unrestricted claim follows from the coupon-collector factorization, the log-concavity induction and the odd-step first-draw identity in `RESULT.md`. There is no independent mathematical audit.
