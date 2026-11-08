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

The explicit proofs of (i) the greedy weak-descent criterion, (ii) the rank-one evaluation of the weighted trace, and (iii) the cyclic-descents extremal classification are in `RESULT.md`. A standard-library executable `verify.py` provides independent finite checks of both the rational coefficients and the exact sets of scattered squares.

Run `python3 verify.py` in the directory containing this file and `verify.py`. The actual run returned:

```
PASS: 19 complete position-enumerated (q,k) profiles; 85 rational coefficients; 11992 independent greedy/descents decisions.
Examples: q=3, k=4 -> [3, 9, 17, 15, 6, 1]
          q=4, k=3 -> [4, 12, 12, 4]
```

The finite checks include all positive half-lengths for each tested \(q,k\), compare sets of distinct subsequence strings rather than embedding counts, and verify the predicted sets of maximal roots. They are not exhaustive over infinitely many parameters. A completed self-review is not an independent scientific audit, which remains unperformed. The bibliographic search is not a proof that no equivalent theorem exists.
