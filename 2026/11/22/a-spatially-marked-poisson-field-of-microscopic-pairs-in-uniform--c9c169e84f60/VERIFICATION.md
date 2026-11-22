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

# Reproducible finite verification

In the folder containing `verify_local_pairs.py`, run:

```sh
python3 verify_local_pairs.py
```

The execution produced: `PASS: 364 finite exact checks, exhaustive permutations through n=8`.

The independent enumeration path checks all permutations on \(3\) to \(8\) labels for the signed displacement marks \((h,k,s)\) with \(1\le h,k\le3\). For five pairs of marks, it compares exact mixed second factorial moments from complete permutation enumeration to a separate construction based on partial injective assignments with probabilities \(1/(n)_v\). It additionally verifies finite mean formulas and exact lattice intersection identities for \(1\le d,r\le10\).

These finite checks do not establish the infinitely many-size Poisson limit. The proof uses a factorial-moment component bound with contribution \(O(n^{2c-v})\), so any component on at least three horizontal vertices vanishes as the sample size grows. Only fixed finite marks and fixed distance thresholds are treated. No independent review is represented by this document.
