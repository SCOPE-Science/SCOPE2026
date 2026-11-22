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

Reproduce with standard Python 3 and no dependencies:

```sh
python3 verify.py
```

The checker independently enumerates partial injections for the eight parameter pairs \((1,1),(2,1),(2,2),(3,1),(3,2),(3,3),(4,2),(5,1)\), tests the induced-graph isomorphism property, classifies extension via global-part preservation (and global part exchange in the balanced case), and compares both rank-count polynomials coefficient by coefficient with the binomial formulas. It reports `PASS` when every comparison succeeds. The delivered script was executed and returned `PASS`.

The full theorem for all \(a>b\ge1\) follows from the bipartition classification and factorization in `RESULT.md`, not from the finite enumeration. No external formal proof certification or independent audit was performed. The earliest source date, 2015-06-06, is the public first-submission date of arXiv:1506.02093, not its later publication/revision date.
