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

Run `python3 verify.py` from the directory containing this file. No third-party packages or network connectivity are used.

The checker enumerates all \((n-1)!\) parent-choice tuples for each \(2\le n\le8\). For each fixed subset of nonroot labels it independently calculates the parent tuples of the surviving tree under the event that all selected labels were leaves, and confirms that **all** reduced recursive-tree parent tuples appear with exactly equal frequency. It separately checks the conditional depth distributions for every earlier-leaf subset and the indexed and aggregate covariance formulas using exact fractions. It also checks the \(n/12\) leaf-count variance. The successful package replay reports `PASS: 17014 exact rational distribution/moment assertions; exhaustive through n=8.`

These computations check the finite cases only. The infinite conditional-law, sign, and asymptotic claims follow from the product-condition argument, generating-function recursion and variance recurrence in `RESULT.md`.
