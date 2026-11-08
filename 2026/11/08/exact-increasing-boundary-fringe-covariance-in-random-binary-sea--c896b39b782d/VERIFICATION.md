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

# Verification of exact boundary–fringe covariance

Execute `python bst_spine_leaf_checker.py` with Python 3. The program uses only the standard library and prints `PASS: 47438 exact assertions; n<=8 permutation exhaustive, n<=300 rational recurrence` when all tests pass. It enumerates each of the \(n!\) insertion permutations for \(1\le n\le8\) and checks the exact rational covariance against a separate root-split recurrence up to \(n=300\). It tests the leftmost-path/record and ordinary-leaf/permutation-peak interpretations. Finite enumeration alone is not a proof for unbounded \(n\); the separate analytic recurrence proof is given in RESULT.md.

No independent audit has been performed.
